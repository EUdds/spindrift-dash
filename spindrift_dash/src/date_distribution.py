import pandas as pd
import plotly.express as px

from dash import dcc
from utils import Distribution

class DateDistribution(Distribution):
    def __init__(self, drinks_df: pd.DataFrame):
        super().__init__(drinks_df)
        self.date_count = self._get_date_count()
    
    def _get_date_count(self):
        self.drinks['date'] = self.drinks['date'].apply(lambda x: pd.Timestamp(x[:x.index("T")]))
        dff = self.drinks.groupby(['date', 'flavor_name'])['flavor_name'].count()
        dff = dff.to_frame()
        dff.columns = ['total']
        dff.reset_index(inplace=True)
        dff = dff.pivot(index='date', columns='flavor_name', values='total').fillna(0)
        dff['total'] = dff.sum(axis=1)
        dff.reset_index(inplace=True)
        return dff

    @property 
    def average_drinks_per_day(self):
        return self.date_count['total'].mean()
    
    @average_drinks_per_day.setter
    def average_drinks_per_day(self, value):
        raise AttributeError("Cannot set average_drinks_per_day")
    
    def pie_chart(self):
        fig = px.pie(self.date_count, values='total', names='date', title='Date Distribution')
        fig_cmp = dcc.Graph(figure=fig, id="date_distribution_pie_chart")
        return fig_cmp
    
    def bar_chart(self):
        dff = self.drinks.groupby(['date', 'flavor_name'])['flavor_name'].count()
        dff = dff.to_frame()
        dff.columns = ['total']
        dff.reset_index(inplace=True)
        fig = px.bar(dff, x='date', y='total', color="flavor_name", title='Date Distribution')
        fig_cmp = dcc.Graph(figure=fig, id="date_distribution_bar_chart")
        return fig_cmp
    
    def line_chart(self):
        fig = px.line(self.date_count, x='date', y='total', title='Date Distribution')
        fig_cmp = dcc.Graph(figure=fig, id="date_distribution_line_chart")
        return fig_cmp

