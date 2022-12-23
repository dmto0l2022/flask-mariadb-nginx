# This Code was written by Ann Marie - a Plotly Forum Moderator
from dash import Dash, dcc, html, Input, Output, dash_table, no_update  # Dash version >= 2.0.0
import pandas as pd
import plotly.express as px
import json
import requests
###

import requests
import json


class MakeApiCall():

    def get_data(self, api):
        response = requests.get(f"{api}")
        if response.status_code == 200:
            print("sucessfully fetched the data")
            self.formatted_print(response.json())
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")

    '''def get_user_data(self, api, parameters):
        response = requests.get(f"{api}", params=parameters)
        if response.status_code == 200:
            print("sucessfully fetched the data with parameters provided")
            self.formatted_print(response.json())
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")
    '''
    def formatted_print(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)
    '''
    def __init__(self, api):
        # self.get_data(api)

        parameters = {
            "username": "kedark"
        }
        self.get_user_data(api, parameters)
    '''
###


app = Dash(__name__, requests_pathname_prefix='/wsgi_app2/')

##data_request = requests.get('/plots/getall')
url = "http://10.154.0.20:8004/plots/getall/"
#url = "http://localhost:8002/todo/list/1"
#data_request = requests.get(url="http://0.0.0.0:8002/todo/list/1")
##url = "http://dev4.dmtools.info:8002/todo/list/1"
#url = "http://10.154.0.20:8004/todo/list/1"
##10.154.0.20

r = requests.get(url, 
                 headers={'Accept': 'application/json'})

print(f"Response: {r.json()}")

#data_request = requests.get(url=url)
#text = json.dumps(data_request, sort_keys=True, indent=4)
#print(text)
#MakeApiCall().get_data(url)
##data_request = requests.get(url)
#print(data_request)
##data_frame = pd.read_json(data_request)
##print(data_frame)
##dff = data_frame.copy()
df = px.data.gapminder()
df["id"] = df.index
# print(df.head(15))
dff = df[df.year == 2007].copy()
dff['create'] = "create"
dff['read'] = "read"
dff['update'] = "update"
dff['delete'] = "delete"
columns = ["country", "continent", "lifeExp", "pop", "gdpPercap", "create", "read", "update", "delete"]
#columns = ["id", "plotid", "name", "create", "read", "update", "delete"]
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
    
    cell_value = dff.iat[active_cell['row'], active_cell['column'] + 1]
    
    ##http://127.0.0.1:5000/query-example?plotid=Python
    
    return cell_value, country

##json.dumps(list(active_cell))
