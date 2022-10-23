# -*- coding: utf-8 -*-
from __future__ import division
import os
import xml.etree.ElementTree as ET
import cv2
import numpy as np
import random

from shapely.geometry import Polygon


def read_xml(ImgPath=r'/datasets/before', AnnoPath=r'datasets/JPEGImages', Savepath=r'/datasets/SegmentationClass'):
    # if not os.path.isdir(Savepath):
    #     os.makedirs(Savepath)

    imagelist = os.listdir(AnnoPath)

    points_list = []

    for image in imagelist:
        image_pre, ext = os.path.splitext(image)
        imgfile = ImgPath + '/' + image_pre + '.jpg'
        xmlfile = AnnoPath + '/' + image_pre + '.xml'
        im = cv2.imread(imgfile)

        etree = ET.parse(xmlfile)
        root = etree.getroot()
        box = []
        for obj in root.iter('object'):
            s= obj.find('polygon')
            points=[x.text for x in obj.find('polygon')]
            print(s)
            i=0
            one_segm_points_list = []
            while i < len(points):
                x=int(float(points[i]))
                y=int(float(points[i+1]))
                i=i+2
                one_segm_points_list.append([x, y])
            pts = np.array(one_segm_points_list, np.int32)
            #
            # r = random.randint(0, 255)
            #
            # g = random.randint(0, 255)
            #
            # b = random.randint(0, 255)
            #
            # im = np.zeros([im.shape[0], im.shape[1], 3], np.uint8)

            # 如果我没有记错的话原本代码生成的标签应该是单通道，因为只有一类，所以标记为1
            r = 1
            # g = random.randint(0, 255)
            # b = random.randint(0, 255)
            im = np.zeros([im.shape[0], im.shape[1], 1], np.uint8)

            print('pts = ', pts)

            # cv2.fillPoly(im, [pts], (b, g, r))
            cv2.fillPoly(im, [pts], r)
        path = Savepath + '/' + image_pre + '.jpg'

        cv2.imwrite(path, im)


read_xml()

