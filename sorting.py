def counting_sort(elements, k):
    count = [0] * (k + 1)
    print('Before:', count)
    for i in range(len(elements)):
        count[elements[i]] += 1
    print('After:', count)

    counter = 0
    for i in range(k + 1):
        for j in range(count[i]):
            elements[counter] = i
            print(counter, elements)
            counter += 1

    return elements

l = [0, 0, 0, 2, 2, 1, 1, 5, 5, 3, 3]
k = 5
# counting_sort(l, k)

# print([0] * 5)


# Menurunkan angka n sampai 0
def reduce(n):
    # Base case
    if n == 0:
        return n
    
    # Recursive case
    else:
        print(n)
        return reduce(n - 1)

def fib(n):
    if n == 1:
        print(1)
        return
    
    else:
        print((n - 2) + (n - 1))
        fib(n - 1)

fib(5)