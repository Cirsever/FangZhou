# 火山引擎方舟平台大模型API调用示例

import requests
import json
import os
from dotenv import load_dotenv

# 加载环境变量（如果有.env文件）
load_dotenv()

# 从环境变量获取API密钥，或者使用默认值（实际使用时请替换为您的密钥）
API_KEY = os.getenv("VOLCENGINE_API_KEY", "YOUR_API_KEY")

def call_ark_llm_api(prompt, model="deepseek-v3", max_tokens=1000, temperature=0.7):
    """
    调用火山引擎方舟平台大模型API
    
    参数:
        prompt (str): 输入提示词
        model (str): 使用的模型，默认为deepseek-v3
        max_tokens (int): 最大生成token数
        temperature (float): 温度参数，控制随机性
        
    返回:
        dict: API响应结果
    """
    url = "https://api.volcengine.com/ark/llm/generate"
    headers = {
        "Content-Type": "application/json",
        "Authorization": API_KEY
    }
    data = {
        "model": model,
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # 检查HTTP错误
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def main():
    # 示例1: 基础问答
    prompt1 = "请介绍火山引擎方舟平台的主要功能"
    print(f"\n示例1: {prompt1}")
    result1 = call_ark_llm_api(prompt1)
    print_result(result1)
    
    # 示例2: 内容创作
    prompt2 = "请帮我写一篇关于大模型在企业应用中价值的短文，300字左右"
    print(f"\n示例2: {prompt2}")
    result2 = call_ark_llm_api(prompt2)
    print_result(result2)
    
    # 示例3: 代码生成
    prompt3 = "请用Python写一个简单的网页爬虫，能够提取网页标题和主要内容"
    print(f"\n示例3: {prompt3}")
    result3 = call_ark_llm_api(prompt3)
    print_result(result3)

def print_result(result):
    """格式化打印API结果"""
    if "error" in result:
        print(f"错误: {result['error']}")
    elif "response" in result:
        print(f"回复: {result['response']}")
    else:
        print(f"未知响应格式: {result}")

if __name__ == "__main__":
    main()