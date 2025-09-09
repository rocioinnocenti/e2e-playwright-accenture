#Code created using codegen
from playwright.sync_api import Page, expect
import re

#To use codegen: python3 -m playwright codegen --device='iPhone 12 Pro' https://www.accenture.com/es-es

#Search valid value
def test_codegen_search_valid_value(page:Page):
    print("Given the user visits Accenture search page")
    page.goto("https://www.accenture.com/es-es/search/results")

    print("And the user accepts all cookies")
    page.get_by_role("button", name="Aceptar todas").click()

    print("When the user fills the search bar with a valid value")
    page.get_by_role("textbox", name="search field").click()
    page.get_by_role("textbox", name="search field").fill("Artificial Intelligence")

    print("And the user clicks on BUSCAR button")
    page.get_by_role("button", name="search field").click()

    print("Then the user should see their search")
    expect(page.locator("#searchheromodule-59df0cdd39")).to_contain_text("Resultados para \"Artificial Intelligence\"")
    expect(page.get_by_role("heading", name="Resultados para \"Artificial")).to_be_visible()

#Search invalid value
def test_codegen_search_invalid_value(page:Page):
    print("Given the user visits Accenture search page")
    page.goto("https://www.accenture.com/es-es/search/results")

    print("And the user accepts all cookies")
    page.get_by_role("button", name="Aceptar todas").click()

    print("When the user fills the search bar with an invalid value")
    page.get_by_role("textbox", name="search field").click()
    page.get_by_role("textbox", name="search field").fill("abcdef")

    print("And the user clicks on BUSCAR button")
    page.get_by_role("button", name="search field").click()

    print("Then the user should see no results page")
    expect(page.get_by_role("heading", name="No results for \"abcdef\"")).to_be_visible()
    expect(page.locator("#searchheromodule-59df0cdd39")).to_contain_text("No results for \"abcdef\"")
    
#Search empty value
def test_codegen_search_empty_value(page:Page):
    print("Given the user visits Accenture search page")
    page.goto("https://www.accenture.com/es-es/search/results")

    print("And the user accepts all cookies")
    page.get_by_role("button", name="Aceptar todas").click()

    print("When the user fills the search bar with an empty value")
    page.get_by_role("textbox", name="search field").click()
    page.get_by_role("textbox", name="search field").fill("")

    print("And the user clicks on BUSCAR button")
    page.get_by_role("button", name="search field").click()

    print("Then the user should see no results page")
    expect(page.locator("#searchheromodule-59df0cdd39")).to_contain_text("No results for \"\"")
    expect(page.get_by_role("heading", name="No results for \"\"")).to_be_visible()