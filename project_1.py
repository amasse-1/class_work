import random as r
import cProfile as cp

#randomized lists of 1,000 to 10,000
a1 = [r.randint(-100, 100) for _ in range(1000)] #array 1
a2 = [r.randint(-100, 100) for _ in range(2000)] #array 2
a3 = [r.randint(-100, 100) for _ in range(3000)] #array 3
a4 = [r.randint(-100, 100) for _ in range(4000)] #array 4
a5 = [r.randint(-100, 100) for _ in range(5000)] #array 5
a6 = [r.randint(-100, 100) for _ in range(6000)] #array 6
a7 = [r.randint(-100, 100) for _ in range(7000)] #array 7
a8 = [r.randint(-100, 100) for _ in range(8000)] #array 8
a9 = [r.randint(-100, 100) for _ in range(9000)] #array 9
a10 = [r.randint(-100, 100) for _ in range(10000)] #array 10

def bubble_sort(a):
    
    n = len(a)

    for i in range(n):
        for j in range(0,n - i - 1):
            if(a[j]> a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]

    
for i in range(1,11):
    print(f"""============================== Array {i} ==============================""")
    cp.run(f'bubble_sort(a{i})')
    
