from .imports import *

def getIersTable():
    """
    :return: iers table
    """

    try:
        iers_b_file = iers.download_file(iers.IERS_B_URL, cache=True)
        iers_b = iers.IERS_B.open(iers_b_file)
        iers.IERS.iers_table = iers_b
    except:
        try:
            iers_a_file = iers.download_file(iers.IERS_A_URL, cache=True)
            iers_a = iers.IERS_A.open(iers_a_file)
            iers.IERS.iers_table=iers_a
        except:
            print('Could not load IERS_B nor IERS_A !')

    return iers.IERS.iers_table