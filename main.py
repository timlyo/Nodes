from file import File
import window as Window
import input as Input

import pygame
from pygame.locals import *

from reference import Objects
from reference import Reference


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
	variables["activeNodeX"] = None
	variables["activeNodeY"] = None

	window = Window.Window(variables)
	mouseInput = Input.MouseInput()
	keyboardInput = Input.KeyboardInput()

	Objects.grid = window.getGrid()
	Objects.mouseInput = mouseInput

	Reference.mainFont = pygame.font.Font(None, 24)

	Objects.gui.create()

	displacement = [0, 0]

	while window.isRunning():
		clock.tick(60)
		window.updateGuiVariable("fps", int(clock.get_fps()))
		# input
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				window.quit()

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button in (1, 2, 3):
					mouseInput.mouseDown(pygame.mouse.get_pos())

			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button in (1, 2, 3):
					mouseInput.mouseUp(pygame.mouse.get_pos(), displacement, event.button)
				elif event.button in (KMOD_SHIFT, K_q):
					keyboardInput.handleKey(event.key)
				elif event.button == 4:
					window.zoomIn()
				elif event.button == 5:
					window.zoomOut()

			elif event.type == pygame.KEYUP:
				if event.key == K_SPACE:
					displacement[0] = 0
					displacement[1] = 1
					window.updateGrid()
				else:
					keyboardInput.handleKey(event.key)

			elif event.type == pygame.VIDEORESIZE:
				window.resize(event.size[0], event.size[1])

		if mouseInput.isMouseClicked():
			movement = mouseInput.getMouseMovement()
			displacement[0] += movement[0]
			displacement[1] += movement[1]
			window.gridChanged = True
		else:
			mouseInput.getMouseMovement()

		window.updateGuiVariable("oInput", str(Objects.grid.getValueString("input")))
		window.updateGuiVariable("oOutput", str(Objects.grid.getValueString("output")))
		mousePos = (pygame.mouse.get_pos()[0] - displacement[0], pygame.mouse.get_pos()[1] - displacement[1])
		window.updateGuiVariable("mousePos", Objects.grid.getGridCoord(mousePos))
		try:
			window.updateGuiVariable("nValue", Objects.grid.getActiveNode().getValue())
			window.updateGuiVariable("nPos", Objects.grid.getActiveNode().coords)
			window.updateGuiVariable("nConnectionX", Objects.grid.getActiveNode().getConnectionTypes()[0])
			window.updateGuiVariable("nConnectionY", Objects.grid.getActiveNode().getConnectionTypes()[1])
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

	File.saveFile(Objects.grid.getNodeList())


if __name__ == "__main__":
	main()
