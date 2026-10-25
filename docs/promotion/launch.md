# 发出去：P2-7 传播执行清单

文案与素材已经就绪，这份清单只解决一件事：**按顺序点下去**。
四个渠道的正文在 [show-hn.md](show-hn.md)、[小红书.md](小红书.md)、[bilibili.md](bilibili.md)，
封面在 [assets/](assets/)；本文按"点哪个按钮、粘哪段字、传哪张图"组织。

---

## 0. 发布前核验（5 条命令，全绿才发）

```bash
python -m bookkit lint --all-versions     # 结构/锚点/版本串/分享卡片元数据
python -m bookkit check --claims --index  # README、index.html 的宣称值与死链
python scripts/web_smoke.py               # 21 页 console 零报错
python scripts/sync_site.py --dry-run     # 站点同步计划（含分享卡片 cover-og.png）
```

> 19 种语言的 `build --verify` 由 CI 全量跑（`.github/workflows/ci.yml` 的 build job），本地只需确认最近一次 CI 是绿的。

**外部链接已逐一实测为 200**（2026-10-25）：

| 链接 | 状态 |
|------|------|
| GitHub 仓库主页 | 200 |
| 在线阅读 <https://classtechstar.github.io/Yihggh.github.io/> | 200 |
| `v1.8/en.html`（英文书） | 200 |
| Release `v1.8`（19 APK + 19 HTML） | 200 |
| `latex-pdf-v1.8-final` / `v1.7` / `v1.6` / `v1.5`（74 本 PDF） | 200 |
| `html-archive` / `legacy-html-archive`（历史版本） | 200 |

**发布前必须完成一次站点同步**（否则分享卡片抓不到图，因为 `og:image` 指向站点根）：

```bash
python scripts/sync_site.py     # 把 v1.8/zh-CN.html + cover-og.png + PWA 资产推到站点仓库
cd ../Yihggh.github.io && git add -A && git commit -m "feat: 分享卡片封面" && git push
```

验证（可选，抓一次 OpenGraph）：

```bash
curl -s https://classtechstar.github.io/Yihggh.github.io/ | grep -o 'og:image[^>]*'
curl -sI https://classtechstar.github.io/Yihggh.github.io/cover-og.png | head -3   # 期望 200 image/png
```

---

## 1. 素材清单

| 文件 | 尺寸 | 用在哪 |
|------|------|--------|
| [assets/cover-og.png](assets/cover-og.png) | 1200×630 | 站点 `og:image`、GitHub 仓库社交预览（Settings → Social preview 上传同一张） |
| [assets/cover-xiaohongshu.png](assets/cover-xiaohongshu.png) | 1080×1440（3:4） | 小红书笔记首图（其余 8 张配章节截图） |
| [assets/cover-bilibili.png](assets/cover-bilibili.png) | 1920×1080（16:9） | B 站视频封面（10 期共用，期号压在标题上） |

重新生成（改了章数/版本号后必须重跑，否则图与正文对不上）：

```bash
python scripts/gen_cover.py
```

---

## 2. 发布顺序与节奏

| 时间 | 渠道 | 为什么这个顺序 |
|------|------|----------------|
| **D0 上午** | 小红书主笔记 | 国内读者先看到，评论区沉淀问题，后面视频有素材 |
| **D0 北京 20:00–22:00**（美东工作日 08:00–10:00） | Show HN | HN 前 2 小时的投票决定能否上首页，卡美东上班时间发 |
| **D0 晚** | r/smartphone | 与 HN 错开 6 小时，避免同一天同一批人看到两次 |
| **D1–D2** | 评论区值守 | HN 用 [show-hn.md](show-hn.md) 的答问预案；Reddit 只回技术问题 |
| **D3 起** | B 站 + 小红书双日更 | 同素材分平台剪，每期片尾挂书；选题表见 [小红书.md](小红书.md) |

**一稿多投的边界**：HN / Reddit 是英文技术社区，用 show-hn.md 的英文稿；
小红书 / B 站用中文稿。不要把中文文案机翻后贴到 HN —— 那里的读者会直接点开 `en.html` 验货。

---

## 3. 逐渠道执行

### 3.1 小红书

