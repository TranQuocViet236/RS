import re

with open("tmp_new_files_7.dat", "r") as file:
    lines = file.readlines()

# Xóa kí tự tab cuối mỗi dòng
# lines = [line.rstrip() for line in lines]
# lines = [re.sub(r'&amp\s+', '&amp Stoughton', line) for line in lines]
# lines = [re.sub(r'&amp\s+', '&amp Schuster', line) for line in lines]
# lines = [re.sub(r'&amp\s+', '&amp Demons', line) for line in lines]
# lines = [re.sub(r'&amp\s+', '&amp Stevie', line) for line in lines]
# lines = [re.sub(r'&amp\s+', '&amp ', line) for line in lines]
lines = [re.sub(r'&amp\s+', '&amp ', line) for line in lines]


# &amp	 Small Ltd &amp	 Stoughton Stevie Magickal JanÃ©s
# Ghi dữ liệu đã xử lý vào file mới
with open("items_info.dat", "w") as new_file:
    for line in lines:
        # line = line.rstrip('\t')
        # line.replace('&amp	 Company', '&amp Company')
        new_file.write(line)