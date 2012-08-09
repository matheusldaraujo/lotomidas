import os
import tempfile
import sqlalchemy

from zope.component import provideUtility
from z3c.saconfig.utility import EngineFactory
from z3c.saconfig.utility import GloballyScopedSession
class OptiluxCinemaContent(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)
    
    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import lotomidas.content
        xmlconfig.file('configure.zcml', lotomidas.content, context=configurationContext)
    
        # Make sure initialize() is called
        z2.installProduct(app, 'lotomidas.content')
    
        # Create database in a temporary file
        fileno, self.dbFileName = tempfile.mkstemp(suffix='.db')
        dbURI = 'sqlite:///%s' % self.dbFileName
        dbEngine = sqlalchemy.create_engine(dbURI)
        lotomidas.content.ORMBase.metadata.create_all(dbEngine)
        
        # Register z3c.saconfig utilities for testing
        engine = EngineFactory(dbURI, echo=False,
        convert_unicode=False)
        provideUtility(engine, name=u"ftesting")
        session = GloballyScopedSession(engine=u"ftesting",twophase=False)
        provideUtility(session)


    def tearDownZope(self, app):
        # Uninstall products installed above
        z2.uninstallProduct(app, 'optilux.cinemacontent')
        
        # Clean up the database
        os.unlink(self.dbFileName)
    
    def setUpPloneSite(self, portal):
        applyProfile(portal, 'optilux.cinemacontent:default')

