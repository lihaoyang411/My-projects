
import datetime

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
    # open file for reading
    file = open (txt_file, "r")

    #set count
    count = 0

    

    festival = file.readline().strip()
    print ('Fest: ' + festival)
    genres = file.readline().strip()
    genre_list = genres.split('/')
    print (genre_list)
    location = file.readline().strip()
    print ('Location: ' + location)
    print ('Fest: ' + festival)
    fest_start = file.readline().strip()
    print ('Fest Start: ' + fest_start)
    fest_end = file.readline().strip()
    print ('Fest End: ' + fest_end)
    

    i = file.readline().strip()
    print (i)

    while i != 'END':
        day = i
        print ('Day: ' + day)
        i = file.readline().strip()
        
        while i != ';':

            artist = i
            #print ('Artist: ' + artist)
            
            time = file.readline().strip()
            #print ('Time: ' + time)
            
            
            splittime = time.split('-')
            
            
            start_split = splittime[0].split(':')
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
    
    print ('Done')
        
        
    
    
def main():
  '''fest_days = []
  shows = []
  shows2 = []
  shows3 = []
  # open file for reading
  file = open ("gov.txt", "r")

  i = file.readline().strip()

  while i != 'END':
  festival = file.readline().strip()
  print (festival)

  date = file.readline().strip()
  print (date)

  day = file.readline().strip()
  print (day)

  artist = file.readline().strip()
  print (artist)

  time = file.readline().strip()
  print (time)

  splittime = time.split('-')
  print (splittime)

  start = date + ' ' + splittime[0]
  end = date + ' ' + splittime[1]

  show1 = Show(artist, start, end)

  print (show1.artist)
  print (show1.start.time())
  print (show1.end.time())

  shows.append(show1)

  i = file.readline().strip()

  while i != ';':
    artist = i

    time = file.readline().strip()
    

    splittime = time.split('-')
    

    start = date + ' ' + splittime[0]
    end = date + ' ' + splittime[1]

    show1 = Show(artist, start, end)

    print (show1.artist)
    print (show1.start.time())
    print (show1.end.time())

    shows.append(show1)

    i = file.readline().strip()

  fest_days.append(Festival_Day(day, shows))

  festival = file.readline().strip()
  print (festival)

  date = file.readline().strip()
  print (date)

  day = file.readline().strip()
  print (day)

  artist = file.readline().strip()
  print (artist)

  time = file.readline().strip()
  print (time)

  splittime = time.split('-')
  print (splittime)

  start = date + ' ' + splittime[0]
  end = date + ' ' + splittime[1]

  show1 = Show(artist, start, end)

  print (show1.artist)
  print (show1.start.time())
  print (show1.end.time())

  shows2.append(show1)

  i = file.readline().strip()

  while i != ';':
    artist = i

    time = file.readline().strip()
    

    splittime = time.split('-')
    

    start = date + ' ' + splittime[0]
    end = date + ' ' + splittime[1]

    show1 = Show(artist, start, end)

    print (show1.artist)
    print (show1.start.time())
    print (show1.end.time())

    shows2.append(show1)

    i = file.readline().strip()

  fest_days.append(Festival_Day(day, shows2))

  festival = file.readline().strip()
  print (festival)

  date = file.readline().strip()
  print (date)

  day = file.readline().strip()
  print (day)

  artist = file.readline().strip()
  print (artist)

  time = file.readline().strip()
  print (time)

  splittime = time.split('-')
  print (splittime)

  start = date + ' ' + splittime[0]
  end = date + ' ' + splittime[1]

  show1 = Show(artist, start, end)

  print (show1.artist)
  print (show1.start.time())
  print (show1.end.time())

  shows3.append(show1)

  i = file.readline().strip()

  while i != ';':
    artist = i

    time = file.readline().strip()
    

    splittime = time.split('-')
    

    start = date + ' ' + splittime[0]
    end = date + ' ' + splittime[1]

    show1 = Show(artist, start, end)

    print (show1.artist)
    print (show1.start.time())
    print (show1.end.time())

    shows3.append(show1)

    i = file.readline().strip()
    
  fest_days.append(Festival_Day(day, shows3))
  
  print (fest_days)

  GOV_BALL = Festival('Governors Ball', [], ['Hip-Hop', 'EDM', 'Pop', 'Rock'], 'Austin', '2018-8-4', '2018-8-6')'''
  
  GOV_BALL = create_festival ('gov_copy.txt')
  print (GOV_BALL)

  
main()
