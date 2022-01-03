
## How to run flask app

```sh
# set up poetry first 
poetry install
poetry shell

export FLASK_APP=account
export FLASK_ENV=development
flask run  --host=0.0.0.0 --port=5888

# init db using
http://localhost:5888/initdb
```

## test pass 

the main logic is test in `test_user.py`

<img width="1040" alt="Screen Shot 2022-01-03 at 2 43 14 PM" src="https://user-images.githubusercontent.com/666683/147905172-ca9679b8-7e16-4a0f-95b6-07bacb726ee7.png">



