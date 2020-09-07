from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
# CHROME_PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
# CHROMEDRIVER_PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
WINDOW_SIZE = "1920,1080"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument("--log-level=3")
# chrome_options.binary_location = CHROME_PATH


url = 'https://www.facebook.com/tran.thanh.ne/'
path = "chromedriver.exe"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)


def post_with_link():
    driver.find_element_by_css_selector('a#expanding_cta_close_button').click()
    title = driver.find_elements_by_css_selector('div p')[0].text
    like = \
        driver.find_elements_by_xpath(
            '//form[@class="commentable_item collapsed_comments"]//span[@class="_3dlh"]//span')[
            0].text
    show_comment = driver.find_element_by_css_selector('div[role="feed"] a[class="_3hg- _42ft"]')
    share_num = driver.find_element_by_css_selector('div[role="feed"] span[class="_355t _4vn2"]').text
    comment_num = show_comment.text
    driver.execute_script("arguments[0].click();", show_comment)
    time.sleep(1)
    show_more = driver.find_element_by_css_selector('div[role="feed"] span[class=" _4ssp"]')
    driver.execute_script("arguments[0].click();", show_more)
    time.sleep(3)
    comment_element_having_name = driver.find_elements_by_xpath('//div[@class="_72vr"]')
    comment_element = driver.find_elements_by_xpath('//span[@class="_3l3x"]')
    print("Title: " + title)
    print("Number of React: " + like)
    print("Number of Comment: " + comment_num)
    print("Number of Share: " + share_num)
    for i in range(6):
        name = comment_element_having_name[i].text.split(" " + comment_element[i].text)[0]
        comment = comment_element[i].text
        print(name + ": " + comment)
        if i == 5:
            print("-----------------------------------------------------------------------------------")
        else:
            print("----------------------------")


def post_img(index):
    driver.get(url)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(4)
    driver.find_element_by_css_selector('a#expanding_cta_close_button').click()
    all_spans = driver.find_elements_by_xpath("//div[@data-testid='story-subtitle']//span[@class='timestampContent']")
    try:
        all_spans[index].click()
    except:
        driver.execute_script("arguments[0].click();", all_spans[index])
    time.sleep(4)
    title = driver.find_element_by_css_selector(".hasCaption").text

    try:
        like_num = driver.find_element_by_css_selector('div[class="UFILikeSentenceText"] span').text
    except:
        like_num = driver.find_element_by_css_selector('div[class="UFILikeSentenceText"] span')[0].text
    try:
        comment_num = driver.find_elements_by_xpath('//div[@class="UFIRow UFIShareRow"]//span').text
    except:
        comment_num = driver.find_elements_by_xpath('//div[@class="UFIRow UFIShareRow"]//span')[0].text
    try:
        share_num = driver.find_elements_by_xpath('//div[@class="UFIRow UFIShareRow"]//a').text
    except:
        share_num = driver.find_elements_by_xpath('//div[@class="UFIRow UFIShareRow"]//a')[0].text

    comment_element_having_name = driver.find_elements_by_xpath("//div[@class='UFICommentActorAndBodySpacing']")
    comment_element = driver.find_elements_by_xpath("//span[@class='UFICommentBody']")

    print("Title: " + title)
    print("Number of React: " + like_num)
    print("Number of Comment: " + comment_num)
    print("Number of Share: " + share_num)
    print("Title: " + title)
    for i in range(6):
        name = comment_element_having_name[i].text.split(" " + comment_element[i].text)[0]
        comment = comment_element[i].text
        print(name + ": " + comment)
        if i == 5:
            print("-----------------------------------------------------------------------------------")
            print("-----------------------------------------------------------------------------------")
        else:
            print("----------------------------")


def get_comment():
    driver.get(url)
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    driver.find_element_by_css_selector('a#expanding_cta_close_button').click()
    time.sleep(2)
    all_spans = driver.find_elements_by_xpath("//div[@data-testid='story-subtitle']//span[@class='timestampContent']")

    for index in range(5):

        print("Post " + str(index + 1))

        try:
            all_spans[index].click()
        except:
            driver.execute_script("arguments[0].click();", all_spans[index])
        time.sleep(4)
        try:
            post_with_link()
        except:
            post_img(index)
        driver.get(url)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
        driver.find_element_by_css_selector('a#expanding_cta_close_button').click()
        time.sleep(3)
        all_spans = driver.find_elements_by_xpath("//div[@data-testid='story-subtitle']//span[@class='timestampContent']")


get_comment()
