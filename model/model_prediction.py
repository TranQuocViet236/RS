import pandas as pd
from gensim.models import Word2Vec
from model.var_from_cfg import embedd_model_path

class ModelPred():
    def __init__(self):
        """
         Initialize the model. This is called by __init__ and should not be called directly
        """
        self.model = self.load_model()


    def load_model(self):
        """
         Load model from file embedd.bin . This is used to train the model
         
         @return A word2vec model loaded
        """

        # Load saved model
        model = Word2Vec.load(embedd_model_path)
        return model


    def predict(self, user_id):
        """
         Predicts most similar books for a user. 
         
         @param user_id - ID of user to predict
         
         @return DataFrame with book title and score for each book that is
        """
        
        result = self.model.wv.most_similar(user_id)

        result_df = pd.DataFrame(result)
        result_df.columns = ['Book-Title', 'Score']

        print(result_df)

        return result_df


if __name__ == '__main__':
    model_pred = ModelPred()
    model_pred.predict(1)

