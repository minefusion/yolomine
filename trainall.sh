
sleep 5
yolo train data=automine-2d.yaml model=rtdetr-l.pt imgsz=1024 batch=2 epochs=30

yolo val data=automine-2d.yaml model=automine-rtdetr-l.pt imgsz=1024 


exit

sleep 5

yolo train data=automine-2d.yaml model=yolov8s.pt imgsz=1024 batch=4 epochs=30


sleep 5

yolo train data=automine-2d.yaml model=yolov8l.pt imgsz=1024 batch=4 epochs=30


sleep 5

yolo train data=automine-2d.yaml model=yolov9e.pt imgsz=1024 batch=2 epochs=30


sleep 5

yolo train data=automine-2d.yaml model=yolov9c.pt  batch=8 epochs=30


sleep 5

#yolo train data=automine-2d.yaml model=yolov8s-rtdetr.pt  imgsz=1024 batch=4

