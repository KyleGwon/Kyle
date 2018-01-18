from graphics import *
import random
import time
class LeftPaddle:
	def __init__(self, win, lPaddleDimensions):
		self.win = win
		self.lPaddleWidth = lPaddleDimensions[0]
		self.lPaddleHeight = lPaddleDimensions[1]
		lP1 = Point(0, self.win.getHeight() / 2 - self.lPaddleHeight / 2)
		lP2 = Point(self.lPaddleWidth, self.win.getHeight() / 2 + self.lPaddleHeight / 2)
		lPaddle = Rectangle(lP1, lP2)
		lPaddle.setFill("black")
		lPaddle.draw(self.win)
		self.lPaddle = lPaddle
	def getLPaddle(self):
		return self.lPaddle
	def getP1Y(self):
		return self.lPaddle.getP1().getY()
	def getP2Y(self):
		return self.lPaddle.getP2().getY()
class RightPaddle:
	def __init__(self, win, rPaddleDimensions):
		self.win = win
		self.rPaddleWidth = rPaddleDimensions[0]
		self.rPaddleHeight = rPaddleDimensions[1]
		rP1 = Point(self.win.getWidth() - self.rPaddleWidth, self.win.getHeight() / 2 - self.rPaddleHeight / 2)
		rP2 = Point(self.win.getWidth(), self.win.getHeight() / 2 + self.rPaddleHeight / 2)
		rPaddle = Rectangle(rP1, rP2)
		rPaddle.setFill("black")
		rPaddle.draw(self.win)
		self.rPaddle = rPaddle
	def getRPaddle(self):
		return self.rPaddle
	def getP1Y(self):
		return self.rPaddle.getP1().getY()
	def getP2Y(self):
		return self.rPaddle.getP2().getY()
class Ball:
	def __init__(self, win, center, radius):
		self.win = win
		self.center = center
		self.radius = radius
		ball = Circle(self.center, self.radius)
		ball.setFill("black")
		ball.draw(self.win)
		self.ball = ball
	def getBall(self):
		return self.ball
	def getBallXCord():
		return self.ball.getX()
	def getBallYCord():
		return self.ball.getY()
def main():
		width = 1600
		height = 800
		win = GraphWin("Turtle Pong", width, height)
		dimensions = [width / 100, height / 8]
		leftPaddle = LeftPaddle(win, dimensions)
		rightPaddle = RightPaddle(win, dimensions)
		lPaddle = leftPaddle.getLPaddle()
		rPaddle = rightPaddle.getRPaddle()
		ballCenter = Point(width/2, height/2)
		ballRadius = dimensions[1] / 5
		moveDist = height / 20
		ball = Ball(win, ballCenter, ballRadius)
		getBall = ball.getBall()
		while True:
			if ball.getBallXCord() + moveDist < 
			getBall().move(moveDist, 0)
			key = win.getKey()
			if key == "Escape":
				win.close()
			if key == "a":
				distanceToTop = leftPaddle.getP1Y()
				if distanceToTop >= moveDist:
					lPaddle.move(0, -moveDist)
				elif distanceToTop < moveDist:
					lPaddle.move(0, -distanceToTop)
			elif key == "z":
				distanceToBottom = height - leftPaddle.getP2Y()
				if distanceToBottom >= moveDist:
					lPaddle.move(0, moveDist)
				elif distanceToBottom < moveDist:
					lPaddle.move(0, distanceToBottom)
			if key == "k":
				distanceToTop = rightPaddle.getP1Y()
				if distanceToTop >= moveDist:
					rPaddle.move(0, -moveDist)
				elif distanceToTop < moveDist:
					rPaddle.move(0, -distanceToTop)
			elif key == "m":
				distanceToBottom = height - rightPaddle.getP2Y()
				if distanceToBottom >= moveDist:
					rPaddle.move(0, moveDist)
				elif distanceToBottom < moveDist:
					rPaddle.move(0, distanceToBottom)
main()