import flet as ft
import networkx as nx


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._grafo=None
    def caricaDDanni(self):
        anni = self._model.getAnniModel()
        for a in anni:
            self._view._ddAnno.options.append(

                ft.dropdown.Option(a)

            )
    def getSquadreAnnoController(self,e):
        anno=self._view._ddAnno.value
       # print(anno)
        squadre = self._model.getSquadreAnnoModel(anno)
       # print(squadre)
        self._view._txtOutSquadre.controls.append(
            ft.Text(f"squadre:{len(squadre)}")
        )
        for s in squadre:
             #print(s)
             self._view._txtOutSquadre.controls.append(
                 ft.Text(s.nameCode)
             )
             self._view._ddSquadra.options.append(
                 ft.dropdown.Option(key=s,text=s.nameCode)
             )




        self._view.update_page()

    def handleCreaGrafo(self, e):
        self._grafo=self._model.creaGrafo()
        print(f"CONTROLLI GRAFO ------- nodi:{len(self._grafo.nodes)}")


    def handleDettagli(self, e):
        print("DENTRO DETTAGLI")
        s=self._view._ddSquadra.value
        print(s)
        if s in self._grafo.nodes:
            print("dentro il grafo")
        else:
            print("NON e dentro")

        vicini = list(self._grafo.neighbors(s))
        print(vicini)



        pass

    def handlePercorso(self, e):
        pass