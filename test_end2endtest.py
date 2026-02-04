# from playwright.sync_api import sync_playwright
# import time

# import pytest

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()

#     page.goto("https://www.tranktechnologies.com")
#     page.wait_for_timeout(5000)

   
#     def ver():
#         page.locator('(//a[text()="Verticals"])[1]').hover()
#         page.wait_for_timeout(5000)
#         page.locator('//strong[text()="Trading"]').hover()
   

    
#     @pytest.mark.smoke
#     def test_trading():
#         st='//div[@id="trading"]/ul/li[1]'
#         pt='//div[@id="trading"]/ul/li[2]'
#         cfdt='//div[@id="trading"]/ul/li[3]'
#         adt='//div[@id="trading"]/ul/li[4]'
#         algot='//div[@id="trading"]/ul/li[5]'
#         custt='//div[@id="trading"]/ul/li[6]'
#         webt='//div[@id="trading"]/ul/li[7]'
#         tr_list=[st,pt,cfdt,adt,algot,custt,webt]
        
#         for i in tr_list:
#             ver()
#             page.locator(i).wait_for(state="visible")
#             page.locator(i).click()
#             page.wait_for_load_state("load")
#             print("completedc trading menu")  
#             #page.go_back()
#     """        
#     #test_trading()
   
#     #Retail and Ecommerce
#     #@pytest.mark.smoke
#     def test_R_E():
#         page.locator('(//a[text()="Verticals"])[1]').hover()
#         #page.wait_for_timeout(5000)
#         page.locator('//strong[text()="Retail and Ecommerce"]').hover()
#     @pytest.mark.smoke
#     def test_Rerail_Ecom():
#         ecom_web='//div[@id="retailEcommerce"]/ul/li[1]'
#         ecom_app='//div[@id="retailEcommerce"]/ul/li[2]'
        
#         ecom_list=[ecom_web,ecom_app]
        
#         for i in ecom_list:
#             test_R_E()
#             page.locator(i).wait_for(state="visible")
#             page.locator(i).click()
#             page.wait_for_load_state("load")
#         print("Retail and Ecommerce")
#             #page.go_back()
            
#     #test_Rerail_Ecom()
#     #Healthcare

    
#     @pytest.mark.smoke   
#     def test_healthcare_menu():
#         page.locator('(//a[text()="Verticals"])[1]').hover()
#         #page.wait_for_timeout(5000)
#         page.locator('//strong[text()="Healthcare"]').hover()
#     @pytest.mark.smoke
#     def test_health_care_sub():
#         dait='//div[@id="healthcare"]/ul/li[1]'
#         track='//div[@id="healthcare"]/ul/li[2]'
        
#         healthcare_list=[dait,track]
        
#         for i in healthcare_list:
#             test_healthcare_menu()
#             page.locator(i).wait_for(state="visible")
#             page.locator(i).click()
#             page.wait_for_load_state("load")
#         print("completed healthcare")
#             #page.go_back()
            
#     #test_health_care_sub()
#      #Fintech
#     @pytest.mark.smoke    
#     def test_fintech_menu():
#         page.locator('(//a[text()="Verticals"])[1]').hover()
#         #page.wait_for_timeout(5000)
#         page.locator('//strong[text()="Fintech"]').hover()
#     @pytest.mark.smoke
#     def test_fintech_care_sub():
#         pos='//div[@id="fintech"]/ul/li[1]'
#         cripto='//div[@id="fintech"]/ul/li[2]'
        
#         fintech_list=[pos,cripto]
        
#         for i in fintech_list:
#             test_fintech_menu()
#             page.locator(i).wait_for(state="visible")
#             page.locator(i).click()
#             page.wait_for_load_state("load")
#         print("completed fintech")
#             #page.go_back()
            
#     #test_fintech_care_sub()

#     #Custom App
#     @pytest.mark.smoke 
#     def test_custom_menu():
#         page.locator('(//a[text()="Verticals"])[1]').hover()
#         #page.wait_for_timeout(5000)
#         page.locator('//strong[text()="Custom App"]').hover()
#     @pytest.mark.smoke
#     def test_custom_sub():
#         desktop = '//div[@id="customApp"]/ul/li[1]'
#         crm = '//div[@id="customApp"]/ul/li[2]'
#         hrm = '//div[@id="customApp"]/ul/li[3]'
#         erp = '//div[@id="customApp"]/ul/li[4]'
#         travel = '//div[@id="customApp"]/ul/li[5]'
#         e_learn = '//div[@id="customApp"]/ul/li[6]'
#         dating = '//div[@id="customApp"]/ul/li[7]'
#         real = '//div[@id="customApp"]/ul/li[8]'	
#         crm_dev = '//div[@id="customApp"]/ul/li[9]'

        
#         custom_list=[desktop,crm,hrm,erp,travel,e_learn,dating,real,crm_dev]
        
