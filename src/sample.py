from datetime import datetime


def get_current_datetime(tz):
    return datetime.now(tz=tz)


def get_knowing_libs():
    return ['numpy',
            'pandas',
            'pytest',
            'unittest'
            'pyspark'
            'pendulum'
            'pymongo'
            'airflow'
            'boto']
