import requests
from bs4 import BeautifulSoup

DIAN_URL = "https://www.dian.gov.co/normatividad/Paginas/Normatividad.aspx"

def obtener_cambios_legales():
    response = requests.get(DIAN_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    cambios = []
    for link in soup.find_all("a"):
        if "pdf" in link.get("href", ""):
            cambios.append({"titulo": link.text, "url": link["href"]})

    return cambios
