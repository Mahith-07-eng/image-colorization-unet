from tensorflow.keras.models import load_model

def load_colorizer():

    model = load_model("models/my_color_model.keras")

    return model


def colorize_image(model,input_image):

   prediction = model.predict(input_image)

   return prediction[0]