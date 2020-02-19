class LinkedList:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

    def print_nodes(ll):

        while start:
            end = start 
            total = 0
            skip = False

            while end:
                total += end.data
                if start == end:
                    total == 0
                    skip = True
                    break
                end = end.next 

            if not skip:
                print(start.data)

            start = start.next