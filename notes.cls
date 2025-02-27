\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{notes}[2024/09/03 v1.0 Notes Class based on ctexart]

% 继承 ctexart 类
\LoadClass[UTF8]{ctexart}

% 数学、表格、图形、排版与超链接相关包
\RequirePackage{amsthm,amsmath,amsfonts,amssymb,bm} % 数学相关
\RequirePackage{array,makecell,mdframed,floatrow}   % 表格与内容框
\RequirePackage{graphicx,tikz,pgfplots}             % 图形相关
\RequirePackage{indentfirst,enumitem,hyperref}      % 排版与超链接
\usepackage{subcaption}                             % 子图支持

% TikZ 和 PGFPlots 设置
\pgfplotsset{compat=1.18}
\usetikzlibrary{shapes,snakes}

% 页面布局
\RequirePackage[a4paper,left=1.5cm,right=1.5cm,top=3cm,bottom=3cm]{geometry}

% 链接设置
\hypersetup{
  colorlinks=true,
  urlcolor=black,
  linkcolor=black
}

% 定义定理风格
\newtheoremstyle{mystyle} % 名称
  {3pt}                   % 上间距
  {3pt}                   % 下间距
  {}                      % 正文字体
  {}                      % 缩进
  {\bfseries}             % 标题字体
  {}                      % 标题后的标点
  {.5em}                  % 标题后的空格
  {}                      % 头部填充

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
\newtheorem{homework}[theorem]{作业}

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
\newcommand\nl[1]{\textup{#1}}                          % 正体
\newcommand\bd[1]{\textbf{\textup{#1}}}                 % 粗体 
\newcommand\ia[1]{\textit{#1}}                          % 斜体
\newcommand\set[1]{\mathbb{#1}}                         % 集合
\newcommand\abs[1]{\left|#1\right|}                     % 绝对值
\newcommand\mathe{\mathrm{e}}                           % 自然对数的底数 e
\newcommand\mathi{\mathrm{i}}                           % 虚数单位 i
\newcommand\D[1]{\mathrm{d}{#1}}                        % 微分算子 d
\newcommand\sa[1]{\mathrm{Sa}{#1}}                             % Sa 函数
\newcommand\sgn[1]{\mathrm{sgn}(#1)}                    % 符号函数
\newcommand\ip[2]{\left\langle#1, #2\right\rangle}      % 内积
\newcommand\re[1]{\mathrm{Re}{#1}}                      % 实部
\newcommand\im[1]{\mathrm{Im}{#1}}                      % 虚部
\newcommand\DTFT[1]{\mathrm{DTFT}\left[#1\right]}       % DTFT 变换
\newcommand\IDTFT[1]{\mathrm{IDTFT}\left[#1\right]}     % IDTFT 变换
\newcommand\DFT[1]{\mathrm{DFT}\left[#1\right]}         % DFT 变换
\newcommand\IDFT[1]{\mathrm{IDFT}\left[#1\right]}       % IDFT 变换
\newcommand\rev[1]{\widetilde{#1}}                      % 序列回绕
\newcommand\vct[1]{\bm{#1}}                             % 向量

% 设置列表环境的行间距
\setlist[enumerate,1]{itemsep=1pt,parsep=0pt,topsep=0pt}
\setlist[itemize,1]{itemsep=1pt,parsep=0pt,topsep=0pt}
