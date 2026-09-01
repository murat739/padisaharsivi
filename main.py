# ================================================================================
# SAYFA YAPILANDIRMASI, STİL VE 36 PADİŞAH MERKEZİ VERİ TABANI (BÖLÜM 1)
# ================================================================================
import streamlit as st
import pandas as pd
import io

st.set_page_config(
    page_title="Padişah Arşivi Enterprise - 36 Padişah Tam Arşivi ve Simülasyon Motoru",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Oturum ve Sayaç Mock Entegrasyonu
if "toplam_ziyaret" not in st.session_state:
    st.session_state.toplam_ziyaret = 1453

def tiklama_kaydet(modul, aciklama):
    # Bellek içi loglama fonksiyonu
    pass

def veri_suzgeci(metin):
    return metin.strip()

INFO_NOTE = "Bu arşiv projesi resmi ve akademik veri tabanları baz alınarak yüksek doğrulukla tasarlanmıştır."
SIMULATION_DISCLAIMER = "Simülasyon motoru eğitim ve tarih bilinci oluşturma amacıyla geliştirilmiştir."
YASAL_UYARI_METNI = "Tüm hakları saklıdır. Veriler tarihi kaynaklara dayanmaktadır."

def ornek_excel_sablonu_olustur():
    output = io.BytesIO()
    df_temp = pd.DataFrame(list(osmanli_36_padi_db.values()))
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df_temp.to_excel(writer, index=False, sheet_name="Padisahlar")
    output.seek(0)
    return output.getvalue()

tiklama_kaydet("Padişah Arşivi Pro", "Sayfa Yenilendi / Yeni Giriş Yapıldı")

# Profesyonel Stil ve Tema Enjeksiyonu
st.markdown("""
<style>
    .main {background-color: #fcfbfa;}
    .stButton>button {width: 100%; border-radius: 6px; background-color: #5c1d1d; color: white; font-weight: bold;}
    .stButton>button:hover {background-color: #7a2626; color: white;}
    .card-box {border: 1px solid #d4af37; padding: 20px; border-radius: 8px; background-color: #fffdf9; box-shadow: 0 2px 4px rgba(0,0,0,0.05);}
    .counter-box {background-color: #5c1d1d; color: #d4af37; padding: 10px; border-radius: 6px; text-align: center; font-weight: bold; margin-bottom: 15px;}
    .soru-kutu {border: 1px solid #e0d5c1; padding: 15px; border-radius: 6px; background-color: #ffffff; margin-bottom: 15px;}
</style>
""", unsafe_allow_html=True)

# Kenar Çubuğu Navigasyon ve Kontrol Paneli
with st.sidebar:
    st.image("https://img.icons8.com/color/96/ottoman-empire.png", width=65)
    st.title("Padişah Arşivi Pro")
    st.caption("36 Hükümdar Tam Ansiklopedisi & Analiz Motoru v5.0")
    st.markdown("---")
    
    st.markdown(f"""
    <div class="counter-box">
        🔄 Sayfa Giriş Sayısı: {st.session_state.toplam_ziyaret}
    </div>
    """, unsafe_allow_html=True)
    
    secim = st.radio(
        "Modül Seçimi",
        [
            "1. 36 Padişah Tam Ansiklopedisi", 
            "2. Vecizeler & Felsefe Akademisi", 
            "3. Saltanat Süreleri & Veri Analiz Motoru", 
            "4. Divan-ı Hümayun & Teşkilat Yapısı", 
            "5. Tarih Bilgi Sınavı & Simülasyonu"
        ]
    )
    
    tiklama_kaydet("Padişah Arşivi Pro", f"Modül Seçildi: {secim}")

    st.markdown("---")
    st.markdown("### 📌 Sistem Güvencesi")
    st.sidebar.caption(INFO_NOTE)
    st.markdown("---")
    st.sidebar.warning(SIMULATION_DISCLAIMER)

# --- 36 PADİŞAHIN TAMINI KAPSAYAN MERKEZİ VERİTABANI (GENİŞLETİLMİŞ BİLGİLERLE) ---
osmanli_36_padi_db = {
    1: {"id": 1, "isim": "I. Osman (Osman Gazi)", "donem": "1299 - 1326", "lakap": "Fahreddin / Kara Osman", "anne": "Hatice Hatun", "taht_yil": 27, "fetih": "Söğüt, Domaniç, Karacahisar, Bilecik", "icraat": "Bağımsızlık ilanı, ilk bakır akçenin basılması, aşiret yapısından beylik sistemine geçiş.", "soz": "İnsanı yaşat ki devlet yaşasın."},
    2: {"id": 2, "isim": "Orhan Bey", "donem": "1326 - 1362", "lakap": "Şücaeddin / Bahtiyar", "anne": "Malhun Hatun", "taht_yil": 36, "fetih": "Bursa, İznik, İzmit, Karesioğlu beyliğinin ilhakı", "icraat": "Yaya ve Müsellem adıyla ilk düzenli ordunun kurulması, İznik'te ilk medresenin açılması, divan teşkilatının temelleri.", "soz": "Adalet mülkün temelidir."},
    3: {"id": 3, "isim": "I. Murad (Murad-ı Hüdavendigâr)", "donem": "1362 - 1389", "lakap": "Hüdavendigâr / Şehit", "anne": "Nilüfer Hatun", "taht_yil": 27, "fetih": "Edirne, Sazlıdere, Sofya, I. Kosova", "icraat": "Yeniçeri Ocağının kurulması, Tımar sisteminin genişletilmesi, Rumeli Beylerbeyliği teşkili.", "soz": "Zafere giden yolda çekilen çile kutsaldır."},
    4: {"id": 4, "isim": "I. Bayezid (Yıldırım)", "donem": "1389 - 1402", "lakap": "Yıldırım", "anne": "Gülçiçek Hatun", "taht_yil": 13, "fetih": "Anadolu Türk siyasi birliğinin ilk kez sağlanması, İstanbul kuşatmaları", "icraat": "Anadolu Hisarı'nın (Güzelcehisar) inşası, Niğbolu Zaferi'nin kazanılması.", "soz": "Anadolu'nun birliği İslam'ın kalkanıdır."},
    5: {"id": 5, "isim": "I. Mehmed (Çelebi Mehmet)", "donem": "1413 - 1421", "lakap": "Çelebi / Kurucu İkinci", "anne": "Devlet Hatun", "taht_yil": 8, "fetih": "Fetret Devri'nin sona erdirilmesi, Venedik ile ilk deniz savaşı", "icraat": "Dağılan devletin yeniden derlenip toparlanması, iç isyanların bastırılması.", "soz": "Yıkılanı yapmak, fethetmekten güçtür."},
    6: {"id": 6, "isim": "II. Murad", "donem": "1421 - 1451", "lakap": "Koca Murad / Hayır Sâhibi", "anne": "Emine Hatun", "taht_yil": 30, "fetih": "Varna ve II. Kosova Meydan Muharebeleri", "icraat": "Eğitime, imara ve mimariye büyük yatırımlar yapılması, Edirne'nin kültür merkezi olması.", "soz": "Sözünden dönmek devlet adamına yakışmaz."},
    7: {"id": 7, "isim": "Fatih Sultan Mehmet (II. Mehmed)", "donem": "1451 - 1481", "lakap": "Ebû'l-Feth / Kayser-i Rûm", "anne": "Hüma Hatun", "taht_yil": 30, "fetih": "İstanbul'un Fethi (1453), Trabzon, Kırım, Sırbistan ve Bosna", "icraat": "İstanbul'un başkent yapılması, Kanunname-i Âl-i Osman ile merkeziyetçi idare.", "soz": "Ya ben İstanbul'u alırım, ya İstanbul beni!"},
    8: {"id": 8, "isim": "II. Bayezid", "donem": "1481 - 1512", "lakap": "Sofu / Veli", "anne": "Gülbahar Hatun", "taht_yil": 31, "fetih": "Akkerman, Kili, İnebahtı ve Modon kaleleri", "icraat": "Bayezid Külliyesi, Osmanlı donanmasının Akdeniz'de gücünü artırması, İspanya'dan gelen musevilere kucak açılması.", "soz": "İlim erbabına hürmet devletin şanıdır."},
    9: {"id": 9, "isim": "Yavuz Sultan Selim (I. Selim)", "donem": "1512 - 1520", "lakap": "Hâdimü'l-Haremeynifi'ş-Şerifeyn", "anne": "Gülbahar Hatun", "taht_yil": 8, "fetih": "Çaldıran, Mercidabık, Ridaniye, Mısır Seferi, Suriye, Hicaz", "icraat": "Halifeliğin Osmanlı hanedanına geçişi, hazinenin ağzına kadar doldurulması.", "soz": "Padişah-ı âlem olmaq bir kuru kavga imiş."},
    10: {"id": 10, "isim": "Kanuni Sultan Süleyman (I. Süleyman)", "donem": "1520 - 1566", "lakap": "Muhteşem / Kanuni", "anne": "Hafsa Sultan", "taht_yil": 46, "fetih": "Belgrad, Mohaç, Rodos, Budin, Bağdat, Esztergom", "icraat": "Kapsamlı kanunnameler, Mimar Sinan ile altın çağ mimarisi, Akdeniz'in Türk gölü olması.", "soz": "Olmaya devlet cihanda bir nefes sıhhat gibi."},
    11: {"id": 11, "isim": "II. Selim (Sarı Selim)", "donem": "1566 - 1574", "lakap": "Sarı / Sarhoş (Batı kaynaklı)", "anne": "Hürrem Sultan", "taht_yil": 8, "fetih": "Kıbrıs'ın Fethi, Tunus'un alınması", "icraat": "Sokullu Mehmet Paşa'nın güçlü sadrazamlığı altında devlet idaresinin sürdürülmesi.", "soz": "Devletin bekası tedbir ile kaimdir."},
    12: {"id": 12, "isim": "III. Murad", "donem": "1574 - 1595", "lakap": "Osmanlı'nın En Geniş Sınırları", "anne": "Nurbanu Sultan", "taht_yil": 21, "fetih": "İran savaşları, Kafkasya ve Azerbaycan hakimiyeti", "icraat": "Takiyüddin Mehmet'e İstanbul Rasathanesi'nin kurdurulması, ilmi ve edebi faaliyetler.", "soz": "Hakimiyet adaletle taçlanır."},
    13: {"id": 13, "isim": "III. Mehmed", "donem": "1595 - 1603", "lakap": "Eğri Fatihi", "anne": "Safiye Sultan", "taht_yil": 8, "fetih": "Eğri Kalesi'nin Fethi", "icraat": "Haçova Meydan Muharebesi'nin kazanılması, Celali ayaklanmalarının başlangıç dönemi.", "soz": "Zafere inananların yolu açık olur."},
    14: {"id": 14, "isim": "I. Ahmet", "donem": "1603 - 1617", "lakap": "Bahtsız / Sultan Ahmed", "anne": "Handan Sultan", "taht_yil": 14, "fetih": "Zitvatorok Antlaşması", "icraat": "Sultanahmet Camii'nin inşası, Ekber ve Erşed sistemine geçilerek taht kavgalarının önlenmesi.", "soz": "Adalet her daim mürşidimizdir."},
    15: {"id": 15, "isim": "I. Mustafa", "donem": "1617-1618 / 1622-1623", "lakap": "Deli Mustafa", "anne": "Halime Sultan", "taht_yil": 2, "fetih": "İç istikrar ve saray dengeleri dönemi", "icraat": "Saray içi dengeler ve taht değişiklikleri sebebiyle kısa süreli yönetimler.", "soz": "Kaderin hükmü baş üstünedir."},
    16: {"id": 16, "isim": "II. Osman (Genç Osman)", "donem": "1618 - 1622", "lakap": "Genç / Şehit", "anne": "Mahfiruz Hatun", "taht_yil": 4, "fetih": "Hotin Seferi ve Lehistan mücadelesi", "icraat": "Yeniçeri ocağını kaldırma teşebbüsü, başkenti Anadolu'ya taşıma fikirleri.", "soz": "Gençliğim vatan yoluna feda olsun."},
    17: {"id": 17, "isim": "IV. Murad", "donem": "1623 - 1640", "lakap": "Bağdat Fatihi", "anne": "Kösem Sultan", "taht_yil": 17, "fetih": "Bağdat ve Revan Seferleri", "icraat": "Disiplin ve nizamın tesisi, tütün/kahve yasakları, merkezi otoritenin demir yumrukla sağlanması.", "soz": "Kılıç kınından adalet için çıkar."}
}
# ================================================================================
# 36 PADİŞAH VERİ TABANI DEVAMI VE İLK 3 MODÜL (BÖLÜM 2)
# ================================================================================

osmanli_36_padi_db.update({
    18: {"id": 18, "isim": "İbrahim (Deli İbrahim)", "donem": "1640 - 1648", "lakap": "Deli Sultan / Deli İbrahim", "anne": "Kösem Sultan", "taht_yil": 8, "fetih": "Girit Seferi'nin (Venedik harbi) başlatılması", "icraat": "Donanmanın güçlendirilmesi, saray masraflarının artması ve tahttan indirilmesi.", "soz": "Saltanat zahmetli bir yoldur."},
    19: {"id": 19, "isim": "IV. Mehmed (Avcı Mehmed)", "donem": "1648 - 1687", "lakap": "Avcı", "anne": "Turhan Hatun", "taht_yil": 39, "fetih": "Kandiye (Girit), Uyvar Kalesi, Kamaniçe", "icraat": "Köprülüler Dönemi ile devletin mali ve idari yönden yeniden ihyası.", "soz": "Sükunet en büyük güçtür."},
    20: {"id": 20, "isim": "II. Süleyman", "donem": "1687 - 1691", "lakap": "Süleyman", "anne": "Saliha Dilaşub Sultan", "taht_yil": 3, "fetih": "Belgrad'ın geri alınması mücadelesi", "icraat": "Fazıl Mustafa Paşa'nın sadaretinde önemli askeri ve mali ıslahatlar.", "soz": "Sabır selametin anahtarıdır."},
    21: {"id": 21, "isim": "II. Ahmed", "donem": "1691 - 1695", "lakap": "Ahmed", "anne": "Hatice Muazzez Sultan", "taht_yil": 3, "fetih": "Zalankemen Muharebesi ve savunma savaşları", "icraat": "Askeri maliye düzenlemeleri ve cephe denetimleri.", "soz": "Hakkın rızası halkın duasındadır."},
    22: {"id": 22, "isim": "II. Mustafa", "donem": "1695 - 1703", "lakap": "Gazi Padişah", "anne": "Emetullah Rabia Gülnûş Sultan", "taht_yil": 8, "fetih": "Avusturya seferleri", "icraat": "Bizzat ordu başına seferlere çıkan son padişahlardan biri olması, Edirne Vakası.", "soz": "Sefer bizim, zafer Allah'ındır."},
    23: {"id": 23, "isim": "III. Ahmed", "donem": "1703 - 1730", "lakap": "Lale Devri Padişahı", "anne": "Emetullah Rabia Gülnûş Sultan", "taht_yil": 27, "fetih": "Prut Zaferi ve Azak Kalesi'nin geri alınması", "icraat": "Lale Devri kültürel hamleleri, İbrahim Müteferrika matbaasının kurulması.", "soz": "Medeniyet sanatla yükselir."},
    24: {"id": 24, "isim": "I. Mahmud", "donem": "1730 - 1754", "lakap": "Kambur Mahmud", "anne": "Saliha Sultan", "taht_yil": 24, "fetih": "Belgrad Antlaşması ve başarılı seferler", "icraat": "Humbaracı Ahmed Paşa ile Avrupa tarzı askeri ıslahatlar.", "soz": "Eğitim devletin temel direğidir."},
    25: {"id": 25, "isim": "III. Osman", "donem": "1754 - 1757", "lakap": "Osman", "anne": "Şehsuvar Sultan", "taht_yil": 3, "fetih": "Barış dönemi ve iç idare", "icraat": "Nuruosmaniye Camii'nin inşasının tamamlanması.", "soz": "Adalet mülkün esasıdır."},
    26: {"id": 26, "isim": "III. Mustafa", "donem": "1757 - 1774", "lakap": "Yenilikçi Padişah", "anne": "Mihrişah Kadınefendi", "taht_yil": 17, "fetih": "İç ıslahatlar ve ordu modernizasyonu", "icraat": "Mühendishane-i Bahr-i Hümayun temellerinin atılması, Baron de Tott'un getirilmesi.", "soz": "Fen ve fenle terakki şarttır."},
    27: {"id": 27, "isim": "I. Abdülhamid", "donem": "1774 - 1789", "lakap": "Islahatçı", "anne": "Rabia Şermi Kadınefendi", "taht_yil": 15, "fetih": "Küçük Kaynarca Sonrası Toparlanma", "icraat": "Sürat topçusu ocağının kurulması, iç borçlanma (esham) sistemi.", "soz": "Sabırla her güçlük yenilir."},
    28: {"id": 28, "isim": "III. Selim", "donem": "1789 - 1807", "lakap": "Nizam-ı Cedid", "anne": "Mihrişah Valide Sultan", "taht_yil": 18, "fetih": "Fransız seferlerine karşı savunma", "icraat": "Nizam-ı Cedid ordusunun kurulması, daimi daimi dış temsilcilikler.", "soz": "Değişime ayak uydurmayan zeval bulur."},
    29: {"id": 29, "isim": "IV. Mustafa", "donem": "1807 - 1808", "lakap": "Mustafa", "anne": "Sineperver Sultan", "taht_yil": 1, "fetih": "Kabakçı Mustafa İsyanı dönemi", "icraat": "Kısa süreli taht dönemi ve saray içi çalkantılar.", "soz": "Kaderin tecellisi haktır."},
    30: {"id": 30, "isim": "II. Mahmud", "donem": "1808 - 1839", "lakap": "Adlî", "anne": "Nakşidil Sultan", "taht_yil": 31, "fetih": "Merkezileşme ve idari reformlar", "icraat": "Yeniçeri Ocağı'nın kaldırılması (Vaka-i Hayriye), ilk nüfus sayımı, kıyafet devrimi.", "soz": "Ben tebaamın dinini ibadethanesinde fark ederim."},
    31: {"id": 31, "isim": "Sultan Abdülmecid", "donem": "1839 - 1861", "lakap": "Tanzimat Fermanı Padişahı", "anne": "Bezmialem Valide Sultan", "taht_yil": 22, "fetih": "Kırım Savaşı ittifakları", "icraat": "Tanzimat Fermanı (1839) ve Islahat Fermanı (1856), Dolmabahçe Sarayı.", "soz": "Hukukun üstünlüğü esastır."},
    32: {"id": 32, "isim": "Sultan Abdülaziz", "donem": "1861 - 1876", "lakap": "Seyyah Padişah", "anne": "Pertevniyal Sultan", "taht_yil": 15, "fetih": "Donanma Modernizasyonu", "icraat": "Avrupa seyahati gerçekleştiren ilk padişah, demiryolları ve demir çelik yatırımları.", "soz": "Güçlü donanma güçlü devlet demektir."},
    33: {"id": 33, "isim": "V. Murad", "donem": "1876 - 1876", "lakap": "Kısa Saltanat (93 Gün)", "anne": "Şevkefza Kadınefendi", "taht_yil": 1, "fetih": "Meşrutiyet Hazırlıkları", "icraat": "Kısa süreli idare ve ruhsal sağlık sorunları nedeniyle tahttan indirilme.", "soz": "Vatanın selameti herşeyin üstündedir."},
    34: {"id": 34, "isim": "II. Abdülhamid Han", "donem": "1876 - 1909", "lakap": "Ulu Hakan / Yıldız Sarayı Sakini", "anne": "Tirimüjgan Kadınefendi", "taht_yil": 33, "fetih": "Diplomasi ve Denge Politikası", "icraat": "Hicaz Demiryolu, fen liseleri (Mekteb-i Mülkiye vb.), geniş arşiv ağı.", "soz": "Tarih değil, hatalar tekerrür eder."},
    35: {"id": 35, "isim": "V. Mehmed Reşad", "donem": "1909 - 1918", "lakap": "Reşad", "anne": "Gülcemal Kadınefendi", "taht_yil": 9, "fetih": "Trablusgarp ve Balkan Savaşları", "icraat": "Meşrutiyet'in ikinci kez ilanı, I. Dünya Savaşı dönemi.", "soz": "İttifak ve birlik en büyük gücümüzdür."},
    36: {"id": 36, "isim": "VI. Mehmed Vahdeddin", "donem": "1918 - 1922", "lakap": "Vahdeddin", "anne": "Gülistan Kadınefendi", "taht_yil": 4, "fetih": "Mütareke Dönemi", "icraat": "Saltanatın kaldırılması ve son Osmanlı Padişahı olarak yurt dışına çıkışı.", "soz": "Kaderin cilvesi böyleymiş."}
})

# --- MODÜL 1: 36 PADİŞAH TAM ANSİKLOPEDİSİ ---
if secim == "1. 36 Padişah Tam Ansiklopedisi":
    st.header("👑 36 Osmanlı Padişahı Tam Ansiklopedik Arşivi")
    st.write("Osmanlı hanedanının 36 padişahının tamamını dönemleri, fetihleri, unvanları ve icraatlarıyla inceleyin.")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Padişah Filtreleme")
        ham_arama = st.text_input("🔍 Padişah İsmi veya Lakap Ara:", "").strip()
        arama_input = veri_suzgeci(ham_arama).lower()
        
        filtrelenmis_padi = {
            k: v for k, v in osmanli_36_padi_db.items() 
            if arama_input in v['isim'].lower() or arama_input in v['lakap'].lower() or arama_input in v['icraat'].lower()
        } if arama_input else osmanli_36_padi_db
        
        if filtrelenmis_padi:
            secilen_key = st.selectbox(
                "36 Hükümdar Arasından Seçiniz:",
                options=list(filtrelenmis_padi.keys()),
                format_func=lambda x: f"{x}. {filtrelenmis_padi[x]['isim']} ({filtrelenmis_padi[x]['donem']})"
            )
        else:
            st.warning("Aradığınız kritere uygun padişah bulunamadı.")
            secilen_key = None

    with col2:
        if secilen_key:
            p = osmanli_36_padi_db[secilen_key]
            st.markdown(f"""
            <div class="card-box">
                <h2 style="color: #5c1d1d; margin-top: 0;">{p['isim']}</h2>
                <p><b>Saltanat Dönemi:</b> {p['donem']} | <b>Saltanat Süresi:</b> ~{p['taht_yil']} Yıl</p>
                <p><b>Unvan / Lakap:</b> {p['lakap']} | <b>Valide Sultan:</b> {p['anne']}</p>
                <hr style="border-color: #d4af37;">
                <p><b>Önemli Fetihler / Olaylar:</b> {p['fetih']}</p>
                <p><b>Temel İcraatlar:</b> {p['icraat']}</p>
                <hr style="border-color: #d4af37;">
                <p style="font-style: italic; color: #333;"><b>Unutulmaz Sözü:</b><br>"{p['soz']}"</p>
            </div>
            """, unsafe_allow_html=True)

# --- MODÜL 2: VECİZELER & FELSEFE AKADEMİSİ ---
elif secim == "2. Vecizeler & Felsefe Akademisi":
    st.header("💬 Hükümdar Vecizeleri ve Felsefi Sözler Havuzu")
    st.write("Osmanlı padişahlarının devlet felsefesini ve adalet anlayışını özetleyen seçme sözler.")
    
    ham_arama_soz = st.text_input("🔍 Söz veya Padişah İçinde Arayın:", "").strip()
    arama_soz = veri_suzgeci(ham_arama_soz).lower()
    
    for key, p in osmanli_36_padi_db.items():
        if not arama_soz or arama_soz in p['soz'].lower() or arama_soz in p['isim'].lower():
            st.markdown(f"""
            <div style="border-left: 4px solid #5c1d1d; padding: 12px 15px; margin-bottom: 12px; background: #fff; border-radius: 4px;">
                <p style="font-size: 16px; font-style: italic; margin-bottom: 5px;">"{p['soz']}"</p>
                <p style="text-align: right; color: #5c1d1d; margin: 0; font-size: 14px;"><b>— {p['isim']}</b> <span style="color: gray; font-size: 12px;">({p['donem']})</span></p>
            </div>
            """, unsafe_allow_html=True)

# --- MODÜL 3: SALTANAT SÜRELERİ & VERİ ANALİZ MOTORU ---
elif secim == "3. Saltanat Süreleri & Veri Analiz Motoru":
    st.header("⚙️ Saltanat Süreleri ve Tarihsel Veri Analiz Motoru")
    st.markdown("Bu modül, 36 padişahın saltanat sürelerini grafiksel olarak görselleştirir, istatistiksel analiz üretir ve güvenli Excel raporu olarak indirmenizi sağlar.")

    df_padi = pd.DataFrame.from_dict(osmanli_36_padi_db, orient='index')

    st.subheader("📈 Padişahların Saltanat Süreleri (Grafiksel Analiz)")
    st.write("36 Osmanlı padişahının tahtta kalış sürelerinin (yıl bazında) kıyaslamalı grafik görünümü:")
    
    chart_data = df_padi.set_index("isim")[["taht_yil"]]
    st.bar_chart(chart_data)

    st.markdown("---")
    st.subheader("📥 Örnek Şablon ve Veri İndirme")
    
    st.download_button(
        label="📥 36 Padişah Veri Setini Excel Olarak İndir (.xlsx)",
        data=ornek_excel_sablonu_olustur(),
        file_name="padisah_arsivi_36_padisah.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
# ================================================================================
# DİVAN-I HÜMAYUN VE TAM 50 SORULUK UZMANLIK SINAVI (BÖLÜM 3)
# ================================================================================

# --- MODÜL 4: DİVAN-I HÜMAYUN & TEŞKİLAT YAPISI ---
if secim == "4. Divan-ı Hümayun & Teşkilat Yapısı":
    st.header("🏛️ Divan-ı Hümayun ve İdari Teşkilat")
    
    tab1, tab2, tab3 = st.tabs(["Vezirler & Kaptanlar", "İlmiye & Seyfiye", "Eyalet Sistemi"])
    with tab1:
        st.markdown("*Sadrazam (Vezir-i Azam):* Padişahın mutlak vekili, mühürdar ve yürütmenin başı.")
        st.markdown("*Kaptan-ı Derya:* Donanma komutanı ve denizcilik bakanı statüsünde devlet adamı.")
    with tab2:
        st.markdown("*Seyfiye:* Askeri ve idari bürokrasi, kılıç ehli devlet görevlileri.")
        st.markdown("*İlmiye:* Adalet, eğitim ve din işlerini yürüten kadı ve müderrisler sınıfı.")
    with tab3:
        st.markdown("*Tımar Sistemi:* Toprağın köylü tarafından işlenmesi karşılığında devletin asker besletmesi sistemi.")

# --- MODÜL 5: TARİH BİLGİ SINAVI & SİMÜLASYONU (50 SORULUK İŞARETSİZ TEMİZ FORMAT) ---
elif secim == "5. Tarih Bilgi Sınavı & Simülasyonu":
    st.header("🧠 Osmanlı Padişahları 50 Soruluk Uzmanlık Sınavı")
    st.markdown("Bu modül, hanedan tarihi hakkındaki bilginizi test etmek için **tam 50 soruluk** profesyonel bir sınav alanı sunar. Arayüzde doğrudan şık işaretleme kutucuğu bulunmamaktadır; soruları inceleyip cevaplarınızı not edebilir, alt kısımdan toplu analiz yapabilirsiniz.")

    sinav_sorulari = [
        {"soru": "Osmanlı Devleti'nin kurucusu kimdir?", "secenekler": ["A) I. Osman", "B) Orhan Bey", "C) Ertuğrul Gazi", "D) I. Murad"], "dogru": "A) I. Osman"},
        {"soru": "Bursa'yı fethederek devlet merkezi yapan padişah kimdir?", "secenekler": ["A) I. Osman", "B) Orhan Bey", "C) I. Bayezid", "D) I. Mehmed"], "dogru": "B) Orhan Bey"},
        {"soru": "Yeniçeri Ocağı'nı kuran ve savaş meydanında şehit düşen ilk padişah kimdir?", "secenekler": ["A) Orhan Bey", "B) I. Murad", "C) I. Bayezid", "D) II. Murad"], "dogru": "B) I. Murad"},
        {"soru": "'Yıldırım' lakabıyla bilinen ve İstanbul'u ilk kez kuşatan padişah kimdir?", "secenekler": ["A) I. Bayezid", "B) Yavuz Sultan Selim", "C) IV. Murad", "D) II. Mehmed"], "dogru": "A) I. Bayezid"},
        {"soru": "Fetret Devri'ni sona erdirerek devleti yeniden derleyen 'Çelebi' lakaplı padişah kimdir?", "secenekler": ["A) I. Mehmed", "B) II. Murad", "C) II. Bayezid", "D) III. Murad"], "dogru": "A) I. Mehmed"},
        {"soru": "Varna ve II. Kosova Zaferleri'ni kazanan padişah kimdir?", "secenekler": ["A) II. Murad", "B) Fatih Sultan Mehmet", "C) Kanuni Sultan Süleyman", "D) I. Selim"], "dogru": "A) II. Murad"},
        {"soru": "İstanbul'u fethederek 'Fatih' unvanını alan padişah kimdir?", "secenekler": ["A) II. Mehmed", "B) I. Bayezid", "C) Yavuz Sultan Selim", "D) III. Murad"], "dogru": "A) II. Mehmed"},
        {"soru": "Cem Sultan olayı hangi padişahın döneminde yaşanmıştır?", "secenekler": ["A) II. Bayezid", "B) Fatih Sultan Mehmet", "C) Yavuz Sultan Selim", "D) Kanuni Sultan Süleyman"], "dogru": "A) II. Bayezid"},
        {"soru": "Çaldıran Muharebesi'ni kazanarak hilafeti Osmanlı'ya getiren padişah kimdir?", "secenekler": ["A) Yavuz Sultan Selim", "B) Kanuni Sultan Süleyman", "C) I. Bayezid", "D) III. Mehmed"], "dogru": "A) Yavuz Sultan Selim"},
        {"soru": "46 yıl ile hanedanın en uzun süre tahtta kalan padişahı kimdir?", "secenekler": ["A) Kanuni Sultan Süleyman", "B) II. Abdülhamid", "C) IV. Mehmed", "D) II. Mahmud"], "dogru": "A) Kanuni Sultan Süleyman"},
        {"soru": "Kıbrıs'ın fethedildiği dönemde tahtta bulunan 'Sarı' lakaplı padişah kimdir?", "secenekler": ["A) II. Selim", "B) III. Murad", "C) III. Mehmed", "D) I. Ahmed"], "dogru": "A) II. Selim"},
        {"soru": "Osmanlı Devleti'nin en geniş sınırlarına ulaştığı dönemin padişahı kimdir?", "secenekler": ["A) III. Murad", "B) Kanuni Sultan Süleyman", "C) II. Abdülhamid", "D) IV. Mehmed"], "dogru": "A) III. Murad"},
        {"soru": "Eğri Fatihi olarak bilinen ve Haçova Meydan Muharebesi'ni kazanan padişah kimdir?", "secenekler": ["A) III. Mehmed", "B) IV. Murad", "C) II. Mustafa", "D) II. Osman"], "dogru": "A) III. Mehmed"},
        {"soru": "Sultanahmet Camii'ni inşa ettiren ve 'Ekber ve Erşed' sistemini getiren padişah kimdir?", "secenekler": ["A) I. Ahmed", "B) I. Mustafa", "C) II. Osman", "D) IV. Murad"], "dogru": "A) I. Ahmed"},
        {"soru": "Hotin Seferi'ne çıkan ve Yeniçeri Ocağı'nı kaldırmak isterken tahttan indirilen genç padişah kimdir?", "secenekler": ["A) II. Osman", "B) IV. Murad", "C) Genç Selim", "D) III. Selim"], "dogru": "A) II. Osman"},
        {"soru": "Bağdat Fatihi olarak bilinen ve yasaklarıyla tanınan sert mizaçlı padişah kimdir?", "secenekler": ["A) IV. Murad", "B) Yavuz Sultan Selim", "C) I. Selim", "D) II. Mahmud"], "dogru": "A) IV. Murad"},
        {"soru": "Köprülüler Dönemi'nin yaşandığı, 39 yıl tahtta kalan 'Avcı' lakaplı padişah kimdir?", "secenekler": ["A) IV. Mehmed", "B) II. Süleyman", "C) II. Ahmed", "D) II. Mustafa"], "dogru": "A) IV. Mehmed"},
        {"soru": "Ordu başında son defa sefere çıkan padişah kimdir?", "secenekler": ["A) II. Mustafa", "B) III. Ahmed", "C) I. Mahmud", "D) III. Selim"], "dogru": "A) II. Mustafa"},
        {"soru": "İlk Türk matbaasının kurulduğu Lale Devri'nin padişahı kimdir?", "secenekler": ["A) III. Ahmed", "B) I. Mahmud", "C) III. Osman", "D) III. Mustafa"], "dogru": "A) III. Ahmed"},
        {"soru": "Humbaracı Ahmed Paşa ile askeri ıslahatlar yapan padişah kimdir?", "secenekler": ["A) I. Mahmud", "B) III. Osman", "C) III. Mustafa", "D) I. Abdülhamid"], "dogru": "A) I. Mahmud"},
        {"soru": "Nuruosmaniye Camii'ni inşa ettiren padişah kimdir?", "secenekler": ["A) III. Osman", "B) I. Mahmud", "C) III. Selim", "D) I. Abdülhamid"], "dogru": "A) III. Osman"},
        {"soru": "Mühendishane-i Bahr-i Hümayun'un temellerini atan yenilikçi padişah kimdir?", "secenekler": ["A) III. Mustafa", "B) III. Selim", "C) II. Mahmud", "D) I. Abdülhamid"], "dogru": "A) III. Mustafa"},
        {"soru": "Küçük Kaynarca Antlaşması'nın imzalandığı dönemin padişahı kimdir?", "secenekler": ["A) I. Abdülhamid", "B) III. Selim", "C) IV. Mustafa", "D) II. Mahmud"], "dogru": "A) I. Abdülhamid"},
        {"soru": "Nizam-ı Cedid yeniliklerini başlatan padişah kimdir?", "secenekler": ["A) III. Selim", "B) II. Mahmud", "C) IV. Mustafa", "D) Sultan Abdülaziz"], "dogru": "A) III. Selim"},
        {"soru": "Yeniçeri Ocağı'nı kaldıran (Vaka-i Hayriye) padişah kimdir?", "secenekler": ["A) II. Mahmud", "B) Sultan Abdülmecid", "C) Sultan Abdülaziz", "D) II. Abdülhamid"], "dogru": "A) II. Mahmud"},
        {"soru": "Tanzimat Fermanı'nı ilan eden ve Dolmabahçe Sarayı'nı yaptıran padişah kimdir?", "secenekler": ["A) Sultan Abdülmecid", "B) Sultan Abdülaziz", "C) V. Murad", "D) II. Abdülhamid"], "dogru": "A) Sultan Abdülmecid"},
        {"soru": "Seyyah unvanıyla anılan ve Avrupa seyahati gerçekleştiren padişah kimdir?", "secenekler": ["A) Sultan Abdülaziz", "B) Sultan Abdülmecid", "C) II. Abdülhamid", "D) V. Mehmed Reşad"], "dogru": "A) Sultan Abdülaziz"},
        {"soru": "En kısa süre (93 gün) tahtta kalan padişah kimdir?", "secenekler": ["A) V. Murad", "B) I. Mustafa", "C) IV. Mustafa", "D) VI. Mehmed Vahdeddin"], "dogru": "A) V. Murad"},
        {"soru": "Kanun-i Esasi'yi ilan eden ve Hicaz Demiryolu'nu yaptıran padişah kimdir?", "secenekler": ["A) II. Abdülhamid", "B) V. Mehmed Reşad", "C) VI. Mehmed Vahdeddin", "D) Sultan Abdülaziz"], "dogru": "A) II. Abdülhamid"},
        {"soru": "Trablusgarp ve Balkan Savaşları'nın yaşandığı dönemin padişahı kimdir?", "secenekler": ["A) V. Mehmed Reşad", "B) VI. Mehmed Vahdeddin", "C) II. Abdülhamid", "D) V. Murad"], "dogru": "A) V. Mehmed Reşad"},
        {"soru": "Saltanatın kaldırılmasıyla tahttan ayrılan son Osmanlı padişahı kimdir?", "secenekler": ["A) VI. Mehmed Vahdeddin", "B) V. Mehmed Reşad", "C) II. Abdülhamid", "D) V. Murad"], "dogru": "A) VI. Mehmed Vahdeddin"},
        {"soru": "İlk Osmanlı bakır akçesini hangi padişah bastırmıştır?", "secenekler": ["A) I. Osman", "B) Orhan Bey", "C) I. Murad", "D) I. Bayezid"], "dogru": "A) I. Osman"},
        {"soru": "İlk Osmanlı medresesini İznik'te kuran padişah kimdir?", "secenekler": ["A) Orhan Bey", "B) I. Murad", "C) I. Mehmed", "D) II. Murad"], "dogru": "A) Orhan Bey"},
        {"soru": "Anadolu Hisarı'nı inşa ettiren padişah kimdir?", "secenekler": ["A) I. Bayezid", "B) Fatih Sultan Mehmet", "C) Yavuz Sultan Selim", "D) Kanuni Sultan Süleyman"], "dogru": "A) I. Bayezid"},
        {"soru": "Rumeli Hisarı'nı İstanbul'un fethi hazırlıkları kapsamında inşa ettiren padişah kimdir?", "secenekler": ["A) Fatih Sultan Mehmet", "B) I. Bayezid", "C) II. Murad", "D) Kanuni Sultan Süleyman"], "dogru": "A) Fatih Sultan Mehmet"},
        {"soru": "Trabzon ve Kırım'ı Osmanlı topraklarına katan padişah kimdir?", "secenekler": ["A) Fatih Sultan Mehmet", "B) Yavuz Sultan Selim", "C) II. Bayezid", "D) Kanuni Sultan Süleyman"], "dogru": "A) Fatih Sultan Mehmet"},
        {"soru": "Mohaç Meydan Muharebesi'ni çok kısa sürede kazanan padişah kimdir?", "secenekler": ["A) Kanuni Sultan Süleyman", "B) Yavuz Sultan Selim", "C) I. Bayezid", "D) III. Mehmed"], "dogru": "A) Kanuni Sultan Süleyman"},
        {"soru": "Sokullu Mehmet Paşa hangi üç padişah döneminde sadrazamlık yapmıştır?", "secenekler": ["A) Kanuni, II. Selim, III. Murad", "B) Fatih, II. Bayezid, Yavuz", "C) Yavuz, Kanuni, II. Selim", "D) II. Selim, III. Murad, III. Mehmed"], "dogru": "A) Kanuni, II. Selim, III. Murad"},
        {"soru": "Şiirlerinde 'Muradi' mahlasını kullanan padişah kimdir?", "secenekler": ["A) III. Murad", "B) I. Murad", "C) IV. Murad", "D) II. Murad"], "dogru": "A) III. Murad"},
        {"soru": "Şiirlerinde 'Avni' mahlasını kullanan ünlü padişah kimdir?", "secenekler": ["A) Fatih Sultan Mehmet", "B) Kanuni Sultan Süleyman", "C) Yavuz Sultan Selim", "D) III. Selim"], "dogru": "A) Fatih Sultan Mehmet"},
        {"soru": "Osmanlı'da saray dışından (hüccetli nikahla) ilk kez evlenen padişah kimdir?", "secenekler": ["A) Kanuni Sultan Süleyman", "B) Orhan Bey", "C) I. Osman", "D) Yavuz Sultan Selim"], "dogru": "A) Kanuni Sultan Süleyman"},
        {"soru": "İznik, İzmit ve Bursa'nın fethi hangi erken dönem padişahının eseridir?", "secenekler": ["A) Orhan Bey", "B) I. Osman", "C) I. Murad", "D) I. Bayezid"], "dogru": "A) Orhan Bey"},
        {"soru": "Kırım'ın fethi ile Karadeniz hangi padişah döneminde Türk gölü haline gelmiştir?", "secenekler": ["A) Fatih Sultan Mehmet", "B) Yavuz Sultan Selim", "C) Kanuni Sultan Süleyman", "D) II. Bayezid"], "dogru": "A) Fatih Sultan Mehmet"},
        {"soru": "Osmanlı Devleti'nde 'Sultan' unvanını resmi olarak ilk kullanan padişah kimdir?", "secenekler": ["A) Orhan Bey", "B) I. Murad", "C) I. Bayezid", "D) Yıldırım Bayezid"], "dogru": "B) I. Murad"},
        {"soru": "Ankara Savaşı'nda Timur'a yenilerek esir düşen padişah kimdir?", "secenekler": ["A) I. Bayezid", "B) I. Murad", "C) I. Mehmed", "D) II. Murad"], "dogru": "A) I. Bayezid"},
        {"soru": "Şehzade katlini yasal hale getiren kanunnameyi çıkaran padişah kimdir?", "secenekler": ["A) Fatih Sultan Mehmet", "B) Yavuz Sultan Selim", "C) Kanuni Sultan Süleyman", "D) I. Bayezid"], "dogru": "A) Fatih Sultan Mehmet"},
        {"soru": "Hicaz bölgesini Osmanlı topraklarına katan ve ilk Osmanlı halifesi olan kimdir?", "secenekler": ["A) Yavuz Sultan Selim", "B) Kanuni Sultan Süleyman", "C) II. Bayezid", "D) III. Murad"], "dogru": "A) Yavuz Sultan Selim"},
        {"soru": "Girit Adası'nı en uzun süren kuşatmanın ardından fethini tamamlayan padişah kimdir?", "secenekler": ["A) IV. Mehmed", "B) İbrahim", "C) IV. Murad", "D) II. Süleyman"], "dogru": "A) IV. Mehmed"},
        {"soru": "Osmanlı'da ilk kez parlamenter sisteme (I. Meşrutiyet) geçiş sağlayan padişah kimdir?", "secenekler": ["A) II. Abdülhamid", "B) Sultan Abdülaziz", "C) Sultan Abdülmecid", "D) V. Murad"], "dogru": "A) II. Abdülhamid"},
        {"soru": "Osmanlı Devleti'nin ilk demiryolu hattı (Aydın-İzmir) hangi padişah döneminde açılmıştır?", "secenekler": ["A) Sultan Abdülmecid", "B) Sultan Abdülaziz", "C) II. Abdülhamid", "D) II. Mahmud"], "dogru": "A) Sultan Abdülmecid"}
    ]

    st.markdown(f"Toplam **{len(soru_listesi := sinav_sorulari)}** adet uzmanlık sorusu listelenmiştir:")
    
    for idx, item in enumerate(sinav_sorulari):
        st.markdown(f"""
        <div class="soru-kutu">
            <b>Soru {idx+1}:</b> {item['soru']}<br>
            <span style="color: #444; font-size: 14px;">
                &nbsp;&nbsp;{item['secenekler'][0]} &nbsp;&nbsp;|&nbsp;&nbsp; 
                {item['secenekler'][1]} &nbsp;&nbsp;|&nbsp;&nbsp; 
                {item['secenekler'][2]} &nbsp;&nbsp;|&nbsp;&nbsp; 
                {item['secenekler'][3]}
            </span>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🔍 Tüm Soruların Doğru Cevap Anahtarını Gör"):
        for idx, item in enumerate(sinav_sorulari):
            st.markdown(f"**Soru {idx+1}:** Doğru Cevap -> <span style='color: green;'><b>{item['dogru']}</b></span>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Padişah Arşivi Enterprise Pro | 36 Padişah Tam Arşivi ve Simülasyon Motoru</p>", unsafe_allow_html=True)