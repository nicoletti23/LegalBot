import requests
import xmltodict

DIAN_API_URL = "https://apidepruebas.dian.gov.co"

def firmar_documento(documento_xml: str):
    headers = {"Content-Type": "application/xml"}
    response = requests.post(f"{DIAN_API_URL}/firmaElectronica", data=documento_xml, headers=headers)
    
    if response.status_code == 200:
        return xmltodict.parse(response.text)
    return {"error": "No se pudo firmar el documento"}
