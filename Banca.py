from Conto import Conto


class Banca:


    def __init__(self, nome, numeroconti, radiceiban):
        self._nome = nome
        self._numeroconti = numeroconti
        self._listaConti = []
        self._radiceiban = radiceiban
        self._contatoreattivi = 0


    def aggiungi_conto(self, cf):  # generatore di iban

        if self._contatoreattivi < self._numeroconti:
            conto = Conto(self._radiceiban, cf)
            self._listaConti.append(conto)
            print("nuovo conto aggiunto")
            self._contatoreattivi += 1

    def totale_saldi(self):
        tot_saldi = 0
        for conto in self._listaConti:
            tot_saldi += conto.saldo
