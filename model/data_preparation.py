import networkx as nx
from data_loader import DataLoader

class DataPreparation(DataLoader):
    def __init__(self):
        super().__init__()
        self.books, self.users, self.edges = self.get_graph_info()

    def get_graph_info(self):
        # Merging book rate info and item info
        df = self.book_rate_df.merge(self.items_info_df, on="Book-ID")

        # Removing duplicates
        df = df[~ df.duplicated(subset=["User-ID", "Book-Title"], keep='first')]

        print(df.sample(3))

        books = sorted(df['Book-Title'].unique().tolist())
        users = sorted(df['User-ID'].unique().tolist())
        edges = df[[
            'Book-Title',
            'User-ID',
            'rating'
        ]].values.tolist()

        return books, users, edges

    @property
    def generate_graph(self):
        # init graph
        G = nx.Graph()

        # Add nodes to graph
        G.add_nodes_from(self.books, bipartite=0)
        G.add_nodes_from(self.users, bipartite=1)

        # Add edges to graph
        G.add_weighted_edges_from(self.edges)

        return G




if __name__ == '__main__':
    DataPreparation = DataPreparation()
    DataPreparation.merge_df()
