import pandas as pd
from dash import dcc

class Distribution:
    def __init__(self, raw_drinks_df: pd.DataFrame):
        self.drinks = self._expand_flavor_name(raw_drinks_df)
    
    def _expand_flavor_name(self, raw_df: pd.DataFrame) -> pd.DataFrame:
        df = raw_df.copy()
        df['flavor_name'] = df.apply(lambda row: row['flavor']['name'], axis=1)
        return df
    
    def pie_chart(self) -> dcc.Graph:
        raise NotImplementedError()
    
    def bar_chart(self) -> dcc.Graph:
        raise NotImplementedError()