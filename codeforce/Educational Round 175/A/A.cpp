#include <iostream>
#include <vector>
#include <string>

int main() {
    int t;
    std::cin >> t;
    
    for (int i = 0; i < t; i++) {
        uint64_t n;
        std::cin >> n;
        
        uint64_t quotient = n / 15;
        uint64_t remainder = (n % 15 <= 2) ? (n % 15 + 1) : 3;
        
        std::cout << quotient * 3 + remainder << std::endl;
    }
    
    return 0;
}