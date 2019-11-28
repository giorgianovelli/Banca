class Conto(object):
    def __init__(self, iban, cf):
        self.iban = iban
        self.cf = cf
        self.saldo = 0.0

    def preleva(self, importo):
        if importo < self.saldo :
            self.saldo -=  importo
            print("Prelevato %d. Nuovo saldo: %d" %(importo, self.saldo))
            return True
        else:
            return False

    def deposita(self, importo):  # controllare che importo sia valido
        self.saldo += importo
        return True

    def scrivi_info(self):
        print("Info conto: %s %s %d " % (self.iban, self.cf, self.saldo))







