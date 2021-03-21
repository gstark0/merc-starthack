from django.shortcuts import render
from .serializers import InputSerializer, OtherInputSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# ML STUFF HERE
import base64
import tensorflow.keras
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications import imagenet_utils
from PIL import Image, ImageOps
import numpy as np
import io

model = tensorflow.keras.models.load_model('keras_model.h5')

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

def prepare_image(image, target):
    # if the image mode is not RGB, convert it
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    filename = 'image_to_process.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(base64.b64decode(image))

    opened_image = Image.open(filename)
    opened_image = ImageOps.fit(opened_image, target, Image.ANTIALIAS)

    image_array = np.asarray(opened_image) 
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    data[0] = normalized_image_array

    # return the processed image
    return data



# Create your views here.
@api_view(['POST'])
def facial_recognition(request):
    """
    Perform Facial recognition
    """

    people = ["Jim Carrey", "Sunveer", "Elon Musk", "Obama"]

    welcome_string = ""
    sound_url = ""
    image_url = ""

    """
    if visiting:
        welcome_string = "Mr XXX was informed about your arrival, he’ll come to you as soon as possible"
        sound_url = "some_sound_here"
        image_url = ""
    else:
        welcome_string = "Welcome to Mercedes-Benz, please choose the purpose of your visit on the screen"
        sound_url = "some_other_sound"
        image_url = ""
    """

    if request.method == 'POST':
        print(request.data)
        serializer = InputSerializer(request.data)

        image = serializer.data.get("image")
        image = prepare_image(image, (224, 224))

        preds = model.predict(image)
        # After prediction
        #return preds

        """
        data["predictions"] = []
        # loop over the results and add them to the list of
        # returned predictions
        for (imagenetID, label, prob) in results[0]:
            r = {"label": label, "probability": float(prob)}
            data["predictions"].append(r)
        """

        #return JsonResponse(data)

        #return Response(preds[0][1])
        print(preds[0])
        
        return Response({"name": people[preds[0].tolist().index(max(preds[0]))]})



    #return Response({"string": ""})

@api_view(['GET'])
def sales(request):
    if request.method == 'POST':
        serializer = OtherInputSerializer(request.data)
        data = serializer.data.type_of_car
        if data == "neutral":
            return Response("neutral_sound_here")
        elif data == "calm": 
            return Response("calm_sound_here")

@api_view(['GET'])
def showroom(request):
    if request.method == 'POST':
        serializer = OtherInputSerializer(request.data)
        data = serializer.data.type_of_car
        if data == "neutral":
            return Response("neutral_sound_here")
        elif data == "calm": 
            return Response("calm_sound_here")



