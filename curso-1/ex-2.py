num = int(input("digite um número: "))

if (num%2==0):
    print(f"{num} é par")
else:
    print(f"{num} é impar")

idade = int(input("Qual sua idade: "))

if (idade<=12):
    print("Você é criança")
elif (idade > 13) & (idade < 18):
    print("você é adolecente")
elif (idade > 18):
    print("você é adulto")
    
