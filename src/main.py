"""This file uses the Selenium library to create a web bot that plays the New York Times Spelling Bee Game and attempts to get a Genius or Queen Bee score
A copy of the main website will be used, as the original New York Times game is behind a paywall after inputting three guesses
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from answer_generator import main as create_possible_answers_and_panagrams
import time


#constants
WEBSITE_URL = "https://nytimes-spellingbee.com/"
SHORT_WAIT_TIME = 0.2 #seconds
LONG_WAIT_TIME = 5 #seconds


#ChromeDriverManager().install()
def main() -> None:
    """Opens a window for the Spelling Bee game and plays the game"""
    #intialize driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    #open website
    driver.get(WEBSITE_URL)

    #the game window is in a nested iframe, so switch context to the inner frame
    outer_frame = driver.find_element(By.ID, "iframe_game_play")
    driver.switch_to.frame(outer_frame)
    inner_frame = driver.find_element(By.ID, "iframehtml5")
    driver.switch_to.frame(inner_frame)

    #start the game
    play_button = WebDriverWait(driver, LONG_WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='portal-game-modals']/div/div/div/div/div/div/div[3]/button")))
    play_button.click()

    #scrape letters of puzzle
    letters = driver.find_elements(By.CLASS_NAME, "cell-letter")
    
    #center letter is first in DOM
    #need lowercase letter or create_possible_answers_and_panagrams does not work
    center_letter = letters[0].text.lower()
    
    #satellite letters are other letters
    satellite_letters = []
    for i in range(1, len(letters)):
        satellite_letters.append(letters[i].text.lower())

    #find out possible words
    possible_words = create_possible_answers_and_panagrams(center_letter, satellite_letters)[0]

    #input each word
    actions = ActionChains(driver)
    for word in possible_words:
        #check if the Genius screen is up, and if it is, click it
        try:
            #this slight pause is needed for the game to register all inputs properly
            keep_playing_button = WebDriverWait(driver, SHORT_WAIT_TIME).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#portal-game-modals > div > div > div > div > div > div.sb-modal-buttons-section > button")))
            keep_playing_button.click()
            time.sleep(LONG_WAIT_TIME) #needed to allow time for popup to close

        #WebDriverWait throws an error if the button is not there so ignore the error
        except Exception: 
            pass

        finally:
            actions.send_keys(word)
            actions.send_keys(Keys.RETURN)
            actions.perform()
    
    #scrape correct answers from DOM and print to command line
    answer_guesses = driver.find_elements(By.CLASS_NAME, "sb-anagram")
    answers = [answer.text.lower() for answer in answer_guesses if answer.text.lower()]
    print(f"The correct answers are: {answers}")

    #keep window open until user stops it in command line
    input("Please input something to close the window:")


if __name__ == "__main__":
    main()