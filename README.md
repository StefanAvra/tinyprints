# tinyprints
Flask web app that lets anyone create small prints that will be printed on my thermal printer.


## Usage

Clone this repo.
cd into repo and create a venv and install requirements. 
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

You can run the app by executing ```flask run```. 

### Dev

Flask will look for environment variables in ```.flaskenv```.

```flask run``` uses ```run.py``` as an entry point. If you start ```flask shell``` the database and TinyText model will be avaliable as shell context ```db```  and ```TinyText``` respectively.

## Contributing
Contributions are welcome!

Open an issue if you found a bug or want to make a feature request.
You can also check TODO.md for hints on what is planned / could be improved. Check if there is already an issue and if not open one if you've found something you want to improve.

## To do
See [TODO.md](/TODO.md)

## License
StefanAvra/tinyprints is licensed under the
GNU General Public License v3.0