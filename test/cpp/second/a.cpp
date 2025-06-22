#include <iostream>
#include <fstream>
#include <ctime>
#include <windows.h> // 仅适用于Windows
int main() {
    SetConsoleOutputCP(CP_UTF8);
    // 以追加模式打开文件
    std::ofstream appFile("log.txt", std::ios::app);
    
    if (!appFile) {
        std::cerr << "无法打开日志文件！" << std::endl;
        return 1;
    }
    
    // 追加写入数据
    appFile << "这是一条新的日志记录\n";
    appFile << "时间戳: " << time(nullptr) << std::endl;
    
    appFile.close();
    std::cout << "日志已追加写入！" << std::endl;
    
    return 0;
}