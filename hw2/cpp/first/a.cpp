//1. 基本文件写入
#include <iostream>
#include <fstream>

int main(){
    std::ofstream outfile; // 创建一个输出文件流对象
    outfile.open("output.txt");
    if(!outfile.is_open()){
        std::cerr << "Error opening file!" << std::endl;
        return 1;
    }
    outfile << "这是第一行文本\n";
    outfile << "这是第二行文本\n";
    outfile <<12345 <<" " <<3.1415926<<std::endl;
    outfile.close(); // 关闭文件流 

}