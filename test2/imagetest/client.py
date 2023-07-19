import requests
import base64
try:
    import cv2
except:
    pass
import numpy as np

if __name__ == "main":

    image_name = '.\\car6.jpg'
    ff = np.fromfile(image_name, np.uint8)
    img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
    cv2.imshow("test", img)
    jpg_img = cv2.imencode('.jpg', img)
    b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')


    files = {
                "img": b64_string,
            }

    r = requests.post("https://port-0-aiserver-20zynm2mljxybsqy.sel4.cloudtype.app/carNum", json=files)
    print(r.json())