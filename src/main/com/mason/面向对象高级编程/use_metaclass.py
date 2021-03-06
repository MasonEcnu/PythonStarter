#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用元类
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的


def fn(self, name="world"):
    print("Hello %s" % name)


# type()函数既可以返回一个对象的类型，又可以创建出新的类型
# 创建Hello Class
# 要创建一个class对象，type()函数依次传入3个参数：
# 1. class的名称；
# 2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
Hello = type("Hello", (object,), dict(hello=fn))
h = Hello()
h.hello()

print(type(h))


# 因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法
# 然后调用type()函数创建出class

# 元类--metaclass
# 先定义metaclass，就可以创建类，最后创建实例

# __new__()方法接收到的参数依次是：
# 1.当前准备创建的类的对象；
# 2.类的名字；
# 3.类继承的父类集合；
# 4.类的方法集合。
class ListMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        attrs["add"] = lambda self, value: self.append(value)
        return type.__new__(mcs, name, bases, attrs)


# metaclass: 它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建
class MyList(list, metaclass=ListMetaclass):
    pass


ml = MyList()
ml.add(1)
print(ml)


# 编写一个ORM框架
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return "<%s:%s>" % (self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, "varchar(100)")


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, "int")


class LongField(Field):

    def __init__(self, name):
        super(LongField, self).__init__(name, "bigint")


class ModelMetaclass(type):

    def __new__(mcs, name, bases, attrs):
        if name == "Model":
            return type.__new__(mcs, name, bases, attrs)
        print("Found model: %s" % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print("Found mapping: %s ==> %s" % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs["__mappings__"] = mappings  # 保存属性和列的映射关系
        attrs["__table__"] = name  # 假设表名和类名一致
        return type.__new__(mcs, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"Model object has no attribute %s" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append(str(getattr(self, k, None)))
            args.append(getattr(self, k, None))
        sql = "insert into %s (%s) values (%s)" % (self.__table__, ",".join(fields), ",".join(params))
        print("SQL: %s" % sql)
        print("ARGS: %s" % str(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = LongField("id")
    name = StringField("username")
    email = StringField("email")
    password = StringField("password")


# 创建一个实例：
u = User(id=12345, name="Michael", email="test@orm.org", password="my-pwd")
# 保存到数据库：
u.save()
