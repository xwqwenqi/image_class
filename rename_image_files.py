# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 下午5:57
# @Author  : Xie
# @File    : rename_image_files.py
# @Discription : to rename the image files


import os
import glob

image_dirs_root_path = '/media/xwq/Elements/image_classification/images/toll_gate'
image_index = 0

for image_dirs_root_path, image_dirs_list, files in os.walk(image_dirs_root_path):
    for image_dir_name in image_dirs_list:
        image_abs_dir = os.path.join(image_dirs_root_path, image_dir_name)

        os.chdir(image_abs_dir)

        print (image_abs_dir)
        image_name_list = glob.glob('*.jpg')
        #print (image_name_list)
        for image_name in image_name_list:
            image_abs_path = os.path.join(image_abs_dir, image_name)
            print (image_abs_path)
            image_index_str = str('%05d' % image_index)
            image_new_name = 'IMG_' + image_index_str + '.jpg'
            image_new_abs_path = os.path.join(image_abs_dir, image_new_name)

            print (image_new_abs_path)

            os.rename(image_abs_path, image_new_abs_path)

            image_index += 1


