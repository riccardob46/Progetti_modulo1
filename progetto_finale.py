import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#==================== PARTE 1 ====================
"""Importazione file csv"""
df = pd.read_csv("vendite.csv")

#==================== PARTE 2 ====================
print("\n---- PARTE 2 ----\n")

"""Stampa prime 5 righe, numero di righe e colonne, informazioni generali"""
print(f"Prime 5 righe del DataFrame: {df.head(5)}\n")

print(f"Numero di righe e colonne: {df.shape}\n")

print(f"Info del DataFrame: {df.info()}\n")

#==================== PARTE 3 ====================
print("\n---- PARTE 3 ----\n")

"""Aggiunta colonna Incasso calcolata come Quantità * Prezzo_unitario"""
df["Incasso"]= df["Quantità"] * df["Prezzo_unitario"]
df.to_csv("vendite.csv", index=False)
print(df.head(5)) #per verificare l'aggiunta

"""Calcolo incassso tot catena"""
incasso_totale_catena = df["Incasso"].sum()
print(f"Incasso Totale Catena: \n{incasso_totale_catena}\n")

"""Calcolo incasso medio per punto vendita"""
incasso_medio_negozio = df.groupby("Negozio")["Incasso"].mean().sort_values(ascending= False).round(2)
print(f"Incasso medio per punto vendita: \n{incasso_medio_negozio}\n")

"""Top 3 prodotti più venduti"""
top_3 = df.groupby("Prodotto")["Quantità"].sum().sort_values(ascending= False).head(3)
print(f"Top 3 prodotti più venduti: \n{top_3}\n")

"""Raggruppare i dati per negozio e prodotto e mostrare l'incasso medio"""
incasso_medio_per_prodotto = df.groupby(["Negozio", "Prodotto"])["Incasso"].mean()
print(f"Incasso medio negozio/prodotto: \n{incasso_medio_per_prodotto}")

#==================== PARTE 4 ====================
print("\n---- PARTE 4 ----\n")

"""Estrazione colonna "Quantità" dal DataFrame"""
quantità = df["Quantità"].to_numpy()

"""Calcolo media, minimo, massimo e deviazione standard"""
media_quantità_vendute = quantità.mean()
print(f"Quantità media vendite: {round(media_quantità_vendute)}\n")

quantità_minima = quantità.min()
print(f"Quantità minima venduta: {quantità_minima}\n")

quantità_massima = quantità.max()
print(f"Quantità massima venduta: {quantità_massima}\n")

dev_std_quantità = quantità.std()
print(f"Deviazione Standard delle Quantità vendute {dev_std_quantità}\n")

"""Creazione array 2D Quantità/Prezzo_unitario per calcolare incasso per ogni riga"""
prezzo_unitario = df["Prezzo_unitario"].to_numpy() #estraggo anche la colonna Prezzo_unitario dal DataFrame

array_2d = np.array([quantità, prezzo_unitario])

incassi_array = array_2d[0] * array_2d[1]

print(incassi_array)

"""Verifica della corrispondenza di valori con la colonna "Incasso" del DataFrame"""
if (incassi_array == df["Incasso"].to_numpy()).all():
    print("I risultati corrispondono")
else:
    print("Errore!")

#==================== PARTE 5 ====================

"""Creazione grafico a barre: incasso totale per ogni negozio"""
incasso_totale_negozio = df.groupby("Negozio")["Incasso"].sum()
plt.figure(figsize= (10,6))
incasso_totale_negozio.plot(kind= "bar", color= "skyblue", edgecolor= "black" )
plt.title("Incasso Totale Per Punto Vendita", fontsize= 16)
plt.xlabel("Punto Vendita", fontsize= 14)
plt.ylabel("Incasso Totale (€)", fontsize= 14)
plt.xticks(rotation= 45)
plt.tight_layout()
plt.show()

"""Creazione grafico a torta: percentuale incassi per ciascun prodotto"""
incasso_totale_prodotto = df.groupby("Prodotto")["Incasso"].sum()

