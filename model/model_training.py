from data_preparation import DataPreparation
from deepwalk import DeepWalk
from gensim.models import Word2Vec

# DEEPWALK PARAMETERS
MAX_WALK_LEN = 40       # maximum length a sentence can have in corpus
N_WALKS_PER_NODE = 50   # these many sentences will be generated by taking one node as start

# EMBEDDING PARAMETERS
EMB_DIM = 128
WINDOW_SIZE = 2
USE_SKIPGRAPM = False
EPOCHS = 10


class Model:
    def __init__(self):
        self.graph = DataPreparation().generate_graph
        self.walks = self.get_walks()
        print(self.graph.nodes)

    def get_walks(self):
        deepwalk = DeepWalk(self.graph)
        walks = deepwalk.get_walks(MAX_WALK_LEN, N_WALKS_PER_NODE)
        print("Total Number of Walks:", len(walks))
        print("First Walk:", walks[0])
        return walks

    def train_graph_embedd(self):
        # Initializing the word2vec
        model = Word2Vec(
            vector_size=EMB_DIM,
            window=WINDOW_SIZE,
            min_count=0,
            sg=USE_SKIPGRAPM,
            epochs=EPOCHS
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
        model.save('embedd.bin')

if __name__ == '__main__':
    model = Model()
    model.train_graph_embedd()