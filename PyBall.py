import pygame
import sys
import os.path
import palleteImages
import palleteFont

width = 256
height = 240
scale = 2
game = "test.lvl"
if len(sys.argv) > 1:
	scale = int(sys.argv[1])
if len(sys.argv) > 2:
	game = sys.argv[2]
	if not path.exists(game) or not path.isfile(game):
		print "%s is not a file" % (game,)
		game = "test.lvl"

dWidth = width * scale
dHeight = height * scale
mainPalette = {0:(0, 0, 0), 1:(64, 64, 64), 2:(128, 128, 128), 3:(192, 192, 192), 4:(255, 255, 255), 5:(0, 0, 0)}
background = 0

		
class Ball:
	
	def __init__(self, x, y):
		self.image = 0
		self.x = x
		self.y = y
		self.vy = -1.0
		self.vx = 1.0
		self.vScale = 1.0
		self.vScaleSpeed = 0.0001
		self.collide = 0
		self.palette = 1
		self.offScreen = 0
		self.bounced = 0
		
	def move(self):
		self.x += self.vx * self.vScale
		self.y += self.vy * self.vScale
		self.vScale += self.vScaleSpeed
		
	def checkBorders(self):
		if self.x < 0 or self.x + len(images[self.image].imageData[0]) > width - 1:
			self.vx *= -1
			if self.x < 0:
				self.x = 0
			else:
				self.x = width - 1 - len(images[self.image].imageData[0])
		if self.y < 16:
			self.vy *= -1
			if self.y < 0:
				self.y = 0
		if self.y > height:
			self.offScreen = 1
			
	def draw(self):
		self.collide = images[self.image].draw(int(self.x), int(self.y), self.palette, scale)
		
	def collideWith(self, other, type):
		xIn = 0.0
		yIn = 0.0
		collides = 0
		if self.x + len(images[self.image].imageData[0]) >= other.x and self.x <= other.x + len(images[other.image].imageData[0]):
			if self.x < other.x:
				xIn = self.x + len(images[self.image].imageData[0]) - other.x
			else:
				xIn = other.x + len(images[other.image].imageData[0]) - self.x
		if self.y + len(images[self.image].imageData) >= other.y and self.y <= other.y + len(images[other.image].imageData):
			if self.y < other.y:
				yIn = self.y + len(images[self.image].imageData) - other.y
			else:
				yIn = other.y + len(images[other.image].imageData) - self.y
		if xIn > 0 and yIn > 0 and not self.bounced:
			self.bounced = 1
			collides = 1
			
			if type:
				other.alive = 0
				other.erase()
			if xIn < yIn:
				if self.x < other.x:
					self.x -= xIn
				else:
					self.x += xIn
				self.vx *= -1
			elif yIn < xIn:
				if self.vx > 0:
					self.vx = ((len(images[other.image].imageData[0]) / 2) / xIn)
				else:
					self.vx = -1 * ((len(images[other.image].imageData[0]) / 2) / xIn)
				
				if self.vx > 2:
					self.vx = 2.0
				elif self.vx < -2:
					self.vx = -2.0
					
				if self.y < other.y:
					self.y -= yIn
				else:
					self.y += yIn
				self.vy *= -1
			else:
				if self.x < other.x:
					self.x -= xIn
					self.y -= yIn
				else:
					self.x += xIn
					self.y += yIn
				self.vy *= -1
				self.vx *= -1
		
		return collides

class Brick:

	def __init__(self, surface, x, y, palette = 1):
		self.surface = surface
		self.x = x
		self.y = y
		self.image = 2
		self.palette = palette
		self.alive = 1
		
	def draw(self):
		images[self.image].draw(self.x, self.y, self.palette, scale)
	
	def erase(self):
		pygame.draw.rect(self.surface, mainPalette[background], (self.x * scale, self.y * scale, len(images[self.image].imageData[0]) * scale, len(images[self.image].imageData) * scale))
		
class Paddle:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.image = 1
		self.palette = 0
	
	def handleEvent(self, event):
		self.x = (event.pos[0] - 16) / scale
		if self.x < 0:
			self.x = 0
		elif self.x + len(images[self.image].imageData[0]) > width - 1:
			self.x = width - 1 - len(images[self.image].imageData[0])
			
	def draw(self):
		images[self.image].draw(self.x, self.y, self.palette, scale)

