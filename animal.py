class Animal(object):

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(self.name + ' ' + self.sound)

    def get_name(self):
        return self.name

    def replicate_me(self, new_name):
        new_animal = Animal(new_name, self.sound)
        return new_animal

if __name__ == '__main__':

    dog = Animal('Fido', 'Bark')
    dog.make_sound()

    new_dog = dog.replicate_me('Joe')
    new_dog.make_sound()


