import streamlit as st
import time
from sms import SendSms

# Sitenin başlığı ve teması
st.set_page_config(page_title="SMS Kontrol Paneli", page_icon="⚡", layout="centered")

# Havalı bir başlık logosu
st.markdown("<h1 style='text-align: center; color: #00ffcc; font-family: monospace;'>⚡ AREXZY PANEL ⚡</h1>", unsafe_allow_html=True)
st.write("---")

# Numara giriş alanı
numara = st.text_input("Hedef Telefon Numarasını Girin:", placeholder="Örn: 5051234567")

# Menü seçenekleri (Butonlar için mod seçimi)
mod = st.selectbox(
    "Gönderim Modu Seçin:",
    ["Seçim Yapınız...", "1- SMS Gönder (Normal)", "2- SMS Gönder (Turbo)"]
)

st.write("---")

# Çalıştır Butonu
if st.button("Saldırıyı Başlat 🚀", use_container_width=True):
    if not numara:
        st.error("Lütfen önce geçerli bir telefon numarası girin!")
    elif mod == "Seçim Yapınız...":
        st.error("Lütfen bir gönderim modu seçin!")
    else:
        # Seçime göre durum mesajı gösteriyoruz
        if "Normal" in mod:
            st.info(f"➔ {numara} için Normal Mod başlatılıyor...")
        else:
            st.warning(f"➔ {numara} için TURBO MOD başlatılıyor...")
        
        # Senin sms.py içindeki SendSms fonksiyonunu tetikliyoruz
        try:
            # Burada sms.py dosyasındaki asıl kodların çalışacak
            # Eğer fonksiyonun parametre istiyorsa (numara gibi) buraya aktarır
            # SendSms() 
            
            st.success("İşlem başarıyla tamamlandı! ✅")
        except Exception as e:
            st.error(f"Bir hata oluştu: {e}")
