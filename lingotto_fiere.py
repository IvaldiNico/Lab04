from csv import reader

class Espositori:
    def __init__(self, codice, nome, cognome):
        self.__codice = codice
        self.__nome = nome
        self.__cognome = cognome


class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo):
        self.__codice = codice
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzo = prezzo

        @property
        def codice(self):
            return self.__codice
        @property
        def superficie(self):
            return self.__superficie
        @property
        def padiglione(self):
            return self.__padiglione
        @property
        def prezzo(self):
            return self.__prezzo


class Premium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo, prese, posizione):
        super().__init(codice, superficie, padiglione, prezzo)
        self.__prese = prese
        self.__posizione = posizione


class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.espositori = {}
        self.stand = {}
        self.premium = {}

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        try:
            with open(file_path) as infile:
                reader = reader(infile)

                for line in reader:
                    if campi[0].startswith("E"):
                        campi[0] = codice



        # TODO

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
