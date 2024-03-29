import pygame
import pygame.locals as local

class Menu(object):
    def __init__(self):
	
	#Set default menu option
    	self.Resume = 1
	self.Options = 0
	self.Quit = 0
	
	#Load all menu images
	self.bg = pygame.image.load('images/menubg.png')
	self.StartPressed = pygame.image.load('images/button4a.png')
	self.StartUnpressed = pygame.image.load('images/button4b.png')
	self.ResumePressed = pygame.image.load('images/button1a.png')
	self.ResumeUnpressed = pygame.image.load('images/button1b.png')
	self.OptionsPressed = pygame.image.load('images/button2a.png')
	self.OptionsUnpressed = pygame.image.load('images/button2b.png')
	self.QuitPressed = pygame.image.load('images/button3a.png')
	self.QuitUnpressed = pygame.image.load('images/button3b.png')
	self.screen = pygame.display.get_surface()
	
	
    def update(self,game):
	
	#Check if first time for start/resume differentiation
	if game.firstTime == 1:
		topButtonPressed = self.StartPressed
		topButtonUnpressed = self.StartUnpressed
	else:
		topButtonPressed = self.ResumePressed
		topButtonUnpressed = self.ResumeUnpressed

	#Highlight appropriate menu items
	if self.Resume == 1:
		self.bg.blit(topButtonPressed, (240,240))
		self.bg.blit(self.OptionsUnpressed, (240,304))
		self.bg.blit(self.QuitUnpressed, (240,368))
	elif self.Options == 1:
		self.bg.blit(topButtonUnpressed, (240,240))
		self.bg.blit(self.OptionsPressed, (240,304))
		self.bg.blit(self.QuitUnpressed, (240,368))
	else:
		self.bg.blit(topButtonUnpressed, (240,240))
		self.bg.blit(self.OptionsUnpressed, (240,304))
		self.bg.blit(self.QuitPressed, (240, 368))

	#Check for key presses and alter menu highlight accordingly
	#If action button is pressed, perform menu function
	if local.K_UP in game.key_presses:
		if self.Options == 1:
			self.Resume = 1
			self.Options = 0
		elif self.Quit == 1:
			self.Options = 1
			self.Quit = 0
	elif local.K_DOWN in game.key_presses:
		if self.Resume == 1:
			self.Options = 1
			self.Resume = 0
		elif self.Options == 1:
			self.Quit = 1
			self.Options = 0
	elif local.K_x in game.key_presses:
		if self.Resume == 1:
			game.state = 1
			game.firstTime = 0
		elif self.Quit == 1:
			quit()

    def draw(self):
	#Draw background
	self.screen.blit(self.bg, (1,1))
	
