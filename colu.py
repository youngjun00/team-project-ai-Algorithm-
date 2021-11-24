import tkinter as tkt                               #GUI 모듈을 포함시킴

root = tkt.Tk()                                     # 가장 기본적인 윈도우root 생성
root.title("계산기")                                # 윈도우 창 타이틀 생성
root.resizable(0, 0)                                # 윈도우 크기 고정한다
root.wm_attributes("-topmost", 1)                   # 화면 상단에 유지된다.

 # 변수 선언
equa = ""
equation = tkt.StringVar()

calculation = tkt.Label(root, textvariable=equation)
equation.set("계산식을 입력하세요 : ")              #입력 위치
calculation.grid(row=3, columnspan=8)              #객체 배치 담당


def btnPress(num):               #번호 저장 및 설정
     global equa
     equa = equa + str(num)
     equation.set(equa)

def EqualPress():                #연산자 설정 및 결과값 생성
     global equa
     total = str(eval(equa))
     equation.set(total)
     equa = ""

def ClearPress():                #계산기 클리어
     global equa
     equa = ""
     equation.set("")

def LaplcePress():
     global equa
     total = str((equa))
     equation.set(total)
     equa = ""

#####################
#해당 윈도우 버튼 생성#
#####################

#기본계산기 버튼#
################

Button0 = tkt.Button(root, text="0", bg='white',command=lambda: btnPress(0), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button0.grid(row=7, column=2, padx=10, pady=10)
Button1 = tkt.Button(root, text="1", bg='white',command=lambda: btnPress(1), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button1.grid(row=4, column=1, padx=10, pady=10)
Button2 = tkt.Button(root, text="2", bg='white',command=lambda: btnPress(2), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button2.grid(row=4, column=2, padx=10, pady=10)
Button3 = tkt.Button(root, text="3", bg='white',command=lambda: btnPress(3), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button3.grid(row=4, column=3, padx=10, pady=10)
Button4 = tkt.Button(root, text="4", bg='white',command=lambda: btnPress(4), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button4.grid(row=5, column=1, padx=10, pady=10)
Button5 = tkt.Button(root, text="5", bg='white',command=lambda: btnPress(5), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button5.grid(row=5, column=2, padx=10, pady=10)
Button6 = tkt.Button(root, text="6", bg='white',command=lambda: btnPress(6), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button6.grid(row=5, column=3, padx=10, pady=10)
Button7 = tkt.Button(root, text="7", bg='white',command=lambda: btnPress(7), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button7.grid(row=6, column=1, padx=10, pady=10)
Button8 = tkt.Button(root, text="8", bg='white',command=lambda: btnPress(8), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button8.grid(row=6, column=2, padx=10, pady=10)
Button9 = tkt.Button(root, text="9", bg='white',command=lambda: btnPress(9), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button9.grid(row=6, column=3, padx=10, pady=10)
Plus = tkt.Button(root, text="+", bg='white',command=lambda: btnPress("+"), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Plus.grid(row=4, column=4, padx=10, pady=10)
Minus = tkt.Button(root, text="-", bg='white',command=lambda: btnPress("-"), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Minus.grid(row=5, column=4, padx=10, pady=10)
Multiply = tkt.Button(root, text="*", bg='white',command=lambda: btnPress("*"), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Multiply.grid(row=6, column=4, padx=10, pady=10)
Divide = tkt.Button(root, text="/", bg='white',command=lambda: btnPress("/"), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Divide.grid(row=7, column=4, padx=10, pady=10)
Equal = tkt.Button(root, text="=", bg='white',command=EqualPress, height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Equal.grid(row=7, column=3, padx=10, pady=10)
Clear = tkt.Button(root, text="C", bg='white',command=ClearPress, height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Clear.grid(row=7, column=1, padx=10, pady=10)

# 라플라스 버튼생성#

Laplace1 = tkt.Button(root, text="a", bg='white',command=lambda: btnPress("a="), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Laplace1.grid(row=4, column=5, padx=10, pady=10)
Laplace2 = tkt.Button(root, text="w", bg='white',command=lambda: btnPress("w="), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Laplace2.grid(row=5, column=5, padx=10, pady=10)
Laplace3 = tkt.Button(root, text="n", bg='white',command=lambda: btnPress("n="), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Laplace3.grid(row=6, column=5, padx=10, pady=10)
Laplace4 = tkt.Button(root, text="1/s", bg='white',command=lambda: btnPress("1/s"), height=1, width=10, borderwidth=1, relief=tkt.SOLID)
Laplace4.grid(row=1, column=1, padx=10, pady=10)
Laplace5 = tkt.Button(root, text="n!/(s+a)ⁿ+¹", bg='white',command=lambda: btnPress("n!/(s+a)ⁿ+¹"), height=1, width=10, borderwidth=1, relief=tkt.SOLID, )
Laplace5.grid(row=1, column=2, padx=10, pady=10)
Laplace6 = tkt.Button(root, text="w/s²+w²", bg='white',command=lambda: btnPress("w/s²+w²"), height=1, width=10, borderwidth=1, relief=tkt.SOLID, )
Laplace6.grid(row=1, column=3, padx=10, pady=10)
Laplace7 = tkt.Button(root, text="s/s²+w²", bg='white',command=lambda: btnPress("s/s²+w²"), height=1, width=10, borderwidth=1, relief=tkt.SOLID, )
Laplace7.grid(row=1, column=4, padx=10, pady=10)
Laplace8 = tkt.Button(root, text="a/s²-a²", bg='white',command=lambda: btnPress("a/s²-a²"), height=1, width=10, borderwidth=1, relief=tkt.SOLID, )
Laplace8.grid(row=1, column=5, padx=10, pady=10)
Laplace9 = tkt.Button(root, text="s/s²-a²", bg='white',command=lambda: btnPress("s/s²-a²"), height=1, width=10, borderwidth=1, relief=tkt.SOLID, )
Laplace9.grid(row=2, column=1, padx=10, pady=10)
Laplace = tkt.Button(root, text="L", bg='white',command=lambda: LaplcePress("L"), height=1, width=7, borderwidth=1, relief=tkt.SOLID, )
Laplace.grid(row=7, column=5, padx=10, pady=10)
Laplace10 = tkt.Button(root, text="2ws/(s²+w²)²", bg='white',command=lambda: btnPress("2ws/(s²+w²)²"), height=1, width=10, borderwidth=1, relief=tkt.SOLID, )
Laplace10.grid(row=2, column=2, padx=10, pady=10)
Laplace11 = tkt.Button(root, text="s²-w²/(s²+w²)²", bg='white',command=lambda: btnPress("s²-w²/(s²+w²)²"), height=1, width=10, borderwidth=1, relief=tkt.SOLID, )
Laplace11.grid(row=2, column=3, padx=10, pady=10)
Laplace12 = tkt.Button(root, text="w/(s+a)²+w²", bg='white',command=lambda: btnPress("w/(s+a)²+w²"), height=1, width=10, borderwidth=1, relief=tkt.SOLID, )
Laplace12.grid(row=2, column=4, padx=10, pady=10)
Laplace13 = tkt.Button(root, text="s+a/(s+a)²+w²", bg='white',command=lambda: btnPress("s+a/(s+a)²+w²"), height=1, width=10, borderwidth=1, relief=tkt.SOLID, )
Laplace13.grid(row=2, column=5, padx=10, pady=10)


root.mainloop()                         #이벤트 메세지 루프
