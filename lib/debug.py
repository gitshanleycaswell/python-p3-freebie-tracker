#!/usr/bin/env python3
import ipdb
from freebietracker import *
from sqlalchemy import create_engine
from models import *


from models import *

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    companies = session.query(Company).all()
    devs = session.query(Dev).all()
    freebies = session.query(Freebie).all()
    
    c1=companies[0]
    d1=devs[0]
    d2=devs[1]
    f1=freebies[0]

    ipdb.set_trace()
