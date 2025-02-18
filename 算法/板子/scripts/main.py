import os
import json
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 从配置文件中加载设置
def load_config(config_file):
    with open(config_file, 'r', encoding='utf-8') as f:
        return json.load(f)

# 根据后缀推断 VSCode 需要的 scope（语言标签）
def get_language_from_extension(ext):
    language_map = {
        "py": "python",
        "cpp": "cpp",
        "js": "javascript",
        "html": "html",
        "css": "css",
        "java": "java",
        "json": "json"
    }
    return language_map.get(ext, "plaintext")

# 生成 VSCode snippets（合并所有语言到一个 JSON）
def generate_snippets(directory, file_types):
    snippets = {}

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            name, ext = os.path.splitext(filename)
            ext = ext.lstrip('.')

            if ext not in file_types:
                continue

            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()

            language = get_language_from_extension(ext)
            snippet_key = name  # 使用文件名作为 snippet 名称
            snippet_value = {
                "prefix": name,
                "body": file_content.splitlines(),
                "description": f"Snippet for {name} in {language}",
                "scope": language  # 让 VSCode 只在对应语言的文件中生效
            }

            snippets[snippet_key] = snippet_value

    return snippets

# 保存 snippets 为 VSCode 可识别的 .code-snippets 文件
def save_snippets(snippets, output_file):
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # 确保输出目录存在

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(snippets, file, indent=4, ensure_ascii=False)

    print(f"Snippets saved: {output_file}")

# 监听目录变化的处理类
class SnippetsUpdateHandler(FileSystemEventHandler):
    def __init__(self, config):
        self.config = config

    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"File modified: {event.src_path}")
        self.update_snippets()

    def on_created(self, event):
        if event.is_directory:
            return
        print(f"File created: {event.src_path}")
        self.update_snippets()

    def on_deleted(self, event):
        if event.is_directory:
            return
        print(f"File deleted: {event.src_path}")
        self.update_snippets()

    def update_snippets(self):
        input_directory = self.config["input_directory"]
        output_file = self.config["output_file"]
        file_types = self.config["file_types"]

        snippets = generate_snippets(input_directory, file_types)
        save_snippets(snippets, output_file)

        print(f"Snippets updated and saved in {output_file}")

if __name__ == "__main__":
    config_file = "算法/板子/scripts/_config.json"
    config = load_config(config_file)

    event_handler = SnippetsUpdateHandler(config)
    observer = Observer()
    observer.schedule(event_handler, path=config["input_directory"], recursive=True)

    print(f"Watching for changes in {config['input_directory']}...")
    observer.start()

    try:
        while True:
            time.sleep(1)  # 保持脚本运行
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
