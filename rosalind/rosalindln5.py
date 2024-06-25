

def evennumbers(input_file, output_file):

    with open(input_file, 'r') as fpin:
        lines = fpin.readlines()
    
    even_lines = []
    for i in range(1, len(lines), 2):
        even_lines.append(lines[i])


    with open(output_file, 'w') as fpout:
        fpout.writelines(even_lines)



if __name__ == '__main__':
        evennumbers("/home/mako/PE/rosalind_ini5.txt", "/home/mako/PE/output.txt")