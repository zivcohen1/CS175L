def main():
   
    total , count = get_values()
    avg = average(total,count)
    print(f'Average: {avg:.1f}')
def get_values():
    total = 0
    count = 0
    try:
        with open(r"C:\Users\zivco\OneDrive\Desktop\numbers.txt", 'r') as infile:
            for line in infile:
                try:
                    num = float(line)
                    total += num 
                    count += 1
                    print (f'I read in {count} number(s), current number is: {num:>8.2f}, Total is: {total:>8.2f}')
                except ValueError:
                    print(f'Bad data: {line.strip()} skipping')
        return total, count 
        

                    
    except IOError:
        print("SystemExit: File not found: numbers.txt - exiting")
        return 
def average(total, count):
    avg = total / count
    return avg
    
    

if __name__ == '__main__':
    main()
