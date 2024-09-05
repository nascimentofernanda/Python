#Faça um programa que leia a temperatura e faça a conversão para outras temperaturas
temperatura=float(input('Digite a temperatura \n'))
escala_atual=input('Digite em qual escala a temperatura está \n')
if(escala_atual=="celsius"):
    kelvin=temperatura+273.15
    fahrenheit=(temperatura*1.8)+32
    print(f'A temperatura em Kelvin é: {kelvin:,.2f}')
    print(f'A temperatura em Fahrenheit é: {fahrenheit:,.2f}')
elif(escala_atual=="kelvin"):
    celsius=temperatura-273.15
    fahrenheit=((temperatura-273)*1.8)+32
    print(f'A temperatura em Celsius é: {celsius:,.2f}')
    print(f'A temperatura em Fahrenheit é: {fahrenheit:,.2f}')
else:
    celsius=(temperatura-32)/1.8
    kelvin=((temperatura-32)*(5/9))+273.15
    print(f'A temperatura em Celsius é: {celsius:,.2f}')
    print(f'A temperatura em Kelvin é: {kelvin:,.2f}')