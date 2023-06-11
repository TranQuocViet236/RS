## **I.  Source code structure:**
  - **book-crossing**: Thư mục chứa toàn bộ dữ liệu đã được extract từ folderzip data.
    + **link**: "https://github.com/caserec/Datasets-for-Recommender-Systems/tree/master/Processed%20Datasets/BookCrossing"

  - **config**: Thư mục chứa thông tin config, đường dẫn file dữ liệu, các tham số cho mô hình.

  - **eda_notebooks**: Thư mục chứa file Jupyter notebook (file .ipynb) mô tả thông tin EDA dữ liệu.

  - **model**: Thư mục chứa source code liên quan đến mô hình:
    + **data_loader.py**: File code nhằm load dữ liệu từ file .dat, kèm theo xử lý một số case dữ liệu lỗi, reformat dữ liệu.
    + **data_preparation.py**: File code này sẽ sử dụng dữ liệu từ **data_loader.py**, lấy các thông tin về node (dữ liệu user, item), và thông tin edge (dữ liệu rating), nhằm khởi tạo một **Graph**, chuẩn bị cho quá trình training.
    + **deepwalk.py**: Đây là file code nhằm sử dụng thuật toán **Deepwalk** để chuẩn bị dữ liệu các chuỗi bước đi, nhằm chuẩn bị cho quá trình training thuật toán **word2vec** để tạo ra embedding cho các node trên đồ thị.
    + **model_training.py**: Trong file này, mô hình sẽ sử dụng dữ liệu được sinh ra từ **deepwalk** để training mô hình embedding, sau đó lưu vào file **embedd.bin**.
    + **model_prediction.py**: File này có nhiệm vụ, dự đoán ra một list danh sách cuốn sách có thể gợi ý cho người dùng, dựa trên độ tương tự của các **embedding node**.
  - **requirement.txt**: Thông tin các packages cần thiết cho quá trình running source code.

## II. Usage: