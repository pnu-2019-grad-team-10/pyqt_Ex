import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QTextEdit, QAction, QFileDialog, QDesktopWidget, QHBoxLayout, QTextBrowser, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QCoreApplication, Qt


class MyApp(QWidget):

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()

        super().__init__()

        self.stylesheet = """

       

        QWidget
        {
        color: #b1b1b1;
        background-color: #323232;
        }

        QWidget:item:hover
        {
        background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);
        color: #000000;
        }

        QWidget:item:selected
        {
        background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
        }



        QWidget:disabled
        {
        color: #404040;
        background-color: #323232;
        }


        QWidget:focus
        {
        /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/
        }

        QLineEdit
        {
        background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);
        padding: 1px;
        border-style: solid;
        border: 1px solid #1e1e1e;
        border-radius: 5;
        }

        QPushButton
        {
        color: #b1b1b1;
        background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);
        border-width: 1px;
        border-color: #1e1e1e;
        border-style: solid;
        border-radius: 6;
        padding: 3px;
        font-size: 18px;
        padding-left: 5px;
        padding-right: 5px;
        }

        QPushButton:pressed
        {
        background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);
        }

        QComboBox
        {
        selection-background-color: #ffaa00;
        background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);
        border-style: solid;
        border: 1px solid #1e1e1e;
        border-radius: 5;
        }

        QComboBox:hover,QPushButton:hover
        {
        border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
        }


        QComboBox:on
        {
        padding-top: 3px;
        padding-left: 4px;
        background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);
        selection-background-color: #ffaa00;
        }

        QComboBox QAbstractItemView
        {
        border: 2px solid darkgray;
        selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
        }

        QComboBox::drop-down
        {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 15px;

        border-left-width: 0px;
        border-left-color: darkgray;
        border-left-style: solid; /* just a single line */
        border-top-right-radius: 3px; /* same radius as the QComboBox */
        border-bottom-right-radius: 3px;
        }

        QComboBox::down-arrow
        {
        image: url(:/down_arrow.png);
        }

       
        QTextEdit:focus
        {
        border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
        }

        

        QTextEdit
        {
        background-color: #242424;
        }

        QPlainTextEdit
        {
        background-color: #242424;
        }

        
        QMainWindow::separator
        {
        background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);
        color: white;
        padding-left: 4px;
        border: 1px solid #4c4c4c;
        spacing: 3px; /* spacing between items in the tool bar */
        }

        QMainWindow::separator:hover
        {

        background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);
        color: white;
        padding-left: 4px;
        border: 1px solid #6c6c6c;
        spacing: 3px; /* spacing between items in the tool bar */
        }

        

        """

        self.initUI()
        
        self.app.setStyleSheet(self.stylesheet)


    def initUI(self): 

        

        title = QLabel('Data Analysis', self)   #화면 Title
        title.setAlignment(Qt.AlignCenter)     

        font_t = title.font()                   #폰트 설정
        font_t.setFamily('Times new Roman')
        font_t.setBold(True)
        font_t.setPointSize(14)
        
        title.setFont(font_t)

        ex_text = QTextBrowser(self)
        ex_text.setText( "예시 문장 화면입니다.")

       

        self.label= QLabel()
        self.label.setText("파일경로")

        #label2 = QTextBrowser(self)

        #self.label = QLabel()
        #self.label.setText("파일 경로")

        #self.label2 = QTextBrowser()
        
        self.resize(600, 600)   
        self.center()               #창을 모니터 화면 정중앙으로

        openFile = QAction(self)            
        openFile.triggered.connect(self.showDialog)

      
        btn1 = QPushButton('파일선택', self)        #Qdialog 이용하여 파일 선택
        btn1.setCheckable(True)
        btn1.clicked.connect(self.showDialog)
        

        uploadButton = QPushButton('등록')          #등록 버튼
        cancelButton = QPushButton('취소')          #취소 버
   

        hbox = QHBoxLayout()                        #수평 박스
        hbox.addStretch(1)
        hbox.addWidget(uploadButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        vbox = QVBoxLayout()                        #수직 박스 
        vbox.addWidget(title)
        vbox.addStretch(1.3)
        vbox.addWidget(ex_text)
        vbox.addWidget(self.label)
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
        self.label.setText(fname[0])
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