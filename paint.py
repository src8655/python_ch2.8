from point import Point


# 바운드
from rect import Rect


def test_bound_instance_method():
    p = Point()
    p.setx(10)
    p.sety(20)
    p.show()


# 언바운드
def test_unbound_class_method():
    p = Point()
    Point.setx(p, 10)
    Point.sety(p, 20)
    Point.show(p)


def test_other_method():
    # print(Point.class_method(Point))
    print(Point.class_method())
    Point.static_method()


def test_constructor():
    p1 = Point(10, 20)
    print('점[{0}, {1}], {2}'.format(p1.x, p1.y, Point.count_of_instance))

    p2 = Point(100, 200)
    print('점[{0}, {1}], {2}'.format(p2.x, p2.y, Point.count_of_instance))

    del p1
    print(Point.count_of_instance)
    del p2
    print(Point.count_of_instance)


def test_to_string():
    p = Point()
    print(p)
    print(repr(p))

    p2 = eval(repr(p))
    print(p2)


def test_class_rect():
    r1 = Rect(10, 10, 50, 50)
    r2 = eval(repr(r1))

    print(r1, str(r1.area()), sep=':')
    print(r2, str(r2.area()), sep=':')

    r1.draw()
    r2.draw()


def test_operator_overloading():
    p1 = Point(10, 20)
    print('점[{0}, {1}], {2}'.format(p1.x, p1.y, Point.count_of_instance))

    p2 = Point(100, 200)
    print('점[{0}, {1}], {2}'.format(p2.x, p2.y, Point.count_of_instance))

    p1 = p1 + p2
    print('점[{0}, {1}], {2}'.format(p1.x, p1.y, Point.count_of_instance))

    p2 = p1 - p2
    print('점[{0}, {1}], {2}'.format(p2.x, p2.y, Point.count_of_instance))

    p3 = Point(10, 20)
    p4 = Point(100, 200)
    p3 += Point(-10, -10)
    p4 -= Point(-10, -10)
    print(p3)
    print(p4)

    print(Rect(10, 20) == Rect(20, 10))
    print(Rect(10, 10) > Rect(10, 5))
    print(Rect(10, 20) < Rect(20, 10))


def main():
    # 인스턴스멤버 변수로 저장된다
    # 인스턴스멤버에 생기므로 클래스멤버를 찾기 전에 12를 먼저 찾는다
    # p.count_of_instance = 12 === self.count_of_instance = 12

    # test_bound_instance_method()
    # test_unbound_class_method()
    # test_other_method()
    # test_constructor()
    # test_to_string()
    # test_class_rect()
    test_operator_overloading()


if __name__ == '__main__':
    main()