plt.figure(figsize= (9,9))
plt.pie(incasso_totale_prodotto, labels= incasso_totale_prodotto.index, autopct= "%1.1f%%", startangle= 140)
plt.title("Percentuale Incassi Per Prodotto", fontsize= 16)
plt.axis("equal")
plt.tight_layout()
plt.show()

"""Creazione grafico a linee: andamento giornaliero degli incassi totali della catena"""
df["Data"] = pd.to_datetime(df['Data']) #conversione colonna Data nel giusto formato

andamento_giornaliero = df.groupby("Data")["Incasso"].sum().sort_index()

plt.figure(figsize=(12, 6))
plt.plot(andamento_giornaliero.index, andamento_giornaliero.values, marker= "o", linestyle= "-", color= "green", linewidth= 2)
plt.title("Andamento Giornaliero Degli Incassi Totali", fontsize= 16)
plt.xlabel("Data")
plt.ylabel("Incasso Totale (€)")
plt.grid(True, linestyle= '--', alpha= 0.6)
plt.xticks(rotation= 45)
plt.tight_layout()
plt.show()

#==================== PARTE 6 ====================
print("\n---- PARTE 6 ----\n")

"""Creazione ed aggiunta colonna 'Categoria'"""
categorie_prodotti = {
    "iPhone 15": "Smartphone e Tablet",
    "Smartphone Samsung Galaxy": "Smartphone e Tablet",
    "Tablet iPad Air": "Smartphone e Tablet",
    "MacBook Air M2": "Informatica e PC",
    "Laptop ASUS Vivobook": "Informatica e PC",
    "Hard Disk Esterno 2TB": "Accessori Informatica",
    "Monitor Gaming MSI": "Accessori Informatica",
    "Router Wi-Fi 6": "Accessori Informatica",
    "Mouse Wireless Logitech": "Accessori Informatica",
    "Smart TV LG 55 pollici": "TV e Multimedia",
    "Fotocamera Canon EOS": "TV e Multimedia",
    "Cuffie Sony Noise Cancelling": "TV e Multimedia",
    "Console PlayStation 5": "Gaming",
    "Smartwatch Apple Watch": "Wearable"
}

df["Categoria"] = df["Prodotto"].map(categorie_prodotti)
df.to_csv("vendite_analizzate.csv", index= False) 
print(df[["Prodotto", "Categoria"]].head(5)) #per verificare aggiunta colonna

incasso_totale_categoria = df.groupby("Categoria")["Incasso"].sum()
print(f"\nIncasso Totale per Categoria Prodotto: \n{incasso_totale_categoria}\n")

quantità_media_categoria = df.groupby("Categoria")["Quantità"].mean().sort_values(ascending= False)
print(f"Quantità media vendite per categoria: \n{round(quantità_media_categoria)}\n")

#==================== PARTE 7 ====================
print("\n---- PARTE 7 ----\n")

"""Creazione grafico combinato incasso medio per categoria + quantità media venduta"""
incasso_medio_categoria = df.groupby("Categoria")["Incasso"].mean().sort_values(ascending= False)
quantita_allineata = quantità_media_categoria.reindex(incasso_medio_categoria.index)

fig, ax1 = plt.subplots(figsize=(12, 7))
ax1.bar(incasso_medio_categoria.index, incasso_medio_categoria, color= "lightgreen", alpha= 0.7, label= "Incasso Medio (€)")
ax1.tick_params(axis= "y", labelcolor= "darkgreen")

ax2 = ax1.twinx() 
ax2.plot(incasso_medio_categoria.index, quantita_allineata, color= "red", marker= "o", linewidth= 2, label= "Quantità Media")
ax2.set_ylabel("Quantità Media", color= "red")
ax2.tick_params(axis= "y", labelcolor= "red")

plt.title("Rapporto tra incasso medio e media quantità vendute")

h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1+h2, l1+l2, loc="upper right")

fig.tight_layout()
plt.show()

"""Creazione funzione top_n_prodotti(n)"""
def top_n_prodotti(n):
    classifica_prodotti = df.groupby("Prodotto")["Incasso"].sum()

    top = classifica_prodotti.sort_values(ascending=False).head(n)
    
    return top

risultato = top_n_prodotti(5)

print(f"I primi 5 prodotti per incasso sono: \n{risultato}")