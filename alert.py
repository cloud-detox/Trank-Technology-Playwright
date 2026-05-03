from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://demo.automationtesting.in/Alerts.html")
    page.wait_for_timeout(2000)
#Alert with OK buttom   
    alert_ok=page.locator('//button[@onclick="alertbox()"]')
    page.once("dialog", lambda dialog: dialog.accept())
    alert_ok.click()
    page.wait_for_timeout(5000)
#Alert with cancel button
    alert_ok_cancel=page.locator('//a[@href="#CancelTab"]')
    alert_ok_cancel.click()
    button_ok_cancel=page.locator('//button[@onclick="confirmbox()"]')
    page.once("dialog", lambda dialog: dialog.dismiss())
    button_ok_cancel.click()
    page.wait_for_timeout(5000)
#Alert with text box
    alert_with_text=page.locator('//a[@href="#Textbox"]')
    alert_with_text.click()
    button_with_text=page.locator('//button[@onclick="promptbox()"]')
    page.once("dialog", lambda dialog: dialog.accept("Karan"))
    button_with_text.click()
    page.wait_for_timeout(5000)
    
    page.close()