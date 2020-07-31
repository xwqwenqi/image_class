# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 上午9:46
# @Author  : Xie
# @File    : video_split_to_images.py
# @Discription : split the video to images


import cv2
import glob
import os


FRAME_PER_SECOND = 30

video_root_path = '/media/xwq/Elements/image_classification/video_data'
images_save_path = '/media/xwq/Elements/image_classification/images_data'

if not os.path.exists(images_save_path):
    os.mkdir(images_save_path)

os.chdir(video_root_path)
video_name_list = glob.glob('*.avi')

frame_index = 0
for video_name in video_name_list:
    video_abs_path = os.path.join(video_root_path, video_name)
    cap = cv2.VideoCapture(video_abs_path)
    ret, image = cap.read()
    while ret:
        ret, image = cap.read()
        frame_index += 1
        if frame_index % (7*FRAME_PER_SECOND) == 0:
            #image_name = '%06d' % frame_index
            image_name = str('%07d' % frame_index) + '.jpg'
            print (image_name)
            cv2.imwrite(os.path.join(images_save_path, image_name), image)

#print (video_name_list)
