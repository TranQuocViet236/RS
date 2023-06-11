import pandas as pd
from gensim.models import Word2Vec


class ModelPred():
    def __init__(self):
        self.model = self.load_model()

    def load_model(self):
        # Load saved model
        model = Word2Vec.load("embedd.bin")
        return model

    def predict(self, user_id):
        result = self.model.wv.most_similar(user_id)
        print(result)
        print(pd.DataFrame(result))


if __name__ == '__main__':
    model_pred = ModelPred()
    model_pred.predict(1)

