import datetime

# 获取当前日期
current_date = datetime.date.today()
current_year = current_date.year
current_month = current_date.month

# 计算某月份有多少天
def days_in_month(year, month):
    if month == 12:
        return (datetime.date(year + 1, 1, 1) - datetime.date(year, month, 1)).days
    else:
        return (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days

# 生成日历表格
def generate_calendar(year, month):
    days_in_month_value = days_in_month(year, month)
    start_day = datetime.date(year, month, 1).weekday()

    svg = []
    x = 25
    y = 20
    day = 1

    for i in range(7):
        for j in range(7):
            if day > days_in_month_value:
                break

            if i == 0 and j < start_day:
                # 跳过不需要的日期
                rect = f'<rect class="day" width="11" height="11" x="{x}" y="{y}" fill="#EBEDF0" data-items="" data-date=""></rect>'
            else:
                rect = f'<rect class="day" width="11" height="11" x="{x}" y="{y}" fill="#EBEDF0" data-items="" data-date="{year}-{month + 1}-{day}"></rect>'
                day += 1

            svg.append(rect)
            x += 13

        x = 25
        y += 13

    return '\n'.join(svg)

# 调用函数生成当前月份的日历
calendar_svg = generate_calendar(current_year, current_month)

# 将生成的SVG内容插入到HTML文件中
with open('d:/AcEasy/assets/html/签到表.html', 'r+', encoding='utf-8') as file:
    content = file.read()
    svg_start = content.find('<svg')
    svg_end = content.find('</svg>') + len('</svg>')
    new_content = content[:svg_start] + '<svg xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMinYMin meet" viewBox="0 0 721 110">\n' + calendar_svg + '\n</svg>' + content[svg_end:]
    file.seek(0)
    file.write(new_content)
    file.truncate()
