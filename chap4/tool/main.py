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

    for name, sign, ori, coeff in [("x", 1, "east", coeff_x), ("y", -1, "west", coeff_y)]:
        for i, v in enumerate(coeff):
            if name == "y" and i == 0:
                continue
            if v != 0:
                if i == 0:
                    if v != 1:
                        results.append(f"        \\node [gain{name}, right of=circ{name}, xshift={sign * 1}cm] (zg{name}{i}) {{${v}$}};")
                        results.append(f"        \\path [line] (circ{name}) -- (zg{name}{i});")
                        results.append(f"        \\path [line] (zg{name}{i}) -- (sum);")
                    else:
                        results.append(f"        \\path [line] (circ{name}) -- (sum);")
                else:
                    if v != 1:
                        results.append(f"        \\node [gain{name}, below of=z{name}{i}, xshift={sign * 2}cm, yshift=-0.5cm] (zg{name}{i}) {{${sign * v}$}};")
                        if i != len(coeff) - 1:
                            results.append(f"        \\node [circ, below of=z{name}{i}, yshift=-0.5cm] (circ{name}{i}) {{}};")
                            results.append(f"        \\path [line] (circ{name}{i}) -- (zg{name}{i});")
                        else:
                            results.append(f"        \\path [line] (z{name}{i}) |- (zg{name}{i});")
                        results.append(f"        \\path [line] (zg{name}{i}.{ori}) -- (sum);")
                    else:
                        if i != len(coeff) - 1:
                            results.append(f"        \\node [circ, below of=z{name}{i}, yshift=-0.5cm] (circ{name}{i}) {{}};")
                            results.append(f"        \\coordinate (zg{name}{i}) at ([xshift={sign * 2}cm] circ{name}{i});")
                            results.append(f"        \\path [no-arrow-line] (circ{name}{i}) -- (zg{name}{i});")
                            results.append(f"        \\path [line] (zg{name}{i}) -- (sum);")
                        else:
                            results.append(f"        \\coordinate (zg{name}{i}) at ([xshift={sign * 2}cm, yshift=-1cm] z{name}{i});")
                            results.append(f"        \\path [no-arrow-line] (z{name}{i}) |- (zg{name}{i});")
                            results.append(f"        \\path [line] (zg{name}{i}) -- (sum);")

    return "\n".join(results)


def generate_graph_2_str(coeff_x, coeff_y):
    assert coeff_y[0] == 1


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
    print(prelude_str + generate_graph_1_str(coeff_x, coeff_y) if tp == 1 else generate_graph_2_str(coeff_x, coeff_y) + finale_str)


if __name__ == '__main__':
    print_flow_chart(1, [1, 0, 0, 1], [1, -0.7, -0.6], "1", "2")
