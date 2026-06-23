from database.DAO import DAO
import networkx as nx
class Model:

    def __init__(self):
        self._squadre=None
        self._graph=nx.Graph()
        self._guadagni=None
        self._idMap={}


    def getAnniModel(self):

        return DAO.getAnni()

    def getSquadreAnnoModel(self,anno):

        self._squadre=DAO.getSquadreAnno(anno)
        self._guadagni=DAO.getSalariTeam(anno)
        for g in self._guadagni:
            self._idMap[g[1]]=g[2]
            print(g[1])
            print(self._idMap[g[1]])



        return self._squadre
    def creaGrafo(self):
        nodi=self._squadre
        self._graph.add_nodes_from(nodi)

        for i in range(len(self._squadre)):
            for j in range(i+1,len(self._squadre)):
                s1=self._squadre[i]
                s2=self._squadre[j]
                g1=self._idMap[s1.idTeam]
                g2=self._idMap[s2.idTeam]
                if not self._graph.has_edge(s1,s2):
                    self._graph.add_edge(s1,s2,weight=g1+g2)



        return self._graph

