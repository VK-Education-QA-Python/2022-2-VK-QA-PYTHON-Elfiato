from sqlalchemy import inspect


class Builder:
    def __init__(self, client):
        self.client = client

    def add_data(self, amount=None, table=None, script=None):
        if amount is None:
            res = script()
        else:
            res = script(amount)
        table_columns = [f'`{i.key}`' for i in inspect(table).attrs if i.key != 'id']
        for el in res:
            if type(el) is tuple:
                el = map(lambda x: f'"{x}"', el)
                values = f'{",".join(el)}'
            else:
                values = f'"{el}"'
            self.client.execute_query(
                f'insert into `{table.__tablename__}` ({",".join(table_columns)}) values ({values})')
