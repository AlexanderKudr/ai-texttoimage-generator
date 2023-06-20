import torch
from PIL import Image

from .config import initializeModel
from utils import getImagesFromFolder


model, featureExtractor, tokenizer, generateKwargs, device = initializeModel()


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


def generateImageData(path: str) -> list:
    payload = lambda file: {
        "imagePath": file.replace("\\", "/"),
        "caption": generateImageCaption([file])[0],
    }
    result = list(map(payload, getImagesFromFolder(path)))
    return result
