from django.test import TestCase
from django.test import Client
# Create your tests here.
class QuestionMethodTests(TestCase):
    def testPollsHome(self):
        c=Client()
        response=c.get('/polls/')
        self.assertEquals(response.status_code,200)




