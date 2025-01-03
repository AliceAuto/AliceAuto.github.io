# JAVA 常用包
- **java.lang** ：提供基本的类，如Object、String、Thread、Math、ClassLoader等。
- **java.util** ：提供常用集合类，如ArrayList、HashMap、Hashtable、LinkedList、Properties、Random、Scanner、Stack、Timer、TimeZone等。
- **java.io** ：提供输入/输出相关类，如InputStream、OutputStream、Reader、Writer、File、FileReader、FileWriter等。
- **java.net** ：提供网络相关类，如URL、URLConnection、Socket、ServerSocket等。
- **java.sql** ：提供数据库相关类，如Connection、Statement、PreparedStatement、ResultSet等。


# 面现对象3大特特性
- **封装**
- **继承**
- **多态**
  

# Java 访问修饰符
下面是一个关于Java权限修饰符作用的表格，涵盖了常用的权限修饰符及其特点：

| 修饰符         | 类别         | 同类访问 | 同包访问 | 子类访问 | 其他包访问 | 备注                             |
|----------------|--------------|----------|----------|----------|------------|----------------------------------|
| `public`       | 类、方法、变量 | 是       | 是       | 是       | 是         | 任何地方都可以访问                |
| `protected`    | 方法、变量    | 是       | 是       | 是       | 否         | 同包内或子类可以访问              |
| `default`（无修饰符） | 类、方法、变量 | 是       | 是       | 否       | 否         | 仅在同包内可访问                  |
| `private`      | 方法、变量    | 是       | 否       | 否       | 否         | 仅在本类内可访问                  |

### 备注
- **public**：任何类都可以访问，包括不同包中的类。
- **protected**：同一包中的其他类以及所有子类（不论包）都可以访问。
- **default**（包私有）：只在同一包内可见，不能被子类访问。
- **private**：只在定义它的类内可见，无法被子类或同包的其他类访问。


# 对象实例化的方法

- **构造方法**
- **序列化与反序列化**
- **Colne**
- **反射**