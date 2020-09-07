from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.facebook.com/tran.thanh.ne/'
path = "chromedriver.exe"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install())
index = 0

def post_with_link():
    driver.find_element_by_css_selector('a#expanding_cta_close_button').click()
    title = driver.find_elements_by_css_selector('div p')[0].text
    show_comment = driver.find_element_by_css_selector('div[role="feed"] a[class="_3hg- _42ft"]')
    driver.execute_script("arguments[0].click();", show_comment)
    time.sleep(1)
    show_more = driver.find_element_by_css_selector('div[role="feed"] span[class=" _4ssp"]')
    driver.execute_script("arguments[0].click();", show_more)
    time.sleep(3)
    comment_element_having_name = driver.find_elements_by_xpath('//div[@class="_72vr"]')
    comment_element = driver.find_elements_by_xpath('//span[@class="_3l3x"]')
    print("Title: " + title)
    for i in range(6):
        name = comment_element_having_name[i].text.split(" " + comment_element[i].text)[0]
        comment = comment_element[i].text
        print(name + ": " + comment)


#
#
def post_img():
    driver.get(url)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    driver.find_element_by_css_selector('a#expanding_cta_close_button').click()
    all_spans = driver.find_elements_by_xpath("//span[@class='timestampContent']")
    try:
        all_spans[index].click()
    except:
        driver.execute_script("arguments[0].click();", all_spans[index])
    time.sleep(4)
    title = driver.find_element_by_css_selector(".hasCaption").text
    comment_element_having_name = driver.find_elements_by_xpath("//div[@class='UFICommentActorAndBodySpacing']")
    comment_element = driver.find_elements_by_xpath("//span[@class='UFICommentBody']")
    print("Title: " + title)
    for i in range(6):
        name = comment_element_having_name[i].text.split(" " + comment_element[i].text)[0]
        comment = comment_element[i].text
        print(name + ": " + comment)


def get_comment():
    driver.get(url)
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    driver.find_element_by_css_selector('a#expanding_cta_close_button').click()
    time.sleep(2)
    all_spans = driver.find_elements_by_xpath("//span[@class='timestampContent']")

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
            post_img()
        driver.get(url)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
        driver.find_element_by_css_selector('a#expanding_cta_close_button').click()
        time.sleep(3)
        all_spans = driver.find_elements_by_xpath("//span[@class='timestampContent']")


get_comment()
