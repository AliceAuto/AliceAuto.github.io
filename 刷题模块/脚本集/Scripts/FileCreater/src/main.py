import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import keyboard  # 用于监听快捷键
import threading
from tkinter import simpledialog


# 获取配置文件的路径并加载配置
def load_config():
    try:
        config_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "config.json")

        if not os.path.isfile(config_path):
            messagebox.showerror("错误", f"配置文件不存在: {config_path}")
            return None

        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        return config
    except Exception as e:
        messagebox.showerror("错误", f"无法加载配置文件: {e}")
        return None

def get_full_path_from_config(config, subfolder):
    try:
        root_path = config.get("root_directory", "")
        if not root_path:
            messagebox.showerror("错误", "配置中缺少根目录路径")
            return None
        return os.path.join(root_path, subfolder)
    except Exception as e:
        messagebox.showerror("错误", f"获取根目录路径时发生错误: {e}")
        return None


# 加载题目信息文件
def load_questions_info():
    try:
        questions_info_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "questions_info.json")

        if not os.path.isfile(questions_info_path):
            messagebox.showerror("错误", f"题目信息文件不存在: {questions_info_path}")
            return None

        with open(questions_info_path, "r", encoding="utf-8") as f:
            questions_info = json.load(f)

        return questions_info
    except Exception as e:
        messagebox.showerror("错误", f"无法加载题目信息文件: {e}")
        return None


# 获取当前用户的名称
def get_current_user():
    try:
        current_user_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "currentUser.json")

        if not os.path.isfile(current_user_path):
            messagebox.showerror("错误", f"当前用户文件不存在: {current_user_path}")
            return None

        with open(current_user_path, "r", encoding="utf-8") as f:
            user_config = json.load(f)
            username = user_config.get("username", "")
        return username
    except Exception as e:
        messagebox.showerror("错误", f"读取当前用户文件时发生错误: {e}")
        return None


# 获取当前用户的默认文件夹路径
def get_default_folder():
    try:
        current_user_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "currentUser.json")

        if not os.path.isfile(current_user_path):
            messagebox.showerror("错误", f"当前用户的配置文件不存在: {current_user_path}")
            return None

        with open(current_user_path, "r", encoding="utf-8") as f:
            user_config = json.load(f)

        return user_config.get("default_folder", "")
    except Exception as e:
        messagebox.showerror("错误", f"读取用户配置文件时发生错误: {e}")
        return None


# 更新默认文件夹路径
def update_default_folder(new_folder_path):
    try:
        current_user_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "currentUser.json")

        if not os.path.isfile(current_user_path):
            messagebox.showerror("错误", f"当前用户的配置文件不存在: {current_user_path}")
            return

        with open(current_user_path, "r+", encoding="utf-8") as f:
            user_config = json.load(f)
            user_config["default_folder"] = new_folder_path

            f.seek(0)  # 回到文件开头
            json.dump(user_config, f, ensure_ascii=False, indent=4)
            f.truncate()  # 删除原文件中的额外内容

        messagebox.showinfo("成功", f"默认文件夹路径已更新为：{new_folder_path}")
    except Exception as e:
        messagebox.showerror("错误", f"更新用户配置时发生错误: {e}")


# 创建文件的函数，只写用户名
import os
from tkinter import messagebox
from datetime import datetime

import os
from tkinter import messagebox
from datetime import datetime

import os
from datetime import datetime
from tkinter import messagebox

import os
from datetime import datetime
from tkinter import messagebox

import os
from datetime import datetime
from tkinter import messagebox

import os
from datetime import datetime
from tkinter import messagebox

def create_file_in_directory(root_dir, subfolder, file_name, username):
    try:
        # 如果选择了子文件夹，构造完整路径
        folder_path = os.path.join(root_dir, subfolder)
        if not os.path.isdir(folder_path):
            os.makedirs(folder_path)  # 如果子文件夹不存在，则创建

        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            messagebox.showerror("错误", f"文件已存在：{file_path}")
            return

        # 获取当前日期并格式化为 YYYY-MM-DD
        current_date = datetime.now().strftime("%Y-%m-%d")

        # 使用文件名或当前日期来动态生成 permalink
        # 构造相对路径，相对于刷题模块根目录
        relative_path = os.path.relpath(file_path, root_dir)  # 计算相对路径
        permalink = f"/{relative_path.replace(os.sep, '/')}/"  # 替换路径分隔符为 "/"

        # 从文件名中提取题目名称作为 title
        # 倒数第一个"_"后的部分到".md"之前的部分
        base_name = file_name.replace('.md', '')  # 去掉文件扩展名
        title = base_name.rsplit('_', 1)[-1]  # 提取倒数第一个"_"后的部分作为标题

        with open(file_path, 'w', encoding="utf-8") as file:
            # 写入 Front Matter 信息，包括作者字段、实时日期和动态链接
            file.write(f"---\n")
            file.write(f"layout: post\n")
            file.write(f"title: \"{title}\"\n")  # 使用提取的标题
            file.write(f"permalink: {permalink[3::]}\n")  # 使用动态生成的相对 permalink
            file.write(f"date: {current_date}\n")  # 使用实时日期
            file.write(f"author: \"{username}\"\n")
            file.write(f"---\n\n")
            file.write("#### [备用返回通道](../../README.md)\n")  # 可以根据需要填充更多内容

        messagebox.showinfo("成功", f"文件已创建：{file_path}")
        

    except Exception as e:
        messagebox.showerror("错误", f"创建文件时发生错误：{e}")


