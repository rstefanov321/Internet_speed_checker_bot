import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

speedtest_url = "https://www.speedtest.net/"
driver.get(speedtest_url)

time.sleep(3)

# accept cookies:
accept_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
accept_button.click()

time.sleep(2)

#click on the button GO
go_button = driver.find_element(By.CLASS_NAME, "start-text")
go_button.click()

# wait for the scan to finish
time.sleep(50)
download_speed = driver.find_element(By.CLASS_NAME, "download-speed")
upload_speed = driver.find_element(By.CLASS_NAME, "upload-speed")

# save the test values for later
download_speed_var = download_speed.text
upload_speed_var = upload_speed.text

# Make the test between the speedtest scan and the promised speeds (example given here, so that the next code works
# my ISP is compliant with their promise :) )
if float(download_speed.text) < 200 and float(upload_speed.text) < 40:
    notepad_url = "https://onlinenotepad.org/notepad"
    driver.get(notepad_url)

    # accept cookies
    time.sleep(3)
    manage_options = driver.find_element(By.CSS_SELECTOR, ".fc-primary-button p")
    manage_options.click()

    # Start writing on to a notepad
    time.sleep(1)
    write_body = driver.find_element(By.TAG_NAME, "body")
    write_body.click()
    time.sleep(1)

    phrase = f"Hi <ISP>, you promised me <dwon speed> download/ <upload speed> upload internet speeds, while I only get\n" \
             f"{download_speed_var} down and {upload_speed_var} up.\n" \
             f"Just tried it with Speedtest.net and I want my money back."

    write_body.send_keys(phrase)


time.sleep(20)
driver.quit()