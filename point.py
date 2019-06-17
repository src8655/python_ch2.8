# class Point


class Point:
    count_of_instance = 1000

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
