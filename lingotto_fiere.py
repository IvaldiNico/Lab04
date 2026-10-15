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

    def __eq__(self, other):
        if isinstance(other, Espositori):
            return self.codice_espositore == other.codice_espositore
        return False

    def __str__(self):
        return f"{self.__codice_espositore},{self.__nome} {self.__cognome}"


class Stand:
    def __init__(self, codice_stand, superficie, padiglione, prezzo):
        self.__codice_stand = codice_stand
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzo = prezzo
        self.__espositore = None

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
    @prezzo.setter
    def prezzo(self, prezzo):
        self.__prezzo = prezzo

    @property
    def espositore(self):
        return self.__espositore
    @espositore.setter
    def espositore(self, espositore):
        self.__espositore = espositore

    @property
    def disponibile(self):
        return self.__espositore is None

    @property
    def stato(self):
        if self.disponibile:
            return "Disponibile"
        return "Non disponibile"

    def nuovo_prezzo(self):
        return self.prezzo

    def __lt__(self, other):
        return self.nuovo_prezzo() < other.nuovo_prezzo()

    def __str__(self):
        return f"{self.__codice_stand}: Standard | {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo {self.prezzo}€ - {self.stato}"


class Premium(Stand):
    def __init__(self, codice_stand, superficie, padiglione, prezzo, posizione):
        super().__init__(codice_stand, superficie, padiglione, prezzo)
        self.__posizione = posizione

    @property
    def posizione(self):
        return self.__posizione

    def nuovo_prezzo(self):
        return self.prezzo * 1.30

    def __str__(self):
        return f"{self.codice_stand}: Premium | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.nuovo_prezzo()}€ - Posizione: {self.__posizione} - {self.stato}"


class Prese(Stand):
    def __init__(self, codice_stand, superficie, padiglione, prezzo, prese):
        super().__init__(codice_stand, superficie, padiglione, prezzo)
        self.__prese = prese

    @property
    def prese(self):
        return self.__prese

    def nuovo_prezzo(self):
        return self.prezzo * (1 + 0.07 * self.__prese)

    def __str__(self):
        return f"{self.codice_stand}: Prese Extra | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.nuovo_prezzo()}€ - Prese aggiuntive: {self.__prese} - {self.stato}"


class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.espositori = {}
        self.stand = {}

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""

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
                    prezzo = float(line[3])
                    stand = Stand(codice_stand, superficie, padiglione, prezzo)
                    self.stand[codice_stand] = stand

                if len(line) == 5:
                    codice_stand = line[0]
                    superficie = line[1]
                    padiglione = line[2]
                    prezzo = float(line[3])
                    valore = line[4]

                    if valore.isdigit():
                        prese_elettriche = int(valore)
                        prese = Prese(codice_stand, superficie, padiglione, prezzo, prese_elettriche)
                        self.stand[codice_stand] = prese

                    else:
                        posizione = valore
                        premium = Premium(codice_stand, superficie, padiglione, prezzo,posizione)
                        self.stand[codice_stand] = premium



    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        if codice_stand not in self.stand:
            raise Exception(f"Stand {codice_stand} non trovato")

        if codice_espositore not in self.espositori:
            raise Exception(f"Espositore {codice_espositore} non trovato")

        if not self.stand[codice_stand].disponibile:
            raise Exception(f"Stand {codice_stand} già occupato")

        espositore = self.espositori[codice_espositore]
        for s in self.stand.values():

            if s.espositore == espositore:
                raise Exception(f"Espositore {codice_espositore} già assegnato a uno stand")

        self.stand[codice_stand].espositore = espositore


    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for espositore in self.espositori.values():
            codice_stand = None

            for s in self.stand.values():
                if s.espositore == espositore:
                    codice_stand = s.codice_stand
                    break

            if codice_stand is None:
                print(f"Nessuno stand assegnato all'espositore {espositore}")

            else:
                print(f"Stand {codice_stand} assegnato all'espositore {espositore}")


    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        return sorted(self.stand.values())