1. 打开 <https://creator.xiaohongshu.com/publish/publish> → 上传图片（首图 `cover-xiaohongshu.png`，共 9 张）
2. 标题三选一（见 [小红书.md](小红书.md)），正文整段复制，末尾带 10 个标签
3. **正文里不放外链**（会被限流）：只写"GitHub 搜「Your-Missing-Phone-Class」"
4. 发布后立刻在自己笔记下置顶评论：「在线阅读零门槛，PDF 74 本全部免费下载 → 主页链接」
5. 话题补齐：`#适老化` `#给爸妈的手机课` `#数字生活` `#防诈骗` `#免费资源`

### 3.2 Show HN

1. 打开 <https://news.ycombinator.com/submit>
2. Title 用候选 1（`Show HN: I wrote an 84-chapter smartphone literacy book…`），
   正文里的数字（84 章 / 11 篇 / 19 语言 / 74 本 PDF）与 README 完全一致，不要临场改数
3. URL 填仓库主页 `https://github.com/ClassTechStar/Your-Missing-Phone-Class`
4. 正文粘贴 [show-hn.md](show-hn.md) 的 `**正文：**` 段落
5. 发布后 10 分钟内自己回一条：补充"19 种语言的 build --verify 由 CI 逐章校验"的工程细节（HN 吃这个）
6. 不要求赞、不在其他帖子引流——HN 对自推的容忍度只看"是否有真东西"

### 3.3 r/smartphone

1. 打开 <https://www.reddit.com/r/smartphone/submit>
2. 用同一条英文正文，Title 换成候选 2
3. Flair 选 `Resource` / `Guide`（若无此 flair，先看版规再发）
4. 首评补一句「PDF 与 APK 都在 Releases，作者全程在评论区」

### 3.4 B 站

1. 打开 <https://member.bilibili.com/platform/upload/video/frame>
2. 封面用 `cover-bilibili.png`；标题「手机丢了，黄金 30 分钟做对 6 件事」
3. 简介固定结尾（每期都挂）：

   ```text
   本书 84 章全部免费，19 种语言，PDF / 离线网页 / Android App 三种形态：
   https://github.com/ClassTechStar/Your-Missing-Phone-Class
   PDF 直链：https://github.com/ClassTechStar/Your-Missing-Phone-Class/releases/tag/latex-pdf-v1.8-final
   交流群：1074995524
   ```

4. 建合集「你缺失的那门手机课」，第 1–10 期按 [bilibili.md](bilibili.md) 拍

---

## 4. 数据回收（每周一填，决定加更方向）

| 渠道 | 看什么 | 基准线 | 判定 |
|------|--------|--------|------|
| Show HN | points / 评论数（2 小时内） | ≥ 50 分 | 上首页则 D2 再发一条"作者答疑"评论 |
| Reddit | upvote 率、评论质量 | ≥ 85% upvote | 低于则换标题重发（帖子保留不删） |
| 小红书 | 曝光 / 收藏率 / 涨粉 | 收藏率 ≥ 5% | 达标选题做续集，未达标换钩子重拍 |
| B 站 | 播放 / 完播率 / 简介点击 | 完播 ≥ 30% | 达标则该选题拆成 3 期系列 |
| GitHub | stars、Release 下载量 | 周环比 | 下载涨而 star 不涨 → 说明读者不是开发者，小红书加码 |

取数命令（不用手点后台）：

```bash
gh api repos/ClassTechStar/Your-Missing-Phone-Class --jq '.stargazers_count'
gh api repos/ClassTechStar/Your-Missing-Phone-Class/releases --jq '.[].assets[].download_count' | awk '{s+=$1} END {print s}'
```

---

## 5. 合规与踩坑

- **署名**：所有渠道都要写明 CC BY-NC-SA 4.0；B 站简介里"免费"必须伴随协议名，避免被当成盗版资源。
- **非商业**：不接"9.9 元解锁 PDF"类导流，违反协议也不利于口碑。
- **HN 自推**：允许 Show HN，但同一链接 1 年内不要重复提交；被 flag 就不要再申诉。
- **小红书**：站外链接一律走"评论区/主页"，正文出现 `github.com` 会被降权。
- **Reddit**：账号需有一定历史再发，纯新号发资源帖会被自动过滤。
- **翻译质量**：HN 会有人抽查 `en.html` 与中文原稿是否等价；这正是 CI 逐章校验的价值，答问时直接给
  `.github/workflows/ci.yml` 的 build job 链接。
- **RTL 语言**：阿拉伯语/希伯来语截图是最好的"真做了 19 种语言"证据，发 Twitter/Bluesky 时优先用。
