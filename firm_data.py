import requests

def get_firm_data(firm_name):
    url = f"https://api.opencorporates.com/v0.4/companies/search?q={firm_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

firm_name = "SUMA Jeoteknik"
firm_data = get_firm_data(firm_name)

if firm_data:
    print("✅ Firma bilgileri başarıyla çekildi!")
    print(firm_data)
else:
    print("❌ Firma bilgileri bulunamadı!")