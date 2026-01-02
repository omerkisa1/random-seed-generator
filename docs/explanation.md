# Lagged Fibonacci Generator (LFG) - Algoritma Açıklaması

## 1. Giriş

Lagged Fibonacci Generator (LFG), sözde rastgele sayı üretimi için kullanılan bir algoritmadır. Fibonacci serisinden esinlenmiş olup, iki gecikmeli (lagged) değerin kombinasyonuyla yeni sayılar üretir.

## 2. Algoritmanın Çalışma Prensibi

### 2.1 Temel Formül

```
X(n) = (X(n-j) + X(n-k)) mod m
```

Parametreler:
- j = 24 (kısa gecikme)
- k = 55 (uzun gecikme, aynı zamanda tampon boyutu)
- m = 2^64 (modül değeri)

### 2.2 Başlatma (Initialization)

Algoritma başlamadan önce 55 elemanlık bir tampon (buffer) gereklidir. Bu tampon, Linear Congruential Generator (LCG) kullanılarak doldurulur:

```
temp = (a * temp + c) mod m
```

LCG sabitleri:
- a = 6364136223846793005
- c = 1442695040888963407

### 2.3 Sayı Üretme Adımları

1. İndeks j ve k konumlarını hesapla
2. Bu konumlardaki değerleri topla
3. Modül işlemi uygula
4. Yeni değeri tampona yaz
5. İndeksi ilerlet

## 3. Neden Bu Algoritma?

| Özellik | LCG | LFG |
|---------|-----|-----|
| Periyot | m | m^k (çok büyük) |
| Hız | Çok hızlı | Hızlı |
| Kalite | Orta | İyi |
| Bellek | O(1) | O(k) |

## 4. İstatistiksel Testler

### 4.1 Ki-Kare Testi

0 ve 1 sayılarının beklenen dağılıma uygunluğunu ölçer.

Formül:
```
χ² = Σ (Gözlenen - Beklenen)² / Beklenen
```

Kritik değer: 3.841 (α=0.05)
- χ² < 3.841 → BAŞARILI
- χ² >= 3.841 → BAŞARISIZ

### 4.2 Runs (Koşiş) Testi

Ardışık 0 ve 1 gruplarının rastgeleliğini test eder.

Örnek: 0011100101 → Koşişler: 00, 111, 00, 1, 0, 1 = 6 koşiş

Z değeri hesaplanır ve ±1.96 aralığında olmalıdır.

## 5. Avantajları ve Dezavantajları

Avantajları:
- Uzun periyot
- İyi istatistiksel özellikler
- Hızlı çalışma

Dezavantajları:
- Kriptografik olarak güvenli değil
- Başlangıç için ek bellek gerekli

## 6. Kullanım Alanları

- Monte Carlo simülasyonları
- Oyun geliştirme
- Bilimsel hesaplamalar
- İstatistiksel örnekleme

## 7. Sonuç

LFG algoritması, iyi bir denge sunan sözde rastgele sayı üreteci olup, güvenlik gerektirmeyen uygulamalar için uygundur.
