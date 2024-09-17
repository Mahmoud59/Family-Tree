import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestFamilyTree(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the sample family data
        client.post("/setup_sample_data/")

    def test_james_and_jenny_relationship(self):
        # Test relationship degree between James and Jenny (Expected: 3)
        response = client.post("/get_relationship_degree/", json={
            "member1_fullname": "James Doe",
            "member2_fullname": "Jenny Doe"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['degree'], 3)

    def test_john_and_james_relationship(self):
        # Test relationship degree between John and James (Expected: 2)
        response = client.post("/get_relationship_degree/", json={
            "member1_fullname": "John Doe",
            "member2_fullname": "James Doe"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['degree'], 2)

    def test_jenny_and_jane_relationship(self):
        # Test relationship degree between Jenny and Jane (Expected: 2)
        response = client.post("/get_relationship_degree/", json={
            "member1_fullname": "Jenny Doe",
            "member2_fullname": "Jane Doe"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['degree'], 2)

    def test_jason_and_jason_relationship(self):
        # Test relationship between same member should return 1
        response = client.post("/get_relationship_degree/", json={
            "member1_fullname": "Jason Doe",
            "member2_fullname": "Jason Doe"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['degree'], 1)

    def test_non_existent_member(self):
        # Test request with a non-existent member 1
        response = client.post("/get_relationship_degree/", json={
            "member1_fullname": "NonExistent",
            "member2_fullname": "Jenny Doe"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("Both members must exist", response.json()['detail'])

    def test_invalid_relationship(self):
        # Test request with a non-existent member 2
        response = client.post("/get_relationship_degree/", json={
            "member1_fullname": "Jenny Doe",
            "member2_fullname": "NonExistentMember"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("Both members must exist", response.json()['detail'])

    def test_cycle_in_relationship(self):
        # Create a cycle in the relationships
        response = client.post("/define_relationship/", json={
            "member1_fullname": "John Doe",
            "member2_fullname": "Jenny Doe",
            "relation": "CHILD"
        })
        self.assertEqual(response.status_code, 200)

        # Even though there's a cycle, the relationship degree between Jenny and John should still be 1
        response = client.post("/get_relationship_degree/", json={
            "member1_fullname": "Jenny Doe",
            "member2_fullname": "John Doe"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['degree'], 1)

        # The reverse should also return 1 since they are directly related
        response = client.post("/get_relationship_degree/", json={
            "member1_fullname": "John Doe",
            "member2_fullname": "Jenny Doe"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['degree'], 1)

if __name__ == '__main__':
    unittest.main()
