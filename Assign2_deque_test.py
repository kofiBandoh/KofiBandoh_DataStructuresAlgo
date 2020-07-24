from deque import deque

def main():
    d = deque(20)

    d.add_to_back(5)
    d.add_to_back(6)
    d.add_to_back(7)
    d.add_to_back(8)
    d.add_to_front(666)
    d.add_to_front(999)
    print(d.remove_front())

    print(d.remove_back())
    print()
    d.print_deque()


main()