import unittest
import json
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_start_test_throughput(self):
        response = self.app.post('/start_test', data=json.dumps({'type': 'throughput'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['status'], 'throughput test started')

    def test_start_test_latency(self):
        response = self.app.post('/latency_test', data=json.dumps({'target': '8.8.8.8'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertIn('result', response_data)  # Check if 'result' is in the response

    def test_start_test_fault(self):
        response = self.app.post('/fault_test', data=json.dumps({'target': '8.8.8.8'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertIn('status', response_data)  # Check if 'status' is in the response

    def test_start_test_speed(self):
        response = self.app.post('/speed_test', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertIn('download_speed_mbps', response_data)
        self.assertIn('upload_speed_mbps', response_data)

    def test_start_test_invalid_type(self):
        response = self.app.post('/start_test', data=json.dumps({'type': 'invalid_type'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['error'], 'Invalid test type')

if __name__ == "__main__":
    unittest.main()
