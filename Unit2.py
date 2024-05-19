# Animal Class
class Animal:

    zoo_name = 'Hayaton'

    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name

    # Returns True if hunger is greater than zero
    def is_hungry(self):
        return self._hunger > 0

    # Reduces the hunger by 1
    def feed(self):
        self._hunger -= 1

    # Prints the animal's talking sound
    def talk(self):
        print('talking')


# Dog Class
class Dog(Animal):

    def __init__(self, name, hunger=0):
        Animal.__init__(self, name, hunger)

    def talk(self):
        print('woof woof')

    @staticmethod
    def fetch_stick(self):
        print('There you go, sir!')


# Cat Class
class Cat(Animal):

    def __init__(self, name, hunger=0):
        Animal.__init__(self, name, hunger)

    def talk(self):
        print('meow')

    @staticmethod
    def chase_laser(self):
        print('Meeeeow')


# Skunk Class
class Skunk(Animal):

    def __init__(self, name, hunger=0, stink_count=6):
        Animal.__init__(self, name, hunger)
        self._stink_count = stink_count

    def talk(self):
        print('tsssss')

    @staticmethod
    def stink(self):
        print('Dear lord!')


# Unicorn Class
class Unicorn(Animal):

    def __init__(self, name, hunger=0):
        Animal.__init__(self, name, hunger)

    def talk(self):
        print('Good day, darling')

    @staticmethod
    def sing(self):
        print('I’m not your toy...')


# Dragon Class
class Dragon(Animal):

    def __init__(self, name, hunger=0, color='Green'):
        Animal.__init__(self, name, hunger)
        self._color = color

    def talk(self):
        print('Raaaawr')

    @staticmethod
    def breath_fire(self):
        print('$@#$#@$')


def main():
    # Create first batch of animals with distinct values
    dog_brownie = Dog('Brownie', 10)
    cat_zelda = Cat('Zelda', 3)
    skunk_stinky = Skunk('Stinky', 0)
    unicorn_keith = Unicorn('Keith', 7)
    dragon_lizzy = Dragon('Lizzy', 1450)

    # Adds the animals to the zoo_lst list
    zoo_lst = [dog_brownie, cat_zelda, skunk_stinky, unicorn_keith, dragon_lizzy]

    # Create new animals for the zoo and add them to the zoo_lst list
    dog_doggo = Dog('Doggo', 80)
    cat_kitty = Cat('Kitty', 80)
    skunk_stinky_jr = Skunk('Stinky Jr.', 80)
    unicorn_clair = Unicorn('Clair', 80)
    dragon_mc_fly = Dragon('McFly', 80)

    # Add new animals to list
    zoo_lst += [dog_doggo, cat_kitty, skunk_stinky_jr, unicorn_clair, dragon_mc_fly]

    # Iterate through the zoo animals list and print the hungry animals type and name and feed them until hunger is zero
    for animal in zoo_lst:
        if animal.is_hungry():
            print('{} {}'.format(animal.__class__.__name__, animal.get_name()))
        while animal.is_hungry():  # Feeds the animal until their hunger is zero i.e. not hungry
            animal.feed()

        animal.talk()  # Print the animals unique talk function based on type

        # Check animals type and print appropriate special message
        if isinstance(animal, Dog):  # Is Dog
            animal.fetch_stick(animal)
        elif isinstance(animal, Cat):  # Is Cat
            animal.chase_laser(animal)
        elif isinstance(animal, Skunk):  # Is Skunk
            animal.stink(animal)
        elif isinstance(animal, Unicorn):  # Is Unicorn
            animal.sing(animal)
        elif isinstance(animal, Dragon):  # Is Dragon
            animal.breath_fire(animal)

    # Print the static zoo name
    print(Animal.zoo_name)


if __name__ == '__main__':
    main()
