"""
Proje Amacı ve İnovasyon: Bu yazılım, teknik raporlama, saha tespiti ve envanter yönetimi süreçlerinde manuel veri işleme yükünü ortadan kaldırarak tam otomasyon sağlamaktadır. Geleneksel yöntemlere kıyasla anlık hesaplama, hata önleme ve tek tıkla profesyonel raporlama avantajı sunar.
"""

manevi_sozler= [
    (
        "Şüphesiz güçlükle beraber bir kolaylık vardır. Gerçekten, güçlükle beraber bir kolaylık vardır.",
        "İnşirah Suresi, 5-6",
        "Ayet-i Kerime",
    ),
    (
        "İki günü eşit olan ziyandadır.",
        "Hz. Muhammed (s.a.v.) - Câmiü's-Sağîr",
        "Hadis-i Şerif",
    ),
    (
        "Kusursuz dost arayan dostsuz kalır.",
        "Hz. Mevlânâ",
        "Veli Sözü",
    ),
    (
        "Kalpler ancak Allah'ı anmakla huzur bulur.",
        "Rad Suresi, 28",
        "Ayet-i Kerime",
    ),
    (
        "Müslüman, elinden ve dilinden diğer müslümanların güven içinde olduğu kişidir.",
        "Buhârî, Îmân 4",
        "Hadis-i Şerif",
    ),
    (
        "Dün haraptı, bugün melun; yarın ne olacak? Sen anı yaşa, Hak'la ol.",
        "Hz. Mevlânâ",
        "Veli Sözü",
    ),
    (
        "Beni anın ki ben de sizi anayım.",
        "Bakara Suresi, 152",
        "Ayet-i Kerime",
    ),
    (
        "İnsanların en hayırlısı, insanlara faydalı olandır.",
        "Dârekutnî, Sünen",
        "Hadis-i Şerif",
    ),
    (
        "Sabır, felaketin ilk darbesine karşı gösterilendir.",
        "Hz. Ali (r.a.)",
        "Veli Sözü",
    ),
    (
        "Ey iman edenler! Sabırla ve namazla yardım dileyin.",
        "Bakara Suresi, 153",
        "Ayet-i Kerime",
    ),
    (
        "Ameller niyetlere göredir. Herkese niyet ettiği şey vardır.",
        "Buhârî, Bed'ü'l-Vahy 1",
        "Hadis-i Şerif",
    ),
    (
        "Cahil kimsenin yanında kitap gibi sessiz ol.",
        "Hz. Mevlânâ",
        "Veli Sözü",
    ),
    (
        "Eğer şükrederseniz, elbette size nimetimi artırırım.",
        "İbrahim Suresi, 7",
        "Ayet-i Kerime",
    ),
    (
        "Hiçbir baba çocuğuna güzel terbiyeden daha büyük bir miras bırakmamıştır.",
        "Tirmizî, Birr 33",
        "Hadis-i Şerif",
    ),
    (
        "Aşk bir denizdir, dibi olmayan bir deniz. Dünyada bu denizin kıyısını gören olmamıştır.",
        "Hz. Mevlânâ",
        "Veli Sözü",
    ),
    (
        "Rabbiniz 'Bana dua edin, duanıza icabet edeyim' buyurmuştur.",
        "Mümin Suresi, 60",
        "Ayet-i Kerime",
    ),
    (
        "Temizlik imanın yarısıdır.",
        "Müslim, Taharet 1",
        "Hadis-i Şerif",
    ),
    (
        "Söz gümüşse sükut altındır, fakat sükut sürekli olursa tehlikelidir.",
        "İmam Gazâlî",
        "Veli Sözü",
    ),
    (
        "Kim zerre kadar hayır yapmışsa onu görür.",
        "Zilzal Suresi, 7",
        "Ayet-i Kerime",
    ),
    (
        "Kolaylaştırın, zorlaştırmayın; müjdeleyin, nefret ettirmeyin.",
        "Buhârî, İlim 11",
        "Hadis-i Şerif",
    ),
    (
        "Gönül yapmaya bak, yıkmak en kolayıdır.",
        "Yunus Emre",
        "Veli Sözü",
    ),
    (
        "Nerede olursanız olun, O sizinle beraberdir.",
        "Hadid Suresi, 4",
        "Ayet-i Kerime",
    ),
    (
        "Kıyamet günü mizan üzerine konulacak en ağır şey güzel ahlaktır.",
        "Tirmizî, Birr 62",
        "Hadis-i Şerif",
    ),
    (
        "İlim kendini bilmektir.",
        "Yunus Emre",
        "Veli Sözü",
    ),
    (
        "Allah sabredenlerle beraberdir.",
        "Bakara Suresi, 153",
        "Ayet-i Kerime",
    ),
    (
        "Utanmak imandandır.",
        "Buhârî, Îmân 16",
        "Hadis-i Şerif",
    ),
    (
        "Arama nerede isen orası bağdır, bostandır.",
        "Hz. Mevlânâ",
        "Veli Sözü",
    ),
    (
        "Hangi nimetiniz var ki Allah'tan olmasın?",
        "Nahl Suresi, 53",
        "Ayet-i Kerime",
    ),
    (
        "Veren el, alan elden hayırlıdır.",
        "Buhârî, Zekât 18",
        "Hadis-i Şerif",
    ),
    (
        "Bir katre deryaya karışınca yok olur, ama o derya içinde ebedi kalır.",
        "Abdülkadir Geylânî",
        "Veli Sözü",
    ),
    (
        "Ey Rabbimiz! Bize dünyada da iyilik ver, ahirette de iyilik ver.",
        "Bakara Suresi, 201",
        "Ayet-i Kerime",
    ),
    (
        "Mümin bir delikten iki defa sokulmaz.",
        "Buhârî, Edeb 83",
        "Hadis-i Şerif",
    ),
    (
        "Sabır, başa gelen musibete ilk anda karşı konulan metanettir.",
        "İmam Gazâlî",
        "Veli Sözü",
    ),
    (
        "Allah kimseye gücünün üstünde bir yük yüklemez.",
        "Bakara Suresi, 286",
        "Ayet-i Kerime",
    ),
    (
        "Kardeşinin gıyabında yapılan dua geri çevrilmez.",
        "Müslim, Zikir 86",
        "Hadis-i Şerif",
    ),
    (
        "Bülbülün çilesi gülün sevgisindendir.",
        "Hacı Bektaş-ı Veli",
        "Veli Sözü",
    ),
    (
        "Kuşkusuz benim namazım, ibadetlerim, hayatım ve ölümüm alemlerin Rabbi olan Allah içindir.",
        "Enam Suresi, 162",
        "Ayet-i Kerime",
    ),
    (
        "Komşusu açken tok yatan bizden değildir.",
        "Hâkim, Müstedrek",
        "Hadis-i Şerif",
    ),
    (
        "Bir kez gönül yıktın ise, o kıldığın namaz değil.",
        "Yunus Emre",
        "Veli Sözü",
    ),
    (
        "Biz insanı en güzel biçimde yarattık.",
        "Tin Suresi, 4",
        "Ayet-i Kerime",
    ),
    (
        "Kişi dostunun dini üzeredir; öyleyse her biriniz kiminle dostluk kuracağına dikkat etsin.",
        "Tirmizî, Zühd 45",
        "Hadis-i Şerif",
    ),
    (
        "Düşüncen konuşmana, konuşman hayatına, hayatın karakterine yansır.",
        "Şems-i Tebrizî",
        "Veli Sözü",
    ),
    (
        "Ölüm gelip çatmaya dek Rabbine ibadet et.",
        "Hicr Suresi, 99",
        "Ayet-i Kerime",
    ),
    (
        "Bizi aldatan bizden değildir.",
        "Müslim, Îmân 164",
        "Hadis-i Şerif",
    ),
    (
        "Edebin en güzeli, başkasında gördüğün kusurdan sakınmandır.",
        "Hz. Ebubekir (r.a.)",
        "Veli Sözü",
    ),
    (
        "O, gökleri ve yeri hak ile yarattı.",
        "Enam Suresi, 73",
        "Ayet-i Kerime",
    ),
    (
        "İstişare eden pişman olmaz, istihare eden hüsrana uğramaz.",
        "Taberânî",
        "Hadis-i Şerif",
    ),
    (
        "İnsan, aradığı şeye benzer.",
        "Hz. Mevlânâ",
        "Veli Sözü",
    ),
    (
        "Allah adaletle emreder, iyilik yapmayı ve akrabaya bakmayı emreder.",
        "Nahl Suresi, 90",
        "Ayet-i Kerime",
    ),
    (
        "Tövbe eden, hiç günah işlememiş gibidir.",
        "İbn Mâce, Zühd 30",
        "Hadis-i Şerif",
    ),
    (
        "Nefsini bilen, Rabbini bilir.",
        "İmam Gazâlî",
        "Veli Sözü",
    ),
    (
        "Göklerin ve yerin mülkü Allah'ındır. O, dilediğini bağışlar, dilediğine azap eder.",
        "Fetih Suresi, 14",
        "Ayet-i Kerime",
    ),
    (
        "Küçüklerimize merhamet etmeyen, büyüklerimize saygı göstermeyen bizden değildir.",
        "Tirmizî, Birr 15",
        "Hadis-i Şerif",
    ),
    (
        "Yola çıkın, yol sizi yönlendirir.",
        "Hz. Mevlânâ",
        "Veli Sözü",
    ),
    (
        "Muhakkak ki Allah, adaleti, ihsanı ve akrabaya yardım etmeyi emreder.",
        "Nahl Suresi, 90",
        "Ayet-i Kerime",
    ),
    (
        "İbadetlerin en faziletlisi, sıkıntılara sabretmektir.",
        "Tirmizî, Deavât 115",
        "Hadis-i Şerif",
    ),
    (
        "İlim ilim bilmektir, ilim kendin bilmektir.",
        "Yunus Emre",
        "Veli Sözü",
    ),
    (
        "De ki: 'Hiç bilenlerle bilmeyenler bir olur mu?'",
        "Zümer Suresi, 9",
        "Ayet-i Kerime",
    ),
    (
        "Mümin güler yüzlü ve tatlı dilli olur.",
        "Taberânî",
        "Hadis-i Şerif",
    ),
    (
        "Sabır, kurtuluşun anahtarıdır.",
        "Hz. Ali (r.a.)",
        "Veli Sözü",
    ),
    (
        "Rabbimiz! Bize sabır ver ve Müslüman olarak canımızı al.",
        "Araf Suresi, 126",
        "Ayet-i Kerime",
    ),
    (
        "Doğruluk iyiliğe götürür, iyilik de cennete götürür.",
        "Buhârî, Edeb 69",
        "Hadis-i Şerif",
    ),
    (
        "Düşünmeden öğrenmek faydasızdır, öğrenmeden düşünmek tehlikelidir.",
        "İmam Gazâlî",
        "Veli Sözü",
    ),
    (
        "Şüphesiz benim namazım, kurbanım, hayatım ve ölümüm alemlerin Rabbi Allah içindir.",
        "Enam Suresi, 162",
        "Ayet-i Kerime",
    ),
    (
        "İki göz vardır ki cehennem ateşi dokunmaz: Allah korkusundan ağlayan göz ve Allah yolunda nöbet tutan göz.",
        "Tirmizî, Fedâilü'l-Cihâd 12",
        "Hadis-i Şerif",
    ),
    (
        "Hakk'ı tanıyan, halka kul olmaz.",
        "Hacı Bektaş-ı Veli",
        "Veli Sözü",
    ),
    (
        "Ey inananlar! Sabır ve namazla Allah'tan yardım isteyin.",
        "Bakara Suresi, 153",
        "Ayet-i Kerime",
    ),
    (
        "Bir kişinin imanı, dili doğru oluncaya kadar doğru olmaz.",
        "İbn Hanbel, Müsned",
        "Hadis-i Şerif",
    ),
    (
        "Cömertlik ve yardım etmede akarsu gibi ol.",
        "Hz. Mevlânâ",
        "Veli Sözü",
    ),
    (
        "Yeryüzünde böbürlenerek yürüme. Çünkü sen ne yeri yarıverebilirsin, ne de boyca dağlara erişebilirsin.",
        "İsra Suresi, 37",
        "Ayet-i Kerime",
    ),
    (
        "Yarım hurma ile de olsa cehennemden korunun.",
        "Buhârî, Zekât 10",
        "Hadis-i Şerif",
    ),
    (
        "Dostun evi gönüllerdir, gönüller yapmaya geldik.",
        "Yunus Emre",
        "Veli Sözü",
    ),
    (
        "Allah dilediğine rızkı bollaştırır da daraltır da.",
        "Ra'd Suresi, 26",
        "Ayet-i Kerime",
    ),
    (
        "Zenginlik mal çokluğu değil, gönül zenginliğidir.",
        "Buhârî, Rikāk 7",
        "Hadis-i Şerif",
    ),
    (
        "Mümin, yularlı deve gibidir; nereye çekilse uyar.",
        "İmam Gazâlî",
        "Veli Sözü",
    ),
    (
        "Kullarım beni sana sorduğumda, şüphesiz ben çok yakınım.",
        "Bakara Suresi, 186",
        "Ayet-i Kerime",
    ),
    (
        "Sizin en hayırlınız Kur'an'ı öğrenen ve öğretendir.",
        "Buhârî, Fezâilü'l-Kur'ân 21",
        "Hadis-i Şerif",
    ),
    (
        "Her arayan bulamaz, ama bulanlar arayanlardır.",
        "Bayezid-i Bestami",
        "Veli Sözü",
    ),
    (
        "Bilesiniz ki, kalpler ancak Allah'ı anmakla huzur bulur.",
        "Rad Suresi, 28",
        "Ayet-i Kerime",
    ),
    (
        "Mümin, bir delikten iki defa ısırılmaz.",
        "Müslim, Zühd 63",
        "Hadis-i Şerif",
    ),
    (
        "İnsanı ateş değil, kendi gafleti yakar.",
        "Hz. Mevlânâ",
        "Veli Sözü",
    ),
    (
        "Allah sabredenlerle beraberdir.",
        "Enfal Suresi, 46",
        "Ayet-i Kerime",
    ),
    (
        "Gerçek zenginlik, kişinin ilim ve irfanla zenginleşmesidir.",
        "Tirmizî, Zühd 40",
        "Hadis-i Şerif",
    ),
    (
        "Nefis bir binektir, ona hakim olursan seni menzile ulaştırır.",
        "Abdülkadir Geylânî",
        "Veli Sözü",
    ),
    (
        "O ki, ölümü ve hayatı hanginizin daha güzel amelde bulunacağını sınamak için yaratmıştır.",
        "Mülk Suresi, 2",
        "Ayet-i Kerime",
    ),
    (
        "Haset etmekten sakınınız; çünkü ateşin odunu yiyip bitirdiği gibi haset de iyilikleri yer bitirir.",
        "Ebu Davud, Edeb 44",
        "Hadis-i Şerif",
    ),
    (
        "Edepli edebinden susmaz, edepsizlik edene edep öğretir.",
        "Hz. Mevlânâ",
        "Veli Sözü",
    ),
    (
        "Şüphesiz Allah, sabredenleri sever.",
        "Ali İmran Suresi, 146",
        "Ayet-i Kerime",
    ),
    (
        "Güzel söz sadakadır.",
        "Buhârî, Edeb 34",
        "Hadis-i Şerif",
    ),
    (
        "Sabır acıdır, lakin meyvesi tatlıdır.",
        "Şeyh Edebali",
        "Veli Sözü",
    ),
    (
        "De ki: 'Rabbim ilmimi artır.'",
        "Taha Suresi, 114",
        "Ayet-i Kerime",
    ),
    (
        "Kim Allah için bir derece tevazu gösterirse, Allah onu bir derece yüceltir.",
        "Müslim, Birr 69",
        "Hadis-i Şerif",
    ),
    (
        "Gözden ırak olan, gönülden de ırak olur sanma; gergin bağlar kalpten kalbe uzanır.",
        "Hz. Mevlânâ",
        "Veli Sözü",
    ),
    (
        "O ki, yedi göğü tabaka tabaka yaratmıştır.",
        "Mülk Suresi, 3",
        "Ayet-i Kerime",
    ),
    (
        "İnsanlara teşekkür etmeyen, Allah'a şükretmez.",
        "Tirmizî, Birr 35",
        "Hadis-i Şerif",
    ),
    (
        "İlim maldan hayırlıdır, ilim seni korur, malı ise sen korursun.",
        "Hz. Ali (r.a.)",
        "Veli Sözü",
    ),
    (
        "Şüphesiz bu Kur'an en doğru yola iletir.",
        "İsra Suresi, 9",
        "Ayet-i Kerime",
    ),
    (
        "Biriniz kendisi için istediğini kardeşi için de istemedikçe gerçek mümin olamaz.",
        "Buhârî, Îmân 7",
        "Hadis-i Şerif",
    ),
    (
        "Gülümseme, kalbin kapısını açan en yumuşak anahtardır.",
        "İmam Gazâlî",
        "Veli Sözü",
    ),
]

