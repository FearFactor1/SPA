import pytest
from fixture.application import Application


fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    executor = request.config.getoption("--executor")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url, executor=executor)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url, executor=executor)
    fixture.session.ensure_login(username="", password="")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_exit_spa()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--baseUrl", action="store", default="")
    # Локальный ip адресс хоста где selenium
    parser.addoption("--executor", default="")