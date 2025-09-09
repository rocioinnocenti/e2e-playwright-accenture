from playwright.sync_api import Page, expect
import re
import utils

#Homepage - menu
def test_visit_menu_links(page:Page):
    print("Given the user visits Accenture homepage")
    #Navegation, open url in browser
    page.goto("https://www.accenture.com/es-es")
    
    print("When the user accepts all cookies")
    #Locate the element by text or role
    page.get_by_role("button", name="Aceptar todas las cookies").click()
    page.wait_for_url("https://www.accenture.com/es-es")

    #Locate the element by role (link, button, div) and text. If it has no role and the text is repeated, then use nth (0 is the first one, 1 is the second one, etc)
    #See if it's mobile or desktop
    if(utils.is_mobile(page)):
        page.get_by_role("button", name="menu", exact=True).click()

    #Menu
    #print("And clicks on Servicios in the menu")
    page.get_by_role("button", name="Qué hacemos", exact=True).click()
    #print("Then the user should see a display with a list of services and a list of industries")
    expect(page.get_by_role("link", name="Cloud")) 

    #Go back to be able to select something else in the mobile menu
    if(utils.is_mobile(page)):
        page.get_by_role("button", name=" Back").click()

    print("And clicks on Quiénes somos in the menu")
    page.get_by_role("button", name="Quiénes somos", exact=True).click()
    print("Then the user should see a display with three lists under: Quiénes somos, Cómo estamos organizados, and En España")
    expect(page.get_by_role("link", name="Quiénes somos", exact=True))
    
    #Go back to be able to select something else in the mobile menu
    if(utils.is_mobile(page)):
        page.get_by_role("button", name=" Back").click()

    print("And clicks on Incorpórate in the menu")
    page.get_by_role("button", name="Incorpórate").click()
    print("Then the user should see a display with the title Tu carrera and three columns: Únete a nuestro equipo, Busca ofertas, and a list of technologies")
    expect(page.get_by_role("link", name="Tu carrera"))