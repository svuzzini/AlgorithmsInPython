# This is a program to reverse digits of a 32-bit signed integer

class reverse:    
    def reverseint(self, x: int) -> int:
        
        if(x<0):
            y=str((-1*x))
            x=int(y[::-1])
            x=-1*x

        elif(x>0):
            y=str(x)
            x=int(y[::-1])

        if (x > (2**31 - 1)) or (x < (-2**31 - 1) or x==0):
            return 0

        return x

# driver function to test

first=reverse()
print(first.reverseint(x=435454545))
