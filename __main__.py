from PyQt5 import QtWidgets,QtCore,uic
import threading,pyautogui,win32api,time

pyautogui.FAILSAFE = False
class Position:
	def __init__(self,x,y):
		self.x = x
		self.y = y

class AutoClicker(QtWidgets.QMainWindow):
	leftClick = 1

	rightClick = 2
	def __init__(self):
		super(AutoClicker,self).__init__()
		uic.loadUi("AutoClicker.ui",self)
		self.isSelecting = False
		self.clicks = []
		self.selectAreaButton.clicked.connect(self.selectArea)
		self.isClicking = False
		self.pos = 0
		self.startButton.clicked.connect(self.__startClick__)
		self.selectThread = threading.Thread(target=self.__selectPos__,daemon=True).start()

	def selectArea(self):
		if self.isSelecting == False:
			self.isSelecting = True
			self.showMinimized()

	def __selectPos__(self):
		while True:
		    if win32api.GetAsyncKeyState(1) != 0 and self.isSelecting == True:
			    self.isSelecting = False
			    self.showNormal()
			    self.clicks.append(Position(pyautogui.position().x,pyautogui.position().y))

	def start(self):
		self.__startClick__()
	
	def __startClick__(self):
		self.timer_1 = QtCore.QTimer()
		self.timer_1.timeout.connect(self.__startClick__)
		
		pyautogui.leftClick(x=self.clicks[self.pos].x,y=self.clicks[self.pos].y)
		self.pos += 1

		if self.pos == len(self.clicks):
			self.pos = 0


		if win32api.GetAsyncKeyState(0x78) != 0:
			self.timer_1.stop()
			self.showNormal()

		self.showMinimized()
		self.timer_1.start(1)



	


			



	



		

			






if __name__ == '__main__':
	app = QtWidgets.QApplication([])
	autocl = AutoClicker()
	autocl.show()
	app.exec_()