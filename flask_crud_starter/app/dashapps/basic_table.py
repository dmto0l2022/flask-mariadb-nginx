# This Code was written by Ann Marie - a Plotly Forum Moderator
from dash import Dash, dcc, html, Input, Output, dash_table, no_update  # Dash version >= 2.0.0
import pandas as pd
import plotly.express as px
import json
import requests

app = Dash(__name__, requests_pathname_prefix='/wsgi_app2/')

df = px.data.gapminder()
df["id"] = df.index
# print(df.head(15))
dff = df[df.year == 2007].copy()
dff['create'] = "create"
dff['read'] = "read"
dff['update'] = "update"
dff['delete'] = "delete"
columns = ["country", "continent", "lifeExp", "pop", "gdpPercap", "create", "read", "update", "delete"]
initial_active_cell = {"row": 0, "column": 0, "column_id": "country", "row_id": 0}

app.layout = html.Div(
    [
        html.Div(
            [
                dash_table.DataTable(
                    id="table",
                    columns=[{"name": c, "id": c} for c in columns],
                    data=dff.to_dict("records"),
                    page_size=10,
                    sort_action="native",
                    active_cell=initial_active_cell,
                ),
            ],
            style={"margin": 50},
            className="five columns"
        ),
        html.Div(id="output-div", className="six columns"),
    ],
    className="row"
)


@app.callback(
    Output("output-div", "children"), Input("table", "active_cell"),
)
def cell_clicked(active_cell):
    if active_cell is None:
        return no_update

    row = active_cell["row_id"]
    print(f"row id: {row}")

    country = df.at[row, "country"]
    print(country)

    col = active_cell["column_id"]
    print(f"column id: {col}")
    print("---------------------")   
    
    cell_value = dff.iat[active_cell['row'], active_cell['column']]
    
    return cell_value, country

##json.dumps(list(active_cell))
