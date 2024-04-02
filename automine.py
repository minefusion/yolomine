from ultralytics.data.converter import convert_coco
cls91to80 = False
annotations_dir = "/home/zhanjun/PHD/datasets/automine-2d/images/annotations"
convert_coco(labels_dir=annotations_dir,use_segments=False,cls91to80=False)

#False
# multi
#WARNING train2017/003210.png: ignoring corrupt image/label: negative label values [         -1]

#yolo train data=./automine-2d.yaml model=yolov8n.yaml epochs=1 lr0=0.01
# yolo explorer
# yolo settings reset