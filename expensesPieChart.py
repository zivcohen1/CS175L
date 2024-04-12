#CS 175L
#Ziv Cohen
#expensePieChart

import matplotlib.pyplot as plt

def read_expenses():
    labels = []
    values = []
    try:
        with open(r"C:\Users\zivco\Downloads\expenses.txt", 'r') as file:
            for line in file:
                label, value = line.strip().split('\t')
                try:
                    value =float(value)
                except ValueError as e:
                    print(f"Error: Invalid value '{value}' in line: '{line.strip()}")
                    continue
                labels.append(label)
                values.append(float(value))
              
                 
    except IOError:
        print("Error: Could not open the file.")
    return labels, values

def plot_pie_chart(labels, values):
   # print("Labels:", labels)
    #print("Values:", values)
 

    plt.figure(figsize=(10, 6))
    plt.pie(values, labels=labels)
    plt.title('Monthly Expenses')

    plt.show()

def main():
     labels, values = read_expenses()
     
     plot_pie_chart(labels, values)
      

if __name__ == "__main__":
    main()

