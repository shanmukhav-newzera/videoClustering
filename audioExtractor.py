import moviepy.editor

video = moviepy.editor.VideoFileClip("kapil2.mp4")

video.audio.write_audiofile("kapil2Audio.wav")