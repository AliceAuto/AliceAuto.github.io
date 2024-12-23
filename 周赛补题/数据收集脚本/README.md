
---

**项目名称**

Python 脚本，用于分析 Markdown 文件并生成统计图表。支持中文字体配置和定时刷新功能。

---

**功能**

- 扫描文件夹中的 `.md` 文件，统计 `div1` 到 `div5` 和类型分布。
- 生成柱状图展示统计结果。
- 支持一次性生成数据图，或定时刷新。

---

**环境要求**

- Python 3.x
- 安装 `matplotlib`与 `watchdog`库

---

**安装依赖**

运行以下命令安装依赖：

```
pip install -r requirements.txt
```

或者单独安装 `matplotlib`与 `watchdog`：

```
pip install matplotlib watchdog
```

---

**使用说明**

1. **运行脚本**（在main.py所在目录下运行）：

```
python main.py
```

2. **定时刷新图表**  （每次更新缓冲一定时间后刷新图表）：

```
python main.py --mode 0 --interval 60
```

3. **配置文件**：

配置文件 `Script.json` 示例：

```json
{
    "root_directory": "..\\..\\",   // 扫描的根目录
    "png_save_directory": "..\\img",     // 保存图表的目录
}
```

---

**输出**

- 打印 `div1` 到 `div5` 和类型的分布。
- 生成并保存统计图表 `训练数据.png`。

---
**将脚本设置为开机自启动**

**许可**

MIT 许可证

---

