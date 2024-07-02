# Sun Bank

- Bank Account Site - Deposit, Withdraw, Transfer to different Bank Account



## How To Use

- Register On The Site to Create a Bank Account

- Deposit, Withdraw, Transfer to another Bank Account.

- See Transactions History for Every Account Actions.

- See Current Month Total Transactions Income/Expense information in Home Route.

- Pre-configured Admin Account - admin:admin

## How to Setup:
Docker:
```
docker run -p 8000:8000 docker.io/randomg1/sun-bank-app:latest
```

Locally:
```
git clone https://github.com/SunLaria/Sun-Bank-App.git
cd Sun-Bank-App
python -m pip install -r requirements.txt
python ./manage.py runserver
```

## How To Run:
Navigate to http://localhost:8000/ or http://127.0.0.1:8000/


## Additional Information

- This Project Is Written in Python, JS, HTML, Jinja, CSS.
- Build in Django Framework and using API Requests with Axios JS for Account actions.
- Used WhiteNoise For Serving Static Files in Django FrameWork
