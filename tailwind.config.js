/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./presentation/templates/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [
    require("daisyui")
  ],
}