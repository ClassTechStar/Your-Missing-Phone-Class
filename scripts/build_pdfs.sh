#!/bin/bash
# 逐语言生成 LaTeX 并编译 PDF（两遍以生成目录）
cd "C:/Users/18948/Documents/GitHub/Your-Missing-Phone-Class"
for lang in "$@"; do
  echo "===== $lang: generate ====="
  python -m bookkit latex --lang "$lang" --out "latex/$lang" 2>&1 | tail -2
  if [ "$lang" = "zh-CN" ]; then
    dir="latex"
  else
    dir="latex/$lang"
  fi
  echo "===== $lang: xelatex pass 1 ====="
  (cd "$dir" && xelatex -interaction=nonstopmode main.tex > pass1.log 2>&1; echo "exit=$?")
  echo "===== $lang: xelatex pass 2 ====="
  (cd "$dir" && xelatex -interaction=nonstopmode main.tex > pass2.log 2>&1; echo "exit=$?")
done
echo ALL_DONE
