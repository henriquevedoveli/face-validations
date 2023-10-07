from src.main import VideoProcessor

if __name__ == "__main__":
    video_processor = VideoProcessor(render_keypoints=False)
    video_processor.run()