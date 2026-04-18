import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#---- PARTE 1 ----
print("\n---- PARTE 1 ----\n")

nome = str("Riccardo Berti")
età = int(28)
saldo_conto = float(2500.10)
vip = True
print(nome, età, saldo_conto, vip)

destinazioni = ["Roma", "Las Vegas", "Tokio", "Madrid", "Londra"]
print(destinazioni)

"""Dizionario che associa destinazione a prezzo medio"""
dest_medium_price= {"Roma": 1500, "Las Vegas": 3000, "Tokio": 2500, "Madrid": 1000, "Londra": 1800}
print(dest_medium_price)

#---- PARTE 2 ----
print("\n---- PARTE 2 ----\n")

class Clienti:
    def __init__(self, nome, età, vip):
        self.nome = nome
        self.età = età
        self.vip = vip

    def info(self):
        return f"Nome: {self.nome}, Età: {self.età}, Vip: {self.vip}"

class Viaggio:
    def __init__(self, destinazione, prezzo, durata):
        self.destinazione = destinazione
        self.prezzo = prezzo
        self.durata = durata

class Prenotazione:
    def __init__(self, cliente, viaggio):
        self.cliente = cliente
        self.viaggio = viaggio

        self.prezzo_finale = self.calcola_prezzo()
    
    def calcola_prezzo(self):
        prezzo_base = self.viaggio.prezzo
        if self.cliente.vip:
            return prezzo_base * 0.9
        return prezzo_base
    
    def dettagli(self):
        info_cliente = self.cliente.info()
        return (f"--- Dettagli Prenotazione ---\n"
                f"Cliente: {info_cliente}\n"
                f"Destinazione: {self.viaggio.destinazione}\n"
                f"Durata: {self.viaggio.durata} giorni\n"
                f"Prezzo Finale: {self.prezzo_finale:.2f}€")

"""Test perte 2"""
cliente1 = Clienti("Riccardo Berti", 28, True)
viaggio1 = Viaggio("Roma", 1800, 10)
print(cliente1.info())

prenotazione1 = Prenotazione(cliente1, viaggio1)
print(prenotazione1.calcola_prezzo())
print(prenotazione1.dettagli())

# ---- PARTE 3 ----
print("\n---- PARTE 3 ----\n")

np.random.seed(42)
prenotazioni_simulate = np.random.randint(200,2001, size= 100)
print(prenotazioni_simulate)
print("Prezzo medio: ", np.mean(prenotazioni_simulate))
print("Prezzo minimo: ", np.min(prenotazioni_simulate))
print("Prezzo massimo: ", np.max(prenotazioni_simulate))
print("Deviazione standard: ", np.std(prenotazioni_simulate))

media = np.mean(prenotazioni_simulate)
sopra_media = np.sum(prenotazioni_simulate > media)
prenotazioni_sopra_media = (sopra_media / len (prenotazioni_simulate)) * 100
print(f"Percentuale prenotazioni sopra la media: {prenotazioni_sopra_media}%")

# ---- PARTE 4 ----
print("\n---- PARTE 4 ----\n")

dati = {
    "Cliente": ["Riccardo Berti", "Marco Rossi", "Giulia Verdi", "Marta Gialli", "Luca Neri", "Valerio Foscarini", "Zeno Baldovini", "Tiziano Marrone", "Enea Brambilla", "Flavio Torrigiani", "Ginevra Malaspina", "Ambra Dell'Orto", "Sveva Vinciguerra", "Livia Sereni", "Loris Pellegrini", "Mirko Altomonte", "Mario Bianchi" ],
    "Destinazione": ["Roma", "Tokio", "Las Vegas", "Madrid", "Londra", "Tokio", "Londra", "Roma", "Roma", "Madrid", "Tokio", "Las Vegas", "Roma", "Londra", "Madrid", "Roma", "Marrakech"],
    "Prezzo": [1800, 2000, 1600, 1200, 1900, 900, 1050, 2000, 2300, 3000, 1500, 1890, 2100, 850, 600, 1000, 1550],
    "Giorno_Partenza": ["2025-05-10", "2025-07-20", "2025-08-01", "2025-08-16", "2025-12-05", "2025-06-15", "2025-09-10", "2025-12-20", "2025-04-18", "2025-07-04", "2025-03-10", "2025-07-20", "2025-04-10", "2025-08-15", "2025-06-30", "2025-12-26", "2025-04-10"],
    "Durata": [10, 6, 7, 5, 6, 4, 6, 7, 8, 15, 6, 9, 7, 4, 3, 5, 5],
    "Incasso": [1950, 2200, 1750, 1320, 2100, 1000, 1170, 2210, 2450, 3480, 1610, 2000, 2320, 970, 710, 1180, 1390]
}


