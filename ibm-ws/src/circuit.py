import numpy as np
import matplotlib.pyplot as plt


from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.circuit.library import QFT
from qiskit.circuit import Parameter
from qiskit.tools.visualization import plot_histogram

from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime import Sampler, Session


def create_qpe_circuit(theta, num_qubits):
    '''Creates a QPE circuit given theta and num_qubits.'''

    # Step 1: Create a circuit with two quantum registers and one classical register.
    first = QuantumRegister(size=num_qubits, name='first')  # the first register for phase estimation
    second = QuantumRegister(size=1, name='second')  # the second register for storing eigenvector |psi>
    classical = ClassicalRegister(size=num_qubits, name='readout') # classical register for readout
    qpe_circuit = QuantumCircuit(first, second, classical)

    # Step 2: Initialize the qubits.
    # All qubits are initialized in |0> by default, no extra code is needed to initialize the first register.
    qpe_circuit.x(second)  # Initialize the second register with state |psi>, which is |1> in this example.

    # Step 3: Create superposition in the first register.
    qpe_circuit.barrier()  # Add barriers to separate each step of the algorithm for better visualization.
    qpe_circuit.h(first)

    # Step 4: Apply a controlled-U^(2^j) black box.
    qpe_circuit.barrier()
    for j in range(num_qubits):
        qpe_circuit.cp(theta*2*np.pi*(2**j), j, num_qubits)  # Theta doesn't contain the 2 pi factor.

    # Step 5: Apply an inverse QFT to the first register.
    qpe_circuit.barrier()
    qpe_circuit.compose(QFT(num_qubits, inverse=True), inplace=True)

    # Step 6: Measure the first register.
    qpe_circuit.barrier()
    qpe_circuit.measure(first, classical)

    return qpe_circuit

num_qubits = 4
theta = Parameter('theta')  # Create a parameter `theta` whose values can be assigned later.
qpe_circuit_parameterized = create_qpe_circuit(theta, num_qubits) # Create a QPE circuit with fixed theta=1/2.
qpe_circuit_parameterized.draw('mpl', filename="circuit.png")

number_of_phases = 21
phases = np.linspace(0, 2, number_of_phases)
individual_phases = [[ph] for ph in phases]  # Phases need to be expressed as a list of lists.

service = QiskitRuntimeService()
backend = "ibmq_qasm_simulator"  # use the simulator

with Session(service=service, backend=backend):
    results = Sampler().run(
        [qpe_circuit_parameterized]*len(individual_phases),
        parameter_values=individual_phases
    ).result()


idx = 6
plot_histogram(results.quasi_dists[idx].binary_probabilities(), legend=[f'$\\theta$={phases[idx]:.3f}'], filename="histogram.png")

def most_likely_bitstring(results_dict):
    '''Finds the most likely outcome bitstring from a result dictionary.'''
    return max(results_dict, key=results_dict.get)

def find_neighbors(bitstring):
    '''Finds the neighbors of a bitstring.

    Example:
        For bitstring '1010', this function returns ('1001', '1011')
    '''
    if bitstring == len(bitstring)*'0':
        neighbor_left = len(bitstring)*'1'
    else:
        neighbor_left = format((int(bitstring,2)-1), '0%sb'%len(bitstring))

    if bitstring == len(bitstring)*'1':
        neighbor_right = len(bitstring)*'0'
    else:
        neighbor_right = format((int(bitstring,2)+1), '0%sb'%len(bitstring))

    return (neighbor_left, neighbor_right)

def estimate_phase(results_dict):
    '''Estimates the phase from a result dictionary of a QPE circuit.'''

    # Find the most likely outcome bitstring N1 and its neighbors.
    num_1_key = most_likely_bitstring(results_dict)
    neighbor_left, neighbor_right = find_neighbors(num_1_key)

    # Get probabilities of N1 and its neighbors.
    num_1_prob = results_dict.get(num_1_key)
    neighbor_left_prob = results_dict.get(neighbor_left)
    neighbor_right_prob = results_dict.get(neighbor_right)

    # Find the second most likely outcome N2 and its probability P2 among the neighbors.
    if neighbor_left_prob is None:
        # neighbor_left doesn't exist
        if neighbor_right_prob is None:
            # both neighbors don't exist, N2 is N1
            num_2_key = num_1_key
            num_2_prob = num_1_prob
        else:
            # If only neighbor_left doesn't exist, N2 is neighbor_right.
            num_2_key = neighbor_right
            num_2_prob = neighbor_right_prob
    elif neighbor_right_prob is None:
        # If only neighbor_right doesn't exist, N2 is neighbor_left.
        num_2_key = neighbor_left
        num_2_prob = neighbor_left_prob
    elif neighbor_left_prob > neighbor_right_prob:
        # Both neighbors exist and neighbor_left has higher probability, so N2 is neighbor_left.
        num_2_key = neighbor_left
        num_2_prob = neighbor_left_prob
    else:
        # Both neighbors exist and neighbor_right has higher probability, so N2 is neighor_right.
        num_2_key = neighbor_right
        num_2_prob = neighbor_right_prob

    # Calculate the estimated phases for N1 and N2.
    num_qubits = len(num_1_key)
    num_1_phase = (int(num_1_key, 2) / 2**num_qubits)
    num_2_phase = (int(num_2_key, 2) / 2**num_qubits)

    # Calculate the weighted average phase from N1 and N2.
    phase_estimated = (num_1_phase * num_1_prob + num_2_phase * num_2_prob) / (num_1_prob + num_2_prob)

    return phase_estimated

qpe_solutions = []
for idx, result_dict in enumerate(results.quasi_dists):
    qpe_solutions.append(estimate_phase(result_dict.binary_probabilities()))

ideal_solutions = np.append(
    phases[:(number_of_phases-1)//2],  # first period
    np.subtract(phases[(number_of_phases-1)//2:-1], 1)  # second period
)
ideal_solutions = np.append(ideal_solutions, np.subtract(phases[-1], 2))  # starting point of the third period

fig = plt.figure(figsize=(10, 6))
plt.plot(phases, ideal_solutions, '--', label='Ideal solutions')
plt.plot(phases, qpe_solutions, 'o', label='QPE solutions')

plt.title('Quantum Phase Estimation Algorithm')
plt.xlabel('Input Phase')
plt.ylabel('Output Phase')
plt.legend()

plt.savefig('plot.png')

