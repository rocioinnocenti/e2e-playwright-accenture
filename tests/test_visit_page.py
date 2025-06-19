from playwright.sync_api import Page, expect

def test_visit(page:Page):
    print("Given user visit homepage")
    page.goto("https://www.accenture.com/es-es")
    #page.pause()
    
    #LOCATOR EXAMPLES
    #Alt text image: expect(page.get_by_alt_text("alt_text_name")).to_be_visible() (it's the alt text that appears in the HTML by inspecting the element)
    
    #get_by_title (it's the HTML title) If there is more than one with that title, you can filter it: get_by_title("HTML tutorial").filter(has_text="Tutorial")
    
    #To pick the first, last or a specific one by position: get_by_title("HTML tutorial").first() .last() .nth(0) 0 is 1, 1 is 2, and so on. 

    #By CSS selector: 
    # Look the HTML and get id: page.locator("#id") use asterisk
    # Get class: page.locator(".class") use dot
    # By element: page.locator("element") you can use it with a filter too: page.locator("element").filter(has_text="text")
    # By any atribute of the HTML: page.locator("input[nameofatribute='text']") Examples of atribute names: aria-label, autocomplete, onclick, onfocus, oninput, etc. 
    # Nesting locators: page.locator("#id").locator("a") It's going to get all the links inside of the previous locator (the one located by the id) 


    #TO TEST IN MOBILES
    #Use: python3 -m pytest tests/test_menu.py --headed --device='iPhone 12 Pro' 
    #Check that nothing changes, sometimes you may have to add an extra click to display a menu that appears directly in the desktop version, but not in the mobile one (since it's smaller)