import pandas as pd


class datafra:

    def __init__(self):
        ...

    def frame(self, ano, id_site, texto):
        data = {
            'ID': [id_site],
            'ANO': [ano],
            'TEXTO': [texto]
        }

        df = pd.DataFrame(data)
        print(df)


