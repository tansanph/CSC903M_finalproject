import sys
import dlib
from skimage import io
from PIL import Image

def crop_face(image_file):
	
	#filenames of saved cropped faces
	faces_filenames = []

	# Create a HOG face detector using the built-in dlib class
	face_detector = dlib.get_frontal_face_detector()

	# Load the image into an array
	image = io.imread(image_file)

	# Run the HOG face detector on the image data.
	# The result will be the bounding boxes of the faces in our image.
	detected_faces = face_detector(image, 1)

	#print("I found {} faces in the file {}".format(len(detected_faces), image_file))

	#import image into PIL
	im = Image.open(image_file)

	# Loop through each face we found in the image
	for i, face_rect in enumerate(detected_faces):

		# Detected faces are returned as an object with the coordinates 
		# of the top, left, right and bottom edges
		#print("- Face #{} found at Left: {} Top: {} Right: {} Bottom: {}".format(i, face_rect.left(), face_rect.top(), face_rect.right(), face_rect.bottom()))
		
		#expand faces boundaries
		f_height = face_rect.bottom() - face_rect.top()
		f_width = face_rect.right() - face_rect.left()
		b_lr = f_width*0.4
		b_top = f_height*0.7
		b_bottom = f_height*0.4
		
		#crop image into detected faces boundaries
		cim = im.crop((face_rect.left()-b_lr, face_rect.top()-b_top, face_rect.right()+b_lr, face_rect.bottom()+b_bottom))
		
		#save the cropped face to file
		cim.save("face" + str(i) + ".jpg")
		
		faces_filenames.append("face" + str(i) + ".jpg")
		
	return faces_filenames
