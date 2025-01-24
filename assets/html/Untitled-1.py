from datetime import datetime
import calendar

def generate_calendar_html(year):
    # 导入必要的库
    import calendar
    
    # 定义HTML模板
    html_template = """
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
    </g>"Your browser does not support inline SVG."
</svg>
    """

    # 定义每个周的HTML模板
    week_template = """
    <g transform="translate({},{})">
        {}
    </g>
    """

    # 定义每个日期的HTML模板
    day_template = """<rect class="day" width="11" height="11" x="{}" y="{}" fill="{}" data-items="{}" data-date="{}"></rect>"""

    # 生成每个日期的HTML
    weeks_each_year = []  # 记录每年的周HTML
    week_counter = 0  # 记录第几周
    day_in_year_cnt = 0  # 标记每周周几
    
    # 遍历一年的每个月份
    for month in range(1, 13):
        cal = calendar.monthcalendar(year, month)

        # 遍历每个月的每个周
        for week in cal:
            days_each_week = []  # 记录每周的日期HTML
            day_in_week_cnt = 0  # 标记每周周几
        
            # 遍历每一天
            for day in week:
                if day !=0:
                    date = datetime(year, month, day).strftime("%m/%d/%Y")  # 格式化日期
                    y = day_in_week_cnt * 13  # 13为每个日期的宽度
                    x = (week_counter % 4) * 26  # 26为每个周的高度
                    # 绿色
                    color = "#EBEDF0" # 标记是否为工作日
                    days_each_week.append(day_template.format(x, y, color, 0, date))  # 加入日期的HTML模板
                    day_in_week_cnt += 1

            if days_each_week:
                str_week_str = ''.join(days_each_week)  # 转换为字符串
                weeks_each_year.append(week_template.format(week_counter * 13, 0, str_week_str))  # 加入周的HTML模板
                week_counter += 1

   

    # 生成完整的HTML
    html = html_template.format(''.join(weeks_each_year))

    # 将生成的HTML保存到文件
    with open('assets/html/calendar.html', 'w') as file:
        file.write(html)

    return html

# 调用函数生成HTML
year = datetime.now().year
html = generate_calendar_html(year)

# 打印生成的HTML
print(html)
