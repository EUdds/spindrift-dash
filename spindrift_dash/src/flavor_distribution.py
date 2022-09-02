import pandas as pd
import plotly.express as px
from dash import dcc

from utils import Distribution

class FlavorDistribution(Distribution):
    def __init__(self, drinks_df: pd.DataFrame):
        super().__init__(drinks_df)
        self.flavor_count = self._get_flavor_count()
    
    def _get_flavor_count(self):
        dff = pd.DataFrame()
        dff['flavor_name'] = self.drinks['flavor_name'].value_counts().index
        dff['count'] = self.drinks['flavor_name'].value_counts().values
        return dff

    def pie_chart(self):
        fig = px.pie(self.flavor_count, values='count', names='flavor_name', title='Flavor Distribution')
        fig_cmp = dcc.Graph(figure=fig, id="flavor_distribution_pie_chart")
        return fig_cmp
    
    def bar_chart(self):
        fig = px.bar(self.flavor_count, x='flavor_name', y='count', color='flavor_name', barmode='group', title='Flavor Distribution')
        fig_cmp = dcc.Graph(figure=fig, id="flavor_distribution_bar_chart")
        return fig_cmp
    
