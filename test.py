import numpy as np
from math import inf, hypot, sqrt
from optparse import OptionParser

def distance(a, b):
    return hypot(a[0] - b[0], a[1] - b[1])


def main(draw_always, points, runs):
    for i in range(runs):
        print("-------------------------------------")
        xs, ys = np.random.randint(low=0, high=100, size=(2,points))

        diam = -inf
        alg_diam = -inf
        real_p1 = None
        real_p2 = None

        alg_p1 = None
        alg_p2 = None

        for x1, y1 in zip(xs, ys):
            for x2, y2 in zip(xs, ys):
                dist = distance((x1, y1), (x2, y2))
                # print(round(x1, 2), round(y1, 2), round(x2, 2), round(y2, 2), round(dist, 2))
                if dist > diam:
                    real_p1 = (x1, y1)
                    real_p2 = (x2, y2)
                    diam = dist

        for x, y in zip(xs, ys):
            if alg_p1 is None:
                alg_p1 = (x, y)
                continue
            if alg_p2 is None:
                alg_p2 = (x, y)
                alg_diam = hypot(alg_p1[0] - x, alg_p1[1] - y)
                print("update", alg_p1, alg_p2, alg_diam)
                continue

            dist1 = distance(alg_p1, (x, y))
            dist2 = distance(alg_p2, (x, y))
            if dist2 > alg_diam and dist2 > dist1:
                alg_p1 = (x, y)
                alg_diam = dist2
                print("update", alg_p1, alg_p2, alg_diam)
                continue
            if dist1 > alg_diam and dist1 >= dist2:
                alg_p2 = (x, y)
                alg_diam = dist1
                print("update", alg_p1, alg_p2, alg_diam)


        print("real result", real_p1, real_p2, diam)
        print("alg result", alg_p1, alg_p2, alg_diam)
        print("ratio", alg_diam/diam, "1/sqrt(3)", 1/sqrt(3))

        if alg_diam/diam < 1/sqrt(3) or draw_always:
            import matplotlib.pyplot as plt
            for z in zip(xs, ys):
                print(z)

            plt.scatter(xs, ys)
            plt.plot([real_p1[0], real_p2[0]], [real_p1[1], real_p2[1]], 'ro-')
            plt.plot([alg_p1[0], alg_p2[0]], [alg_p1[1], alg_p2[1]])
            plt.show()

if __name__ == "__main__":
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option("--draw-always", dest="draw_always", action="store_true", help="Always draw the points",
                      default=False)
    parser.add_option("--points", dest="points", type="int", action="store", help="Number of points for each run",
                      default=50)
    parser.add_option("--runs", dest="runs", type="int", action="store", help="Number of runs", default=50)
    opt, args = parser.parse_args()
    main(opt.draw_always, opt.points, opt.runs)
