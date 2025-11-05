class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        # 方法：显示动物信息（封装）
        print(f"{self.name} ({self.age}岁)")

    def speak(self):
        print("汪汪！")

if __name__ == '__main__':
    dog = Dog('小黄', '2')
    dog.info()