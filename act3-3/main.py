from os import read


'''
0/1 Knapsack solution using dp

Advanced algorithms class

Authors:

Rafael Jimenez A01637850
Joshua Hernandez A01246538

'''
def optimal_profit(elements, knapsack_cap):
    # initiate cost table (item amount * knapsack's capasity + 1 matrix).
    cost_table = [[0 for _ in range(knapsack_cap + 1)] for _ in range(len(elements))]

    # iterate for all items.
    for item, [value, weight] in enumerate(elements):
        # Iterate from 1 to knapsack's capacity.
        for current_cap in range(1, knapsack_cap + 1):
            # Only get value from the row above and same column or the value
            # from a left column (current capacity - item's weight) in the row
            # above + current item's value.
            if weight <= current_cap:
                cost_table[item][current_cap] = max(
                    value + cost_table[item - 1][current_cap - weight],
                    cost_table[item - 1][current_cap]
                    )
            else:
                cost_table[item][current_cap] = cost_table[item - 1][current_cap]
 
    # Return the lower right most value in the cost table.
    return cost_table[len(elements) - 1][knapsack_cap]

if __name__ == "__main__":

    with open("test.txt") as reader:
        element_amount = reader.readline()
        test_No = 0

        while element_amount != '':
            test_No += 1
            print("test {number}".format(number=test_No))

            elements = []


            for value in range(int(element_amount)):
                elements.append([int(reader.readline()), -1])

            for item in elements:
                item[1] = int(reader.readline())

            knapsack_cap = int(reader.readline())

            print(optimal_profit(elements, knapsack_cap))

            # Next test set up.
            
            element_amount = reader.readline()

'''

Test cases explanation 
----------------------

Test case 1: 
Validate the algorithm since we have the output to compare to 

Test case 2:
What happens if all the possible items its heavier that the max capacity

Test case 3:


Test case 4:

'''