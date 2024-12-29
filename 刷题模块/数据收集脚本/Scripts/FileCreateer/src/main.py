import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import keyboard  # 用于监听快捷键
import threading


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

        with open(file_path, 'w', encoding="utf-8") as file:
            # 只写用户名到文件，格式为 "用户名"
            file.write(f"[{username}]\n")

        messagebox.showinfo("成功", f"文件已创建：{file_path}")
        # 关闭文件创建窗口
        classification_window.quit()

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
    file_name = f"div{difficulty}_{{{';'.join(tags)}}}_{oj}_{question_name}.md"

    # 创建文件，传递用户名
    create_file_in_directory(root_dir, default_folder, file_name, username)  # 只传递需要的 4 个参数


# 弹出分类窗口
def show_classification_window(config):
    # 加载题目信息
    questions_info = load_questions_info()
    if not questions_info:
        return

    global classification_window  # 使分类窗口全局可用
    classification_window = tk.Toplevel(root)
    classification_window.title("选择标签")

    # 获取并显示当前的默认文件夹路径
    current_folder = get_default_folder()
    if current_folder is None:
        return

    folder_label = tk.Label(classification_window, text=f"当前默认文件夹: {current_folder}")
    folder_label.pack(pady=5)

    # 创建浏览文件夹按钮
    def browse_folder():
        new_folder = filedialog.askdirectory(initialdir=current_folder, title="选择文件夹")
        if new_folder:
            folder_input.delete(0, tk.END)
            folder_input.insert(0, new_folder)

            # 更新用户配置中的默认文件夹路径
            update_default_folder(new_folder)

    folder_input = tk.Entry(classification_window, width=50)
    folder_input.insert(0, current_folder)  # 设置当前默认文件夹路径为输入框初始值
    folder_input.pack(pady=10)

    # 创建浏览按钮
    browse_button = tk.Button(classification_window, text="浏览", command=browse_folder)
    browse_button.pack(pady=5)

    # 创建 Canvas 和 Scrollbar
    canvas = tk.Canvas(classification_window)
    scrollbar = tk.Scrollbar(classification_window, orient="vertical", command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)

    # 创建一个Frame来包含标签
    tags_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=tags_frame, anchor="nw")
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # 动态加载标签
    tag_buttons = []
    for idx, tag in enumerate(questions_info.get("tags", [])):
        var = tk.BooleanVar()
        tag_button = tk.Checkbutton(tags_frame, text=tag, variable=var)
        tag_button.grid(row=idx, column=0, padx=10, pady=5, sticky="w")
        tag_buttons.append((tag, var))

    tags_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

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

    confirm_button = tk.Button(classification_window, text="确认", command=on_confirm)
    confirm_button.pack(pady=20)


# 初始化GUI
root = tk.Tk()

# 隐藏主窗口
root.withdraw()

# 创建一个按钮来显示分类选择窗口
open_classification_window_button = tk.Button(root, text="创建新文件", command=lambda: show_classification_window(load_config()))
open_classification_window_button.pack(pady=20)

# 设置快捷键监听
def listen_for_shortcut():
    # 监听 Ctrl+N 快捷键，触发创建新文件按钮的点击事件
    keyboard.add_hotkey('ctrl+d', lambda: open_classification_window_button.invoke())

# 使用线程异步运行快捷键监听，避免阻塞主线程
shortcut_thread = threading.Thread(target=listen_for_shortcut, daemon=True)
shortcut_thread.start()

root.mainloop()