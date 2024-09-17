from typing import Optional, Dict, List
from pydantic import BaseModel

class Member:
    def __init__(self, fullname):
        self.fullname = fullname
        self.relationships: Dict[str, List[Member]] = {}

    def relationship_with(self, member, relation):
        if relation not in self.relationships:
            self.relationships[relation] = []
        self.relationships[relation].append(member)

    def __repr__(self):
        return self.fullname

class MemberInput(BaseModel):
    fullname: str
