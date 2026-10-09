import sqlite3
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


# Veritabanını ve notlar tablosunu oluşturan fonksiyon
def veritabani_olustur():
  baglanti = sqlite3.connect('veritabani.db')
  cursor = baglanti.cursor()

  # Notlar için yeni bir tablo oluşturuyoruz
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS notlar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            icerik TEXT NOT NULL
        )
    """)
  baglanti.commit()
  baglanti.close()


# Uygulama başlarken veritabanını hazırla
veritabani_olustur()


@app.route('/', methods=['GET', 'POST'])
def anasayfa():
  baglanti = sqlite3.connect('veritabani.db')
  cursor = baglanti.cursor()

  # Eğer kullanıcı yeni bir not gönderdiyse (Form doldurulduysa)
  if request.method == 'POST':
    yeni_not = request.form.get('not_icerigi')
    if yeni_not:  # Boş değilse kaydet
      cursor.execute(
          'INSERT INTO notlar (icerik) VALUES (?)', (yeni_not,)
      )
      baglanti.commit()
    baglanti.close()
    return redirect(url_for('anasayfa'))  # Sayfayı yenile

  # Veritabanındaki tüm notları çekiyoruz (En son eklenen en başta gelsin diye ORDER BY id DESC)
  cursor.execute('SELECT id, icerik FROM notlar ORDER BY id DESC')
  notlar = cursor.fetchall()  # Liste şeklinde gelir: [(1, 'not 1'), (2, 'not 2')]
  baglanti.close()

  # Notları HTML sayfasına gönderiyoruz
  return render_template('index.html', notlar=notlar)


import os
# ... (diğer kodların aynı kalıyor)


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)