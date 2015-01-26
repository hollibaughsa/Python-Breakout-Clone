import pygame
import random
import sys

width = 256
height = 240
ballCount = 20
if len(sys.argv) >= 3:
	width = int(sys.argv[1])
	height = int(sys.argv[2])
if len(sys.argv) >= 4:
	ballCount = int(sys.argv[3])

mainPalette = {0:(0, 0, 0), 1:(64, 64, 64), 2:(128, 128, 128), 3:(192, 192, 192), 4:(255, 255, 255), 5:(0, 0, 0)}
palBall = {0:(0, 0, 0), 1:(64, 64, 64), 2:(128, 128, 128), 3:(192, 192, 192), 4:(255, 255, 255), 5:(0, 0, 0)}
palPaddle = {0:(0, 0, 0), 1:(48, 48, 48), 2:(94, 94, 94), 3:(142, 142, 142), 4:(0, 128, 64), 5:(0, 255, 128), 6:(255, 255, 255)}
palRed = {0:(0, 0, 0), 1:(128, 0, 0), 2:(255, 0, 0), 3:(255, 128, 128), 4:(255, 255, 255), 5:(0, 0, 0)}
palGreen = {0:(0, 0, 0), 1:(0, 128, 0), 2:(0, 255, 0), 3:(128, 255, 128), 4:(255, 255, 255), 5:(0, 0, 0)}
palBlue = {0:(0, 0, 0), 1:(0, 0, 128), 2:(0, 0, 255), 3:(128, 128, 255), 4:(255, 255, 255), 5:(0, 0, 0)}
palPurple = {0:(0, 0, 0), 1:(128, 0, 128), 2:(255, 0, 255), 3:(255, 128, 255), 4:(255, 255, 255), 5:(0, 0, 0)}
palCyan = {0:(0, 0, 0), 1:(0, 128, 128), 2:(0, 255, 255), 3:(128, 255, 255), 4:(255, 255, 255), 5:(0, 0, 0)}
palYellow = {0:(0, 0, 0), 1:(128, 128, 0), 2:(255, 255, 0), 3:(255, 255, 128), 4:(255, 255, 255), 5:(0, 0, 0)}
palFont = {0:(0, 0, 0), 1:(128, 128, 128), 2:(255, 255, 255)}
palettes = [palPaddle, palBall, palRed, palGreen, palBlue, palCyan, palPurple, palYellow, palFont]
background = 0

class paletteImage:
	
	def __init__(self, surface, image = []):
		self.surface = surface
		self.imageData = []
		if len(image) > 0:
			self.imageData = image
		else:
			self.imageData = [
				[0, 0, 1, 1, 1, 1, 0, 0],
				[0, 1, 2, 2, 2, 2, 1, 0],
				[1, 2, 2, 3, 3, 2, 2, 1],
				[1, 2, 3, 4, 4, 3, 2, 1],
				[1, 2, 3, 4, 4, 3, 2, 1],
				[1, 2, 2, 3, 3, 2, 2, 1],
				[0, 1, 2, 2, 2, 2, 1, 0],
				[0, 0, 1, 1, 1, 1, 0, 0]
				]
	def draw(self, x, y, palette = 0, scale = 1):
		x *= scale
		y *= scale
		collision = 0
		yOff = 0
		for row in self.imageData:
			xOff = 0
			for col in row:
				if x > 0 and y > 0 and x + xOff <= width - 1 and y + yOff <= height - 1 and col != 0:
					(r, g, b, a) = self.surface.get_at((x + xOff, y + yOff))
					if (r, g, b) != mainPalette[background]:
						collision = 1
				if col != 0:
					if scale == 1:
						self.surface.set_at((x + xOff, y + yOff), palettes[palette][col])
					else:
						pygame.draw.rect(self.surface, palettes[palette][col], (x + xOff, y + yOff, scale, scale))
				xOff += scale
			
			yOff += scale
			
		return collision
		
class Ball:
	
	def __init__(self, surface, x, y, image = 0, palette = 0):
		self.surface = surface
		self.image = image
		self.x = x
		self.y = y
		self.vy = random.randint(-1, 1)
		self.vx = random.randint(-1, 1)
		if self.vy == 0:
			self.vy = 1
		if self.vx == 0:
			self.vx = 1
		self.collide = 0
		self.palette = palette
		
	def move(self):
		self.x += self.vx
		self.y += self.vy
		
	def checkBorders(self):
		if self.x < 0 or self.x + len(images[self.image].imageData[0]) > width - 1:
			self.vx *= -1
			if self.x < 0:
				self.x = 0
			else:
				self.x = width - 1 - len(images[self.image].imageData[0])
		if self.y < 0 or self.y + len(images[self.image].imageData) > height - 1:
			self.vy *= -1
			if self.y < 0:
				self.y = 0
			else:
				self.y = height - 1 - len(images[self.image].imageData)
			
	def draw(self):
		self.collide = images[self.image].draw(self.x, self.y, self.palette)
		
	def collideWith(self, other):
		xIn = 0
		yIn = 0
		collides = 0
		if self.x + len(images[self.image].imageData[0])>= other.x and self.x <= other.x + len(images[other.image].imageData[0]):
			if self.x < other.x:
				xIn = self.x + len(images[self.image].imageData[0]) - other.x
			else:
				xIn = other.x + len(images[other.image].imageData[0]) - self.x
		if self.y + len(images[self.image].imageData) >= other.y and self.y <= other.y + len(images[other.image].imageData):
			if self.y < other.y:
				yIn = self.y + len(images[self.image].imageData) - other.y
			else:
				yIn = other.x + len(images[other.image].imageData) - self.y
		if xIn > 0 and yIn > 0:
			if xIn < yIn:
				if self.x < other.x:
					self.x -= xIn / 2
					other.x += xIn / 2
				else:
					self.x += xIn / 2
					other.x -= xIn /2
				self.vx *= -1
				other.vx *= -1
			elif yIn < xIn:
				if self.y < other.y:
					self.y -= yIn / 2
					other.y += yIn / 2
				else:
					self.y += yIn / 2
					other.y -= yIn / 2
				self.vy *= -1
				other.vy *= -1
			else:
				if self.x < other.x:
					self.x -= xIn / 2
					self.y -= yIn / 2
					other.x += xIn / 2
					other.y += yIn / 2
				else:
					self.x += xIn / 2
					self.y += yIn / 2
					other.x -= xIn / 2
					other.y -= yIn /2
				self.vy *= -1
				self.vx *= -1
				other.vy *= -1
				other.vx *= -1
			
screen = pygame.display.set_mode((width, height))
images = [paletteImage(screen),]
clock = pygame.time.Clock()

def main():
	running = 1
	balls = []
	for i in range(0, ballCount + 1):
		x = random.randint(8, width - 16)
		y = random.randint(8, height - 16)
		pal = random.randint(0, 3)
		balls.append(Ball(screen, x, y, 0, pal))

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = 0
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_0:
					mainPalette = palGrey
				elif event.key == pygame.K_1:
					mainPalette = palRed
				elif event.key == pygame.K_2:
					mainPalette = palGreen
				elif event.key == pygame.K_3:
					mainPalette = palBlue
				
		screen.fill((0, 0, 0))
		
		for ball in balls:
			ball.collide = 0
			ball.move()
			ball.checkBorders()
			ball.draw()
			if ball.collide:
				for oBall in balls:
					ball.collideWith(oBall)
			
		
		pygame.display.flip()
		clock.tick(120)
		
if __name__ == "__main__":
	main()