import dash_bootstrap_components as dbc

from dash import Dash, html
from datetime import datetime
from dateutil import tz

from_zone = tz.tzutc()
to_zone = tz.tzlocal()

from spindrift_dash.src.Spindrift import SpindriftData

app = Dash(external_stylesheets=[dbc.themes.CYBORG])

data = SpindriftData("http://localhost:8000")

def serve_layout() -> dbc.Container:
    data.refresh_data()

    all_drinks_table_header = [
        html.Thead(html.Tr([html.Th("Date"), html.Th("Flavor")]))
    ]
    all_drinks_table_body = []

    for drink in data.drinks_df.itertuples():
        clean_date_str = drink.date[:drink.date.index(".")] if "." in drink.date else drink.date
        utc = datetime.strptime(clean_date_str, '%Y-%m-%dT%H:%M:%S')
        local = utc.replace(tzinfo=from_zone).astimezone(to_zone)
        local = local.strftime('%m-%d-%Y %H:%M')
        all_drinks_table_body.append(html.Tr([html.Td(local), html.Td(drink.flavor['name'])]))

    all_drinks_table = dbc.Table(all_drinks_table_header + all_drinks_table_body, bordered=True, hover=True)
    return dbc.Container([
        dbc.Row([
            dbc.Container(
                dbc.Alert("What's Up Drifter? You've drank %d Spindrift!" % data.total_drinks, color="primary")
            )
        ]),
        dbc.Row([
            dbc.Row([html.H1("Drink Stats")]),
            dbc.Row([
                dbc.Col(dbc.Badge("Average Spindrift Per Day"), md=12),
                dbc.Col(dbc.Badge("%.1f" % data.date_distribution.average_drinks_per_day, color="primary"), md=12)
            ]),
        ]),
        dbc.Row([
                dbc.Col(data.flavor_distribution.pie_chart(), md=6), dbc.Col(data.flavor_distribution.bar_chart(), md=6)
        ]),
        dbc.Row([
                dbc.Col(data.date_distribution.line_chart(), md=6), dbc.Col(data.date_distribution.bar_chart(), md=6)
        ]),
        dbc.Row([
            dbc.Container([
                dbc.Col(all_drinks_table, md=12),
                dbc.Col([data.add_drink_form()], md=12)
            ])
        ]),
    ])

app.layout = serve_layout

if __name__ == "__main__":
    app.run_server(debug=True)