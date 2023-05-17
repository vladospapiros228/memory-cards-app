#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox, QRadioButton, QButtonGroup
from random import shuffle


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


questions_list = []
questions_list.append(Question('Государственный язык Бразилии', 'Португальский','Английский', 'Испанский','Бразильский'))
questions_list.append(Question('Каого цвета нет на флаге России?','Зелёный','Красный','Белый','Синий'))
questions_list.append(Question('Национальная хижина якутов','Ураса','Юрта','Иглу','Хата'))


app = QApplication([])

window.setWindowTitle('Memo Card')

btn_ok = QPushButton('Ответить')
lb_question = QLabel('Самый сложный вопрос в мире')

RadioGroupoBox = QGroupBox('Варианты ответов')

rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')


RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupoBox.setLayout(layout_ans1)


AnsGroupBox = QGroupBox('Результаты теста')
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignLeft))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()


layout_line1.addWidget(lb_question, alignment=(Qt.AlignVCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupoBox)
#layout_line3.addWidget(btn_ok, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addWidget(btn_OK)


layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)

window.setLayout(layout_card)
window.show()
app.exec()