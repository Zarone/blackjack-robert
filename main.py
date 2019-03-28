import time
import os
import cv2
import Cards
import VideoStream
from blackjack import Blackjack

IM_WIDTH = 1280
IM_HEIGHT = 720
FRAME_RATE = 10

frame_rate_calc = 1
freq = cv2.getTickFrequency()

font = cv2.FONT_HERSHEY_SIMPLEX

video_stream = VideoStream.VideoStream((IM_WIDTH, IM_HEIGHT), FRAME_RATE, 2, 0).start()
time.sleep(1)

path = os.path.dirname(os.path.abspath(__file__))
train_ranks = Cards.load_ranks(path + '/Card_Imgs/')
train_suits = Cards.load_suits(path + '/Card_Imgs/')

game = Blackjack(video_stream, train_ranks, train_suits)
game.new_game(1)
game.resolve_round()
video_stream.stop()
