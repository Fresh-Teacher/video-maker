from moviepy.editor import *

def create_video(audio_file, video_file, cover_photo):
    # Load the audio file
    audio_clip = AudioFileClip(audio_file)
    
    # Load the cover photo
    cover_clip = ImageClip(cover_photo)
    
    # Set duration of the video to match the duration of the audio
    duration = audio_clip.duration
    
    # Resize cover photo to match video dimensions
    cover_clip = cover_clip.resize((640, 480))
    
    # Create a video clip with the cover photo
    video_clip = CompositeVideoClip([cover_clip.set_duration(duration)])
    
    # Set the audio of the video clip to the loaded audio
    video_clip = video_clip.set_audio(audio_clip)
    
    # Write the video file
    video_clip.write_videofile(video_file, codec='libx264', audio_codec='aac', fps=24)

if __name__ == "__main__":
    audio_file = "Akamuli ka Lillie.mp3"  # Change this to your input audio file
    video_file = "Akamuli ka Lillie.mp4"  # Change this to your desired output video file
    cover_photo = "akamuli ka lillie.jpg"  # Change this to the path of your thumbnail cover photo
    create_video(audio_file, video_file, cover_photo)
