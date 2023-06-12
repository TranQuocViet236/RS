## **I.  Source code structure:**
  - **book-crossing**: Thư mục chứa toàn bộ dữ liệu đã được extract từ folderzip data.
    + **link**: "https://github.com/caserec/Datasets-for-Recommender-Systems/tree/master/Processed%20Datasets/BookCrossing"

  - **config**: Thư mục chứa thông tin config, đường dẫn file dữ liệu, các tham số cho mô hình.

  - **documents**: Chứa file pdf mô tả thông tin document về dự án.

  - **eda_notebooks**: Thư mục chứa file Jupyter notebook (file .ipynb) mô tả thông tin EDA dữ liệu.

  - **model**: Thư mục chứa source code liên quan đến mô hình:
    + **data_loader.py**: File code nhằm load dữ liệu từ file .dat, kèm theo xử lý một số case dữ liệu lỗi, reformat dữ liệu.
    + **data_preparation.py**: File code này sẽ sử dụng dữ liệu từ **data_loader.py**, lấy các thông tin về node (dữ liệu user, item), và thông tin edge (dữ liệu rating), nhằm khởi tạo một **Graph**, chuẩn bị cho quá trình training.
    + **deepwalk.py**: Đây là file code nhằm sử dụng thuật toán **Deepwalk** để chuẩn bị dữ liệu các chuỗi bước đi, nhằm chuẩn bị cho quá trình training thuật toán **word2vec** để tạo ra embedding cho các node trên đồ thị.
    + **model_prediction.py**: File này có nhiệm vụ, dự đoán ra một list danh sách cuốn sách có thể gợi ý cho người dùng, dựa trên độ tương tự của các **embedding node**.
  - **weight**: Thư mục chứ thông tin mô hình embedding sau khi được train.
  - **requirement.txt**: Thông tin các packages cần thiết cho quá trình running source code.
  - **model_training.py**: Trong file này, mô hình sẽ sử dụng dữ liệu được sinh ra từ **deepwalk** để training mô hình embedding, sau đó lưu vào file **embedd.bin** ở thư mục **weight**.
     Nếu bạn muốn training lại mô hình, có thể chạy lại file này, và điều chỉnh tham số ở file config.yaml trong thư mục config.
  - **easy_user.ipynb**: File này ghi lại flow (clone source, cài đặt requirement và dự đoán) dễ, đơn giản và nhanh chóng để tương tác với mô hình.

## **II. Usage**:
  - **Setup environment**:  
    + **Install required packages**: pip install -r requirements.txt
    
  **1. Prediction with user_id**: python .\main.py --user_id **user_id_muốn_gợi_ý**

    + Example:  python .\main.py --user_id 2
    * Output: 

  | Book-Title                                        | Score   |
  |---------------------------------------------------|---------|
  | Thinking in Java (2nd Edition)                    | 0.601480| 
  | Something M.Y.T.H. Inc (Robert Asprin's Myth)     |0.536046|
  | Meet Felicity: An American Girl : 1774 (The Am... |0.535973|
| Runaway Pony (Pony Pals (Paperback))              |0.493083|
| The Book of Lost Tales 1 (The History of Middl... |0.491807|
 | Crazy Horse                                       | 0.486763  |
 | Bunnicula: A Rabbit-Tale of Mystery               |0.479550|
  | When the Wind Blows                               |0.476952|
   | Real Father (Twins) (Super Romance Series)        |0.474158|
 | Harry Potter and the Chamber of Secrets (Book 2)  |0.471537|
    
    + Run with API: python .\app.py
    + Truy cập vào đường dẫn: localhost:5000/get_user_data?user_id=1 (tham số user_id=1)
    + Output:
[{"Book-Title":"The Other Side of the Story : A Novel (Keyes, Marian)","Score":0.421561569},{"Book-Title":"Happy and Sad, Grouchy and Glad (Little Golden Book)","Score":0.3790979981},...]

