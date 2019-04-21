import pymongo
import pytest

from sshtunnel import SSHTunnelForwarder

from utils import Log

# init the mongodb config
#TODO should these settings move to the config file?
MONGO_HOST = '182.140.144.180'
MONGO_DB = 'sndo'
MONGO_USER = 'staff'
MONGO_PASS = 'zxt@56$%998*'
BIND_HOST = '127.0.0.1'
BIND_PORT = 27018
# mongodb connect with ssh tunnel
server = SSHTunnelForwarder(
    MONGO_HOST,
    ssh_username=MONGO_USER,
    ssh_password=MONGO_PASS,
    remote_bind_address=(BIND_HOST, BIND_PORT)
)


@pytest.fixture(scope='session', autouse=True)
def base():
    """The base test for all other test cases. All tests should 
    mark the annotation as usefixtures('base').

    Establish the test. Same as unit test, the setup steps should 
    be front of segment 'yield', the teardown steps shoule be after 
    of segment 'yield'.

    The segment 'yield' is the generator for test cases execution.

    Example:
        @pytest.mark.userfixtures('base')
        class TestExample(object):
            ...
    """    
    log = Log.getlog('Base')
    log.info('set up test')
    yield
    log.info('tear down test')


@pytest.fixture(scope="session")
def mongo_connection():
    """Start the ssh tunnel for mongodb and connect db. 
    This func NOT RECOMMAND USED in common test case steps.

    Returns:
        Return the mongodb connection instance.
    """ 
    server.start()
    client = pymongo.MongoClient(BIND_HOST, server.local_bind_port)
    return client


@pytest.fixture(scope="session")
def mongodb(mongo_connection):
    """Mongodb connection instance for test cases.
    This func RECOMMAND USED in common test case steps.
    After yield segment, the ssh tunnel stopped.

    Returns:
        Yield the mongodb connection instance.
    """ 
    yield mongo_connection
    server.stop()
