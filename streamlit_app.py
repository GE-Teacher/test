import streamlit as st
import datetime

# Xử lý sự kiện nhấn nút
def add_task():
    task = st.text_input("Nhập tên công việc:")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if task:
        with open("tasks.txt", "a") as f:
            f.write(f"{task} ({now})\n")

# Hiển thị giao diện
st.title("To-Do List")
st.write("Nhập tên công việc và nhấn nút để thêm vào danh sách.")
add_button = st.button("Thêm công việc")
if add_button:
    add_task()