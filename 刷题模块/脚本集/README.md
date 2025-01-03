
---

## **项目名称**

Python 脚本，用于分析 Markdown 文件并生成统计图表。支持中文字体配置和定时刷新功能。

---

## **功能**
- 可视化创建博客文件。(markdown)
- 扫描文件夹中的 `.md` 文件，统计 `div1` 到 `div5` 和类型分布。
- 生成柱状图展示统计结果。
- 支持一次性生成数据图，或定时刷新。

---

## **环境要求**

- Python 3.x
  - 安装 `matplotlib`、`keyboard`与 `watchdog`库

---

 ## **安装依赖**

运行以下命令安装依赖：

```
pip install -r requirements.txt
```

或者单独安装 `matplotlib`、`keyboard`与 `watchdog`：

```
pip install matplotlib watchdog keyboard
```

---

## **使用说明**



### **配置文件**：

配置文件 `config.json` 示例：

```json
{
    "root_directory": "..\\..\\",   // 扫描的根目录
    "png_save_directory": "..\\img",     // 保存图表的目录
}
```

---

