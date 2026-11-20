/** 静态 Tailwind 构建：替代 cdn.tailwindcss.com 运行时 JIT */
module.exports = {
  darkMode: 'class',
  content: ['v1.8/*.html', 'v1.9/*.html', '*.html'],
  theme: {
    extend: {
      colors: {
        primary: '#4f46e5',
        secondary: '#6B7280',
        light: '#F3F4F6',
        dark: '#1F2937',
        accent: '#7c3aed',
      },
      fontFamily: {
        sans: ['MiSans', 'Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont',
               'Segoe UI', 'Roboto', 'PingFang SC', 'Microsoft YaHei', 'sans-serif'],
      },
    },
  },
  corePlugins: { preflight: true },
}
