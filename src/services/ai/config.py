from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch


def initializeModel():
    numBeams = 4
    maxLength = 16

    gptModel = "nlpconnect/vit-gpt2-image-captioning"
    model: VisionEncoderDecoderModel = VisionEncoderDecoderModel.from_pretrained(
        gptModel
    )
    featureExtractor: ViTImageProcessor = ViTImageProcessor.from_pretrained(gptModel)
    tokenizer: AutoTokenizer = AutoTokenizer.from_pretrained(gptModel)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    generateKwargs = {"max_length": maxLength, "num_beams": numBeams}

    return model, featureExtractor, tokenizer, generateKwargs, device
