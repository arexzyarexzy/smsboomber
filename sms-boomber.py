# -*- coding: utf-8 -*-
import sys
from types import ModuleType

# Zorunlu çakışma önleyici sanal katman
if 'colorama' not in sys.modules:
    colorama_mock = ModuleType('colorama')
    colorama_mock.Fore = type('Fore', (object,), {'LIGHTRED_EX': '', 'LIGHTGREEN_EX': ''})
    colorama_mock.Style = type('Style', (object,), {'RESET_ALL': ''})
    sys.modules['colorama'] = colorama_mock

import streamlit as st
import time
import re
from datetime import datetime

st.set_page_config(
    page_title="WYREX SYSTEM v9.8.5",
    page_icon="🔴",
    layout="centered",
    initial_sidebar_state="collapsed"
)

try:
    from sms import SendSms
except ImportError:
    st.error("CRITICAL FAULT: 'sms.py' dosyası yüklenemedi!")

# Görsel CSS Stilleri
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Fira+Code:wght@400;500;700&display=swap');
        * { font-family: 'Share Tech Mono', monospace !important; }
        .stApp { background: radial-gradient(circle at center, #1e0002 0%, #030001 100%) !important; }
        .ana-siber-baslik { text-align: center; color: #ffffff; font-size: 46px; font-weight: 700; letter-spacing: 4px; }
        .ana-siber-baslik span { color: #ff1a22 !important; text-shadow: 0 0 12px rgba(255, 26, 34, 0.9); }
        label { color: #d6242b !important; font-weight: bold !important; text-transform: uppercase; }
        .stTextInput > div, .stTextInput div[data-baseweb="input"] { background-color: #0c0203 !important; border: 1px solid #4a0a0d !important; }
        .stTextInput input { color: #ffffff !important; -webkit-text-fill-color: #ffffff !important; }
        div.stButton > button { background: linear-gradient(135deg, #2b0104 0%, #080000 100%) !important; color: #ffffff !important; border: 1px solid #821418 !important; width: 100%; }
        div.stButton > button:hover { background: #ff1a22 !important; }
        .terminal-log-kutusu { background-color: #020000 !important; border-left: 4px solid #ff1a22 !important; padding: 15px !important; margin-bottom: 8px; font-family: 'Fira Code', monospace !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="ana-siber-baslik"><span>wyrex</span> System</div>', unsafe_allow_html=True)

if "saldiri_aktif" not in st.session_state:
    st.session_state.saldiri_aktif = False

numara_input = st.text_input("HEDEF TELEFON NUMARASI:", placeholder="Örn: 5051234567")
mail_input = st.text_input("E-POSTA ADRESİ (OPSİYONEL):", value="arexzy_panel@gmail.com")

mod = st.selectbox("OPERASYON MODÜLÜ SEÇİNİZ:", ["Seçim Yapınız...", "1- Normal Mod", "2- Turbo Mod"])

miktar = 0
if "Normal Mod" in mod:
    miktar = st.slider("MİKTAR:", min_value=1, max_value=100, value=15)

def terminal_logu_uret(mesaj, durum_tipi="success"):
    zaman = datetime.now().strftime("%H:%M:%S")
    tag = "<span style='color: #00ff66; font-weight:bold;'>[PACKET_OK]</span>" if durum_tipi == "success" else "<span style='color: #ffea00; font-weight:bold;'>[LOOP_WARN]</span>"
    return f'<div class="terminal-log-kutusu"><span style="color: #666666;">[{zaman}]</span> {tag} <span style="color: #ffffff;">{mesaj}</span></div>'

if not st.session_state.saldiri_aktif:
    if st.button("⚡ SİSTEMİ BAŞLAT", use_container_width=True):
        if not numara_input or mod == "Seçim Yapınız...":
            st.error("Lütfen tüm alanları doldurun.")
        else:
            cleaned = re.sub(r"\D", "", numara_input)
            if cleaned.startswith("0"): cleaned = cleaned[1:]
            if len(cleaned) != 10:
                st.error("Numara 10 hane olmalıdır.")
            else:
                st.session_state.saldiri_aktif = True
                st.session_state.temiz_numara = cleaned
                st.session_state.girilen_mail = mail_input
                st.session_state.secilen_mod = mod
                st.session_state.miktar = miktar
                st.rerun()

if st.session_state.saldiri_aktif:
    if st.button("❌ OPERASYONU DURDUR", use_container_width=True):
        st.session_state.saldiri_aktif = False
        st.rerun()

    log_slot = st.empty()
    
    try:
        sms_instance = SendSms(st.session_state.temiz_numara, st.session_state.girilen_mail)
        
        if "Normal Mod" in st.session_state.secilen_mod:
            for i in range(st.session_state.miktar):
                if not st.session_state.saldiri_aktif: break
                sms_instance.KahveDunyasi()
                log_slot.markdown(terminal_logu_uret(f"Kahve Dunyasi Paketi Gönderildi [{i+1}]"), unsafe_allow_html=True)
                time.sleep(0.1)
                sms_instance.Ido()
                log_slot.markdown(terminal_logu_uret(f"Ido Paketi Gönderildi [{i+1}]"), unsafe_allow_html=True)
                time.sleep(0.1)
            st.session_state.saldiri_aktif = False
            st.success("İşlem Tamamlandı.")
            st.rerun()
            
        elif "Turbo Mod" in st.session_state.secilen_mod:
            counter = 0
            while st.session_state.saldiri_aktif:
                counter += 1
                sms_instance.KahveDunyasi()
                sms_instance.Ido()
                log_slot.markdown(terminal_logu_uret(f"Turbo Akış Döngüsü #{counter} Aktif", "warn"), unsafe_allow_html=True)
                time.sleep(0.2)
    except Exception as e:
        st.error(f"Hata oluştu: {str(e)}")
        st.session_state.saldiri_aktif = False
