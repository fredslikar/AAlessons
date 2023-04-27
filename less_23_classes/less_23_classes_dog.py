class Dog():
    """Esy model of dog"""

    def __init__(self, name, age):
        """Inicialisation of atributs of names and ages of dogs"""
        self.name = name
        self.age = age
        print(self.name.title() + " like a dog is creating")

    def sit(self):
        """Dogs will sit down after the comand"""
        print(self.name.title() + " is siting")

    def jump(self):
        """Dogs will jump after the command"""
        print(self.name.title() + " jumpd one time")

    def vuf(self):
        """Dogs will make "vuf" """
        print(self.name.title() + " makes 'vuf'")

my_dog1 = Dog("cezar", 5)
my_dog2 = Dog("zeus", 10)
my_dog1.jump()
my_dog2.sit()
Gera = Dog("gera", 7)
Gera.vuf()






