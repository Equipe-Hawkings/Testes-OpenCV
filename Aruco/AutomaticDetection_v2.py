''' Detecção Automática de um aruco, sem definir previamente o tipo de tag (4x4, 5x5 ou 6x6 ...)
	Detecção feita analisando uma transmissão de vídeo via webcam
	Essa versao 2 do "AutomaticDetection", busca uma detecção contínua do aruco sem pausas '''


#!/usr/bin/env python3	
from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import sys

# define names of each possible ArUco tag OpenCV supports
ARUCO_DICT = {
	"DICT_4X4_50": cv2.aruco.DICT_4X4_50,
	"DICT_4X4_100": cv2.aruco.DICT_4X4_100,
	"DICT_4X4_250": cv2.aruco.DICT_4X4_250,
	"DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
	"DICT_5X5_50": cv2.aruco.DICT_5X5_50,
	"DICT_5X5_100": cv2.aruco.DICT_5X5_100,
	"DICT_5X5_250": cv2.aruco.DICT_5X5_250,
	"DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
	"DICT_6X6_50": cv2.aruco.DICT_6X6_50,
	"DICT_6X6_100": cv2.aruco.DICT_6X6_100,
	"DICT_6X6_250": cv2.aruco.DICT_6X6_250,
	"DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
	"DICT_7X7_50": cv2.aruco.DICT_7X7_50,
	"DICT_7X7_100": cv2.aruco.DICT_7X7_100,
	"DICT_7X7_250": cv2.aruco.DICT_7X7_250,
	"DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
	"DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
	"DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
	"DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
	"DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
	"DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
}

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)
# loop over the frames from the video stream
# loop over the frames from the video stream
while 1:
	for (arucoName, arucoDict) in ARUCO_DICT.items():
		frame = vs.read()
		frame = imutils.resize(frame, width=1000)
		# load the ArUCo dictionary, grab the ArUCo parameters, and
		# attempt to detect the markers for the current dictionary
		arucoDict = cv2.aruco.Dictionary_get(arucoDict)
		arucoParams = cv2.aruco.DetectorParameters_create()
		(corners, ids, rejected) = cv2.aruco.detectMarkers(frame,
		arucoDict, parameters=arucoParams)
		# verify *at least* one ArUco marker was detected
		if len(corners) > 0:
			while 1:
				frame = vs.read()
				frame = imutils.resize(frame, width=1000)
				(corners, ids, rejected) = cv2.aruco.detectMarkers(frame,
				arucoDict, parameters=arucoParams)
				# flatten the ArUco IDs list
				if len(corners) > 0:
					ids = ids.flatten()
					# loop over the detected ArUCo corners
					for (markerCorner, markerID) in zip(corners, ids):
						# extract the marker corners (which are always returned
						# in top-left, top-right, bottom-right, and bottom-left
						# order)
						corners = markerCorner.reshape((4, 2))
						(topLeft, topRight, bottomRight, bottomLeft) = corners
						# convert each of the (x, y)-coordinate pairs to integers
						topRight = (int(topRight[0]), int(topRight[1]))
						bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
						bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
						topLeft = (int(topLeft[0]), int(topLeft[1]))

					# draw the bounding box of the ArUCo detection
						cv2.line(frame, topLeft, topRight, (0, 255, 0), 2)
						cv2.line(frame, topRight, bottomRight, (0, 255, 0), 2)
						cv2.line(frame, bottomRight, bottomLeft, (0, 255, 0), 2)
						cv2.line(frame, bottomLeft, topLeft, (0, 255, 0), 2)
						# compute and draw the center (x, y)-coordinates of the
						# ArUco marker
						cX = int((topLeft[0] + bottomRight[0]) / 2.0)
						cY = int((topLeft[1] + bottomRight[1]) / 2.0)
						cv2.circle(frame, (cX, cY), 4, (0, 0, 255), -1)
						# draw the ArUco marker ID on the frame
						cv2.putText(frame, str(markerID),
							(topLeft[0], topLeft[1] - 15),
							cv2.FONT_HERSHEY_SIMPLEX,
							0.5, (0, 255, 0), 2)
				# show the output frame
				cv2.imshow("Frame", frame)
				key = cv2.waitKey(1) & 0xFF
				# if the `q` key was pressed, break from the loop
				if key == ord("q"):
					break
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF
		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break 
	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break 
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
