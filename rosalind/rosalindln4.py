"""
Given: Two positive integers a and b (a<b<10000)

Return: The sum of all odd integers from a through b, inclusively
"""

def dici(file_name):
        
        with open(file_name) as fp:
                string1 = fp.readlines().split()


        a = int(string1[0])
        b = int(string1[1])

        cList = range(a, b+1)
        #print(cList)
        oddnumbersc = []
        for item in cList:
                if item %2 != 0:
                         oddnumbersc.append(item)      
        #print(oddnumbersc)
        return sum(oddnumbersc)


if __name__ == '__main__':
        print (dici("/home/mako/PE/rosalind_ini4(2).txt"))