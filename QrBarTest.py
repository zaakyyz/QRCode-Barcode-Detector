import cv2
import numpy as np
from pyzbar.pyzbar import decode


def draw_barcode_boundary(img, barcode, color):
    x, y, w, h = barcode.rect

    if barcode.type == 'QRCODE' and len(barcode.polygon) >= 4:
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, color, 5)
    else:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 5)

    return x, y


def get_label_position(x, y):
    return x, max(y - 10, 30)


#img = cv2.imread('1.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:

    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        x, y = draw_barcode_boundary(img, barcode, (255,0,255))
        cv2.putText(img,myData,get_label_position(x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255,0,255),2)

    cv2.imshow('Result',img)
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27 or cv2.getWindowProperty('Result', cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
