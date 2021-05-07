from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# global webdriver
selenium = webdriver.Chrome(executable_path="./chromedriver")

def main():
    #Choose your url to visit
    selenium.get('http://127.0.0.1:8000/admin')

    #
    # User must enter create a student group, user, and
    # login with that user. Afterwards wait on the mssage board
    # page until re-directed to the chatroom url
    #

    sleep(30) 

    # go to chatroom
    selenium.get('http://127.0.0.1:8000/chatroom')

    #
    # User must wait until prompt is entered. Enter the
    # name 'ben' for now.
    #

    sleep(5) 

    # tests
    test_send_message()

    # close/quit
    sleep(3)
    selenium.close()
    selenium.quit()

# TEST GO HERE
def test_send_message():
    #cache DOM elements
    modal_user_button =  selenium.find_element_by_id('modal-button')
    modal_classmate_area =  selenium.find_element_by_id('modal-classmate-area')
    user_area =  selenium.find_element_by_id('user-area')
    text_submit = selenium.find_element_by_id('text-submit')

    # open a user
    modal_user_button.click()
    sleep(1)
    listOfButtons = modal_classmate_area.find_elements_by_tag_name('button')
    listOfButtons[0].click()
    sleep(1)
    userListOfButtons = user_area.find_elements_by_tag_name('button')
    userListOfButtons[0].click()

    #send a message
    sleep(1)
    text_submit.send_keys('Hello, how are you?')
    sleep(1)
    text_submit.send_keys(Keys.ENTER)

    

if __name__ == "__main__":
    main()