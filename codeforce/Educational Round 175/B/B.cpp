#include <iostream>
#include <string>
#include <vector>
#include <sstream>

// 解析一行输入到整数向量
std::vector<long long> parseLine() {
    std::string line;
    std::getline(std::cin, line);
    std::stringstream ss(line);
    std::vector<long long> result;
    long long value;
    while (ss >> value) {
        result.push_back(value);
    }
    return result;
}

// 读取单个整数
template<typename T>
T readSingle() {
    std::string line;
    std::getline(std::cin, line);
    T value;
    std::stringstream(line) >> value;
    return value;
}

// 读取一行字符串
std::string readString() {
    std::string line;
    std::getline(std::cin, line);
    return line;
}

int main() {
    // 读取测试用例数
    int t = readSingle<int>();
    
    for (int i = 0; i < t; i++) {
        // 读取n, x, k
        auto input = parseLine();
        unsigned long long n = static_cast<unsigned long long>(input[0]);
        long long x = input[1];
        unsigned long long k = static_cast<unsigned long long>(input[2]);
        
        // 读取字符串
        std::string s = readString();
        
        bool first_reach0 = false;
        unsigned long long first_reach0_time = 0;
        bool sec_reach0 = false;
        unsigned long long period = 0;
        long long temp_x = x;
        
        // 检查首次到达0的时间
        for (size_t idx = 0; idx < s.length(); idx++) {
            if (s[idx] == 'L') {
                temp_x -= 1;
            } else {
                temp_x += 1;
            }
            
            if (temp_x == 0) {
                first_reach0 = true;
                first_reach0_time = idx + 1;
                break;
            }
        }
        
        // 如果找到第一次到达0的时间，检查周期
        if (first_reach0) {
            long long temp = 0;
            for (size_t idx = 0; idx < s.length(); idx++) {
                if (s[idx] == 'L') {
                    temp -= 1;
                } else {
                    temp += 1;
                }
                
                if (temp == 0) {
                    sec_reach0 = true;
                    period = idx + 1;
                    break;
                }
            }
        }
        
        // 计算结果
        if (first_reach0) {
            unsigned long long res = 1;
            unsigned long long temp_k = k - first_reach0_time;
            
            if (sec_reach0) {
                res += temp_k / period;
            }
            
            std::cout << res << std::endl;
        } else {
            std::cout << "0" << std::endl;
        }
    }
    
    return 0;
}