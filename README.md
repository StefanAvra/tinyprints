# tinyprints
Flask web app that lets anyone create small prints that will be printed on my thermal printer.


## todo
- /create
    - text editor
        - "working" but dirty. need a better way to force line breaks.
        - switch from textarea to pre for displaying text
    - image editor
        - upload custom images and convert them to 1bit dithered pngs
        - printer has 184 dots per line but cannot heat them all up at once >> find out how many dots per line at once possible and dither image according to this. might be enough to do this server side only
        - actual editor for creating/drawing in browser?
- /
    - toplist (voting)
        - countdown
    - write a decorator for upvote validation and refactor redundant code
    - write a decorator for init site_data and refactor redundant code
- /t/<id>
    - delete function
- /api
    - get hottest open
    - close
- deploy to heroku
- license