#include <iostream>

int get_change(int m) {
  int count = 0;

  while(m != 0) {
    if(m - 10 >= 0) {
      m -= 10;
    }
    else if(m - 5 >= 0) {
      m -= 5;
    }else{
      m--;
    }

    count++;
  }

  return count;
}

int main() {
  int m;
  std::cin >> m;
  std::cout << get_change(m) << '\n';
}
