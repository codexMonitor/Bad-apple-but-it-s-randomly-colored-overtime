import cv2, os

video = "bad_apple.mp4"
cap = cv2.VideoCapture(video)

output_folder = "extract_frames"
os.makedirs(output_folder, exist_ok=True)

frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.png")
    cv2.imwrite(frame_filename, frame)

    frame_count += 1

cap.release()
print(f"Extracted {frame_count} frames.")