from playwright.sync_api import Page, expect
import re
import utils

#Argentina
def test_language_menu_argentina(page:Page):
    print("Given the user visits the Accenture homepage")
    page.goto("https://www.accenture.com/es-es")

    print("When the user accepts all cookies")
    page.get_by_role("button", name="Aceptar todas").click()
    page.wait_for_url("https://www.accenture.com/es-es")

    #See if it's mobile or desktop
    if(utils.is_mobile(page)):
        print("And clicks on the menu")
        page.get_by_role("button", name="menu", exact=True).click()
        print("And clicks on the language menu")
        page.get_by_role("button", name="Country and language selector").click()
    else:
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

#Australia 
def test_language_menu_australia(page:Page):
    print("Given the user visits the Accenture homepage")
    page.goto("https://www.accenture.com/es-es")

    print("When the user accepts all cookies")
    page.get_by_role("button", name="Aceptar todas").click()
    page.wait_for_url("https://www.accenture.com/es-es")

    #See if it's mobile or desktop
    if(utils.is_mobile(page)):
        print("And clicks on the menu")
        page.get_by_role("button", name="menu", exact=True).click()
        print("And clicks on the language menu")
        page.get_by_role("button", name="Country and language selector").click()
    else:
        print("And clicks on the language menu")
        page.get_by_text("Spain", exact=True).click()

    print("Then user should see a display with a list of countries and languages")
    page.wait_for_selector("text=Australia (English)") 
    
    print("When the user clicks on Australia (English)")
    page.get_by_text("Australia (English)", exact=True).click()
    page.wait_for_url("https://www.accenture.com/au-en")

    print("Then the user should go to the Australian website")
    expect(page).to_have_url("https://www.accenture.com/au-en")
    expect(page).to_have_url(re.compile("au-en"))
    expect(page).to_have_title(re.compile("Australia"))
    expect(page.get_by_role("heading", name=re.compile("TOGETHER"))).to_be_visible
    
#Austria
def test_language_menu_austria(page:Page):
    print("Given the user visits the Accenture homepage")
    page.goto("https://www.accenture.com/es-es")

    print("When the user accepts all cookies")
    page.get_by_role("button", name="Aceptar todas").click()
    page.wait_for_url("https://www.accenture.com/es-es")

    #See if it's mobile or desktop
    if(utils.is_mobile(page)):
        print("And clicks on the menu")
        page.get_by_role("button", name="menu", exact=True).click()
        print("And clicks on the language menu")
        page.get_by_role("button", name="Country and language selector").click()
    else:
        print("And clicks on the language menu")
        page.get_by_text("Spain", exact=True).click()

    print("Then user should see a display with a list of countries and languages")
    page.wait_for_selector("text=Austria (German)")
    
    print("When the user clicks on Austria (German)")
    page.get_by_text("Austria (German)", exact=True).click()
    page.wait_for_url("https://www.accenture.com/at-de")

    print("Then the user should go to Austria's website")
    expect(page).to_have_url("https://www.accenture.com/at-de")
    expect(page).to_have_url(re.compile("at-de"))
    expect(page).to_have_title(re.compile("Österreich"))
    expect(page.get_by_role("heading", name=re.compile("GEMEINSAM"))).to_be_visible