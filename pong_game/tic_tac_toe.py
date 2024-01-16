import cv2
import time
from cvzone.HandTrackingModule import HandDetector

curr_state = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


def check_state():
    f11=0
    f12=0
    f13=0
    f21=0
    f22=0
    f23=0
    f31=0
    f32=0
    f33=0
    for i in range(5):
        if 345 < c[i][0] < 445 and 160 < c[i][1] < 230:
            curr_state[0][0] = 1
            f11=1
        elif 345 < d[i][0] < 445 and 160 < d[i][1] < 230:
            curr_state[0][0] = 2
            f11=2
        elif f11==0:
            curr_state[0][0] = 0

        if 445 < c[i][0] < 545 and 160 < c[i][1] < 230:
            curr_state[0][1] = 1
            f12=1
        elif 445 < d[i][0] < 545 and 160 < d[i][1] < 230:
            curr_state[0][1] = 2
            f12=2
        elif f12==0:
            curr_state[0][1] = 0

        if 545 < c[i][0] < 645 and 160 < c[i][1] < 230:
            curr_state[0][2] = 1
            f13=1
        elif 545 < d[i][0] < 645 and 160 < d[i][1] < 230:
            curr_state[0][2] = 2
            f13=2
        elif f13==0:
            curr_state[0][2] = 0

        if 345 < c[i][0] < 445 and 230 < c[i][1] < 300:
            curr_state[1][0] = 1
            f21=1
        elif 345 < d[i][0] < 445 and 230 < d[i][1] < 300:
            curr_state[1][0] = 2
            f21=2
        elif f21==0:
            curr_state[1][0] = 0

        if 445 < c[i][0] < 545 and 230 < c[i][1] < 300:
            curr_state[1][1] = 1
            f22=1
        elif 445 < d[i][0] < 545 and 230 < d[i][1] < 300:
            curr_state[1][1] = 2
            f22=2
        elif f22==0:
            curr_state[1][1] = 0

        if 545 < c[i][0] < 645 and 230 < c[i][1] < 300:
            curr_state[1][2] = 1
            f23=1
        elif 545 < d[i][0] < 645 and 230 < d[i][1] < 300:
            curr_state[1][2] = 2
            f23=2
        elif f23==0:
            curr_state[1][2] = 0

        if 345 < c[i][0] < 445 and 300 < c[i][1] < 370:
            curr_state[2][0] = 1
            f31=1
        elif 345 < d[i][0] < 445 and 300 < d[i][1] < 370:
            curr_state[2][0] = 2
            f31=2
        elif f31==0:
            curr_state[2][0] = 0

        if 445 < c[i][0] < 545 and 300 < c[i][1] < 370:
            curr_state[2][1] = 1
            f32=1
        elif 445 < d[i][0] < 545 and 300 < d[i][1] < 370:
            curr_state[2][1] = 2
            f32=2
        elif f32==0:
            curr_state[2][1] = 0

        if 545 < c[i][0] < 645 and 300 < c[i][1] < 370:
            curr_state[2][2] = 1
            f33=1
        elif 545 < d[i][0] < 645 and 300 < d[i][1] < 370:
            curr_state[2][2] = 2
            f33=2
        elif f33==0:
            curr_state[2][2] = 0

def check_win():
    cs = curr_state
    s=0
    for i in range(3):
        for j in range(3):
            s += cs[i][j]
    if s<3:
        return 0, 0, 0, 0, 0

    if cs[0][0]==cs[1][1] and cs[1][1]==cs[2][2]:
        return cs[0][0], 345, 160, 645, 370

    if cs[0][2]==cs[1][1] and cs[1][1]==cs[2][0]:
        return cs[0][2], 345, 370, 645, 160

    if cs[0][0]==cs[0][1] and cs[0][0]==cs[0][2]:
        return cs[0][0], 345, 195, 645, 195

    if cs[1][0]==cs[1][1] and cs[1][0]==cs[1][2]:
        return cs[1][0], 345, 265, 645, 265

    if cs[2][0]==cs[2][1] and cs[2][0]==cs[2][2]:
        return cs[2][0], 345, 335, 645, 335

    if cs[0][0]==cs[1][0] and cs[0][0]==cs[2][0]:
        return cs[0][0], 395, 160, 395, 370

    if cs[0][1]==cs[1][1] and cs[0][1]==cs[2][1]:
        return cs[0][1], 495, 160, 495, 370

    if cs[0][2]==cs[1][2] and cs[0][2]==cs[2][2]:
        return cs[0][2], 595, 160, 595, 370

    return 0, 0, 0, 0, 0

