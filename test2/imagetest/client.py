"""import requests
import base64
import cv2
import numpy as np

image_name = 'C:\\Users\\82104\\Desktop\\testFlask\\test2\\imagetest\\car6.jpg'
ff = np.fromfile(image_name, np.uint8)
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
cv2.imshow("test", img)
jpg_img = cv2.imencode('.jpg', img)
b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')


files = {
            "img": b64_string,
        }

r = requests.post("http://127.0.0.1:5000", json=files)
print(r.json())"""