import os.path
#ZCXV Zfrom os.path import exists

#from joblib.testing import timeout
from playwright.sync_api import expect


def test_assignement(page):
    #page.goto("https://www.google.com/")
    page.goto("https://demowebshop.tricentis.com")
    #page.press('input[name="/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a"]').click()
    page.locator('a.ico-login').click()

def test_firstitem(page):
    page.goto("https://demowebshop.tricentis.com")
    page.locator('a.ico-login').click()
    page.locator('#Email').fill("gfrraqnfl@emlhub.com")
    page.locator('#Password').fill("qwerty123456")
    page.locator('#RememberMe').check()
    page.locator('//input[@value="Log in"]').click()
    page.locator("//ul[@class='top-menu']//a[normalize-space()='Computers']").hover()
    page.screenshot(path="Step 1.png")



#To extract all links given in the web page.
    block = page.locator('//input[@/html/body/div[4]/div[1]/div[4]/div[2]')
    links = page.locator("a").all()
    print(f"Total values are : {len(links)}")
    for link in links :
        text = link.inner_text()
        url = link.get_attribute("href")
        print(f"{text}---{url}")

#select First item and add to cart
    page.locator('//html/body/div[4]/div[1]/div[2]/ul[1]/li[2]/a').click()
    page.locator("//img[@title='Show products in category Notebooks']").click()
    page.locator("//input[@value='Add to cart']").click()
    page.screenshot(path="Step2 select first item & add to cart.png")


# Select another item and add to cart

    page.locator("//ul[@class='top-menu']//a[normalize-space()='Digital downloads']").click()
    page.locator("//div[@class='product-grid']//div[3]//div[1]//div[2]//div[3]//div[2]//input[1]").click()
    page.locator("//span[normalize-space()='Shopping cart']").click()
    page.locator('//*[@id="topcartlink"]/a/span[1]').click()
    page.select_option('#CountryId', value="41")

    page.locator("#termsofservice").click()
    page.locator("#checkout").click()
    page.screenshot(path="Select another item and add to cart.png")


#Billing Address #
    page.locator("xpath=//input[@onclick='Billing.save()']").click()
    page.screenshot(path="Billing Address.png")

#Shipping Address
    page.locator("xpath=//input[@onclick='Shipping.save()']").click()
    page.screenshot(path="Shipping Address.png")

#Shipping Method
    page.locator("#shippingoption_1").click()
    # page.locator("//input[@class='button-1 shipping-method-next-step-button']").click()
    page.locator("input[class='button-1 shipping-method-next-step-button']").click()
    page.screenshot(path="Shipping Method.png")

#Payment Method
    page.locator("#paymentmethod_1").click()
    page.locator("input[class='button-1 payment-method-next-step-button']").click()
    page.screenshot(path="Payment Method.png")

#Payment Information
    page.locator("input[class='button-1 payment-info-next-step-button']").click()
    page.screenshot(path="Payment Information")

#Confirm Order
    page.locator("//input[@value='Confirm']").click()
    page.screenshot(path="Confirm Order.png")

#Order detail
    page.wait_for_selector("//input[@value='Continue']")
    page.locator("//input[@value='Continue']").click()
    page.screenshot(path = "Order detail.png")
    page.wait_for_timeout(3000)


def test_webtable(page):

    page.goto("https://cosmocode.io/automation-practice-webtable/")

    #page.goto = page.goto("https://www.udemy.com/course/playwright-python-training-tutorials/learn/lecture/49127911#overview")

    Country_count = page.locator("tbody > tr ").count()
    print("country lists: ", Country_count)

    Column_count = page.locator("tbody > tr:nth-child(1) > td").count()
    print("column list", Column_count)

    # text = page.locator("tbody > tr:nth-child(2) > td:nth-child(2)")
    text = page.locator("div[class='inside-navigation'] li[id='mega-menu-item-5323'] a")
    expect(text).to_contain_text("About Us")
    print(text.inner_text())

    all_inner_text = page.locator("#countries > tbody > tr").all_inner_texts()
    for table_text in all_inner_text:
        print(table_text)


def test_shadowroot(page):

    page.goto("chrome://downloads/")

    page.locator("#searchInput").fill("vinod")
    page.wait_for_timeout(3000)

def test_mousehover(page):
    page.goto("https://www.way2automation.com/")

    page.locator("//*[@id='menu-item-27580']/a/span[2]").hover()

    page.locator("//*[@id='menu-item-27593']/a/span[2]").click()
    page.wait_for_timeout(5000)


####################################################################################
#Handling slider

def test_slider(page):
    page.goto("https://jqueryui.com/resources/demos/slider/default.html")

    slider = page.locator("//span[@class='ui-slider-handle ui-corner-all ui-state-default']")

    bounding_box = slider.bounding_box()

    start_x = bounding_box["x"] + bounding_box["width"] / 2
    start_y = bounding_box ["y"] + bounding_box ["height"] / 2

    page.mouse.move(start_x, start_y)

    page.mouse.down()

    page.mouse.move(start_x + 400, start_y)

    page.mouse.up()

    page.wait_for_timeout(3000)

###########################################################################################
#Handling Resizable

def test_resizable(page):
    page.goto("https://jqueryui.com/resources/demos/resizable/default.html")

    resizable = page.locator("//*[@id='resizable']/div[3]")

    bounding_box = resizable.bounding_box()

    start_x = bounding_box["x"] + bounding_box["width"] / 2
    start_y = bounding_box ["y"] + bounding_box ["height"] / 2

    page.mouse.move(start_x, start_y)

    page.mouse.down()

    page.mouse.move(start_x + 400, start_y + 400)

    page.mouse.up()

    page.wait_for_timeout(3000)

