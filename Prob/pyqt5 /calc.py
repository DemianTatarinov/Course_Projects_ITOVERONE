import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtGui import QFont, QPalette


class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.my_input = []
        self.operand_1 = []
        self.operand_2 = []

    def initUI(self):
        self.setGeometry(300, 300, 360, 225)
        self.setWindowTitle('Калькулятор')
        self.setStyleSheet('background : grey')

        self.label = QLabel(self)
        self.label.setFont(QFont('timer', 30))
        self.label.setText('0')
        self.label.setBackgroundRole(QPalette.Dark)
        self.label.resize(360, 50)
        self.move(0, 0)

        self.num_1 = QPushButton('1', self)
        self.num_1.resize(70, 35)
        self.num_1.move(5, 70)
        self.num_1.setStyleSheet("QPushButton { background-color: white}"
                                 "QPushButton:pressed { background-color: grey }")

        self.num_2 = QPushButton('2', self)
        self.num_2.resize(70, 35)
        self.num_2.move(75, 70)
        self.num_2.setStyleSheet("QPushButton { background-color: white}"
                                 "QPushButton:pressed { background-color: grey }")

        self.num_3 = QPushButton('3', self)
        self.num_3.resize(70, 35)
        self.num_3.move(145, 70)
        self.num_3.setStyleSheet("QPushButton { background-color: white}"
                                 "QPushButton:pressed { background-color: grey }")

        self.div_ = QPushButton('/', self)
        self.div_.resize(70, 35)
        self.div_.move(215, 70)
        self.div_.setStyleSheet("QPushButton { background-color: orange}"
                                "QPushButton:pressed { background-color: grey }")

        self.canc = QPushButton('C', self)
        self.canc.resize(70, 35)
        self.canc.move(285, 70)
        self.canc.setStyleSheet("QPushButton { background-color: red}"
                                "QPushButton:pressed { background-color: grey }")

        self.num_4 = QPushButton('4', self)
        self.num_4.resize(70, 35)
        self.num_4.move(5, 105)
        self.num_4.setStyleSheet("QPushButton { background-color: white}"
                                 "QPushButton:pressed { background-color: grey }")

        self.num_5 = QPushButton('5', self)
        self.num_5.resize(70, 35)
        self.num_5.move(75, 105)
        self.num_5.setStyleSheet("QPushButton { background-color: white}"
                                 "QPushButton:pressed { background-color: grey }")

        self.num_6 = QPushButton('6', self)
        self.num_6.resize(70, 35)
        self.num_6.move(145, 105)
        self.num_6.setStyleSheet("QPushButton { background-color: white}"
                                 "QPushButton:pressed { background-color: grey }")

        self.mul = QPushButton('*', self)
        self.mul.resize(70, 35)
        self.mul.move(215, 105)
        self.mul.setStyleSheet("QPushButton { background-color: orange}"
                               "QPushButton:pressed { background-color: grey }")

        self.step = QPushButton('^', self)
        self.step.resize(70, 35)
        self.step.move(285, 105)
        self.step.setStyleSheet("QPushButton { background-color: white}"
                                "QPushButton:pressed { background-color: grey }")

        self.num_7 = QPushButton('7', self)
        self.num_7.resize(70, 35)
        self.num_7.move(5, 140)
        self.num_7.setStyleSheet("QPushButton { background-color: white}"
                                 "QPushButton:pressed { background-color: grey }")

        self.num_8 = QPushButton('8', self)
        self.num_8.resize(70, 35)
        self.num_8.move(75, 140)
        self.num_8.setStyleSheet("QPushButton { background-color: white}"
                                 "QPushButton:pressed { background-color: grey }")

        self.num_9 = QPushButton('9', self)
        self.num_9.resize(70, 35)
        self.num_9.move(145, 140)
        self.num_9.setStyleSheet("QPushButton { background-color: white}"
                                 "QPushButton:pressed { background-color: grey }")

        self.minus = QPushButton('-', self)
        self.minus.resize(70, 35)
        self.minus.move(215, 140)
        self.minus.setStyleSheet("QPushButton { background-color: orange}"
                                 "QPushButton:pressed { background-color: grey }")

        self.sqr = QPushButton('x√ ', self)
        self.sqr.resize(70, 35)
        self.sqr.move(285, 140)
        self.sqr.setStyleSheet("QPushButton { background-color: white}"
                               "QPushButton:pressed { background-color: grey }")

        self.num_0 = QPushButton('0', self)
        self.num_0.resize(70, 35)
        self.num_0.move(5, 175)
        self.num_0.setStyleSheet("QPushButton { background-color: white}"
                                 "QPushButton:pressed { background-color: grey }")

        self.dot_key = QPushButton('.', self)
        self.dot_key.resize(70, 35)
        self.dot_key.move(75, 175)
        self.dot_key.setStyleSheet("QPushButton { background-color: white}"
                                   "QPushButton:pressed { background-color: grey }")

        self.is_ = QPushButton('=', self)
        self.is_.resize(70, 35)
        self.is_.move(145, 175)
        self.is_.setStyleSheet("QPushButton { background-color: green}"
                               "QPushButton:pressed { background-color: grey }")

        self.plus = QPushButton('+', self)
        self.plus.resize(70, 35)
        self.plus.move(215, 175)
        self.plus.setStyleSheet("QPushButton { background-color: orange}"
                                "QPushButton:pressed { background-color: grey }")

        self.per = QPushButton('%', self)
        self.per.resize(70, 35)
        self.per.move(285, 175)
        self.per.setStyleSheet("QPushButton { background-color: white}"
                               "QPushButton:pressed { background-color: grey }")

        self.num_1.clicked.connect(self.one)
        self.num_2.clicked.connect(self.two)
        self.num_3.clicked.connect(self.three)
        self.num_4.clicked.connect(self.four)
        self.num_5.clicked.connect(self.five)
        self.num_6.clicked.connect(self.six)
        self.num_7.clicked.connect(self.seven)
        self.num_8.clicked.connect(self.eight)
        self.num_9.clicked.connect(self.nine)
        self.num_0.clicked.connect(self.zero)
        self.dot_key.clicked.connect(self.dot)
        self.plus.clicked.connect(self.plus_1)
        self.minus.clicked.connect(self.minus_1)
        self.div_.clicked.connect(self.div_1)
        self.mul.clicked.connect(self.mul_1)
        self.sqr.clicked.connect(self.sqr_1)
        self.per.clicked.connect(self.per_1)
        self.step.clicked.connect(self.step_1)
        self.is_.clicked.connect(self.is_1)
        self.canc.clicked.connect(self.clear)

    def enterValue(self):
        if self.label.text() == '0':
            self.label.setText('')
        elif self.label.text() == str(self.is_1):
            self.label.setText('')
        elif self.label.text() == str(self.operand_1):
            self.label.setText('')
        elif self.label.text() == str(self.operand_2):
            self.label.setText('')

        self.label.setText(self.label.text() + self.my_input)

    def one(self):
        self.my_input = '1'
        self.enterValue()

    def two(self):
        self.my_input = '2'
        self.enterValue()

    def three(self):
        self.my_input = '3'
        self.enterValue()

    def four(self):
        self.my_input = '4'
        self.enterValue()

    def five(self):
        self.my_input = '5'
        self.enterValue()

    def six(self):
        self.my_input = '6'
        self.enterValue()

    def seven(self):
        self.my_input = '7'
        self.enterValue()

    def eight(self):
        self.my_input = '8'
        self.enterValue()

    def nine(self):
        self.my_input = '9'
        self.enterValue()

    def zero(self):
        self.my_input = '0'
        self.enterValue()

    def dot(self):
        if '.' in self.label.text():
            if self.label.text() == str(self.operand_1):
                self.label.setText('0.')
            else:
                pass
        else:
            self.my_input = '.'
            self.enterValue()

    def float_or_int(self):
        if '.' in self.label.text():
            if self.label.text()[0] == '.':
                self.label.setText('0' + self.label.text())
            return float(self.label.text())

        else:
            return int(self.label.text())

    def plus_1(self):
        self.operation = '+'
        self.operand_1 = self.float_or_int()

    def minus_1(self):
        self.operation = '-'
        self.operand_1 = self.float_or_int()

    def mul_1(self):
        self.operation = '*'
        self.operand_1 = self.float_or_int()

    def div_1(self):
        self.operation = '/'
        self.operand_1 = self.float_or_int()

    def per_1(self):  # %
        self.operation = '%'
        self.operand_1 = self.float_or_int()

    def sqr_1(self):  # √
        self.operation = '√'
        self.operand_1 = self.float_or_int()

    def step_1(self):
        self.operation = '^'
        self.operand_1 = self.float_or_int()

    def is_1(self):
        self.operand_2 = self.float_or_int()
        if self.operation == '+':
            self.is_1 = self.operand_1 + self.operand_2
        elif self.operation == '-':
            self.is_1 = self.operand_1 - self.operand_2
        elif self.operation == '/':
            if self.operand_2 == 0:
                self.is_1 = 'error'
            else:
                self.is_1 = self.operand_1 / self.operand_2
        elif self.operation == '*':
            self.is_1 = self.operand_1 * self.operand_2
        elif self.operation == '%':
            self.is_1 = self.operand_2 * self.operand_1 / 100
        elif self.operation == '√':
            self.is_1 = self.operand_1 ** (1 / self.operand_2)
        elif self.operation == '^':
            self.is_1 = self.operand_1 ** (self.operand_2)
        self.label.setText(str(self.is_1))

    def clear(self):
        self.label.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())