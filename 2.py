a = int(input('Первый катет: '))
b = int(input('Второй катет: '))
гипотенуза = (a ** 2 + b ** 2) ** 0.5
периметр = a + b + гипотенуза
площадь = (a * b)/2
print ("Периметр="+ str(периметр))
print("Площадь=" + str(площадь))