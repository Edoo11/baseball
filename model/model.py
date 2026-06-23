from database.DAO import DAO

class Model:

    def __init__(self):
        pass

    def getAnniModel(self):

        return DAO.getAnni()

    def getSquadreAnnoModel(self,anno):
       # print(f"MODEL:")
       # print(DAO.getSquadreAnno(anno))
        return DAO.getSquadreAnno(anno)