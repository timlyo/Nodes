from file import File
import window as Window
import input as Input

import pygame
from pygame.locals import *

from reference import objects


def main():
	pygame.init()
	print("==Started==")

	clock = pygame.time.Clock()

	variables = dict()
	variables["clock"] = clock
	variables["input"] = ""
	variables["output"] = ""
	variables["activeNode"] = None
	variables["mousePos"] = (0, 0)

	window = Window.Window(variables)
	mouseInput = Input.MouseInput(window)

	objects.window = window
	objects.grid = window.getGrid()
	objects.mouseInput = mouseInput

	objects.gui.create()

	displacement = [0, 0]

	running = True
	while running:
		clock.tick(60)
		window.updateGuiVariable("fps", int(clock.get_fps()))
		# input
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1 or event.button == 2 or event.button == 3:
					mouseInput.mouseDown(pygame.mouse.get_pos())

			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1 or event.button == 2 or event.button == 3:
					mouseInput.mouseUp(pygame.mouse.get_pos(), displacement, event.button)
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

		if mouseInput.isMouseClicked():
			movement = mouseInput.getMouseMovement()
			displacement[0] += movement[0]
			displacement[1] += movement[1]
			window.gridChanged = True
		else:
			mouseInput.getMouseMovement()

		window.updateGuiVariable("oInput", str(objects.grid.getValueString("input")))
		window.updateGuiVariable("oOutput", str(objects.grid.getValueString("output")))
		mousePos = (pygame.mouse.get_pos()[0] - displacement[0], pygame.mouse.get_pos()[1] - displacement[1])
		window.updateGuiVariable("mousePos", objects.grid.getGridCoord(mousePos))
		try:
			window.updateGuiVariable("nValue", objects.grid.getActiveNode().getValue())
			window.updateGuiVariable("nPos", objects.grid.getActiveNode().coords)
		except AttributeError:
			window.updateGuiVariable("nValue", "")

		#rendering
		window.clear()
		window.drawGridLines(displacement)
		window.updateNodes()
		window.drawNodes(displacement)
		window.drawGui()
		window.blitSurfaces()
		window.update()

	print("==Shutting down==")
	pygame.quit()

	File.saveFile(objects.grid.getNodeList())


if __name__ == "__main__":
	main()
