C++ 文件 I/O 经典案例

以下是几个经典的 C++ 文件读写案例，包含详细注释：

1. 基本文件写入

```cpp
#include <iostream>
#include <fstream> // 包含文件流头文件

int main() {
    // 创建输出文件流对象
    std::ofstream outFile;
    
    // 打开文件，如果文件不存在则创建
    outFile.open("example.txt", std::ios::out);
    
    // 检查文件是否成功打开
    if (!outFile.is_open()) {
        std::cerr << "无法打开文件！" << std::endl;
        return 1;
    }
    
    // 写入数据到文件
    outFile << "这是第一行文本\n";
    outFile << "这是第二行文本\n";
    outFile << 12345 << " " << 3.14159 << std::endl;
    
    // 关闭文件
    outFile.close();
    
    std::cout << "数据已成功写入文件！" << std::endl;
    return 0;
}
```

2. 基本文件读取

```cpp
//注意在该文件代码中，文本文档保存格式对中文不友好，在linux环境和windows环境中的读取中文和输出中文不一样
#include <iostream>
#include <fstream>
#include <string>

int main() {
    // 创建输入文件流对象
    std::ifstream inFile;
    
    // 打开文件
    inFile.open("example.txt", std::ios::in);
    
    if (!inFile.is_open()) {
        std::cerr << "无法打开文件！" << std::endl;
        return 1;
    }
    
    std::string line;
    std::cout << "文件内容：" << std::endl;
    
    // 逐行读取文件内容
    while (std::getline(inFile, line)) {
        std::cout << line << std::endl;
    }
    
    // 关闭文件
    inFile.close();
    
    return 0;
}

```

3. 二进制文件读写

```cpp
#include <iostream>
#include <fstream>

struct Person {
    char name[50];
    int age;
    double height;
};

int main() {
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
```

4. 文件追加写入

```cpp
#include <iostream>
#include <fstream>

int main() {
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
```

5. 文件拷贝功能

```cpp
#include <iostream>
#include <fstream>

int main(int argc, char* argv[]) {
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
```

6. 文件随机访问

```cpp
//这个文件写入有大问题，日后再研究，或许能找一些文件写入的论文
#include <iostream>
#include <fstream>
#include <string>

int main() {
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
    
    // 移动到文件开头
    file.seekg(0, std::ios::beg);
    
    // 读取第5行（从0开始计数）
    std::string line;
    for (int i = 0; i < 5; ++i) {
        std::getline(file, line);
    }
    
    std::cout << "第5行内容: " << line << std::endl;
    
    // 修改第5行
    file.seekp(file.tellg()); // 定位到当前位置
    file << "这是修改后的第5行" << std::endl;
    
    file.close();
    return 0;
}
```

关键点总结
==**这个文件写入有大问题，日后再研究，或许能找一些文件写入的论文**==

1. 文件流类：
   • `ifstream` - 用于文件输入（读取）

   • `ofstream` - 用于文件输出（写入）

   • `fstream` - 用于文件输入和输出


2. 文件打开模式：
   • `ios::in` - 读取模式

   • `ios::out` - 写入模式

   • `ios::app` - 追加模式

   • `ios::binary` - 二进制模式

   • `ios::trunc` - 截断模式（清空文件）


3. 重要方法：
   • `open()` - 打开文件

   • `close()` - 关闭文件

   • `is_open()` - 检查文件是否打开

   • `seekg()`/`seekp()` - 移动读写位置

   • `tellg()`/`tellp()` - 获取当前位置


这些案例涵盖了C++文件I/O的基本操作，包括文本和二进制文件的读写、追加写入、文件拷贝和随机访问等常见需求。