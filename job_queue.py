# python3
'''
This code simulate a program that processes a list of jobs in parallel usingg priority queue  
'''


def sift_down(i):
    c = True
    n = len(heap_time)

    while (c == True):
        l = 2 * i + 1
        r = 2 * i + 2

        min = i
        c = False

        if l < n and heap_time[l] <= heap_time[i]:
            if heap_time[l] == heap_time[i]:
                if processor[l] < processor[i]:
                    min = l
                    c = True
            else:
                min = l
                c = True

        if r < n and heap_time[r] <= heap_time[min]:
            if heap_time[r] == heap_time[min]:
                if processor[r] < processor[min]:
                    min = r
                    c = True
            else:
                min = r
                c = True

        # Swap H[i] & H[min]

        if (c == True):
            x = heap_time[i]
            heap_time[i] = heap_time[min]
            heap_time[min] = x

            y = processor[i]
            processor[i] = processor[min]
            processor[min] = y
            i = min


def min_heap():
    n = len(heap_time)

    for i in range(int(n/2), -1, -1):
        sift_down(i)


def assign_jobs(n, m):
    #global n, m
    if n < m:
        for i in range(0, n):
            processor[i] = i
            heap_time[i] = jobs[i]
            assigned_workers[i] = i
            start_times[i] = 0

        #construct min_heap from heap_time and corresponding store processor

        min_heap()

        for j in range(n, m):
            assigned_workers[j] = processor[0]
            start_times[j] = heap_time[0]
            heap_time[0] = heap_time[0] + jobs[j]
            sift_down(0)

    else:
        for i in range(0, m):
            assigned_workers[i] = i
            start_times[i] = 0


    for k in range(0, m):
        print(assigned_workers[k], start_times[k])


n, m = map(int, input().split())
jobs = list(map(int, input().split()))
m = len(jobs)
assigned_workers = [None] * m
start_times = [0]*m
processor = [None]*n
heap_time = [0]*n
assign_jobs(n, m)



