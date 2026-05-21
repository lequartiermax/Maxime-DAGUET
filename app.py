import plotly.express as px
import pandas as pd

données = pd.read_csv('http://github.com/lequartiermax/Maxime-DAGUET/blob/main/ventes%20-%20ventes.csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par region')

figure.write_html('ventes-par-region.html')

figure = px.pie(données, values='qte', names='produit', title='quantité vendue par produit')

figure.write_html('ventes-par-région.html')

figure = px.pie(données, values='CA', names='produit', title='CA par produit' )

figure.write_html('CA-par-région.html')