# 获取目标文件的路径并执行创建操作
def execute_file_creation(config, tags, difficulty, oj, default_folder, question_name):
    username = get_current_user()
    if not username:
        return

    root_dir = get_full_path_from_config(config, "")
    if not root_dir:
        return

    # 使用默认文件夹路径
    folder_path = os.path.join(root_dir, default_folder)

    # 构造文件名，问题名称放在文件名中
    file_name = f"{difficulty}_{{{';'.join(tags)}}}_{oj}_{question_name}.md"

    # 创建文件，传递用户名
    create_file_in_directory(root_dir, default_folder, file_name, username)  # 只传递需要的 4 个参数

# 检查并初始化 currentUser.json 文件
def check_and_initialize_user():
    current_user_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "currentUser.json")
    
    # 如果文件不存在，弹出窗口让用户输入信息
    if not os.path.isfile(current_user_path):
        # 创建输入框让用户输入用户名和默认文件夹路径
        username = simpledialog.askstring("输入用户名", "请输入用户名：")
        if not username:
            messagebox.showerror("错误", "用户名不能为空")
            return None, None  # 返回 None 表示失败
        
        # 用户输入默认文件夹路径
        default_folder = filedialog.askdirectory(title="选择默认文件夹")
        if not default_folder:
            messagebox.showerror("错误", "请选择一个默认文件夹")
            return None, None
        
        # 创建并写入 currentUser.json
        user_config = {
            "username": username,
            "default_folder": default_folder
        }

        try:
            with open(current_user_path, "w", encoding="utf-8") as f:
                json.dump(user_config, f, ensure_ascii=False, indent=4)
            messagebox.showinfo("成功", "用户信息已初始化")
            return username, default_folder
        except Exception as e:
            messagebox.showerror("错误", f"创建用户信息时发生错误: {e}")
            return None, None
    
    # 如果文件已经存在，直接读取
    try:
        with open(current_user_path, "r", encoding="utf-8") as f:
            user_config = json.load(f)
            username = user_config.get("username", "")
            default_folder = user_config.get("default_folder", "")
            return username, default_folder
    except Exception as e:
        messagebox.showerror("错误", f"读取用户信息时发生错误: {e}")
        return None, None


# 获取配置文件路径
def load_config():
    try:
        config_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "config.json")
        
        if not os.path.isfile(config_path):
            messagebox.showerror("错误", f"配置文件不存在: {config_path}")
            return None
        
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        return config
    except Exception as e:
        messagebox.showerror("错误", f"无法加载配置文件: {e}")
        return None


# 在现有主窗口按钮下方添加管理标签按钮
def show_tag_management_window():
    management_window = tk.Toplevel(root)
    management_window.title("标签管理")
    
    # 新增标签输入框
    new_tag_label = tk.Label(management_window, text="输入新标签")
    new_tag_label.pack(pady=5)
    
    new_tag_entry = tk.Entry(management_window, width=30)
    new_tag_entry.pack(pady=10)
    
    # 确认添加按钮
    def add_new_tag():
        new_tag = new_tag_entry.get()
        if not new_tag:
            messagebox.showerror("错误", "标签内容不能为空")
            return
        
        # 加载现有标签配置
        questions_info_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "questions_info.json")
        try:
            with open(questions_info_path, "r+", encoding="utf-8") as f:
                data = json.load(f)
                if new_tag in data["tags"]:
                    messagebox.showerror("错误", "标签已存在")
                    return
                
                data["tags"].append(new_tag)
                f.seek(0)
                json.dump(data, f, ensure_ascii=False, indent=4)
                f.truncate()
            
            messagebox.showinfo("成功", f"已添加新标签: {new_tag}")
            management_window.destroy()
        except Exception as e:
            messagebox.showerror("错误", f"保存标签失败: {e}")

    add_button = tk.Button(management_window, text="添加标签", command=add_new_tag)
    add_button.pack(pady=20)

