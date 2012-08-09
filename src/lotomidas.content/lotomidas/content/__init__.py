  # -*- extra stuff goes here -*- 
from sqlalchemy.ext import declarative
ORMBase = declarative.declarative_base()


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
