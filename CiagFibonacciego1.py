n = int(input("Podaj ktory wyraz ciagu chcesz zobaczyc(nieujemna liczba calkowita):"))

wyrazy_cf = {}
wyrazy_cf[0] = 0
wyrazy_cf[1] = 1

for i in range(2, n+1):
    wyrazy_cf[i] = (wyrazy_cf[i - 1] + wyrazy_cf[i - 2])

print(f"Wyrazem nr {n} ciagu Fibonacciego jest liczba {wyrazy_cf[n]}")


