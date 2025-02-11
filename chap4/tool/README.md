# Type 1/Type 2 Flow Chart LaTeX Code Generator

## Introduction

这个 Python 脚本用于生成 I 型和 II 型流图的 LaTeX 代码。

## Usage

假设差分方程为

$$
\sum_{k = 0}^{K}b_ky(n-k) = \sum_{r = 0}^{R}a_rx(n-r).
$$

在 `main.py` 中调用 `print_flow_chart` 函数即可。其中，`print_flow_chart` 函数的参数如下：

- `chart_type`：流图类型，取值为 `1` 或 `2`，分别表示 I 型和 II 型流图；
- `coeff_x`：差分方程中 $x(n - r)$ 前的系数 $a_r$；
- `coeff_y`：差分方程中 $y(n - k)$ 前的系数 $b_k$；
- `caption_str`：流图标题。
- `label_str`：流图标签。

**注意**：需要保证 $a_0 \neq 0, b_0 = 1, K > 1$。
