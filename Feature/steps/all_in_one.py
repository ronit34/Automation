from selenium.webdriver.common.by import By

def masterbalance(context,amt):
    context.driver.find_element(By.ID, "menu_master_balance").click()
    context.driver.find_element(By.ID, "update_balance").click()
    context.driver.find_element(By.ID, "amount").send_keys(amt)
    context.driver.find_element(By.ID, "add").click()