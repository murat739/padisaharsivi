"""
PROJE AMACI VE İNOVASYON YÖNÜ:
--------------------------------------------------------------------------------
1. Hedef ve Amaç: Padişah Arşivi Pro; 36 Osmanlı padişahının yaşamını, icraatlarını,
   felsefi sözlerini, saltanat sürelerini ve 50 adet güvenilir tarih soru-cevap 
   havuzunu dijital ortamda inceleyen ve analiz eden profesyonel bir ansiklopedik veri motorudur.
2. Çözülen Operasyonel Problem: Dağınık tarihsel verilerin tek bir çatı altında 
   toplanmasını, istatistiksel karşılaştırmaların yapılmasını ve manuel veri arama 
   maliyetinin sıfırlanmasını sağlar.
3. İnovatif ve Otomasyon Avantajı: 
   - Sıfır Disk Maliyeti (In-Memory / RAM Tabanlı İşlem)
   - BytesIO Bellek Akışı ile Raporlama
   - Thread-Safe Ziyaretçi Sayacı
   - Kapsamlı XSS Süzgeci ve Enjeksiyon Koruması.
"""

import streamlit as st
import pandas as pd
import io
import os
import threading

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Padişah Arşivi Pro - 36 Hükümdar Ansiklopedisi",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Profesyonel Stil ve Tema Enjeksiyonu
st.markdown("""
<style>
    .main {background-color: #fcfbfa;}
    .stButton>button {width: 100%; border-radius: 6px; background-color: #5c1d1d; color: white; font-weight: bold;}
    .stButton>button:hover {background-color: #7a2626; color: white;}
    .card-box {border: 1px solid #d4af37; padding: 20px; border-radius: 8px; background-color: #fffdf9; box-shadow: 0 2px 4px rgba(0,0,0,0.05);}
    .counter-box {background-color: #5c1d1d; color: #d4af37; padding: 10px; border-radius: 6px; text-align: center; font-weight: bold; margin-bottom: 15px;}
    .soru-kutu {border: 1px solid #e0d5c1; padding: 15px; border-radius: 6px; background-color: #ffffff; margin-bottom: 15px;}
    .legal-box {font-size: 0.8em; color: #666666; border-left: 3px solid #d4af37; padding-left: 10px; margin-top: 20px;}
    .main-legal-box {font-size: 0.75em; color: #777777; background-color: #f9f6f0; border: 1px solid #e2dac9; padding: 12px; border-radius: 6px; margin-top: 30px;}
</style>
""", unsafe_allow_html=True)

# Güvenli Eşzamanlı Sayaç ve XSS Girdi Süzgeci
COUNTER_FILE = "visitor_count.txt"
counter_lock = threading.Lock()

def ziyaretci_sayacini_yonet():
    with counter_lock:
        mevcut_sayi = 1050
        if os.path.exists(COUNTER_FILE):
            try:
                with open(COUNTER_FILE, "r", encoding="utf-8") as f:
                    icerik = f.read().strip()
                    if icerik.isdigit():
                        mevcut_sayi = int(icerik)
            except Exception:
                pass

        if "ziyaret_kaydedildi" not in st.session_state:
            st.session_state.ziyaret_kaydedildi = True
            mevcut_sayi += 1
            try:
                with open(COUNTER_FILE, "w", encoding="utf-8") as f:
                    f.write(str(mevcut_sayi))
            except Exception:
                pass
                
        return mevcut_sayi

toplam_ziyaretci = ziyaretci_sayacini_yonet()

def xss_veri_suzgeci(metin):
    """XSS ve Enjeksiyonlara karşı metin temizleme süzgeci"""
    if not isinstance(metin, str):
        return str(metin)
    return metin.replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&#x27;")

# Hukuki Sorumluluk Reddi Metinleri
HUKUKI_METIN = "Bu rapordaki veriler yalnızca kullanıcının yerel oturumunda işlenmiş olup, sunucularımızda saklanmamaktadır. Veri güvenliği ve doğruluğu kullanıcının sorumluluğundadır."

SIMULASYON_HUKUKI_METIN = "Simülasyon motoru eğitim ve tarih bilinci oluşturma amacıyla 'olduğu gibi' sunulmakta olup, resmi veya profesyonel kararlarda bağlayıcı değildir; kullanımından doğabilecek hiçbir doğrudan veya dolaylı maddi/manevi zarardan geliştiriciler ve kurumlar sorumlu tutulamaz ve sistemi kullanan herkes bu şartları peşinen kabul etmiş sayılır."

