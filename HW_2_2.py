print('##### САМОРЕЗЫ #####')
x=1
while x==1:
    print('Привет! Я помогаю считать сколько саморезов нужно взвесить')
    screw_data = {(16,2):1, (16,3):1.6, (16,4):1.8, (16,5):2,
        (25,2):1.4, (25,3):2, (25,4):2.3, (25,5):2.5,
        (32,3):3.2, (32,4):3.5, (32,5):3.8,
        (35,4):3.8, (35,5):4,
        (40,5):5}
    screw_length = int(input('Введите длину самореза в мм - '))
    screw_diameter = int(input('Введите диаметр самореза в мм - '))
    screw_checking = float(screw_data.get((screw_length,screw_diameter),0))
    if screw_checking == 0:
        print('Извините, таких саморезов нет(((','\n\n')
    else:
        screw_amount = int(input('Сколько саморезов вам нужно? - '))
        screw_wight = screw_amount*float(screw_data.get((screw_length,screw_diameter),0))/1000
        print('Вам нужно взвесить', screw_wight,'кг саморезов','\n\n')