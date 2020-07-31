#!/usr/bin/env bash

modelName="VGG16,VGG19,InceptionV3,Xception,MobileNet,AlexNet,LeNet,ZF_Net,ResNet18,ResNet34,ResNet50,ResNet101,ResNet152"
className="city_road_day,garden_road,highway_day,parking_area,toll_gate,under_highway_day"

model=(${modelName//,/ })
clses=(${className//,/ })

for mdl in ${model[@]}
do
    for cls in ${clses[@]}
    do
        echo python predict.py $mdl $cls
        python predict.py $mdl $cls
    done

done