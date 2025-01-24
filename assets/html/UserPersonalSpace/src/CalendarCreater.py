from datetime import datetime
import calendar
import json

#生成对应 user的html文件
def generate_calendar_html(user):
    # 导入必要的库
    import calendar
    year = datetime.now().year
    # 定义HTML模板
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
        </style>
    </head>
    <div class="_UserActivityFrame_header xh-highlight">
        <div class="_UserActivityFrame_title" style="text-align: center;">
            <div class="_UserActivityFrame_titleText" style="font-weight: bold;">{}的个人空间</div>
        </div>
    </div>
    <div class="_UserActivityFrame_body xh-highlight">
    
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
                <div class="_UserActivityFrame_counterDescription">
                    总文章数
                </div>
            </div>
        </div>
    
        <div class="_UserActivityFrame_countersRow">
            <div class="_UserActivityFrame_counter">
                <div class="_UserActivityFrame_counterValue">{} 天</div>
                <div class="_UserActivityFrame_counterDescription">
                    最多连续打卡.
                </div>
            </div>
        </div>
        </div>
    </div>
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
    # 假设您已经有了一个函数来读取JSON数据
    # 读取JSON文件时指定编码
    def read_json_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    
    #获得脚本的当前路径
    import os
    current_path = os.path.dirname(os.path.abspath(__file__))
    #获得父级路径
    parent_path = os.path.dirname(current_path)
    # 在路径下找到data文件夹中的users_data.json文件
    file_path = os.path.join(parent_path, "data", "users_data.json")
    json_data = read_json_file(file_path)
    
    # 获取用户数据
    user_data = json_data.get(user, {})
    
    # 获取每日报告数据
    daily_report_count_in_year = user_data.get("daliy_report_count_in_year", {})
    total_report_count_in_all = user_data.get("total_report_count_in_all", {})
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
    weeks_each_year = []  # 记录每年的周HTML
    first_day_of_year = datetime(year, 1, 1).weekday()  # 返回的是0（星期一）到6（星期日）
    day_in_year_cnt = first_day_of_year  # 计数一年的第几天
    days_each_week = []  # 开始的一周
    # 遍历一年的每个月份
    for month in range(1, 13):
        cal = calendar.monthcalendar(year, month)

        # 遍历每个月的每个周
        for week in cal:
            # 遍历每一天
            for day in week:
                if day != 0:
                
                    if day_in_year_cnt % 7 == 0:  # 星期一
                        days_each_week.clear()  # 清空上一周的日期
                    date = datetime(year, month, day).strftime("%m/%d/%Y")  # 格式化日期
                    y = (day_in_year_cnt % 7) * 13  # 13为每个日期的宽度
                    
                    # 从JSON数据中获取每日数据
                    daily_data = user_data.get("daliy_report_count_in_year",{}).get(date, 0)   # 假设默认值为0
                 
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
                    days_each_week.append(day_template.format(y, color, daily_data, date))  # 加入日期的HTML模板
                    day_in_year_cnt += 1

            if days_each_week:
                str_week_str = ''.join(days_each_week)  # 转换为字符串
                weeks_each_year.append(week_template.format((day_in_year_cnt // 7) * 13, str_week_str))  # 加入周的HTML模板

    # 生成完整的HTML
    html = html_template.format(user,''.join(weeks_each_year), total_report_count_in_all, max_consecutive_days)

    #获得当前文件的路径
    import os
    current_path = os.path.abspath(__file__)
    #获得爷级目录的路径
    parent_path = os.path.dirname(os.path.dirname(current_path))
    
    folder_path = os.path.join(parent_path, "users_html")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        # 保存HTML文件
    with open(os.path.join(folder_path, user + ".html"), "w", encoding="utf-8") as f:
        f.write(html)
# 调用函数生成HTML

html = generate_calendar_html("Tester")

# 打印生成的HTML
## print(html)
