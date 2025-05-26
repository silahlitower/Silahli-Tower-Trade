import requests
import pandas as pd

# UN Comtrade API'sinden veri çekme örneği
def get_un_comtrade_data():
    url = "https://comtrade.un.org/api/get?max=100&type=C&freq=A&px=HS&cc=TOTAL&r=all&ps=latest&fmt=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data["dataset"])
    else:
        return None

# Veri çekme işlemi
un_data = get_un_comtrade_data()
if un_data is not None:
    print("✅ UN Comtrade verileri başarıyla çekildi!")
    un_data.to_csv("un_comtrade_data.csv", index=False)
else:
    print("❌ Veri çekme hatası!")