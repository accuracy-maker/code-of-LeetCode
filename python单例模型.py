def singleton(cls,*args,**kwargs): # 创建外层函数singleton,可以传入类
    instances = {} # 创建一个instances字典用来保存单例
    def get_instance(*args,**kwargs):
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
        return instances[cls] # 判断instances字典是否含有单例，如果没有就创建
    return get_instance()

#创建一个带有装饰器的类
@singleton
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

student = Student('ght',21)