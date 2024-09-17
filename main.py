from fastapi import FastAPI, HTTPException

from FamilyTreeClass import FamilyTree
from MemberClass import MemberInput
from RelationshipClass import RelationshipInput, RelationshipDegreeInput

app = FastAPI()

# Instantiate family tree
family_tree = FamilyTree()


@app.post("/add_member/")
def add_member(member_input: MemberInput):
    try:
        family_tree.add_member(member_input.fullname)
        return {"message": f"Member {member_input.fullname} added successfully."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/define_relationship/")
def define_relationship(relationship_input: RelationshipInput):
    try:
        family_tree.define_relationship(
            relationship_input.member1_fullname,
            relationship_input.member2_fullname,
            relationship_input.relation
        )
        return {"message": f"Relationship '{relationship_input.relation}' between {relationship_input.member1_fullname} and {relationship_input.member2_fullname} defined successfully."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/get_relationship_degree/")
def get_relationship_degree(relationship_degree_input: RelationshipDegreeInput):
    try:
        degree = family_tree.get_relationship_degree(
            relationship_degree_input.member1_fullname,
            relationship_degree_input.member2_fullname
        )
        if degree is None:
            raise HTTPException(status_code=404, detail="No relationship found.")
        return {"degree": degree}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to set up the sample family data
@app.post("/setup_sample_data/")
def setup_sample_data():
    try:
        family_tree.add_member("Jenny Doe")
        family_tree.add_member("Jimmy Doe")
        family_tree.add_member("John Doe")
        family_tree.add_member("Jane Doe")
        family_tree.add_member("James Doe")
        family_tree.add_member("Jezza Doe")
        family_tree.add_member("Jason Doe")

        family_tree.define_relationship("Jenny Doe", "Jimmy Doe", "CHILD")
        family_tree.define_relationship("Jimmy Doe", "Jezza Doe", "CHILD")
        family_tree.define_relationship("Jenny Doe", "John Doe", "CHILD")
        family_tree.define_relationship("John Doe", "Jane Doe", "SPOUSE")
        family_tree.define_relationship("Jane Doe", "James Doe", "SIBLING")
        family_tree.define_relationship("James Doe", "Jason Doe", "CHILD")
        family_tree.define_relationship("Jason Doe", "Jezza Doe", "SPOUSE")

        return {"message": "Sample family data set up successfully."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
