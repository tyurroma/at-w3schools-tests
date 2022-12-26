import pytest

from sdk.utils.config import Config


def pytest_addoption(parser):
    parser.addoption('--ep', '--endpoint', action='store', dest='ENDPOINT', help='site url')


def get_option(options):
    for option in options:
        if option is not None:
            return option


@pytest.fixture(scope='session')
def endpoint(request):
    request.config.ENDPOINT = get_option([
        Config.get_variable(variable_name='endpoint', config_section='config'),
        None,
    ])

    return request.config.ENDPOINT
