from django.test import TestCase
from django.test import Client
from rest_framework.response import Response
import os


# Create your tests here.
class AnalyzeTest(TestCase):
    def setUp(self):
        self.client = Client()
    def test_analyze(self):
        file_path = os.path.abspath("quantum_api\\file1.qasm")
        f = open(file_path, "r",encoding='utf-8')
        data = {
        'file_uploaded': f}
        response = self.client.post("http://localhost:8000/analyze/", data, format='multipart')
        correct_response = "Number of qubits: 2, Depth: 12, Gate Count: OrderedDict([('h', 10), ('x', 4), ('cx', 2), ('measure', 2)])"
        self.assertContains(response, correct_response)
        f.close()
    def test_with_error(self): 
        file_path = os.path.abspath("quantum_api\\file2.qasm")
        f = open(file_path, "r",encoding='utf-8')
        data = {
        'file_uploaded': f}
        response = self.client.post("http://localhost:8000/analyze/", data, format='multipart') 
        self.assertContains(response, "There was an error when trying to get the circuit")
        f.close()
        
        