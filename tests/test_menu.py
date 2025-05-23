from playwright.sync_api import Page, expect
import re

#Homepage - menu
def test_visit_menu_links(page:Page):
    print("Given the user visits Accenture homepage")
    #Navegation, open url in browser
    page.goto("https://www.accenture.com/es-es")
    
    print("When the user accepts all cookies")
    #Locate the element by text or role
    page.get_by_role("button", name="Aceptar todas las cookies.").click()
    page.wait_for_url("https://www.accenture.com/es-es")

    #Locate the element by role (link, button, div) and text. If it has no role and the text is repeated, then use nth (0 is the first one, 1 is the second one, etc)
    #Menu
    print("And clicks on Servicios in the menu")
    page.locator("div.rad-button__text", has_text="Servicios").nth(0).click()
    print("Then the user should see a display with a list of services and a list of industries")

    print("And clicks on Quiénes somos in the menu")
    page.locator("div.rad-button__text", has_text="Quiénes somos").nth(0).click()
    print("Then the user should see a display with three lists under: Quiénes somos, Cómo estamos organizados, and En España")

    print("And clicks on Incorpórate in the menu")
    page.locator("div.rad-button__text", has_text="Incorpórate").nth(0).click()
    print("Then the user should see a display with the title Tu carrera and three columns: Únete a nuestro equipo, Busca ofertas, and a list of technologies")

#Search - Search
def test_search(page:Page):
    print("Given the user visits Accenture homepage")
    page.goto("https://www.accenture.com/es-es")
    
    print("When the user accepts all cookies")
    page.get_by_role("button", name="Aceptar todas las cookies.").click()
    page.wait_for_url("https://www.accenture.com/es-es")

    print("And clicks on the magnifying glass icon")
    page.locator("div.rad-icon__search").click()
    page.wait_for_url("https://www.accenture.com/es-es/search/results")
    
    print("Then the user should go to the search site")
    expect(page).to_have_url("https://www.accenture.com/es-es/search/results")
    expect(page).to_have_url(re.compile("search/results"))

    #Search valid value

    #Search invalid value

#Homepage - Language menu
    #Argentina
def test_language_menu_argentina(page:Page):
    print("Given the user visits the Accenture homepage")
    page.goto("https://www.accenture.com/es-es")

    print("When the user accepts all cookies")
    page.get_by_role("button", name="Aceptar todas las cookies.").click()
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

    #Italy
def test_language_menu_italy(page:Page):
    print("Given the user visits the Accenture homepage")
    page.goto("https://www.accenture.com/es-es")

    print("When the user accepts all cookies")
    page.get_by_role("button", name="Aceptar todas las cookies.").click()
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
    
    #USA
def test_language_menu_usa(page:Page):
    print("Given the user visits the Accenture homepage")
    page.goto("https://www.accenture.com/es-es")

    print("When the user accepts all cookies")
    page.get_by_role("button", name="Aceptar todas las cookies.").click()
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