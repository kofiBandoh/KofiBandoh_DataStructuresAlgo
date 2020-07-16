from point import point
from rectangle import rectangle

def main():

    r1 = rectangle(point(1,1), point(5,5))
    r2 = rectangle(point(3,3), point(8,7))
    r3 = rectangle(point(4,4), point(7,6))


    print(r1.calc_area())
    print(r1.calc_perimeter())
    print(r1.check_overlap(r3))

main()