def main():
    suma = 0
    for i in range(0,5):
        wyraz = input()
        if wyraz[0].isupper():
            suma = suma +1
    return suma

if __name__ == '__main__':
	print("kalkulator działa sobie tak")
	print("druga zmiana")
    print(main())