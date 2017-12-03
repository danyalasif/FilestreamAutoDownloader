from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import bencodepy
import hashlib
import base64

def make_magnet_from_file(file):
    metadata = bencodepy.decode_from_file(file)
    subj = metadata[b'info']
    hashcontents = bencodepy.encode(subj)
    digest = hashlib.sha1(hashcontents).digest()
    b32hash = base64.b32encode(digest).decode()
    return 'magnet:?' + 'xt=urn:btih:' + b32hash


email = ""
password = ""

browser = webdriver.Chrome()
browser.get("https://filestream.me/members/user/login")

email_elem = browser.find_element_by_name("username")
email_elem.send_keys(email)
pass_elem = browser.find_element_by_name("password")
pass_elem.send_keys(password)
browser.implicitly_wait(10)
browser.find_element_by_class_name("submitBtn").click()

torrent_file = "Movie.torrent" #Make it so it monitors a folder and takes torrents automatically
mag_link = make_magnet_from_file(torrent_file)

upload_elem = browser.find_element_by_id("uploadLink")
upload_elem.send_keys(mag_link)
browser.implicitly_wait(10)
browser.find_element_by_css_selector("a#header-upload-link").click()

#mag = make_magnet_from_file("E:\\Ninja Girl.torrent")
#print(mag)


'''
torrentLink = input("Enter the torrent link")
elem.clear()
elem.send_keys(torrentLink)
elem.send_keys(Keys.RETURN)
'''
