import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def context(playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    yield context
    context.close()
    browser.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()