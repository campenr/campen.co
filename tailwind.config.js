module.exports = {
  theme: {
    fontFamily: {
      'sans': ['Libre Franklin', 'sans-serif'],
    },
    colors: {
      'blue': '#007BFF',
      'grey-50': '#F9FAFB',
      'black-muted': '#212529',
    },
    extend: {
      screens: {
        xs: '480px',
      }
    }
  },
  purge: {
    enabled: true,
    content: ['./app/app/**/*.html'],
  },
}