import cv2, glob, os

input_folder = "colored_frames"
frame_files = sorted(glob.glob(os.path.join(input_folder, "*.png")))
video = "bad_apple.mp4"

frame_sample = cv2.imread(frame_files[0], cv2.IMREAD_GRAYSCALE)
frame_height, frame_width = frame_sample.shape
cap = cv2.VideoCapture(video)
fps = cap.get(cv2.CAP_PROP_FPS)  
cap.release()

output_filename = "bad_apple_colored.mp4"
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))

for frame_file in frame_files:
    frame = cv2.imread(frame_file)

    cv2.imshow("Bad Apple", frame)
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
cv2.destroyAllWindows()

print(f"Video has saved as {output_filename}")