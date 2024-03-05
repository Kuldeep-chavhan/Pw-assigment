#!/usr/bin/env python
# coding: utf-8

# In[111]:


import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as ureq
import logging


# In[112]:


flipcart_url = "https://www.flipkart.com/search?q=" + "iphone12pro"


# In[113]:


flipcart_url


# In[114]:


urlclient = ureq(flipcart_url)


# In[115]:


urlclient


# In[116]:


flipcart_page = urlclient.read()


# In[117]:


flipcart_html = bs(flipcart_page,'html.parser')


# In[118]:


flipcart_html.find("div", "class" : <div class="_1AtVbE col-12-12"><div class="_13oc-S"><div data-id="MOBFWBYZXYSCEEEH" style="width: 100%;"><div class="_2kHMtA" data-tkid="818a8221-82e2-49b0-ae20-88fb86ba2c66.MOBFWBYZXYSCEEEH.SEARCH"><a class="_1fQZEK" target="_blank" rel="noopener noreferrer" href="/apple-iphone-12-pro-pacific-blue-128-gb/p/itm97c833296c221?pid=MOBFWBYZXYSCEEEH&amp;lid=LSTMOBFWBYZXYSCEEEHWV51IN&amp;marketplace=FLIPKART&amp;q=iphone12pro&amp;store=tyy%2F4io&amp;srno=s_1_2&amp;otracker=search&amp;otracker1=search&amp;iid=818a8221-82e2-49b0-ae20-88fb86ba2c66.MOBFWBYZXYSCEEEH.SEARCH&amp;ssid=112xl6k1ww0000001707736103009&amp;qH=712933e6bd68e7b9"><div class="MIXNux"><div class="_2QcLo-"><div><div class="CXW8mj" style="height: 200px; width: 200px;"><img loading="eager" class="_396cs4" alt="Apple iPhone 12 Pro (Pacific Blue, 128 GB)" src="https://rukminim2.flixcart.com/image/312/312/kg8avm80/mobile/u/c/d/apple-iphone-12-pro-dummyapplefsn-original-imafwgbrzxg3nggd.jpeg?q=70"></div></div></div><div class="_3wLduG"><div class="_3PzNI-"><span class="f3A4_V"><label class="_2iDkf8"><input type="checkbox" class="_30VH1S" readonly=""><div class="_24_Dny"></div></label></span><label class="_6Up2sF"><span>Add to Compare</span></label></div></div><div class="_2hVSre _3nq8ih"><div class="_36FSn5"><svg xmlns="http://www.w3.org/2000/svg" class="_1l0elc" width="16" height="16" viewBox="0 0 20 16"><path d="M8.695 16.682C4.06 12.382 1 9.536 1 6.065 1 3.219 3.178 1 5.95 1c1.566 0 3.069.746 4.05 1.915C10.981 1.745 12.484 1 14.05 1 16.822 1 19 3.22 19 6.065c0 3.471-3.06 6.316-7.695 10.617L10 17.897l-1.305-1.215z" fill="#2874F0" class="eX72wL" stroke="#FFF" fill-rule="evenodd" opacity=".9"></path></svg></div></div></div><div class="_3pLy-c row"><div class="col col-7-12"><div class="_4rR01T">Apple iPhone 12 Pro (Pacific Blue, 128 GB)</div><div class="gUuXy-"><span id="productRating_LSTMOBFWBYZXYSCEEEHWV51IN_MOBFWBYZXYSCEEEH_" class="_1lRcqv"><div class="_3LWZlK">4.5<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==" class="_1wB99o"></div></span><span class="_2_R_DZ"><span><span>1,334 Ratings&nbsp;</span><span class="_13vcmD">&amp;</span><span>&nbsp;99 Reviews</span></span></span></div><div class="fMghEO"><ul class="_1xgFaf"><li class="rgWa7D">128 GB ROM</li><li class="rgWa7D">15.49 cm (6.1 inch) Super Retina XDR Display</li><li class="rgWa7D">12MP + 12MP + 12MP | 12MP Front Camera</li><li class="rgWa7D">A14 Bionic Chip with Next Generation Neural Engine Processor</li><li class="rgWa7D">Ceramic Shield | Industry-leading IP68 Water Resistance</li><li class="rgWa7D">All Screen OLED Display</li><li class="rgWa7D">LiDAR Scanner for Improved AR Experiences, Night Mode Portraits</li><li class="rgWa7D">Brand Warranty for 1 Year</li></ul></div></div><div cl)


# In[119]:


bigbox = flipcart_html.findAll("div",{ "class":"_1AtVbE col-12-12"})


# In[120]:


len(bigbox)


# In[121]:


del bigbox[0:4]


# In[122]:


"https://www.flipkart.com" +bigbox[5].div.div.div.a["href"]


# In[123]:


product_link = "https://www.flipkart.com" +bigbox[5].div.div.div.a["href"]


# In[124]:


product_link


# In[125]:


product_html = bs(product_req.text,"html.parser")


# In[126]:


comment_box = product_html.find_all("div",{"class" : "_16PBlm"})


# In[ ]:





# In[142]:


comment_box[0].div.find_all('div',{"class" : "row _3n8db9"})[0].text


# 

# In[143]:


for i in comment_box:
    print(i.div.find_all('div',{"class" : "row _3n8db9"})[0].text)


# In[144]:


for i in comment_box:
    print(i.div.div.div.div.text)


# # scraping coustomer feedback on iphone12 pro
# 

# In[147]:


for i in comment_box:
    print(i.div.find_all('div',{"class" : "t-ZTKy"})[0].text)


# In[151]:


for i in comment_box:
    print(i.div.div.div.p.text)


# In[ ]:





# In[128]:


len(comment_box)


# In[129]:


comment_box[0]


# In[130]:


comment_box[0].div.div.find_all('p',{"class":"_2cs7ZR _2V5EHH"})[0]


# In[ ]:


for i in comment_box:
    print(i.div.div.find_all('p',{"class":"_2cs7ZR _2V5EHH"})[0])


# In[ ]:





# In[ ]:





# In[106]:


for i in comment_box:
    print(i.div.div.find_all('p',{"class" : "_2cs7ZR _2V5EHH"})[].text)


# In[ ]:





# In[85]:


requests.get(product_link)


# # scraping all links on i-phone12pro

# In[76]:


for i in bigbox:
    print("https://www.flipkart.com" +i.div.div.div.a["href"])


# In[88]:


requests.get(product_link)


# In[89]:


product_req = requests.get(product_link)


# In[90]:


product_link


# In[ ]:




