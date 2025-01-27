
import os
import re
import json
import sys
import time
import argparse
from collections import defaultdict
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import matplotlib
matplotlib.use('Agg')  # 使用非 GUI 后端
import matplotlib.pyplot as plt
from matplotlib import font_manager
from threading import Timer  # 导入定时器



# ------------------------------ 配置文件处理 ------------------------------
def resource_path(relative_path):
    """ 获取资源文件的路径 """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)


def load_config():
    """ 读取 JSON 配置文件 """
    json_path = resource_path("../../../data/config.json")

    if not os.path.exists(json_path):
        print(f"错误: 找不到配置文件 {json_path}")
        sys.exit(1)

    with open(json_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    return config
import os
import re

import os
import re

import os
import re

import os
import re

import os
import re

import os
import re

import os
import re

import os
import re

import os
import re
import os
import re

def generate_catalog_html(root_directory, catalog_html_path):
    """生成带有题目 div 的目录 HTML 文件"""
    catalog_html = []
    
    # 添加 HTML 标题和头部
    catalog_html.append("<!DOCTYPE html>")
    catalog_html.append("<html lang=\"zh\">")
    catalog_html.append("<head>")
    catalog_html.append("    <link rel=\"icon\" href=\"/assets/images/logo.png\" type=\"image/png\">")
    catalog_html.append("    <meta charset=\"UTF-8\">")
    catalog_html.append("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
    catalog_html.append("    <title>题目目录</title>")
    catalog_html.append("    <style>")
    catalog_html.append("        body { font-family: 'Arial', sans-serif; line-height: 1.6; margin: 0; padding: 0; background-color: #f9f9f9; }")
    catalog_html.append("        .container { max-width: 800px; margin: 50px auto; background: #e7e6e6; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }")
    catalog_html.append("        h1 { text-align: center; color: #333; margin-bottom: 20px; }")
    catalog_html.append("        p { text-align: center; color: #666; margin-bottom: 30px; }")
    
    # 为不同难度设置题目链接颜色
    catalog_html.append("        .div1 a { color: #f44336; }")  # 红色
    catalog_html.append("        .div2 a { color: #ff9800; }")  # 橙色
    catalog_html.append("        .div3 a { color: #ffeb3b; }")  # 黄色
    catalog_html.append("        .div4 a { color: #4caf50; }")  # 绿色
    catalog_html.append("        .div5 a { color: #2196f3; }")  # 蓝色
    
    # 为不同难度设置不同的容器背景色
    catalog_html.append("        .problem-item { margin: 15px 0; padding: 15px; border-radius: 5px; transition: all 0.3s ease;background-color: #ffffff;}")  
    catalog_html.append("        .div1 .problem-item { background-color: #ffebee; }")  # 红色容器背景
    catalog_html.append("        .div2 .problem-item { background-color: #fff3e0; }")  # 橙色容器背景
    catalog_html.append("        .div3 .problem-item { background-color: #fffde7; }")  # 黄色容器背景
    catalog_html.append("        .div4 .problem-item { background-color: #e8f5e9; }")  # 绿色容器背景
    catalog_html.append("        .div5 .problem-item { background-color: #e3f2fd; }")  # 蓝色容器背景
    catalog_html.append("        .problem-item:hover { background: #eaeaea; transform: translateY(-2px); }")
    catalog_html.append("        .problem-item a { text-decoration: none; font-size: 18px; font-weight: bold; }")
    catalog_html.append("        .problem-item a:hover { text-decoration: underline; }")
    catalog_html.append("        .problem-meta { font-size: 14px; color: #999; margin-top: 5px; }")
    catalog_html.append("        .back-button { position: fixed; top: 20px; left: 20px; padding: 10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; }")
    catalog_html.append("        .back-button:hover { background-color: #0056b3; }")
    catalog_html.append("    </style>")
    catalog_html.append("</head>")
    catalog_html.append("<body>")
    catalog_html.append("<button class=\"back-button\" onclick=\"window.location.href='https://aliceauto.github.io/刷题模块/'\">返回</button>")
    catalog_html.append("<div class=\"container\">")
    catalog_html.append("<h1>题目目录</h1>")
    catalog_html.append("<p>以下是所有题目的目录，点击链接可跳转到对应题目。</p>")

    # 定义文件名匹配的正则模式
    pattern = r"^(?P<difficulty>div[1-5])_(?P<types>\{[^\}]*\})_(?P<oj>[^_]+)_(?P<title>[^.]+)\.md$"  # 更新后的匹配模式
    
    # 遍历文件目录，从 OJ 子文件夹开始
    oj_directory = os.path.join(root_directory, 'OJ')
    catalog_items = []

    for root, dirs, files in os.walk(oj_directory):
        for file in files:
            if file.endswith(".md"):
                # 解析文件名，获取题目标题
                match = re.match(pattern, file)
                if match:
                    title = match.group("title")
                    oj = match.group("oj")
                    difficulty = match.group("difficulty")
                    types = match.group("types")[1:-1].split(';')  # 移除花括号并分割类型
                    
                    # 生成相对路径链接，并移除 `OJ` 前缀
                    relative_path = os.path.relpath(os.path.join(root, file), oj_directory)
                    
                    # 构建带有前缀的目录项链接
                    full_url = f"{relative_path.replace(os.sep, '/')}"

                    # 目录项
                    catalog_items.append({
                        "title": title,
                        "difficulty": difficulty,
                        "types": ', '.join(types),
                        "oj": oj,
                        "url": full_url
                    })

                    # 根据 difficulty 设置对应的 CSS 类
                    difficulty_class = difficulty.lower()  # 获取 div1, div2, ..., div5
                    
                    # HTML 目录项
                    catalog_html.append("<div class=\"problem-item " + difficulty_class + "\">")
                    catalog_html.append(f"  <a href=\"{full_url}\">{title}</a>")
                    catalog_html.append(f"  <div class=\"problem-meta\">难度: {difficulty} | 类型: {', '.join(types)} | OJ: {oj}</div>")
                    catalog_html.append("</div>")

    # 添加 HTML 尾部
    catalog_html.append("</div>")
    catalog_html.append("</body>")
    catalog_html.append("</html>")

    # 将目录内容写入 HTML 文件
    with open(catalog_html_path, "w", encoding="utf-8") as f:
        f.write("\n".join(catalog_html))

    # 输出生成的 HTML 文件的绝对路径
    absolute_html_path = os.path.abspath(catalog_html_path)
    print(f"目录 HTML 文件已生成: {absolute_html_path}")
    
    # 同时生成 README.md 文件
    generate_readme_md(catalog_items, os.path.join(root_directory, "OJ/README.md"))
    
def generate_readme_md(catalog_items, readme_md_path):
    """生成 Markdown 格式的目录文件"""
    readme_md = []

    # 添加标题和简介
    readme_md.append("---")
    readme_md.append("title: \"不渲染的页面\"")
    readme_md.append("published: false")
    readme_md.append("---")
    readme_md.append(" ")
    readme_md.append("# 题目目录")
    readme_md.append("\n以下是所有题目的目录，点击题目名称可跳转到对应题目。\n")

    # 添加表格的表头
    readme_md.append("| 题目名称 | 难度 | 类型 | OJ平台 |")
    readme_md.append("| :------- | :--- | :--- | :----- |")

    # 遍历每个目录项，按格式生成表格行
    for item in catalog_items:
        # 确保 item 是一个字典对象
        if isinstance(item, dict):
            # 题目名称变成一个链接
            readme_md.append(f"| [**{item['title']}**]({item['url']}) | {item['difficulty']} | {item['types']} | {item['oj']} |")

    # 添加结尾
    readme_md.append("\n---")
    readme_md.append("欢迎贡献更多题目！")

    # 将目录内容写入 Markdown 文件
    with open(readme_md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(readme_md))

    # 输出生成的 README 文件的绝对路径
    absolute_readme_path = os.path.abspath(readme_md_path)
    print(f"目录 README 文件已生成: {absolute_readme_path}")

# ------------------------------ 中文字体设置 ------------------------------
import os
import matplotlib.pyplot as plt
from matplotlib import font_manager

import os
import matplotlib.pyplot as plt
from matplotlib import font_manager

def set_chinese_font(config=None):
    """ 设置中文字体 """
    font_found = False

    # 如果 config 为 None，则设置为空字典
    if config is None:
        config = {}

    # 获取配置文件中指定的字体目录
    font_dir = config.get("font_path", "")
    if font_dir:
        print(f"配置文件指定的字体目录：{font_dir}")
    else:




        print("未指定字体目录，将尝试从系统中查找字体...")

    # 如果配置文件中指定了字体目录，查找该目录下的字体文件
    if font_dir and not font_found:
    
        print("正在查找系统中的中文字体...")
        font_paths = font_manager.findSystemFonts(fontpaths=None, fontext='ttf')  # 仅查找 ttf 格式的字体
        for font_path in font_paths:
            try:
                # 打印出找到的字体文件路径，方便调试
                print(f"找到字体文件路径：{os.path.abspath(font_path)}")
                font_prop = font_manager.FontProperties(fname=font_path)
                font_name = font_prop.get_name()
                # 判断是否包含常见中文字体
                if any(font in font_name for font in ['Microsoft YaHei']):
                    plt.rcParams['font.family'] = font_name
                    plt.rcParams['axes.unicode_minus'] = False
                    font_found = True
                    print(f"已找到并加载字体：{font_name}")
                    break  # 找到第一个合适的字体后即停止
            except Exception as e:
                print(f"加载字体 {font_path} 时出错: {e}")
    
    # 如果没有找到字体文件，则查找系统中的字体
    if not font_found:
        print(f"正在查找目录 {font_dir} 中的字体文件...")
        if os.path.isdir(font_dir):
            # 查找该目录下的所有 ttf 文件
            font_paths = [os.path.join(font_dir, f) for f in os.listdir(font_dir) if f.endswith('.ttf')]
            for font_path in font_paths:
                try:
                    font_prop = font_manager.FontProperties(fname=font_path)
                    font_name = font_prop.get_name()
                    # 判断是否是中文字体
                    if any(font in font_name for font in ['Microsoft YaHei']):
                        plt.rcParams['font.sans-serif'] =font_name
                        plt.rcParams['font.family'] = font_name
                        plt.rcParams['axes.unicode_minus'] = False
                        font_found = True
                        print(f"{font_path}:已找到并加载字体：{font_name}")
                        break  # 找到第一个合适的字体后即停止
                except Exception as e:
                    print(f"加载字体 {font_path} 时出错: {e}")
        else:
            print(f"指定的字体目录 {font_dir} 不存在，继续搜索系统字体")
    # 如果依然没有找到中文字体，则使用默认字体
    if not font_found:
        print("未能加载中文字体，使用默认字体 Arial")
        plt.rcParams['font.sans-serif'] =plt.rcParams['font.family'] = 'Arial'






# ------------------------------ 文件分析 ------------------------------
# 用于解析文件名的正则表达式


import re
import os

import os
import re

import re
import os

import os
import re

def analyze_filename(filename, directory, max_lines=20):
    """解析文件名并返回 div、类型、OJ 和作者信息，同时读取文件的 Front Matter 获取作者信息"""
    # 文件名格式预期为 divX_{类型}_OJ_比赛名.md
    # 我们可以通过字符串分割来提取相关信息

    # 确保文件名符合预期格式
    if filename.endswith(".md"):
        try:
            # 解析文件名
            parts = filename[:-3].split('_')  # 去除 ".md" 后分割文件名
            div_part = parts[0]  # divX
            types_part = parts[1][1:-1]  # 去除花括号
            oj_part = parts[2]  # OJ
            contest_part = parts[3]  # 比赛名
            
            div = div_part[3:]  # 获取数字部分，即 divX 中的 X
            types = types_part.split(';')  # 处理类型，可以有多个
            oj = oj_part  # OJ 平台
            contest = contest_part  # 比赛名

            # 默认作者信息为空
            authors = None
            
            try:
                # 读取文件的 Front Matter 部分，获取作者信息
                with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                    front_matter = ''
                    line_count = 0

                    while line_count < max_lines:
                        line = file.readline().strip()
                        if not line:  # 如果是空行则跳过
                            continue
                        
                        if line == '---':  # 到达 Front Matter 的分隔符
                            if front_matter:  # 如果已经读取了 Front Matter，跳出
                                break
                        front_matter += line + '\n'
                        line_count += 1

                    # 从 Front Matter 中提取作者信息
                    author_match = re.search(r'author:\s*"([^"]+)"', front_matter)
                    if author_match:
                        authors = [author_match.group(1).strip()]  # 提取作者并去除空白字符
                    else:
                        authors = ['Unknown']  # 如果没有找到作者信息，设置为 'Unknown'

            except Exception as e:
                print(f"读取文件 {filename} 出错: {e}")
            
            return div, types, authors
        
        except Exception as e:
            print(f"文件名解析失败: {filename}, 错误: {e}")
            return None, None, None

    return None, None, None


'''
(['div1'], ['type1', 'type2'], ['小明'])

'''
def count_author_contributions(file_info):
    """统计每个作者的创作量"""
    author_counts = defaultdict(int)
    for _, _, authors in file_info:
        if authors:
            for author in authors:
                if author:  # 确保作者名不为空
                    author_counts[author] += 1
    return author_counts

# 其他函数保持不变...

def scan_directory(directory, mode):
    """ 扫描目录及子目录中的所有文件并提取信息 """
    print(f"扫描的根目录的绝对路径：{os.path.abspath(directory)}")  # 打印根目录的绝对路径
    file_info = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".md"):
                div_match, types, author = analyze_filename(filename, root)
                if div_match:
                    file_info.append((div_match, types, author))
                print(f"扫描文件: {filename}")
    return file_info
def plot_author_ranking(author_counts, save_path):
    """可视化作者创作量排名，并保存为 PNG 图片"""
    # 根据创作量对作者进行排序，创作量多的在前
    sorted_author_counts = sorted(author_counts.items(), key=lambda item: item[1], reverse=False)
    
    labels = [author for author, count in sorted_author_counts]
    sizes = [count for author, count in sorted_author_counts]
    
    plt.figure(figsize=(10, 8), dpi=150)
    plt.barh(labels, sizes, color='skyblue')
    plt.xlabel("创作量")
    plt.ylabel("作者")
    plt.title("Ranking")
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"作者排名榜图表已保存到：{save_path}")
    plt.close()
   
