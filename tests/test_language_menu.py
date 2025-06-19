from playwright.sync_api import Page, expect
import re

#Argentina
def test_language_menu_argentina(page:Page):
    print("Given the user visits the Accenture homepage")
    page.goto("https://www.accenture.com/es-es")

    print("When the user accepts all cookies")
    page.get_by_role("button", name="Aceptar todas las cookies").click()
    page.wait_for_url("https://www.accenture.com/es-es")

    print("And clicks on the language menu")
    page.get_by_text("Spain", exact=True).click()

    print("Then user should see a display with a list of countries and languages")
    page.wait_for_selector("text=Argentina (Spanish)")
    
    print("When the user clicks on Argentina (Spanish)")
    page.get_by_text("Argentina (Spanish)", exact=True).click()
    page.wait_for_url("https://www.accenture.com/ar-es")

    print("Then the user should go to the Argentinian website")
    expect(page).to_have_url("https://www.accenture.com/ar-es")
    expect(page).to_have_url(re.compile("ar-es"))
    expect(page).to_have_title(re.compile("Argentina"))
    expect(page.get_by_role("heading", name=re.compile("Juntos"))).to_be_visible

#Italy
def test_language_menu_italy(page:Page):
    print("Given the user visits the Accenture homepage")
    page.goto("https://www.accenture.com/es-es")

    print("When the user accepts all cookies")
    page.get_by_role("button", name="Aceptar todas las cookies").click()
    page.wait_for_url("https://www.accenture.com/es-es")

    print("And clicks on the language menu")
    page.get_by_text("Spain", exact=True).click()

    print("Then user should see a display with a list of countries and languages")
    page.wait_for_selector("text=Italy (Italian)")
    
    print("When the user clicks on Italy (Italian)")
    page.get_by_text("Italy (Italian)", exact=True).click()
    page.wait_for_url("https://www.accenture.com/it-it")

    print("Then the user should go to the Italian website")
    expect(page).to_have_url("https://www.accenture.com/it-it")
    expect(page).to_have_url(re.compile("it-it"))
    expect(page).to_have_title(re.compile("Italia"))
    expect(page.get_by_role("heading", name=re.compile("INSIEME"))).to_be_visible
    
#USA
def test_language_menu_usa(page:Page):
    print("Given the user visits the Accenture homepage")
    page.goto("https://www.accenture.com/es-es")

    print("When the user accepts all cookies")
    page.get_by_role("button", name="Aceptar todas las cookies").click()
    page.wait_for_url("https://www.accenture.com/es-es")

    print("And clicks on the language menu")
    page.get_by_text("Spain", exact=True).click()

    print("Then user should see a display with a list of countries and languages")
    page.wait_for_selector("text=USA (English)")
    
    print("When the user clicks on USA (English)")
    page.get_by_text("USA (English)", exact=True).click()
    page.wait_for_url("https://www.accenture.com/us-en")

    print("Then the user should go to the USA website")
    expect(page).to_have_url("https://www.accenture.com/us-en")
    expect(page).to_have_url(re.compile("us-en"))
    expect(page).to_have_title(re.compile("U.S."))
    expect(page.get_by_role("heading", name=re.compile("TOGETHER"))).to_be_visible