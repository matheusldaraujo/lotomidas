import sqlalchemy
def script(arg):
    engine = sqlalchemy.create_engine('mysql://root:chronos@localhost/loteria?charset=utf8&use_unicode=0', pool_recycle=3600)
    import ipdb;ipdb.set_trace()
    connection = engine.connect()
import ipdb;ipdb.set_trace()
script()
