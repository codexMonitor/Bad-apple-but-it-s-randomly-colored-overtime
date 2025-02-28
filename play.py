import cv2, os, pygame, glob, threading, time

frames_folder = "colored_frames"
audio_path = "audio.wav"
video = "bad_apple.mp4"

frame_files = sorted(glob.glob(os.path.join(frames_folder, "*.png")))

cap = cv2.VideoCapture(video)
fps = cap.get(cv2.CAP_PROP_FPS)  
cap.release()

frame_time = 1.0 / fps

pygame.mixer.init()
pygame.mixer.music.load(audio_path)

def play_audio():
    pygame.mixer.music.play()

audio_thread = threading.Thread(target=play_audio)
audio_thread.start()

start_time = time.perf_counter()
for i, frame_file in enumerate(frame_files):
    frame = cv2.imread(frame_file)
    if frame is None:
        continue

    cv2.imshow("Bad Apple but it's randomly colored overtime", frame)
    
    elapsed_time = time.perf_counter() - start_time
    expected_time = (i + 1) * frame_time
    delay = max(0, expected_time - elapsed_time)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(delay) 

cv2.destroyAllWindows()
pygame.mixer.music.stop()
