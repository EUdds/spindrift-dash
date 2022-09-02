import requests
import pandas as pd
import dash_bootstrap_components as dbc

from dash import html
from spindrift_dash.src.flavor_distribution import FlavorDistribution
from spindrift_dash.src.date_distribution import DateDistribution


class SpindriftData:
    def __init__(self, url):
        self.url = url
        self.flavors_json = None
        self.drinks_json = None
        self.flavors_df = None
        self.drinks_df = None
        self.flavor_distribution = None
        self.date_distribution = None
        self.total_drinks = 0
        self.refresh_data()

    
    def refresh_data(self):
        self.flavors_json = requests.get(self.url + "/flavors").json()
        self.drinks_json = requests.get(self.url + "/drinks").json()
        self.flavors_df = pd.DataFrame(self.flavors_json)
        self.drinks_df = pd.DataFrame(self.drinks_json)
        self.flavor_distribution = FlavorDistribution(self.drinks_df)
        self.date_distribution = DateDistribution(self.drinks_df)
        self.total_drinks = len(self.drinks_df)
    
    def add_drink_form(self):
        form = dbc.Form(action="/drinks/now", method="POST", id="add_drink_form", children=[
            html.Div(children=[
                dbc.Label("Flavor", html_for="flavor"),
                dbc.Select(id="flavor", name="flavor_id", options=[{"label": row['name'], "value": row['id']} for row in self.flavors_df.to_dict('records')]),
            ], className="mb-3"),
            html.Div(children=[
                dbc.Button("Add Drink", color="primary", type="submit")
            ], className="mb-3")
        ])
        return form
