import pytest
import docker  # type: ignore
from sqlmodel import create_engine, Session, SQLModel


DATABASE_URL = "postgresql://postgres:postgres@localhost/test_db"


@pytest.fixture(scope='session')
def postgres_container():
    client = docker.from_env()
    container = client.containers.run(
        "postgres:latest",
        detach=True,
        auto_remove=True,
        environment=[
            "POSTGRES_DB=test_db",
            "POSTGRES_USER=postgres",
            "POSTGRES_PASSWORD=postgres",
        ],
        port={"5432/tcp": 5432},
    )
    yield container
    container.stop()


@pytest.fixture(scope='session')
def engine(postgres_container):
    return create_engine(DATABASE_URL)


@pytest.fixture(scope='function', autouse=True)
def set_up_test_db(engine):
    SQLModel.metadata.create_all(engine)
    try:
        yield
    finally:
        SQLModel.metadata.drop_all(engine)


@pytest.fixture(scope='session')
def db_session(engine):
    with Session(engine) as session:
        yield session