df = pd.DataFrame(dati)
print(df)

incasso_totale = df["Incasso"].sum()
print("\nIncasso totale: ", incasso_totale)

incasso_medio_destinazione = df.groupby("Destinazione")["Incasso"].mean()
print("\nIncasso medio destinazione: ", incasso_medio_destinazione)

top_destinazioni = df["Destinazione"].value_counts().head(3)
print("\nTop 3 destinazioni: ", top_destinazioni)

# ---- PARTE 5 ----

"""Grafico incasso/destinazione"""
incasso_destinazione = df.groupby("Destinazione")["Incasso"].sum()
destinazioni= incasso_destinazione.index
valori= incasso_destinazione.values

plt.figure(figsize= (10, 6))
plt.bar(destinazioni, valori, color="skyblue", edgecolor="black")
plt.title("Incasso totale per destinazione", fontsize= 14)
plt.xlabel("Destinazioni", fontsize= 12)
plt.ylabel("Incasso (€)", fontsize= 12)
plt.grid(True, linestyle= "--", alpha= 0.7)
plt.show()

"""Grafico andamento giornaliero incassi"""
df["Giorno_Partenza"] = pd.to_datetime(df["Giorno_Partenza"])
df = df.sort_values("Giorno_Partenza")

plt.figure(figsize= (10,6))
plt.plot(df["Giorno_Partenza"], df["Incasso"], marker= "o", linestyle= "--", color= "green")
plt.title("Andamento vendite 2025", fontsize= 14)
plt.xlabel("Data di partenza", fontsize= 12)
plt.ylabel("Incasso (€)", fontsize= 12)
plt.grid(True, linestyle= "--", alpha= 0.7)
plt.xticks(rotation= 45)
plt.tight_layout()
plt.show()

"""Grafico percentuale vendite per destinazione"""
vendite_destinazione = df["Destinazione"].value_counts()

plt.figure(figsize= (8,8))
plt.pie(vendite_destinazione, labels= vendite_destinazione.index, autopct= "%1.1f%%",)
plt.title("Percentuale di vendite per destinazione", fontsize= 14)
plt.show()

# ---- PARTE 6 ----
print("\n---- PARTE 6 ----\n")

continenti = {
    "Roma": "Europa",
    "Las Vegas": "America",
    "Tokio": "Asia", 
    "Madrid": "Europa",
    "Londra": "Europa",
    "Africa": "Marrakech"
}

df["Continente"] = df["Destinazione"].map(continenti)

incasso_per_categoria = df.groupby("Continente")["Incasso"].sum()
print("Incasso totale per continente: ", incasso_per_categoria)

durata_media_per_continente = df.groupby("Continente")["Durata"].mean().round().astype(int)
print("\nDurata media del viaggio per continente: ", durata_media_per_continente)

df.to_csv("prenotazioni_analizzate.csv", index= False)

# ---- PARTE 7 ----
print("\n---- PARTE 7 ----\n")

def top_clienti(df_input, n):
    risultato = df_input["Cliente"].value_counts().head(n)
    return risultato
print("Top 3 clienti: ", top_clienti(df, 3))

"""Grafico combinato incasso medio/durata media"""

media_settore = df.groupby('Continente').agg({
    "Incasso": "mean",
    "Durata": "mean"
})

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.bar(media_settore.index, media_settore["Incasso"], color= "skyblue", alpha=0.7, label= "Incasso Medio (€)")
ax1.set_xlabel("Continente")
ax1.set_ylabel("Incasso Medio (€)", color= "blue")
ax1.tick_params(axis= "y", labelcolor= "blue")


ax2 = ax1.twinx() 

ax2.plot(media_settore.index, media_settore["Durata"], color= "red", marker= "D", linewidth= 2, label= "Durata Media (Giorni)")
ax2.set_ylabel("Durata Media (Giorni)", color= "red")
ax2.tick_params(axis= "y", labelcolor= "red")

plt.title("Analisi Media per Continente")
fig.tight_layout()
plt.show()