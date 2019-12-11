class Animal(object):

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(self.sound)

    def get_name(self):
        return self.name

if __name__ == '__main__':

    dog = Animal('Fido', 'Bark')
    dog.make_sound()
