import streamlit as st
import time
import re

# sms.py entegrasyonu
try:
    from sms import SendSms
except ImportError:
    st.error("HATA: sms.py dosyası bulunamadı!")

# 1. Sayfa Ayarları
st.set_page_config(page_title="WYREX SYSTEM", page_icon="🔴", layout="centered")

# 2. GÖRSELDEKİ REPLIT TEMASININ BİREBİR CSS UYARLAMASI
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
        
        /* Tüm sayfayı kapsayan font ve temel sıfırlama */
        * {
            font-family: 'Share Tech Mono', monospace !important;
        }
        
        /* Sol Üst Köşedeki Yapımcı İmzası */
        .credits {
            position: absolute;
            top: -50px;
            left: -10px;
            color: #8c1c1c;
            font-size: 13px;
            font-weight: bold;
            letter-spacing: 1px;
            text-shadow: 0 0 4px rgba(255, 0, 0, 0.4);
        }

        /* Arka Plan Derin Kırmızı Degrade (Görseldeki gibi karanlık ve kırmızı parlamalı) */
        .stApp {
            background: radial-gradient(circle at center, #290004 0%, #0d0001 100%) !important;
        }

        /* Merkez Kalkan Logosu Görünümü */
        .shield-icon {
            text-align: center;
            font-size: 40px;
            color: #ff1a22;
            margin-top: 10px;
            margin-bottom: -10px;
            filter: drop-shadow(0 0 8px #ff0000);
        }
        
        /* wyrex System Başlığı */
        .wyrex-title {
            text-align: center;
            color: #ffffff;
            font-size: 38px;
            font-weight: bold;
            margin-bottom: 0px;
        }
        .wyrex-title span {
            color: #ff1a22 !important;
            text-shadow: 0 0 10px rgba(255, 26, 34, 0.6);
        }
        
        /* Alt Açıklama Yazısı */
        .wyrex-desc {
            text-align: center;
            color: #7d7d7d;
            font-size: 13px;
            margin-bottom: 25px;
        }
        
        /* Form Alanı Başlıkları */
        label {
            color: #d6363b !important;
            font-size: 14px !important;
            letter-spacing: 1px;
        }
        
        /* İnce Kırmızı Çizgili Input ve Kutu Tasarımları (Görseldeki gibi) */
        div[data-baseweb="input"], div[data-baseweb="select"] {
            background-color: #120102 !important;
            border: 1px solid #4a0d10 !important;
            border-radius: 4px !important;
        }
        div[data-baseweb="input"]:focus-within, div[data-baseweb="select"]:focus-within {
            border: 1px solid #ff1a22 !important;
            box-shadow: 0 0 8px rgba(255, 26, 34, 0.3) !important;
        }
        input {
            color: #ffffff !important;
        }

        /* Buton Tasarımı */
        div.stButton > button {
            background-color: #1a0204 !important;
            color: #ffffff !important;
            border: 1px solid #8c1c1c !important;
            border-radius: 4px !important;
            padding: 10px 0px !important;
            font-size: 16px !important;
            transition: all 0.3s ease;
        }
        div.stButton > button:hover {
            background-color: #ff1a22 !important;
            color: #ffffff !important;
            border: 1px solid #ff1a22 !important;
            box-shadow: 0 0 15px rgba(255, 26, 34, 0.5);
        }

        /* Seçim kutusunda arama yapmayı / yazı yazmayı kapatan kilit */
        div[data-baseweb="select"] input {
            pointer-events: none !important;
            caret-color: transparent !important;
        }

        /* Slider Kırmızı Neonlaştırma */
        div[data-baseweb="slider"] {
            padding-bottom: 20px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Sol üst köşedeki yapımcı bilgisi
st.markdown('<div class="credits">by : arexzy & william</div>', unsafe_allow_html=True)

# Görseldeki kalkan ikonu ve Wyrex başlığı
st.markdown('<div class="shield-icon">🛡️</div>', unsafe_allow_html=True)
st.markdown('<div class="wyrex-title"><span>wyrex</span> System</div>', unsafe_allow_html=True)
st.markdown('<div class="wyrex-desc">Kapsamlı sorgu ve OSINT platformu — sağ menüden modül seç</div>', unsafe_allow_html=True)

# 3. Giriş Alanları
numara_input = st.text_input("TELEFON NUMARASI:", placeholder="Örn: 5051234567")
gizli_mail = "arexzy_panel@gmail.com"

mod = st.selectbox(
    "MODÜL SEÇİMİ:",
    ["Seçim Yapınız...", "1- SMS Gönder (Normal Mod - Belirli Sayıda)", "2- SMS Gönder (Turbo Mod - Sonsuz/Durdurana Kadar)"]
)

# Filtreleme: Turbo modda miktar çubuğunu gizle
miktar = 0
if mod == "1- SMS Gönder (Normal Mod - Belirli Sayıda)":
    miktar = st.slider("MİKTAR BELİRLE:", min_value=1, max_value=100, value=10)

st.write("")

# 4. Operasyon Durum Yönetimi
if "saldiri_aktif" not in st.session_state:
    st.session_state.saldiri_aktif = False

# Tetikleme Alanı
if not st.session_state.saldiri_aktif:
    if st.button("SORGULAMAYI BAŞLAT ⚡", use_container_width=True):
        if not numara_input:
            st.error("❌ Numara alanı boş bırakılamaz!")
        elif mod == "Seçim Yapınız...":
            st.error("❌ Lütfen geçerli bir modül seçin!")
        else:
            temiz_numara = re.sub(r"\D", "", numara_input)
            if temiz_numara.startswith("0"):
                temiz_numara = temiz_numara[1:]
            
            if len(temiz_numara) != 10:
                st.error("❌ Geçersiz numara formatı!")
            else:
                st.session_state.saldiri_aktif = True
                st.session_state.temiz_numara = temiz_numara
                st.session_state.secilen_mod = mod
                st.session_state.miktar = miktar
                st.rerun()

# Döngü Çalışma Ekranı
if st.session_state.saldiri_aktif:
    st.markdown("<p style='color: #ff1a22; text-align: center; font-weight: bold; font-size: 14px;'>🔴 MODÜL ÇALIŞIYOR: VERİ AKIŞI AKTİF</p>", unsafe_allow_html=True)
    
    dur_butonu = st.button("❌ İŞLEMİ DURDUR (STOP)", use_container_width=True)
    if dur_butonu:
        st.session_state.saldiri_aktif = False
        st.rerun()

    no = st.session_state.temiz_numara
    aktif_mod = st.session_state.secilen_mod
    
    with st.spinner("Sinyaller gönderiliyor..."):
        try:
            islem = SendSms(no, gizli_mail)
            
            # sms.py fonksiyonlarını çek
            servisler_sms = []
            for attribute in dir(SendSms):
                attribute_value = getattr(SendSms, attribute)
                if callable(attribute_value) and not attribute.startswith('__'):
                    servisler_sms.append(attribute)

            # 🚀 NORMAL MOD
            if "Normal Mod" in aktif_mod:
                toplam_adet = st.session_state.miktar
                sayac_alani = st.empty()
                
                for i in range(toplam_adet):
                    for metot_adi in servisler_sms:
                        metot = getattr(islem, metot_adi)
                        metot()
                    sayac_alani.markdown(f"<p style='color: #7d7d7d; text-align: center;'>İlerleme: [{i+1}/{toplam_adet}] tur tamamlandı.</p>", unsafe_allow_html=True)
                    time.sleep(0.3)
                
                st.session_state.saldiri_aktif = False
                st.success("🎯 Paket iletimi başarıyla sonlandırıldı!")
                st.rerun()

            # 🚀 TURBO MOD
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
                    turbo_sayac_alani.markdown(f"<p style='color: #ff1a22; font-size: 18px; text-align: center; font-weight: bold;'>🔥 SÜREKLİ AKIŞ: {sayac}. döngü basılıyor...</p>", unsafe_allow_html=True)
                    time.sleep(0.1)
                    
        except Exception as e:
            st.error(f"Kritik Bağlantı Hatası: {e}")
            st.session_state.saldiri_aktif = False

# Alt Bilgi
st.markdown("<p style='text-align: center; color: #3b0507; font-size: 11px; margin-top: 50px;'>WYREX SYSTEM v4.2.6</p>", unsafe_allow_html=True)
