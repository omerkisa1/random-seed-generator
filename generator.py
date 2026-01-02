import time
import math

class LaggedFibonacciRNG:
    def __init__(self, seed=None):
        self.j = 24
        self.k = 55  
        self.m = 2**64 

        if seed is None:
            seed = time.time_ns()
            
        self.state_buffer = []
        temp_state = seed
        
        for _ in range(self.k):
            temp_state = (6364136223846793005 * temp_state + 1442695040888963407) % self.m
            self.state_buffer.append(temp_state)
            
        self.index = 0

    def next(self):
        idx_j = (self.index - self.j) % self.k
        idx_k = (self.index - self.k) % self.k 
        
        new_val = (self.state_buffer[idx_j] + self.state_buffer[idx_k]) % self.m
        
        self.state_buffer[self.index] = new_val
        
        self.index = (self.index + 1) % self.k
        
        return new_val

    def next_bit(self):
        return self.next() % 2

def chi_square_test(bits):
    n = len(bits)
    ones = sum(bits)
    zeros = n - ones
    expected = n / 2
    chi2 = ((ones - expected) ** 2 / expected) + ((zeros - expected) ** 2 / expected)
    critical_value = 3.841
    p_value_approx = 1 - (chi2 / 10) if chi2 < 10 else 0.001
    return {
        "toplam_bit": n,
        "birler": ones,
        "sifirlar": zeros,
        "beklenen": expected,
        "chi_kare_degeri": round(chi2, 4),
        "kritik_deger": critical_value,
        "sonuc": "BASARILI" if chi2 < critical_value else "BASARISIZ"
    }

def runs_test(bits):
    n = len(bits)
    ones = sum(bits)
    zeros = n - ones
    
    if ones == 0 or zeros == 0:
        return {"sonuc": "BASARISIZ", "aciklama": "Tum bitler ayni"}
    
    runs = 1
    for i in range(1, n):
        if bits[i] != bits[i-1]:
            runs += 1
    
    pi = ones / n
    expected_runs = 2 * n * pi * (1 - pi) + 1
    variance = 2 * n * pi * (1 - pi) * (2 * n * pi * (1 - pi) - 1) / (n - 1)
    
    if variance <= 0:
        return {"sonuc": "BASARISIZ", "aciklama": "Varyans hesaplanamadi"}
    
    std_dev = math.sqrt(variance)
    z = (runs - expected_runs) / std_dev
    
    critical_z = 1.96
    
    return {
        "toplam_bit": n,
        "kosis_sayisi": runs,
        "beklenen_kosis": round(expected_runs, 2),
        "standart_sapma": round(std_dev, 2),
        "z_degeri": round(z, 4),
        "kritik_z": critical_z,
        "sonuc": "BASARILI" if abs(z) < critical_z else "BASARISIZ"
    }

def frequency_analysis(bits):
    n = len(bits)
    ones = sum(bits)
    zeros = n - ones
    ratio = ones / zeros if zeros > 0 else float('inf')
    
    return {
        "toplam_bit": n,
        "birler": ones,
        "sifirlar": zeros,
        "bir_yuzdesi": round(ones / n * 100, 2),
        "sifir_yuzdesi": round(zeros / n * 100, 2),
        "oran": round(ratio, 4),
        "ideal_oran": 1.0,
        "sapma": round(abs(ratio - 1.0) * 100, 2)
    }

if __name__ == "__main__":
    print("=" * 60)
    print("LAGGED FIBONACCI RASTGELE SAYI URETECI (LFG)")
    print("=" * 60)
    
    rng = LaggedFibonacciRNG(seed=42)
    
    print("\n[1] URETILEN ILK 10 SAYI:")
    print("-" * 40)
    for i in range(10):
        print(f"  {i+1:2}. Sayi: {rng.next()}")
    
    rng2 = LaggedFibonacciRNG(seed=42)
    sample_size = 10000
    bits = [rng2.next_bit() for _ in range(sample_size)]
    
    print(f"\n[2] FREKANS ANALIZI ({sample_size} bit):")
    print("-" * 40)
    freq = frequency_analysis(bits)
    print(f"  Toplam Bit     : {freq['toplam_bit']}")
    print(f"  1'ler          : {freq['birler']} (%{freq['bir_yuzdesi']})")
    print(f"  0'lar          : {freq['sifirlar']} (%{freq['sifir_yuzdesi']})")
    print(f"  Oran (1/0)     : {freq['oran']} (ideal: {freq['ideal_oran']})")
    print(f"  Sapma          : %{freq['sapma']}")
    
    print(f"\n[3] KI-KARE TESTI ({sample_size} bit):")
    print("-" * 40)
    chi = chi_square_test(bits)
    print(f"  1'ler          : {chi['birler']}")
    print(f"  0'lar          : {chi['sifirlar']}")
    print(f"  Beklenen       : {chi['beklenen']}")
    print(f"  Ki-Kare Degeri : {chi['chi_kare_degeri']}")
    print(f"  Kritik Deger   : {chi['kritik_deger']} (alpha=0.05)")
    print(f"  Sonuc          : {chi['sonuc']}")
    
    print(f"\n[4] RUNS (KOSIS) TESTI ({sample_size} bit):")
    print("-" * 40)
    runs = runs_test(bits)
    print(f"  Kosis Sayisi   : {runs['kosis_sayisi']}")
    print(f"  Beklenen Kosis : {runs['beklenen_kosis']}")
    print(f"  Standart Sapma : {runs['standart_sapma']}")
    print(f"  Z Degeri       : {runs['z_degeri']}")
    print(f"  Kritik Z       : +-{runs['kritik_z']} (alpha=0.05)")
    print(f"  Sonuc          : {runs['sonuc']}")
    
    print("\n" + "=" * 60)
    print("GENEL DEGERLENDIRME")
    print("=" * 60)
    
    all_passed = chi['sonuc'] == "BASARILI" and runs['sonuc'] == "BASARILI"
    if all_passed:
        print("  Algoritma tum istatistiksel testleri GECTI.")
        print("  Uretilen sayilar rastgelelik kriterlerini karsilamaktadir.")
    else:
        print("  Algoritma bazi testlerden gecemedi.")
    
    print("=" * 60)