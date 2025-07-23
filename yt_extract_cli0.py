#!/usr/bin/env python3
"""
Command-line interface for YouTube video extraction
"""
import argparse
import os
import sys
from dotenv import load_dotenv

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#from mcp_youtube_extract.src.mcp_youtube_extract.youtube import get_video_info, get_video_transcript, format_video_info
from src.mcp_youtube_extract.youtube import get_video_info, get_video_transcript, format_video_info

def main():
    parser = argparse.ArgumentParser(description="Extract YouTube video information and transcript")
    parser.add_argument("video_id", help="YouTube video ID (e.g., dQw4w9WgXcQ)")
    parser.add_argument("--info-only", action="store_true", help="Get only video information, skip transcript")
    parser.add_argument("--transcript-only", action="store_true", help="Get only transcript, skip video info")
    parser.add_argument("--output", "-o", help="Output file (default: stdout)")
    
    args = parser.parse_args()
    
    # Load environment variables
    load_dotenv()
    api_key = os.getenv("YOUTUBE_API_KEY")
    
    if not api_key:
        print("Error: YOUTUBE_API_KEY not found in environment variables", file=sys.stderr)
        print("Please set it in your .env file or environment", file=sys.stderr)
        sys.exit(1)
    
    try:
        result = []
        
        if not args.transcript_only:
            # Get video information
            video_info = get_video_info(api_key, args.video_id)
            result.append("=== VIDEO INFORMATION ===")
            result.append(format_video_info(video_info))
            result.append("")
        
        if not args.info_only:
            # Get transcript
            transcript = get_video_transcript(args.video_id)
            result.append("=== TRANSCRIPT ===")
            
            if transcript and not transcript.startswith("Transcript error:") and not transcript.startswith("Could not retrieve"):
                result.append(transcript)
            else:
                result.append(f"Transcript issue: {transcript}")
        
        output = "\n".join(result)
        
        # Write output
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output)
            print(f"Output written to {args.output}")
        else:
            print(output)
            
    except Exception as e:
        print(f"Error processing video {args.video_id}: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()