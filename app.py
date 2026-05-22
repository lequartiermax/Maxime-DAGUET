import plotly.express as px
import pandas as pd

données = pd.read_csv('https://raw.githubusercontent.com/lequartiermax/Maxime-DAGUET/main/ventes%20-%20ventes.csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-région.html')

print('ventes-par-région')

figure = px.pie(données, values='qte', names='produit', title='quantité vendue par produit')

figure.write_html('ventes-par-produit.html')

print('ventes-par-produit')

figure = px.pie(données, values='CA', names='produit', title='CA par produit' )

figure.write_html('CA-par-produit.html')

print('CA-par-produit')
