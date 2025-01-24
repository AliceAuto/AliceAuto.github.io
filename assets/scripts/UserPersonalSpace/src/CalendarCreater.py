from datetime import datetime
import calendar
import json
import os
# 生成对应 user 的 HTML 文件
def generate_calendar_html(user):
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
        ._UserActivityFrame_countersRow {{
            display: inline-block;
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
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            transition: transform 0.2s, background-color 0.2s;
        }}
        .blog-button:hover {{
            background-color: #0056b3;
            transform: scale(1.05);  /* 按钮放大效果 */
        }}
        .blog-button:active {{
            background-color: #003f7f;
            transform: scale(1.1);  /* 按钮点击时的放大效果 */
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

    # 读取JSON文件
    def read_json_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    # 获取脚本的当前路径
    import os
    current_path = os.path.dirname(os.path.abspath(__file__))
    parent_path = os.path.dirname(current_path)
    file_path = os.path.join(parent_path, "data", "users_data.json")
    users_data = read_json_file(file_path)

    # 获取用户数据
 
    user_data = users_data.get(user, {})

    # 获取博客数据
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

    # 保存HTML文件
    folder_path = os.path.join(parent_path, "users_html")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    with open(os.path.join(folder_path, user + ".html"), "w", encoding="utf-8") as f:
        f.write(html)

# 调
# 读取 JSON 文件
def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# 获取用户数据
def process_all_users():
    current_path = os.path.dirname(os.path.abspath(__file__))
    parent_path = os.path.dirname(current_path)
    file_path = os.path.join(parent_path, "data", "users_data.json")
    users_data = read_json_file(file_path)
    
    
    
    # 遍历所有用户生成 HTML
    for user, user_data in users_data.items():
        print(f"为{user}生成个人空间")
        generate_calendar_html(user)
process_all_users()