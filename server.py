import cv2
import jsonpickle
import numpy as np
from flask import Flask, jsonify, request
from PIL import Image
import faceshape

app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Hello world'

# @app.route('/image/test', methods=['POST'])
# def test():
#     r = request
#     # convert string of image data to uint8
#     nparr = np.fromstring(r.data, np.uint8)
#     # decode image
#     img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

#     # do some fancy processing here....

#     # build a response dict to send back to client
#     response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
#                 }
#     # encode response using jsonpickle
#     response_pickled = jsonpickle.encode(response)

#     return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route("/im_size", methods=["POST"])
def process_image():
    # file = request.files.get('image', '')
    f1 = request.files['image']
    print(type(f1))
    
    # Read the image via file.stream
    # file = request.form.files["image"]
    print(f1)
    img1 = Image.open(f1)
    print(img1)
    # img2 = cv2.imread(img1)
    # convert string of image data to uint8
    res = faceshape.detectFaceShape(img1)
    return jsonify({'shape': res,})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
