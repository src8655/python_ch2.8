# class Point


class Point:
    count_of_instance = 0            # 클래스 멤버
    # self.count_of_instance 했을때
    # 인스턴스 멤버 변수에 없으면
    # 클래스 멤버에서 찾는다

    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        Point.count_of_instance += 1

        # __init__의 멤버변수가 되었다가 사라진다
        # count_of_instance = 0

        # 현재 생성된 객체의 인스턴스 변수가 새로 생겨버린다
        # self.count_of_instance = 0

    def __del__(self):
        Point.count_of_instance -= 1

    def __str__(self):
        return str(type(self)) + 'Point({0}, {1})'.format(self.x, self.y)

    def __repr__(self):
        return 'Point({0}, {1})'.format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __iadd__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __isub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def show(self):
        print('점[{0}, {1}]'.format(self.x, self.y))

    # cls를 안줘도 에러안남
    @classmethod
    def class_method(cls):
        return cls.count_of_instance

    @staticmethod
    def static_method():
        print('static method called')
