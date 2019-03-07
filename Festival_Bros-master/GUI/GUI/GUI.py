
screen = 0
city = ''
festival = ''
genre = ''
cities = ["Austin", "New York", "Dallas", "San Francisco", "Santa Fe", "New Orleans", "New York"]
genres = ["Alternative", "Blues", "Christian", "Classical", "Country", "EDM", "Folk", "Hip Hop", "Indie", "Jazz", "Pop", "Rap", "Rock", "R&B"]
city_selected = -1
genre_selected = -1
frame = 0
import sys

# general setup for Processing draw window

def setup():
	global title_font
	global button_font
	global detail_font
	size(900,650)
	strokeWeight(2)
	title_font = createFont("Arial", 50)
	button_font = createFont("Arial", 32)
	detail_font = createFont("Arial", 22)

# draw loop

def draw():

	global title_font
	global button_font
	global detail_font
	global screen
	global city
	global festival
	global genre
	global cities
	global genres
	global city_selected
	global genre_selected
	global frame
	rectMode(CENTER)

	# main menu page

	if (screen == 0):

		# place text and button outlines

		background(200)
		fill(100)
		rect(150,315,270,100)
		rect(450,315,270,100)
		rect(750,315,270,100)
		fill(200,0,0)
		rect(875,25,50,50)

		textFont(title_font)
		fill(0)
		textAlign(CENTER)
		text("Festival Bros", 450, 50)

		textFont(button_font)
		text("Find Festivals\nNear Me", 150, 300)
		text("Create a Custom\nFestival Schedule", 450, 300)
		text("Randomize a\nFestival Schedule", 750, 300)

		textFont(button_font)
		text("Welcome!", 450, 100)

		textFont(detail_font)
		text("X",875,35)

		# read button press based on mouse location

		if (mousePressed and mouseX > 15 and mouseX < 285 and mouseY > 265 and mouseY < 365):
			screen = 1
		if (mousePressed and mouseX > 315 and mouseX < 585 and mouseY > 265 and mouseY < 365):
			screen = 2
		if (mousePressed and mouseX > 615 and mouseX < 885 and mouseY > 265 and mouseY < 365):
			screen = 3
		if (mousePressed and mouseX > 850 and mouseX < 900 and mouseY > 0 and mouseY < 50):
			sys.exit()

	# Festival Suggestion Page

	if (screen == 1):

		# text and button outlines

		background(200)
		textFont(title_font)
		fill(0)
		textAlign(CENTER)
		text("Festivals Near Me", 450, 50)

		fill(50,200,50)
		rect(825,40,120,25)

		# loop to create city buttons and determine which one is currently selected
		offset = 0
		for i in range(0,7):
			if(city_selected == i):
				fill(50,150,50)
			else:
				fill(200,50,50)
			rect(150,offset+150,150,50)
			fill(0)
			textFont(detail_font)
			text(cities[i],150,offset+160)
			if(mousePressed and mouseX > 75 and mouseX < 225 and mouseY > offset+125 and mouseY < offset+175):
				city_selected = i
				city = cities[i]
			offset += 75

		# loop to create genre buttons and determine which on is currently selected
		offset = 0
		shift = 0
		for i in range(0,14):
			if(genre_selected == i):
				fill(50,150,50)
			else:
				fill(50,50,200)
			rect(350+shift,offset+150,150,50)
			fill(0)
			textFont(detail_font)
			text(genres[i],350+shift,offset+160)
			if(mousePressed and mouseX > 275+shift and mouseX < 425+shift and mouseY > offset+125 and mouseY < offset+175):
				genre_selected = i
				genre = genres[i]
			offset += 75
			if(i == 6):
				shift = 175
				offset = 0

		# submit buttont that ony works when all criteria have been selected
		fill(175,50,100)
		rect(750,125,150,50)
		fill(0)
		text("Submit",750,135)
		if(mousePressed and mouseX > 675 and mouseX < 825 and mouseY > 100 and mouseY < 175 and city_selected != -1 and genre_selected != -1):
			festival = "Governors Ball Music Festival"

		# display the suggested festival
		text(festival,750,300)

		if(city_selected != -1 and genre_selected != -1 and mousePressed and mouseX > 625 and mouseX < 875 and mouseY > 275 and mouseY < 325 and frame>5):
			link("https://github.com/ella-garcia/Festival_Bros")
			frame = 0

		fill(0)
		textFont(detail_font)
		text("Main Menu",825,50)

		# read button press based on mouse location

		if (mousePressed and mouseX > 800 and mouseX < 850 and mouseY > 15 and mouseY < 65):
			screen = 0

	# Scheduler Page

	if (screen == 2):

		# text and button outlines

		background(200)
		textFont(title_font)
		fill(0)
		textAlign(CENTER)
		text("Festival Scheduler", 450, 50)

		fill(50,200,50)
		rect(825,40,120,25)

		fill(0)
		textFont(detail_font)
		text("Main Menu",825,50)

		# read button press based on mouse location

		if (mousePressed and mouseX > 800 and mouseX < 850 and mouseY > 15 and mouseY < 65):
			screen = 0

	# Randomizer Page

	if (screen == 3):

		# text and button outlines

		background(200)
		textFont(title_font)
		fill(0)
		textAlign(CENTER)
		text("Schedule Randomizer", 450, 50)

		fill(50,200,50)
		rect(825,40,120,25)

		fill(0)
		textFont(detail_font)
		text("Main Menu",825,50)

		# read button press based on mouse location

		if (mousePressed and mouseX > 800 and mouseX < 850 and mouseY > 15 and mouseY < 65):
			screen = 0

	frame+=1





















	
