from django.db import models


# Create your models here.
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField


def my_default():
    return {'foo': 'bar'}


class Values(models.Model):
    request_id = models.AutoField(verbose_name="Request ID", primary_key=True)
    movies = ArrayField(models.CharField(max_length=20, blank=True, null=True),
                        verbose_name="movies", blank=True, null=True)
    movies = ArrayField(JSONField(default=my_default))
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'movies'
        verbose_name = "Kanika Dawar Assignment"


# {
#   "movies" : [
#     {"Bala": {
#         "start_time" : "08-01-2021",
#         "end_time" : "28-01-2021"
#     }
#     },
#     {"Rock": {
#         "start_time" : "20-01-2021",
#         "end_time" : "30-01-2021"
#     }
#     },
#     {"PolicyMaker": {
#         "start_time": "29-01-2021",
#         "end_time": "26-02-2021"
#     }
#     },
#     {"Brave": {
#         "start_time": "02-02-2021",
#         "end_time": "14-02-2021"
#     }
#     },
#     {"Drive": {
#         "start_time": "10-02-2021",
#         "end_time": "18-02-2021"
#     }
#     },
#     {"Race": {
#         "start_time": "15-02-2021",
#         "end_time": "28-02-2021"
#     }
#     }
# ]
# }
# ['%d-%m-%Y']


