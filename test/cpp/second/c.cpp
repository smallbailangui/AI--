#include <iostream>
#include <fstream>
#include <string>
#include <windows.h> // 仅适用于Windows

int main() {
    //这个文件写入有大问题，日后再研究，或许能找一些文件写入的论文
    SetConsoleOutputCP(CP_UTF8);
    // 创建并写入测试文件
    std::fstream file("random_access.txt", std::ios::in | std::ios::out | std::ios::trunc);
    
    if (!file) {
        std::cerr << "无法创建文件！" << std::endl;
        return 1;
    }
    
    // 写入一些数据
    for (int i = 0; i < 10; ++i) {
        file << "Line " << i << std::endl;
    }
    
    //移动到文件开头
    file.seekg(0, std::ios::beg);
    
    // 读取第5行（从0开始计数）
    std::string line;
    for (int i = 0; i < 5; ++i) {
        std::cout << "第i行内容: " << line << std::endl;
        std::getline(file, line);
    }
    
    std::cout << "第5行内容: " << line << std::endl;
    
    // 修改第5行
    file.seekp(file.tellg()); // 定位到当前位置
    file << "第5行" << std::endl;
    
    file.close();
    return 0;
}