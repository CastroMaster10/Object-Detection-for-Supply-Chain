from ultralytics import YOLO

model = YOLO('yolov8x.pt')

results = model.predict('football.mp4',save=True)
boxes = results[0]
print(boxes)
print("-----------------------------------------------")
for box in boxes.boxes:
    print(box)