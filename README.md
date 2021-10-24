# README #

Generate voices from SRT file (subtitles).

### Requirements ###

```
$ pip install --user --upgrade -r requirements.txt
```

### Usage ###

```
$ python srt-to-voice.py -f input.srt -o audio.mp3

$ ffmpeg -i video.mp4 -i audio.mp3 -c copy -map 0:v:0 -map 1:a:0 output.mp4

$ ffmpeg -i output.mp4 -preset ultrafast -vf "subtitles=input.srt:force_style='Alignment=2,FontName=Noto Sans CJK TC Medium,FontSize=24,MarginV=10'" output[burned].mp4
```

### Author ###

SHIE, Li-Yi <lyshie@tn.edu.tw>
