import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

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
        for s in squadre:
             self._view._txtOutSquadre.controls.append(
                 ft.Text(s.nameCode)
             )

        self._view.update_page()

    def handleCreaGrafo(self, e):
        pass

    def handleDettagli(self, e):
        pass

    def handlePercorso(self, e):
        pass