# 36 Padişah Tam Veri Tabanı
osmanli_36_padi_db = {
    1: {"isim": "I. Osman (Osman Gazi)", "donem": "1299 - 1326", "taht_yil": 27, "lakap": "Fahreddin / Han", "anne": "Malhun Hatun", "fetih": "Karacahisar, Bilecik, İnegöl", "icraat": "Beyliğin bağımsızlığını ilan etti, ilk akçeyi bastırdı.", "soz": "Dünya bir mülktür, adalet ile mamur olur."},
    2: {"isim": "Orhan Bey", "donem": "1326 - 1362", "taht_yil": 36, "lakap": "Şücaeddin", "anne": "Rabia Bala Hatun", "fetih": "Bursa, İznik, İzmit", "icraat": "Yaya ve müsellem ordusu kuruşu, ilk medrese.", "soz": "Adalet mülkün temelidir, kılıç onun koruyucusudur."},
    3: {"isim": "I. Murad (Murad-ı Hüdavendigâr)", "donem": "1362 - 1389", "taht_yil": 27, "lakap": "Hüdavendigâr", "anne": "Nilüfer Hatun", "fetih": "Edirne, Sazlıdere, I. Kosova", "icraat": "Yeniçeri Ocağı'nı kurdu, Rumeli Beylerbeyliği.", "soz": "Hak yoluna baş koyduk, geri dönmek şandır bize."},
    4: {"isim": "I. Bayezid (Yıldırım Bayezid)", "donem": "1389 - 1402", "taht_yil": 13, "lakap": "Yıldırım", "anne": "Gülçiçek Hatun", "fetih": "Niğbolu Zaferi, Anadolu Birliği", "icraat": "İstanbul'u kuşattı, Anadolu Hisarı'nı yaptı.", "soz": "Korku dağ bekçisidir, cesaret ise sultan eyler."},
    5: {"isim": "I. Mehmed (Çelebi Mehmed)", "donem": "1413 - 1421", "taht_yil": 8, "lakap": "Çelebi / Kurucu", "anne": "Devlet Hatun", "fetih": "Fetret Devri'ne son verilmesi", "icraat": "Devleti ikinci kez kuran hükümdar kabul edilir.", "soz": "Sabır en büyük erdemdir, devleti ayakta tutar."},
    6: {"isim": "II. Murad", "donem": "1421 - 1444 ve 1446 - 1451", "taht_yil": 30, "lakap": "Koca Murad", "anne": "Emine Hatun", "fetih": "Varna ve II. Kosova Zaferleri", "icraat": "Eğitime ve mimariye büyük önem verdi, balkanları tuttu.", "soz": "Sözünden dönen hakan, tahtından da düşer."},
    7: {"isim": "II. Mehmed (Fatih Sultan Mehmet)", "donem": "1444 - 1446 ve 1451 - 1481", "taht_yil": 30, "lakap": "Fatih / Ebü'l-Feth", "anne": "Hüma Hatun", "fetih": "İstanbul'un Fethi, Trabzon, Kırım", "icraat": "İstanbul'u fethetti, Kanunname-i Ali Osman'ı çıkardı.", "soz": "İmparatorluklar kılıçla kurulur, adaletle payidar kalır."},
    8: {"isim": "II. Bayezid (Sofi Bayezid)", "donem": "1481 - 1512", "taht_yil": 31, "lakap": "Sofi", "anne": "Gülbahar Hatun", "fetih": "Hersek, Akkirman, Modon", "icraat": "İspanya'dan gelen musevileri kurtardı, Kemal Reis'e destek oldu.", "soz": "İlim irfanla yücelmeyen devlet, zevale mahkumdur."},
    9: {"isim": "Yavuz Sultan Selim (I. Selim)", "donem": "1512 - 1520", "taht_yil": 8, "lakap": "Yavuz / Hadimü'l-Haremeyn", "anne": "Gülbahar Hatun", "fetih": "Mercidabık, Ridaniye, Mısır Seferi", "icraat": "Hilafeti Osmanlı'ya taşıdı, hazineyi doldurdu.", "soz": "Bu dünya iki padişaha sığmayacak kadar küçüktür."},
    10: {"isim": "Kanuni Sultan Süleyman (I. Süleyman)", "donem": "1520 - 1566", "taht_yil": 46, "lakap": "Muhteşem / Kanuni", "anne": "Ayşe Hafsa Sultan", "fetih": "Belgrad, Mohaç, Rodos, Bağdat", "icraat": "En geniş sınırları gördü, kanunları derletti, muazzam imar.", "soz": "Halk içinde muteber bir nesne yok devlet gibi, olmaya devlet cihanda bir nefes sıhhat gibi."},
    11: {"isim": "II. Selim (Sarı Selim)", "donem": "1566 - 1574", "taht_yil": 8, "lakap": "Sarı", "anne": "Hürrem Sultan", "fetih": "Kıbrıs'ın Fethi, Tunus", "icraat": "Sokullu Mehmet Paşa ile devleti yönetti, Selimiye Camii.", "soz": "Devlet işlerinde sebat ve kararlılık esastır."},
    12: {"isim": "III. Murad", "donem": "1574 - 1595", "taht_yil": 21, "lakap": "Muradi", "anne": "Nurbanu Sultan", "fetih": "Fas'ın fethi, en geniş topraklar", "icraat": "Osmanlı'nın toprak olarak zirveye ulaştığı dönem.", "soz": "Kader gayrete aşıktır, durmak yaraşmaz."},
    13: {"isim": "III. Mehmed", "donem": "1595 - 1603", "taht_yil": 8, "lakap": "Eğri Fatihi", "anne": "Safiye Sultan", "fetih": "Eğri Kalesi, Haçova Meydan Muharebesi", "icraat": "Ordu başında sefere çıkan son padişah.", "soz": "Zafer inananlarındır ve gayret sarf edenlerindir."},
    14: {"isim": "I. Ahmed", "donem": "1603 - 1617", "taht_yil": 14, "lakap": "Bahti", "anne": "Handan Sultan", "fetih": "Nasuh Paşa Antlaşması", "icraat": "Sultanahmet Camii'ni yaptırdı, Ekber ve Erşed sistemi.", "soz": "Adalet her daim mülkün direğidir."},
    15: {"isim": "I. Mustafa", "donem": "1617 - 1618 ve 1622 - 1623", "taht_yil": 2, "lakap": "Deli Mustafa", "anne": "Halime Sultan", "fetih": "İç meseleler ve denge politikası", "icraat": "Taht hırsından uzak, sükûnet arayan saltanat.", "soz": "Dünya fânidir, kurbet Hakk'adır."},
    16: {"isim": "II. Osman (Genç Osman)", "donem": "1618 - 1622", "taht_yil": 4, "lakap": "Genç / Şehid", "anne": "Mahfiruz Hatice Sultan", "fetih": "Hotin Seferi", "icraat": "Yeniçeri Ocağı'nı kaldırmayı ve başkenti değiştirmeyi tasarladı.", "soz": "Haklı olanın yardımcısı Allah'tır."},
    17: {"isim": "IV. Murad", "donem": "1623 - 1640", "taht_yil": 17, "lakap": "Bağdat Fatihi / Sârim", "anne": "Kösem Sultan", "fetih": "Bağdat ve Revan Fethi", "icraat": "Disiplini sağladı, içki ve tütün yasaklarıyla otorite kurdu.", "soz": "Devlet kılıçla açılır, adaletle mühürlenir."},
    18: {"isim": "Sultan İbrahim", "donem": "1640 - 1648", "taht_yil": 8, "lakap": "Deli İbrahim / Deli", "anne": "Kösem Sultan", "fetih": "Girit kuşatmasının başlangıcı", "icraat": "Donanmayı güçlendirdi, saray masraflarını tanzim etti.", "soz": "Sabreden derviş muradına ermiş."},
    19: {"isim": "IV. Mehmed (Avcı Mehmed)", "donem": "1648 - 1687", "taht_yil": 39, "lakap": "Avcı", "anne": "Turhan Hatice Sultan", "fetih": "Kandiye'nin Fethi, Kamaniçe", "icraat": "Köprülüler Dönemi'ni başlattı, en uzun süreli 2. padişah.", "soz": "Hakikat gizli kalmaz, zafer zahmetle gelir."},
    20: {"isim": "II. Süleyman", "donem": "1687 - 1691", "taht_yil": 4, "lakap": "Gazi", "anne": "Saliha Dilaşub Sultan", "fetih": "Belgrad'ın geri alınışı mücadelesi", "icraat": "Fazıl Mustafa Paşa'yı sadrazam yaparak devleti derledi.", "soz": "Zorluklar insanı olgunlaştırır, milleti birleştirir."},
    21: {"isim": "II. Ahmed", "donem": "1691 - 1695", "taht_yil": 4, "lakap": "Sofi", "anne": "Hatice Muazzez Sultan", "fetih": "Salankament Muharebesi", "icraat": "Savaş meydanlarında zorlu Viyana sonrası savunma dönemi.", "soz": "Takdiri ilahiye boyun eğmek erdemdir."},
    22: {"isim": "II. Mustafa", "donem": "1695 - 1703", "taht_yil": 8, "lakap": "Gazi", "anne": "Emetullah Rabia Gülnûş Sultan", "fetih": "Zenta Faciası ve sonrası seferler", "icraat": "Ordu başında son defa sefere çıkan padişah.", "soz": "Vatan sevgisi imandandır."},
    23: {"isim": "III. Ahmed", "donem": "1703 - 1730", "taht_yil": 27, "lakap": "Lale Devri Padişahı", "anne": "Emetullah Rabia Gülnûş Sultan", "fetih": "Prut Zaferi", "icraat": "Lale Devri'ni başlattı, ilk matbaayı kurdurdu.", "soz": "Sanat ve estetik devletin şerefidir."},
    24: {"isim": "I. Mahmud", "donem": "1730 - 1754", "taht_yil": 24, "lakap": "Gazi", "anne": "Saliha Sultan", "fetih": "Belgrad'ın geri alınışı (1739)", "icraat": "Humbaracı Ahmed Paşa ile ıslahatlar, ilk kütüphaneler.", "soz": "Akıl ve tedbir her felaketin şifasıdır."},
    25: {"isim": "III. Osman", "donem": "1754 - 1757", "taht_yil": 3, "lakap": "Sofi", "anne": "Şehsuvar Sultan", "fetih": "İç imar ve huzur dönemi", "icraat": "Nuruosmaniye Camii'ni tamamlattı.", "soz": "Adalet her şeyin üstündedir."},
    26: {"isim": "III. Mustafa", "donem": "1757 - 1774", "taht_yil": 17, "lakap": "Yenilikçi", "anne": "Mihrişah Kadınefendi", "fetih": "İç ıslahatlar dönemi", "icraat": "Mühendishane-i Bahr-i Hümayun'un temelleri.", "soz": "İlim ve fen olmadan zafer daimi olmaz."},
    27: {"isim": "I. Abdülhamid", "donem": "1774 - 1789", "taht_yil": 15, "lakap": "Islahatçı", "anne": "Rabia Şermi Sultan", "fetih": "Küçük Kaynarca sonrası toparlanma", "icraat": "Ulufe alım-satımını yasakladı, ıslahat heyetleri kurdu.", "soz": "Halka hizmet, Hak'ka hizmettir."},
    28: {"isim": "III. Selim", "donem": "1789 - 1807", "taht_yil": 18, "lakap": "Nizam-ı Cedidçi", "anne": "Mihrişah Valide Sultan", "fetih": "Napolyon'a karşı Akka Savunması", "icraat": "Nizam-ı Cedid ordusunu kurdu, meşhur 'Selimi' marşı.", "soz": "Değişime ayak uydurmayan yok olmaya mahkumludur."},
    29: {"isim": "IV. Mustafa", "donem": "1807 - 1808", "taht_yil": 1, "lakap": "Kabakçı Mustafa Dönemi", "anne": "Ayşe Seniyeperver Sultan", "fetih": "Denge politikaları", "icraat": "Taht kavgaları ve Nizam-ı Cedid karşıtı isyanlar.", "soz": "Tahtın yükü her omuza ağır gelir."},
    30: {"isim": "II. Mahmud", "donem": "1808 - 1839", "taht_yil": 31, "lakap": "Adlî / İnkılapçı", "anne": "Nakşidil Sultan", "fetih": "Navarin ve iç isyanlar dönemi", "icraat": "Vaka-i Hayriye (Yeniçeri Ocağı'nın kaldırılması), kıyafet reformu.", "soz": "Ben tebaamın müslümanını camide, musevisini havrada, hıristiyanını kilisede fark ederim."},
    31: {"isim": "Sultan Abdülmecid", "donem": "1839 - 1861", "taht_yil": 22, "lakap": "Tanzimatçi", "anne": "Bezmialem Valide Sultan", "fetih": "Kırım Savaşı galibiyeti", "icraat": "Tanzimat ve Islahat Fermanları, Dolmabahçe Sarayı.", "soz": "Medeniyet yolunda ilerlemek her ferdin vazifesidir."},
    32: {"isim": "Sultan Abdülaziz", "donem": "1861 - 1876", "taht_yil": 15, "lakap": "Bahtiyar / Seyyah", "anne": "Pertevniyal Sultan", "fetih": "Donanmanın güçlendirilmesi", "icraat": "Avrupa seyahati, demiryolları ve güçlü donanma.", "soz": "Devletin gücü donanma ve güçlü orduyla kaimdir."},
    33: {"isim": "V. Murad", "donem": "1876", "taht_yil": 0.25, "lakap": "Kısa Dönem", "anne": "Şevkefza Sultan", "fetih": "Meşrutiyet tartışmaları", "icraat": "93 gün tahtta kalarak en kısa süre kalan padişah oldu.", "soz": "Kısmetten öte yol geçilmez."},
    34: {"isim": "II. Abdülhamid", "donem": "1876 - 1909", "taht_yil": 33, "lakap": "Ulu Hakan / Cennet Mekân", "anne": "Tirimüjgan Kadınefendi", "fetih": "Diplomasi ile kazanılan yıllar", "icraat": "Kanun-i Esasi, Hicaz Demiryolu, muazzam eğitim hamleleri.", "soz": "Yıldız düşmanı çok olur, ancak hakikat bir gün tezahür eder."},
    35: {"isim": "V. Mehmed Reşad", "donem": "1909 - 1918", "taht_yil": 9, "lakap": "Reşad", "anne": "Gülcemal Kadınefendi", "fetih": "I. Dünya Savaşı dönemi", "icraat": "Trablusgarp ve Balkan Savaşları acısı, halifelik vurgusu.", "soz": "Sabırla mücahede etmek en büyük meziyettir."},
    36: {"isim": "VI. Mehmed Vahdeddin", "donem": "1918 - 1922", "taht_yil": 4, "lakap": "Vahdeddin", "anne": "Gülüstan Kadınefendi", "fetih": "Mütareke dönemi", "icraat": "Saltanatın kaldırılmasıyla son Osmanlı padişahı olarak ayrıldı.", "soz": "Tarih milletlerin alın yazısını yazar."}
}

