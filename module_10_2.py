from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        from time import sleep
        enemies = 100
        days_of_battle = 0
        print(f'{self.name} на нас напали!')
        while enemies != 0:
            enemies -= self.power
            days_of_battle += 1
            if enemies <= 0:
                enemies -= enemies
                print(f'{self.name} сражается {days_of_battle} день(дня)..., осталось {enemies} воинов')
                break
            print(f'{self.name} сражается {days_of_battle} день(дня)..., осталось {enemies} воинов')

            sleep(1)
        print(f'{self.name} одержал победу спустя {days_of_battle} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончилась!')
