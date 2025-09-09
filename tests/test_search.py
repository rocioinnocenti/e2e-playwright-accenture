#Code without using codegen
from playwright.sync_api import Page, expect
import re

#Search - Search
def test_search(page:Page):
    print("Given the user visits Accenture homepage")
    page.goto("https://www.accenture.com/es-es")
    
    print("When the user accepts all cookies")
    page.get_by_role("button", name="Aceptar todas las cookies").click()
    page.wait_for_url("https://www.accenture.com/es-es")

    print("And clicks on the magnifying glass icon")
    page.locator("div.rad-icon__search").click()
    page.wait_for_url("https://www.accenture.com/es-es/search/results")
    
    print("Then the user should go to the search page")
    expect(page).to_have_url("https://www.accenture.com/es-es/search/results")
    expect(page).to_have_url(re.compile("search/results"))
    expect(page).to_have_title(re.compile("Search Page"))
    expect(page.get_by_role("heading", name="Búsquedas populares", exact=True, level=2)).to_be_visible()

#Search valid value
def test_search_valid_value(page:Page):
    print("Given the user visits Accenture search page")
    page.goto("https://www.accenture.com/es-es/search/results")
    
    print("And the user accepts all cookies")
    page.get_by_role("button", name="Aceptar todas las cookies").click()
    page.wait_for_url("https://www.accenture.com/es-es/search/results")

    print("When the user fills the search bar with a valid value")
    page.get_by_placeholder("Type to search...").clear()
    page.get_by_placeholder("Type to search...").fill("Artificial Intelligence")
    
    print("And the user clicks on BUSCAR button")
    page.get_by_role("button", name="search field").click()

    print("Then the user should see their search")
    expect(page).to_have_url(re.compile("Artificial"))
    expect(page.get_by_role("heading", name="Resultados para \"Artificial Intelligence\"", exact=True, level=2)).to_be_visible()

#Search invalid value
def test_search_invalid_value(page:Page):
    print("Given the user visits Accenture search page")
    page.goto("https://www.accenture.com/es-es/search/results")
    
    print("When the user accepts all cookies")
    page.get_by_role("button", name="Aceptar todas las cookies").click()
    page.wait_for_url("https://www.accenture.com/es-es/search/results")

    print("And the user fills the search bar with an ivalid value")
    page.get_by_placeholder("Type to search...").clear()
    page.get_by_placeholder("Type to search...").fill("fghijk")

    print("And the user clicks on BUSCAR button")
    page.get_by_role("button", name="search field").click()

    print("Then the user should see their search")
    expect(page).to_have_url(re.compile("fghijk"))
    expect(page.get_by_role("heading", name="No results for \"fghijk\"", exact=True, level=2)).to_be_visible()

#Search empty value
def test_search_empty_value(page:Page):
    print("Given the user visits Accenture search page")
    page.goto("https://www.accenture.com/es-es/search/results")
    
    #print("And the user accepts all cookies")
    #page.get_by_role("button", name="Aceptar todas las cookies").click()
    #page.wait_for_url("https://www.accenture.com/es-es/search/results")

    print("When the user fills the search bar with an empty value")
    page.get_by_placeholder("Type to search...").clear()

    print("And the user presses Enter")
    page.get_by_placeholder("Type to search...").press("Enter")

    print("Then the user should see their search")
    expect(page.get_by_role("heading", name="No results for \"\"", exact=True, level=2)).to_be_visible()