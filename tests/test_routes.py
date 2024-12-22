import unittest
from app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_status(self):
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)

    def test_predict(self):
        data = {
            "destination_port": 80,
            "flow_duration": 500,
            "flow_bytes_per_s": 1000,
            "total_fwd_packets": 10,
            "packet_length_mean": 200
        }
        response = self.app.post('/predict', json=data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()