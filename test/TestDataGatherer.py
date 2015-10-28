from src.train_data_gatherer import TrainDataGatherer
import unittest

class TestDataGatherer(unittest.TestCase):

    def test_get_train_data(self):
        TrainDataGatherer().get

if __name__ == '__main__':
    unittest.main()
