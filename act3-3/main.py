from os import read


'''
0/1 Knapsack solution using dp

Advanced algorithms class

Authors:

Rafael Jimenez A01637850
Joshua Hernandez A01246538

'''


# INPUT:
#   - elements: the possible elements to be added to the knapsack in format [value, weight]
#   - knapsack_cap: int, max weight available
# OUTPUT:
#   - solution to the knapsack problem.
# DESCRIPTION:
#   Given weights and values of n items, put these items 
#   in a knapsack of capacity W to get the maximum total value in the knapsack. (gfg https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/)
# Time Complexity: 
#   O(N*W) where N is the number of different elements and W is the knapsack_cap
# Space Complexity:
#  O(N*W) where N is the number of different elements and W is the knapsack_cap

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


# INPUT:
#   none
# OUTPUT:
#   none
# DESCRIPTION:
#   Reads the test cases from test.txt
# Time Complexity: 
#   O(N*W) because we call the function optimal_solution.
# Space Complexity:
#   O(1) 

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
Weight is a big number to test if there is going to be any memory or index issues and
to take advantage of the really optimal bottom-up(dp) implementation.

Test case 4:
In this example the greedy approach would fail and we would like to prove that dp
approach is going to take the best possible solution always.

Greedy would have taken the first value and the solution its the second + third one
'''