# ------------------------------ 绘图和输出 ------------------------------
# ------------------------------ 绘图和输出 ------------------------------
def plot_div_distribution(div_counts, save_path):
    """ 可视化 div1 到 div5 的分布，并保存为 PNG 图片 """
    
    # 创建图像并设置大小和分辨率
    fig_width = 10
    fig_height = 6
    dpi = 150
    font_size = 12

    plt.figure(figsize=(fig_width, fig_height), dpi=dpi)
    
    # 指定 div 的排序顺序
    div_order = ['div1', 'div2', 'div3', 'div4', 'div5']
    # 按照指定顺序绘制 div 的条形图
  
    ordered_div_counts = {div: div_counts[div[3::]] for div in div_order if div[3::] in div_counts}
    
    if(len(ordered_div_counts)==0):
        print("数据异常")
        return
    # 绘制 div1-div5 分布的条形图
    plt.bar(ordered_div_counts.keys(), ordered_div_counts.values(), color='lightblue')
    plt.title("div1到div5分布", fontsize=font_size)
    plt.xlabel("div类别", fontsize=font_size)
    plt.ylabel("数量", fontsize=font_size)
    
    # 动态调整字体大小
    xticks_fontsize = max(font_size, fig_width // len(ordered_div_counts))
    plt.xticks(rotation=45, ha='right', fontsize=xticks_fontsize)
    
    # 优化布局，避免标签重叠
    plt.tight_layout()
    
    # 保存图片
    plt.savefig(save_path)
    print(f"div统计图表已保存到：{save_path}")
    plt.close()

def plot_type_distribution(type_counts, save_path):
    """ 可视化类型分布，并保存为 PNG 图片 """
    if(len(type_counts)==0):
        print("数据异常")
        return
    # 创建图像并设置大小和分辨率
    fig_width = 10
    fig_height = 6
    dpi = 150
    font_size = 12

    plt.figure(figsize=(fig_width, fig_height), dpi=dpi)
    
    # 绘制类型分布的条形图
    plt.bar(type_counts.keys(), type_counts.values(), color='lightgreen')
    plt.title("类型分布", fontsize=font_size)
    plt.xlabel("类型", fontsize=font_size)
    plt.ylabel("数量", fontsize=font_size)
    
    # 动态调整字体大小
    xticks_fontsize = max(font_size, fig_width // len(type_counts))
    plt.xticks(rotation=45, ha='right', fontsize=xticks_fontsize)
    
    # 优化布局，避免标签重叠
    plt.tight_layout()
    
    # 保存图片
    plt.savefig(save_path)
    print(f"类型统计图表已保存到：{save_path}")
    plt.close()

from collections import defaultdict

def print_statistics(file_info, save_directory):
    """打印统计信息并调用可视化输出"""
    div_counts = defaultdict(int)
    type_counts = defaultdict(int)
    author_counts = defaultdict(int)

    # 统计 div1-div5 分布、类型分布和作者创作量
    for div_match, types, authors in file_info:
        for div in div_match:
            div_counts[div] += 1
        for t in types:
            type_counts[t] += 1
        if authors:  # 确保 authors 不为空
            for author in authors:  # 遍历 authors 列表
                if author:  # 确保作者名不为空
                    author_counts[author] += 1

    # 输出文本统计
    print("div1到div5分布:")
    for div, count in div_counts.items():
        print(f"{div}: {count} 个")

    print("\n类型分布:")
    for t, count in type_counts.items():
        print(f"{t}: {count} 个")

    print("\n作者创作量排名榜:")
    for author, count in author_counts.items():
        print(f"{author}: {count} 个")

    # 确定保存路径
    div_save_path = os.path.join(save_directory, "div_distribution.png")
    type_save_path = os.path.join(save_directory, "type_distribution.png")
    author_save_path = os.path.join(save_directory, "author_ranking.png")
    
    os.makedirs(save_directory, exist_ok=True)

    # 分别保存 div、type 和 author 的统计图表
    plot_div_distribution(div_counts, div_save_path)
    plot_type_distribution(type_counts, type_save_path)
    plot_author_ranking(author_counts, author_save_path)
# ------------------------------ 文件夹监听 ------------------------------
class DirectoryHandler(FileSystemEventHandler):
    """ 文件夹变化事件处理 """

    def __init__(self, directory, save_directory, mode, interval):
        self.directory = directory
        self.save_directory = save_directory
        self.mode = mode
        self.interval = interval
        self.timer = None  # 定时器，用于延迟执行

    def on_any_event(self, event):
        """ 当任何文件发生变化时，重新扫描并更新统计 """
        if event.event_type != 'modified':  # 仅处理文件修改事件
            return

        # 如果变化的文件在输出目录（例如 PNG 文件）中，则忽略
        if event.src_path.endswith(".png"):
            print(f"忽略变化文件: {event.src_path} (PNG 文件)")
            return
        if event.src_path.endswith("README.md"):
            print(f"忽略变化文件: {event.src_path} (README 文件)")
            return
        if event.src_path.endswith("index.html"):
            print(f"忽略变化文件: {event.src_path} (README 文件)")
            return

        # 如果已有定时任务正在等待，先取消它
        if self.timer is not None:
            self.timer.cancel()

        # 打印文件变化日志
        print(f"检测到变化: {event.src_path}")

        # 设置定时任务：等待一段时间后更新
        self.timer = Timer(self.interval, self.update_statistics)
        self.timer.start()

    def update_statistics(self):
        """ 更新统计并执行操作 """
        print("开始更新统计...")
        file_info = scan_directory(self.directory, self.mode)
        print_statistics(file_info, self.save_directory)
        generate_catalog_html(self.directory, "OJ/index.html")




def start_watching(directory, save_directory, interval, mode):
    """ 启动目录监听 """
    event_handler = DirectoryHandler(directory, save_directory, mode, interval)
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=True)
    observer.start()
    print(f"开始监听目录: {directory}，每 {interval} 秒检查一次")

    try:
        while True:
            time.sleep(interval)  # 使用监听间隔时间
    except KeyboardInterrupt:
        observer.stop()
        print("监听停止")
    observer.join()

import os
import json
import re
from datetime import datetime
from collections import defaultdict

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
import os
import json
from datetime import datetime
from collections import defaultdict

def extract_metadata_from_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # 使用正则表达式提取头部信息
        metadata = {}
        import re
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

def scan_markdown_files(directory):
    author_data = defaultdict(list)  # 用一个列表存储每个作者作者的文章信息
    
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
        print("No author data found")
    
    return author_data

def update_json_users(author_data, json_file_path):
    # 检查文件是否存在，并且不是空文件
    if os.path.exists(json_file_path):
        file_size = os.stat(json_file_path).st_size
        if file_size == 0:
            data = {"users": {}}  # 如果文件为空，初始化为默认结构
            print(f"JSON文件为空，初始化为默认结构: {json_file_path}")
        else:
            try:
                # 读取现有的 JSON 数据
                with open(json_file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)  # 尝试加载 JSON 数据
                print(f"成功读取现有 JSON 数据: {json_file_path}")
            except (json.JSONDecodeError, ValueError) as e:
                # 如果 JSON 格式不正确，初始化为默认结构
                print(f"读取 JSON 文件时发生错误，初始化为默认结构: {json_file_path}")
                print(f"详情: {e}")
                data = {"users": {}}  # 格式不正确时使用标准结构
    else:
        data = {"users": {}}  # 如果文件不存在，初始化为空结构
        print(f"JSON 文件不存在，初始化为默认结构: {json_file_path}")

    # 确保 JSON 数据包含 users 键
    if "users" not in data:
        data["users"] = {}

    # 更新每个作者的 posts 部分
    for author, posts in author_data.items():
        # 去掉作者名两端的引号
        author = author.strip('"')  # 去除首尾的引号

        if author not in data["users"]:
            # 如果作者不存在，则创建新作者并初始化 posts 和报告计数
            data["users"][author] = {
                "posts": [],
                "total_report_count_in_all": 0,
                "daily_report_count_in_year": {}  # 修正拼写错误
            }
            print(f"新作者 {author} 已添加到 JSON 数据中")
        
        # 获取当前作者的 posts 列表
        current_posts = data["users"][author].get("posts", [])
        total_report_count_in_all = data["users"][author].get("total_report_count_in_all", 0)
        daily_report_count_in_year = data["users"][author].get("daily_report_count_in_year", {})  # 修正拼写错误
        
        # 合并文章信息到 posts 部分，避免重复
        existing_titles = {post['title'] for post in current_posts}  # 记录已存在文章的标题
        for post in posts:
            # 去掉文章标题两端的引号
            post['title'] = post['title'].strip('"')  # 去除首尾的引号

            # 更新 total_report_count_in_all
            total_report_count_in_all += post['report_count']
            print(f"更新 total_report_count_in_all 为 {total_report_count_in_all} 对于作者 {author}")

            # 更新 daily_report_count_in_year
            date_str = post['date']
            if date_str in daily_report_count_in_year:
                daily_report_count_in_year[date_str] += post['report_count']
                print(f"更新 daily_report_count_in_year 中 {date_str} 的计数为 {daily_report_count_in_year[date_str]} 对于作者 {author}")
            else:
                daily_report_count_in_year[date_str] = post['report_count']
                print(f"新日期 {date_str} 已添加到 daily_report_count_in_year 对于作者 {author}")

        # 如果有新的文章，添加到 posts 中
        new_posts = [post for post in posts if post['title'] not in existing_titles]
        if new_posts:
            current_posts.extend(new_posts)
            data["users"][author]["posts"] = current_posts
            data["users"][author]["total_report_count_in_all"] = total_report_count_in_all
            data["users"][author]["daily_report_count_in_year"] = daily_report_count_in_year
            print(f"新帖子已添加到作者 {author} 的 posts 中")
        else:
            print(f"Skipping duplicate posts for {author}: {posts}")

    # 将更新后的数据写回 JSON 文件
    if data:
        # 使用 ensure_ascii=False 来确保中文字符正常存储
        with open(json_file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f'用户数据已更新到 {json_file_path}')
    else:
        print("No data to update in JSON.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="文件夹统计工具")
    parser.add_argument(
        "-m", "--mode", type=int, choices=[0, 1], default=1,
        help="运行模式：1 为手动扫描模式，0 为实时监听模式（默认: 1）"
    )
    parser.add_argument(
        "-i", "--interval", type=float, default=2.0,
        help="监听间隔时间，仅在 0 模式下有效（单位：秒，默认: 2.0）"
    )
    args = parser.parse_args()

    # 读取 JSON 配置文件
    config = load_config()
    root_directory = config.get("root_directory", "")
    save_directory = config.get("png_save_directory", "")
    
    if not root_directory:
        # 如果为空，使用当前脚本目录作为根目录
        root_directory = os.path.dirname(os.path.abspath(__file__))

    # 拼接根目录路径，将配置中的相对路径与脚本目录拼接
    root_directory = os.path.join( os.getcwd(), root_directory)

    set_chinese_font(config)  # 设置中文字体

    if args.mode == 1:
        print("手动扫描模式")
        file_info = scan_directory(root_directory, args.mode)
        print_statistics(file_info, save_directory)

       
        generate_catalog_html(".", "OJ/index.html")
  

    else:
        print("实时监听模式")
        start_watching(root_directory, save_directory, args.interval, args.mode)
        

    DB_PATH = '../assets/json_Database/Database.json'  # 这里指定 JSON 文件的路径
    
    # 扫描文件并获取按作者分类的文件信息
    author_data = scan_markdown_files(root_directory)
    
    if author_data:
        # 更新用户数据中的作者信息
        update_json_users(author_data, DB_PATH)
    else:
        print("没有扫描到任何文章。")
