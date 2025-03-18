import datetime

try:
   
    n = int(input("Podaj ktory wyraz ciagu chcesz zobaczyc:"))
    if n < 0:
        print("Liczba musi byc nieujemna")
    else:
        wyrazy_cf = [0, 1]
       
        for i in range(2, n + 1):
            wyrazy_cf.append((wyrazy_cf[i - 1] + wyrazy_cf[i - 2]))
        
        data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        plik = f"Data obliczenia: {data} \nN = {n} \n{wyrazy_cf} \n"
        
        with open("fibonacci.txt", "a") as fib:
            print(plik, file=fib)
        
        print(f"Wyrazem nr {n} ciagu Fibonacciego jest liczba {wyrazy_cf[n]}")

except ValueError:
    print("Podaj liczbe calkowita")

