import json
from qiskit_ibm_runtime import QiskitRuntimeService

credentials_file = open("credentials.json")
credentails = json.load(credentials_file)
credentials_file.close()

# Save an IBM Quantum account.
QiskitRuntimeService.save_account(channel=credentails["channel"], token=credentails["token"])