pygame.display.set_caption("PyBall")
screen = pygame.display.set_mode((dWidth, dHeight))
bgImage = pygame.Surface((dWidth, dHeight))
font = palleteFont.setFontSurface(screen)
images = [
	palleteImages.paletteImage(screen),
	palleteImages.paletteImage(screen, [
		[0, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 0],
		[5, 5, 6, 6, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 6, 6, 5, 5],
		[5, 6, 6, 6, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 6, 6, 6, 6, 5],
		[5, 6, 6, 6, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 6, 6, 6, 5],
		[5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5],
		[4, 4, 5, 5, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 4, 4],
		[4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4],
		[0, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 0]
	]),
	palleteImages.paletteImage(bgImage, [
		[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3],
		[3, 5, 5, 5, 5, 1, 5, 1, 1, 2, 1, 2, 1, 2, 2, 1],
		[3, 5, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 3, 1],
		[3, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 1],
		[3, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 3, 1],
		[3, 1, 2, 2, 2, 2, 2, 2, 3, 2, 3, 3, 3, 3, 4, 1],
		[3, 2, 2, 3, 2, 3, 2, 3, 3, 4, 3, 4, 4, 4, 4, 1],
		[2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
	])
	]
clock = pygame.time.Clock()
	
def LoadLevel(levelName):
	bricks = []
	levelData = []
	file = open(levelName, "r")
	x = 0
	y = 16
	while 1:
		levelData.append(file.readline().split(", "))
		if levelData[-1] == [""]:
			levelData.pop()
			break
	
	file.close()
	for list in levelData:
		if "\n" in list:
			list.remove("\n")
		for elem in list:
			if elem != "0":
				bricks.append(Brick(bgImage, x, y, int(elem)))
			x += 16
		x = 0
		y += 8
	
	return bricks
	
def ResetLevel(bricks):
	bgImage.fill(mainPalette[background])
	for brick in bricks:
		brick.draw()
		brick.alive = 1
		
def TitleScreen():
	tsList = [
		"OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
		"O                              O",
		"O   PP  Y Y  BB   A  L   L     O",
		"O   P P Y Y  B B A A L   L     O",
		"O   PP   Y   BB  AAA L   L     O",
		"O   P    Y   B B A A L   L     O",
		"O   P    Y   BB  A A LLL LLL   O",
		"O                              O",
		"O   PP  Y Y  BB   A  L   L     O",
		"O   P P Y Y  B B A A L   L     O",
		"O   PP   Y   BB  AAA L   L     O",
		"O   P    Y   B B A A L   L     O",
		"O   P    Y   BB  A A LLL LLL   O",
		"O                              O",
		"O   PP  Y Y  BB   A  L   L     O",
		"O   P P Y Y  B B A A L   L     O",
		"O   PP   Y   BB  AAA L   L     O",
		"O   P    Y   B B A A L   L     O",
		"O   P    Y   BB  A A LLL LLL   O",
		"O                              O",
		"O   PP  Y Y  BB   A  L   L     O",
		"O   P P Y Y  B B A A L   L     O",
		"O   PP   Y   BB  AAA L   L     O",
		"O   P    Y   B B A A L   L     O",
		"O   P    Y   BB  A A LLL LLL   O",
		"O                              O",
		"O                              O",
		"O     CLICK MOUSE TO START!    O",
		"O                              O",
		"OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
	]
	tsAnim = []
	for i in range(7):
		pal = i + 2
		if pal > 8:
			pal = 2
		tsAnim.append(pygame.Surface((dWidth, dHeight)))
		tsFont = palleteFont.setFontSurface(tsAnim[i])
		index = 0
		for line in tsList:
			palleteFont.fontPrint(0, index * 8, line, tsFont, scale, pal)
			pal += 1
			index += 1
			if pal > 8:
				pal = 2
				
	return tsAnim

def main(loadFile = game):
	balls = []
	paddle = Paddle(128, height - 24)
	bricks = LoadLevel(loadFile)
	ResetLevel(bricks)
	balls.append(Ball(128.0, 168.0))
	running = 1
	ballFreeze = 0
	ballTime = 0
	pygame.mouse.set_visible(0)
	lives = 3
	score = 0
	nextLife = 1000
	lifeScore = 1000
	failed = 0
	won = 0
	attractMode = 1
	title = TitleScreen()
	frame = 0
	while attractMode:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				attractMode = 0
				running = 0
			elif event.type == pygame.MOUSEBUTTONDOWN:
				attractMode = 0
				
		screen.fill(mainPalette[background])
		screen.blit(title[frame], (0, 0))
		pygame.display.flip()
		frame += 1
		if frame >= len(title):
			frame = 0
		clock.tick(30)
	
	if running:
		pygame.time.wait(500)
	
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = 0
			elif event.type == pygame.MOUSEMOTION:
				paddle.handleEvent(event)
				
		screen.fill(mainPalette[background])
		screen.blit(bgImage, (0, 0))
		
		paddle.draw()
		
		if not ballFreeze:
			for ball in balls:
				colBrick = 0
				ball.bounced = 0
				ball.collide = 0
				ball.move()
				ball.checkBorders()
				ball.draw()
				for brick in bricks:
					if brick.alive:
						if ball.collideWith(brick, 1):
							score += 10
							if score >= nextLife:
								lives += 1
								nextLife += lifeScore
							colBrick = 1
							break
				if not colBrick:
					ball.collideWith(paddle, 0)
						
				if ball.offScreen:
					balls.remove(ball)
					if len(balls) == 0:
						balls.append(Ball(128.0, 168.0))
						ballTime = 60
						ballFreeze = 1
						lives -= 1
						if lives == 0:
							running = 0
							failed = 1
		
		palleteFont.fontPrint(4, 4, "SCORE:%05d" % (score,), font, scale)
		palleteFont.fontPrint(256 - 68, 4, "LIVES:%02d" % (lives,), font, scale)
		if not [elem for elem in bricks if elem.alive]:
			running = 0
			won = 1
					
		else:
			ballTime -= 1
			if ballTime == 0:
				ballFreeze = 0
				
		pygame.display.flip()
		clock.tick(120)
	
	screen.fill(mainPalette[background])
	if failed:
		palleteFont.fontPrint(88, 116, "GAME OVER!", font, scale, 2)
		pygame.display.flip()
		pygame.time.wait(1000)
	if won:
		palleteFont.fontPrint(96, 116, "YOU WIN!", font, scale, 3)
		pygame.display.flip()
		pygame.time.wait(1000)
	
			
if __name__ == "__main__":
	main()