from app import schemas
from .database import client,session


def test_create_user(client,session):
    #session.query(models.table_users) --> now we can also access db values
    res = client.post("/users/",json={"email":"testing@gmail.com","password":"1234"})

    new_user = schemas.UserCreateOut(**res.json())
    assert new_user.email == "testing@gmail.com"
    assert res.status_code == 201

# pytest .\tests\test_users.py -s -v



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