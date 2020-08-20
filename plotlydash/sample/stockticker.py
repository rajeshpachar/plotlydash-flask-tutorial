# """Instantiate a Dash app."""
# import dash
# from layouts.sample.stockticker.index_html import html_layout
# from layouts.sample.stockticker.layout import create_layout


# def create_dashboard(dash_app):
#     """Create a Plotly Dash dashboard."""
#     # dash_app = dash.Dash(
#     #     server=server,
#     #     routes_pathname_prefix='/dashapp/',
#     #     external_stylesheets=[
#     #         '/static/dist/css/styles.css',
#     #         'https://fonts.googleapis.com/css?family=Lato'
#     #     ]
#     # )

#     # Custom HTML layout
#     dash_app.index_string = html_layout

#     # Create Layout
#     dash_app.layout = create_layout(df)
#     return dash_app.server


# # def create_data_table(df):
# #     """Create Dash datatable from Pandas DataFrame."""
# #     table = dash_table.DataTable(
# #         id='database-table',
# #         columns=[{"name": i, "id": i} for i in df.columns],
# #         data=df.to_dict('records'),
# #         sort_action="native",
# #         sort_mode='native',
# #         page_size=300
# #     )
# #     return table

