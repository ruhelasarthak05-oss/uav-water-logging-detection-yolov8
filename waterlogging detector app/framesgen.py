

import cv2
import os

def extract_frames_from_folder(input_folder, output_base_folder, interval_seconds=0.5):
    # Supported video extensions
    valid_extensions = ['.mp4', '.avi', '.mov', '.mkv']
    
    # Check if the input folder actually exists
    if not os.path.exists(input_folder):
        print(f"Error: The input folder '{input_folder}' does not exist.")
        return

    # Create the main output directory if it doesn't exist
    if not os.path.exists(output_base_folder):
        os.makedirs(output_base_folder)
        print(f"Created main output folder: {output_base_folder}")

    # Loop through every single file in the input folder
    for filename in os.listdir(input_folder):
        # Get the file extension to make sure we are only looking at videos
        _, ext = os.path.splitext(filename)
        if ext.lower() not in valid_extensions:
            continue # Skip non-video files
            
        video_path = os.path.join(input_folder, filename)
        video_name = os.path.splitext(filename)[0] # Get the name without the .mp4 part
        
        print(f"\nProcessing video: {filename}")
        
        # Load the video
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print(f"  Error: Could not open {filename}")
            continue

        fps = cap.get(cv2.CAP_PROP_FPS)
        
        # Safety check: if FPS is 0, the video is likely corrupted
        if fps == 0:
             print(f"  Error: Could not read FPS for {filename}. Skipping.")
             cap.release()
             continue
             
        # Calculate frame skip interval
        frame_interval = int(fps * interval_seconds)
        print(f"  Original FPS: {fps} | Extracting 1 image every {frame_interval} frames")

        frame_count = 0
        saved_count = 0

        while True:
            success, frame = cap.read()
            if not success:
                break # Video has ended

            if frame_count % frame_interval == 0:
                # Save directly to the main folder, using the video name to prevent overwriting
                out_filename = os.path.join(output_base_folder, f"{video_name}frame{saved_count:04d}.jpg")
                cv2.imwrite(out_filename, frame)
                saved_count += 1

            frame_count += 1

        cap.release()
        print(f"  Done! Saved {saved_count} images from {filename}.")

    print("\nAll videos processed successfully! All frames are in one folder.")

# ==========================================
# RUNNING THE SCRIPT
# ==========================================

# 1. Name of the folder containing all your raw drone videos
input_directory = r'C:\Users\SARTHAK\OneDrive\Documents\SELF PROJECTS\yolo\videos for frame generation'

# 2. Name of the SINGLE folder where all extracted frames will be saved
output_directory = r'C:\Users\SARTHAK\OneDrive\Documents\SELF PROJECTS\yolo\testing images'

# 3. Execute the function
extract_frames_from_folder(input_directory, output_directory, interval_seconds=0.5)