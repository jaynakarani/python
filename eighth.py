class Animal:
    def __init__(self):
        self.eyes = 2
        self.tongue = 1
    def move(self):
        self.movement = "Freely"
        print(self.movement)

    def eat(self):
        self.eating = "Mouth"
        print(self.eating)

class Snake(Animal):
    def __init__(self):
        super().__init__()

    def move(self):
        self.movement = "Crawl"
        print(self.movement)

    def eat(self):
        self.eating = "Tongue"
        print(self.eating)

print("ANIMAL CLASS")
animal = Animal()
animal.move()
animal.eat()

print("SNAKE CLASS")
snake = Snake()
snake.move()
snake.eat()