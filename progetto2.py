import numpy as np

#========== Parte 1 ==========
nome = "Marco"
cognome = "Rossi"
cf= "RSSMRC66A01H501Y"
eta = 60
peso = 81.3
analisi = ["Colesterolo", "Urine", "Trigliceridi"]

nome1 = "Giorgia"
cognome1 = "Bianchi"
cf = "BNCGRG96A41F205S"
eta1 = 30
peso1 = 50.6
analisi1 = ["Emocromo", "Creatina", "Sideremia"]

nome2 = "Luca"
cognome2 = "Verdi"
cf = "VRDLCU81A01F839O"
eta2 = 45
peso2 = 90.0
analisi2 = ["Ferritina", "Emocromo", "Azotemia"]

#========== Parte 2 ==========
class Paziente:
    def __init__(self, nome, cognome, codice_fiscale, eta, peso, analisi_effettuate, risultato_analisi):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.eta = eta
        self.peso = peso
        self.analisi_effettuate = analisi_effettuate
        self.risultato_analisi = risultato_analisi #========== Parte 4 ==========

    def scheda_personale(self):
        return f"Nome: {self.nome}, Cognome: {self.cognome}, CF: {self.codice_fiscale}, Età: {self.eta}, Peso: {self.peso}, Analisi Effettuate: {self.analisi_effettuate}"
    def statistiche_analisi(self): #========== Parte 4 ==========
        return f"Media valori: {np.mean(self.risultato_analisi)}, Valore minimo: {np.min(self.risultato_analisi)}, Valore massimo: {np.max(self.risultato_analisi)}, Deviazione standard: {np.std(self.risultato_analisi)}"
    

class Medico: 
    def __init__(self, nome, cognome, specializzazione):
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione

    def visita_paziente(self, paziente):
        return f"Il medico {self.nome} {self.cognome} sta visitando il paziente {paziente.nome} {paziente.cognome}"

class Analisi:
    limite_analisi = {
              "Colesterolo":150,
              "Trigliceridi":100,
              "Glicemia":80,
              "Transaminasi":110,
              "Creatinina":150,
              "Azotemia":200,
              "Ferritina":100,
              "Urine":90,
              "Emocromo":150,
              "Sideremia":70
              }
    
    def __init__(self, tipo_di_analisi, risultato):
        self.tipo_di_analisi = tipo_di_analisi
        self.risultato = risultato

    def valuta(self):
        limite = self.limite_analisi.get(self.tipo_di_analisi, 100)

        if self.risultato > limite:
            return f"Valore fuori norma (Limite: {limite})"
        else:
            return "Valore nella norma"

#========== Parte 3 ========== 
arr_colesterolo = np.random.randint(100, 170, size = 10)
print("\nPARTE 3")
print(arr_colesterolo)
print(f"Media dei valori: {np.mean(arr_colesterolo)}")
print(f"Valore minimo: {np.min(arr_colesterolo)} e Valore massimo: {np.max(arr_colesterolo)}")
print(f"Deviazione standard: {np.std(arr_colesterolo)}")

#========== Parte 5 ==========
print("\nTEST\n")
"""Lista Medici"""
medici = [
    Medico("Andrea", "Bianchi", "Cardiologia"),
    Medico("Sara", "Neri", "Ortopedia"),
    Medico("Luca", "Gialli", "Medicina Generale")
]

"""Lista Pazienti"""
pazienti = [
    Paziente("Marco", "Rossi", "RSSMRC66A01H501Y", 60, 81.3, 
             ["Colesterolo", "Urine", "Trigliceridi"], [160, 85, 110]),
    Paziente("Giorgia", "Bianchi", "BNCGRG96A41F205S", 30, 50.6, 
             ["Emocromo", "Creatina", "Sideremia"], [140, 0.9, 75]),
    Paziente("Luca", "Verdi", "VRDLCU81A01F839O", 45, 90.0, 
             ["Ferritina", "Emocromo", "Azotemia"], [120, 155, 180]),
    Paziente("Anna", "Neri", "NRANNA90M41L219Z", 34, 62.5, 
             ["Glicemia", "Colesterolo", "Urine"], [95, 145, 88]),
    Paziente("Paolo", "Bruni", "BRNPLA75T12H501U", 49, 78.0, 
             ["Transaminasi", "Creatinina", "Azotemia"], [105, 130, 210])
]

"""Ciclo per stampa scheda, visite, analisi e statistiche"""
for i, paziente in enumerate(pazienti):
    print(f"\n--- Paziente {i+1} ---")

    print(f"Scheda: {paziente.scheda_personale()}")

    medico_assegnato = medici[i % len(medici)] #assegnazione casuale medici
    print(f"Visita: {medico_assegnato.visita_paziente(paziente)}")

    print("Dettaglio Analisi:")
    for j, nome_analisi in enumerate(paziente.analisi_effettuate):
        valore = paziente.risultato_analisi[j]
        esame = Analisi(nome_analisi, valore)
        print(f"  - {nome_analisi}: {valore} -> {esame.valuta()}")


    print(f"Statistiche Mediche: {paziente.statistiche_analisi()}")
