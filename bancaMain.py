from Conto import Conto

if __name__ == '__main__':

    conto1 = Conto('adcd', 'efg')
    conto1.scrivi_info()
    conto1.deposita(1000)
    conto1.scrivi_info()
    conto1.preleva(100)


