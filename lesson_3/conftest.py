import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def chrome_options():
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--window-size=1080,1080')

    yield options

@pytest.fixture
def driver(chrome_options):
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver


@pytest.fixture
def driver_impl(chrome_options):
    service = Service(executable_path=ChromeDriverManager().install())
    driver_impl = webdriver.Chrome(service=service, options=chrome_options)
    driver_impl.implicitly_wait(15)

    yield driver_impl

@pytest.fixture
def driver_expl(chrome_options):
    service = Service(executable_path=ChromeDriverManager().install())
    driver_expl = webdriver.Chrome(service=service, options=chrome_options)

    yield driver_expl

@pytest.fixture
def wait(driver_expl):
    wait = WebDriverWait(driver_expl, 10, poll_frequency=1)

    yield wait