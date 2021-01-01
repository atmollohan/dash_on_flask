from datetime import datetime as dt

import pandas_datareader as pdr
from dash.dependencies import Input
from dash.dependencies import Output

from flask_login import current_user
from app.models import Watching



def register_callbacks(dashapp):
    @dashapp.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
    def update_graph(selected_dropdown_value):
        df = pdr.get_data_yahoo(selected_dropdown_value, start=dt(2017, 1, 1), end=dt.now())
        return {
            'data': [{
                'x': df.index,
                'y': df.Close
            }],
            'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
        }

    @dashapp.callback(Output('my-dropdown', 'options'), [Input('my-dropdown', 'value')])
    def set_dropdown_options(selected_dropdown_value):
        if current_user.is_authenticated:
            my_stonks = [{'label': item.stock_name, 'value': item.stock_ticker} for item in Watching.query.filter_by(user_id=current_user.id).all()]
            # print(my_stonks)
            # selected_dropdown_value = current_user.favorite_stock
            # print(current_user.favorite_stock)
            return my_stonks

    # @dashapp.callback(Output('my-dropdown', 'value'), [Input('my-dropdown', 'options')])
    # def set_dropdown_value(available_options):
    #     if current_user.is_authenticated:
    #         return current_user.favorite_stock
