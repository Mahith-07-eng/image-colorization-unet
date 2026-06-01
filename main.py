
from src.preprocess import preprocess_image
from src.predict import (
    load_colorizer,
    colorize_image
)
from src.utils import save_output

image_path = (
    "images/input/test1.png"
)

_, gray, input_image = preprocess_image(
    image_path
)

model = load_colorizer()

predicted = colorize_image(
    model,
    input_image
)

save_output(
    predicted,
    "images/output/colorized_test1.png"
)

print(
    "Colorized image saved successfully!"
)