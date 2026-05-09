class aboutUs_page:
    def __init__(self, page):
        self.page = page
        # about us main menu
        self.about_us = page.locator('(//a[@href="https://www.tranktechnologies.com/about"])[1]')
        # about us web development
        self.web_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/web-development-company"])[2]')
        self.cms_dev = page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]')
        self.ecommerce_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[7]')
        self.ecommerce_dev_drop = page.locator('(//i[@aria-hidden="true"])[3]')
        self.website_dev = page.locator('//a[@href="https://www.tranktechnologies.com/website-development-company"]')
        self.custom_web_dev = page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')
        
        # app develpment
        self.app_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[1]')
        self.ios_app_dev = page.locator('//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"]')
        
        self.android_app_dev = page.locator('//a[@href="https://www.tranktechnologies.com/android-mobile-app-development-company"]')
        self.andriod_app_dev_drop = page.locator('(//i[@aria-hidden="true"])[4]')
        self.android_app_dev_option = page.locator('//a[@href="https://www.tranktechnologies.com/android-app-development-company"]')
        self.app_dev_option = page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[2]')

        self.hybrid_mobile_app_dev = page.locator('//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"]')
        self.cross_platform_app_dev = page.locator('//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"]')
        self.progressive_web_app_dev = page.locator('//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company"]')


        # Graphic design
        self.graphic_design = page.locator('//a[@href="https://www.tranktechnologies.com/graphic-design-company"]')
        self.logo_design = page.locator('//a[@href="https://www.tranktechnologies.com/logo-design-company"]')
        self.pacakaging_design = page.locator('//a[@href="https://www.tranktechnologies.com/packaging-design-company"]')
        self.business_card_design = page.locator('//a[@href="https://www.tranktechnologies.com/business-cards-design-company"]')

        # ui/ux design
        self.ui_ux_design = page.locator('//a[@href="https://www.tranktechnologies.com/ui-ux-design-company"]')
        self.mobile_app_design = page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"]')
        self.responsive_web_design = page.locator('//a[@href="https://www.tranktechnologies.com/responsive-web-design-company"]')
        self.brand_identity_design = page.locator('//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company"]')


    def about_us_hover(self):
        self.about_us.hover()
        self.page.wait_for_timeout(1000)

    def about_us_web_dev_menu_clicking(self):
        self.web_developement_list = [self.web_dev, self.cms_dev, self.ecommerce_dev, self.custom_web_dev]
        for i in self.web_developement_list:
            if i == self.ecommerce_dev:
                self.about_us.hover()
                self.page.wait_for_timeout(1000)

                self.ecommerce_dev.click()
                self.page.wait_for_timeout(1000)
                self.page.go_back()
                self.ecommerce_dev_drop.click()
                self.page.wait_for_timeout(1000)
                # Handle new tab opening
                with self.page.context.expect_page() as new_page_info:
                    self.website_dev.click()
                new_page = new_page_info.value
                new_page.close()
                self.page.wait_for_timeout(1000)
            else:
                i.click()
                self.page.wait_for_timeout(1000)
                self.page.go_back()


    def about_us_app_dev_menu_clicking(self):
        self.app_development_list = [self.app_dev, self.ios_app_dev, self.android_app_dev, self.hybrid_mobile_app_dev, self.cross_platform_app_dev, self.progressive_web_app_dev]
        for i in self.app_development_list:
            self.about_us.hover()
            self.page.wait_for_timeout(1000)

            if i == self.android_app_dev:
                self.android_app_dev.click()
                self.page.wait_for_timeout(2000)
                self.page.go_back()

                # Click dropdown to show options
                self.andriod_app_dev_drop.click()
                self.page.wait_for_timeout(10000)

                with self.page.expect_popup() as popup_info:
                    self.android_app_dev_option.click()
                new_page = popup_info.value
                new_page.close()
                self.page.wait_for_timeout(1000)

                with self.page.expect_popup() as popup_info:
                    self.app_dev_option.click()
                new_page = popup_info.value
                new_page.close()
                self.page.wait_for_timeout(1000)

            else:
                # Wait for element to be visible before clicking
                i.wait_for(state="visible", timeout=5000)
                i.click()
                self.page.wait_for_timeout(5000)
                self.page.go_back()

    def about_us_graphic_design_menu_clicking(self):
        self.graphic_design_list = [self.graphic_design, self.logo_design, self.pacakaging_design, self.business_card_design]
        for j in self.graphic_design_list:
            self.about_us.hover()
            self.page.wait_for_timeout(1000)
            j.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    def about_us_ui_ux_design_menu_clicking(self):
        self.ui_ux_design_list = [self.ui_ux_design, self.mobile_app_design, self.responsive_web_design, self.brand_identity_design]
        for k in self.ui_ux_design_list:
            self.about_us.hover()
            self.page.wait_for_timeout(1000)
            k.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()