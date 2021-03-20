from django.shortcuts import render
from .serializers import InputSerializer

# ML STUFF HERE
import base64
import tensorflow.keras
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications import imagenet_utils
from PIL import Image, ImageOps
import numpy as np
import io

model = tensorflow.keras.models.load_model('keras_model.h5')

def prepare_image(image, target):
    # if the image mode is not RGB, convert it
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    opened_image = Image.open(image)

    if image.mode != "RGB":
        image = image.convert("RGB")

    image_array = np.asarray(image) 
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    # return the processed image
    return data



# Create your views here.
@api_view(['GET'])
def facial_recognition(request):
    """
    List all code snippets, or create a new snippet.
    """
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

    if request.method == 'GET':
        serializer = InputSerializer(request.data)
        image = serializer.image.decode('base64')

        prepare_image(image, (224, 224))

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

        return Response(preds)



    #return Response({"string": ""})
