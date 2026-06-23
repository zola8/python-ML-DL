import datetime

import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)

with open('./whitelist.txt', 'r') as f:
    authorized_users = [line.strip() for line in f.readlines() if len(line) > 1]

print(authorized_users)

log_path = './log.txt'

while (True):
    ret, frame = cap.read()

    qr_info = decode(frame)

    if len(qr_info) > 0:
        qr = qr_info[0]

        data = qr.data
        rect = qr.rect
        polygon = qr.polygon

        frame = cv2.rectangle(
            frame,
            (rect.left, rect.top),
            (rect.left + rect.width, rect.top + rect.height),
            (0, 255, 0),
            5
        )
        frame = cv2.polylines(frame, np.array([polygon]), True, (255, 0, 0), 5)

        if data.decode() in authorized_users:
            cv2.putText(frame, '[Access granted]', (rect.left, rect.top - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (0, 0, 255), 2)
            # most_recent_access
            # with open(log_path, 'a') as f:
            #     f.write("{} | {}\n".format(datetime.datetime.now(), data.decode()))
        else:
            cv2.putText(frame, '[Access denied]', (rect.left, rect.top - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (0, 0, 255), 2)

        cv2.putText(frame, data, (rect.left, rect.top - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
