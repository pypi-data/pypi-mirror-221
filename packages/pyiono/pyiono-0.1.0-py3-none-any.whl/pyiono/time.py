from .imports import *

def utcToMjd(epoch: datetime.datetime):
    """
    Converts UTC epoch to MJD
    :param: epoch - datetime.datetime object
    :return: mjd
    """
    return astropy_time(epoch, format='datetime', scale='utc').mjd

def ut1ToMjd(epoch: datetime.datetime):
    """
    Converts UTC epoch to MJD
    :param: epoch - datetime.datetime object
    :return: mjd
    """
    return astropy_time(epoch, format='datetime', scale='ut1').mjd

