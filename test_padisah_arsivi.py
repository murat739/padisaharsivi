# padisah-arsivi Proje Test ve Doğrulama Aracı
import os
import streamlit as st

st.title("🏛️ Padişah Arşivi - Proje Test ve Yayın Kontrol Paneli")
st.markdown("""
Bu araç, **`padisah-arsivi`** projenizin Streamlit Cloud ortamına hatasız bir şekilde 
dağıtılabilmesi (deploy) için dosya yapısını, bağımlılıkları ve temel modülleri yerel RAM üzerinde test eder.
""")

# Proje yolu doğrulama
project_path = r"C:\Users\omerg\Desktop\padisah-arsivi"

st.subheader("📁 Dizin ve Dosya Kontrolü")
if os.path.exists(project_path):
    st.success(f"✅ Hedef dizin doğrulandı: `{project_path}`")
    
    # Kritik dosyaları listele
    files = os.listdir(project_path)
    st.write("**Dizindeki Mevcut Dosya ve Klasörler:**")
    st.code("\n".join(files))
    
    # requirements.txt kontrolü
    if "requirements.txt" in files:
        st.success("✅ `requirements.txt` dosyası mevcut.")
        with open(os.path.join(project_path, "requirements.txt"), "r", encoding="utf-8") as f:
            req_content = f.read()
        st.text_area("Gerekli Kütüphaneler (requirements.txt):", req_content, height=100)
    else:
        st.warning("⚠️ `requirements.txt` dosyası bulunamadı! Streamlit Cloud dağıtımı için eklemeniz önerilir.")
        
    # main.py veya ana dosya kontrolü
    main_candidates = ["main.py", "app.py", "Anasayfa.py"]
    found_main = [m for m in main_candidates if m in files]
    if found_main:
        st.success(f"✅ Ana giriş dosyası tespit edildi: `{found_main[0]}`")
    else:
        st.error("❌ Ana uygulama dosyası (`main.py` veya `app.py`) kök dizinde bulunamadı!")
        
else:
    st.error(f"❌ Belirtilen dizin bulunamadı: `{project_path}`. Lütfen klasör yolunu kontrol edin.")

st.markdown("---")
st.subheader("🚀 Streamlit Cloud Yayın Öncesi Kontrol Listesi")
st.markdown("""
1. **GitHub Deposu:** Projeyi bir GitHub repository'sine (örneğin `padisah-arsivi`) `git push` komutuyla yükleyin.
2. **Bağımlılıklar:** `requirements.txt` dosyanızda `streamlit`, `pandas`, `numpy`, `reportlab` gibi kullanılan tüm kütüphanelerin ekli olduğundan emin olun.
3. **Streamlit Cloud Paneli:** [share.streamlit.io](https://share.streamlit.io) adresine giderek `New app` butonuna tıklayın, ilgili GitHub deposunu ve ana dosyanızı (`main.py`) seçerek deploy işlemini başlatın.
""")

st.info("💡 Tüm yerel testler tamamlandığında projenizi sorunsuz bir şekilde buluta aktarabilirsiniz.")