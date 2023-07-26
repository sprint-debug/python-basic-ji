# 목표: 메인페이지에서 시작하기 누르면 테스트 시작, 한 화면에 질문이 하나씩 나오게 구현, 총 3개의 옵션으로 구현 (그렇다 보통이다 아니다), 결과는 각 유형별 평균 퍼센트로 나타내기

from tkinter import *
import tkinter.ttk
import json

# json 파일 가져오기
questions_data = []
file_name = './survey/mbti_questions.json'
with open(file_name, 'r', encoding="utf-8") as file: questions_data = json.load(file)

class Comments :
    title = "성격유형검사지"
    mbti = "MBTI"
    decs = "본 검사는 MBTI를 기준으로 작성되었습니다.\n아래 버튼을 클릭하면 시작할 수 있습니다."
    q_tit = "Q%s."
    prev = "이전문항"
    next = "다음문항"
    start = "시작하기"
    result = "결과보기"
    result_tit = "내 성격유형은?"
    back = "돌아가기"
    error = "아직 선택되지 않았습니다."
    one = "그렇지 않다."
    two = "보통이다."
    three = "그렇다."
 
# 문항의 현재 숫자, 페이지 
question_num = 0 

# 옵셥
options = ["그렇지 않다", "보통이다", "그렇다"]  

# 초기화
def init():
    question_num = 0

# 현재 숫자 표시
def surveyNum(question_num):
    survey_num = Label(survey_frame, text=Comments.q_tit%question_num, anchor="w", bg="#ECF1F5", font=("Pretendard", 18, 'bold'), fg="#888888")
    survey_num.place(x=20, y=90, width=60, height=28)
  
# 질문 나열  
def questionText(question_num):
    question_text = Label(survey_frame, text=questions_data[question_num-1], font=("Pretendard", 20), wraplength=310, anchor="nw", justify="left", bg="#ECF1F5")
    question_text.place(x=20, y=138, width=310, height=84)
  
# 다음문항
def nextBtn():
    global question_num, questions_data
    question_num += 1
  
    # 테스트 페이지 표시
    survey_frame.place(x=0, y=0, width=350, height=750)
    
    # 프로그래스바 단계 설정
    ## 원래는 1이지만, max에 도달하면 다 채워지는 것이 아니라 아예 처음 단계로 돌아가기때문에 1에 가까운 숫자로 max로 채워주지 않는 것.
    survey_progress.step(0.9999999)
    
    surveyNum(question_num)
    questionText(question_num)
    
    # 버튼비활성화
    next_btn.config(state="normal")
    prev_btn.config(state="normal")
    if question_num >= len(questions_data):
        next_btn.config(state="disabled")
    elif question_num == 1:
        prev_btn.config(state="disabled")

 
# 이전문항
def prevBtn():
    global question_num
    question_num -= 1
    
    survey_progress.step(-0.9999999)

    surveyNum(question_num)
    questionText(question_num)
    
    # 버튼 비활성화
    prev_btn.config(state="normal")
    next_btn.config(state="normal")
    if question_num <= 1:
        prev_btn.config(state="disabled")
   
# 시작하기
def testStart():
    # 다음화면으로 넘어가는 것처럼 연출하기 위해서 place_forget을 사용해서 삭제해줌.
    main_title.place_forget()
    sub_title.place_forget()
    decs_txt.place_forget()
    start_btn.place_forget()
    back_btn.place_forget()
    
    nextBtn()
       


root = Tk()
root.title("MBTI TEST")
root.geometry("350x750")

main_title = Label(root, text=Comments.title, font=("helvetica", 25), bg="#ECF1F5")
main_title.place(x=87, y=178, width=175, height=31)


sub_title = Label(root, text=Comments.mbti, font=("helvetica", 45), bg="#ECF1F5")
sub_title.place(x=118, y=209, width=114, height=55)

decs_txt = Label(root, text=Comments.decs, font=("Pretendard", 12), bg="#ECF1F5", justify="center")
decs_txt.place(x=20, y=274, width=310, height=42)

start_btn = Button(root, text=Comments.start, relief=FLAT, font=("Pretendard", 12), command=testStart)
start_btn.place(x=20, y=346, width=310, height=50)

back_btn = Button(root, text=Comments.back, font=("Pretendard", 12), relief=FLAT )
back_btn.place(x=20, y=406, width=310, height=50)


# 테스트 화면
survey_frame = Frame(root, bg="#ECF1F5")

survey_progress = tkinter.ttk.Progressbar(survey_frame, maximum=16, mode="determinate")
survey_progress.place(x=20, y=50, width=310, height=10)

prev_btn = Button(survey_frame, text=Comments.prev, relief=FLAT, font=("Pretendard", 12), command=prevBtn)
prev_btn.place(x=222, y=90, width=54, height=28)

next_btn = Button(survey_frame, text=Comments.next, relief=FLAT, font=("Pretendard", 12), command=nextBtn)
next_btn.place(x=276, y=90, width=54, height=28)

# if question_num >= len(questions_data):
#     next_btn.config(state="disabled")
# else : next_btn.config(state="normal")
# if question_num <= 1:
#     prev_btn.config(state="disabled")
# else : prev_btn.config(state="normal")
      
root.configure(bg="#ECF1F5")
root.mainloop()
    
    