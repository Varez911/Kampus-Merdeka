import re

def inputNumber(num:str) -> list:
    number = [float(x) for x in re.split(r"[,\s]+", num) if x != ""]
    for i, bil in enumerate(number):
        if bil % 1 == 0:
            number[i] = int(bil)
    return number

def heap(bil:list, n:int, i:int):
    bilTerbesar = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and bil[bilTerbesar] < bil[l]:
        bilTerbesar = l
    if r < n and bil[bilTerbesar] < bil[r]:
        bilTerbesar = r

    if bilTerbesar != i:
        bil[i], bil[bilTerbesar] = bil[bilTerbesar], bil[i]
        heap(bil, n, bilTerbesar)

def sortAlgorithm(bil:list):
    n = len(bil)

    for i in range(n // 2 - 1, -1, -1):
        heap(bil, n, i)

    for i in range(n - 1, 0, -1):
        bil[i], bil[0] = bil[0], bil[i]
        heap(bil, i, 0)

def meanValue(bil:list) -> float:
    value = sum(bil) / len(bil)
    return round(value, 3)

def medianValue(bil:list) -> float:
    if len(bil) % 2 == 1:
        return bil[len(bil)//2]
    else:
        return (bil[len(bil)//2] + bil[len(bil)//2 - 1]) / 2

def productValue(bil:list) -> float:
    value = 1
    for b in bil:
        value *= b
    return round(value, 3)

if __name__ == '__main__':
    while True:
        print("=" * 35)
        arr = input("Masukan bilangan yang akan diolah: ")
        numList = inputNumber(arr)
        print(f"Bilangan yang anda input: \n{numList}")
        sortAlgorithm(numList)
        print(f"Bilangan yang telah diurutkan: \n{numList}")
        nilaiMean = meanValue(numList)
        print(f"Nilai rata-rata bilangan: {nilaiMean}")
        nilaiMedian = medianValue(numList)
        print(f"Nilai median bilangan: {nilaiMedian}")
        nilaiProduk = productValue(numList)
        print(f"Nilai produk dari bilangan: {nilaiProduk}")
        ans = input("Ingin Mengulang? (Y/N) \n>")
        print("-" * 35)
        if ans.lower() == 'n':
            break



