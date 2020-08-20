from datasets.sample.data import create_dataframe

class DataManager():
    def __init__(self, auth_token:str=''):
        self.auth_token = auth_token

    def get_data(self, data_setname:str, params:dict={}):
        if data_setname == 'table_sample':
            return create_dataframe()
        print(f"{data_setname} data set not found" )
        return None