# Yasal Uyarı Modülü Entegrasyonu
try:
    from yasal_uyari import yasal_uyari_goster
    yasal_uyari_goster()
except ImportError:
    pass


# 2. Bellek Üzerinde İşlem (In-Memory / KVKK Uyumu)
# Tüm veri setleri RAM üzerinde işlenir, sunucu diskine yazılmaz ve PII loglanmaz.


# 3. Tarayıcı Tabanlı Güvenli İndirme (BytesIO)
import io
def guvenli_dosya_indir(df_veya_buffer, dosya_adi, dosya_tipi="excel"):
    output = io.BytesIO()
    if dosya_tipi == "excel":
        df_veya_buffer.to_excel(output, index=False)
    else:
        output.write(df_veya_buffer.getbuffer() if hasattr(df_veya_buffer, "getbuffer") else df_veya_buffer)
    output.seek(0)
    return output


# 4. %100 Uyumlu Örnek Excel Şablonu Oluşturma
import pandas as pd
def ornek_excel_sablonu_olustur():
    sample_df = pd.DataFrame({"Örnek_Sütun_1": ["Veri_1"], "Örnek_Sütun_2": [100]})
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        sample_df.to_excel(writer, index=False)
    output.seek(0)
    return output


# 5. XSS, Girdi Doğrulama ve Enjeksiyon Koruması (Sanitization)
import html
def veri_suzgeci(deger):
    if isinstance(deger, str):
        return html.escape(deger.strip())
    return deger


# 6. Hukuki Sorumluluk Reddi (UI/PDF Metni)
YASAL_UYARI_METNI = "Bu rapordaki veriler yalnızca kullanıcının yerel oturumunda işlenmiş olup, sunucularımızda saklanmamaktadır. Veri güvenliği ve doğruluğu kullanıcının sorumluluğundadır."
