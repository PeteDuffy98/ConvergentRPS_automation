import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pyairtable import Api, Base

# Your Airtable credentials
AIRTABLE_BASE_ID = 'appjTbn52Fbj6HCRv'
AIRTABLE_TABLE_NAME = 'tblZgXNX8mTYERs9K'
AIRTABLE_PERSONAL_ACCESS_TOKEN = 'patBGMC0XcevEXj7M.0d89df592bde3199c4b110875633eadffc37af7d78a9ec0b5b21dd63d22fca1d'

def fetch_questions_from_airtable():
    api = Api(AIRTABLE_PERSONAL_ACCESS_TOKEN)
    base = Base(api, AIRTABLE_BASE_ID)
    table = base.table(AIRTABLE_TABLE_NAME)

    try:
        records = table.all()
        questions = [record['fields'].get('question', '') for record in records if record['fields'].get('question')]
        return questions
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def run_script():
    questions = fetch_questions_from_airtable()
    if not questions:
        print("No questions available. Exiting script.")
        return

    driver = webdriver.Chrome()
    driver.get("https://indemn-discovery.framer.website/convergent")
    time.sleep(5)

    for _ in range(10):  # Changed '*' to '_'
        try:
            text_area = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]/form/textarea")
            time.sleep(2)

            random_question = random.choice(questions)

            text_area.send_keys(random_question)
            text_area.send_keys(Keys.RETURN)
            time.sleep(6)
        except Exception as e:
            print(f"An error occurred during script execution: {e}")

    driver.quit()

def run_multiple_times(n):
    for _ in range(n):  # Changed '*' to '_'
        run_script()  # Fixed typo: changed 'run*script()' to 'run_script()'
        time.sleep(10)

run_multiple_times(50)