# 목표: 메인페이지에서 시작하기 누르면 테스트 시작, 한 화면에 질문이 하나씩 나오게 구현, 총 3개의 옵션으로 구현 (그렇다 보통이다 아니다), 결과는 각 유형별 평균 퍼센트로 나타내기

# 보안점: 이전문항으로 갔을 때 다시 다음버튼을 누르게 된다면 점수가 더 추가가 됨.;;
# 나중에 데이터를 저장할 수 있는 것을 배우면 보안해보자

from tkinter import *
import tkinter.ttk
import json

root = Tk()
root.title("MBTI TEST")
root.geometry("350x750")

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
    next_shot = "다음"
    start = "시작하기"
    result = "결과보기"
    result_tit = "내 성격유형은?"
    back = "돌아가기"
    error = "아직 선택되지 않았습니다."
    one = "그렇지 않다."
    two = "보통이다."
    three = "그렇다."
    test_num = "I: %s, E:%s \n S:%s, N:%s \n F:%s, T:%s \n P:%s, J:%s"
 
# 문항의 현재 숫자, 페이지 
question_num = 0 
select_score = []
scores = {}

# 질문과 옵션 자료 넣어두기
question_txt = []
options = []
for question_data in questions_data: 
    question_txt.append(question_data["question"])
    options.append(question_data["options"])

# StringVar로 하면 처음에 모두 선택이 되어있음. value값을 임의로 설정해줘야만 하나만 선택되어 있음.
var = StringVar(value="1")
var.set("1")

# 초기화
def init():
    global question_num, scores
    question_num = 0
    scores = {
    "E": 0, "I": 0, 
    "S": 0, "N": 0,
    "T": 0, "F": 0,
    "J": 0, "P": 0
}
        
# 옵션의 값 더하기
def addScores(question_num, select_option):
    global scores
    option_select = options[question_num - 1]
    
    # 라디오 셀렉한 옵션의 리스트를 그대로 담기.
    selected_value = option_select.get(select_option, {})

    # key 값으로 value 찾아서 계산.
    for mbti_type, score in selected_value.items():
        scores[mbti_type] += score

    # 값 계산이 보이기 위해 일단 둠.
    test = Label(survey_frame, text=str(scores), wraplength=310)
    test.place(x=20, y=550)


# 현재 숫자 표시
def surveyNum(question_num):
    survey_num = Label(survey_frame, text=Comments.q_tit%question_num, anchor="w", bg="#ECF1F5", font=("Pretendard", 18, 'bold'), fg="#888888")
    survey_num.place(x=20, y=90, width=60, height=28)

# 질문 나열  
def questionText(question_num):
    question_text = Label(survey_frame, text=question_txt[question_num-1], font=("Pretendard", 20), wraplength=310, anchor="nw", justify="left", bg="#ECF1F5")
    question_text.place(x=20, y=138, width=310, height=84) 
    
    # 옵션 버튼 만들기
    option_buttons = []
    for idx, option in enumerate(options[question_num - 1]):
        option_btn = Radiobutton(survey_frame, text=option, variable=var, value=option, anchor='w', bg="white", font=("Pretendard", 18))
        option_btn.place(x=20, y=252 + (70 * idx), width=310, height=50)
        option_buttons.append(option_btn)

    option_buttons[1].invoke() 


# 결과보기
def resultPage():
    # 결과 페이지 표시
    result_frame.place(x=0, y=0, width=350, height=750)
    
    # 테스트 페이지 삭제 
    survey_frame.place_forget()
    
  
# 다음문항
def nextBtn():
    global question_num, questions_data
    question_num += 1

    selected_option = var.get()

    
    # 테스트 페이지 표시
    survey_frame.place(x=0, y=0, width=350, height=750)
    
    # 프로그래스바 단계 설정
    ## 원래는 1이지만, max에 도달하면 다 채워지는 것이 아니라 아예 처음 단계로 돌아가기때문에 1에 가까운 숫자로 max로 채워주지 않는 것.
    survey_progress.step(0.9999999)
    
    surveyNum(question_num)
    questionText(question_num)
    
    # 버튼비활성화
    # 마지막 문항에서는 다음버튼 > 결과보기로 표시 변환 되어야함.
    next_btn.config(state="normal")
    prev_btn.config(state="normal")
    big_next.config(text=Comments.next_shot, command=nextBtn)
    
    if question_num >= len(questions_data):
        next_btn.config(state="disabled")
        big_next.config(text=Comments.result, command=resultPage)
    elif question_num == 1:
        prev_btn.config(state="disabled")
        
    addScores(question_num, selected_option)
    
        

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
    init()
        




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


##### 테스트 화면 #####
survey_frame = Frame(root, bg="#ECF1F5")

survey_progress = tkinter.ttk.Progressbar(survey_frame, maximum=16, mode="determinate")
survey_progress.place(x=20, y=50, width=310, height=10)

prev_btn = Button(survey_frame, text=Comments.prev, relief=FLAT, font=("Pretendard", 12), command=prevBtn)
prev_btn.place(x=222, y=90, width=54, height=28)

next_btn = Button(survey_frame, text=Comments.next, relief=FLAT, font=("Pretendard", 12), command=nextBtn)
next_btn.place(x=276, y=90, width=54, height=28)


# 다음 버튼
big_next = Button(survey_frame, text=Comments.next_shot, font=("Pretendard", 15), bg="gray", command=nextBtn)
big_next.place(x=20, y=472, width=310, height=50) 


##### 결과 페이지 #####
result_frame = Frame(root, bg="#ECF1F5")  
      
root.configure(bg="#ECF1F5")
root.mainloop()
    
    