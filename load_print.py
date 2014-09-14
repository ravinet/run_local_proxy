import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import os
from time import sleep
#TO RUN: download https://pypi.python.org/packages/source/s/selenium/selenium-2.39.0.tar.gz
#run sudo apt-get install python-setuptools
#after untar, run sudo python setup.py install
#follow directions here: https://pypi.python.org/pypi/PyVirtualDisplay to install pyvirtualdisplay

#For chrome, need chrome driver: https://code.google.com/p/selenium/wiki/ChromeDriver
#chromedriver variable should be path to the chromedriver
#the default location for firefox is /usr/bin/firefox and chrome binary is /usr/bin/google-chrome
#if they are at those locations, don't need to specify

site = sys.argv[1]

display = Display(visible=0, size=(800,600))
display.start()

curr_dir = os.getcwd()
chrome_path = str(curr_dir) + "/chromedriver"
### to run chrome ###
options=Options()
options.add_argument("--incognito")
options.add_argument("--ignore-certificate-errors")
#options.add_argument('--disable-application-cache')
driver=webdriver.Chrome(chrome_path, chrome_options=options)

# to run firefox ###
#driver = webdriver.Firefox()

#profile = webdriver.FirefoxProfile()
#profile.set_preference("webdriver_assume_untrusted_issuer", "false") 
driver.set_page_load_timeout(150)
driver.get(site)
#sleep(10)


#notes: http://www.sitepoint.com/profiling-page-loads-with-the-navigation-timing-api/

#beginning of page load as perceived by user (same as fetchstart if no previous document)
navigationStart = driver.execute_script("return window.performance.timing.navigationStart")

#end of page load
loadEventEnd = driver.execute_script("return window.performance.timing.loadEventEnd")
count = 0
while loadEventEnd == 0 and count < 3:
    loadEventEnd = driver.execute_script("return window.performance.timing.loadEventEnd")
    sleep(2)
    count = count + 1
if ( type(loadEventEnd) == int and type(navigationStart) == int ):
    complete_process = loadEventEnd - navigationStart
    if ( complete_process > 0 ):
        print str(complete_process)
    else:
        print str(-1)
else:
    print str(-1)

sleep(2)
driver.quit()
