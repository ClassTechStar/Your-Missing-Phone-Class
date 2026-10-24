# -*- coding: utf-8 -*-
"""为视觉验收渲染样页：每本 PDF 取 封面/目录页/正文页/尾页 各 1 张 PNG。

用法：python scripts/render_audit.py <pdf目录> <输出目录> [版本...]
"""
import sys
from pathlib import Path

import pymupdf

def toc_page(doc):
    """找到目录所在页（书签第一章页之前的最大页码，或含大量章标题行的页）。"""
    toc = doc.get_toc()
    if toc:
        first = min(t[2] for t in toc)
        if first > 1:
            return first - 1
    return 2

def render(pdf: Path, outdir: Path):
    doc = pymupdf.open(pdf)
    pages = sorted({0, min(1, doc.page_count - 1),
                    toc_page(doc), doc.page_count // 3,
                    doc.page_count - 2})
    outdir.mkdir(parents=True, exist_ok=True)
    for pno in pages:
        if not (0 <= pno < doc.page_count):
            continue
        pix = doc[pno].get_pixmap(dpi=110)
        f = outdir / f'{pdf.parent.name}_{pdf.stem}_p{pno + 1:04d}.png'
        pix.save(f)
    return len(pages)

def main():
    root = Path(sys.argv[1])
    out = Path(sys.argv[2])
    vers = sys.argv[3:] or ['v1.8']
    n = 0
    for v in vers:
        d = root / v
        if not d.is_dir():
            continue
        for p in sorted(d.glob('*.pdf')):
            n += render(p, out / v)
    print(f'rendered {n} pages -> {out}')

if __name__ == '__main__':
    main()
