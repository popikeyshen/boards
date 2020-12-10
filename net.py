

from ctypes import *
import math
import random
import os
import cv2
import numpy as np
import time
import darknet


class NeuralNet:
    def __init__(self, ):
        #configPath2 = "./608.cfg"
        #weightPath2 = "./608.backup"

        configPath2 = "/home/popikeyshen/yolo_run/tiny_likes.cfg"
        weightPath2 = "/home/popikeyshen/yolo_run/tiny_likes_last.weights"

        metaPath2 = "./darknet.data"
        self.netMain2 = darknet.load_net_custom(configPath2.encode("ascii"), weightPath2.encode("ascii"), 0, 1)  # batch size = 1
        self.metaMain2 = darknet.load_meta(metaPath2.encode("ascii"))
        print("Starting the YOLO loop...")
        self.darknet_image2 = darknet.make_image(darknet.network_width(self.netMain2),darknet.network_height(self.netMain2),3)

    def detect(self, frame_read):
        frame_read = cv2.cvtColor(frame_read, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize(frame_read, (darknet.network_width(self.netMain2),  darknet.network_height(self.netMain2)), interpolation=cv2.INTER_LINEAR)
        darknet.copy_image_from_bytes(self.darknet_image2,frame_resized.tobytes())
        detections = darknet.detect_image(self.netMain2, self.metaMain2, self.darknet_image2, thresh=0.5)
        return detections, frame_resized

    def convertBack(self, x, y, w, h):
        xmin = int(round(x - (w / 2)))
        xmax = int(round(x + (w / 2)))
        ymin = int(round(y - (h / 2)))
        ymax = int(round(y + (h / 2)))
        return xmin, ymin, xmax, ymax

    def cvDrawBoxes(self, detections, img):
        for detection in detections:
            x, y, w, h = detection[2][0], \
                detection[2][1], \
                detection[2][2], \
                detection[2][3]

            xmin, ymin, xmax, ymax = self.convertBack(float(x), float(y), float(w), float(h))
            pt1 = (xmin, ymin)
            pt2 = (xmax, ymax)
            cv2.rectangle(img, pt1, pt2, (0, 255, 0), 1)
            cv2.putText(img, detection[0].decode() + " [" + str(round(detection[1] * 100, 2)) + "]",
                        (pt1[0], pt1[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        [0, 255, 0], 2)
        return img

    def show(self, detections, frame_read):
        image = self.cvDrawBoxes(detections, frame_read)  # ,f)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cv2.imshow('stage_end', image)
        cv2.waitKey(1)


class Cameras:
    def __init__(self, ):
        #self.cap1 = cv2.VideoCapture("")
        #self.cap2 = cv2.VideoCapture("")
        self.cap3 = cv2.VideoCapture(0)

        self.frames = 0

    def get_multiple(self, ):
        self.frames += 1
        cam_id = 0
        if frames % 2 == 0:
            ret, frame_read = self.cap1.read()
            cam_id = 2
        else:
            ret, frame_read = self.cap2.read()
            cam_id = 1
        return frame_read, cam_id

    def get_one(self,):
        ret, frame_read = self.cap3.read()
        cam_id = 3
        return frame_read, cam_id



def run_test():
    # init the network
    N = NeuralNet()
    # init the cameras
    C = Cameras()

    while True:
        # emulate multiple camera feed
        frame_read, cam_id = C.get_one()

        # block for testing x module #
        ##########################################

    

        ##########################################

        detections,frame_resized  = N.detect(frame_read)
        N.show(detections, frame_resized)


if __name__ == "__main__":
    run_test()





