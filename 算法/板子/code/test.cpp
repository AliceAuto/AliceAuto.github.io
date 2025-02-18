#include <iostream>
#include <vector>
#include <ranges>
#include <algorithm>
#include <numeric>


int main() {
    // 初始化一个整数 vector
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // 使用 ranges::transform 将每个元素乘以 2
    auto doubled = vec | std::ranges::transform([](int n) { return n * 2; });

    // 打印乘以 2 后的结果
    std::cout << "Doubled values: ";
    for (int n : doubled) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    // 使用 ranges::filter 筛选出大于 6 的元素
    auto filtered = doubled | std::ranges::filter([](int n) { return n > 6; });

    // 打印过滤后的结果
    std::cout << "Filtered values (greater than 6): ";
    for (int n : filtered) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    // 使用 ranges::sort 对原始 vector 进行排序
    std::ranges::sort(vec);

    std::cout << "Sorted values: ";
    for (int n : vec) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    // 使用 ranges::reverse 对原始 vector 进行反转
    std::ranges::reverse(vec);

    std::cout << "Reversed values: ";
    for (int n : vec) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    // 使用 ranges::accumulate 计算总和
    int sum = std::ranges::accumulate(vec, 0);
    std::cout << "Sum of elements: " << sum << std::endl;

    // 使用 ranges::max_element 和 ranges::min_element 找到最大和最小元素
    auto max_it = std::ranges::max_element(vec);
    auto min_it = std::ranges::min_element(vec);

    std::cout << "Max element: " << *max_it << ", Min element: " << *min_it << std::endl;

    // 使用 ranges::find 查找元素 3
    auto find_it = std::ranges::find(vec, 3);
    if (find_it != vec.end()) {
        std::cout << "Found element: " << *find_it << std::endl;
    }

    // 使用 ranges::join 将多个范围连接在一起
    std::vector<std::vector<int>> vec2d = {{1, 2}, {3, 4}, {5, 6}};
    auto joined = vec2d | std::ranges::join;

    std::cout << "Joined values: ";
    for (int n : joined) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    // 使用 ranges::cartesian_product 计算两个范围的笛卡尔积
    std::vector<int> a = {1, 2};
    std::vector<int> b = {3, 4};
    auto product = std::ranges::cartesian_product(a, b);

    std::cout << "Cartesian product: ";
    for (auto [x, y] : product) {
        std::cout << "(" << x << ", " << y << ") ";
    }
    std::cout << std::endl;

    // 使用 ranges::to 转换为容器
    auto transformed = vec | std::ranges::transform([](int n) { return n * 2; })
                            | std::ranges::to<std::vector<int>>();

    std::cout << "Transformed (to vector): ";
    for (int n : transformed) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    return 0;
}
