[TR--Türkçe]
ARCHMAN LINUX FONT YÜKLEYİCİ
Sürüm: 1.0
Tarih: 22.01.2025
Yazar: PeGaSuS için özelleştirilmiş script

AÇIKLAMA
---------
Bu script, Archman Linux sistemine kapsamlı bir font koleksiyonu yüklemek için tasarlanmıştır. 
Temel fontlardan özel kullanım fontlarına kadar geniş bir yelpazede font paketi içerir.

GEREKSİNİMLER
-------------
- Python 3.x
- Root yetkisi
- İnternet bağlantısı

KURULUM
--------
1. Dosyayı font_installer.py olarak kaydedin
2. Terminal'de şu komutu çalıştırın:
   sudo python font_installer.py

İÇERDİĞİ FONT PAKETLERİ
-----------------------
1. Temel Fontlar:
   - DejaVu
   - Liberation
   - Noto Fonts (CJK, Emoji dahil)

2. Programlama Fontları:
   - Fira Code
   - JetBrains Mono
   - Cascadia Code

3. Asya Fontları:
   - Baekmuk
   - WQY MicroHei
   - WQY ZenHei

4. Ek Fontlar:
   - Adobe Source
   - Google Fonts
   - Microsoft Uyumlu Fontlar

NOT
---
- Kurulum sırasında sistem otomatik olarak güncellenecektir
- AUR paketleri için yay otomatik olarak yüklenecektir
- Kurulum sonrası sistemi yeniden başlatmanız önerilir

SORUN GİDERME
-------------
Eğer pacman kilitlenme hatası alırsanız:
sudo rm /var/lib/pacman/db.lck
komutunu çalıştırıp tekrar deneyin.

İLETİŞİM
--------
Sorun veya önerileriniz için GitHub üzerinden issue açabilirsiniz.

[En--English]
ARCHMAN LINUX FONT LOADER
Version: 1.0
Date: 22.01.2025
Author: Custom script for PeGaSuS

DESCRIPTION
---------
This script is designed to install a comprehensive font collection on an Archman Linux system.

It includes a wide range of font packages, from basic fonts to special use fonts.

REQUIREMENTS
-------------
- Python 3.x
- Root permissions
- Internet connection

INSTALLATION
--------
1. Save the file as font_installer.py
2. Run the following command in Terminal:
sudo python font_installer.py

INCLUDED FONT PACKAGES
-----------------------
1. Base Fonts:
- DejaVu
- Liberation
- Noto Fonts (including CJK, Emoji)

2. Programming Fonts:
- Fira Code
- JetBrains Mono
- Cascadia Code

3. Asian Fonts:
- Baekmuk
- WQY MicroHei
- WQY ZenHei

4. Additional Fonts:
- Adobe Source
- Google Fonts
- Microsoft Compatible Fonts

NOTE
---
- The system will be updated automatically during the installation
- Spring will be installed automatically for AUR packages
- You need to restart the system after the installation recommended

TROUBLESHOOTING
-------------
If you get a pacman crash error:
run the command sudo rm /var/lib/pacman/db.lck
and try again.

CONTACT
--------
You can open an issue on GitHub for your problems or suggestions. 
