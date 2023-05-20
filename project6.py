import numpy as np

def LP(A, b, c):
    inv_A = np.linalg.inv(A)
    x = inv_A.dot(b) #x = inv(A).b
    cx = np.multiply(c,x) #c mulitplied by x
    sum = np.sum(cx) #sum of cx
    print(f'A: {A}\nb: {b}\nx: {x}\nc: {c}\nc*x: {cx}\nsolution(sum): {sum}') #output

def main():
    shape = int(input('Please enter the number of rows of matrix A: '))
    A=[]
    for i in range(0,shape):
        row = np.fromstring(input(f'Please enter the numbers in the row #{i+1}: '), dtype=int, sep=',')
        A.append(row)
    A = np.array(A)
    b = np.array(np.fromstring(input('Please enter the constraint limits: '), dtype=int, sep=','))
    c = np.array(np.fromstring(input('Please enter the objective function numbers: '), dtype=int, sep=','))

    LP(A,b,c)

if __name__ == '__main__':
    main()