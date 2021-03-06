import os, sys
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def estimate_age(face):

	# Read in the image_data
	image_data = tf.gfile.FastGFile(face, 'rb').read()

	# Loads label file, strips off carriage return
	label_lines = [line.rstrip() for line 
					   in tf.gfile.GFile("retrained_labels.txt")]

	# Unpersists graph from file
	with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
		graph_def = tf.GraphDef()
		graph_def.ParseFromString(f.read())
		tf.import_graph_def(graph_def, name='')

	with tf.Session() as sess:
		# Feed the image_data as input to the graph and get first prediction
		softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
		
		predictions = sess.run(softmax_tensor, \
				 {'DecodeJpeg/contents:0': image_data})
		
		# Sort to show labels of first prediction in order of confidence
		top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
		
		temp = 0
		predict_node_id = 0
		
		for node_id in top_k:

			score = predictions[0][node_id]        
			
			if score > temp:
				temp = score
				predict_node_id = node_id
			
	return label_lines[predict_node_id]