#         for i in custom_list:
#             test_custom_menu()
#             page.locator(i).wait_for(state="visible")
#             page.locator(i).click()
#             page.wait_for_load_state("load")
#         print("completed custom menu")
#             #page.go_back()
            
#     #test_custom_sub()

#     #Technogies main menu
#     @pytest.mark.smoke
#     def test_technologies():
#         page.locator('(//a[text()="Technologies"])[1]').hover()
#     @pytest.mark.smoke
#     def test_ecom_dev_sub():
#         page.locator('//strong[text()="eCommerce Development"]').hover()
#     @pytest.mark.smoke
#     def test_mobile_app_dev_seb():
#         page.locator('//strong[text()="Mobile App Development"]').hover()
#     @pytest.mark.smoke
#     def test_ai_sub():
#         print("\n started ai submenu \n")
#         test_technologies()
#         page.locator('//strong[text()="Artificial Intelligence"]').click()
#         page.wait_for_load_state("load")
    
#     @pytest.mark.smoke
#     def test_ecom_dev_child():              
#         sub_menu_items=page.locator('//div[@id="ecomm"]/ul/li')
#         number_of_items_submenu = sub_menu_items.count()
#         print(f"\n Total number chuld pages in ecoeCommerce Development submenu is {number_of_items_submenu} \n")


#         for i in range(number_of_items_submenu):
#             test_technologies()
#             test_ecom_dev_sub()
#             #sub_menu_items.nth(i).wait_for(state='visible')
#             sub_menu_items.nth(i).wait_for(state='visible')
#             sub_menu_items.nth(i).click()
#             page.wait_for_load_state("load")
#             print(page.title())
#     #test_ecom_dev_child()
#     @pytest.mark.smoke
#     def test_mobile_app_dev_child():
#         sub_menu_items=page.locator('//div[@id="mobileApp"]/ul/li')
#         number_of_items_submenu = sub_menu_items.count()
#         print(f"\n Total number chuld pages in Mobile App Development submenu is {number_of_items_submenu}\n")

#         for i in range(number_of_items_submenu):
#             test_technologies()
#             test_mobile_app_dev_seb()
#             sub_menu_items.nth(i).wait_for(state='visible')
#             sub_menu_items.nth(i).click()
#             page.wait_for_load_state("load")
#             print(page.title())

#     #test_mobile_app_dev_child()
#     #test_ai_sub()



#     #About us main manu
#     @pytest.mark.smoke
#     def test_about_us():
#         page.locator('(//a[text()="About us"])[1]').click() #About us mainmenu
#         page.wait_for_load_state("load")
#         print("About tab    :   " + page.title())
#     #Blog main menu 
#     @pytest.mark.smoke    
#     def test_Blog():
#         page.locator('(//a[text()="Blog"])[1]').click() #Blog mainmenu
#         page.wait_for_load_state("load")
#         print("Blog menu    :   " + page.title())
#     #Contact_us main menu
#     @pytest.mark.smoke
#     def test_contact_us():
#         page.locator('(//a[text()="Contact us"])[1]').click() #Contact us mainmenu
#         page.wait_for_load_state("load")
#         print("Contact us menu    :   " +page.title())
#     #portfolio main menu
#     @pytest.mark.smoke
#     def test_protfolio():
#         page.locator('(//a[text()="Portfolio"])[1]').click() # protfolio mainmenu
#         page.wait_for_url("https://www.tranktechnologies.com/portfolio")
#         print("Portfolio menu    :   " + page.title())

#     #test_about_us()
#     # test_Blog()   
#     # test_contact_us()
#     # test_protfolio()
  

#     #Get a Free Quote
#     @pytest.mark.smoke
#     def test_get_Free_Quote():
#         page.locator('(//a[text()="Get a Free Quote"])[1]').click()
#         page.locator('//input[@placeholder="Your Name"]').fill("Haritha")
#         page.locator('//input[@placeholder="Your Mail"]').fill("victory.haritha@gmail.com")
#         page.on("dialog", lambda dialog: dialog.accept())
#         page.get_by_role("button",name = "Send OTP").click()
#         page.get_by_placeholder("Enter OTP").fill("12345")
#         page.get_by_placeholder("Your Company").fill("xyz")
#         page.select_option('//select[@name="service"]',value="Web Development")
#         page.get_by_placeholder("Your Phone").fill("1234567891")
#         page.get_by_placeholder("Message").fill("text message")
        
