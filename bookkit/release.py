"""release：发布清单（HTML 校验和 + 每语言独立包名 + SHA256SUMS）。

APK 打包依赖外部工具链（Android SDK / buildozer 等），不在本仓库内实现；
本模块生成"待打包清单"，供发布流水线按清单产出 APK 并校验。
"""

import hashlib
import json
from pathlib import Path

PACKAGE_PREFIX = 'com.classtechstar.phoneclass'


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_release(root: Path, mf, version: str, out_dir: Path = None) -> dict:
    out_dir = Path(out_dir) if out_dir else (root / 'dist' / 'release')
    files = mf.html_files(version)
    if not files:
        raise RuntimeError(f'{version} 下没有可发布的 HTML')

    entries = []
    sums = []
    for code, path in files:
        digest = _sha256(path)
        pkg = f'{PACKAGE_PREFIX}.{code.replace("-", "").lower()}'
        entries.append({
            'lang': code,
            'html': path.relative_to(root).as_posix(),
            'bytes': path.stat().st_size,
            'sha256': digest,
            'package': pkg,
            'apk': f'{version}/{code}.apk',
        })
        sums.append(f'{digest}  {path.relative_to(root).as_posix()}')

    manifest = {
        'version': version,
        'generated_from': 'manifest/languages.json',
        'count': len(entries),
        'assets': entries,
    }

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f'release-{version}.json').write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + '\n',
        encoding='utf-8', newline='\n')
    (out_dir / f'SHA256SUMS-{version}.txt').write_text(
        '\n'.join(sums) + '\n', encoding='utf-8', newline='\n')
    return manifest
