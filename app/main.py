from app.calculator import Calculator
from app.validator import is_valid_number

def run():
    calc = Calculator()
    print("=== Simple Calculator ===")
    a = input("Angka pertama: ")
    b = input("Angka kedua: ")

    if not is_valid_number(a) or not is_valid_number(b):
        print("Input tidak valid")
        return

    a, b = float(a), float(b)
    print(f"Hasil penjumlahan: {calc.add(a, b)}")
    print(f"Hasil pengurangan: {calc.subtract(a, b)}")
    print(f"Hasil perkalian: {calc.multiply(a, b)}")

if __name__ == "__main__":
    run()