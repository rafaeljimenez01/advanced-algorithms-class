#include <iostream>
#include <vector>

/*******************************************************************************
 * Prints solution.
 * 
 *  - Time complexity O(w).
 *  - Space complexity O(w).
 * 
 * Where w is the minimum number of needed coins to achieve the neede change.
*******************************************************************************/
void print(const std::vector<int*> &minCoins, int change) {
  while(change > 0) {
    std::cout << *minCoins[change] << std::endl;
    change -= *minCoins[change];
  }
}


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
std::vector<int*> changeDp(std::vector<int> &coins, const int &change) {
  std::vector<int*> solution(change + 1, nullptr);
  std::vector<int> minCoins(change + 1, change);

  minCoins[0] = 0;

  for(size_t money = 1; money <= change; ++money) {
    for(int &coin : coins) {
      if(coin <= money && minCoins[money - coin] < minCoins[money]) {
          solution[money] = &coin;
          minCoins[money] = minCoins[money - coin]  + 1;
      }
    }
  }

  return solution;
}

std::vector<int*> changeGreedy(std::vector<int> coins, int m) {

  // sort(coins.begin(), coins.end(), std::greater<int>());
  int current = 0;
  std::vector<int*> solution;

  while (m > 0){
    if (m - coins[current] >= 0){
      solution.push_back(&coins[current]);
      m -= coins[current];
    }
    else{
      current += 1;
      if (current >= coins.size()) {
        std::cout << "u trying to trick me nigga" << std::endl;
        break;
      }
    }
  }

  return solution;

}


int main() {
int n,        //number of coins
    p,        //price of product
    q,        //money received
    change;   //change to give 

  //creates a vector with every different coin denomination
  std::cout << "Enter number of diferent denominations" << std::endl;
  std::cin >> n;
  std::cout << "Enter denominations now" << std::endl;
  std::vector<int> coins(n);
  for(int &coin : coins) {
    std::cin >> coin;
  }

  //Calculates the change and determains the minimum number of coins to complete the change
  std::cout << "Enter price" << std::endl;
  std::cin >> p;
  std::cout << "Enter amount received" << std::endl;
  std::cin >> q;
  change = q - p;

  std::cout << "Dynamic programing solution:" << std::endl;
  print(changeDp(coins, change), change);

  // std::cout << "Greedy solution:" << std::endl;
  // print(changeGreedy(coins, change), change);

  return 0;
}