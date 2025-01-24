import json
import os
import sys

# 获得当前脚本的所在目录
MAIN_DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'Database.json')


def get_json_data(file_path, json_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    keys = json_path.split('.')
    for key in keys:
        if key.isdigit():
            data = data[int(key)]
        else:
            data = data[key]
    return data


def update_json_data(file_path, json_path, temp_json_path):
    if not isinstance(file_path, str) or not isinstance(temp_json_path, str):
        print("文件路径必须是字符串类型")
        return
    try:
        # 读取原始数据库文件
        with open(file_path, 'r') as file:
            data = json.load(file)
        print(f"原始数据: {data}")  # 打印原始数据

        # 解析路径
        keys = json_path.split('.')
        current_data = data

        # 遍历路径的每一部分，创建缺失的部分
        for key in keys[:-1]:
            if key.isdigit():  # 数字是数组索引
                key = int(key)
                if isinstance(current_data, list):
                    # 扩展列表至足够的长度
                    while len(current_data) <= key:
                        current_data.append({})
                else:
                    # 如果当前节点不是列表，报错
                    print(f"路径错误: 预期是列表，但找到了 {type(current_data)}")
                    return
                current_data = current_data[key]
            else:
                if key not in current_data:
                    current_data[key] = {}  # 创建空字典
                current_data = current_data[key]

        # 获取目标字段的最后部分
        last_key = keys[-1]
        print(f"最终路径的键: {last_key}")

        # 从临时文件读取新值
        try:
            with open(temp_json_path, 'r') as temp_file:
                new_value = json.load(temp_file)
            print(f"从临时文件读取的新值: {new_value}")  # 打印新值

            # 更新数据
            if last_key.isdigit():
                current_data[int(last_key)] = new_value
            else:
                current_data[last_key] = new_value
        except FileNotFoundError:
            print(f"临时文件未找到: {temp_json_path}")
            return

        # 保存更新后的数据
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"更新后的数据: {data}")  # 打印更新后的数据

    except FileNotFoundError:
        print(f"文件未找到: {file_path}")
        return


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("请提供三个参数：读写模式、键、临时JSON文件位置")
        sys.exit(1)

    mode = sys.argv[1].lower()
    json_key = sys.argv[2]
    temp_json_path = sys.argv[3]

    if mode == "r":
        # 获取数据
        try:
            extracted_data = get_json_data(MAIN_DATABASE_PATH, json_key)
            with open(temp_json_path, 'w') as file:
                json.dump(extracted_data, file, indent=4)
            print(f"数据已保存到 {temp_json_path}")
        except Exception as e:
            print(f"读取数据时出错: {e}")
    elif mode == "w":
        # 从临时JSON文件中读取新值
        try:
            new_value = None
            with open(temp_json_path, 'r') as file:
                new_value = json.load(file)
            update_json_data(MAIN_DATABASE_PATH, json_key, temp_json_path)
            print(f"数据已更新到 {MAIN_DATABASE_PATH}")
        except Exception as e:
            print(f"更新数据时出错: {e}")
    else:
        print("无效的操作模式，请选择读取或更新。")
