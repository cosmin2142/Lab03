lista_strumenti=[]
lista_prestiti=[]
class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.__responsabile = responsabile
    @property
    def responsabile(self):
        return self.__responsabile
    @responsabile.setter
    def responsabile(self, responsabile):
        self.__responsabile = responsabile
        print(responsabile)

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            infile=open(file_path, 'r')
            for riga in infile:
                diz={}
                campo=riga.strip().split(',')
                diz["codice"]=campo[0]
                diz["tipo"]=campo[1]
                diz["marca"]=campo[2]
                diz["anno_acquisto"]=campo[3]
                diz["valore"]=campo[4]
                lista_strumenti.append(diz)

        except FileNotFoundError:
            print("File non trovato")



    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        lista_codici=[]
        for el in lista_strumenti:
            lista_codici.append(int(el["codice"].strip("S")))
        for el in lista_codici:
            max_codice=int(max(lista_codici))

        lista_strumenti.append({
            "codice": f"S{max_codice+1}",
            "tipo": tipo,
            "marca": marca,
            "anno_acquisto": int(anno_acquisto),
            "valore": int(valore)
        })

        return lista_strumenti[len(lista_strumenti) - 1]

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        lista_ordinata=sorted(lista_strumenti, key=lambda x: x["marca"])
        return lista_ordinata

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        codici_prestiti=[]
        for el in lista_prestiti:
            codici_prestiti.append(int(el["codice"].strip("P")))
        max_prestiti=0
        for el in codici_prestiti:
            max_prestiti=int(max(codici_prestiti))
        lista_strumenti_prestati=[]
        for el in lista_prestiti:
            lista_strumenti_prestati.append(el["id_strumento"])
        codici_strumenti=[]
        for el in lista_strumenti:
            codici_strumenti.append(el["codice"])
        if id_strumento in lista_strumenti_prestati:
            print("strumento già in prestito")
            raise Exception
        elif id_strumento not in codici_strumenti:
            print("strumento inesistente")
            raise Exception
        else:
            lista_prestiti.append({
                "codice": f"P{max_prestiti+1}",
                "data": data,
                "id_strumento": id_strumento,
                "cognome_allievo": cognome_allievo
            })
        return lista_prestiti[len(lista_prestiti) - 1]

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        cod_prestiti = []
        for el in lista_prestiti:
            cod_prestiti.append(el["codice"])
            if id_prestito==el["id_strumento"]:
                lista_prestiti.remove(el)

        if id_prestito not in cod_prestiti:
            print("codice prestito inesistente")
            raise Exception

