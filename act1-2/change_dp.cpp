#include <iostream>
#include <vector>
#include <utility>
#include <bits/stdc++.h>

void get_change(std::vector<int> &coins, std::vector<std::pair<int, int*>> &minCoins, const int &change) {
  for(int money = 1; money <= change; ++money) {
    for(int &coin : coins) {
      if(coin <= money && minCoins[money - coin].first < minCoins[money].first) {
          minCoins[money].first = minCoins[money - coin].first + 1;
          minCoins[money].second = &coin;
      }
    }
  }
}

int main() {
  int n,
      p,
      q,
      change;

  std::cin >> n;
  std::vector<int> coins(n);
  for(int &coin : coins) {
    std::cin >> coin;
  }

  std::cin >> p;
  std::cin >> q;
  change = p - q;
  std::vector<std::pair<int, int*>> minCoins(change + 1, std::make_pair(INT_MAX, nullptr));
  minCoins[0].first = 0;

  get_change(coins, minCoins, change);


  while(change > 0) {
    std::cout << *minCoins[change].second << std::endl;
    change -= *minCoins[change].second;
  }

  return 0;
}