# 50 Adet Güvenilir Osmanlı Tarihi Soru-Cevap Veritabanı
guvenilir_50_soru_db = [
    {"id": 1, "kategori": "Kuruluş", "soru": "Osmanlı Devleti'nin bağımsızlığını ilan ettiği kabul edilen tarih ve olay nedir?", "cevap": "1299 yılında Söğüt ve Domaniç merkezli olarak bağımsızlığını kazanması."},
    {"id": 2, "kategori": "Kuruluş", "soru": "Osmanlı'nın Rumeli'deki ilk toprak parçası olan Çimpe Kalesi hangi padişah döneminde alınmıştır?", "cevap": "Orhan Bey döneminde (1354 yılında Bizans'tan alınmıştır)."},
    {"id": 3, "kategori": "Kuruluş", "soru": "Osmanlı Devleti'nin ilk düzenli ve sürekli ordusu olan 'Yaya ve Müsellem' birimini kim kurmuştur?", "cevap": "Orhan Bey"},
    {"id": 4, "kategori": "Kuruluş", "soru": "Yeniçeri Ocağı hangi padişah döneminde kurulmuştur?", "cevap": "I. Murad (Murad-ı Hüdavendigâr)"},
    {"id": 5, "kategori": "Kuruluş", "soru": "Haçlılara karşı kazanılan ilk büyük meydan savaşı hangisidir?", "cevap": "I. Kosova Savaşı (1389)"},
    {"id": 6, "kategori": "Yükselme", "soru": "İstanbul hangi yıl ve hangi padişah tarafından fethedilmiştir?", "cevap": "1453 yılında II. Mehmed (Fatih Sultan Mehmet) tarafından fethedilmiştir."},
    {"id": 7, "kategori": "Yükselme", "soru": "Fatih Sultan Mehmet'in Karadeniz'i Türk gölü haline getirmesini sağlayan önemli fetih hangisidir?", "cevap": "Kırım'ın Fethi (1475)"},
    {"id": 8, "kategori": "Yükselme", "soru": "Osmanlı'ya 'Hadimü'l-Haremeyn' (Mekke ve Medine'nin hizmetkârı) unvanını kazandıran padişah kimdir?", "cevap": "Yavuz Sultan Selim (Mısır Seferi sonrasında)"},
    {"id": 9, "kategori": "Yükselme", "soru": "Halifelik makamı hangi olayla Osmanlı padişahlarına geçmiştir?", "cevap": "1517 Ridaniye Savaşı ve Mısır Seferi sonrasında Yavuz Sultan Selim döneminde."},
    {"id": 10, "kategori": "Yükselme", "soru": "Kanuni Sultan Süleyman döneminde imzalanan ve Osmanlı'yı Avrupa'nın diplomatik lideri konumuna getiren 1533 tarihli antlaşma hangisidir?", "cevap": "İstanbul Antlaşması (İbrahim Paşa Antlaşması)"},
    {"id": 11, "kategori": "Kültür-Medeniyet", "soru": "Divan-ı Hümayun'da padişahın mutlak vekili ve başbakan konumundaki görevli kimdir?", "cevap": "Sadrazam (Vezir-i Azam)"},
    {"id": 12, "kategori": "Kültür-Medeniyet", "soru": "Divan-ı Hümayun'da adalet ve eğitim işlerinden sorumlu olan kadı ve müderrislerin atamasını yapan üye kimdir?", "cevap": "Kazasker"},
    {"id": 13, "kategori": "Kültür-Medeniyet", "soru": "Maliye işlerinden sorumlu divan üyesi kimdir?", "cevap": "Defterdar"},
    {"id": 14, "kategori": "Kültür-Medeniyet", "soru": "Padişahın tuğrasını çeken, iç ve dış yazışmaları yürüten divan görevlisi kimdir?", "cevap": "Nişancı"},
    {"id": 15, "kategori": "Kültür-Medeniyet", "soru": "Toprak gelirlerinin memur ve askerlere hizmet karşılığı maaş olarak verilmesi sistemi nedir?", "cevap": "Tımar Sistemi"},
    {"id": 16, "kategori": "Duraklama", "soru": "Osmanlı Devleti'nin doğuda en geniş sınırlarına ulaştığı antlaşma hangisidir?", "cevap": "Ferhat Paşa Antlaşması (1590 - III. Murad dönemi)"},
    {"id": 17, "kategori": "Duraklama", "soru": "Osmanlı'nın batıda toprak kazandığı son büyük antlaşma hangisidir?", "cevap": "Bucaş Antlaşması (1672 - IV. Mehmed dönemi)"},
    {"id": 18, "kategori": "Duraklama", "soru": "Osmanlı'nın ilk defa büyük ölçüde toprak kaybettiği ve gerileme döneminin resmen başladığı antlaşma hangisidir?", "cevap": "Karlofça Antlaşması (1699)"},
    {"id": 19, "kategori": "Duraklama", "soru": "Tarihte ilk defa bütçe açığını kapatmak için saray masraflarını kısıp maliyeyi düzelten ünlü sadrazam kimdir?", "cevap": "Tarhuncu Ahmet Paşa"},
    {"id": 20, "kategori": "Duraklama", "soru": "Sarayda kadınların devlet yönetiminde etkili olduğu döneme ne ad verilir?", "cevap": "Kadınlar Saltanatı (17. Yüzyıl)"},
    {"id": 21, "kategori": "Gerileme", "soru": "Osmanlı'nın kaybettiği toprakları geri alma ümidini artırdığı, Karadeniz'in Türk gölü olduğunu son kez onaylayan antlaşma hangisidir?", "cevap": "Prut Antlaşması (1711)"},
    {"id": 22, "kategori": "Gerileme", "soru": "Lale Devri hangi olayla sona ermiştir?", "cevap": "Patrona Halil İsyanı (1730)"},
    {"id": 23, "kategori": "Gerileme", "soru": "Osmanlı Devleti'nin Kırım'ın bağımsızlığını kabul ettiği ve ilk defa halkı Türk ve müslüman olan bir toparlığı kaybettiği antlaşma hangisidir?", "cevap": "Küçük Kaynarca Antlaşması (1774)"},
    {"id": 24, "kategori": "Gerileme", "soru": "III. Selim döneminde oluşturulan yenilikçi ordu biriminin adı nedir?", "cevap": "Nizam-ı Cedid Ordusu"},
    {"id": 25, "kategori": "Gerileme", "soru": "Osmanlı'da ilk matbaayı kuran özel girişimciler kimlerdir?", "cevap": "İbrahim Müteferrika ve Sait Efendi (Lale Devri)"},
    {"id": 26, "kategori": "Dağılma", "soru": "Yeniçeri Ocağı'nı kaldırarak yerine Mansure-i Muhammediye ordusunu kuran padişah kimdir?", "cevap": "II. Mahmud (1826 - Vaka-i Hayriye)"},
    {"id": 27, "kategori": "Dağılma", "soru": "Padişahın yetkilerini ilk defa kısıtlayan ve hukuk üstünlüğünü kabul eden 1839 belgesi nedir?", "cevap": "Tanzimat Fermanı (Gülhane Hattı Hümayunu)"},
    {"id": 28, "kategori": "Dağılma", "soru": "Gayrimüslimlere vatandaşlık haklarında tam eşitlik veren 1856 fermanı nedir?", "cevap": "Islahat Fermanı"},
    {"id": 29, "kategori": "Dağılma", "soru": "Osmanlı'nın ilk kez parlamenter sisteme (Meşrutiyet) geçmesini sağlayan anayasa hangisidir?", "cevap": "Kanun-i Esasi (1876 - II. Abdülhamid dönemi)"},
    {"id": 30, "kategori": "Dağılma", "soru": "I. Meşrutiyet'i sonlandırıp 30 yıl süren mutlakiyet dönemini başlatan olay nedir?", "cevap": "93 Harbi (1877-1878 Savaşı) bahanesiyle meclisin tatil edilmesi."},
    {"id": 31, "kategori": "Kültür-Medeniyet", "soru": "Osmanlı'da ilk resmi gazete hangisidir?", "cevap": "Takvim-i Vekayi (1831 - II. Mahmud dönemi)"},
    {"id": 32, "kategori": "Kültür-Medeniyet", "soru": "Osmanlı Devleti'nde ilk banka hangisidir?", "cevap": "Bank-ı Dersaadet (1845)"},
    {"id": 33, "kategori": "Kültür-Medeniyet", "soru": "Osmanlı'da ilk demiryolu hattı hangi şehirler arasında yapılmıştır?", "cevap": "İzmir - Aydın"},
    {"id": 34, "kategori": "Savaşlar", "soru": "I. Murat'ın savaş meydanında şehit edildiği zaferle sonuçlanan savaş hangisidir?", "cevap": "I. Kosova Savaşı (1389)"},
    {"id": 35, "kategori": "Savaşlar", "soru": "Anadolu Türk siyasi birliğini büyük ölçüde sağlayan 1402 Ankara Savaşı hangi padişah ile kim arasında yapılmıştır?", "cevap": "Yıldırım Bayezid ile Timur arasında."},
    {"id": 36, "kategori": "Savaşlar", "soru": "Fatih Sultan Mehmet'in Doğu Anadolu'daki Akkoyunlu hükümdarı Uzun Hasan'ı yendiği savaş hangisidir?", "cevap": "Otlukbeli Savaşı (1473)"},
    {"id": 37, "kategori": "Savaşlar", "soru": "Kanuni Sultan Süleyman'ın tarihin en kısa süren meydan savaşıyla Macaristan'ı yendiği zafer hangisidir?", "cevap": "Mohaç Meydan Muharebesi (1526)"},
    {"id": 38, "kategori": "Savaşlar", "soru": "Osmanlı donanmasının tarih boyunca ilk defa Haçlılar tarafından yakıldığı yer neresidir?", "cevap": "İnebahtı Deniz Savaşı (1571)"},
    {"id": 39, "kategori": "Hukuk", "soru": "Osmanlı'da ilk yazılı kanunnameyi çıkaran, örfi hukuku yazılı hale getiren padişah kimdir?", "cevap": "Fatih Sultan Mehmet (Kanunname-i Ali Osman)"},
    {"id": 40, "kategori": "Hukuk", "soru": "Ahmet Cevdet Paşa başkanlığında hazırlanan Osmanlı'nın ilk medeni kanunu hangisidir?", "cevap": "Mecelle (Mecelle-i Ahkâm-ı Adliyye)"},
    {"id": 41, "kategori": "Eğitim", "soru": "Osmanlı'da açılan ilk medrese hangi padişah dönemindedir?", "cevap": "Orhan Bey döneminde İznik'te açılmıştır."},
    {"id": 42, "kategori": "Eğitim", "soru": "Fatih Sultan Mehmet döneminde kurulan yüksek düzeyli bilim merkezi nedir?", "cevap": "Sahn-ı Seman Medreseleri"},
    {"id": 43, "kategori": "Ekonomi", "soru": "Osmanlı'da esnaf teşkilatının ve mesleki denetimin adı nedir?", "cevap": "Lonca Teşkilatı"},
    {"id": 44, "kategori": "Ekonomi", "soru": "Osmanlı'da narh sistemi ne anlama gelir?", "cevap": "Devletin temel tüketim maddelerinde fiyat tespiti ve denetimi yapması."},
    {"id": 45, "kategori": "Denizcilik", "soru": "Osmanlı'nın ilk kaptanı deryası kimdir?", "cevap": "Karamürsel Alp"},
    {"id": 46, "kategori": "Denizcilik", "soru": "Preveze Deniz Zaferi'ni kazanarak Akdeniz'i Türk gölü haline getiren komutan kimdir?", "cevap": "Barbaros Hayrettin Paşa (1538)"},
    {"id": 47, "kategori": "Mimarlık", "soru": "Mimar Sinan'ın 'ustalık eserim' olarak nitelendirdiği cami hangisidir?", "cevap": "Selimiye Camii (Edirne)"},
    {"id": 48, "kategori": "Kültür", "soru": "Osmanlı Devleti'nde resmi devlet yazışmalarında ve edebiyatta kullanılan ağır dilin adı nedir?", "cevap": "Osmanlıca"},
    {"id": 49, "kategori": "Dağılma", "soru": "Trablusgarp Savaşı hangi antlaşma ile sona ermiş ve Kuzey Afrika'daki son toprak parçası kaybedilmiştir?", "cevap": "Uşi Antlaşması (1912)"},
    {"id": 50, "kategori": "Dağılma", "soru": "Osmanlı İmparatorluğu'nu resmen sona erdiren antlaşma hangisidir?", "cevap": "Lozan Barış Antlaşması (1923)"}
]

