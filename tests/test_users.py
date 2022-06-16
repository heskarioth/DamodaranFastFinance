from app import schemas
from jose import jwt
#from .database import client,session
import pytest
from app.config import other_settings




def test_create_user(client,session):
    #session.query(models.table_users) --> now we can also access db values
    res = client.post("/users/",json={"email":"testing@gmail.com","password":"1234"})

    new_user = schemas.UserCreateOut(**res.json())
    assert new_user.email == "testing@gmail.com"
    assert res.status_code == 201


def test_login_user(client,test_user):
    res = client.post("/login",data={"username":test_user['email'],"password":test_user['password']})
    assert res.status_code == 200
    login_res = schemas.Token(**res.json())

    payload = jwt.decode(login_res.access_token,other_settings.secret_key, algorithms=[other_settings.algorithm])
    email : str = payload.get("sub")
    assert login_res.token_type == "bearer"
    assert email==test_user['email']
# pytest .\tests\test_users.py -s -v


@pytest.mark.parametrize("email,password,status_code",[
    ("test@gmail.com","1234",403),
    ("testing@gmail.com","wrong",403),
    (None,"1234",422),
    ("testing@gmail.com",None,422)
])
def test_incorrect_login(test_user,client,email,password,status_code):
    res = client.post("/login",data={"username":email,"password":password})
    assert  res.status_code == status_code












# def override_get_db():
#     # create a session for every api request and closes it once done.
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @pytest.fixture
# def client():
#     # this way we run create the table, after it is done, it will drop it once test is finished.
#     # run our code before we run our test
#     Base.metadata.create_all(bind=engine)
#     yield TestClient(app)
#     # run our code after our test finishes
#     Base.metadata.drop_all(bind=engine)