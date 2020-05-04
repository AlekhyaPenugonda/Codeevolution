class final:
    def __init__(self, id1, name, gen, dist):
        self.id1 = id1
        self.name = name
        self.gen = gen
        self.dist = dist
    def caldis(self, l, ID, dis):
        for i in l:
            if i.id1 == ID:
                return int(i.dist) * (dis/100)
        return -1

if __name__ == "__main__":
    n = int(input())
    l = []
    for k in range(n):
        id1 = input()
        name = input()
        gen = input()
        dist = input()
        if k == 0:
            obj = final(id1, name, gen, dist)
            l.append(obj)
        else:
            l.append(final(id1, name, gen, dist))
    ID = input()
    dis = int(input())
    val = obj.caldis(l, ID, dis)
    if val == -1:
        print("No value")
    else:
        print(int(val))
