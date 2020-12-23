#import the necessary packages
import mahotas
import cv2
class ZernikeMoments:
	def __init__(self, radius):
		# store the size of the radius that will be
		# used when computing moments
		self.radius = radius
	def describe(self, image):
		# return the Zernike moments for the image
		image = cv2.imread(image)
		image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		#to ensure  edge of image does not touch alphabet
		image = cv2.copyMakeBorder(image, 15, 15, 15, 15,cv2.BORDER_CONSTANT, value = 255)

		thresh = cv2.bitwise_not(image)
		return mahotas.features.zernike_moments(thresh, self.radius)
