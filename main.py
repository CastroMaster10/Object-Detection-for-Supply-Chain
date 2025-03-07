from utils import read_video,save_video
from trackers import Tracker

def main():
    #Read video
    video_frames= read_video('input_videos/bottles.mp4')
    
    #Tracker
    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracks(video_frames)

    #Save video
    save_video(video_frames,"outputs/output_bottles.avi")

if __name__ == "__main__":
    main()