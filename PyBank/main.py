#Import the os and csv modules
import os
import csv

PyBank_csv = os.path.join('Resources','budget_data.csv')
output_path = os.path.join("Analysis", "Budget_Analysis.txt")

def print_output():
    print("Financial Analysis")
    print("---------------------------------")
    print("Total Months: " + str(month_count))
    print("Total: $" + str(profit_loss))
    print("Average Change: $" + str(avg_change))
    print(f"Greatest Increase in Profits:  {greatest_increase_month} ({greatest_increase})")
    print(f"Greatest Decrease in Profits:  {greatest_decrease_month} ({greatest_decrease})")


#create list for store budget values, and change values, variables for incrementer and previous budget value
budget_values = []
change_values = []
i = 1  #start for loop with change values in the first row with data
last_budget_value = 0  #first last_budget_value will be set within if block
greatest_increase = 0
greatest_decrease = 0



with open(PyBank_csv, encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # The first row contains headers
    csv_header = next(csv_reader)

    
    for row in csv_reader:
        #list all budgets
        budget_values.append(int(row[1])) 
        # changes in "Profit/Losses" over the entire period
        if i > 1: 
            change_values.append(int(row[1]) - last_budget_value)
            i += 1
            last_budget_value = int(row[1])
            if change_values[-1] > greatest_increase:
                greatest_increase = change_values[-1]
                greatest_increase_month = str(row[0])
            if change_values[-1] < greatest_decrease:
                greatest_decrease = change_values[-1]
                greatest_decrease_month = str(row[0])
        else:  # inital value of i = 1 so this sets the first budget value and changes i to 2.
            i += 1
            last_budget_value = int(row[1])
     
    
    # total number of months included in the dataset
    month_count = len(budget_values)
   
    
    # net total amount of "Profit/Losses" over the entire period
    profit_loss = sum(budget_values)
    
    
    #average of those changes
    avg_change = round(sum(change_values) / (month_count - 1),2)
    

# print the analysis to the terminal
print_output()


# export a text file with the results
with open(output_path, 'w') as txtfile:
    #txtfile.write(str(print_output()))
    txtfile.write("Financial Analysis")
    txtfile.write("\n---------------------------------")
    txtfile.write("\nTotal Months: " + str(month_count))
    txtfile.write("\nTotal: $" + str(profit_loss))
    txtfile.write("\nAverage Change: $" + str(avg_change))
    txtfile.write(f"\nGreatest Increase in Profits:  {greatest_increase_month} ({greatest_increase})")
    txtfile.write(f"\nGreatest Decrease in Profits:  {greatest_decrease_month} ({greatest_decrease})")
    txtfile.close