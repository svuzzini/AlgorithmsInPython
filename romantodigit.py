class romantoint(object):
    def romtoint(self, s: str) -> int:

        #Creating the map
        m = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}

        # convert to nums
        nums =[m[k] for k in s]

        # special case: small -> large
        # change the sign of the number is enough

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                nums[i] *= -1
        return sum(nums)

# driver to test the function

test=romantoint()
print(test.romtoint('VI'))

