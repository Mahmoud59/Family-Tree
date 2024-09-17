from pydantic import BaseModel

class RelationshipInput(BaseModel):
    member1_fullname: str
    member2_fullname: str
    relation: str


class RelationshipDegreeInput(BaseModel):
    member1_fullname: str
    member2_fullname: str
