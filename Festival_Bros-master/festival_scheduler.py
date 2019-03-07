import random.randint
import datetime

#Function that, given a location and genre, makes a list of possible festivals that the user would want to attend (including time conflicts, they will be accounted for in the scheduler)
def select_festival(location, genre, global_festivals_list):
	possible_festivals = []	
	#Iterate through the global festivals list
	for festival in global_festivals_list:
		#check that the item in the list matches location and genre, add to possibility list
		if (festival.location == location) and (genre in festival.genres):
			possible_festivals.append(festival)
	#Return error if there are no festivals
	if len(possible_festivals) == 0:
		return "ERROR: There are no festivals near this location."
	#Return a list of all festivals in the desired location
	else: 
		return possible_festivals

def get_days(festival):
	if len(festival.days) == 0:
		return "ERROR: Festival has no days."
	else:
		return festival.days

def get_shows(day):
	if len(day.shows) == 0:
		return "ERROR: day has no shows."
	else:
		return day.shows

#Function to make a schedule of random shows and return a list of strings with artist/time
def random_shows(festival):
	#Create the empty Schedule
	schedule = []

	#Make a list of the Festival Days, randomly select a day
	festival_days = get_days(festival)
	if type(festival_days) == str:
		return festival_days

	#From the list, make another list of all combinations of shows possible with non-conflicting times
	day_index = random.randint(0, (len(festival_days)))
	day = festival_days[day_index]

	#Get shows from the days
	shows = get_shows(day)
	if type(shows) == str:
		return shows

	#Make a list of shows before 1:00
	time = 13.0
	shows_before_1 = []
	for show in shows:
		if show.start <= time:
			shows_before_1.append(show)

	#Get a random index to select a random show from this list
	show_index = random.randint(0, (len(shows_before_1)))
	schedule.append(shows_before_1[show_index])

	#Select a random show that starts after the selected show ends
	show_target = schedule[0]
	end_of_day = False 
	while not end_of_day:
		for show in shows:
			if show.start >= show_target.end:
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
			showstring = "Artist: " + str(show.artist) + "Start Time: " + str(show.start)
			show_strings.append(showstring)
		return show_strings

# Function that schedules shows based on user picks
def festival_scheduler(festival):
	user_schedule = []

	#Make a list of the Festival Days, randomly select a day
	festival_days = get_days(festival)
	if type(festival_days) == str:
		return festival_days

	#Get shows from the days
	shows = get_shows(day)
	if type(shows) == str:
		return shows

	#User chooses shows they want to watch


	#Check that the schedule list was made, return an error if not
	if len(schedule) == 0:
		return "ERROR: The list is empty-- there is no schedule."
	else: 
		show_strings = []
		#Create list of strings to send back to GUI
		for show in schedule: 
			showstring = "Artist: " + str(show.artist) + "Start Time: " + str(show.start)
			show_strings.append(showstring)
		return show_strings

# Function to save & write shows into text file
def save_shows(artistList, timeList):

	# write to text file
	f = open('MyFestivalSchedule.txt', 'w')

	f.write('My Festival Schedule:')

	for i in range(len(artistList)):
		f.write('Artist: ' + artistList(i) + ' | Time: ' + timeList(i))

	# output string that file has been created
	f.close()

Takes in show objects save into text file
'''
1. Display list of festivals, user chooses 1 festival
2. Display list of shows at festival
3. User chooses shows they want to watch
4. Schedule shows
5. Display user's schedule
'''