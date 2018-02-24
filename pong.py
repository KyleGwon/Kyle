from graphics import *
import random
import time
class LeftPaddle:
	def __init__(self, win, lPaddleDimensions):
		self.win = win
		self.lPaddleWidth = lPaddleDimensions[0]
		self.lPaddleHeight = lPaddleDimensions[1]
		self.lP1 = Point(0, self.win.getHeight() / 2 - self.lPaddleHeight / 2)
		self.lP2 = Point(self.lPaddleWidth, self.win.getHeight() / 2 + self.lPaddleHeight / 2)
		lPaddle = Rectangle(self.lP1, self.lP2)
		lPaddle.setFill("black")
		lPaddle.draw(self.win)
		self.lPaddle = lPaddle
	def getLPaddle(self):
		return self.lPaddle
	def getP1X(self):
		# return self.lPaddle.getP1().getX()
		return self.lP1.getX()
	def getP2X(self):
		# return self.lPaddle.getP2().getX()
		return self.lP2.getX()
	def getP1Y(self):
		return self.lPaddle.getP1().getY()
		# return self.lP1.getY()
	def getP2Y(self):
		return self.lPaddle.getP2().getY()
class RightPaddle:
	def __init__(self, win, rPaddleDimensions):
		self.win = win
		self.rPaddleWidth = rPaddleDimensions[0]
		self.rPaddleHeight = rPaddleDimensions[1]
		self.rP1 = Point(self.win.getWidth() - self.rPaddleWidth, self.win.getHeight() / 2 - self.rPaddleHeight / 2)
		self.rP2 = Point(self.win.getWidth(), self.win.getHeight() / 2 + self.rPaddleHeight / 2)
		rPaddle = Rectangle(self.rP1, self.rP2)
		rPaddle.setFill("black")
		rPaddle.draw(self.win)
		self.rPaddle = rPaddle
	def getRPaddle(self):
		return self.rPaddle
	def getP1X(self):
		return self.rP1.getX()
	def getP2X(self):
		return self.rP2.getX()
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
	def getBallXCord(self):
		return self.ball.getCenter().getX()
	def getBallYCord(self):
		return self.ball.getCenter().getY()
