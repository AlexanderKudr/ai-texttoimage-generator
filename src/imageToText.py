from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image
import torch

from utils.osHelper import get_name_and_age

getImagesFromFolder, someData = get_name_and_age

model = VisionEncoderDecoderModel.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning"
)
featureExtractor = ViTImageProcessor.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning"
)
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


maxLength = 16
numBeams = 4
generateKwargs = {"max_length": maxLength, "num_beams": numBeams}


def generateImageCaption(path: str) -> list[str]:
    store = []
    for imagePath in path:
        image = Image.open(imagePath)
        if image.mode != "RGB":
            image = image.convert(mode="RGB")

        store.append(image)

    pixel_values: torch.Tensor = featureExtractor(
        images=store, return_tensors="pt"
    ).pixel_values
    pixel_values = pixel_values.to(device)

    output_ids = model.generate(pixel_values, **generateKwargs)

    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]
    return preds


def generateImageData() -> list:
    payload = lambda file: {
        "imagePath": file,
        "caption": generateImageCaption([file])[0],
    }
    result = list(map(payload, getImagesFromFolder("img")))
    return result


print(generateImageData())
