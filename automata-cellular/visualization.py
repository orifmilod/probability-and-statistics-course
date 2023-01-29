import cv2
import numpy


class Visualization:
    def draw(self, pixels):

        image = numpy.array([[ [0,0,255] if pixels[i][j] else [0,0,0] for i in range(0, len(pixels[j]))] for j in range(0, len(pixels))], numpy.uint8)

        resized = cv2.resize(image, (1000,1000), interpolation = cv2.INTER_AREA)
        cv2.imshow("Automata Cellular", resized)
        cv2.waitKey()



