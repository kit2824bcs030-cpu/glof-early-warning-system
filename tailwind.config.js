/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        command: {
          bg: "#0B0F17",
          panel: "#111827",
          card: "#162032",
          border: "#1F2E47",
          accent: "#38BDF8",
          highlight: "#0284C7",
        },
        risk: {
          normal: "#10B981",    // Emerald
          watch: "#F59E0B",     // Amber
          warning: "#F97316",   // Orange
          critical: "#EF4444",  // Crimson Red
        }
      },
      fontFamily: {
        mono: ['ui-monospace', 'SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', 'monospace'],
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
      },
      boxShadow: {
        'glow-cyan': '0 0 15px rgba(56, 189, 248, 0.25)',
        'glow-red': '0 0 20px rgba(239, 68, 68, 0.35)',
        'glow-amber': '0 0 15px rgba(245, 158, 11, 0.25)',
      }
    },
  },
  plugins: [],
}
