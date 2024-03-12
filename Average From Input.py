#AverageFromInput
#Ziv Cohen
#CS175L
def main():
    total = 0
    count = 0
    infile = open(r"C:\Users\zivco\OneDrive\Desktop\numbers.txt", 'r')
    for line in infile:
        num = int(line)
        total += num 
        count += 1
        
        print (f'I read in {count} numbers(s) current number is: {num:>8.2f}  Total is:     {total:>8.2f}')

    average = total / count
    print(f'Average: {average:.1f}')

    
    infile.close()

    
    

if __name__ == '__main__':
    main()
    
