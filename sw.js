/* 你缺失的那门手机课 · Service Worker
 * ------------------------------------------------------------------
 * 目标：阅读门户 + 19 个语言单文件 HTML 全部可离线。
 *
 * 设计：
 * - 安装时只预热「应用外壳」（门户、manifest、自测页与题库），体积小；
 * - 语言正文每本约 1MB，按需缓存（用户点开哪本才存哪本），
 *   避免一次性写 20MB。
 * - 同源 GET：stale-while-revalidate（秒开 + 后台更新）。
 * - 页面导航：network-first，失败回退缓存（保证改版后能拿到新版，
 *   断网时仍可打开）。
 * - 跨域 CDN（Tailwind / Font Awesome）：cache-first，opaque 响应也存，
 *   断网时样式不塌。
 *
 * 改版本号 CACHE 即可让所有客户端重新预热并清掉旧缓存。
 */
'use strict';

const VERSION = 'v1';
const CACHE = 'phoneclass-' + VERSION;
const SHELL = [
  './',
  './index.html',
  './manifest.webmanifest',
  './quiz.html',
  './quiz/zh-CN.json',
  './icons/icon-192.png',
  './icons/icon-512.png',
];
// 只有这些跨域域名允许进缓存（其余一概不碰，避免缓存污染）
const CORS_OK = [
  'https://cdn.tailwindcss.com',
  'https://cdnjs.cloudflare.com',
];

self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE);
    // 逐个 addAll：某一项失败不要拖垮整个安装
    await Promise.allSettled(SHELL.map((url) => cache.add(new Request(url, { cache: 'reload' }))));
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter((k) => k.startsWith('phoneclass-') && k !== CACHE)
      .map((k) => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);
  const sameOrigin = url.origin === self.location.origin;

  if (!sameOrigin && !CORS_OK.some((o) => url.href.startsWith(o))) return;

  // 页面导航：网络优先，保证改版可见；断网才用缓存
  if (req.mode === 'navigate') {
    event.respondWith((async () => {
      try {
        const fresh = await fetch(req);
        const cache = await caches.open(CACHE);
        cache.put('./index.html', fresh.clone());
        return fresh;
      } catch (_) {
        const cache = await caches.open(CACHE);
        return (await cache.match('./index.html'))
          || (await cache.match(req))
          || new Response('离线且缓存为空，请联网后重试。', {
            status: 503, headers: { 'Content-Type': 'text/html; charset=utf-8' },
          });
      }
    })());
    return;
  }

  // 其余 GET：stale-while-revalidate
  event.respondWith((async () => {
    const cache = await caches.open(CACHE);
    const cached = await cache.match(req);
    const network = fetch(req).then((res) => {
      // opaque 响应（跨域 no-cors）状态为 0，同样可缓存
      if (res && (res.ok || res.type === 'opaque')) {
        cache.put(req, res.clone());
      }
      return res;
    }).catch(() => null);
    if (cached) {
      event.waitUntil(network);
      return cached;
    }
    const fresh = await network;
    if (fresh) return fresh;
    return new Response('', { status: 504, statusText: 'offline' });
  })());
});

// 页面可主动触发「把全部语言正文也存下来」（每本约 1MB，共 19 本）
self.addEventListener('message', (event) => {
  if (event.data !== 'cache-all-languages') return;
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE);
    const res = await fetch('./index.html');
    const html = await res.text();
    const files = [...html.matchAll(/v1\.8\/([a-z\-]+)\.html/g)]
      .map((m) => `./v1.8/${m[1]}.html`);
    await Promise.allSettled(files.map((u) => cache.add(u)));
  })());
});
