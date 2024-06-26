def printTour(arr, n):
    start, s, d = 0, 0, 0
    for i in range(n):
        s += arr[i][0] - arr[i][1]
        if s < 0:
            start = i+1
            d += s
            s = 0
    return start if (s+d)>=0 else -1


if __name__ == "__main__":
    arr = [[6, 4], [3, 6], [7, 3]]
    start = printTour(arr, 3)
    if start == -1:
        print("No Solution Possible !!!")
    else:
        print("start = {}".format(start))

