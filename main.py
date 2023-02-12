import plotly.express as px
import pandas as pd

def read_data():
    # Charger les données from data.gouv
    df = pd.read_csv("rehabilitation_logementsocial_surface_prix.csv", delimiter=";")
    print(f'Our data: {df}')
    # Créer un graphique en colonnes avec Plotly Express
    fig = px.bar(df, x="Région", y="Construction_Prixderevient_logement", barmode="group")

    # Afficher le graphique
    fig.show()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_data()
