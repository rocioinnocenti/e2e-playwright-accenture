from playwright.sync_api import Page, expect

def test_visual_homepage(page:Page, assert_snapshot):
    print("Given user visit homepage")
    page.goto("https://www.accenture.com/es-es")
    page.wait_for_timeout(3000)
    assert_snapshot(page.screenshot())