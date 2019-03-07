
import random
import datetime
import sys

screen = 0
city = ''
festival = ''
genre = ''

#THESE ARE PLACEHOLDERS. THEY WILL ACTUALLY JUST BE WHATEVER CITIES/GENRES THEY DECIDED ON AND HAVE IN THEIR CODE
cities = ["Austin", "New York", "Dallas", "San Francisco", "Santa Fe", "New Orleans", "Las Vegas"]
genres = ["Alternative", "Blues", "Christian", "Classical", "Country", "EDM", "Folk", "Hip-Hop", "Indie", "Jazz", "Pop", "Rap", "Rock", "R&B"]
city_selected = -1
genre_selected = -1
band_selected = -1
selected = 0
bands = []
showtimes = []
festival = ''
frame = 0
festivalNames = ["Governor's Ball","ACL","Coachella","Essence Fest"]
festivalLocations = ["New York","Austin","Las Vegas","New Orleans"]

#Function that, given a location and genre, makes a list of possible festivals that the user would want to attend (including time conflicts, they will be accounted for in the scheduler)
def select_festival(location):
	possible_festivals = []	
	#Iterate through the global festivals list
	for indx,festival in enumerate(festivalNames):
		if festivalLocations[indx] == location:
			possible_festivals.append(festivalNames[indx])

	print ( possible_festivals)
	return (possible_festivals)

def city_festivals(location,global_festivals_list):
	possible_festivals = []
	for festival in global_festivals_list:
		#check that the item in the list matches location and genre, add to possibility list
		if (festival.location == location):
			possible_festivals.append(festival)
	#Return error if there are no festivals
	if len(possible_festivals) == 0:
		return [-1]
	#Return a list of all festivals in the desired location
	else: 
		return possible_festivals


def random_shows(festival):
	#Create the empty Schedule
	schedule = []

	#Make a list of the Festival Days, randomly select a day
	festival_days = festival.days

	#From the list, make another list of all combinations of shows possible with non-conflicting times
	day_index = random.randint(-1, (len(festival_days) + 1))
	day = festival_days[day_index]

	#Get shows from the days
	shows = festival.day.shows

	#Make a list of shows before 1:00
	time = 1
	shows_before_1 = []
	for show in shows:
		if show.start.time <= time:
			shows_before_1.append(show)

	#Get a random index to select a random show from this list
	show_index = random.randint(-1, (len(shows_before_1) + 1))
	schedule.append(shows_before_1[show_index])

	#Select a random show that starts after the selected show ends
	show_target = schedule[0]
	end_of_day = False 
	while not end_of_day:
		for show in shows:
			if show.start.time > show_target.end.time:
				shows_after_show.append(show)
		#Check that there are shows after the selected show, if not exit loop
		if len(shows_after_show) == 0:
			end_of_day = True
		else: 
			show_index = random.randint(-1, (len(shows_after_show) + 1))
			schedule.append(shows_after_show[show_index])
			#Empty list, move index over one, select new target
			shows_after_show = []
			new_index += 1
			show_target = shows[new_index]
	
	#Check that the schedule list was made, return an error if not
	if len(schedule) == 0:
		return "ERROR: The list is empty-- there is no schedule."
	else: 
		show_strings = []
		#Create list of strings to send back to GUI
		for show in schedule: 
			showstring = "Artist: " + str(show.artist) + "Start Time: " + str(show.start.time)
			show_strings.append(showstring)
		return show_strings

class Show(object):
	# The class "constructor" - It's actually an initializer 
	def __init__(self, artist, start, end):

		start_time = float(start)

		end_time = float(end)

		self.artist = artist
		self.start = start_time
		self.end = end_time

class Festival_Day(object):
	def __init__(self, day, shows):
		self.day = day
		self.shows = shows

