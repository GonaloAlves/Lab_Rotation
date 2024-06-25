

def strings(infile):
    fp = open(infile)
    #string1 = fp.readline()
    #string2 = fp.readline().split()
    
    #strings = fp.readlines()
    #strings[1] = strings[1].split()
    
    fp.close()

    with open(infile) as fp:
        string1 = fp.readline()
        string2 = fp.readline().split()

    a=int(string2[0])
    b=int(string2[1])
    c=int(string2[2])
    d=int(string2[3])

    return string1[a:b+1], string1[c:d+1]


if __name__ == '__main__':
        print (strings("/home/mako/PE/rosalind_ini3(1).txt"))

