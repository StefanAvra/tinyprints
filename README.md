# tinyprints
Flask web app that lets anyone create small prints that will be printed on my thermal printer.


## todo
- /new
    - text editor
        - "working" but dirty. need a better way to force line breaks.
    - image editor
        - upload custom images and convert them to 1bit dithered pngs
        - printer has 184 dots per line but cannot heat them all up at once >> find out how many dots per line at once possible and dither image according to this. might be enough to do this server side only
- /
    - toplist (voting)
        - countdown
    - let people vote
        - check if user did upvote
    - write a decorator for upvote validation and refactor redundant code
- /t/<id>
    - delete function
- /top
- /api
- deploy to heroku
- license