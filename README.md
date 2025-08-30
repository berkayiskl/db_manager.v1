# Discord Football Bot

Bu Discord botu, futbol verilerini sunmak için tasarlanmıştır. (Not: Futbol burada sadece bir örnektir, kullanıcılar kendi verilerini ekleyerek değiştirebilir.)  
Bot, FIFA sıralamaları, maç sonuçları ve Dünya Kupası kazananları gibi bilgileri gösterebilir ve SQLite veritabanı kullanır.

---

## Özellikler

- **!ping** → Botun çalışıp çalışmadığını test eder.  
- **!hello** → Kullanıcıyı adıyla selamlar.  
- **!echo [mesaj]** → Kullanıcının gönderdiği mesajı tekrarlar.  
- **!worldcup** → Dünya Kupası yılları ve kazanan takımlarını listeler.  
- **!rank** → FIFA sıralamalarını gösterir.  
- **!matches** → Maç sonuçlarını listeler.  
- **Üye katıldığında otomatik karşılama** → "ortak" kanalında hoş geldin mesajı gönderir.  

---

## Gereksinimler

- Python 3.10 - 3.12  
- `discord.py` kütüphanesi  
- SQLite (`football.db` veritabanı)

### Kütüphaneleri yüklemek için:
```bash
pip install discord.py
