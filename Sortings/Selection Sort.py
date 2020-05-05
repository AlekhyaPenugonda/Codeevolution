def selec_sort(l):
    for i in range(len(l)-1):
        min_idx = i
        for  j in range(i+1, len(l)):
            if l[j] < l[min_idx]:
                min_idx = j
        l[i], l[min_idx] = l[min_idx], l[i]
        print(l)
    return l

if __name__ == "__main__":
    lt = list(map(int, input().split()))
    result = selec_sort(lt)
    print(result)