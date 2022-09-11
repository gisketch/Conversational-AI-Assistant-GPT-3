import random

class Clips:

    @staticmethod
    def boot():
        v = ['./clips/startup.mp4'] # add more clips in the future
        return random.choice(v)

    @staticmethod
    def idle():
        v = ['./clips/idle_loop.mp4'] # add more clips in the future
        return random.choice(v)

    @staticmethod
    def listening():
        v = ['./clips/listen_loop.mp4']
        return random.choice(v)

    @staticmethod
    def thinking():
        v = ['./clips/thinking_loop.mp4']
        return random.choice(v)

    @staticmethod
    def talking():
        v = ['./clips/talking_loop.mp4'] #TODO: change this placeholder
        return random.choice(v)