from playwright.sync_api import Page, expect

def test_visual_homepage(page:Page, assert_snapshot):
    print("Given user visit homepage")
    page.goto("https://www.accenture.com/es-es")
    assert_snapshot(page.screenshot())