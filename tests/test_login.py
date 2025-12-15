from playwright.sync_api import sync_playwright

def test_saucedemo_login():
    # 启动 Playwright
    with sync_playwright() as p:
        # 启动 Chromium 浏览器
        browser = p.chromium.launch(headless=False)  # headless=False 会看到浏览器界面
        # 创建一个新页面
        page = browser.new_page()

        # 打开 Saucedemo 登录页面
        page.goto("https://www.saucedemo.com/")

        # 输入用户名和密码
        page.fill('input[id="user-name"]', 'standard_user')
        page.fill('input[id="password"]', 'secret_sauce')

        # 点击登录按钮
        page.click('input[id="login-button"]')

        # 断言登录成功后是否跳转到 Inventory 页面
        page.wait_for_selector('div[class="inventory_list"]')  # 等待页面元素加载
        assert page.title() == "Swag Labs"  # 断言页面标题

        # 截图（可选，帮助你确认步骤）
        page.screenshot(path="screenshots/login_success.png")

        # 关闭浏览器
        browser.close()

