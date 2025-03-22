#!/usr/bin/env python3
"""
Voice Isolator CLI

Command-line interface for the voice isolator package.
"""

import os
import argparse
import logging
from pathlib import Path

from voice_isolator.processor import process_video, batch_process_videos
from voice_isolator.utils.logger import setup_logger

# Set up logger
logger = setup_logger("voice_isolator.cli")


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Process videos with ElevenLabs voice isolation"
    )
    
    # Add arguments
    parser.add_argument(
        "input",
        help="Input video file or directory containing video files"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file or directory for processed videos"
    )
    parser.add_argument(
        "--batch",
        action="store_true",
        help="Process all video files in the input directory"
    )
    parser.add_argument(
        "--temp-dir",
        help="Directory for temporary files (only used in batch mode)"
    )
    parser.add_argument(
        "--keep-temp",
        action="store_true",
        help="Keep temporary files"
    )
    parser.add_argument(
        "--api-key",
        help="ElevenLabs API key (will use ELEVENLABS_API_KEY env var if not provided)"
    )
    parser.add_argument(
        "--video-codec",
        default="copy",
        help="Video codec to use (default: copy - no re-encoding)"
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite output files if they exist"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    
    args = parser.parse_args()
    
    # Set logging level
    if args.verbose:
        logging.getLogger("voice_isolator").setLevel(logging.DEBUG)
    
    # Get API key
    api_key = args.api_key or os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        parser.error(
            "ElevenLabs API key not provided. Set ELEVENLABS_API_KEY environment variable or use --api-key."
        )
    
    try:
        # Batch processing mode
        if args.batch:
            input_path = Path(args.input)
            if not input_path.is_dir():
                parser.error(f"Input path must be a directory in batch mode: {args.input}")
            
            output_files = batch_process_videos(
                input_dir=input_path,
                output_dir=args.output,
                temp_dir=args.temp_dir,
                api_key=api_key,
                video_codec=args.video_codec,
                keep_temp_files=args.keep_temp,
                overwrite=args.overwrite
            )
            
            if output_files:
                logger.info(f"Successfully processed {len(output_files)} video files")
                for output_file in output_files:
                    logger.info(f"  - {output_file}")
        
        # Single file processing mode
        else:
            input_path = Path(args.input)
            if not input_path.is_file():
                parser.error(f"Input path must be a file in single file mode: {args.input}")
            
            output_file = process_video(
                video_path=input_path,
                output_path=args.output,
                keep_temp_files=args.keep_temp,
                api_key=api_key,
                video_codec=args.video_codec,
                overwrite=args.overwrite
            )
            
            logger.info(f"Successfully processed video: {output_file}")
    
    except Exception as e:
        logger.error(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
