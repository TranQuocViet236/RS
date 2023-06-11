from omegaconf import OmegaConf

# load source config
src_cfg = OmegaConf.load('config/config.yaml')

# data paths
book_hist_path = src_cfg.file_path.book_hist
book_rate_path = src_cfg.file_path.book_rate
items_info_path = src_cfg.file_path.items_info
users_info_path = src_cfg.file_path.users_info

# deepwalk parameters
min_edge_weight = int(src_cfg.parameters.deepwalk.min_edge_weight)
percent_select_node = int(src_cfg.parameters.deepwalk.percent_select_node)
max_walk_length = int(src_cfg.parameters.deepwalk.max_walk_length)
n_walks_per_node = int(src_cfg.parameters.deepwalk.n_walks_per_node)

# word2vec parameters
embedd_dim = int(src_cfg.parameters.word2vec.embedd_dim)
window_size = int(src_cfg.parameters.word2vec.window_size)
use_skipgram = src_cfg.parameters.word2vec.use_skipgram
epochs = int(src_cfg.parameters.word2vec.epochs)

# embedding model path
embedd_model_path = src_cfg.model_path