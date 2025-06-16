import os
import json
from openai import OpenAI # type: ignore
from dotenv import load_dotenv # type: ignore
from datetime import datetime

load_dotenv()
# 配置 DeepSeek API
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),  # 从 .env 读取,  
    base_url="https://api.deepseek.com"  # DeepSeek API 地址
)

# 任务1：文章摘要
def summarize(text):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一个专业的文本摘要助手"},
            {"role": "user", "content": f"用中文简洁总结以下文章，不超过100字：\n\n{text}"}
        ],
        temperature=0.7,
        stream=False
    )
    return response.choices[0].message.content



# 主函数：处理输入文件并输出JSON
def process_tasks(input_txt_path, output_json_path):
    # 读取输入文件
    with open(input_txt_path, 'r', encoding='utf-8') as f:
        input_text = f.read().strip()

    # 执行所有任务
    results = {
        "timestamp": datetime.now().isoformat(),
        "input_file": input_txt_path,
        "output_file": output_json_path,
        "tasks": {
            "summarization": {
                "prompt": "用中文简洁总结文章",
                "input": input_text,
                "output": summarize(input_text)
            },
            
        }
    }

    # 写入JSON文件
    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"处理完成！结果已保存到: {output_json_path}")

if __name__ == "__main__":
    # 输入输出文件路径
    input_txt = "input.txt"    # 输入文本文件
    output_json = "output.json" # 输出JSON文件

    # 检查输入文件是否存在，若不存在则创建示例文件
    if not os.path.exists(input_txt):
        with open(input_txt, 'w', encoding='utf-8') as f:
            f.write("人类评估对于评估机器学习模型生成的文本或人工撰写的文本质量是不可或缺且不可避免的。")
        print(f"已创建示例输入文件: {input_txt}")
        print("请编辑此文件后重新运行程序。")
    else:
        # 执行任务处理
        print(f"正在处理文件: {input_txt}...")
        # 调用主函数
        process_tasks(input_txt, output_json)