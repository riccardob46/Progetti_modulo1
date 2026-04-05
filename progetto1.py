# ====== PARTE 1 ======
print("\n=== PARTE 1  ===\n")

titolo_libro = str("Python per principianti")
n_copie = int(5)
prezzo_medio = float(12.99)

print(f"Titolo: {titolo_libro}")
print(f"Numero copie: {n_copie}")
print(f"Prezzo medio: {prezzo_medio}")

if n_copie > 0:
    print("Disponibile")
else:
    print("Non Disponibile")

# ====== PARTE 2 =====
print("\n=== PARTE 2 ===\n")

lista_libri = ["Python per principianti", "Cercasi Energia", "Il tesoro al piano terra", "Essere Leader", "Lavorare con l'Intelligenza Emotiva", "La via della bellezza"]
diz_libri = {"Python per principianti": 2, "Cercasi Energia": 5, "Il resoro al piano terra": 8, "Essere Leader": 1, "Lavorare con l'Intelligenza Emotiva": 3, "La via della bellezza": 2}
for k, v in diz_libri.items():
    print(k, v)
utenti_registrati = {"Mario Rossi", "Marco Verdi", "Nicola Bianchi", "Giorgio Viola", "Anna Rose", "Giulia Margherite", "Francesca Camelie", "Elena Tulipani" }
print(utenti_registrati) 
utenti_registrati.add("Riccardo Berti")
print(utenti_registrati)

# ====== PARTE 3 ======
print("\n=== PARTE 3 ===\n")

class Libro:
    def __init__(self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili
    
    def info(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Anno: {self.anno}, Copie disponibili: {self.copie_disponibili}"
    
libro1 = Libro("La via della bellezza", "Vito Mancuso", 2018, 1)
print(libro1.info())

class Utente:
    def __init__(self, nome, età, id_utente):
        self.nome = nome
        self.età = età
        self.id_utente = id_utente

    def scheda(self):
        return f"Nome: {self.nome}, Età: {self.età}, User: {self.id_utente}"
    
utente1 = Utente("Riccardo Berti", 28, "_riccardo_1998")
print(utente1.scheda())

class Prestito:
    def __init__(self, utente, libro, giorni):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni

    def dettagli(self):
        info_utente = self.utente.scheda()
        info_libro = self.libro.info()
        return f"\nDETTAGLI PRESTITO\n {info_utente}\n {info_libro}\n Durata prestito: {self.giorni}"
    
prestito1 = Prestito(utente1, libro1, 15)
print(prestito1.dettagli())

# ====== PARTE 4 ======
print("\n=== PARTE 4 ===\n")

registro_prestiti = []

def presta_libro(utente, libro, giorni):
    if libro.copie_disponibili > 0:
        libro.copie_disponibili -= 1

        nuovo_prestito = Prestito(utente, libro, giorni)

        registro_prestiti.append(nuovo_prestito)

        print(f"Prestito registrato per '{libro.titolo}'")
        return nuovo_prestito
    else:
        print(f"Il libro '{libro.titolo}' non è disponibile al momento")
        return None


libro2 = Libro("Cercasi Energia", "Andrea Moccia", 2020, 5)
libro3 = Libro("Essere Leader", "Daniel Goleman", 2022, 0) # Errore per 0 copie disponibili
utente2 = Utente("Marco Verdi", 30, "m_verdi_94")
utente3 = Utente("Anna Rose", 25, "arose_99")


presta_libro(utente1, libro1, 7) 
presta_libro(utente2, libro2, 14)
presta_libro(utente3, libro3, 10)

print("Aggiornamento copie disponibili\n")
for libro in [libro1, libro2, libro3]:
    print(f"{libro.titolo}: {libro.copie_disponibili} copie rimanenti")

print("Prestiti Effettuati\n")
for prestito in registro_prestiti:
    print(prestito.dettagli())
    