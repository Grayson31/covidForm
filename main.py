from selenium import webdriver
import time


driver = webdriver.Edge(executable_path="c:\selenium browser drivers\msedgedriver.exe")

driver.get("https://uoguelph.eu.qualtrics.com/jfe/form/SV_6lh1bNRMHDEU1OR")

time.sleep(2)

fname = "John Smith"

email = "youremail@domain.com"

phone = "123-456-6789"


def covid_form():
    btn_yes = driver.find_element_by_id('QID3-1-label')
    btn_yes.click()

    p1_next = driver.find_element_by_id('NextButton')

    p1_next.click()

    time.sleep(2)

    p2_next = driver.find_element_by_id('NextButton')

    p2_next.click()

    time.sleep(2)

    p3_cat = driver.find_element_by_id('QID9-1-label')

    p3_cat.click()

    p3_next = driver.find_element_by_id('NextButton')

    p3_next.click()
    time.sleep(1)

    p4_yes = driver.find_element_by_id('QID11-1-label')

    p4_yes.click()

    time.sleep(1)

    p4_next = driver.find_element_by_id('NextButton')

    p4_next.click()

    time.sleep(2)

    p5_yes = driver.find_element_by_id('QID12-1-label')

    p5_yes.click()

    p5_next = driver.find_element_by_id('NextButton')

    p5_next.click()

    time.sleep(1)

    input_fname = driver.find_element_by_id('QR~QID5')

    input_email = driver.find_element_by_id('QR~QID7')

    input_number = driver.find_element_by_id('QR~QID8')

    input_fname.send_keys(fname)
    time.sleep(1)
    input_email.send_keys(email)
    time.sleep(1)
    input_number.send_keys(phone)
    time.sleep(1)

    p6_next = driver.find_element_by_id("NextButton")
    p6_next.click()

    time.sleep(2)

    no_symptoms = driver.find_element_by_id('QID23-2-label')
    no_symptoms.click()

    time.sleep(2)

    submit = driver.find_element_by_id('NextButton')
    submit.click()

    time.sleep(2)

    driver.close()

    print("Form was filled out!")



covid_form()
