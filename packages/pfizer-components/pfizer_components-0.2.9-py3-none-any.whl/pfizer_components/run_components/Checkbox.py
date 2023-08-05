from dash import html, dcc
import dash
import os
import dash_bootstrap_components as dbc

current_directory = os.getcwd()
file_name = '../assets/dbc.css'
file_path = os.path.join(current_directory, '../assets', file_name)
app = dash.Dash(external_stylesheets=[file_path])

app.layout = html.Div([
    html.Div(className='dbc-row-selectable',
             children=[
                 html.H3(className='label', children="Label"),
                 dcc.Checklist(
                     options=[{'label': html.Span("January", className='checkboxfont'), 'value': 'M1', },
                              {'label': html.Span("Feb", className='checkboxfont'), 'value': 'M2'},
                              {'label': html.Span("Mar", className='checkboxfont'), 'value': 'M3'}],
                     value=['M2', 'M3']),
                 dbc.Checklist(className="checkbox2", options=[{'label': 'APR', 'disabled': True}],
                               inputStyle={'border': '1px solid #858D97', 'background-color': '#DEE0E6'}),
                 dbc.Checklist(className="checkbox2", options=[{'label': 'MAY'}], ),
                 dcc.Checklist(className="checkbox2", options=['JUN'])],
             style={'position': 'relative',
                    'width': 300,
                    'height': 184,
                    'top': 122,
                    'left': 54,
                    'border': '1px solid #7B61FF',
                    'border-radius': '1px',
                    'box-sizing': 'border-box',
                    'font-family': 'Inter'})],
    style={'backgroundColor': '#ffffff', 'margin': 0})

if __name__ == '__main__':
    app.run_server(port=8103, debug=True)
