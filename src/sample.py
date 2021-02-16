from datetime import datetime


def get_current_datetime(tz):
    """
    .:genpydoc:.
    Write a description here.

    Parameters:
    ----------
    param1: type
        Description of param1.
    paramN: type
        Description of paramN.

    Returns:
    ----------
    return_var: type
        Description of return var.
    """
    return datetime.now(tz=tz)


def get_knowing_libs():
    """
    .:genpydoc:.
    Write a description here.

    Parameters:
    ----------
    param1: type
        Description of param1.
    paramN: type
        Description of paramN.

    Returns:
    ----------
    return_var: type
        Description of return var.
    """
    return ['numpy',
            'pandas',
            'pytest',
            'unittest'
            'pyspark'
            'pendulum'
            'pymongo'
            'airflow'
            'boto']
