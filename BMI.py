waga = float(input('Podaj Waga w kg: '))
wzrost = float(input('Podaj Wzrost w m:  '))

BMI = round(waga / (wzrost **2))

if BMI < 16:
    print('wygłodzenie')
elif BMI > 16 and  BMI < 16.99:
    print('wychudzenie')
elif BMI > 17 and BMI < 18.49:
    print('niedowaga')
elif BMI > 18.5 and BMI < 24.99:
    print('wartość prawidłowa')
elif BMI > 25 and BMI < 29.99:
    print('nadwaga')
elif BMI > 30 and BMI < 34.99:
    print('I stopień otyłości')
elif BMI > 35 and BMI < 35.99:
    print('II stopień otyłości')
else:
    print('otyłość skrajna')



