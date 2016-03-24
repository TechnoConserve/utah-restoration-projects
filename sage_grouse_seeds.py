# Written by @TechnoConserve

import os
import time

import requests
from selenium import webdriver

# Project IDs from Utah's Watershed Restoration Initiative that had greater sage-grouse as a primary beneficiary of the project FY2006-FY2012
PROJECT_IDS = [
	10, 17, 22, 24, 28, 31, 32, 33, 39, 52, 53, 55, 64, 66, 69, 73, 92, 93,
	101, 103, 104, 115, 118, 119, 120, 121, 123, 155, 157, 162, 163, 178, 188, 189,
	205, 210, 212, 228, 229, 242, 249, 250, 258, 259, 270, 276, 291, 296, 297, 298,
	299, 302, 305, 310, 314, 315, 316, 317, 319, 323, 328, 330, 333, 340, 346, 348,
	349, 353, 354, 357, 358, 359, 369, 392, 393, 394, 396, 397, 398, 399, 417, 423,
	442, 445, 452, 458, 461, 465, 467, 479, 504, 513, 514, 562, 563, 566, 589, 594,
	606, 607, 608, 613, 659, 661, 662, 678, 680, 682, 685, 687, 691, 692, 696, 712,
	730, 731, 745, 757, 772, 802, 841, 842, 853, 862, 878, 883, 887, 895, 900, 901,
	918, 927, 941, 967, 973, 978, 979, 980, 986, 987, 992, 993, 995, 996, 1006, 1007,
	1010, 1024, 1025, 1026, 1029, 1033, 1034, 1035, 1043, 1050, 1058, 1061, 1076, 1077,
	1078, 1081, 1082, 1084, 1085, 1089, 1090, 1093, 1102, 1103, 1104, 1105, 1106, 1109,
	1117, 1131, 1133, 1137, 1140, 1149, 1150, 1152, 1153, 1155, 1159, 1161, 1169, 1173,
	1177, 1185, 1199, 1201, 1206, 1215, 1216, 1218, 1223, 1224, 1236, 1260, 1266, 1267,
	1280, 1321, 1323, 1327, 1337, 1340, 1342, 1343, 1347, 1348, 1360, 1361, 1362, 1377,
	1380, 1392, 1396, 1420, 1422, 1426, 1435, 1438, 1439, 1441, 1451, 1461, 1470, 1471,
	1474, 1477, 1487, 1491, 1499, 1503, 1504, 1505, 1533, 1564, 1568, 1582, 1583, 1590,
	1593, 1594, 1607, 1610, 1622, 1638, 1652, 1657, 1658, 1659, 1671, 1675, 1678, 1693,
	1697, 1705, 1711, 1715, 1716, 1722, 1738, 1739, 1741, 1744, 1754, 1772, 1787, 1790,
	1794, 1816, 1828, 1877, 1879, 1882, 1887, 1904, 1927, 1928, 1936, 1937, 1938, 1945,
	1966, 1989, 2020, 2024, 2027, 2041, 2050, 2061, 2091, 2124, 2150, 2163, 2172, 2176,
	2181, 2217, 2237,
]

URL = "https://wri.utah.gov/wri/project/seed.html?id="

def download_file(url):
	local_filename = url.split('/')[-1]
	r = requests.get(url, stream=True)
	os.chdir('files')
	with open(local_filename, 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024): 
			if chunk: # filter out keep-alive new chunks
				f.write(chunk)
	os.chdir('..')
	return local_filename

def get_project_page(driver, project_id):
	driver.get(URL + project_id)
	time.sleep(5)

def main():
	driver = webdriver.Chrome()
	
	for project_id in PROJECT_IDS:
		get_project_page(driver, str(project_id))
		elems = driver.find_elements_by_xpath('//table[@id="seedMixTable"]//tr/td//a')
		for link in elems:
			print("Successfully downloaded {}.".format(download_file(link.get_attribute("href"))))
	
	driver.close()
		

if __name__ == '__main__':
	main()