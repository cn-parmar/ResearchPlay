import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Search for Googl")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_label("Toggle Todo").check()
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Learn python")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.locator("li").filter(has_text="Learn python").get_by_label("Toggle Todo").check()
    page.get_by_role("link", name="Active").click()
    page.get_by_role("link", name="Completed").click()
    page.get_by_role("button", name="Clear completed").click()
    page.get_by_placeholder("What needs to be done?").click(button="right")
    expect(page.get_by_placeholder("What needs to be done?")).to_be_visible()
    expect(page.get_by_placeholder("What needs to be done?")).to_be_empty();
    
