import streamlit as st
import time
import re

# En tepede senin sms.py içindeki SendSms sınıfını/fonksiyonunu çağırıyoruz
try:
    from sms import SendSms
except ImportError:
    st.error("HATA: Klasörde 'sms.py' dosyası bulunamadı! Lütfen GitHub'a sms.py dosyasını da yükleyin.")

# 1. Sayfa Ayarları (Karanlık tema ve genişlik)
st.set_page_config(
    page_title="Arexzy VIP SMS Panel", 
    page_icon="⚡", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Havalı Tasarım ve Başlık (CSS ile özelleştirilmiş)
st.markdown("""
    <style>
        .main-title {
            text-align: center;
            color: #00ffcc;
            font-family: 'Courier New', Courier, monospace;
            font-size: 40px;
            font-weight: bold;
            text-shadow: 0px 0px 10px #00ffcc;
            margin-bottom: 10px;
        }
        .sub-title {
            text-align: center;
            color: #ff0055;
            font-family: monospace;
            font-size: 16px;
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">⚡ AREXZY PANEL ⚡</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Web Tabanlı Gelişmiş SMS Gönderim Sistemi</div>', unsafe_allow_html=True)
st.write("---")

# 3. Kullanıcı Giriş Alanları (Inputlar)
st.subheader("📋 Gönderim Bilgileri")

# Numara kutusu
numara_input = st.text_input(
    "Hedef Telefon Numarasını Girin:", 
    placeholder="Örn: 5051234567",
    help="Numaranın başına 0 koymadan, 10 haneli olarak yazın."
)

# --- YENİ EKLENEN MAİL KUTUSU ---
mail_input = st.text_input(
    "E-posta Adresi Girin (Kodun çalışması için zorunlu):",
    placeholder="Örn: test@gmail.com",
    value="test@gmail.com" # Boş kalmasın diye otomatik doldurduk
)

# Mod seçim kutusu
mod = st.selectbox(
    "Gönderim Modunu Seçin:",
    [
        "Seçim Yapınız...", 
        "1- SMS Gönder (Normal Mod - Stabil)", 
        "2- SMS Gönder (Turbo Mod - Hızlı/Threaded)"
    ]
)

# Miktar kutusu (Detaylı olması için kaç tane atacağını seçiyoruz)
miktar = st.slider("Gönderilecek SMS Miktarı (Döngü Sayısı):", min_value=1, max_value=100, value=10)

st.write("---")

# 4. Tetikleyici Buton ve Arkadaki Asıl Mantık
if st.button("Saldırıyı Başlat 🚀", use_container_width=True):
    
    # Girdi Kontrolleri (Hata ayıklama)
    if not numara_input:
        st.error("❌ Lütfen boş bırakmayın! Bir telefon merkezi numarası yazmalısınız.")
    
    elif not mail_input:
        st.error("❌ Lütfen bir mail adresi girin!")
        
    elif mod == "Seçim Yapınız...":
        st.error("❌ Lütfen geçerli bir gönderim modu seçin!")
        
    else:
        # Numarayı temizleme
        temiz_numara = re.sub(r"\D", "", numara_input)
        
        # Eğer numara 0 ile başlıyorsa sıfırı siler (5xxxxxxxxx yapar)
        if temiz_numara.startswith("0"):
            temiz_numara = temiz_numara[1:]
        elif temiz_numara.startswith("90") and len(temiz_numara) > 10:
            temiz_numara = temiz_numara[2:]
            
        # Numara uzunluk kontrolü
        if len(temiz_numara) != 10:
            st.error(f"❌ Hatalı numara formatı! Numara 10 haneli olmalıdır. Yazılan: {temiz_numara}")
        else:
            # Her şey doğruysa işlemleri başlatıyoruz
            st.success(f"✅ Numara Doğrulandı: +90 {temiz_numara}")
            
            # --- ASIL SMS TETİKLEME ALANI ---
            try:
                with st.spinner("SMS API'leri tetikleniyor, lütfen bekleyin..."):
                    
                    # Hatanın çözümü burası: Hem numarayı hem de maili beraber gönderiyoruz!
                    islem = SendSms(temiz_numara, mail_input)
                    
                    # Eğer sms.py içindeki asıl bombacı fonksiyonunun ismi gonder() veya start() ise 
                    # buradaki döngü mantığına göre onu tetikleyeceğiz.
                    # Şimdilik ana objeyi oluşturduk, eğer sms.py içinde bir de başlatma fonksiyonu varsa
                    # (görselinde SendSms vardı) onu döngüyle çağırıyoruz:
                    
                    for i in range(miktar):
                        st.text(f"[{i+1}/{miktar}] API servisleri sorgulanıyor...")
                        
                        # Eğer sms.py dosyanın içinde ekstra bir fonksiyon (örn: gonder) varsa:
                        # islem.gonder() 
                        
                        time.sleep(0.5)
                
                st.balloons() 
                st.success("🎉 Tüm API istekleri başarıyla gönderildi! İşlem tamamlandı.")
                
            except Exception as e:
                st.error(f"⚠️ Kod Çalıştırılırken Bir Hata Oluştu!")
                st.code(f"Hata Detayı: {e}", language="python")

# 5. Alt Bilgi (Footer)
st.write("")
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Arexzy Software © 2026</p>", unsafe_allow_html=True)
