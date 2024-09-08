import base64
import requests
from tkinter import filedialog

# Пример чтения файла и его кодирования в base64
file_path = filedialog.askopenfilename(filetypes=[("IMAGE files", "*.png;*.jpg;*.jpge")])

with open(file_path, "rb") as f:
    file_data = base64.b64encode(f.read()).decode("utf-8")

# Запрос на API
response = requests.post("http://127.0.0.1:8000/upload_doc/", json={
    "filename": file_path.split("/")[-1],
    "file_data": file_data
})

print(response.json())
