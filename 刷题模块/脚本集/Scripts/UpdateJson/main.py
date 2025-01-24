import os
import json
import re
from collections import defaultdict
from datetime import datetime

# 读取 Markdown 文件并提取头部元数据
def extract_metadata_from_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # 使用正则表达式提取头部信息
        metadata = {}
        match = re.match(r'---\s*\n(.*?)\n---', content, re.DOTALL)  # 匹配头部的 YAML 格式
        if match:
            header = match.group(1)
            for line in header.split('\n'):
                # 提取 key: value 格式的数据
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip()
        
        # 返回提取的元数据
        return metadata

# 扫描目录并生成文件信息列表
def scan_markdown_files(directory):
    author_data = defaultdict(list)  # 用一个列表存储每个作者的所有文章信息
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):  # 只处理 Markdown 文件
                file_path = os.path.join(root, file)
                
                # 提取文件的元数据
                metadata = extract_metadata_from_markdown(file_path)
                
                if metadata:  # 只有提取到有效元数据才进行处理
                    creator = metadata.get('author')
                    date = metadata.get('date')
                    link = metadata.get('permalink')  # 使用 permalink 作为链接字段
                    title = metadata.get('title', file)  # 如果没有标题字段，使用文件名
                    
                    if creator and date and link:
                        # 转换日期为 "MM/DD/YYYY" 格式
                        try:
                            date_obj = datetime.strptime(date, "%Y-%m-%d")
                            date_str = date_obj.strftime("%m/%d/%Y")
                            
                            # 每篇文章存储日期、标题、链接和报告数量
                            author_data[creator].append({
                                "date": date_str,
                                "title": title,
                                "link": link,
                                "report_count": 1  # 每篇文章计数 1 次
                            })
                            
                            # 调试：只输出扫描成功的文章
                            print(f"Processed {file_path}: {metadata}")
                        except ValueError:
                            print(f"Date format error in {file_path}: {date}")
                    else:
                        print(f"Skipping {file_path}: Missing required metadata.")
                else:
                    print(f"Skipping {file_path}: No valid metadata found.")
    
    # 输出扫描到的作者数据
    if author_data:
        print(f"Author data collected: {dict(author_data)}")
    else:
        print("No author data found.")
    
    return author_data

# 更新 JSON 文件中的用户信息
def update_json_users(author_data, json_file_path):
    # 读取现有的 JSON 数据
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = {"users": {}}  # 初始化为空字典，包含 users 键

    # 更新每个作者的 posts 部分
    for author, posts in author_data.items():
        if author not in data["users"]:
            # 如果作者不存在，则创建新作者并初始化 posts
            data["users"][author] = {"posts": []}
        
        # 获取当前作者的 posts 列表
        current_posts = data["users"][author].get("posts", [])
        
        # 合并文章信息到 posts 部分，避免重复
        existing_titles = {post['title'] for post in current_posts}  # 记录已存在文章的标题
        new_posts = [post for post in posts if post['title'] not in existing_titles]
        
        # 如果有新的文章，添加到 posts 中
        if new_posts:
            data["users"][author]["posts"].extend(new_posts)
        else:
            print(f"Skipping duplicate posts for {author}: {posts}")

    # 将更新后的数据写回 JSON 文件
    if data:
        with open(json_file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f'用户数据已更新到 {json_file_path}')
    else:
        print("No data to update in JSON.")

# 主函数
def main():
    directory = 'D:/AcEasy/刷题模块/OJ'  # 请替换为你要扫描的文件夹路径
    json_file_path = 'assets/json_Database/Database.json'  # 这里指定 JSON 文件的路径
    
    # 扫描文件并获取按作者分类的文件信息
    author_data = scan_markdown_files(directory)
    
    if author_data:
        # 更新用户数据中的作者信息
        update_json_users(author_data, json_file_path)
    else:
        print("没有扫描到任何文章。")

if __name__ == "__main__":
    main()
