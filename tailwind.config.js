/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./presentation/templates/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        primary: "#4F46E5",
        "primary-dark": "#4338CA",
        "primary-light": "#A5B4FC",
        secondary: "#6B7280",
        muted: "#9CA3AF",
        background: "#F9FAFB",
        card: "#FFFFFF",
        border: "#E5E7EB",
        accent: "#10B981",
        "accent-dark": "#059669",
        "accent-light": "#6EE7B7",
        destructive: "#EF4444",
        "destructive-dark": "#DC2626",
        "destructive-light": "#FCA5A5",
      },
    },
  },
}