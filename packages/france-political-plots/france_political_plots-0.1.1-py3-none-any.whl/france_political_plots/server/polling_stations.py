from dash import Dash, dcc, html, Input, Output, callback
from typing import Self, List, Dict, Any
import json
import pandas as pd
import dash_ag_grid as dag
import dash_mantine_components as dmc
import dash_iconify as dic
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
from ..utils import Pkg, Assets, download, progress, cout,get_each, spinner

FULL_SIZE_STYLE = {
    'width':'100vw',
    'height':'90vh'
}

CONFIG = {'displayModeBar': False, 'responsive': True}

class Dashboard:
    def __new__(cls) -> Self:
        cls.server = None
        cls.app = None
        return cls
    
    @classmethod
    def make(cls) -> Dash:
        plot_numbers = list(range(10))
        url = lambda num: f"https://github.com/arnos-stuff/bureaux-vote-postgis/releases/download/v0.0.3/plot.scores.bureaux.map.part.{num}.json.zip"
        metadata_url = "https://github.com/arnos-stuff/bureaux-vote-postgis/releases/download/v0.0.3/plot.scoring.metadata.table.csv.zip"
        urls = [url(i) for i in plot_numbers]
        
        datas = []
        for raw in get_each(urls = urls):
            datas += [
                json.loads(raw)
            ]
        figs = []
        load = progress.add_task(description="Loading...", filename="Loading unzipped files..", total=len(datas))
        with progress:
            for js in datas:
                if isinstance(js, str):
                    js = json.loads(js)
                figs += [
                    go.Figure(js)
                ]
                progress.advance(load)

        progress.remove_task(load)
        metadata = pd.read_csv(metadata_url)
                        
        external_stylesheets = [
            'https://codepen.io/chriddyp/pen/bWLwgP.css',
            "https://fonts.googleapis.com/css2?family=Fira+Sans:wght@300;400;500;600;700&display=swap",
            ]

        app = Dash(__name__, external_stylesheets=external_stylesheets, title="LFI 2022 Spending")

        textFilterOpts = {
            "filterOptions": ["contains", "notContains"],
            "debounceMs": 200,
            "suppressAndOrCondition": True,
        }
        
        defaultColDef = {
            "flex": 1,
            "sortable": True,
            "filter": True,
            'floatingFilter': True,
            
        }
        
        columnDefs = [
            {
                'field': col, 
                'filter': 'agTextColumnFilter',
                'filterParams': textFilterOpts,
                'sortable': True, 
                'headerName': col
                } 
            for col in metadata.columns
        ]
        
        cout.log("Building AG-Grid...")
        
        grid = dag.AgGrid(
            columnDefs=columnDefs,
            rowData=metadata.to_dict('records'),
            className='ag-theme-material',
            defaultColDef=defaultColDef,
            columnSize="sizeToFit",
            style= FULL_SIZE_STYLE,
        )

        
        @callback(
            Output("download-dataframe-csv", "data", allow_duplicate=True),
            Input("btn_csv", "n_clicks"),
            prevent_initial_call=True,
            
        )
        def func(n_clicks):
            return dcc.send_data_frame(metadata.to_csv, "government-spending.csv")
        
        components = html.Div([
            dcc.Tabs([
                
                *[
                    dcc.Tab(label='Usual Spending', children=[
                        html.Div([
                            dcc.Graph(
                            figure=g,
                            style=FULL_SIZE_STYLE,
                            config=CONFIG
                        )
                        ]
                        )
                    ])
                    for g in figs
                ]
                ,
                
                ]),
                dcc.Tab(label='Data', children=[
                    html.Div([
                        grid,
                        dmc.Button("Download as CSV", variant="gradient", id="btn_csv", leftIcon=dic.DashIconify(icon="ic:baseline-download")),
                        dcc.Download(id="download-dataframe-csv"),
                    ],
                    style=FULL_SIZE_STYLE,
                    )
                ]),
            ])
        
        cout.log("Init layout...")
        
        app.layout = dmc.MantineProvider(
            theme={
                "fontFamily": "'Fira Sans', sans-serif",
                "primaryColor": "violet",
                "components": {
                    "Button": {"styles": {"root": {"fontWeight": 400, "fontSize": 22}}},
                    "Alert": {"styles": {"title": {"fontWeight": 500}}},
                    "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
                },
            },
            inherit=True,
            withGlobalStyles=True,
            withNormalizeCSS=True,
            children=[
                    dmc.Stack([
                        dmc.Header(
                            height=110,
                            style={"backgroundColor": "#82D0F4"},
                            children=[
                            dmc.Grid([
                                dmc.Center([
                                        dmc.Image(width=100, height=100, src="/assets/volt-data.svg"),
                                        dmc.Space(w=50),
                                        dmc.Title("France Political Data")
                                    ])
                            ],
                            align='left',
                            gutter='xs',
                            )
                        ]),
                        components
                    ])
                    
                ],
        )
        
        app._favicon = "volt-data.ico"
        
        cls.server = app.server
        cls.app = app
        
        cout.log("🚀 Starting app !")
        
        return app
        
# dash = Dashboard()
# dash.make()
# server = dash.app.server