class Festival(object):
	def __init__(self, name, days, genres, city, start, end):

		start_str = start
		start_day = datetime.datetime.strptime(start_str, '%m-%d-%Y')

		end_str = start
		end_day = datetime.datetime.strptime(end_str, '%m-%d-%Y')

		self.festival_name = name
		self.genres = genres
		self.location = city
		self.days = days
		self.startday = start_day
		self.endday = end_day

	# create a Graph object

def create_festival(txt_file):
	#create list
	fest_days = []
	shows = []
	shows2 = []
	shows3 = []
	#day number iterative val
	i=1
	artistLine = True
	artist = ""
	start = 0
	end = 0
	# open file for reading
	file = open (txt_file, "r")

	festival = file.readline().strip()
	print ('Fest: ' + festival)

	genres = file.readline().strip()
	genre_list = genres.split('/')
	print (genre_list)

	location = file.readline().strip()
	print ('Location: ' + location)

	fest_start = file.readline().strip()
	print ('Fest Start: ' + fest_start)
	
	fest_end = file.readline().strip()
	print ('Fest End: ' + fest_end)

	for line in file.readlines():
		if not (';') in line and not ('DAY') in line :
			if artistLine:
				artist = line.strip()
				print ("ARTIST: "+artist)
				artistLine =  not artistLine
			else:
				show = line.strip()
				print ("SHOW TIME:" + show)
				artistLine = not artistLine
				show1 = Show(artist, start, end)
		else:
			print ("*********NEW DAY**********")
			i += 1
			
	return Festival(festival, fest_days, genre_list, location, fest_start, fest_end)
	

""" 		if ";DAY" in line:
			pass#Do something

		else:
			pass#Do something """
""" 	while i != 'END':
		day = i
		print ('Day: ' + day)
		i = file.readline().strip()

		while ';' not in i:

			artist = i
			#print ('Artist: ' + artist)

			time = file.readline().strip()
			#print ('Time: ' + time)


			splittime = time.split('-')


			start_split = splittime[0].split(':')
			print(start_split)
			start_hour = float(start_split[0])
			start_minute = float(start_split[1])/100


			e_s = splittime[1].split(':')
			e_h = float(e_s[0])
			e_m = float(e_s[1])/100



			start = start_hour + start_minute
			end = e_h + e_m


			show1 = Show(artist, start, end)
			#print (show1.artist)
			#print (show1.start)
			#print (show1.end)

			#add show to correct day
			if count == 0:
				shows.append(show1)
			if count == 0:
				shows2.append(show1)
			if count == 0:
				shows3.append(show1)

			    
			i = file.readline().strip()


			#create Festival Day object
			if count == 0:
				fest_days.append(Festival_Day(day, shows))
			elif count == 1:
				fest_days.append(Festival_Day(day, shows2))
			elif count == 2:
				fest_days.append(Festival_Day(day, shows3))
			    
			count = count + 1
			    
			i = file.readline().strip()

	return Festival(festival, fest_days, genre_list, location, fest_start, fest_end)

	print ('Done') """

""" GOV_BALL = create_festival('gov_copy.txt')
#print (GOV_BALL)

global_festivals_list = [GOV_BALL]
finalAnswer = select_festival("New Orleans") """
festivals = [0]
days = [0]
day_num = 0

# general setup for Processing draw window

def setup():
	global title_font
	global button_font
	global detail_font
	global small_font
	size(900,650)
	strokeWeight(2)
	title_font = createFont("Arial", 50)
	button_font = createFont("Arial", 32)
	detail_font = createFont("Arial", 22)
	small_font = createFont("Arial", 14)

# draw loop

