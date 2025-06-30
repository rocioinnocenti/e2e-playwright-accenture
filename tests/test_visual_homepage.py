from playwright.sync_api import Page, expect
import utils 

def test_visual_homepage(page:Page, assert_snapshot):
    print("Given user visit homepage")
    page.goto("https://www.accenture.com/es-es")
    page.wait_for_timeout(5000)

    if(utils.is_mobile(page)):
        print("Mobile detected, skipping screenshot")
        return
    else:
        print("Desktop detected, taking screenshot")
        assert_snapshot(page.screenshot())