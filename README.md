# 🔔 Smart Notification System (Python OOP)

Bu proje, Python'da **Nesne Yönelimli Programlama (OOP)** konseptlerini ve **modüler kod yazımını** uygulamalı olarak gösteren bir bildirim yönetim sistemidir. Sistem, farklı iletişim kanallarını tek bir yapı üzerinden yönetmeyi sağlar.

---

## 🚀 Proje Özellikleri

* **Polymorphism (Çok Biçimlilik):** Tüm bildirim türleri (Email, SMS, Push) aynı `send()` metodunu kullanır ancak her biri kendine özgü çıktı üretir.
* **Inheritance (Kalıtım):** Tüm sınıflar ana `Notification` sınıfından türetilerek kod tekrarı önlenmiştir.
* **Modüler Yapı:** Mantıksal işlemler (`utils.py`), sınıf tanımlamaları (`notification.py`) ve ana uygulama (`main.ipynb`) birbirinden ayrılarak düzenli bir yapı oluşturulmuştur.
* **Dinamik İçerik:** `random` kütüphanesi kullanılarak her bildirimde farklı bir mesaj gönderimi simüle edilir.

---

## 📂 Dosya Yapısı

| Dosya | Görevi |
| :--- | :--- |
| `notification.py` | Bildirim sınıflarının (Email, Sms, Push) ve temel sınıfın bulunduğu modül. |
| `utils.py` | Mesaj havuzundan rastgele seçim yapan yardımcı fonksiyon. |
| `main.ipynb` | Projenin çalışma alanı, nesnelerin oluşturulduğu ve test edildiği ana dosya. |

---

## 🛠️ Teknik Detaylar

### Kullanılan Teknolojiler
* **Python 3.x**
* **Jupyter Notebook**
* **DateTime & Random** (Standart Kütüphaneler)

### Örnek Çıktı
Program çalıştırıldığında aşağıdaki gibi bir akış sağlar:
```text
email gönderildi: Yeni bildiriminiz var
Yeni bildiriminiz var - 2026-04-06 23:10:15
--------------------
sms gönderildi: Güvenlik uyarısı!
Güvenlik uyarısı! - 2026-04-06 23:10:15
--------------------
push bildirimi gönderildi : Mesaja bakınız
Mesaja bakınız - 2026-04-06 23:10:15
