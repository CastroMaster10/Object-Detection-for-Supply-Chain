from ultralytics import YOLO

model = YOLO('models/best.pt')

results = model.predict('input_videos/bottles.mp4',save=True)
boxes = results[0]
print(boxes)
print("-----------------------------------------------")
for box in boxes.boxes:
    print(box)