import tkinter as tk
from tkinter import messagebox
import json

questions_data = []
file_name = './survey/questions.json'
with open(file_name, 'r', encoding="utf-8") as file:
    questions_data = json.load(file)

# 결과값 저장을 위한 변수
mytype = ""

class Comments:
    title = "간단한 MBTI 테스트를 해보자"
    select_item = "아래 항목을 선택하세요."
    result = "당신의 MBTI는 %s"
    error = "모든 항목을 선택해주세요!"

def show_result():
    # 선택된 라디오 버튼의 값으로 MBTI 유형 결정
    global mytype
    mytype = ""
    for question_data in questions_data:
        for option in question_data["options"]:
            # 식별자를 넣어야함
            if option["var"].get() == option["value"]:
                mytype += option["type"]

    if len(mytype) != len(questions_data):
        messagebox.showwarning("경고", Comments.error)
    else:
        messagebox.showinfo("결과", Comments.result % mytype)


def question_frame(window, question_data):
    frame = tk.Frame(window, width=400)

    # 질문 보여주기
    label = tk.Label(frame, text=question_data["question"], font=('helvetica', 15))
    label.pack(anchor="w")

    # 각 질문 당 하나만 선택되게 하려면 함수 내부에서 생성하고, 각 질문의 라디오 버튼들에 이 객체를 할당합니다.
    var = tk.IntVar()
    
    # 처음에 radio 버튼 아무것도 check 안되게 설정하는 법
    var.set(None) 

    for idx, option in enumerate(question_data["options"]):
        option["var"] = var
        option["value"] = idx
        radio_button = tk.Radiobutton(
            frame,
            text=option["txt"],
            variable=option["var"],
            # 고유한 식별자를 넣어줘야 mytype의 type을 담을 수 있었음. value 라디오 부분은 숫자, 소수만 가능.
            value=option["value"] 
        )
        radio_button.pack(anchor="w")

    frame.pack(pady=10)

window = tk.Tk()
window.title('MBTI테스트')
window.geometry("500x500")

header_title = tk.Label(window, text=Comments.title, font=('helvetica', 20, 'bold'))
header_title.pack(padx=10, pady=10)

# 각 질문과 옵션을 표시하는 프레임 생성
for question_data in questions_data:
    question_frame(window, question_data)

# 결과 확인 버튼 생성
result_button = tk.Button(window, text="결과 확인", command=show_result)
result_button.pack(pady=10)

window.mainloop()
