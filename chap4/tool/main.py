def generate_graph_1_str(coeff_x, coeff_y):
    assert coeff_y[0] == 1
    results = [
        "        \\node [name=input] (input) {$x(n)$};",
        "        \\node [circ, right of=input, xshift=1cm] (circx) {};",
        "        \\path [no-arrow-line] (input) -- (circx);",
        "        \\node [sum, right of=circx, xshift=4cm] (sum) {$+$};",
        "        \\node [circ, right of=sum, xshift=4cm] (circy) {};",
        "        \\path [no-arrow-line] (sum) -- (circy);",
        "        \\node [name=output, right of=circy, xshift=1cm] (output) {$y(n)$};",
        "        \\path [line] (circy) -- (output);", ""
    ]

    # 画出 Z^{-1} 构成的骨架
    for name, coeff in [("x", coeff_x), ("y", coeff_y)]:
        for i, v in enumerate(coeff):
            if i == 0:
                continue
            if i == 1:
                results.append(f"        \\node [block, below of=circ{name}, yshift=-1cm] (z{name}{i}) {{$Z^{{-1}}$}};")
                results.append(f"        \\path [line] (circ{name}) -- (z{name}{i});")
            else:
                results.append(f"        \\node [block, below of=z{name}{i - 1}, yshift=-2cm] (z{name}{i}) {{$Z^{{-1}}$}};")
                results.append(f"        \\path [line] (z{name}{i - 1}) -- (z{name}{i});")
        results.append("")

    # 画出分叉点和 gain 模块
    for name, sign, ori, coeff in [("x", 1, "east", coeff_x), ("y", -1, "west", coeff_y)]:
        for i, v in enumerate(coeff):
            if (name == "y" and i == 0) or v == 0:
                continue
            # 单独处理 x(n) 前的系数
            if i == 0:
                if v == 1:
                    results.append(f"        \\path [line] (circ{name}) -- (sum);")
                else:
                    results.append(f"        \\node [gain{name}, right of=circ{name}, xshift={sign * 1}cm] (zg{name}{i}) {{${v}$}};")
                    results.append(f"        \\path [line] (circ{name}) -- (zg{name}{i});")
                    results.append(f"        \\path [line] (zg{name}{i}) -- (sum);")
            else:
                if v == 1:
                    if i == len(coeff) - 1:
                        results.append(f"        \\coordinate (zg{name}{i}) at ([xshift={sign * 2}cm, yshift=-1cm] z{name}{i});")
                        results.append(f"        \\path [no-arrow-line] (z{name}{i}) |- (zg{name}{i});")
                        results.append(f"        \\path [line] (zg{name}{i}) -- (sum);")
                    else:
                        results.append(f"        \\node [circ, below of=z{name}{i}, yshift=-0.5cm] (circ{name}{i}) {{}};")
                        results.append(f"        \\coordinate (zg{name}{i}) at ([xshift={sign * 2}cm] circ{name}{i});")
                        results.append(f"        \\path [no-arrow-line] (circ{name}{i}) -- (zg{name}{i});")
                        results.append(f"        \\path [line] (zg{name}{i}) -- (sum);")
                else:
                    results.append(f"        \\node [gain{name}, below of=z{name}{i}, xshift={sign * 2}cm, yshift=-0.5cm] (zg{name}{i}) {{${sign * v}$}};")
                    if i == len(coeff) - 1:
                        results.append(f"        \\path [line] (z{name}{i}) |- (zg{name}{i});")
                    else:
                        results.append(f"        \\node [circ, below of=z{name}{i}, yshift=-0.5cm] (circ{name}{i}) {{}};")
                        results.append(f"        \\path [line] (circ{name}{i}) -- (zg{name}{i});")
                    results.append(f"        \\path [line] (zg{name}{i}.{ori}) -- (sum);")

    return "\n".join(results)


