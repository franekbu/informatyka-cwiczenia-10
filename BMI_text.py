def oblicz_bmi(waga, wzrost):
    """Oblicza BMI na podstawie jednostek"""
    bmi = waga / pow(wzrost,2)
    return bmi

def main(nazwa_pliku):
    """Pobiera dane"""
    with open(nazwa_pliku, "r") as plik:
        file_data = plik.readlines()
    lista_dane = []

    for line in file_data[1:]:
        print(line)
        waga_s, wzrost_s = line.split(";")
        waga, wzrost = int(waga_s), int(wzrost_s)
        print(waga, wzrost)
        bmi = oblicz_bmi(waga, wzrost/100)
        print(bmi)
        lista_dane.append((waga, wzrost, bmi))

    with open("wynik_bmi.txt", 'a', encoding='utf-8') as plik:
        if plik.tell() == 0:  # sprawdza czy plik jest pusty, jesli tak - dopisuje naglowek
            plik.write("waga[kg];wzrost[cm];bmi\n")
        for data in lista_dane:
            #print(f"{data[0]:.2f};{data[1]:.2f};{data[2]:.2f}\n")
            plik.write(f"{data[0]:.2f};{data[1]:.2f};{data[2]:.2f}\n")

main("data.txt")
