from dataclasses import dataclass
@dataclass
class Team:
    idTeam:int
    nameCode:str


    def __eq__(self, other):
        return self.idTeam==other.idteam
    def __hash__(self):
        return hash(self.idTeam)
    def __str__(self):
        return f"idTeam:{self.idTeam} -- nameCode:{self.nameCode}"