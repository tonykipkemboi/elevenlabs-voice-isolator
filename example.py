#!/usr/bin/env python3
"""
Example script demonstrating how to use the voice_isolator package.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

from voice_isolator.processor import process_video, batch_process_videos

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
api_key = os.environ.get("ELEVENLABS_API_KEY")
if not api_key:
    raise ValueError(
        "ElevenLabs API key not found. Set ELEVENLABS_API_KEY environment variable."
    )


def example_single_video():
    """Example of processing a single video."""
    # Replace with your video file path
    video_path = "path/to/your/video.mp4"
    output_path = "path/to/output/video_clean.mp4"
    
    # Process the video
    processed_video = process_video(
        video_path=video_path,
        output_path=output_path,
        api_key=api_key,
        keep_temp_files=True  # Set to True to keep temporary files
    )
    
    print(f"Processed video saved to: {processed_video}")


def example_batch_processing():
    """Example of batch processing videos in a directory."""
    # Replace with your videos directory path
    videos_dir = "path/to/videos"
    output_dir = "path/to/output"
    
    # Process all videos in the directory
    processed_videos = batch_process_videos(
        input_dir=videos_dir,
        output_dir=output_dir,
        api_key=api_key,
        keep_temp_files=True  # Set to True to keep temporary files
    )
    
    print(f"Processed {len(processed_videos)} videos:")
    for video in processed_videos:
        print(f"  - {video}")


if __name__ == "__main__":
    # Uncomment the example you want to run
    # example_single_video()
    # example_batch_processing()
    
    print("Please edit this file to specify your video path and uncomment an example to run.")
