import csv

class Espositori:
    def __init__(self, codice_espositore, nome, cognome):
        self.__codice_espositore = codice_espositore
        self.__nome = nome
        self.__cognome = cognome

    @property
    def codice_espositore(self):
        return self.__codice_espositore
    @property
    def nome(self):
        return self.__nome
    @property
    def cognome(self):
        return self.__cognome

    def __str__(self):
        return f"{self.__codice_espositore},{self.__nome} {self.__cognome}"


class Stand:
    def __init__(self, codice_stand, superficie, padiglione, prezzo):
        self.__codice_stand = codice_stand
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzo = prezzo

    @property
    def codice_stand(self):
        return self.__codice_stand
    @property
    def superficie(self):
        return self.__superficie
    @property
    def padiglione(self):
        return self.__padiglione
    @property
    def prezzo(self):
        return self.__prezzo

    def __str__(self):
        return f"{self.__codice_stand}, {self.__superficie}, {self.__padiglione}, {self.__prezzo}"


class Premium(Stand):
    def __init__(self, codice_stand, superficie, padiglione, prezzo, posizione):
        super().__init__(codice_stand, superficie, padiglione, prezzo)
        self.__posizione = posizione

    @property
    def posizione(self):
        return self.__posizione

    def __str__(self):
        return f"{super().__str__()}, {self.__posizione}"


class Prese(Stand):
    def __init__(self, codice_stand, superficie, padiglione, prezzo, prese):
        super().__init__(codice_stand, superficie, padiglione, prezzo)
        self.__prese = prese

    @property
    def prese(self):
        return self.__prese

    def __str__(self):
        return f"{super().__str__()}, {self.__prese}"


class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.espositori = {}
        self.stand = {}
        self.occupati = {}

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
            with open(file_path,  "r", encoding = "utf-8") as infile:
                reader = csv.reader(infile)

                for line in reader:
                    if line[0].startswith("E"):
                        codice_espositore = line[0]
                        nome = line[1]
                        cognome = line[2]
                        espositore = Espositori(codice_espositore,nome,cognome)
                        self.espositori[codice_espositore] = espositore

                    if line[0].startswith("S") and len(line) < 5:
                        codice_stand = line[0]
                        superficie = line[1]
                        padiglione = line[2]
                        prezzo = line[3]
                        stand = Stand(codice_stand, superficie, padiglione, prezzo)
                        self.stand[codice_stand] = stand

                    if len(line) == 5:
                        codice_stand = line[0]
                        superficie = line[1]
                        padiglione = line[2]
                        prezzo = line[3]
                        valore = line[4]
                        if valore.isdigit():
                            prese_elettriche = int(valore)
                            prese = Prese(codice_stand, superficie, padiglione, prezzo, prese_elettriche)
                            self.stand[codice_stand] = prese
                        else:
                            posizione = valore
                            premium = Premium(codice_stand, superficie, padiglione, prezzo,posizione)
                            self.stand[codice_stand] = premium
        except FileNotFoundError:
            raise Exception(f"File {file_path} non trovato")


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        if codice_stand not in self.stand:
            raise Exception(f"Stand {codice_stand} non trovato")

        if codice_espositore not in self.espositori:
            raise Exception(f"espositori {codice_espositore} non trovato")

        if codice_stand in self.occupati:
            raise Exception (f"Stand {codice_stand} già occupato")

        for esp in self.occupati.values():
            if esp.codice_espositore == codice_espositore:
                raise Exception (f"Espositore {codice_espositore} già assegnato a uno stand")

        if codice_stand not in self.occupati:
            assegnazione = Espositori(codice_espositore, None, None)
            self.occupati[codice_stand] = assegnazione
        return self.occupati


    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """

        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
