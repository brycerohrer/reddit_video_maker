# This clas will hold the class that edits the images into video
#TODO: Once complete, remove global import and only import required

from moviepy.editor import * # movie editor 
import os  # used for some file grabbing
from PIL import Image # Image library

class VideoEditor:
    def __init__(self,num_replies):
        self.num_replies = num_replies
        self.image_path = '../images/'
        self.audio_path = '../audio/'

    def create_movie(self):
        ''' Method will make a slide show movie out of the audio and images
        Note: currently all images are set to 5 second duration, needs to 
        change to the durration of each audio clip
        TODO: Adding audio clips still hasnt happened
        '''
        clips = [] # clips are mp4 clips to be combined to make entire movie
        
        video_name = 'reddit_movie.mp4'

        # Add the title image first
        # Creating an 'ImageClip' of each jpeg we take
        #clips.append(ImageClip(self.image_path + 'title.jpeg').set_duration(5))
        tmp_title = ImageClip(self.image_path + 'title.jpeg').set_duration(5)
        title_audio = AudioFileClip(self.audio_path + 'title.mp3').set_duration(5)
        tmp_title = tmp_title.set_audio(title_audio)
        clips.append(tmp_title)

        
        '''
        for i in range(0, self.num_replies):
            img_name = 'reply' + str(i) + '.jpeg'
            print(f'adding file: {self.image_path + img_name} to the file')
            clips.append(ImageClip(self.image_path + img_name).set_duration(5))
            audio = AudioFileClip(self.audio_path + 'reply' + str(i) + '.mp3')
            #audio.append(AudioFileClip(self.audio_path + 'reply' + str(i) + '.mp3'))
            clips[i] = clips[i].set_audio(audio)

        print(audio)
        '''

        '''
        # add each reply using same method
        for i in range(0, self.num_replies):
            # each reply is named: reply0, reply1, reply2, ....
        '''

        # Output my file of clips
        print(clips)
        # Create a video from the clips and turn it into a video 
        #video = concatenate_videoclips(clips, method='compose')
        video = concatenate_videoclips(clips, method='compose')
        # Currently only 24fps due to wanting quick runtime for debug
        # Can upgrade during production
        video.write_videofile('reddit.mp4', fps=24)


    