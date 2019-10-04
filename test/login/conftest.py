import pytest
from fixture.application import Application


fixture = None


@pytest.fixture(scope="session")
def app2(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url)
    request.addfinalizer(fixture.destroy)
    return fixture