def generate_graph_2_str(coeff_x, coeff_y):
    assert coeff_y[0] == 1
    results = [
        "        \\node [name=input] (input) {$x(n)$};",
        "        \\node [sum, right of=input, xshift=1cm] (sumy) {$+$};",
        "        \\path [line] (input) -- (sumy);",
        "        \\node [circ, right of=sumy, xshift=4cm] (circ) {};",
        "        \\path [no-arrow-line] (sumy) -- (circ);",
        "        \\node [sum, right of=circ, xshift=4cm] (sumx) {$+$};",
        "        \\node [name=output, right of=sumx, xshift=1cm] (output) {$y(n)$};",
        "        \\path [line] (sumx) -- (output);", ""
    ]

    max_len = max(len(coeff_x), len(coeff_y))

    # 画出 Z^{-1} 构成的骨架
    for i in range(max_len):
        # 单独处理 x(n) 前的系数
        if i == 0:
            if coeff_x[i] == 1:
                results.append("        \\path [line] (circ) -- (sumx);")
            else:
                results.append(f"        \\node [gainx, right of=circ, xshift=1cm] (zgx{i}) {{${coeff_x[i]}$}};")
                results.append(f"        \\path [line] (circ) -- (zgx{i});")
                results.append(f"        \\path [line] (zgx{i}) -- (sumx);")
        elif i == 1:
            results.append(f"        \\node [block, below of=circ, yshift=-2cm] (z{i}) {{$Z^{{-1}}$}};")
            results.append(f"        \\path [line] (circ) -- (z{i});")
        else:
            results.append(f"        \\node [block, below of=z{i - 1}, yshift=-2cm] (z{i}) {{$Z^{{-1}}$}};")
            results.append(f"        \\path [line] (z{i - 1}) -- (z{i});")

    # 画出分叉点
    for i in range(max_len):
        if i == 0:
            continue
        if (i < len(coeff_x) and coeff_x[i] != 0) or (i < len(coeff_y) and coeff_y[i] != 0):
            if (i == max_len - 1) and not ((i < len(coeff_x) and coeff_x[i] != 0) and (i < len(coeff_y) and coeff_y[i] != 0)):
                results.append(f"        \\coordinate (circ{i}) at ([yshift=-1.5cm] z{i});")
            else:
                results.append(f"        \\node [circ, below of=z{i}, yshift=-0.5cm] (circ{i}) {{}};")
            results.append(f"        \\path [no-arrow-line] (z{i}) -- (circ{i});")

    # 画出所有 gain 模块
    for name, sign, ori, lr, coeff in [("x", 1, "east", "right", coeff_x), ("y", -1, "west", "left", coeff_y)]:
        for i, v in enumerate(coeff):
            if i == 0 or v == 0:
                continue
            if v == 1:
                results.append(f"        \\coordinate (zg{name}{i}) at ([xshift={sign * 2.5}cm] circ{i});")
                results.append(f"        \\path [no-arrow-line] (circ{i}) -- (zg{name}{i});")
                results.append(f"        \\path [line] (zg{name}{i}) -- (sum{name});")
            else:
                results.append(f"        \\node [gain{name}, {lr} of=circ{i}, xshift={sign * 1}cm] (zg{name}{i}) {{${sign * coeff[i]}$}};")
                results.append(f"        \\path [line] (circ{i}) -- (zg{name}{i});")
                results.append(f"        \\path [line] (zg{name}{i}.{ori}) -- (sum{name});")
    return "\n".join(results)


def print_flow_chart(tp, coeff_x, coeff_y, caption_str, label_str):
    prelude_str = '''
\\begin{figure}[H]
    \\centering
    \\tikzstyle{block} = [draw, rectangle, minimum height=1cm, minimum width=1cm]
    \\tikzstyle{circ} = [draw, fill, circle, inner sep=1.5pt]
    \\tikzstyle{no-circ} = [draw, circle, inner sep=0pt]
    \\tikzstyle{sum} = [draw, circle]
    \\tikzstyle{line} = [draw, -latex]
    \\tikzstyle{no-arrow-line} = [draw, -]
    \\tikzstyle{gainx} = [draw, isosceles triangle, isosceles triangle apex angle=60]
    \\tikzstyle{gainy} = [draw, isosceles triangle, isosceles triangle apex angle=60, shape border rotate=180]
    \\begin{tikzpicture}
'''
    finale_str = f'''
    \\end{{tikzpicture}}
    \\caption{{{caption_str}}}
    \\label{{{label_str}}}
\\end{{figure}}
'''
    print(prelude_str + (generate_graph_1_str(coeff_x, coeff_y) if tp == 1 else generate_graph_2_str(coeff_x, coeff_y)) + finale_str)


if __name__ == '__main__':
    print_flow_chart(1, [2, 0, 1, 1.2], [1, -0.7, -0.6, 1.2], "1", "1")
    print_flow_chart(2, [2, 0, 1, 1.2], [1, -0.7, -0.6, 1.2], "2", "2")
