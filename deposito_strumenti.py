lista=[]
class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        infile=open(file_path, 'r')
        for riga in infile:
            diz={}
            campo=riga.strip().split(';')
            diz["codice"]=int(campo[0])
            diz["tipo"]=campo[1]
            diz["marca"]=campo[2]
            diz["anno_acquisto"]=campo[3]
            diz["valore"]=campo[4]
            lista.append(diz)


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        codice=0
        for el in lista:
            max_codice=int(max(el["codice"]))
        lista.append({
            "codice": max_codice+1,
            "tipo": tipo,
            "marca": marca,
            "anno_acquisto": anno_acquisto,
            "valore": valore
        })
        print(f"aggiunto: {tipo}, {marca}, {anno_acquisto}, {valore}")

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
