import grid as Grid
import window as Window
import input as Input

from pygame import *
import pygame.locals

def main():
	pygame.init()
	print("==Started==")

	window = Window.Window()
	grid = Grid.Grid()
	mouseInput = Input.MouseInput()

	gridDisplacement = [0,0]

	running = True
	while running:
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
			gridDisplacement = mouseInput.getMouseMovement()
		else:
			mouseInput.getMouseMovement()

		#rendering
		window.clear()
		window.drawGrid(gridDisplacement)
		window.update()

	print("==Shutting down==")
	pygame.quit()

if __name__ == "__main__":
	main() 
