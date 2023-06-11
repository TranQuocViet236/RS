from gensim.models import Word2Vec
from model.deepwalk import DeepWalk
from model.data_preparation import DataPreparation
from model.var_from_cfg import max_walk_length, n_walks_per_node, embedd_dim, window_size, use_skipgram, epochs, embedd_model_path



class Model:
    def __init__(self):
        """
         Create graph and walks to be used in embedding models with Word2Vec
        """
        self.graph = DataPreparation().generate_graph
        self.walks = self.get_walks()


    def get_walks(self):
        """
         Gets walks from the graph. This is a helper function to use DeepWalk
         
         
         @return list of walks in
        """
        deepwalk = DeepWalk(self.graph)
        walks = deepwalk.get_walks(max_walk_length, n_walks_per_node)
        print("Total Number of Walks:", len(walks))
        print("First Walk:", walks[0])
        return walks

    def train_graph_embedd(self):
        """
         Train the embedd model with Word2Vec. This is a non - optimized version
        """
        # Initializing the word2vec
        model = Word2Vec(
            vector_size=embedd_dim,
            window=window_size,
            min_count=0,
            sg=use_skipgram,
            epochs=epochs
        )

        # Building Vocabulary
        model.build_vocab(self.walks)

        # Trainig the Model
        model.train(
            self.walks,
            total_examples=len(self.walks),
            epochs=model.epochs
        )

        # Model Saving
        model.save(embedd_model_path)


if __name__ == '__main__':
    model = Model()
    model.train_graph_embedd()