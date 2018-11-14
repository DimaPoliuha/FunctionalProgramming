import time


def print_pyramid(pyramid, title):
    print('{:-^100}'.format(title))
    for elements_in_row in pyramid:
        print('{:^100}'.format('* ' * elements_in_row))


def print_pyramids():
    print_pyramid(a, 'Pyramid A')
    print_pyramid(b, 'Pyramid B')
    print_pyramid(c, 'Pyramid C')


def swap(height, a="A", b="B", c="C"):
    if height >= 1:
        swap(height - 1, a, c, b)
        pop_push(a, b)
        swap(height - 1, c, b, a)


def pop_push(frm, to):
    if frm == 'A' and to == "B":
        b.append(a.pop())
    elif frm == 'A' and to == "C":
        c.append(a.pop())
    elif frm == 'B' and to == "A":
        a.append(b.pop())
    elif frm == 'B' and to == "C":
        c.append(b.pop())
    elif frm == 'C' and to == "A":
        a.append(c.pop())
    elif frm == 'C' and to == "B":
        b.append(c.pop())
    print_pyramids()


if __name__ == '__main__':
    start_time = time.time()
    height = int(input('Height of pyramid: ')) + 1
    a = [i for i in range(1, height)]
    b = []
    c = []

    print_pyramid(a, 'Initial pyramid A')
    swap(len(a))
    print('{:^100}'.format(str(time.time() - start_time)))
