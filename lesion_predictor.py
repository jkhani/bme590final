from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from get_prediction import get_prediction
from ImageConversion import Image

app = Flask(__name__)
CORS(app)

@app.route("/upload_images", methods=['POST'])
def lesion():
    """

    :return: the predicted classification of the lesion (benign or malignant)
    """
    image = str(request.json['fileData'])
    print(image)
    index = 0
    found = False
    while found is False:
        if image[index]==',':
            image = image[index+1:len(image)]
        else:
            index = index + 1

    for ii in range(0, len(image)):


    filename = "lesion.jpg"
    #the below line is for testing outside the docker container only
    #predictions = str(type(image))

    #lesion_image = Image(input_image=image, thefilename=filename)
    #lesion_image.save_image_string(file=filename)
    #(labels, predictions) = get_prediction(imread(filename))
    return jsonify(image)

