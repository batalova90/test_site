import pytest

from application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def destroy(request):
    def fin():
        fixture.teardown_method()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
