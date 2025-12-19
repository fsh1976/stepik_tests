import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language: es, en, fr, etc."
    )


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("--language")

    options = Options()
    options.add_experimental_option(
        "prefs", {"intl.accept_languages": language}
    )

    print(f"\nstart chrome browser with language = {language}")
    browser = webdriver.Chrome(options=options)
    yield browser
    time.sleep(15)
    print("\nquit browser")
    browser.quit()

