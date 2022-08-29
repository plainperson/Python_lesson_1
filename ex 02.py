time = int(input('Введите количество секунд'))

hour = time // 3600
min = ((time - (hour*3600))//60)
sec = (time - ((hour*3600)+(min*60)))



print(f'{hour} часов, {min} минут, {sec} секунд')



