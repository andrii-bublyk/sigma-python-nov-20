import config
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import requests
from datetime import datetime


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


def get_data() -> str:
    resp = requests.get(f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&symbol=BTC&market=USD"
                        f"&apikey={config.apikey}&datatype=csv")

    if resp.status_code != 200:
        raise ConnectionError()

    return resp.text


def save_data(data: str):
    with open(f"static/{config.file_name}", "w") as csv_file:
        csv_file.write(data)


def load_data_from_file() -> dict:
    row_data = pd.read_csv(f"static/{config.file_name}")

    timestamps_str = row_data["timestamp"].tolist()
    timestamps = [datetime.strptime(date, "%Y-%m-%d").date() for date in timestamps_str]

    values = row_data["close (USD)"].tolist()

    data = dict(zip(timestamps, values))
    return data


def make_layout(figure):
    app.layout = html.Div(children=[
        html.H1(children='Bitcoin currency'),

        dcc.Graph(
            id='example-graph',
            figure=figure
        )
    ])


if __name__ == '__main__':
    raw_bitcoin_currency = get_data()
    save_data(raw_bitcoin_currency)
    data = load_data_from_file()

    fig = px.line(x=list(data.keys()), y=list(data.values()))
    make_layout(fig)

    app.run_server(debug=True)
