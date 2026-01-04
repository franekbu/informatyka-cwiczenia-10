import os


def czytaj_float(prompt, dodatnia=False):
    while True:
        s = input(prompt).strip().replace(',', '.')
        try:
            liczba = float(s)
            if dodatnia and liczba <= 0:
                print("Podaj liczbę większą od zera.")
                continue
            return liczba
        except ValueError:
            print("Podaj liczbę.")


def czytaj_int(prompt, dodatnia=False):
    """Czyta liczbę całkowitą z wejścia."""
    while True:
        try:
            liczba = int(input(prompt).strip())
            if dodatnia and liczba <= 0:
                print("Podaj liczbę większą od zera.")
                continue
            return liczba
        except ValueError:
            print("Podaj liczbę całkowitą.")


def oblicz_bmi(waga, wzrost):
    """Oblicza BMI na podstawie jednostek"""
    bmi = waga / pow(wzrost,2)
    return bmi

def funt_na_kg(funty):
    return funty * 0.45359237

def cale_na_cm(cale):
    return cale * 2.54

def interpretacja_bmi(bmi):
    """Interpretuje wynik BMI"""
    if bmi < 18.5:
        return "niedożywienie"
    elif bmi < 25:
        return "normalna masa ciała"
    elif bmi < 30:
        return "nadwaga"
    elif bmi < 35:
        return "otyłość 1 stopnia"
    elif bmi < 40:
        return "otyłość 2 stopnia"
    else:
        return "otyłość 3 stopnia"


# Główna część programu
print("=== KALULATOR BMI ===")
print("Jednostki: m (metryczne: kg, m) lub i (imperialne: funty, stopy/cale)")

# Liczba obserwacji
n = int(input("Ile obserwacji chcesz wpisać? "))


with open("wynik_bmi.txt", 'a', encoding='utf-8') as plik:
    if plik.tell() == 0: #sprawdza czy plik jest pusty, jesli tak - dopisuje naglowek
        plik.write("waga[kg];wzrost[cm];bmi\n")


    for i in range(1, n + 1):
        print(f"\n--- Obserwacja {i}/{n} ---")

        # Wybór jednostek
        while True:
            jednostki = input("Wybierz jednostki metryczne [m] lub imperialne [i]: ").strip()
            if jednostki.lower() in ['m', 'i']:
                break
            print("Podaj: m (metryczne) lub i (imperialne)!")

        # Wczytanie danych
        if jednostki.lower() == 'm':
            waga = czytaj_float("Waga (kg): ", dodatnia=True)
            wzrost_cm = czytaj_float("Wzrost (cm): ", dodatnia=True)
            wzrost = wzrost_cm / 100.0  # konwersja na metry

        else:
            waga_i = czytaj_float("Waga (funty): ", dodatnia=True)
            stopy = czytaj_int("Wzrost - stopy: ", dodatnia=True)
            cale = czytaj_int("Wzrost - cale: ", dodatnia=False)
            wzrost_i = (stopy * 12) + cale  # konwersja na całkowite cale

            waga = funt_na_kg(waga_i)
            wzrost = cale_na_cm(wzrost_i) / 100

        # Obliczenie BMI
        bmi = oblicz_bmi(waga, wzrost)
        interpretacja = interpretacja_bmi(bmi)

        # Wyświetlenie wyniku
        print(f"BMI: {bmi:.2f} - {interpretacja}")


        plik.write(f"{waga:.2f};{wzrost:.2f};{bmi:.2f}\n") #zapis do pliku

print(f"\nWyniki zapisano do pliku: wyniki_bmi.txt")
