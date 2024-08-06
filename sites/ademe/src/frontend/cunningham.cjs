/* Custom Cunningham Tokens for Richie

   In a child project, you can override those tokens by creating a token file like this one,
   merge your custom tokens with default Richie ones then by using cunningham cli to generate
   sass and ts tokens files (take a look to the `build-theme` command within package.json
   see it in action).

   E.g:
     const tokens = require('richie-education/cunningham.cjs')
     module.exports = {
       theme: {
          ...tokens.themes.default
          colors: {
            ...tokens.colors,
            'your-black': '#1E1E1E',
          },
       },
*/

module.exports = {
  themes: {
    default: {
      theme: {
        font: {
          families: { base: 'DIN2014', accent: 'HCo Gotham' },
        },
        colors: {
          'primary-100': '#00E4E4',
          'primary-200': '#00D7D7',
          'primary-300': '#00BDBE',
          'primary-400': '#00C3C3',
          'primary-500': '#009A9A',
          'primary-600': '#007171',
          'primary-700': '#003E3E',
          'primary-800': '#002425',
          'primary-900': '#000B0B',
          'secondary-100': '#eff8ff',
          'secondary-200': '#eaf3fd',
          'secondary-300': '#e2ebf5',
          'secondary-400': '#c0c9d3',
          'secondary-500': '#a3abb4',
          'secondary-600': '#79818a',
          'secondary-700': '#656c75',
          'secondary-800': '#454d55',
          'secondary-900': '#242b32',
          'black': '#000000',
          'white': '#ffffff',
          'battleship-grey': '#686f7a',
          'dark': '#29303b',
          'black-two': '#2d2d2d',
          'black-three': '#121212',
          'dark-aquamarine': '#007171',
          'turquoise-blue': '#08c1c7',
          'topaz': '#14a5a5',
          'black-four': '#181818',
          'tealish': '#21c7c7',
          'dark-two': '#22232b',
          'warm-grey': '#747474',
          'warm-grey-two': '#979797',
          'light-teal': '#a8e8e8',
          'burnt-orange': '#bc5500',
          'pale-grey-two': '#eceff1',
          'pale-grey': '#f2f4f5',
          'pumpkin-orange': '#ff7400',
          'silver': '#d5dbe0',
          'white-three': '#fdfdfd',
        },
      },
      components: {
        button: {
          'font-family': 'HCo Gotham',
        },
      },
    },
  },
};