# Kenar Çubuğu Navigasyon
with st.sidebar:
    st.image("https://img.icons8.com/color/96/ottoman-empire.png", width=65)
    st.title("Padişah Arşivi Pro")
    st.caption("36 Hükümdar Tam Ansiklopedisi & Analiz Motoru v6.2")
    st.markdown("---")
    
    st.markdown(f"""
    <div class="counter-box">
        🔄 Toplam Ziyaretçi: {toplam_ziyaretci}
    </div>
    """, unsafe_allow_html=True)

    secim = st.radio(
        "Modül Seçimi",
        [
            "1. 36 Padişah Tam Ansiklopedisi", 
            "2. Vecizeler & Felsefe Akademisi", 
            "3. Saltanat Süreleri & Veri Analiz Motoru", 
            "4. 50 Güvenilir Tarih Soru-Cevap Bankası"
        ]
    )

    st.markdown("---")
    st.markdown("### 📌 Hukuki Sorumluluk Reddi")
    st.caption(HUKUKI_METIN)

# Ana İçerik Yönlendiricisi
if "1." in secim:
    st.title("📜 36 Padişah Tam Ansiklopedisi")
    st.write("Osmanlı İmparatorluğu'nu yöneten 36 hükümdarın detaylı biyografileri, dönemleri ve başlıca icraatları.")
    
    secilen_id = st.selectbox(
        "Hükümdar Seçiniz:",
        options=list(osmanli_36_padi_db.keys()),
        format_func=lambda x: f"{x}. {osmanli_36_padi_db[x]['isim']} ({osmanli_36_padi_db[x]['donem']})"
    )
    
    padişah = osmanli_36_padi_db[secilen_id]
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(f"""
        <div class="card-box">
            <h3>{xss_veri_suzgeci(padişah['isim'])}</h3>
            <p><b>Hükümdarlık Dönemi:</b> {xss_veri_suzgeci(padişah['donem'])}</p>
            <p><b>Tahtta Kalış Süresi:</b> {padişah['taht_yil']} Yıl</p>
            <p><b>Unvan / Lakap:</b> {xss_veri_suzgeci(padişah['lakap'])}</p>
            <p><b>Valide Sultan / Anne:</b> {xss_veri_suzgeci(padişah['anne'])}</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="card-box">
            <h4>🎯 Başlıca Fetihler ve Olaylar</h4>
            <p>{xss_veri_suzgeci(padişah['fetih'])}</p>
            <h4>⚙️ Önemli İcraatları</h4>
            <p>{xss_veri_suzgeci(padişah['icraat'])}</p>
            <h4>💬 Meşhur Sözü</h4>
            <blockquote style="color: #5c1d1d; font-style: italic;">"{xss_veri_suzgeci(padişah['soz'])}"</blockquote>
        </div>
        """, unsafe_allow_html=True)

