import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help='choose one of language: "ar",\n "ca",\n "cs",\n  "da",\n  "de",\n  "en-gb",\n  "el",\n  "es",\n  "fi",\n  "fr",\n  "it",\n  "ko",\n  "nl",\n  "pl",\n  "pt",\n  "pt-br",\n  "ro",\n  "ru",\n  sk",\n  "uk",\n  "zh-hans"')


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()