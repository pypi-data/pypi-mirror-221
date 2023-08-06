import pandas as pd
import pickle
import base64
import requests

def generate(inputTable):

    inputTable_df = pd.read_csv(inputTable)
    pickled = pickle.dumps(inputTable_df)
    pickled_base64 = base64.b64encode(pickled)

    data = {
        "df_b64": pickled_base64.decode("utf-8")
    }

    a = requests.post("https://adityarai10101--privtab-main.modal.run", json=data)

    new_df = pickle.loads(base64.b64decode(a.text.encode()))
    return new_df

