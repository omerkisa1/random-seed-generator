# Lagged Fibonacci Rastgele Sayı Üreteci (LFG-PRNG)

Sözde rastgele sayı üreteci (PRNG) algoritması implementasyonu.

## Algoritma Özellikleri

- **Tip**: Lagged Fibonacci Generator (LFG)
- **Parametreler**: j=24, k=55, m=2^64
- **Operasyon**: Toplama modüler aritmetik
- **Başlatma**: Linear Congruential Generator (LCG)

## Dosya Yapısı

```
random-seed-generator/
├── generator.py          # Ana algoritma ve istatistiksel testler
├── README.md             # Bu dosya
└── docs/
    ├── pseudocode.txt    # Sözde kod
    ├── diagram.txt       # Akış şeması
    └── explanation.md    # Algoritma açıklaması
```

## Kullanım

```bash
python generator.py
```

## İstatistiksel Testler

1. **Ki-Kare Testi**: 0-1 dağılımının eşitliğini kontrol eder
2. **Runs (Koşiş) Testi**: Bit dizisindeki ardışık grupların rastgeleliğini ölçer
3. **Frekans Analizi**: 0 ve 1 oranlarını hesaplar

## Çıktı Örneği

```
============================================================
LAGGED FIBONACCI RASTGELE SAYI URETECI (LFG)
============================================================

[1] URETILEN ILK 10 SAYI:
----------------------------------------
   1. Sayi: 9507839715877805897
   2. Sayi: 8968578190193078959
   ...

[2] FREKANS ANALIZI (10000 bit):
  1'ler          : ~5000 (%50)
  0'lar          : ~5000 (%50)

[3] KI-KARE TESTI:
  Sonuc          : BASARILI

[4] RUNS TESTI:
  Sonuc          : BASARILI
============================================================
```

## Algoritma Mantığı

LFG algoritması, iki önceki değerin toplamını kullanarak yeni sayılar üretir:

```
X(n) = (X(n-j) + X(n-k)) mod m
```

Bu yaklaşım basit LCG'ye göre daha uzun periyot ve daha iyi istatistiksel özellikler sağlar.
