import pickle

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f'{self.name} ест корм.')


class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} говорит угу")


class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} говорит мурр")


class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} говорит шшшшш")


class ZooKeeper():
    def feed_animal(self, animal):
        print(f'Служитель кормит животное {animal.name}')


class Veterinarian():
    def heal_animal(self, animal):
        print(f'Ветеринар лечит животное {animal.name}')


class Zoo():
    def __init__(self):
        self.workers_list = []
        self.animals_list = []

    def add_worker(self, new_worker):
        self.workers_list.append(new_worker)
        print(f'Работник успешно добавлен')

    def add_animal(self, animal):
        self.animals_list.append(animal)
        print(f'{animal.name} успешно добавлен')

    def save_zoo(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_zoo(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)


def animal_sound(animals_list):

    for animal in animals_list:
        animal.make_sound()


zoo = Zoo()

bird1 = Bird('Сова', 5)
mammal1 = Mammal('Кошка', 4)
reptile1 = Reptile('Крокодил', 13)

zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)

animal_sound(zoo.animals_list)

zookeeper = ZooKeeper()
vet = Veterinarian()

zoo.add_worker(zookeeper)
zoo.add_worker(vet)

zookeeper.feed_animal(mammal1)
vet.heal_animal(bird1)

# Сохранение информации о зоопарке в файл
zoo.save_zoo("zoo.pkl")

# Загрузка информации о зоопарке из файла
new_zoo = Zoo.load_zoo("zoo.pkl")
