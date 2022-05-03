from PIL import Image 
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
class toolset():
    def fetch_link(keyword):
        link_list = {}
        with open('link_list.txt') as li:
            link = li.readline()

            while link:
                link_list[link.split(' ')[0]] = link.split(' ')[1]
                link = li.readline()
        li.close()
        return link_list[keyword.upper()]

    def cropimage(url):
        marketpad = 0
        img = Image.open(r"C:\\Location\\of\\screenshot.png") 
        if "opensea" not in url:
            padding = -680
            marketpad = -750
        else:
            try:
                link_len =  len(url.split("/")[4].split("?")[0])
                if  link_len > 0 and link_len <10:
                    padding = 0
                elif link_len >= 10 and link_len < 21:
                    padding = 40
                elif link_len >= 21:
                    padding = 100
            except Exception:
                print("failed to parse the url in the cropimage() function")
        left = 0
        top = 1140+padding
        right = 460
        bottom = 1930+marketpad
        img_res = img.crop((left, top, right, bottom)) 

        img_res.save(r"C:\\Location\\of\\screenshot.png")

    def fetch_screenshot(keyword):
        URL = toolset.fetch_link(keyword)

        options = Options()
        options.page_load_strategy = 'normal'
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options, executable_path="C:\\Location\\of\\geckodriver.exe")
        driver.set_window_size(460, 2400)
        driver.get(URL)
        time.sleep(5)

        S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
        driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment

        driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')

        driver.quit()

        toolset.cropimage(URL)

    def del_link(keyword):
        #delete link from links list
        link_str = ""
        with open('link_list.txt') as li:
            link = li.readline()

            while link:
                link_str = link_str + link
                link = li.readline()
        li.close()

        link_list = link_str.split("\n")
        counter = 0
        for x in link_list:
            if x.split(" ")[0]==keyword.upper():
                break
            counter += 1
        link_list.pop(counter)
        link_list.pop(len(link_list)-1)
        file1 = open('link_list.txt', 'w')
        s = ""
        for x in link_list:
            s = s + x +("\n")
        # Writing multiple strings
        # at a time
        file1.write(s)

        # Closing file
        file1.close()
    def add_link(activity_link, keyword):
        #check if link had activity page in URL
        if "?tab=activity" not in activity_link:
            activity_link = activity_link+"?tab=activity"
        link_str = ""
        with open('link_list.txt') as li:
            link = li.readline()

            while link:
                link_str = link_str + link
                link = li.readline()
        li.close()

        file1 = open('link_list.txt', 'w')
        s = link_str+keyword.upper()+" "+activity_link+"\n"

        # Writing multiple strings
        # at a time
        file1.write(s)

        # Closing file
        file1.close()

        
    def list_links():
        link_str = ""
        try:
            with open('link_list.txt') as li:
                link = li.readline()

                while link:
                    link_str = link_str + "{:14}".format(link.split(" ")[0]) +link.split("/")[4].split("?")[0] + "\n"
                    link = li.readline()
            li.close()
        except Exception as e:
            print(e)
        return "```"+link_str+"```"
    
    