ptime = 0
ctime = 0



color = [
    [(255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)],
    [(0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)]
]

w, h = 50, 50

c = [
    [45, 125],
    [45, 195],
    [45, 265],
    [45, 335],
    [45, 405]
]

d = [
    [925, 125],
    [925, 195],
    [925, 265],
    [925, 335],
    [925, 405]
]


turn = 0
won = 0
colorT = (255, 0, 0)
last_changed = 0

w1x=0
w2x=0
w1y=0
w2y=0

cap = cv2.VideoCapture(0)
cap.set(3, 1500)
cap.set(4, 900)
detector = HandDetector(detectionCon=0.8)

while cap.isOpened():
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    if hands:
        hand1 = hands[0]
        lmlist1 = hand1["lmList"]

        if lmlist1:
            length, info, img = detector.findDistance(lmlist1[8][0:2], lmlist1[12][0:2], img, color=(255, 0, 0))
            if length < 40:
                cursor = lmlist1[8]
                if 440 < cursor[0] < 540 and 470 < cursor[1] < 510 and time.time()-last_changed>5 and not won:
                    last_changed = time.time()
                    v, kx, ky, lx, ly = check_win()
                    if v:
                        won = v
                        w1x = kx
                        w1y = ky
                        w2x = lx
                        w2y = ly

                    turn = turn + 1
                    if turn%2 == 0:
                        colorT = (255, 0, 0)
                    else:
                        colorT = (0, 0, 255)

                if c[0][0] - w//2 < cursor[0] < c[0][0] + w//2 and c[0][1] - h//2 < cursor[1] < c[0][1] + h//2 and turn%2==0 and not won:
                    color[0][0] = (0, 255, 0)
                    c[0][0] = cursor[0]
                    c[0][1] = cursor[1]
                elif c[1][0] - w//2 < cursor[0] < c[1][0] + w//2 and c[1][1] - h//2 < cursor[1] < c[1][1] + h//2 and turn%2==0 and not won:
                    color[0][1] = (0, 255, 0)
                    c[1][0] = cursor[0]
                    c[1][1] = cursor[1]
                elif c[2][0] - w//2 < cursor[0] < c[2][0] + w//2 and c[2][1] - h//2 < cursor[1] < c[2][1] + h//2 and turn%2==0 and not won:
                    color[0][2] = (0, 255, 0)
                    c[2][0] = cursor[0]
                    c[2][1] = cursor[1]
                elif c[3][0] - w//2 < cursor[0] < c[3][0] + w//2 and c[3][1] - h//2 < cursor[1] < c[3][1] + h//2 and turn%2==0 and not won:
                    color[0][3] = (0, 255, 0)
                    c[3][0] = cursor[0]
                    c[3][1] = cursor[1]
                elif c[4][0] - w//2 < cursor[0] < c[4][0] + w//2 and c[4][1] - h//2 < cursor[1] < c[4][1] + h//2 and turn%2==0 and not won:
                    color[0][4] = (0, 255, 0)
                    c[4][0] = cursor[0]
                    c[4][1] = cursor[1]
                elif d[0][0] - w//2 < cursor[0] < d[0][0] + w//2 and d[0][1] - h//2 < cursor[1] < d[0][1] + h//2 and turn%2==1 and not won:
                    color[1][0] = (0, 255, 0)
                    d[0][0] = cursor[0]
                    d[0][1] = cursor[1]
                elif d[1][0] - w//2 < cursor[0] < d[1][0] + w//2 and d[1][1] - h//2 < cursor[1] < d[1][1] + h//2 and turn%2==1 and not won:
                    color[1][1] = (0, 255, 0)
                    d[1][0] = cursor[0]
                    d[1][1] = cursor[1]
                elif d[2][0] - w//2 < cursor[0] < d[2][0] + w//2 and d[2][1] - h//2 < cursor[1] < d[2][1] + h//2 and turn%2==1 and not won:
                    color[1][2] = (0, 255, 0)
                    d[2][0] = cursor[0]
                    d[2][1] = cursor[1]
                elif d[3][0] - w//2 < cursor[0] < d[3][0] + w//2 and d[3][1] - h//2 < cursor[1] < d[3][1] + h//2 and turn%2==1 and not won:
                    color[1][3] = (0, 255, 0)
                    d[3][0] = cursor[0]
                    d[3][1] = cursor[1]
                elif d[4][0] - w//2 < cursor[0] < d[4][0] + w//2 and d[4][1] - h//2 < cursor[1] < d[4][1] + h//2 and turn%2==1 and not won:
                    color[1][4] = (0, 255, 0)
                    d[4][0] = cursor[0]
                    d[4][1] = cursor[1]
                else:
                    for i in range(2):
                        for j in range(5):
                            if i==0:
                                color[i][j] = (255, 0, 0)
                            else:
                                color[i][j] = (0, 0, 255)
    else:
        for i in range(2):
            for j in range(5):
                if i==0:
                    color[i][j] = (255, 0, 0)
                else:
                    color[i][j] = (0, 0, 255)

    cv2.putText(img, 'Block for X', (20, 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 2)
    cv2.circle(img, (c[0][0], c[0][1]), 25, color[0][0], cv2.FILLED)
    cv2.circle(img, (c[1][0], c[1][1]), 25, color[0][1], cv2.FILLED)
    cv2.circle(img, (c[2][0], c[2][1]), 25, color[0][2], cv2.FILLED)
    cv2.circle(img, (c[3][0], c[3][1]), 25, color[0][3], cv2.FILLED)
    cv2.circle(img, (c[4][0], c[4][1]), 25, color[0][4], cv2.FILLED)

    cv2.putText(img, 'Block for O', (800, 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)
    cv2.rectangle(img, (d[0][0] - w//2, d[0][1] - h//2), (d[0][0] + w//2, d[0][1] + h//2), color[1][0], cv2.FILLED)
    cv2.rectangle(img, (d[1][0] - w//2, d[1][1] - h//2), (d[1][0] + w//2, d[1][1] + h//2), color[1][1], cv2.FILLED)
    cv2.rectangle(img, (d[2][0] - w//2, d[2][1] - h//2), (d[2][0] + w//2, d[2][1] + h//2), color[1][2], cv2.FILLED)
    cv2.rectangle(img, (d[3][0] - w//2, d[3][1] - h//2), (d[3][0] + w//2, d[3][1] + h//2), color[1][3], cv2.FILLED)
    cv2.rectangle(img, (d[4][0] - w//2, d[4][1] - h//2), (d[4][0] + w//2, d[4][1] + h//2), color[1][4], cv2.FILLED)

    cv2.line(img, (345, 230), (645, 230), (0, 0, 0), 2)
    cv2.line(img, (345, 300), (645, 300), (0, 0, 0), 2)
    cv2.line(img, (445, 160), (445, 370), (0, 0, 0), 2)
    cv2.line(img, (545, 160), (545, 370), (0, 0, 0), 2)

    cv2.rectangle(img, (15, 95), (75, 435), (255, 0, 0), 2)
    cv2.rectangle(img, (895, 95), (955, 435), (0, 0, 255), 2)

    if turn%2==0 and not won:
        cv2.putText(img, "Blue's turn", (400, 70), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.4, colorT, 2)
        cv2.rectangle(img, (440, 470), (540, 510), colorT, cv2.FILLED)
        cv2.putText(img, "Done", (450, 500), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    elif turn%2==1 and not won:
        cv2.putText(img, "Red's turn", (400, 70), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.4, colorT, 2)
        cv2.rectangle(img, (440, 470), (540, 510), colorT, cv2.FILLED)
        cv2.putText(img, "Done", (450, 500), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    else:
        cv2.line(img, (w1x, w1y), (w2x, w2y), (0, 0, 0), 4)
        if won==2:
            cv2.putText(img, "RED WON!!!", (400, 70), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.4, (0,0,255), 2)
        else:
            cv2.putText(img, "BLUE WON!!!", (400, 70), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.4, (255,0,0), 2)

    check_state()

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.putText(img, f'FPS: {int(fps)}', (30, 30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
    if success:
        cv2.imshow('Camera', img)
        if cv2.waitKey(25) & 0xff == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
