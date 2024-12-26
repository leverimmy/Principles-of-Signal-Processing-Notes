\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{notes}[2024/09/03 v1.0 Notes Class based on ctexart]

% 继承 ctexart 类
\LoadClass[UTF8]{ctexart}

% 包含的包
\RequirePackage{amsthm,amsmath,amsfonts,amssymb}
\RequirePackage{indentfirst,hyperref,mdframed}
\RequirePackage{floatrow,graphicx}
\RequirePackage{tikz,pgfplots,bm}
\RequirePackage{enumitem}
\pgfplotsset{compat=1.18}
\usepackage{subcaption}
\usetikzlibrary{shapes,snakes}

% 页面布局
\RequirePackage[a4paper,left=1.5cm,right=1.5cm,top=3cm,bottom=3cm]{geometry}

% 链接设置
\hypersetup{
  colorlinks=true,
  linkcolor=black
}

% 定义定理风格
\newtheoremstyle{mystyle}% 名称
  {3pt}% 上间距
  {3pt}% 下间距
  {}% 正文字体
  {}% 缩进
  {\bfseries}% 标题字体
  {.}% 标题后的标点
  {.5em}% 标题后的空格
  {}% 头部填充

% 应用定理风格
\theoremstyle{mystyle}

% 定义定理环境
\newtheorem{theorem}{定理}[subsection]
\newtheorem{axiom}[theorem]{公理}
\newtheorem{lemma}[theorem]{引理}
\newtheorem{corollary}[theorem]{推论}
\newtheorem{property}[theorem]{性质}
\newtheorem{definition}[theorem]{定义}
\newtheorem{example}[theorem]{例}
\newtheorem{remark}[theorem]{注}
\newtheorem{exercise}[theorem]{习题}

% 定义证明环境
\renewcommand{\qedsymbol}{$\blacksquare$}

% 定义解答环境
\newenvironment{solution}
  {\renewcommand{\qedsymbol}{}\begin{proof}[解]}
  {\end{proof}}

% 定义分析环境
\newenvironment{analysis}
  {\renewcommand{\qedsymbol}{}\begin{proof}[分析]}
  {\end{proof}}

% 定义注意环境
\newenvironment{note}
  {\renewcommand{\qedsymbol}{}\begin{mdframed}[linewidth=1pt,linecolor=black,innerleftmargin=10pt,innerrightmargin=10pt,innertopmargin=10pt,innerbottommargin=10pt]\begin{proof}[注意]}
  {\end{proof}\end{mdframed}}

% 定义新命令
\newcommand\nl[1]{\textup{#1}}
\newcommand\bd[1]{\textbf{\textup{#1}}}
\newcommand\ia[1]{\textit{#1}}
\newcommand\set[1]{\mathbb{#1}}
\newcommand\abs[1]{\left|#1\right|}
\newcommand\mathe{\mathrm{e}}
\newcommand\mathi{\mathrm{i}}
\newcommand\D[1]{\mathrm{d}#1}
\newcommand\sa{\mathrm{Sa}}
\newcommand\sgn[1]{\mathrm{sgn}(#1)}
\newcommand\ip[2]{\left\langle#1, #2\right\rangle}
\newcommand\re[1]{\mathrm{Re}#1}
\newcommand\im[1]{\mathrm{Im}#1}
\newcommand\DTFT[1]{\mathrm{DTFT}\left[#1\right]}
\newcommand\IDTFT[1]{\mathrm{IDTFT}\left[#1\right]}
\newcommand\DFT[1]{\mathrm{DFT}\left[#1\right]}
\newcommand\IDFT[1]{\mathrm{IDFT}\left[#1\right]}
\newcommand\rev[1]{\widetilde{#1}}
\newcommand\vct[1]{\bm{#1}}

% 设置列表环境的行间距
\setlist[enumerate,1]{itemsep=1pt,parsep=0pt,topsep=0pt}
\setlist[itemize,1]{itemsep=1pt,parsep=0pt,topsep=0pt}
