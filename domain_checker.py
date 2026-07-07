from playwright.sync_api import sync_playwright
import os
import time
import random

start_time = time.perf_counter()

domain_list = ["greenmountains.ae", "yahoo.com", "biorus.ae", "188[.]92[.]255[.]57", "pragmaticus[.]ru"]
safe_text = "No security vendors flagged this domain as malicious"
safe_rating = "0"
suspicious_list = []
timeout = 15 ## in seconds

headless_mode = True
## For window sizing in headful mode
default_settings = True ## Instead just run with default viewport

screen_height = 982
screen_width = 1512
# if any of the positions are a negative number, load in fullscreen
exec_settings = [screen_height, screen_width, -1, 0]
exec_height, exec_width, exec_xpos, exec_ypos = exec_settings

mac_chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

with sync_playwright() as p:

    fullscreen = False
    for setting in exec_settings:
        if setting < 0:
            fullscreen = True

    if default_settings:
        print("Launching with default viewport ...")
        browser = p.chromium.launch(
            executable_path=mac_chrome_path, 
            headless=headless_mode,
        )
    elif fullscreen:
        print("Launching in fullscreen ...")
        browser = p.chromium.launch(
            executable_path=mac_chrome_path, 
            headless=headless_mode,
            args=["--start-fullscreen",
                  f"--window-position={0},{0}"]
        )
    else:
        print("Launching ...")
        browser = p.chromium.launch(
            executable_path=mac_chrome_path, 
            headless=headless_mode,
            args=[
                f"--window-size={exec_width},{exec_height}",
                f"--window-position={exec_xpos},{exec_ypos}"
            ]
        )

    if not default_settings:
        context = browser.new_context(
            viewport={"width": screen_width, "height": screen_height}
        )
    else :
        context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(timeout*1000)

    for dom in domain_list:
        ## wait for some time to ensure everything has been cleaned up properly
        time.sleep(random.random()*1.5)

        loaded = False
        while not loaded:
            try:
                page.goto("https://www.virustotal.com/gui/search?query=" + dom)

                eval_locator = page.locator("div > div.card-header.hstack.flex-wrap.justify-content-between.gap-2 "
                                            "> div.hstack.gap-2.fw-bold[class*='text-']")
                rating_locator = page.locator("#positives")
                eval_locator.wait_for(state="visible")
                rating_locator.wait_for(state="visible")

                loaded = True
            except Exception as e:
                user_intervention = input("Task has timed out, investigate and type " \
                                    "anything to continue or q to exit: ")
                if user_intervention == "q":
                    quit()
        
        text = eval_locator.text_content()
        text = text.strip()
        rating = rating_locator.text_content()
        rating = rating.strip()

        if rating != safe_rating and text != safe_text:
            print(f"------------------ Suspicious Domain: {dom}")
            page.screenshot(path= os.path.join("screenshots", dom + ".png"))
            suspicious_list.append(dom)
        elif rating != safe_rating or text != safe_text:
            print(f"-------- Perhaps Suspicious Domain: {dom}")
        else:
            print(f"--- Safe Domain: {dom}")
    
        print(f"Evaluation: {text}")
        print(f"Rating: {rating}/91")

    browser.close()
    
print(f"Suspicious Domains: {len(suspicious_list)}")
print(suspicious_list)

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print()
print(f"Ran script in {end_time - start_time:.6f} seconds")