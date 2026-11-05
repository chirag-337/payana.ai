from app.ml.predictor import model_instance

class ModelRegistry:
    def __init__(self):
        self.congestion_model = model_instance

    def get_congestion_model(self):
        return self.congestion_model

registry = ModelRegistry()
