/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        error: "#FF1111",
      },
    },
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["acid"],
  },
};
