#This file will have the utilities to read and save it
import cv2

def read_video(video_path):

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Video could not be opened.")
    
    frames = []
    while True:
        ret,frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    

    return frames


def save_video(frames,output_video_path):

    frame_rate = 20
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path,fourcc,frame_rate,(frames[0].shape[1],frames[0].shape[0]))
    for frame in frames:
        out.write(frame) #Llenamos con frames el Writer

    out.release()
    


    