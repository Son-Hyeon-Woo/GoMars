import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import pykorbit

form_class = uic.loadUiType("now_price.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn1_clicked)
        
        self.setWindowTitle('GoMar_beta_ver_1')
        self.setWindowIcon(QIcon('bitcoin_icon.png'))
    
        
    def btn1_clicked(self):
        print('조회 버튼 클릭')
        price = pykorbit.get_current_price("BTC")
        print(price)
        self.lineEdit.setText(str(price))
 
app = QApplication(sys.argv) # QApplication클래스에서 이벤트루프 설정할 메소드 호출할 수 있다.
window = MyWindow()
window.show()
app.exec_() # 이벤트 루프