from datetime import datetime
from pyhirosi import hira2kata

module = hira2kata.get()

def get_info():
    print('Get {}'.format(module.do()))