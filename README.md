# Family-Tree
 This app is a system to represent family trees.
 The system allow users to find and count the number of paths between any two
 family members.
 
## Installation
 - Go to the GitHib repo https://github.com/Mahmoud59/Family-Tree
 - Clone the repo
 - Create virtual environment beside the app to install the system packages.
   - `virtualenv venv`
 - Install packages.
   - `pip install -r requirements.txt`
 - Go to main.py file and run the app.
   - `uvicorn main:app --reload`
 - You can try 4 endpoints
   - You can add screenshot samples directly
     - POST request `http://127.0.0.1:8000/setup_sample_data/` <br><br>
   - Add member
     - POST request `http://127.0.0.1:8000/add_member/`
     - Body `{"fullname": "Jason Doe"}` <br><br>
   - Add Relation
     - POST request `http://127.0.0.1:8000/define_relationship/`
     - Body `{"member1_fullname": "Jezza Doe", "member2_fullname": "Jason Doe", "relation": "SPOUCE"}` <br><br>
   - Get relationship degree
     - POST request `http://127.0.0.1:8000/get_relationship_degree/`
     - Body `{"member1_fullname": "Jason Doe", "member2_fullname": "Jezza Doe"}`

## Unit Test
 - You can run test cases
   - `python -m unittest tests.py`