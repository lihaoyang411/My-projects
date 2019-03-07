#Import modules
import unittest
import festival_scheduler
import Gov_Festival

class test_festival_methods():
	#Test when there are festivals
	def test_select_festival(self):
		location = 'Austin'
		genre = 'Rock'
		test_possible_festivals = select_festival(location, genre, [GOV_BALL])

		for festival in test_possible_festivals:
			self.AssertEqual(festival.location, location)
			self.AssertIn(genre, festival.genres)
  
	#test that there are no results (-1)
	def test_no_results_select_festival(self):
		location = 'NotReal'
		genre = 'FakeNews'
		test_possible_festivals = select_festival(location, genre, global_festivals_list)

		self.AssertEqual(test_possible_festivals, -1)

	def test_randomizer(self):
		string = 'cow'
		random_list = random_shows(GOV_BALL)
		self.AssertNotEqual((len(random_list)), 0)
		self.AssertEqual(random_list[0].type, string.type)
		
if __name__ == '__main__':
	unittest.main()