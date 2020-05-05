def bubble_sort(l):
    for i in range(len(l)):
        for j in range(0, len(l)-i-1):
            if l[j] > l[j+1] :
                l[j], l[j+1] = l[j+1], l[j]
                print("After swap: ", l)
        print(l)

if __name__ == "__main__":
    lt = list(map(int, input().split()))
    bubble_sort(lt)
    for i in range(len(lt)):
        print("%d" %lt[i])