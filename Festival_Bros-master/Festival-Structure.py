import datetime

class Show(object):
    # The class "constructor" - It's actually an initializer
    def __init__(self, artist, start, end):
        start_str = start
        start_time = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')

        end_str = start
        end_time = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')

        self.artist = artist
        self.start = start_time
        self.end = end_time

class Stage(object):
    def __init__(self, name, shows):
        self.stage_name = name
        self.shows = shows

class Festival(object):
    def __init__(self, name, stages, genres, city, start, end):
        start_str = start
        start_day = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')

        end_str = start
        end_day = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')

        self.festival_name = name
        self.genres = genres
        self.locqtion = city
        self.stages = stages
        self.startday = start_day
        self.endday = end_day

def main():
    festivals = []
    ACL = Festival('ACL',[], ['Hip-Hop', 'EDM', 'Pop', 'Rock'], 'Austin', '2018-8-4', '2018-8-6')
    FLOG_GNAW = Festival('Flog Gnaw',[], ['Hip-Hop', 'R&B'], 'Los Angeles', '2018-11-5', '2018-8-7')
    Ultra_Music = Festival('Ultra Music Festival',[], ['EDM', 'Pop', 'Rock'], 'Miami', '2019-3-29', '2019-3-31')
    Aspen = Festival('Aspen Music Festival',[], ['Classical'], 'Denver', '2019-6-27', '2019-8-18')
    Lolla = Festival('Lollapalooza',[], ['Hip-Hop', 'Pop', 'Rock'], 'Chicago', '2018-8-2', '2018-8-5')
    Boston_Calling = Festival('Boston Calling Music Festival',[], ['Hip-Hop', 'EDM', 'Pop', 'Rock'], 'Boston', '2019-5-24', '2019-5-26')
    Electric = Festival('Electric Zoo',[], ['Hip-Hop', 'EDM', 'Pop', 'Rock', 'Alternative'], 'New York City', '2018-8-31', '2018-9-2')