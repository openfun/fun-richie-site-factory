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
            families: { base: 'Hind', accent: 'Montserrat' },
          },
          colors: {
            'primary-100': '#ACF7F8',
            'primary-200': '#61EFF2',
            'primary-300': '#15E8EC',
            'primary-400': '#0DA0A3',
            'primary-500': '#0B898B',
            'primary-600': '#097274',
            'primary-700': '#075A5C',
            'primary-800': '#054345',
            'primary-900': '#042C2D',
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
            'dark-grey': '#232323',
            'charcoal': '#29303b',
            'slate-grey': '#686868',
            'battleship-grey': '#686f7a',
            'light-grey': '#d2d2d2',
            'silver': '#d5dbe0',
            'azure2': '#eceff1',
            'smoke': '#fdfdfd',
            'white': '#ffffff',
            'denim': '#0067b7',
            'steelblue3': '#3e8dc9',
            'blue-green': '#0da0a3',
            'greeny-blue': '#47b7ba',
            'mediumturquoise': '#58c6c2',
            'firebrick6': '#f72c30',
          },
        },
        components: {
          button: {
            'font-family': 'Montserrat',
          },
        },
      },
    },
  };
  