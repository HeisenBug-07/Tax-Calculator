from myproject import db


class UserIncome(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.Integer, nullable=True)
    job = db.Column(db.Integer, nullable=True)
    basic = db.Column(db.Integer, nullable=False)
    da = db.Column(db.Integer, default=0)
    hra = db.Column(db.Integer, default=0)
    conveyance = db.Column(db.Integer, default=0)
    lta = db.Column(db.Integer, default=0)
    others = db.Column(db.Integer, default=0)
    rent = db.Column(db.Integer, default=0)
    professional_tax = db.Column(db.Integer, default=0)
    ac = db.Column(db.Integer, default=0)
    ad = db.Column(db.Integer, default=0)
    add = db.Column(db.Integer, default=0)
    addb = db.Column(db.Integer, default=0)
    ae = db.Column(db.Integer, default=0)
    ag = db.Column(db.Integer, default=0)
    agg = db.Column(db.Integer, default=0)
    agga = db.Column(db.Integer, default=0)
    aggc = db.Column(db.Integer, default=0)
    atta = db.Column(db.Integer, default=0)
    au = db.Column(db.Integer, default=0)

    def __init__(self, name, age, city, job, basic, da, hra, conveyance, lta, others, rent,
                 professional_tax, ac, ad, add, addb, ae, ag, agg, agga, aggc, atta, au):
        self.name = name
        self.age = age
        self.city = city
        self.job = job
        self.basic = basic
        self.da = da
        self.hra = hra
        self.conveyance = conveyance
        self.lta = lta
        self.others = others
        self.rent = rent
        self.professional_tax = professional_tax
        self.ac = ac
        self.ad = ad
        self.add = add
        self.addb = addb
        self.ae = ae
        self.ag = ag
        self.agg = agg
        self.agga = agga
        self.aggc = aggc
        self.atta = atta
        self.au = au
