import random

class Clips:

    @staticmethod
    def idle():
        idle_clips = ['./clips/idle1.mp4'] # add more clips in the future
        return random.choice(idle_clips)
    
    @staticmethod
    def listen_transition():
        return './clips/listen_transition.mp4'

    @staticmethod
    def listening():
        listening_clips = ['./clips/listen_loop.mp4', './clips/listen_loop_2.mp4']
        return random.choice(listening_clips)

    @staticmethod
    def thinking():
        thinking_clips = ['./clips/thinking_1.mp4']
        return random.choice(thinking_clips)

    @staticmethod
    def talking():
        talking_clips = ['./clips/talking_1.mp4'] #TODO: change this placeholder
        return random.choice(talking_clips)