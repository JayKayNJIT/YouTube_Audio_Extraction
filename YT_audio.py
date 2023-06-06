import pytube
import os

LOSSLESS_FORMATS = ['wav', 'flac', 'aiff', 'alac']

def extract_audio(url):
    try:
        video = pytube.YouTube(url)
        audio_stream = video.streams.filter(only_audio=True).order_by('abr').desc().first()

        if audio_stream:
            audio_extension = audio_stream.subtype
            if audio_extension in LOSSLESS_FORMATS:
                # Download audio using pytube
                audio_file = audio_stream.download()

                # Rename audio file to desired output name
                output_file = 'output.' + audio_extension
                os.rename(audio_file, output_file)

                print('Audio extraction completed.')
            else:
                print('No suitable lossless audio format found.')
        else:
            print('No suitable audio format found.')
    except pytube.exceptions.PytubeError:
        print('Failed to retrieve video information.')

# Example usage: extract highest quality lossless audio from a YouTube video
video_url = 'https://www.youtube.com/watch?v=5WEdd78GDFw'
extract_audio(video_url)
