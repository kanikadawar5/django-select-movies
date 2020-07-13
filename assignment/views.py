import _datetime

from rest_framework.response import Response
from rest_framework import viewsets

from .serialisers import MoviesSerializer
from .models import Values


def unix_to_timestamp(unix):
    return _datetime.datetime.utcfromtimestamp(unix).strftime('%d-%m-%Y')


def timestamp_to_unix(timestamp):
    return _datetime.datetime.timestamp(_datetime.datetime.strptime(timestamp, '%d-%m-%Y'))


def find_max_profit(movies):

    start_times = []
    end_times = []
    for movie in movies:
        st = movie.get(list(movie.keys())[0])['start_time']
        et = movie.get(list(movie.keys())[0])['end_time']
        start_times.append(timestamp_to_unix(st))
        end_times.append(timestamp_to_unix(et))

    times = list(zip(start_times, end_times))
    times.sort(key=lambda x: x[1])

    st = unix_to_timestamp(start_times[0])
    et = unix_to_timestamp(end_times[0])
    movie_name = ""
    for movie in movies:
        if movie.get(list(movie.keys())[0])['start_time'] == st and movie.get(list(movie.keys())[0])['end_time'] == et:
            for m in movie:
                movie_name = m
    S = [{
        'start_time': st,
        'end_time': et,
        "movie_name": movie_name
    }]
    j = 1
    n = len(start_times)
    for i in range(2, n):
        if start_times[i] >= end_times[j]:
            st = unix_to_timestamp(start_times[i])
            et = unix_to_timestamp(end_times[i])
            movie_name = ""
            for movie in movies:
                if movie.get(list(movie.keys())[0])['start_time'] == st and movie.get(list(movie.keys())[0])['end_time'] == et:
                    for m in movie:
                        movie_name = m
            res = {
                'start_time' : st,
                'end_time' : et,
                "movie_name" : movie_name
            }
            print("res", res)
            S.append(res)
            j = i

    return S
    pass


class MoviesSet(viewsets.ModelViewSet):
    queryset = Values.objects.all().order_by('request_id')
    serializer_class = MoviesSerializer

    def perform_create(self, serializer):
        try:
            return serializer.save()
        except:
            message = "Error while creating"
            raise ValueError(message)

    def create(self, request, *args, **kwargs):
        try:
            result = {
                "status_code": 200,
                "message": "",
                "data": {}
            }
            data = request.data
            serializer = self.get_serializer(data=data)
            if serializer.is_valid():
                self.perform_create(serializer)
                if 'movies' in data and isinstance(data['movies'], list):
                    data = find_max_profit(data['movies'])
                    result['data'] = data
                    return Response(result)
        except ValueError as e:
            result = {
                "status_code": 400,
                "message": str(e),
                "data": {}
            }
            return Response(result)
