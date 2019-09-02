import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QTextEdit, QAction, QFileDialog, QDesktopWidget, QHBoxLayout, QTextBrowser, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QCoreApplication, Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self): 

        title = QLabel('Data Analysis', self)   #화면 Title
        title.setAlignment(Qt.AlignCenter)     

        font_t = title.font()                   #폰트 설정
        font_t.setFamily('Times new Roman')
        font_t.setBold(True)
        font_t.setPointSize(14)
        
        title.setFont(font_t)

        text = QTextBrowser(self)
        text.setText( "예시 문장 화면입니다.")


        self.resize(600, 600)   
        self.center()               #창을 모니터 화면 정중앙으로

        openFile = QAction(self)            
        openFile.triggered.connect(self.showDialog)

      
        btn1 = QPushButton('파일선택', self)        #Qdialog 이용하여 파일 선택
        btn1.setCheckable(True)
        btn1.clicked.connect(self.showDialog)

        uploadButton = QPushButton('등록')          #등록 버튼
        cancelButton = QPushButton('취소')          #취소 버튼

        hbox = QHBoxLayout()                        #수평 박스
        hbox.addStretch(1)
        hbox.addWidget(uploadButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        vbox = QVBoxLayout()                        #수직 박스 
        vbox.addWidget(title)
        vbox.addStretch(1.3)
        vbox.addWidget(text)
        vbox.addStretch(0.7)
        vbox.addWidget(btn1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        
        self.setLayout(vbox)
        self.show()

    def center(self):               #창 중앙에 띄우기
    
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())     
    


    def showDialog(self):       # 파일 선택 함수 
    
        fname = QFileDialog.getOpenFileName(self, '파일 선택', './')
'''
        if fname[0]:                    #불러온 파일 내용을 텍스트 박스에 띄우기
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)
'''

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())