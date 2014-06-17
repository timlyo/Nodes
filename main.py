import grid as Grid
import window as Window
import input as Input

import pygame
from pygame.locals import *

def main():
	pygame.init()
	print("==Started==")

	clock = pygame.time.Clock()

	variables = {}
	variables["clock"] = clock

	window = Window.Window(variables)
	grid = Grid.Grid()
	mouseInput = Input.MouseInput()

	displacement = [0, 0]

	running = True
	while running:
		clock.tick()
		window.updateGuiVariable("fps", int(clock.get_fps()))
		#input
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					mouseInput.mouseDown(pygame.mouse.get_pos())

			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					mouseInput.mouseUp(pygame.mouse.get_pos(), displacement)
				elif event.button == 4:
					window.zoomIn()
				elif event.button == 5:
					window.zoomOut()

			elif event.type == pygame.KEYUP:
				if event.key == K_SPACE:
					displacement[0] = 0
					displacement[1] = 1
					window.updateGrid()

			elif event.type == pygame.VIDEORESIZE:
				window.resize(event.size[0], event.size[1])

		if mouseInput.mouseClicked():
			movement = mouseInput.getMouseMovement()
			displacement[0] += movement[0]
			displacement[1] += movement[1]
			window.gridChanged = True
			if displacement[0] > 40:
				displacement[0] = 40
			if displacement[1] > 40:
				displacement[1] = 40
		else:
			mouseInput.getMouseMovement()

		#rendering
		window.clear()
		window.drawGrid(displacement)
		window.drawGui()
		window.update()

	print("==Shutting down==")
	pygame.quit()

if __name__ == "__main__":
	main()
