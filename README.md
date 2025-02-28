# Bad-apple-but-it-s-randomly-colored-overtime

Hi, there are Python scripts that I used to create colored Bad Apple video. 
I'd like to show you how to make things work (If you have experience, you can ignore this text).


Tutorials (To be clear, I don't know if this code works on Linux or MacOS so I will assume that you use Windows):
1. Remember to download Python, there are a lot of tutorials and articles about that.
2. Install dependencies, you just need to write this command in Terminal:
      pip install -r requirements.txt
3. Run this command (this extract audio from video): ffmpeg -i bad_apple.mp4 -q:a 0 -map a audio.wav
4. Run this command (this will extract frames into extract_frames): python extract.py
5. Run this command (this will color frames into colored_frames): python change_color.py
6. Run this command (this plays video): python play.py
7. Enjoy!


When it's done:
![image](https://github.com/user-attachments/assets/923f46e4-1a39-4b8e-ab12-60ec0bc7e498)



Details of each file/folder (Just extra information):
- play.py: This code runs the colored video.
- extract.py: I used this code to extract frames of Bad Apple into extract_frames folder.
- change_color.py: I used this code to change the colors of each frame and get them into colored_frames folder.
- export_video.py: Well, it's just a script I used to export video. The video named bad_apple_colored has no sound.
=> Finally, you can make videos on your own. Just delete the colored_frames and run change_color.py. In case you delete extract_frames, just run extract.py, remember to keep the original video in here.


If there is something new, I will update this repo. 
