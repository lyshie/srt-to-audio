ffmpeg -i video.mp4 -i audio.mp3 -c copy -map 0:v:0 -map 1:a:0 output.mp4
#ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac output.mp4