#         #page.frame_locator('//iframe[@title="reCAPTCHA"]').locator('//div[@class="recaptcha-checkbox-checkmark"]').check()
        
        
#         page.locator('//input[@value="Submit"]').scroll_into_view_if_needed()
#         page.wait_for_timeout(3000)
#         page.locator('//input[@value="Submit"]').click()
#         print("Your application submited ")
#         page.go_back()


#     #test_get_Free_Quote()
#     #County selector
#     @pytest.mark.smoke
#     def test_country_selector():
#         page.wait_for_load_state("load")
#         page.select_option('//select[@id="countrySelector"]',value="India")
#         page.wait_for_timeout(3000)
#         print("country selected ")
    
#     #country_selector()
#     ##############    Home page ################################
#     @pytest.mark.smoke
#     def test_Home_page():
#         page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/logo/trank-logo.webp"]').click()
#         page.locator('//div[@class="cm-home-slide slick-slide slick-current slick-active"]//a[@class="cm-slider-btn cm-prim-bg"][normalize-space()="Explore More"]').click()
#     @pytest.mark.smoke
#     def test_get_in_touch_banner():    
#         test_Home_page()
#         page.locator('//form[@id="get_in_touch_banner"]//input[@placeholder="Your Name"]').fill("Haritha")
#         page.locator('//form[@id="get_in_touch_banner"]//input[@placeholder="Your Mail"]').fill("victory.haritha@gmail.com")
#         page.locator('//form[@id="get_in_touch_banner"]//input[@placeholder="Your Company"]').fill("xyz")

#         page.select_option('//form[@id="get_in_touch_banner"]//select[@name="service"]',value="Website Development")
#         page.locator('//form[@id="get_in_touch_banner"]//input[@placeholder="Your Phone"]').fill("9100955774")
#         page.locator('//form[@id="get_in_touch_banner"]//textarea[@placeholder="Message"]').fill("This is the text message")
#         page.locator("//form[@id='get_in_touch_banner']//input[@value='Submit']").click()
#         print("Your application submited through banner")
#         page.go_back()
#     @pytest.mark.smoke
#     def test_get_in_touch_body():   
#         test_Home_page() 
#         page.locator('//form[@id="get_in_touch_body"]').scroll_into_view_if_needed()
#         page.locator('//form[@id="get_in_touch_body"]//input[@placeholder="Your Name"]').fill("Haritha")
#         page.locator('//form[@id="get_in_touch_body"]//input[@placeholder="Your Mail"]').fill("victory.haritha@gmail.com")
#         page.locator('//form[@id="get_in_touch_body"]//input[@placeholder="Your Company"]').fill("xyz")

#         page.select_option('//form[@id="get_in_touch_body"]//select[@name="service"]',value="eCommerce Development")
#         page.locator('//form[@id="get_in_touch_body"]//input[@placeholder="Your Phone"]').fill("9100955774")
#         page.locator('//form[@id="get_in_touch_body"]//textarea[@placeholder="Message"]').fill("This is the text message")
#         page.locator("//form[@id='get_in_touch_body']//input[@value='Submit']").click()
#         print("Your application submited through form body")
#         page.go_back()

    
#     #test_get_in_touch_banner()
#     #test_get_in_touch_body()
#     @pytest.mark.smoke
#     def test_faqa():
#         test_Home_page()
#         page.locator('//h2[text()="FAQs"]').scroll_into_view_if_needed()
#         faq_lst=page.locator('//div[@class="cm-faq-header cm-flex-type-1"]')
#         num_items_in_lst= faq_lst.count()
#         print(f"no of items in the list with the locator is :  {num_items_in_lst}")
#         for i in range(num_items_in_lst):
#             faq_lst.nth(i).wait_for(state="visible")
#             faq_lst.nth(i).click()
#             page.wait_for_load_state("load")
#             print(faq_lst.nth(i).text_content())
           
#     #test_faqa()
    
#     def test_footer():
#         page.locator('//div[@class="cm-page-center cm-lr-pad"]').scroll_into_view_if_needed()
#         footer_lst = page.locator('//ul[@class="cm-menu-ul cm-footer-links aos-init aos-animate"]/li')
#         page.wait_for_timeout(2000)
#         num_items_footer = footer_lst.count()
#         print(f"no of items in the list with the footer locator is :  {num_items_footer}")


        

#         for i in range(1,num_items_footer):
#             #footer_lst.nth(i).wait_for(state='visible')
#             footer_lst.nth(i).click()
#             page.wait_for_load_state("load")
#             print(page.title)
            
#             page.go_back()
#             page.wait_for_timeout(2000)
#     test_footer()
#     """




        

