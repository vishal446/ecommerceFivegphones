import face_recognition
import cv2
import numpy as np 
import csv
import os
from datetime import datetime

video_capture=cv2.VideoCapture(0)

jobs_image=face_recognition.load_image_file("")
jobs_encoding=face_recognition.face_encoding(jobs_image)[0]

ratan_tata_image=face_recognition.load_image_file("")
ratan_tata_encoding=face_recognition.face_encoding(ratan_tata_image)[0]

tesla_image=face_recognition.load_image_file("")
tesla_encoding=face_recognition.face_encoding(tesla_image)[0]
