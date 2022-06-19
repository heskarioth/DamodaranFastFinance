from curses.ascii import CR
from passlib.context import CryptContext
import logging


pwd_context = CryptContext(schemes=['bcrypt'],deprecated="auto")
## pasword functions
def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_pwd,hashed_pwd):
    return pwd_context.verify(plain_pwd,hashed_pwd)


##### logging functionality

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(module)s:%(message)s')
file_handler = logging.FileHandler('user_searches.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

