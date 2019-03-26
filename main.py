import time
import os
import cv2
import Cards
import VideoStream

def get_cards(img, train_ranks, train_suits):
    pre = Cards.preprocess_image(img)

    cnts, cnt_card = Cards.find_cards(pre)

    if len(cnts) != 0:
        c = []

        for i, cnt in enumerate(cnts):
            if cnt_card[i] == 1:
                found_card = Cards.preprocess_card(cnt, img)
                c.append(found_card)
                found_card.best_rank_match, found_card.best_suit_match, found_card.rank_diff, found_card.suit_diff = Cards.match_card(found_card, train_ranks, train_suits)
        if len(c) != 0:
            return c
    return None



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

cam_quit = False

while not cam_quit:
    img = video_stream.read()

    t1 = cv2.getTickCount()
    cards = get_cards(img, train_ranks, train_suits)

    if cards is not None:
        s = ''
        for i in range(len(cards)):
            s += cards[i].best_rank_match + ' of ' + cards[i].best_suit_match + '. '
        print(s)
    else:
        print('None found')

    if cards != None and len(cards) != 0:
        temp_cnts = []
        for c in cards:
            temp_cnts.append(c.contour)
            img = Cards.draw_results(img, c)
        cv2.drawContours(img, temp_cnts, -1, (255, 0, 0), 2)
    cv2.putText(img, 'FPS: ' + str(int(frame_rate_calc)), (10, 26), font, 0.7, (255, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow('Cards', img)

    t2 = cv2.getTickCount()
    time1 = (t2-t1)/freq
    frame_rate_calc = 1/time1

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        cam_quit = True

cv2.destroyAllWindows()
video_stream.stop()