def test_draganddrop(page):
    page.goto("https://jqueryui.com/resources/demos/droppable/default.html")

    draggable = page.locator("#draggable")
    droppable = page.locator("#droppable")

    draggable_box = draggable.bounding_box()
    droppable_box = droppable.bounding_box()

    page.mouse.move(
        draggable_box["x"] + draggable_box["width"]/2,
        draggable_box["y"] + draggable_box["height"]/2
    )

    page.mouse.down()

    page.mouse.move(
        droppable_box["x"] + droppable_box ["width"]/2,
        droppable_box["y"] + droppable_box ["height"]/2
    )

    page.mouse.up()

    page.wait_for_timeout(3000)


def test_rightclick(page):
    page.goto("https://deluxe-menu.com/popup-mode-sample.html")

    page.locator("//p[2]/img").click(button="right")
    page.wait_for_timeout(3000)

###########################################################################################
#Assignement


def test_assignemen(page):
    page.goto("https://deluxe-menu.com/popup-mode-sample.html")

    page.locator("//p[2]/img").click(button="right")

    page.locator("#dm2m1i1tdT").hover()

    page.wait_for_timeout(5000)

    page.locator("#dm2m2i2tdT").click()

    page.wait_for_timeout(5000)
############################################################################
#Handling alert

def test_alert(page):

    def dialog_handler(dialog):
        page.wait_for_timeout(3000)
        print(dialog.message)
        dialog.accept()

    page.on("dialog", dialog_handler)

    page.goto("https://mail.rediff.com/cgi-bin/login.cgi")
    page.locator("[type='submit']").click()

############################################################################################################
#handeling Frames

def test_hframe(page):
    page.goto("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit")

    frame = page.frame_locator("#iframeResult")

    frame.locator("#fname").clear()
    frame.locator("#fname").fill("Vinod")

    frame.locator("#lname").clear()
    frame.locator("#lname").fill("vyash")

    frame.locator("[type='Submit']").click()

    page.wait_for_timeout(3000)


################################################################################################################
#Handeling tabs and popup

def test_tabs_and_popup(page):
    page.goto("https://sso.teachable.com/secure/673/identity/sign_up/otp" , timeout=6000)

    with page.expect_popup() as popup_info:
        page.locator("text = Privacy").nth(0).click()

        popup = popup_info.value

        popup.locator("[id='header-sign-up-btn']").click()
        popup.locator("#name").fill("vinod@gmail.com")
        popup.wait_for_selector("#name", state="visible")

        page.wait_for_timeout(3000)
        popup.close()


#######################################################################################################
#Evaluating Javascript

def test_JavaScript(page):
    page.goto("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit")

    frame = page.frame_locator("#iframeResult")

    frame.locator("#fname").clear()
    frame.locator("#fname").fill("Vinod")

    frame.locator("#lname").clear()
    frame.locator("#lname").fill("vyash")

    frame.locator("[type='submit']").evaluate("(element) => {element.style.border = '3px solid red';}")

    page.wait_for_timeout(3000)

################################################################################################################
#Capturing screenshot

def test_Jscreenshot(page):
    page.goto("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit")

    frame = page.frame_locator("#iframeResult")

    frame.locator("#fname").clear()
    frame.locator("#fname").fill("Vinod")

    frame.locator("#lname").clear()
    frame.locator("#lname").fill("vyash")

    frame.locator("[type='submit']").evaluate("(element) => {element.style.border = '3px solid red';}")

    #To take element screenshot.
    frame.locator("[type = 'submit']").screenshot(path = "screenshot/element.png")

    page.wait_for_timeout(3000)

    #To take page screenshot.
    page.screenshot(path="screenshot/page.png")

#######################################################################################################################################
#Handiling Basic Auth

def test_screenshot(page,browser):
    context = browser.new_context (
        http_credentials={"username":"admin" , "password":"admin"}
    )
    page= context.new_page()

    page.goto("https://the-internet.herokuapp.com/basic_auth" )
    page.wait_for_timeout(5000)

##################################################################################################################################################33
#Upload file

def test_upload_file(page):
    page.goto("https://www.way2automation.com/way2auto_jquery/registration.php#load_box")

    page.locator("#register_form > fieldset:nth-child(9) > input[type=file]").set_input_files("C:\\Users\\Lenovo\\OneDrive\\Pictures\\BingImageOfTheDay.jpg")

    page.wait_for_timeout(3000)
###################################################################################################
#upload multiple files

def test_upload_multiple_files(page):
    page.goto("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_fileupload_multiple")

    frame = page.frame_locator("#iframeResult")

    frame.locator("#myFile").set_input_files(["C:\\Users\\Lenovo\\OneDrive\\Pictures\\BingImageOfTheDay.jpg",
                                              "C:\\Users\\Lenovo\\OneDrive\\Pictures\\My PAN card.jpg"])

    page.wait_for_timeout(3000)

#################################################################################################################################
#Download file

def test_download_file(page):
    page.goto("https://www.selenium.dev/downloads/", timeout=4000)

    with page.expect_download()as  download_info:
        page.locator("body > div > main > div:nth-child(5) > div.col-sm-6.py-3.ps-0.pe-3 > div > div > p:nth-child(1) > a").click()

    download = download_info.value

    project_directory = os.path.join(os.path.dirname(os.getcwd()),"downloads")
    os.makedirs(project_directory, exist_ok=True)

    file_path = os.path.join(project_directory, "selenium.jar")
    download.save_as(file_path)

    print(f"file downloaded to : {file_path}")
    # page.wait_for_timeout(5000)
