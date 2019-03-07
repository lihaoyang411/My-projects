import datetime
global GOV_BALL

class Show(object):
    # The class "constructor" - It's actually an initializer 
    def __init__(self, artist, start, end):
        start_str = start
        start_time = datetime.datetime.strptime(start_str, '%m-%d-%Y %H:%M')

        end_str = end
        end_time = datetime.datetime.strptime(end_str, '%m-%d-%Y %H:%M')

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
        start_day = datetime.datetime.strptime(start_str, '%Y-%m-%d')

        end_str = start
        end_day = datetime.datetime.strptime(end_str, '%Y-%m-%d')
        
        self.festival_name = name
        self.genres = genres
        self.location = city
        self.days = days
        self.startday = start_day
        self.endday = end_day
        
  # create a Graph object

def main():
  fest_days = []
  shows = []
  shows2 = []
  shows3 = []
  # open file for reading
  file = open ("gov.txt", "r")

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

  GOV_BALL = Festival('Governors Ball', [], ['Hip-Hop', 'EDM', 'Pop', 'Rock'], 'Austin', '2018-8-4', '2018-8-6')

  

  
main()