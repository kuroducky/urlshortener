#Firstly, it is important to note that unit testing is performed so as to test the quality of the code 
#and ensure that they are fit for use. It is to test the correctness of the code


#In my backend, there are 2 specific HTTP requests, where one is a GET request and the other is a POST request
import unittest
import requests
from main import app
import json
app.testing=True

#Do take note that in this test case, we are actually just making use of the backend server that was set up intially 
class TestAPI(unittest.TestCase):
    '''

    # Uncomment this line of code to test with different inputs

    print("Enter shortened string: ")
    shortened_string = input()
    get_route = "http://localhost:8000/"+shortened_string #This url that was given as a test
    '''

    get_route = "http://localhost:8000/sgEOsK" 
    def test_get_route(self):
        response = requests.get(self.get_route)
        self.assertEqual(response.status_code, 200)
        print("GET request unit test completed with success")
    

    def test_post_route(self):
        with app.test_client() as client:
            sent = {"params":{"url_string": "testtest"}}
            result = client.post('/encode', data=json.dumps(sent), content_type ='application/json')
            # check result from server with expected data
            self.assertEqual(result.status_code,200)
        print("POST request unit test completed with success")

if __name__ == "__main__":
    tester = TestAPI()
    tester.test_get_route()
    tester.test_post_route()
