from PIL import Image
from transformers import ViTImageProcessor, ViTForImageClassification

class ImageClassifier:

    def __init__(self):
        self.processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
        self.model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')

    def classify(self, path):
        image= Image.open(path)
        input = self.processor(images=image, return_tensors='pt')
        outputs = self.model(**input)
        logits = outputs.logits
        # model predicts one of the 1000 ImageNet classes
        predicted_class_idx = logits.argmax(-1).item()
        print("Predicted class:", self.model.config.id2label[predicted_class_idx])



