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
          'primary-100': '#ffcad1',
          'primary-200': '#f19597',
          'primary-300': '#e86a6f',
          'primary-400': '#f2444b',
          'primary-500': '#f72c30',
          'primary-600': '#e81f2f',
          'primary-700': '#d60f29',
          'primary-800': '#c90022',
          'primary-900': '#bb0014',
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
          'black-two': '#232323',
          'dark': '#29303b',
          'brownish-grey': '#686868',
          'battleship-grey': '#686f7a',
          'purplish-grey': '#726c74',
          'light-grey': '#d2d2d2',
          'silver': '#d5dbe0',
          'pale-grey': '#eceff1',
          'white-three': '#fdfdfd',
          'white': '#ffffff',
          'turquoise-blue': '#0498be',
          'mediumturquoise': '#becde1',
          'robin-egg-blue': '#4fd0e7',
          'ocean-blue': '#0069b3',
          'tory-blue': '#0b51a1',
          'darkish-blue': '#002d7f',
          'navy-blue': '#001f50',
          'lipstick': '#e51a2d',
          'indianred3': '#df484b',
          'mantis': '#76ce68',
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
