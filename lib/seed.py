#!/usr/bin/env python3
from models import *
from freebietracker import *

convention = {
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s'
}
session.query(Company).delete()
session.query(Freebie).delete()
session.query(Dev).delete()

c1 = Company(name = "Facebook", founding_year = 2004)
c2 = Company(name = "Google", founding_year= 1998)
c3 = Company(name = 'Tesla', founding_year=2003)
session.add_all([c1, c2, c3])
session.commit()

d1 = Dev(name = "Bob")
d2 = Dev(name="Kevin")
session.add_all([d1, d2])
session.commit()

f1 = Freebie(item_name ="Hat", value=20, company_id = c1.id, dev_id = d1.id)
session.add(f1)
session.commit()

