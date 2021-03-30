import random
class sumofarray(object):
    def __init__(self, n=10):
        self.a=[0]*n
        self.sum_row=[2, 4]
        self.sum_col=[2, 4]

  

    def sum_array(self, a):
        sum_i=0
        for i in a:
            sum_i= sum_i + i
        return sum_i

    def create_Arary(self, a):
        while self.sum_array(a) != 21:
            for i in range(len(a)):
                a[i] = random.randint(1, 18)
                temp=a[i]
                for j in range(len(a)):
                    if temp!=a[j]:
                        break





        return a

if __name__ == '__main__':
    n=int(input("Enter the number of element"))
    s=sumofarray(n)
    a=[0]*n
    s.create_Arary(a)
    for i in range(len(a)):
        print(a, end="")



