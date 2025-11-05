# 定义一个基类：动物
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name  # 实例变量：名字
        self.age = age  # 实例变量：年龄

    @abstractmethod  # 抽象方法装饰器
    def speak(self):  # 方法：动物叫声（多态的基础）
        pass  # 不需要具体实现

    def info(self):  # 方法：显示动物信息（封装）
        print(f"{self.name} ({self.age} 岁)")


class Dog(Animal):  # 继承自 Animal 类
    def __init__(self, name, age):
        super().__init__(name, age)  # 调用父类构造函数
        self.name = name  # 实例变量：名字
        self.age = age  # 实例变量：年龄

    def speak(self):  # 方法重写（多态）
        return "汪汪！"  # 输出狗的叫声

class Cat(Animal):  # 继承自 Animal 类
    def __init__(self, name, age, color):
        super().__init__(name, age)  # 调用父类构造函数
        self.color = color  # 实例变量：颜色

    def speak(self):  # 方法重写（多态）
        return "喵喵！"

if __name__ == '__main__':
    # 创建对象
    dog = Dog("旺财", 3)
    # 调用方法
    # dog.info()
    # dog.speak()

    cat = Cat("小猫", 2, "灰色")

    # 多态演示
    animals = [dog, cat]
    for animal in animals:
        print(f"{animal.name} 说: {animal.speak()}")

