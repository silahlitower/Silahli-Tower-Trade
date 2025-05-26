import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasını oku
data = pd.read_csv("un_comtrade_data.csv")

# En çok ithalat yapan ülkeleri göster
top_importers = data.groupby("rtTitle")["TradeValue"].sum().nlargest(10)

plt.figure(figsize=(10, 5))
top_importers.plot(kind="bar", color="purple")
plt.title("En Çok İthalat Yapan Ülkeler")
plt.ylabel("İthalat Değeri")
plt.show()