def main():
		width = 800
		height = 400
		win = GraphWin("Turtle Pong", width, height)
		dimensions = [width / 200, height / 6]
		leftPaddle = LeftPaddle(win, dimensions)
		rightPaddle = RightPaddle(win, dimensions)
		lPaddle = leftPaddle.getLPaddle()
		rPaddle = rightPaddle.getRPaddle()
		ballCenter = Point(width/2, height/2)
		ballRadius = dimensions[1] / 8
		ballSideMoveDist = height / 75
		ballVertMoveDist = height / 25
		moveDist = height / 75
		ball = Ball(win, ballCenter, ballRadius)
		getBall = ball.getBall()
		vertDirection = 2
		sideDirection = 1
		while True:
			if sideDirection == 1:
				#When the ball is in line with the paddle, this happens
				if ball.getBallYCord() - ballRadius >= leftPaddle.getP1Y() and ball.getBallYCord() + ballRadius <= leftPaddle.getP2Y():
					#Left movement command
					if ball.getBallXCord() - ballSideMoveDist - ballRadius > leftPaddle.getP2X():
						getBall.move(-ballSideMoveDist, 0)
						#sleep command so the ball doesn't fly off the screen!
						time.sleep(0.05)
					elif ball.getBallXCord() - ballSideMoveDist - ballRadius <= leftPaddle.getP2X():
						ballDistToLeftPaddle = ball.getBallXCord() - leftPaddle.getP2X() + ballRadius
						getBall.move(-ballDistToLeftPaddle, 0)
						#sleep command so the ball doesn't fly off the screen!
						time.sleep(0.05)
						ballSideMoveDist += 0.5
						sideDirection = 2
				#When the ball is NOT in line with the paddle, this happens
				else:
					#Left movement command
					if ball.getBallXCord() - ballSideMoveDist - ballRadius > leftPaddle.getP2X():
						getBall.move(-ballSideMoveDist, 0)
						#sleep command so the ball doesn't fly off the screen!
						time.sleep(0.05)
					elif ball.getBallXCord() - ballSideMoveDist - ballRadius <= leftPaddle.getP2X():
						ballDistToLeft = ball.getBallXCord() - ballRadius
						getBall.move(-ballDistToLeft, 0)
						#sleep command so the ball doesn't fly off the screen!
						print("Player 2 has won!")
						time.sleep(1)
						break
			if sideDirection == 2:
				if ball.getBallYCord() + ballRadius >= rightPaddle.getP1Y() and ball.getBallYCord() + ballRadius <= rightPaddle.getP2Y():
					if ball.getBallXCord() + ballSideMoveDist + ballRadius < rightPaddle.getP1X():
						getBall.move(ballSideMoveDist, 0)
						time.sleep(0.05)
					elif ball.getBallXCord() + ballSideMoveDist + ballRadius >= rightPaddle.getP1X():
						ballDistToRightPaddle =  rightPaddle.getP1X() - ball.getBallXCord() - ballSideMoveDist
						getBall.move(ballDistToRightPaddle, 0)
						time.sleep(0.05)
						ballSideMoveDist += 0.5
						sideDirection = 1
				else:
					if ball.getBallXCord() + ballSideMoveDist + ballRadius < rightPaddle.getP1X():
						getBall.move(ballSideMoveDist, 0)
						time.sleep(0.05)
					elif ball.getBallXCord() + ballSideMoveDist + ballRadius >= rightPaddle.getP1X():
						ballDistToRight = width - ball.getBallXCord() - ballRadius
						getBall.move(ballDistToRight, 0)
						print("Player 1 has won!")
						time.sleep(1)
						break
	#Vertical is before horizontal to make calculations easier (predictions are already made and executed)
			#Up direction possibility
			time.sleep(0)
			if vertDirection == 1:
				#Up movement command 
				if ball.getBallYCord() - ballVertMoveDist - ballRadius > 0:
					getBall.move(0, -ballVertMoveDist)
				elif ball.getBallYCord() - ballVertMoveDist - ballRadius <= 0:
					ballDistToTop = ball.getBallYCord() - ballRadius
					getBall.move(0, -ballDistToTop)
					#Since the ball hit the top, its direction must change to down
					vertDirection = 2
			#Down direction possibility
			elif vertDirection == 2:
				#Down movement command
				if ball.getBallYCord() + ballVertMoveDist + ballRadius < height:
					getBall.move(0, ballVertMoveDist)
				elif ball.getBallYCord() + ballVertMoveDist + ballRadius >= height:
					ballDistToBottom = height - ball.getBallYCord() - ballRadius
					getBall.move(0, ballDistToBottom)
					vertDirection = 1
					#Since the ball hit the bottom, its direction must change to up
			#Onto horizontal possibilities
			#Left direction possibility




			# if sideDirection == "right":
			# 	if vertDirection == "up":
			# 		if ball.getBallXCord() + moveDist + ballRadius > rPaddle.getP1Y():
			# 			if ball.getBallYCord() + moveDist + ballRadius < rPaddle.getP1Y():
			# 				getBall.move(moveDist, -moveDist)
			# 				time.sleep(0.05)
			# 			elif ball.getBallYCord() + moveDist + ballRadius >= rPaddle.getP1Y():
			# 				distanceToRPaddle = ballCenter + ballRadius + 

			# 		else:
			# 			if ball.getBallYCord() + moveDist + ballRadius < rightPaddle.getP1Y():
			# 				distanceToTop = ball.getBallYCord
			# 				getBall.move(moveDist, -distanceToTop)
			# 			elif ball.getBallYCord() + moveDist + ballRadius >= rightPaddle.getP1Y():
			# 				distanceToBottomToTop = ball.getBallYCord

			# 				getBall.move(moveDist)
			# 			else:
			# 				ballDistToTop = ball.getBallYCord()
			# 				getBall.move(moveDist, -ballDistToTop + ballRadius)
			# 				time.sleep(0.05)
			# 			vertDirection = "down"
			# 	elif vertDirection == "down":
			# 		if ball.getBallXCord() + moveDist + 0 < height and ball.getBallYCord() + moveDist < height:
			# 			getBall.move(moveDist, moveDist)
			# 			time.sleep(0.05)
			# 		else:
			# 			ballDistToBottom = height - ball.getBallYCord()
			# 			getBall.move(moveDist, ballDistToBottom - ballRadius)
			# 			vertDirection = "up"
			# elif sideDirection == "left":
			# 	if vertDirection == "up":
			# 		if ball.getBallXCord() - moveDist > 0 and ball.getBallYCord() - moveDist > 0:
			# 			getBall.move(-moveDist, -moveDist)
			# 			time.sleep(0.05)
			# 	elif vertDirection == "down":
			# 		if ball.getBallXCord() - moveDist > 0 and ball.getBallYCord() + moveDist < height:
			# 			getBall.move(-moveDist, moveDist)
			# 			time.sleep(0.05)





			key = win.checkKey()
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

				# key = win.checkKey()
				# clickkey thingggy setFill thingsy

main()