def draw():
	global title_font
	global button_font
	global detail_font
	global small_font
	global screen
	global city
	global festival
	global genre
	global cities
	global genres
	global city_selected
	global genre_selected
	global band_selected
	global selected
	global bands
	global showtimes
	global Festival_Bros
	global frame
	global global_festivals_list
	global festivals
	global day_num
	rectMode(CENTER)

	# main menu page

	if (screen == 0):

		# place text and button outlines

		background(200)
		fill(100)
		rect(300,315,270,100)


		fill(200,0,0)
		rect(875,25,50,50)

		textFont(title_font)
		fill(0)
		textAlign(CENTER)
		text("Festival Bros", 450, 50)

		textFont(button_font)
		text("Find Festivals\nNear Me", 300, 300)

		textFont(button_font)
		text("Welcome!", 450, 100)

		textFont(detail_font)
		text("X",875,35)

		# read button press based on mouse location

		if (mousePressed and mouseX > 15 and mouseX < 285 and mouseY > 265 and mouseY < 365):
			screen = 1
			frame = 0

		if (mousePressed and mouseX > 315 and mouseX < 585 and mouseY > 265 and mouseY < 365):
			screen = 2
			frame = 0

		if (mousePressed and mouseX > 615 and mouseX < 885 and mouseY > 265 and mouseY < 365):
			screen = 3
			frame = 0

		if (mousePressed and mouseX > 850 and mouseX < 900 and mouseY > 0 and mouseY < 50 and frame > 10):
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

				#THIS IS THE CITY THE USER HAS SELECTED TO GET A FESTIVAL SUGGESTION FROM
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

				#THIS IS THE GENRE THE USER HAS SELECTED TO GET A FESTIVAL SUGGESTION FROM
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

			#THIS NEEDS TO BE THE SUGGESTED FESTIVAL FROM THE ALGORITHM
			festivals = select_festival(city)

		offset = 0
		if len(festivals)==0:
			text("No Matching Festivals",750,300)
		elif(festivals[0]==0):
			x=1
		else:
			for i in range(0,len(festivals)):
				# display the suggested festival
				text(festivals[i],750,200+offset)
				offset+=30

		if(city_selected != -1 and genre_selected != -1 and mousePressed and mouseX > 625 and mouseX < 875 and mouseY > 275 and mouseY < 325 and frame>5):

			#THIS NEED TO BE THE LINK TO THAT FESTIVALS WEBSITE (MAY NOT HAVE THIS YET)
			#link("https://github.com/ella-garcia/Festival_Bros")
			frame = 0

		fill(0)
		textFont(detail_font)
		text("Main Menu",825,50)

		fill(0,200,0)
		rect(825,550,100,100)
		fill(0)
		textFont(detail_font)
		text("Save to \n Text File",825,550)

		# read button press based on mouse location

		if (mousePressed and mouseX > 765 and mouseX < 885 and mouseY > 15 and mouseY < 65):
			screen = 0
			frame = 0

	# Scheduler Page

	if (screen == 2):

		background(200)
		textFont(title_font)
		fill(0)
		textAlign(CENTER)
		text("Festivals Near Me", 450, 50)

		if (selected == 0):

			# loop to create city buttons and determine which one is currently selected
			offset = 0
			for i in range(0,7):
				fill(200,50,50)
				rect(300,offset+150,150,50)
				fill(0)
				textFont(detail_font)
				text(cities[i],300,offset+160)
				if(mousePressed and mouseX > 225 and mouseX < 375 and mouseY > offset+125 and mouseY < offset+175 and frame > 5):

					#THIS IS THE CITY THE USER WANTS TO SEE ALL FESTIVALS FOR TO THEN CHOOSE WHICH ONE TO MAKE A SCHEDULE FOR
					festival = ''
					city2 = cities[i]
					festivals = city_festivals(city2,global_festivals_list)
				offset += 75

			offset = 0
			if (festivals[0] != -1 and festivals[0] != 0):
				for i in range(0,len(festivals)):
					fill(200,50,50)
					rect(500,offset+150,150,50)
					fill(0)
					textFont(detail_font)
					text(festivals[i].festival_name,500,offset+160)
					if(mousePressed and mouseX > 425 and mouseX < 575 and mouseY > offset+125 and mouseY < offset+175 and frame > 5):

						#THIS IS THE CITY THE USER WANTS TO SEE ALL FESTIVALS FOR TO THEN CHOOSE WHICH ONE TO MAKE A SCHEDULE FOR
						festival = festivals[i]
					offset += 75

			offset = 0
			if (festivals[0] != -1 and festivals[0] != 0 and festival != ''):
				for i in range(0,len(festival.days)):
					fill(200,50,50)
					rect(750,offset+300,150,50)
					fill(0)
					textFont(detail_font)
					text(festival.days[i].day,750,offset+300)
					if(mousePressed and mouseX > 675 and mouseX < 825 and mouseY > offset+275 and mouseY < offset+325 and frame > 5):
						day_num = i
						selected = 1
						bands = []
						showtimes = []
					offset += 75

			# text and button outlines

			fill(50,200,50)
			rect(825,40,120,25)

			fill(0)
			textFont(detail_font)
			text("Main Menu",825,50)

			# read button press based on mouse location

			if (mousePressed and mouseX > 765 and mouseX < 885 and mouseY > 15 and mouseY < 65):
				screen = 0
				frame = 0

		if (selected == 1):

			#THESE NEED TO BE THE ARTISTS AND TIMES FOR THE SELECTED FESTIVAL
			artists = []
			times = []
			for i in range(0,len(festival.days[day_num].shows)):
				artists.append(festival.days[day_num].shows[i].artist)
				times.append(str(festival.days[day_num].shows[i].start))

			# loop to create artist buttons and determine which one is currently selected
			offset = 0
			shift = 0
			for i in range(0,len(artists)):
				fill(200,50,50)
				rect(100+shift,offset+100,200,50)
				fill(0)
				textFont(small_font)
				text(artists[i],100+shift,offset+100)
				text(times[i],100+shift,offset+120)
				if(mousePressed and mouseX > 0+shift and mouseX < 200+shift and mouseY > offset+75 and mouseY < offset+125):
					band_selected = i
					enter_band = artists[i]
					enter_time = times[i]
					if enter_band not in bands and len(bands) <= 8:
						bands.append(enter_band)
						showtimes.append(enter_time)
				offset += 75
				if i == 8:
					shift+=220
					offset = 0

			textFont(button_font)
			text("My Schedule",760,100)
			line(600,120,890,120)

			offset2 = 0
			for i in range(0,len(bands)):
				textFont(small_font)
				text(bands[i],600,offset2+150)
				text(showtimes[i],820,offset2+150)
				line(600,offset2+170,890,offset2+170)
				offset2+=50

			fill(0,75,200)
			rect(800,600,120,50)

			fill(0)
			textFont(detail_font)
			text("Reset",800,610)

			if (mousePressed and mouseX > 740 and mouseX < 860 and mouseY > 575 and mouseY < 625):
				bands = []
				showtimes = []

			fill(50,200,50)
			rect(650,600,120,50)

			fill(0)
			textFont(detail_font)
			text("Save",650,610)

			if (mousePressed and mouseX > 590 and mouseX < 710 and mouseY > 575 and mouseY < 625):

				#THIS IS WHEN THE SAVE BUTTON IS PRESSED. NEED TO SEND VARIABLES "BANDS" AND "SHOWTIMES" (SCHEDULE USER HAS MADE)
				#BACK TO ALGORITHM TO BE PRINTED ON A TEXT FILE
				a=1

			fill(50,200,50)
			rect(825,40,120,25)

			fill(0)
			textFont(detail_font)
			text("Main Menu",825,50)

			# read button press based on mouse location

			if (mousePressed and mouseX > 765 and mouseX < 885 and mouseY > 15 and mouseY < 65):
				screen = 0
				selected = 0
				frame = 0

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

		if (mousePressed and mouseX > 765 and mouseX < 885 and mouseY > 15 and mouseY < 65):
			screen = 0
			frame = 0

	frame+=1

  





