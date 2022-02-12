import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("beta.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn1_clicked)
        
        # self.setGeometry(500,200,400,400)
        self.setWindowTitle('GoMar_beta_ver_1')
        self.setWindowIcon(QIcon('bitcoin_icon.png'))
        
        # btn1 = QPushButton('자~ 드가자',self)
        # btn1.move(30,30)
        # btn1.clicked.connect(self.btn1_clicked)
        
        # btn2 = QPushButton('자~ 도망가자',self)
        # btn2.move(200,30)
        
        
        
    def btn1_clicked(self):
        print('풀 매수 !!!')
 
app = QApplication(sys.argv) # QApplication클래스에서 이벤트루프 설정할 메소드 호출할 수 있다.

# btn = QPushButton('Hello')
# btn.show()

window = MyWindow()
window.show()

# label = QLabel("Hello")
# label.show()

app.exec_() # 이벤트 루프