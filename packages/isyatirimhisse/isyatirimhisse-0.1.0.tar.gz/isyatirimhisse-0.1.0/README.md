# isyatirimhisse v0.1.0

## Aciklama

`isyatirimhisse`, Is Yatirim'in web sitesinden veri cekme islemlerini kolaylastirmak amaciyla gelistirilmis, istege gore ozellestirilebilir bir Python kutuphanesidir.

*** UYARI ***

`isyatirimhisse`, resmi Is Yatirim Menkul Degerler A.S. kutuphanesi degildir ve sirket tarafindan dogrulanmamistir. Kullanicilar, bu kutuphaneyi kullanmadan once ilgili tum verilere erisim icin Is Yatirim Menkul Degerler A.S. kullanim kosullarini ve haklarini incelemelidir. `isyatirimhisse` kutuphanesi, yalnizca kisisel kullanim amaclari icin tasarlanmistir.

## Kurulum

Kutuphaneyi kullanmak icin asagidaki adimlari izleyin:

1. Python'i sisteminize yukleyin: https://www.python.org/downloads/
2. Terminali acin ve paketi yuklemek icin asagidaki komutu calistirin:

```bash
pip install isyatirimhisse
```

## Kullanim

### Kutuphanenin Iceri Aktarilmasi

```python
from isyatirimhisse import veri_cek
```

### Veri Cekme Ornekleri

```python
# Tek hisse, gunluk frekans ve logaritmik getiri
sembol = 'AKBNK'
baslangic_tarih = '03-01-2023'
bitis_tarih = '21-07-2023'
frekans = '1g'
gozlem = 'son'
getiri_hesapla = True
logaritmik_getiri = True
na_kaldir = True

veriler = veri_cek(
    sembol=sembol,
    baslangic_tarih=baslangic_tarih,
    bitis_tarih=bitis_tarih,
    frekans=frekans,
    gozlem=gozlem,
    getiri_hesapla=getiri_hesapla,
    logaritmik_getiri=logaritmik_getiri,
    na_kaldir=na_kaldir
)

print(veriler)
```

```python
# Bitis tarihi yok
sembol = 'AKBNK'
baslangic_tarih = '03-01-2023'
frekans = '1g'
gozlem = 'son'
getiri_hesapla = True
logaritmik_getiri = True
na_kaldir = True

veriler = veri_cek(
    sembol=sembol,
    baslangic_tarih=baslangic_tarih,
    frekans=frekans,
    gozlem=gozlem,
    getiri_hesapla=getiri_hesapla,
    logaritmik_getiri=logaritmik_getiri,
    na_kaldir=na_kaldir
)

print(veriler)
```

```python
# Birden fazla hisse, haftalik frekans, basit getiri ve NA kaldir
sembol = ['AKBNK','EUPWR']
baslangic_tarih = '03-01-2023'
bitis_tarih = '21-07-2023'
frekans = '1h'
gozlem = 'son'
getiri_hesapla = True
logaritmik_getiri = False
na_kaldir = True

veriler = veri_cek(
    sembol=sembol,
    baslangic_tarih=baslangic_tarih,
    bitis_tarih=bitis_tarih,
    frekans=frekans,
    gozlem=gozlem,
    getiri_hesapla=getiri_hesapla,
    logaritmik_getiri=logaritmik_getiri,
    na_kaldir=na_kaldir
)

print(veriler)
```

```python
# Birden fazla hisse, aylik frekans, kapanis fiyati ve NA birak
sembol = ['AKBNK','EUPWR']
baslangic_tarih = '03-01-2023'
bitis_tarih = '21-07-2023'
frekans = '1a'
gozlem = 'son'
getiri_hesapla = False
logaritmik_getiri = True
na_kaldir = False

veriler = veri_cek(
    sembol=sembol,
    baslangic_tarih=baslangic_tarih,
    bitis_tarih=bitis_tarih,
    frekans=frekans,
    gozlem=gozlem,
    getiri_hesapla=getiri_hesapla,
    logaritmik_getiri=logaritmik_getiri,
    na_kaldir=na_kaldir
)

print(veriler)
```

```python
# Birden fazla hisse, yillik frekans, kapanis fiyati, ortalama fiyatlar ve NA kaldir
sembol = ['AKBNK','EUPWR']
baslangic_tarih = '03-01-2023'
bitis_tarih = '21-07-2023'
frekans = '1y'
gozlem = 'ortalama'
getiri_hesapla = False
logaritmik_getiri = True
na_kaldir = True

veriler = veri_cek(
    sembol=sembol,
    baslangic_tarih=baslangic_tarih,
    bitis_tarih=bitis_tarih,
    frekans=frekans,
    gozlem=gozlem,
    getiri_hesapla=getiri_hesapla,
    logaritmik_getiri=logaritmik_getiri,
    na_kaldir=na_kaldir
)

print(veriler)
```

### Fonksiyon Parametreleri

* `sembol` (str veya list, varsayilan None): Hisse senedi sembolu veya sembollerinin listesi (Orn. 'AKBNK' veya ['AKBNK','EUPWR'])
* `baslangic_tarih` (str, 'GG-AA-YYYY', varsayilan None): Verilerin baslangic tarihi (Orn. '03-01-2023').
* `bitis_tarih` (str, 'GG-AA-YYYY', varsayilan None): Verilerin bitis tarihi (Orn. '21-07-2023'). Eger belirtilmezse, sistem tarihini (bugunku tarihi) otomatik olarak kullanir.
* `frekans` (str, varsayilan '1g'): Veri frekansi (Gunluk: '1g', Haftalik: '1h', Aylik: '1a', Yillik: '1y').
* `gozlem` (str, varsayilan 'son'): Haftalik, aylik ve yillik frekanslarda istenen gozlem ('son': Son, 'ortalama': Ortalama)
* `getiri_hesapla` (bool, varsayilan True): Getiri hesaplanacak mi?
* `logaritmik_getiri` (bool, varsayilan True): Logaritmik getiri mi hesaplanacak?
* `na_kaldir` (bool, varsayilan True): Eksik degerler kaldirilacak mi?

### Donen Deger

`veri_cek` fonksiyonu bir pandas DataFrame dondurur.

## Notlar

* Kutuphane, Is Yatirim'in web sitesindeki verilere bagimlidir. Bu nedenle, verilerin dogrulugu ve surekliligi icin lutfen ilgili web sitesini kontrol edin: [Is Yatirim](https://www.isyatirim.com.tr/tr-tr/Sayfalar/default.aspx)
* Kutuphanenin gelistirilmesi ve iyilestirilmesi icin geri bildirimlerinizi bekliyorum. GitHub reposuna katkida bulunun: [GitHub Repo](https://github.com/urazakgul/isyatirimhisse)
* Herhangi bir sorun veya oneride lutfen GitHub reposundaki "Issue" bolumunden yeni bir konu acarak bildirim saglayin: [GitHub Issues](https://github.com/urazakgul/isyatirimhisse/issues)

## Degisiklikler

### v0.1.0 - 25/07/2023

* Ilk surum yayinlandi.

## Lisans

Bu proje MIT Lisansi altinda lisanslanmistir.