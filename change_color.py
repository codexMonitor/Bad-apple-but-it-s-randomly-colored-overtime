import random, cv2, glob, os

def luminance(color):
    return 0.299 * color[0] + 0.587 * color[1] + 0.114 * color[2]

def random_two_colors():
    color1 = [random.randint(0, 255) for _ in range(3)]
    color2 = [random.randint(0, 255) for _ in range(3)]

    lu1 = luminance(color1)
    lu2 = luminance(color2)

    while abs(lu1 - lu2) <= 100:
        color2 = [random.randint(0, 255) for _ in range(3)]
        lu2 = luminance(color2)
    
    return tuple(color1), tuple(color2)

output_folder = "colored_frames"
os.makedirs(output_folder, exist_ok=True)
input_folder = "extract_frames"
extract_frames = sorted(glob.glob(os.path.join(input_folder, "*.png")))

frame_count = 0

for i, frame_file in enumerate(extract_frames):
    frame = cv2.imread(frame_file, cv2.IMREAD_GRAYSCALE)

    frame = cv2.resize(frame, (480, 360), interpolation=cv2.INTER_LINEAR)

    if i % 100 == 0:
        color1, color2 = random_two_colors()
        
    colored_frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    colored_frame[frame < 128] = color1
    colored_frame[frame >= 128] = color2

    frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.png")
    cv2.imwrite(frame_filename, colored_frame)

    frame_count += 1

print(f"Extracted {frame_count} frames.")