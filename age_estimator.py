import sys
from crop_faces import crop_face
from estimate_age import estimate_age

# Take the image file name from the command line
#~ file_name = sys.argv[1]

def age_estimator(file_name):
	ages = []
	
	detected_faces = crop_face(file_name)
	#~ detected_ages = estimate_age(detected_faces)

	for face in detected_faces:
		ages.append(estimate_age(face))
		#~ print (str(face) + "->" + str(estimate_age(face)))
		
	return ages

#~ age_estimator(file_name)

#ernie 17016723
