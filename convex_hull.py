
def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])


def convex_graham_scan(points):
    points_i = sorted(set(points))
    l_sup = []
    l_inf = []

    for p in points_i:
        while len(l_sup) >= 2 and ccw(l_sup[-2], l_sup[-1], p) <= 0:
            l_sup.pop()

        l_sup.append(p)

    for p in reversed(points_i):
        while len(l_inf) >= 2 and ccw(l_inf[-2], l_inf[-1], p) <= 0:
            l_inf.pop()

        l_inf.append(p)

    return "No" if (l_sup[:-1] + l_inf[:-1] == points) else "Yes"


def fill_points():
    list_points = []
    f = open("C:/Temp/input.txt", "r")

    for line in f:
        count_p = int(line)

        while count_p > 0:
            values = f.readline().replace("\n", "").split("  ")
            list_points.append((int(values[0]), int(values[1])))

            count_p -= 1

        if len(list_points) > 0:
            print(convex_graham_scan(list_points))

        list_points.clear()


if __name__ == '__main__':
    fill_points()
