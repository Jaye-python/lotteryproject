# Lottery Application
This is an API-based Django app built using Django Rest Framework. You can Create tickets and draws.
Sample `sqlite3` database included with models already migrated.
Commands below uses `Linux OS`.

### Code was optimized by:
```
refactoring
removing unnecessary loops and calculations
using Python multiprocessing.Pool
```

### To launch this app on your system:

1. Navigate to your desktop (or any folder of your choice)
```
cd Desktop
```
2. Create a new folder/directory called `lottery`
```
mkdir lottery
```
3. Navigate into this new folder
```
cd lottery
```
4. Create a new Python Virtual environment in the `lottery` folder.
```
python3 -m venv ./lotvenv
```
5. Activate this new virtual environment
```
source lotvenv/bin/activate
```
6. Clone this git repo
```
git clone https://github.com/Jaye-python/lotteryproject.git
```
7. Move into the `lotteryproject` folder 
```
cd lotteryproject
```
8. Install dependencies
```
pip install -r requirements.txt
```
9. Create `superuser` account (Optional)
```
python manage.py createsuperuser
```
10. Launch application
```
python manage.py runserver
```
11. To create ticket, send below sample payload to `http://127.0.0.1:8000/api/create-ticket` via POSTMAN using `raw/json` format:
```
{
    "plays": [
        [2, [3, 2, 1, 4, 5]],
        [2, [3, 2, 1, 4, 5]],
        [2, [3, 2, 1, 4, 5]]
    ],
    "rtp": 20000
}
```
12. To create draw, send below sample payload to `http://127.0.0.1:8000/api/create-draw/` via POSTMAN using `raw/json` format:
```
{
    "plays": [
        [2, [3, 2, 1, 4, 5]],
        [2, [3, 2, 1, 4, 5]],
        [2, [3, 2, 1, 4, 5]]
    ],
    "rtp": 20000,
    "prices": {
        "1": 100,
        "2": 200,
        "3": 300,
        "4": 400,
        "5": 500
    }
}
```  
13. To check the API documentation, visit either of these:
```
http://127.0.0.1:8000/api/schema/swagger-ui/#/
http://127.0.0.1:8000/api/schema/redoc/
```
14. `DockerFile` already created, so build image using the file and run container (Optional)
15. Launch `VSCode` from terminal (Optional)
```
code .
```





