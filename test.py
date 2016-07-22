# coding=utf-8
import requests
import unittest
import json

api='https://api.douban.com/v2/book/search'

def search_book(**args):
        return requests.get(api, params = dict(**args))

class TestDoubanBookSearchAPI(unittest.TestCase):
    
    def setUp(self):
        with open('mock.json') as f:
            self.mock_data = json.load(f)
        
    def test_default_args(self):
        self.assertEqual(search_book(q = 'linux').json(), search_book(q = 'linux',
                             start = 0, count = 20).json())
        self.assertNotEqual(search_book(q = 'linux').json(), search_book(q = 'linux',
                             start = 0, count = 100).json())

    def test_count_max(self):
        self.assertEqual(len(search_book(q = u'我们',count = 100).json()['books']),
                         len(search_book(q ='linux', count = 99999).json()['books']))
        self.assertNotEqual(101,
                         len(search_book(q ='linux', count = 101).json()['books']))

    def _test_invalid_res(self):
        self.assertEqual(400, search_book().status_code)

    def test_response_struct(self):
        self._test_invalid_res()
        
        data = search_book(q = self.mock_data['title'])
        real_data = data.json()
        self.assertEqual(data.status_code, 200)
        self.assertIsInstance(real_data, dict, msg = "response should be a"
                            "dict but was a {}".format(type(real_data)))
        self.assertEqual(len(real_data), 4)
        self.assertIn('start', real_data)
        self.assertIn('count', real_data)
        self.assertIn('total', real_data)
        self.assertIn('books', real_data)
    
    

    def test_book_struct(self):
        real_data = search_book(q = self.mock_data['title']).json()
        self.assertIsInstance(real_data['books'][0], dict, msg = "books item"
                            " type is {}".format(type(real_data['books'][0])))
        self.assertIsInstance(self.mock_data, dict, msg = "self.mock_data"
                            " type is {}".format(type(self.mock_data)))
        for book in real_data['books']:
            self.assertIsInstance(book, dict)
            self.assertEqual(book.keys().sort(), self.mock_data.keys().sort())  