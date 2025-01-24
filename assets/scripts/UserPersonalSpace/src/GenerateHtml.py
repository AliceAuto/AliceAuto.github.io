import os

def generate_html(directory, output_file):

    title = "贡献者"

    # 生成HTML内容
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Directory Listing for {title}</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f4f7fb;
                color: #333;
                margin: 20px;
                line-height: 1.6;
            }}

            h1 {{
                color: #444;
                text-align: center;
                font-size: 2.2em;
                margin-bottom: 20px;
            }}

            /* 列表样式 */
            ul {{
                list-style-type: none;
                padding-left: 0;
                max-width: 800px;
                margin: 0 auto;
            }}

            li {{
                padding: 12px;
                margin: 8px 0;
                background-color: #ffffff;
                border-radius: 8px;
                box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
                transition: background-color 0.3s ease, transform 0.2s ease;
            }}

            li:hover {{
                background-color: #e1f5fe;
                transform: translateX(5px);
            }}

            /* 链接样式 */
            a {{
                text-decoration: none;
                color: #0066cc;
                font-size: 1.1em;
                font-weight: 500;
                transition: color 0.3s ease, text-decoration 0.2s ease;
            }}

            a:hover {{
                color: #005bb5;
                text-decoration: underline;
            }}

            /* 目录项样式 */
            b {{
                font-weight: 600;
                color: #3a3a3a;
            }}

            /* 响应式设计 */
            @media (max-width: 768px) {{
                h1 {{
                    font-size: 1.6em;
                }}

                ul {{
                    padding-left: 20px;
                }}

                li {{
                    padding: 10px;
                    font-size: 1em;
                }}
            }}
        </style>
    </head>
    <body>
        <h1>{title} 团队</h1>
        <ul>
    """

    # 遍历指定目录及其子目录
    for root, dirs, files in os.walk(directory):
        # 遍历并显示子目录
        for dir_name in dirs:
            html_content += "<li><b>{}</b> (directory)</li>".format(dir_name)
        
        # 遍历并显示文件
        for file_name in files:
            file_path = os.path.join(root, file_name)  # 获取文件的完整路径
            
            # 文件名去除.html作为连接title
            link_title = file_name.replace('.html', '')

            html_content += "<li><a href='{}'>{}</a></li>".format(file_path, link_title)

    # 关闭HTML标签
    html_content += """
        </ul>
    </body>
    </html>
    """

    # 将HTML内容写入到输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"HTML directory listing saved to {output_file}")

# 获取当前文件路径
directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 设置目标目录路径
PATH = os.path.join(directory, 'users_html')

# 设置输出的HTML文件路径
output_file = 'index.html'
output_file_path = os.path.join(directory, output_file)

# 调用生成HTML的函数
generate_html(PATH, output_file_path)
