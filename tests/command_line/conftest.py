import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="http://ya.ru",
        help="tested url"
    )
    parser.addoption(
        "--status-code",
        default=200,
        help="expected status-code"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return int(request.config.getoption("--status-code"))