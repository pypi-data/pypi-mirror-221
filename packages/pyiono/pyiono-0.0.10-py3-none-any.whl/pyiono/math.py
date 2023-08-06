from .imports import *

def square(a: float):
    """
    :param: a
    :return: square of a
    """
    return a*a

def dXyzToDneuMatrix ( lat: float, lon: float ):
    """
    Rotation matrix for xyz to neu transfotmations
    :param: lat
    :param: lon
    :return: ret 3x3 matrix
    """

    sinlat = np.sin ( lat )
    coslat = np.cos ( lat )
    sinlon = np.sin ( lon )
    coslon = np.cos ( lon )
    ret= np.zeros((3,3))

    ret [0][0]= -sinlat * coslon
    ret [0][1]= -sinlat * sinlon
    ret [0][2]=  coslat
    ret [1][0]= -sinlon
    ret [1][1]=  coslon
    ret [1][2]=  0.0
    ret [2][0]=  coslat * coslon
    ret [2][1]=  coslat * sinlon
    ret [2][2]=  sinlat

    return ret

