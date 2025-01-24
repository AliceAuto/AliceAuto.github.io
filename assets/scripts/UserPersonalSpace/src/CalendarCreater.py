from datetime import datetime
import calendar
import json
import os
# 生成对应 user 的 HTML 文件
def generate_calendar_html(user,user_data):

    # 导入必要的库
    import calendar
    year = datetime.now().year
    # 定义 HTML 模板
    html_template = """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
       <style>
        .box-container {{
            display: flex;
            background-color: #f8f8f8; /* 更柔和的背景色 */
            padding: 10px;
            border-top: 1px solid #ddd; /* 更柔和的边框颜色 */
        }}
        ._UserActivityFrame_header {{
            background-color: #f8f8f8; /* 更柔和的背景色 */
            padding: 10px;
            border-bottom: 1px solid #ddd; /* 更柔和的边框颜色 */
        }}
        ._UserActivityFrame_body {{
            background-color: #f8f8f8; /* 更柔和的背景色 */
            padding: 10px;
            border-bottom: 1px solid #ddd; /* 更柔和的边框颜色 */
        }}
        ._UserActivityFrame_footer {{
            background-color: #f8f8f8; /* 更柔和的背景色 */
            padding: 10px;
            border-bottom: 1px solid #ddd; /* 更柔和的边框颜色 */
        }}
        ._UserActivityFrame_countersRow {{
   
            padding: 10px;
        }}
        ._UserActivityFrame_counter {{
            border: 1px solid #ddd; /* 更柔和的边框颜色 */
            padding: 5px;
            background-color: #fff; /* 白色背景 */
            border-radius: 5px; /* 圆角边框 */
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 轻微阴影 */
        }}
        ._UserActivityFrame_counterValue {{
            color: #333; /* 深灰色文本 */
            font-weight: bold; /* 加粗文本 */
        }}
        ._UserActivityFrame_counterDescription {{
            color: #666; /* 中灰色文本 */
        }}
        .blog-directory {{
            margin-top: 20px;
        }}
        .blog-post {{
            padding: 10px;
            border: 1px solid #ddd;
            margin-bottom: 10px;
            border-radius: 5px;
            background-color: #f9f9f9;
        }}
         .blog-button {{
        padding: 12px 24px;  /* 按钮内边距 */
        background: linear-gradient(135deg, #6e7aee, #4e61b2); /* 渐变背景色 */
        color: white;  /* 字体颜色 */
        border: none;  /* 去掉边框 */
        border-radius: 8px;  /* 圆角边框 */
        font-size: 16px;  /* 字体大小 */
        cursor: pointer;  /* 鼠标悬停时变成指针 */
        transition: all 0.3s ease;  /* 过渡效果 */
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);  /* 按钮阴影 */
        text-decoration: none; /* 去掉链接下划线 */
    }}

    .blog-button:hover {{
        background: linear-gradient(135deg, #4e61b2, #6e7aee); /* 悬停时改变背景色 */
        transform: scale(1.05);  /* 放大效果 */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);  /* 更强的阴影效果 */
    }}

    .blog-button:active {{
        background: #2f3d8a;  /* 点击时的背景色 */
        transform: scale(0.98);  /* 按钮点击时缩小 */
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);  /* 还原阴影 */
    }}
        </style>
    </head>
    <body>
    
    <div class="_UserActivityFrame_header xh-highlight">
        <div class="_UserActivityFrame_title" style="text-align: center;">
            <div class="_UserActivityFrame_titleText" style="font-weight: bold;">{}的个人空间</div>
        </div>
    </div>
    <div class="_UserActivityFrame_body xh-highlight">
        <!-- 日历部分内容 -->
        <svg xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMinYMin meet" viewBox="0 0 721 110">
            <g transform="translate(25, 20)">
                {}
                <text x="13" y="-5" class="month">Feb</text><text x="66" y="-5" class="month">Mar</text>
                <text x="130" y="-5" class="month">Apr</text><text x="182" y="-5" class="month">May</text>
                <text x="234" y="-5" class="month">Jun</text><text x="299" y="-5" class="month">Jul</text>
                <text x="351" y="-5" class="month">Aug</text><text x="403" y="-5" class="month">Sep</text>
                <text x="468" y="-5" class="month">Oct</text><text x="520" y="-5" class="month">Nov</text>
                <text x="572" y="-5" class="month">Dec</text><text x="637" y="-5" class="month">Jan</text>
                <text text-anchor="middle" class="wday" dx="-13" dy="22">Mon</text><text text-anchor="middle" class="wday" dx="-13" dy="44">Wed</text>
                <text text-anchor="middle" class="wday" dx="-13" dy="74">Fri</text>
            </g>
        </svg>
    </div>
    <div class="_UserActivityFrame_footer xh-highlight">
        <div class="box-container">
            <div class="_UserActivityFrame_countersRow">
                <div class="_UserActivityFrame_counter">
                    <div class="_UserActivityFrame_counterValue">{} 篇</div>
                    <div class="_UserActivityFrame_counterDescription">总文章数</div>
                </div>
            </div>
            <div class="_UserActivityFrame_countersRow">
                <div class="_UserActivityFrame_counter">
                    <div class="_UserActivityFrame_counterValue">{} 天</div>
                    <div class="_UserActivityFrame_counterDescription">最多连续打卡</div>
                </div>
            </div>
        </div>
        <!-- 个人博客目录部分 -->
        <div class="blog-directory">
            <h3>个人博客目录</h3>
            {}
        </div>
    </div>
    </body>
    </html>
    """


    # 定义每个周的HTML模板
    week_template = """<g transform="translate({},0)">
        {}
    </g>
    """
    # 定义每个日期的HTML模板
    day_template = """<rect class="day" width="11" height="11" y="{}" fill="{}" data-item="{}" data-date="{}"></rect>"""

   
    posts = user_data.get("posts", [])

    # 生成博客目录HTML
    blog_posts_html = ""
    for post in posts:
        
        blog_posts_html += f"""
        <div class="blog-post">
            <button class="blog-button" onclick="window.location.href='{post.get('link', '#')}'">
                {post.get('title', '无标题')}
            </button>
        </div>
        """


    # 获取每日报告数据
    daily_report_count_in_year = user_data.get("daliy_report_count_in_year", {})
    total_report_count_in_all = user_data.get("total_report_count_in_all", 0)
    
    # 计算连续天数的最大值
    max_consecutive_days = 0
    current_consecutive_days = 0
    for date, count in daily_report_count_in_year.items():
        if count > 0:
            current_consecutive_days += 1
            max_consecutive_days = max(max_consecutive_days, current_consecutive_days)
        else:
            current_consecutive_days = 0

    # 生成每个日期的HTML
    weeks_each_year = []
    first_day_of_year = datetime(year, 1, 1).weekday()
    day_in_year_cnt = first_day_of_year
    days_each_week = []
    for month in range(1, 13):
        cal = calendar.monthcalendar(year, month)
        for week in cal:
            for day in week:
                if day != 0:
                    if day_in_year_cnt % 7 == 0:
                        days_each_week.clear()
                    date = datetime(year, month, day).strftime("%m/%d/%Y")
                    y = (day_in_year_cnt % 7) * 13
                    daily_data = user_data.get("daliy_report_count_in_year", {}).get(date, 0)
                    
                    # 根据每日数据设置颜色,逐渐变绿
                    if daily_data == 0:#浅灰色
                        color = "#f2f2f2"
                    elif daily_data == 1:#浅绿色
                        color = "#d4edda"
                    elif daily_data == 2:#深一点的绿色
                        color = "#c3e6cb"
                    elif daily_data == 3:#深绿色
                        color = "#a3c2c2"
                    elif daily_data == 4:#深一点的绿色
                        color = "#85adad"
                    elif daily_data == 5:#深绿色
                        color = "#669696"
                    elif daily_data == 6:#深绿色
                        color = "#4c7878"
                    elif daily_data == 7:#深绿色
                        color = "#354c5c"
                    elif daily_data == 8:#深绿色
                        color = "#2a3f44"
                    elif daily_data == 9:#深绿色
                        color = "#202b33"
                    elif daily_data == 10:#深绿色
                        color = "#151a20"
                    elif daily_data == 11:#深绿色
                        color = "#0a0d10"
                    elif daily_data == 12:#深绿色
                        color = "#000000"
                    else:#深绿色
                        color = "#000000"
                    days_each_week.append(day_template.format(y, color, daily_data, date))
                    day_in_year_cnt += 1
            if days_each_week:
                str_week_str = ''.join(days_each_week)
                weeks_each_year.append(week_template.format((day_in_year_cnt // 7) * 13, str_week_str))

    # 生成完整的HTML
    html = html_template.format(user, ''.join(weeks_each_year), total_report_count_in_all, max_consecutive_days, blog_posts_html)
    parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 保存HTML文件
    folder_path = os.path.join(parent_path, "users_html")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    #去除""
    
    with open(os.path.join(folder_path, user + ".html"), "w", encoding="utf-8") as f:
        f.write(html)


def generate_html(root_path,directory, output_file):

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
            # 获得相对路径
            file_relative_path = os.path.relpath(file_path, root_path)
            html_content += "<li><a href='{}'>{}</a></li>".format(file_relative_path, link_title)

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

#数据库路径常量
DB_PATH = "assets/json_Database/Database.json"
parent_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.join(parent_path, "..","..","..","..")
DB_PATH = os.path.join(parent_path, DB_PATH)

# 读取 JSON 数据
with open(DB_PATH, "r",encoding= "utf-8") as file:
    data = json.load(file)

# 获取所有用户
users = data['users']

# 遍历每个用户并生成对应的 HTML
for username, user_data in users.items():
    print(f"Generating calendar for user: {username}")
    
    # 调用你已经实现的 generate_calendar_html 函数来生成用户的 HTML
    generate_calendar_html(username, user_data)
    
    print(f"Generated calendar for {username}")
#=============================================================

#获得根目录
directory = os.path.dirname(os.path.abspath(__file__))
directory = os.path.join(directory, "..","..","..","..")
# 设置目标目录路径
PATH = os.path.join(directory, "assets","scripts","UserPersonalSpace","users_html")

# 设置输出的HTML文件路径
output_path = os.path.join(directory, "assets","scripts","UserPersonalSpace","index.html")

# 调用生成HTML的函数
generate_html(directory,PATH, output_path)