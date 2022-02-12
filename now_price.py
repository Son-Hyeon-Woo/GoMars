import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pykorbit

form_class = uic.loadUiType("now_price.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn1_clicked)
        
        self.setWindowTitle('GoMar_beta_ver_1')
        self.setWindowIcon(QIcon('bitcoin_icon.png'))
        
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)
    
        
    def btn1_clicked(self):
        print('조회 버튼 클릭')
        price = pykorbit.get_current_price("BTC")
        print(price)
        self.lineEdit.setText(str(price))
        
    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString('hh:mm:ss')
        self.statusBar().showMesseage(str_time)
 
app = QApplication(sys.argv) # QApplication클래스에서 이벤트루프 설정할 메소드 호출할 수 있다.
window = MyWindow()
window.show()
app.exec_() # 이벤트 루프