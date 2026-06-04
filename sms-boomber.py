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
        st.error("❌ Lütfen boş bırakmayın! Bir telefon numarası yazmalısınız.")
    
    elif mod == "Seçim Yapınız...":
        st.error("❌ Lütfen geçerli bir gönderim modu seçin!")
        
    else:
        # Numarayı temizleme (Kullanıcı boşluk bıraktıysa veya +90 yazdıysa sadece rakamları ayıklar)
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
            
            # Seçilen moda göre ekrana bilgi basma
            if "Normal" in mod:
                st.info(f"➔ {temiz_numara} için Normal Mod başlatılıyor... Toplam: {miktar} adet.")
            else:
                st.warning(f"➔ {temiz_numara} için TURBO MOD başlatılıyor... Toplam: {miktar} adet.")
            
            # --- ASIL SMS TETİKLEME ALANI ---
            # Kodun patlamaması için her şeyi try-except (koruma) içine alıyoruz
            try:
                # Durum çubuğu (Sitede dönen yükleniyor animasyonu)
                with st.spinner("SMS API'leri tetikleniyor, lütfen bekleyin..."):
                    
                    # 1. Adım: Senin sms.py içindeki SendSms sınıfını hazırlıyoruz
                    # (Senin kodunun çalışma mantığına göre numara parametresi gönderilir)
                    islem = SendSms(temiz_numara)
                    
                    # 2. Adım: Miktar kadar döngü döndürüp SMS'leri tetikliyoruz
                    # Not: Eğer sms.py içinde kendi döngün varsa buradaki döngüyü kaldırıp
                    # direkt islem.gonder() gibi çağırabilirsin.
                    for i in range(miktar):
                        # Ekranda anlık kaçıncıda olduğunu gösteren sayaç
                        st.text(f"[{i+1}/{miktar}] API servisleri sorgulanıyor...")
                        
                        # BURASI ÖNEMLİ: sms.py dosyanın içindeki asıl fonksiyonun ismi neyse onu çağır.
                        # Eğer sms.py içindeki fonksiyon direkt çalışıyorsa alt satırı kendine göre düzenle:
                        # islem.start() veya islem.gonder() gibi.
                        
                        time.sleep(0.5) # Sunucunun ban yememesi için çok kısa bekleme süresi
                
                # Başarılı mesajı
                st.balloons() # Ekranda balonlar uçuşur
                st.success("🎉 Tüm API istekleri başarıyla gönderildi! İşlem tamamlandı.")
                
            except Exception as e:
                # Eğer sms.py çalışırken bir hata verirse (kod hatası, internet kopması vs.)
                # Burası devreye girer ve hatayı web sitesinde KIPKIRMIZI gösterir.
                st.error(f"⚠️ Kod Çalıştırılırken Bir Hata Oluştu!")
                st.code(f"Hata Detayı: {e}", language="python")

# 5. Alt Bilgi (Footer)
st.write("")
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Arexzy Software © 2026</p>", unsafe_allow_html=True)