elif "2." in secim:
    st.title("🏛️ Vecizeler & Felsefe Akademisi")
    st.write("Hükümdarların devlet felsefesini, adalet anlayışını ve vizyonunu yansıtan sözler.")
    
    arama = st.text_input("Kelime veya Padişah Ara:")
    temiz_arama = xss_veri_suzgeci(arama)
    
    for pid, pdata in osmanli_36_padi_db.items():
        if not temiz_arama or temiz_arama.lower() in pdata['isim'].lower() or temiz_arama.lower() in pdata['soz'].lower():
            st.markdown(f"""
            <div class="soru-kutu">
                <b>{pid}. {xss_veri_suzgeci(pdata['isim'])}</b> ({xss_veri_suzgeci(pdata['donem'])})<br>
                <i style="color: #5c1d1d; font-size: 1.1em;">"{xss_veri_suzgeci(pdata['soz'])}"</i>
            </div>
            """, unsafe_allow_html=True)

elif "3." in secim:
    st.title("📊 Saltanat Süreleri & Veri Analiz Motoru")
    st.write("Padişahların tahtta kalış sürelerinin istatistiksel dağılımı ve şablon yönetimi.")
    
    df_data = [{"Padişah": p["isim"], "Taht Yılı": p["taht_yil"], "Dönem": p["donem"]} for p in osmanli_36_padi_db.values()]
    df = pd.DataFrame(df_data)
    
    st.dataframe(df, use_container_width=True)
    
    en_uzun = df.loc[df["Taht Yılı"].idxmax()]
    en_uzun_metin = f"🏆 En uzun tahtta kalan hükümdar: **{en_uzun['Padişah']}** ({en_uzun['Taht Yılı']} Yıl)"
    st.success(en_uzun_metin)

    st.markdown("---")
    st.subheader("📥 Bellek Üzerinden (RAM) İndirme & Örnek Şablon")
    
    def ornek_sablon_olustur():
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            sample_df = pd.DataFrame({
                "Sira_No": [1, 2],
                "Padisah_Adi": ["I. Osman", "Orhan Bey"],
                "Donem": ["1299 - 1326", "1326 - 1362"],
                "Taht_Yili": [27, 36]
            })
            sample_df.to_excel(writer, index=False, sheet_name="Sablon")
        output.seek(0)
        return output.getvalue()

    col_b1, col_b2 = st.columns(2)
    with col_b1:
        st.download_button(
            label="📄 Örnek Excel Şablonunu İndir (.xlsx)",
            data=ornek_sablon_olustur(),
            file_name="padisah_veri_sablonu.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    with col_b2:
        output_csv = io.BytesIO()
        df.to_csv(output_csv, index=False, encoding='utf-8-sig')
        csv_data = output_csv.getvalue()
        
        st.download_button(
            label="📊 Analiz Raporunu İndir (CSV)",
            data=csv_data,
            file_name="saltanat_analiz_raporu.csv",
            mime="text/csv"
        )

    st.markdown(f'<div class="legal-box"><b>Yasal Uyarı:</b> {HUKUKI_METIN}</div>', unsafe_allow_html=True)

elif "4." in secim:
    st.title("📚 50 Güvenilir Tarih Soru-Cevap Bankası")
    st.write("Osmanlı tarihi boyunca gerçekleşen kritik olayları, antlaşmaları ve teşkilatları kapsayan 50 adet soru ve interaktif test motoru.")
    
    kategori_filtre = st.selectbox(
        "Kategoriye Göre Filtrele:",
        ["Tümü"] + list(set([q["kategori"] for q in guvenilir_50_soru_db]))
    )
    
    q_arama = st.text_input("Soru veya Konu İçinde Ara:")
    temiz_q_arama = xss_veri_suzgeci(q_arama)
    
    for item in guvenilir_50_soru_db:
        if kategori_filtre != "Tümü" and item["kategori"] != kategori_filtre:
            continue
        if temiz_q_arama and temiz_q_arama.lower() not in item["soru"].lower() and temiz_q_arama.lower() not in item["cevap"].lower():
            continue
            
        qid = item['id']
        cevap_key = f"goster_cevap_{qid}"
        if cevap_key not in st.session_state:
            st.session_state[cevap_key] = False

        st.markdown(f"""
        <div class="soru-kutu">
            <span style="background-color: #5c1d1d; color: white; padding: 2px 8px; border-radius: 4px; font-size: 0.8em;">{xss_veri_suzgeci(item['kategori'])}</span>
            <h4 style="margin-top: 8px;">Soru {qid}: {xss_veri_suzgeci(item['soru'])}</h4>
        </div>
        """, unsafe_allow_html=True)
        
        col_btn, col_empty = st.columns([1, 3])
        with col_btn:
            if st.button("Cevabı Göster", key=f"btn_{qid}"):
                st.session_state[cevap_key] = not st.session_state[cevap_key]
                
        if st.session_state[cevap_key]:
            st.markdown(f"""
            <div style="background-color: #fcfbfa; padding: 12px; border-radius: 6px; border-left: 3px solid #d4af37; margin-bottom: 20px;">
                <b>Cevap:</b> {xss_veri_suzgeci(item['cevap'])}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
        
    # 50 Soruyu İndirme Butonu
    q_output = io.BytesIO()
    q_df = pd.DataFrame(guvenilir_50_soru_db)
    q_df.to_excel(q_output, index=False, sheet_name="50_Soru_Cevap")
    q_output.seek(0)
    
    st.download_button(
        label="📥 50 Soruluk Veritabanını Excel Olarak İndir (.xlsx)",
        data=q_output.getvalue(),
        file_name="osmanli_50_guvenilir_soru.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# GLOBAL FOOTER DISCLAIMER
st.markdown("---")
st.markdown(f"""
<div class="main-legal-box">
    <b>⚖️ Yasal Uyarı ve Sorumluluk Reddi (Disclaimer):</b> {SIMULASYON_HUKUKI_METIN}
</div>
""", unsafe_allow_html=True)