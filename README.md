
Hash Olimpiyatları; Hashcat yazılımını ve parola istatistiklerini en efektif şekilde kullanarak, gerçek veritabanlarından sızan hashleri kırmaya yönelik bir yarışmadır. Yarışmacılar bir donanım kullanarak hash kırmaz, fakat hashlerin kırılması için gerekli listeleri hazırlarlar. Dolayısıyla bu bir donanım kapasitesi ya da hız değil, bilgi ve analiz yeteneği yarışmasıdır. Detaylı bilgi için "Yarışma Süreci" bağlığını okuyabilirsiniz.

## Yarışma Süreci

1. Yarışma, bir moderatör (yayıncı) ve belirli sayıda kişi ya da grubun (yarışmacı) katılımıyla gerçekleşir
2. Moderatör, gerçek bir hack vakasından sızan bir veritabanı bulur. Buradaki kişisel verileri silerek parola hashlerini kaydeder. 
3. Sızıntının ya da veritabanının ismi yarışma gününden önce açıklanmaz. Fakat kullanıcıların dili ve varsa platformun parola kuralları (policy) açıklanır.
4. Moderatör, aşağıda yer alan elemanları kullanarak bir saldırı kombinasyonu belirler: (Bu kombinasyonlar her yarışmada farklı olacaktır)
    - Parola sayısı
    - Hashcat kural (rule) sayısı
    - Hashcat mask sayısı

    Örnek kombinasyonlar: 30 parola, 15 kural, 0 mask | 100 parola, 10 kural, 1 mask | 10 parola 50 kural 5 mask

5. Saldırı kombinasyonu yarışmadan en az 1 hafta önceden duyurulur.
6. Yarışmacıların amacı, moderatör tarafından belirlenen saldırı kombinasyonuna göre listeler hazırlayarak, hedef hash listesindeki en çok hash'in kırılmasını sağlamaktır. Yarışmacılar yarışma gününe kadar listelerini moderatör'e e-posta yoluyla iletmelidir. Örnek bir senaryo:
    - Moderatörün belirlediği saldırı kombinasyonu: 5 parola, 5 kural, 1 mask
    - Yarışmacının göndereceği örnek listeler:

        ```
        | Parola.txt | Kural.txt | Mask.txt |
        |------------|-----------|----------|
        | 123456     | :         | ?l?l?l?d |
        | 1234567    | l         |          |
        | qwerty     | u         |          |
        | 19231923   | c         |          |
        | besiktas   | ^X        |          |

        ```

7. Yarışma zamanı geldiğinde moderatör tarafından canlı yayın başlatılır
8. Moderatör tarafından canlı yayında veritabanına ve sızıntıya ait bilgiler paylaşılır
9. Moderatör, yarışmacılardan gelen atak kombinasyon listeleri ile Hashcat yazılımını kullanarak hedef hash listesine saldırı başlatır.
10. Başarılı bir şekilde kırılan hash sayıları not alınır.
11. Tüm saldırılar sonlandıktan sonra, en çok hash kırdırmayı başaran yarışmacılar ilan edilir. Örnek bir sonuç tablosu:

```
| Yarışmacı | Kırılan Hash Sayısı | Kırılan Hash Yüzdesi |
|-----------|---------------------|----------------------|
| Gözde     | 13,678              | %32.1                |
| Kerim     | 11,342              | %30.8                |
| Hikmet    | 9,543               | %27.5                |
```

Bu sonuç tablosuna göre Ayşe birinci, Kerim ikinci, Hikmet üçüncü olmuştur.

## Kurallar

- Eğer dereceye giren yarışmacılardan sonucu aynı olan varsa, listesini daha erken göndermiş olan bir basamak yükselir.
- Yarışmacılar, yarışma saatine kadar saldırı kombinasyon listelerini gizli tutmalıdır. Sosyal medyadan bunu paylaşanlar diskalifiye edilir.
- Yarışmacının başka bir yarışmacıyla liste paylaşması yasaktır. Eğer böyle bir paylaşım tespit edilirse yarışmacılar diskalifiye edilir.

## Yarışma Sonuçları

Henüz tamamlanmış bir yarışma bulunmamaktadır.

## Sıkça Sorulan Sorular

- Yarışmacılar canlı yayında nasıl hash kıracak?

Yarışmacılar hash kırmayacaktır. Hashler canlı yayında moderatör tarafından kırılacaktır. Yarışmacılar sadece hash kırma sürecinde gereken saldırı kombinasyon listelerini iletecektir.

- Katılmak için belirli bir donanıma sahip olmamız gerekir mi?

Hashler moderatör tarafından kırılacağı için yarışmacıların herhangi bir donanıma sahip olması gerekmez. 

- Yarışmaya grup olarak katılabillir miyiz?

Birey ve grup yarışmaları ayrı olarak yapılacaktır. Bireylerin katılacağı yarışmaya grup olarak katılamazsınız.

- Yarışmaya nasıl hazırlanabilirim?

Aşağıda yer alan faydalı kaynaklar kısmına göz atabilirsiniz.

- Yarışma duyurularını nereden takip edebilirim?

Yarışma duyurularını aşağıda paylaşılan Discord kanalımızdan ya da [https://twitter.com/utkusen](https://twitter.com/utkusen) Twitter hesabından takip edebilirsiniz

## Discord Kanalımız

[https://discord.gg/cygpVU6MAc](https://discord.gg/cygpVU6MAc)

## Yarışmaya Hazırlanmak İçin Faydalı Kaynaklar

Utku Şen'in "Hash Saldırıları" video serisi:

- [Yemeksepeti'nin SHA256 Tercihi ve Hashing Hakkında Konuşuyoruz | Hash Atakları 1. Bölüm](https://www.youtube.com/watch?v=oPS5v7OTjnw)
- [Hashcat Kullanımı ve Hash Kırma Saldırıları | Hash Atakları 2. Bölüm](https://www.youtube.com/watch?v=lCFIUd_Wnpg)
- [E-Ticaret Sitelerinden Sızan Hashleri Kırıyoruz | Hash Atakları 3. Bölüm](https://www.youtube.com/watch?v=WkT3xy0etd4)

[Crackstation Password Hashing Security](https://crackstation.net/hashing-security.htm)

[How To Perform A Rule-Based Attack Using Hashcat](https://www.4armed.com/blog/hashcat-rule-based-attack/)
