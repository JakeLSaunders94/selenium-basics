import functions as wd
import time

def check_for_posts():
    group_pages = [
        'https://www.facebook.com/groups/1673228999599587/',
        'https://www.facebook.com/groups/182986305659467/',
        'https://www.facebook.com/groups/supportingsmallukbusinesses/',
        'https://www.facebook.com/groups/361032737422561/',
        'https://www.facebook.com/groups/1578560309058402/'
    ]

    driver = wd.create_driver_window(False)

    wd.navigate_to_page(driver, group_pages[0])

    # Set to sort by recent posts
    possible_id_names = [".//*[contains(@id,'u_0_2p')]",
                         ".//*[contains(@id,'u_0_2t')]"]
    wd.check_for_and_click_from_list_of_xpaths(driver, possible_id_names)
    time.sleep(1.5)
    status, response = wd.check_element_exists(driver, ".//*[contains(@id,'_54nc')]", 5)
    if not status:
        raise LookupError("Cannot find element")

    possible_id_names = [".//*[contains(@id,'_54nc')]"]
    wd.check_for_and_click_from_list_of_xpaths(driver, possible_id_names)
    time.sleep(50)





check_for_posts()