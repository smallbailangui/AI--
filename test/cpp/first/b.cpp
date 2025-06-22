#include <iostream>
#include <fstream>
#include <string>
#include <windows.h> // 仅适用于Windows

int main() {
    // 设置控制台输出编码为UTF-8
    SetConsoleOutputCP(CP_UTF8);
    
    std::ifstream infile("output.txt");
    if (!infile.is_open()) {
        std::cerr << "Error opening file!" << std::endl;
        return 1;
    }
    
    std::string line;
    std::cout << "文件内容如下：\n";
    
    while (std::getline(infile, line)) {
        std::cout << line << std::endl;
    }
    
    infile.close();
    return 0;
}