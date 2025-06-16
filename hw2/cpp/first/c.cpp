#include <iostream>
#include <fstream>
#include <windows.h>
struct Person {
    char name[50];
    int age;
    double height;
};

int main() {
    SetConsoleOutputCP(CP_UTF8);
    // 二进制写入
    Person p1 = {"张三", 25, 175.5};
    
    std::ofstream outBinary("person.dat", std::ios::binary);
    if (!outBinary) {
        std::cerr << "无法创建二进制文件！" << std::endl;
        return 1;
    }
    
    // 写入结构体数据
    outBinary.write(reinterpret_cast<char*>(&p1), sizeof(Person));
    outBinary.close();
    
    // 二进制读取
    Person p2;
    std::ifstream inBinary("person.dat", std::ios::binary);
    if (!inBinary) {
        std::cerr << "无法打开二进制文件！" << std::endl;
        return 1;
    }
    
    inBinary.read(reinterpret_cast<char*>(&p2), sizeof(Person));
    inBinary.close();
    
    std::cout << "读取的数据：" << std::endl;
    std::cout << "姓名: " << p2.name << std::endl;
    std::cout << "年龄: " << p2.age << std::endl;
    std::cout << "身高: " << p2.height << std::endl;
    
    return 0;
}