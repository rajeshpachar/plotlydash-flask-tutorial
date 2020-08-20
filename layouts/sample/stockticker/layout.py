"""Instantiate a Dash app."""
import dash_table
import dash_html_components as html
import dash_core_components as dcc
from datasets.datamanager import DataManager

def get_layout():
    # Load DataFrame
    dataManager = DataManager()
    df = dataManager.get_data('table_sample')

    # Create Layout
    layout = html.Div(
        children=[dcc.Graph(
            id='histogram-graph',
            figure={
                'data': [{
                    'x': df['complaint_type'],
                    'text': df['complaint_type'],
                    'customdata': df['key'],
                    'name': '311 Calls by region.',
                    'type': 'histogram'
                }],
                'layout': {
                    'title': 'NYC 311 Calls category.',
                    'height': 500,
                    'padding': 150
                }
            }),
            create_data_table(df)
        ],
        id='dash-container'
    )
    return layout

def create_data_table(df):
    """Create Dash datatable from Pandas DataFrame."""
    table = dash_table.DataTable(
        id='database-table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        sort_action="native",
        sort_mode='native',
        page_size=300
    )
    return table

