#include <iostream>
#include <fstream>
#include <windows.h> // 仅适用于Windows

int main(int argc, char* argv[]) {
    SetConsoleOutputCP(CP_UTF8);
    //手动执行输入参数
    // 检查命令行参数
    if (argc != 3) {
        std::cerr << "用法: " << argv[0] << " <源文件> <目标文件>" << std::endl;
        return 1;
    }
    
    // 打开源文件
    std::ifstream source(argv[1], std::ios::binary);
    if (!source) {
        std::cerr << "无法打开源文件！" << std::endl;
        return 1;
    }
    
    // 打开目标文件
    std::ofstream dest(argv[2], std::ios::binary);
    if (!dest) {
        std::cerr << "无法创建目标文件！" << std::endl;
        source.close();
        return 1;
    }
    
    // 拷贝文件内容
    dest << source.rdbuf();
    
    // 关闭文件
    source.close();
    dest.close();
    
    std::cout << "文件拷贝完成！" << std::endl;
    return 0;
}