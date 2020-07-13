# django_select_movies

The django project provides support for selecting movies greedily to get maximum profit.

Instructions to run the django program - 

1. Setup a python environment for python3 (Not required if local system has pythonn3).
2. pip install requirements.txt (Inside the root directory)
3. python manage.py migrate
4. python manage.py makemigrations
5. python manage.py runserver
6. Hit the below mentioned url with the request body as given:-

    API url - http://<host>:<port>/movies/ - POST request
    API request - {
                        "movies": [
                            {
                                "Bala": {
                                    "end_time": "28-01-2021",
                                    "start_time": "08-01-2021"
                                }
                            },
                            {
                                "Rock": {
                                    "end_time": "30-01-2021",
                                    "start_time": "20-01-2021"
                                }
                            },
                            {
                                "PolicyMaker": {
                                    "end_time": "26-02-2021",
                                    "start_time": "29-01-2021"
                                }
                            },
                            {
                                "Brave": {
                                    "end_time": "14-02-2021",
                                    "start_time": "02-02-2021"
                                }
                            },
                            {
                                "Drive": {
                                    "end_time": "18-02-2021",
                                    "start_time": "10-02-2021"
                                }
                            },
                            {
                                "Race": {
                                    "end_time": "28-02-2021",
                                    "start_time": "15-02-2021"
                                }
                            }
                        ],
                    }

 Response as - {
                    "status_code": 200,
                    "message": "",
                    "data": [
                        {
                            "start_time": "08-01-2021",
                            "end_time": "28-01-2021",
                            "movie_name": "Bala"
                        },
                        {
                            "start_time": "02-02-2021",
                            "end_time": "14-02-2021",
                            "movie_name": "Brave"
                        },
                        {
                            "start_time": "15-02-2021",
                            "end_time": "28-02-2021",
                            "movie_name": "Race"
                        }
                    ]
                }

Response selects the movies that can give maximum profit.
