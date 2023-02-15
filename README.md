### NOTE:
- 2023-02-15 Web app is down because heroku does not have a free tier anymore. If there is any interest you can contact me / open an issue and I might look for hosting.
- 2022-02-15 Web app is up but printer is currently down. Needed that Raspberry Pi for something else.

# tinyprints
Flask web app that lets anyone create small prints that will be printed on my thermal printer. Deployed on [Heroku](https://tinyprints.herokuapp.com/).

I have set up a thermal printer in our living room that prints on 58mm width receipt paper.
We use it to create small prints of doodles, Pokemon or other insignificant things.
I thought it would be cool if friends could send something to the printer.
This web app allows users to submit some text (images will be added soon) and vote on submissions.

On the **hot** tab submissions are ordered by votes. When the deadline will be reached the entry on top "wins" and will be downloaded by the printer.

There is also a repo for the code that runs on the printer:
https://github.com/StefanAvra/tinyprints-printer

## Usage

Clone this repo.
cd into repo and create a venv and install requirements. 
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

You can run the app by executing ```flask run```. 

### Development

Flask will look for environment variables in ```.flaskenv```.

```flask run``` uses ```run.py``` as an entry point. If you start ```flask shell``` the database and TinyText model will be avaliable as shell context ```db```  and ```TinyText``` respectively.

#### Deployment on Heroku
Necessary env vars can be set as:
```sh
heroku config:set FLASK_APP=run.py                             
heroku config:set SECRET_KEY="your secret key here"
heroku config:set AUTH_SECRET="your pw for api auth"                            

```

## Contributing
Contributions are welcome!

Open an issue if you found a bug or want to make a feature request.
You can also check TODO.md for hints on what is planned / could be improved. Check if there is already an issue and if not open one if you've found something you want to improve.

## To do
See [TODO.md](/TODO.md)

## License
StefanAvra/tinyprints is licensed under the
GNU General Public License v3.0
