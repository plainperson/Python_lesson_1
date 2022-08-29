prof = int(input('Введите сумму выручки'))
exp = int(input('Введите размер издержек'))


while True:
    if prof > exp:
        print('фирма работает с прибылью')
        gain = prof - exp
        print('прибыль составила', {gain},'долларов')
        r = gain / prof
        print('рентабельность фирмы составила', {r})
        n = int(input('Введите количество рабочих'))
        n = gain / n
        print('каждый сотрудник фирмы заработал', {n}, 'долларов')



        break


    else:
        print('фирма работает с убытком')




