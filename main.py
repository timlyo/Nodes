import grid as Grid
import window as Window
import input as Input

from pygame import *
import pygame.locals

def main():
	pygame.init()
	print("==Started==")

	clock = pygame.time.Clock()

	variables = {}
	variables["clock"] = clock

	window = Window.Window(variables)
	grid = Grid.Grid()
	mouseInput = Input.MouseInput()

	gridDisplacement = [0,0]

	running = True
	while running:
		clock.tick()
		window.updateGuiVariable("fps", int(clock.get_fps()))
		#input
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if(event.button == 1):
					mouseInput.mouseDown(mouse.get_pos())

			elif event.type == pygame.MOUSEBUTTONUP:
				if(event.button == 1):
					mouseInput.mouseUp(mouse.get_pos())
				elif(event.button == 4):
					print("zoom")
					window.zoomIn()
				elif(event.button == 5):
					window.zoomOut()
				print(event.button)

			elif event.type == pygame.KEYUP:
				print("Key up")

			elif event.type == pygame.VIDEORESIZE:
				window.resize(event.size[0],event.size[1])
  		
		if mouseInput.mouseClicked():
			movement = mouseInput.getMouseMovement()
			gridDisplacement[0] += movement[0]
			gridDisplacement[1] += movement[1]
			window.gridChanged = True
		else:
			mouseInput.getMouseMovement()

		#rendering
		window.clear()
		window.drawGrid(gridDisplacement)
		window.drawGui()
		window.update()

	print("==Shutting down==")
	pygame.quit()

if __name__ == "__main__":
	main() 
