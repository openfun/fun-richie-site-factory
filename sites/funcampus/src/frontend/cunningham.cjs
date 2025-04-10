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
            'primary-100': '#F5BEA4',
            'primary-200': '#F19D75',
            'primary-300': '#EC7C47',
            'primary-400': '#E75B19',
            'primary-500': '#CC5015',
            'primary-600': '#B04512',
            'primary-700': '#953A10',
            'primary-800': '#792F0D',
            'primary-900': '#5D240A',
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
            'denim2': '#0067b4',
            'steelblue3': '#3e8dc9',
            'blue-green': '#0da0a3',
            'orange': '#e75b19',
            'greeny-blue': '#47b7ba',
            'mediumturquoise': '#58c6c2',
            'firebrick6': '#f72c30',
            'dodgerblue4': '#1057a7',
            'cerulean': '#45bde2',
            'navy': '#08223c',
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
  