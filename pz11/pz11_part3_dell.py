import base64
import requests
from tkinter import filedialog

id_dell = input("Введите ID для удаления: ")
response = requests.delete(f"http://127.0.0.1:8000/doc_delete/{id_dell}")

print(response.json())
