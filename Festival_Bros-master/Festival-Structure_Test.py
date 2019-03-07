import unittest
import Festival_Structure

class TestFestivalAlgorithm():
    def test_createFestivalObject(self):
        self.AssertTrue(isinstance(Festival('ACL',[], ['Hip-Hop', 'EDM', 'Pop', 'Rock'], 'Austin', '2018-8-4', '2018-8-6'), type))

    def test_createStageObject(self):
        self.AssertTrue(isinstance(Stage("Main Stage", ["Eminem", "Brittany Spears"]), type))

    def test_createShowObject(self):
        self.AssertTrue(isinstance(Show("Eminem", "2018-9-31 21:30", "2018-9-31 22:30"), type))

if __name__ == '__main__':
	unittest.main()
