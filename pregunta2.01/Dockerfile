# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install ffmpeg (required by yt-dlp for video processing)
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies - upgrade pip and install specific yt-dlp version
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir yt-dlp==2025.10.14

# Copy the application
COPY lab06video.py .

# Run the script
CMD ["python", "lab06video.py"]
