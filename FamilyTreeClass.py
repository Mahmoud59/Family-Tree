from collections import deque

from MemberClass import Member


class FamilyTree:
    def __init__(self):
        self.members = {}

    def add_member(self, fullname):
        if fullname in self.members:
            raise ValueError("Member already exists")
        member = Member(fullname)
        self.members[fullname] = member
        return member

    def define_relationship(self, member1_name, member2_name, relation):
        member1 = self.members.get(member1_name)
        member2 = self.members.get(member2_name)
        if not member1 or not member2:
            raise ValueError("Both members must exist")
        # Add bidirectional relationship
        member1.relationship_with(member2, relation)
        member2.relationship_with(member1, relation)  # Ensure bidirectional relationship

    def get_relationship_degree(self, member1_name, member2_name):
        member1 = self.members.get(member1_name)
        member2 = self.members.get(member2_name)
        if not member1 or not member2:
            raise ValueError("Both members must exist")
        return self._bfs_find_degree(member1, member2)

    def _bfs_find_degree(self, start_member, target_member):
        if start_member == target_member:
            return 1

        # BFS to find the shortest path between start_member and target_member
        queue = deque([(start_member, 0)])  # (current member, current degree)
        visited = set()

        while queue:
            current_member, degree = queue.popleft()

            if current_member == target_member:
                return degree

            visited.add(current_member)

            # Traverse all related members
            for relation, members in current_member.relationships.items():
                for member in members:
                    if member not in visited:
                        queue.append((member, degree + 1))

        return None
