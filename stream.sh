#!/bin/bash

# Define default values for variables
VIDEO_DEVICE="/dev/video0"
VIDEO_SIZE="640x480"
RTMP_URL="rtmp://localhost:1935/live/stream"

# Parse command-line arguments
while getopts ":d:s:r:h" opt; do
  case $opt in
    d) VIDEO_DEVICE=$OPTARG ;;
    s) VIDEO_SIZE=$OPTARG ;;
    r) RTMP_URL=$OPTARG ;;
    h)
       echo "Usage: $0 [-d device] [-s size] [-r url] [-h]"
       echo "Capture video from a USB webcam and stream it over RTMP"
       echo ""
       echo "Options:"
       echo "  -d device    Video device file (default: /dev/video0)"
       echo "  -s size      Video resolution (default: 640x480)"
       echo "  -r url       RTMP URL (default: rtmp://localhost:1935/live/stream)"
       echo "  -h           Display this help message and exit"
       exit 0
       ;;
    \?) echo "Invalid option -$OPTARG" >&2; exit 1 ;;
    :) echo "Option -$OPTARG requires an argument" >&2; exit 1 ;;
  esac
done

# Run ffmpeg with the specified parameters
ffmpeg -f v4l2 -video_size "$VIDEO_SIZE" -i "$VIDEO_DEVICE" -c:v libx264 -preset ultrafast -tune zerolatency -f flv "$RTMP_URL"
