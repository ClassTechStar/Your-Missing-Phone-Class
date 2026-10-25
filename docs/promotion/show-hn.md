# Show HN 发布文案

**标题（≤80 字符，三选一）：**

1. Show HN: I wrote a 69-chapter smartphone literacy book for everyone – free, in 19 languages
2. Show HN: Your Missing Phone Class – 84 lessons from "what is a SoC" to shipping your first app
3. Show HN: A free phone-literacy textbook for parents and beginners, 19 languages, PDF/APK/Web

**正文：**

Hi HN, I spent months writing "Your Missing Phone Class" (你缺失的那门手机课) — the tech
literacy course that nobody teaches: not at school, not in manuals.

My parents kept asking me things like "storage is full, what do I delete?", "is this
lottery-SMS real?", "how do I move photos to my new phone?". Every book I found was either
a dumbed-down pamphlet or a repair manual. So I wrote the book I wished they had.

**What's inside (84 chapters, 11 parts):**
- Fundamentals: SoC/ROM/RAM without jargon, file management, Wi-Fi vs cellular, permissions
- Security: scam-pattern recognition (including AI voice-clone scams), anti-doxing, what to
  do in the first 30 minutes after losing your phone
- Real life: mobile payment safety, digital-wellbeing (screen time, 20-20-20), remote-support
  setups for elderly parents, smart-home onboarding
- A full developer track (33 chapters): prompt engineering → AI-assisted coding → Kotlin +
Jetpack Compose / Swift + SwiftUI → two real apps → publishing to Play Store

**Everything is free (CC BY-NC-SA):**
- Web (single-file HTML, works offline): 19 languages incl. RTL (Arabic, Hebrew), Classical Chinese
- Typeset PDFs: 74 books across 4 versions, TOC bookmarks, hyphenation, proper RTL
- Android APKs: 19 standalone offline readers

Engineering-wise it's a single-source-of-truth pipeline: 84 Markdown chapters per language →
byte-equivalent HTML (CI-verified, 84/84 chapters), plus a LaTeX typesetting chain. There's
even an MCP server so AI assistants can query the book structure.

Links: [README](https://github.com/ClassTechStar/Your-Missing-Phone-Class) ·
[English book](https://github.com/ClassTechStar/Your-Missing-Phone-Class/blob/main/v1.8/en.html) ·
[PDFs](https://github.com/ClassTechStar/Your-Missing-Phone-Class/releases)

Feedback welcome — especially on what chapters to add next (v1.9 drafts: wearables, travel
eSIM, health data, AI short-video).

**跟帖备用答问：**

- Q: Why 19 languages? A: The content is translation-friendly (plain language, cultural
  notes localized), and each language is a full 84-chapter translation verified by CI.
- Q: How do you keep translations in sync? A: Every language has its own Markdown source
  (source/translations/<lang>/); CI rebuilds and diffs against the published HTML per chapter.
- Q: Is it really free? A: CC BY-NC-SA 4.0 — free to share and adapt non-commercially.