# 弹出分类窗口
def show_classification_window(config):
    # 检查并初始化用户信息
    username, default_folder = check_and_initialize_user()
    if not username or not default_folder:
        return
    
    # 加载题目信息
    questions_info = load_questions_info()
    if not questions_info:
        return

    global classification_window  # 使分类窗口全局可用
    classification_window = tk.Toplevel(root)
    classification_window.title("选择标签")

    # 获取并显示当前的默认文件夹路径
    folder_label = tk.Label(classification_window, text=f"当前默认文件夹: {default_folder}")
    folder_label.pack(pady=5)

    # 创建浏览文件夹按钮
    def browse_folder():
        new_folder = filedialog.askdirectory(initialdir=default_folder, title="选择文件夹")
        if new_folder:
            folder_input.delete(0, tk.END)
            folder_input.insert(0, new_folder)

            # 更新用户配置中的默认文件夹路径
            update_default_folder(new_folder)

    folder_input = tk.Entry(classification_window, width=50)
    folder_input.insert(0, default_folder)  # 设置当前默认文件夹路径为输入框初始值
    folder_input.pack(pady=10)

    # 创建浏览按钮
    browse_button = tk.Button(classification_window, text="浏览", command=browse_folder)
    browse_button.pack(pady=5)

    # 在搜索框下方添加新增标签按钮
    def refresh_tags():
        nonlocal all_tags
        questions_info = load_questions_info()
        all_tags = questions_info.get("tags", [])
        update_tags()
    
    add_tag_button = tk.Button(classification_window, text="＋ 新增标签", 
                              command=lambda: [show_tag_management_window(), 
                                              classification_window.after(500, refresh_tags)])
    add_tag_button.pack(pady=10)
    
    # 创建 Canvas 和 Scrollbar
    canvas = tk.Canvas(classification_window)
    scrollbar = tk.Scrollbar(classification_window, orient="vertical", command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)

    # 创建一个Frame来包含标签
    tags_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=tags_frame, anchor="nw")
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # 创建搜索框
    search_label = tk.Label(classification_window, text="搜索标签")
    search_label.pack(pady=5)

    search_var = tk.StringVar()
    search_entry = tk.Entry(classification_window, textvariable=search_var, width=50)
    search_entry.pack(pady=5)

    # 动态加载标签
    tag_buttons = []
    all_tags = questions_info.get("tags", [])

    # 定义更新标签显示的函数
    def update_tags(*args):
        search_term = search_var.get().lower()  # 获取搜索框中的内容，并转为小写
        for widget in tags_frame.winfo_children():
            widget.destroy()  # 清空标签框

        for idx, tag in enumerate(all_tags):
            if search_term in tag.lower():  # 过滤标签
                var = tk.BooleanVar()
                tag_button = tk.Checkbutton(tags_frame, text=tag, variable=var)
                tag_button.grid(row=idx, column=0, padx=10, pady=5, sticky="w")
                tag_buttons.append((tag, var))

        tags_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    # 监听搜索框内容变化
    search_var.trace_add("write", update_tags)

    # 初始加载标签
    update_tags()

    # 创建OJ下拉框
    oj_label = tk.Label(classification_window, text="选择OJ")
    oj_label.pack(pady=5)

    oj_combobox = ttk.Combobox(classification_window, values=questions_info.get("oj", []))
    oj_combobox.set(questions_info.get("oj", [])[0])  # 默认选第一个OJ
    oj_combobox.pack(pady=5)

    # 创建难度下拉框
    difficulty_label = tk.Label(classification_window, text="选择难度")
    difficulty_label.pack(pady=5)

    difficulty_combobox = ttk.Combobox(classification_window, values=questions_info.get("difficulty", []))
    difficulty_combobox.set(questions_info.get("difficulty", [])[0])  # 默认选第一个难度
    difficulty_combobox.pack(pady=5)

    # 创建题目名称输入框
    question_name_label = tk.Label(classification_window, text="输入题目名称")
    question_name_label.pack(pady=5)

    question_name_entry = tk.Entry(classification_window, width=50)
    question_name_entry.pack(pady=10)

    # 确认按钮
    def on_confirm():
        tags = [tag for tag, var in tag_buttons if var.get()]
        difficulty = difficulty_combobox.get()
        oj = oj_combobox.get()
        question_name = question_name_entry.get()

        execute_file_creation(config, tags, difficulty, oj, folder_input.get(), question_name)
        classification_window.withdraw()  # 隐藏分类窗口

    confirm_button = tk.Button(classification_window, text="确认", command=on_confirm)
    confirm_button.pack(pady=20)


# 初始化GUI
root = tk.Tk()

# 隐藏主窗口
root.withdraw()

# 创建一个按钮来显示分类选择窗口
open_classification_window_button = tk.Button(root, text="创建新文件", command=lambda: show_classification_window(load_config()))
# 修改主窗口布局，在原有按钮下添加管理标签按钮
open_classification_window_button.pack(pady=20)
tk.Button(root, text="管理标签", command=show_tag_management_window).pack(pady=10)

# 设置快捷键监听
def listen_for_shortcut():
    # 监听 Ctrl+N 快捷键，触发创建新文件按钮的点击事件
    keyboard.add_hotkey('ctrl+d', lambda: open_classification_window_button.invoke())

# 使用线程异步运行快捷键监听，避免阻塞主线程
shortcut_thread = threading.Thread(target=listen_for_shortcut, daemon=True)
shortcut_thread.start()

root.mainloop()