#include <iostream>
#include <vector>

/*******************************************************************************
 * Prints solution.
 * 
 * Time complexity O(w).
 * Space complexity O(w).
 * 
 * Where w is the size of the solution or the number of needed coins.
 ******************************************************************************/
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
 *  - Space Complexity O(n)
 * 
 *    Where n is the amount of change and m is the amount of different coin's
 * denomination.
*******************************************************************************/
std::vector<int*> changeDp(std::vector<int> &coins, const int &change) {
  std::vector<int*> solution(change + 1, nullptr);

  for(size_t money = 1; money <= change; ++money) {
    for(int &coin : coins) { //checks every coin in the coins array
      if(coin <= money && solution[money - coin] < solution[money]) { //checks if coin its smaller or equal to the missing then checks if using this
          solution[money] = &coin;                                    //coin the total ammount of coins is reduced
      }
    }
  }

  return solution;
}

std::vector<int*> changeGreedy(std::vector<int> coins, int m) {

  // sort(coins.begin(), coins.end(), std::greater<int>());
  int current = 0; //index of the biggest coin possible
  std::vector<int*> solution;

  while (m > 0){
    if (m - coins[current] >= 0){ //checks if the biggest coin yet it's possible to use
      solution.push_back(&coins[current]); //if so add it to the solution
      m -= coins[current]; //reduce the change
    }
    else{
      current += 1; //if the coins its bigger that the missing change we should look to the next biggest coin
      if (current >= coins.size()) {
        std::cout << "You have choosen a set of coins that can't make up to the change" << std::endl;
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
  change = p - q;

  std::cout << "Dynamic programing solution:" << std::endl;
  print(changeDp(coins, change), change);

  std::cout << "Greedy solution:" << std::endl;
  print(changeGreedy(coins, change), change);

  return 0;
}