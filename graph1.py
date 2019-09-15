import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
from matplotlib.widgets import TextBox, Button

fig, ax = plt.subplots()            #그래프 
plt.subplots_adjust(bottom=0.35)
initial_text = "Your PTP is 343.22ms, which is estimated to 0.125 Alcohol-in-blood percentage."

#뒤로가기 
class Prev(object):
    def prev(self, event):
        print("뒤로가기") #이전 페이지로 돌아가는 함수 작성

a = np.arange(0, 2, 0.2)        #범위

x = [1.0]                       #반환 값 
y = [1.0]

font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/NanumGothic.ttf").get_name()
rc('font', family=font_name)


fig.suptitle("타자 속도", fontsize = 16, fontweight='bold')     #타이틀제목
plt.xlabel("x")    #x축 라벨
plt.ylabel("y")    #y축 라벨

plt.xticks(fontsize = 12, color = '#FF8000')          #눈금 색, 폰트크기
plt.yticks(fontsize = 12, color = '#FF8000')

plt.scatter(x, y, c = 'b', s = 150, marker="*", label = 'dot')   #점 그래프
plt.plot(a, a**2, color='#FF8000', linewidth=2, label = 'line graph')   #선 그래프 
plt.grid(b=True, which ='major', axis='x')      #그리드 그리기


#박스 설정
box = {
    'facecolor' : '.85',
    'edgecolor' : 'r',
    'boxstyle'  : 'round'
}


plt.text(1.05, 0.8, 'Your PTP : 343.22ms', bbox = box)

#텍스트 박스 
axbox = plt.axes([0.1, 0.16, 0.8, 0.09])
text_box = TextBox(axbox, '', initial=initial_text)


''' 화살표 표시(error)
plt.plot([1.0], [1.0])
plt.annotate('Your PTP : 343.22ms' xy=(1.0, 1.0), xytext=(0.7, 0.8),
            arrowprops=dict(facecolor='black', shrink=0.01),
            )
'''

callback = Prev()
axprev = plt.axes([0.80, 0.05, 0.1, 0.075])
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)

plt.legend()
plt.show()