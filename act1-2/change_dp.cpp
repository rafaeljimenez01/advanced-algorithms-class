#include <iostream>
#include <vector>
#include <fstream>
#include <bits/stdc++.h>

/*******************************************************************************
 *   Finds the right mix of coins that add up to the needed change with the
 * least amount of coins.
 * 
 *   Utilizes a dynamic programing aproach. More specifically a bottom up
 * strategy. In other words, to find the solution for change = 10 the algorithm
 * requiers to find the solution for change 1, 2, 3, 4... 9 in this order and 
 * saves it in memory for later use. For each sub-problem it tries every coin.
 * Thus:
 *  - Time Complexity O(n * m)
 *  - Space Complexity O(n^2)
 * 
 *    Where n is the amount of change and m is the amount of different coin's
 * denomination.
*******************************************************************************/
void changeDp(std::vector<int> &coins, int change) {
  std::vector<int> solution(change + 1, -1);
  std::vector<int> minCoins(change + 1, change);

  minCoins[0] = 0;

  // Iterates through all possible changes before the needed change.
  for(size_t money = 1; money <= change; ++money) {
    // Iterates through all coin's denomiantion.
    for(int &coin : coins) {
      //updates best coin and number of coins seen so far for current change.
      if(coin <= money && minCoins[money - coin] < minCoins[money]) {
          solution[money] = coin;
          minCoins[money] = minCoins[money - coin]  + 1;
      }
    }
  }

    // if the solution (neede coin) for the current change was never updates
    // the target change is not posible to reach.
    if(solution[change] == -1) {
      std::cout << "Cannot reach needed change with given coin's denominations" << std::endl;
      return;
    }

    while(change > 0) {
      std::cout << solution[change] << std::endl;
      change -= solution[change];
    }
}

void changeGreedy(std::vector<int> &coins, int m) {

  std::sort(coins.begin(), coins.end(), std::greater<int>());
  int current = 0; //index of the biggest coin possible
  std::vector<int> solution;

  while (m > 0){
    if (m - coins[current] >= 0){ //checks if the biggest coin yet it's possible to use
      solution.push_back(coins[current]); //if so add it to the solution
      m -= coins[current]; //reduce the change
    }
    else{
      current += 1; //if the coins its bigger that the missing change we should look to the next biggest coin
      if (current >= coins.size()) {
        std::cout << "Cannot reach needed change with given coin's denominations" << std::endl;
        return;
      }
    }
  }


  for(const int &value : solution) {
     std::cout << value << std::endl;
  }
}


int main() {
  std::ifstream file("tests.txt");

  if(file.is_open()) {
    int x = 0;
		while(x < 4) {
      int n,        //number of coins
          p,        //price of product
          q,        //money received
          change;   //change to give 

        //creates a vector with every different coin denomination
        file >> n;
        std::vector<int> coins(n);
        for(int &coin : coins) {
          file >> coin;
        }

        //Calculates the change and determains the minimum number of coins to complete the change
        file >> p;
        file >> q;
        change = q - p;

        std::cout << "Dynamic programing solution:" << std::endl;
        changeDp(coins, change);

        std::cout << std::endl;

        std::cout << "\nGreedy solution:" << std::endl;
        changeGreedy(coins, change);
        std::cout << std::endl;

        ++x;
    }
  }

  return 0;
}

/*****
 *  - The first case with coins 1 2 5 is to check if both algorithms work correctly
 *     with a general case
 *  - The second case shows how a greedy algorithm can fail because of the
 *     greedy decissions.
 *  - The thrid case shows that dp can generate better solutions than greedy 
 *  - The forth case is to ensure that the code is robust enough to catch errors
 *    like not being able to reach the target with the given denominations.
****/ 