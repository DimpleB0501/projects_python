import subprocess as sp
import numpy
import cv2

FFMPEG_BIN = "ffmpeg" 
command = [ FFMPEG_BIN,
			'-i', 'tcp://192.168.2.2:2222',
		#	'-f', 'image2pipe',
			'-f', 'rawvideo',
			'-tune', 'zerolatency',
			'-fflags', 'nobuffer',
			'-preset','ultrafast',
			'-pix_fmt', 'rgb24',
			'-vcodec', 'rawvideo', '-']
pipe = sp.Popen(command, stdout = sp.PIPE, bufsize=10**8)
 

# read 1 frame
width = 640
height = 480 
 
while(True):
	# Capture frame-by-frame
	raw_image = pipe.stdout.read(width*height*3) #takes 0.15 secs per call.  
	# transform the byte read into a numpy array
	image =  numpy.fromstring(raw_image, dtype='uint8')
	image = image.reshape((height,width,3))
	# throw away the data in the pipe's buffer.
	pipe.stdout.flush()
	im = cv2.cvtColor (image,cv2.COLOR_RGB2BGR) #In BGR format
	#im = cv2.cvtColor (image,cv2.COLOR_RGB2GRAY) #In gray scale
	# Display the resulting frame
	cv2.imshow('frame',im)
	if cv2.waitKey(1) & 0xFF == ord('q'): #takes about 0.05 secs per call. Work out to 5 fps.
		break
 
cv2.destroyAllWindows()
