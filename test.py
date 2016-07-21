import requests
import unittest
import json

api='https://api.douban.com/v2/book/search'

def search_book(q="", tag="", start=0, count=20, **args):
        return requests.get(api, params={'q':q, 'tag': tag, 
                                'count':count, 'start':start})

class TestDoubanBookSearchAPI(unittest.TestCase):
    
    def setUp(self):
        with open('mock.json') as f:
            self.mock_data = json.load(f)
        self.real_data = search_book(q=self.mock_data['title'])
        self.assertEqual(self.real_data.status_code, 200)
        #self.assertIsInstance(self.real_data.json(), list, msg=
        #                    "self.real_data type is {}".format(type(self.real_data.json())))
        self.assertIsInstance(self.real_data.json()['books'][0], dict, msg = "books item"
                            " type is {}".format(type(self.real_data.json()['books'][0])))
        self.assertIsInstance(self.mock_data, dict, msg = "self"
                            ".mock_data type is {}".format(type(self.mock_data)))

    def test_structure(self):
        for book in self.real_data.json()['books']:
            self.assertIsInstance(book, dict)
            self.assertEqual(book.keys(), self.mock_data.keys())  