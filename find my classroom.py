# 6305 นายจิรกิตต์ มีทรัพย์ประเสริฐ
# 6306 นางสาวจิรษิกา กิจสนาพิทักษ์
# 6308 นางสาวฐาปนีย์ เรืองรองวรรษ
# 6314 นางสาวพิชญ์สินี อังศุชัยกิจ

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# set main window
app = QApplication(sys.argv)
win = QMainWindow()
win.setWindowTitle('Find My Classroom')
win.setGeometry(300, 300, 450, 200)

# set sub window
sub = QMdiSubWindow()
sub.setWindowTitle('Found My Classroom')
sub.setGeometry(300, 50, 600, 650)

# set Ui main window
mbg = QPixmap('bg-main.jpg').scaled(450, 200)
Mbg = QLabel(win)
Mbg.setPixmap(mbg)
Mbg.setGeometry(0, 0, 450, 200)

topic = QLabel(win)
topic.setText('Where\'s my classroom')
topic.setFont(QFont('Times', 30))
topic.setStyleSheet('color: white;')
topic.adjustSize()
topic.move(50, 20)

search = QLineEdit(win)
search.setGeometry(100, 80, 250, 30)

submit = QPushButton(win)
submit.setText("Submit")
submit.setGeometry(180, 130, 70, 40)
submit.setFont(QFont('Times', 15))
submit.setStyleSheet('QPushButton {background-color: #57b9fa; color: black;}')

# set Ui sub window
sbg = QPixmap('bg-sub.jpg').scaled(600, 650)
Sbg = QLabel(sub)
Sbg.setPixmap(sbg)
Sbg.setGeometry(0, 0, 600, 650)

head = QLabel(sub)
head.setText('This is My Classroom')
head.setFont(QFont('Times', 45))
head.setStyleSheet('color: white;')
head.adjustSize()
head.move(40, 0)

building = QLabel(sub)
building.setText('Building :')
building.setFont(QFont('Times', 20))
building.setStyleSheet('color: white;')
building.adjustSize()
building.move(100, 80)

buildings = QLabel(sub)
buildings.setFont(QFont('Times', 20))
buildings.setStyleSheet('color: white;')
buildings.setGeometry(220, 85, 50, 20)

floor = QLabel(sub)
floor.setText('Floor :')
floor.setFont(QFont('Times', 20))
floor.setStyleSheet('color: white;')
floor.adjustSize()
floor.move(100, 120)

floors = QLabel(sub)
floors.setFont(QFont('Times', 20))
floors.setStyleSheet('color: white;')
floors.setGeometry(185, 125, 50, 20)

room = QLabel(sub)
room.setText('Room :')
room.setFont(QFont('Times', 20))
room.setStyleSheet('color: white;')
room.adjustSize()
room.move(100, 160)

rooms = QLabel(sub)
rooms.setFont(QFont('Times', 20))
rooms.setStyleSheet('color: white;')
rooms.setGeometry(195, 165, 50, 20)

back = QPushButton(sub)
back.setGeometry(360, 90, 100, 100)
back.setText('Back')
back.setFont(QFont('Times', 20))
back.setStyleSheet('QPushButton {background-color: #57b9fa; color: black;}')

kmutt = QPixmap('MAP.jpg')
width = kmutt.size().width()
height = kmutt.size().height()

Map = QLabel(sub)
Map.setPixmap(kmutt)
Map.setGeometry(55, 220, width, height)

mark = QPixmap('mark.png')
width = mark.size().width()
height = mark.size().height()

marks = QLabel(sub)
marks.setGeometry(0, 0, 100, 100)


# location building
def location():
    find = search.text().split()
    Bigfind = find[0].upper()
    file = open("gps.txt", "r")
    for i in range(0, 13):
        lines = file.readline().split()
        if lines[0] == Bigfind or lines[1] == Bigfind:
            b = lines[1]
            x = lines[2]
            y = lines[3]
            break
    file.close()
    return (x, y, b, find)


def submits():
    data = location()
    if len(data[3]) == 2:
        floors.setText(data[3][1][0])
        rooms.setText(data[3][1])
        buildings.setText(data[2])
        marks.setPixmap(mark)
        marks.move(int(data[0]), int(data[1]))
    else:
        floors.setText('-')
        rooms.setText('-')
        buildings.setText(data[2])
        marks.setPixmap(mark)
        marks.move(int(data[0]), int(data[1]))
    win.close()
    sub.show()


def backs():
    sub.close()
    win.show()


submit.clicked.connect(submits)
back.clicked.connect(backs)

win.show()
sys.exit(app.exec_())
