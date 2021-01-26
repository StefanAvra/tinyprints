# todo / thoughts
_I use this file during development to note thoughts on what to improve. In case you find something here that you want to contribute on please open an issue for it._

- /create
    - text editor
        - "working" but dirty. need a better way to force line breaks
        - should I base64 it? might be helpful for edge cases / specific characters
        - make list of allowed characters
        - editor could make use of the printers different modes like bold, double height, double width, underlined
    - image editor
        - upload custom images and convert them to 1bit dithered pngs. WASM ImageMagick?
        - printer has 384 dots per line but cannot heat them all up at once >> find out how many dots per line at once possible and dither image according to this. might be enough to do this server side only
        - actual editor for creating/drawing in browser without breaking functionality on phones?
            - this sketchpad seems to work on phones too: https://github.com/yiom/sketchpad. It is provided as an npm package but it looks like it is possible to just serve the sketchpad.js file.
- /
    - switch from textarea to pre for displaying text
    - hot (voting)
        - show a countdown?
- not sure if I should remove db session on appcontext teardown manually
- refactor to subtemplate for a post
- /api add proper auth
- add http errors


- change dates to moment (to show local timezone)
- design
    - keep the app minimal
    - make sure it's responsive
    - favicon


- in the end: rewrite everything to use a restful api and a SPA :)
