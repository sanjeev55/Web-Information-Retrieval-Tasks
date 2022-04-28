#!/usr/bin/env python
# coding: utf-8

# Assignment 6
# 
# Group: kilo

# In[2]:


import pandas as pd


# # Zone Index

# In[3]:


#store filenames in a list
filenames = ['Document1.html',
            'Document2.html',
            'Document3.html',
            'Document4.html',
            'Document5.html']


# ## Read each of the pages from the local repository
# (pages are called page_i, with i (0 - 4) being the index in the order of the list given on the assignment sheet)

# In[4]:


idx = 0
pages = {}
for filename in filenames:
    with open(filename, 'r') as f:
        pages['page_'+str(idx)] = f.read()
        idx+=1

page_0 = pages['page_0']
page_1 = pages['page_1']
page_2 = pages['page_2']
page_3 = pages['page_3']
page_4 = pages['page_4']


# ## Parse the text based on the different zones of the paper
# (images and tables are parsed together with their html tags)

# In[5]:


def zone_parser(pages):
    """takes a list of pages and returns a nested dictionary with the parsed information"""
    tags = ['<br>', '\n', '<p>', '</p>', '</b>', '<i>','</i>', '<r>', '</h2>', '<h3>', '</h3']
    parsed_pages = {}
    idx = 0
    for page in pages.values():
        parsed_page = {}
        #parse the title
        title_start = page.find("<title>")
        title_end = page.find("</title>")
        title = page[title_start+7:title_end]
        for tag in tags:
            title = title.replace(tag, "")
        parsed_page['title'] = title


        #parse the abstract
        abstract_start = page.lower().find("abstract")
        abstract = page[abstract_start+14:]
        abstract_end = abstract.find("\n\n")
        abstract = abstract[:abstract_end]
        for tag in tags:
            abstract = abstract.replace(tag,"")
        abstract = abstract.replace("r>","")
        parsed_page['abstract'] = abstract
        
        #parse the introduction
        intro_start = page.lower().find("<h2>")
        intro = page[intro_start:]
        intro_heading_end = intro.find("</h2>")
        intro = intro[intro_heading_end:]
        intro_end = intro.lower().find("<h2>",10)
        intro = intro[:intro_end]
        for tag in tags:
            intro = intro.replace(tag,"")
        parsed_page['introduction'] = intro
        
        #add it to the parsed_pages dict
        parsed_pages['page_'+str(idx)] = parsed_page
        idx+=1

    return parsed_pages


# In[6]:


#store the parsed info in a nested dictionary parsed_pages
parsed_pages = zone_parser(pages)


# ## Generate a zone index

# In[7]:


from collections import Counter


# In[8]:


token_counts = {}
for key in parsed_pages.keys():
    page_counts = {}
    for k, v in parsed_pages[key].items():
        #replace punctuation
        punct = [".", "?", "!", ":", ";", ",", "(", ")","-"]
        v = v.lower()
        for p in punct:
            v = v.replace(p, " ")
        tokens = v.split(" ")
        cnt = Counter(tokens)
        page_counts[k] = cnt
    token_counts[key] = page_counts


# In[9]:


zone_index = pd.DataFrame.from_dict({(i,j): token_counts[i][j] for i in token_counts.keys() for j in token_counts[i].keys()}, orient='index').fillna(0)

# In[10]:


print(zone_index)


# ## Find the document/documents with term 'eye' in Title and 'performance' in the Abstract and 'methods' in Introduction

# In[11]:


zone_index.index.names = ['page', 'zone']


# In[12]:


title_eye = zone_index.query('(zone == "title" & eye > 0)')['eye']
abstract_performance = zone_index.query('(zone == "abstract" & performance > 0)')['performance']
intro_methods = zone_index.query('(zone == "introduction" & methods > 0)')['methods']


# In[13]:


title_eye.index = title_eye.index.droplevel(level=1)
abstract_performance.index = abstract_performance.index.droplevel(level=1)
intro_methods.index = intro_methods.index.droplevel(level=1)


# In[17]:


matches = title_eye.index.intersection(abstract_performance.index).intersection(intro_methods.index)


# In[24]:


if len(matches) == 0:
    print('There is no page with "eye" in the title, "performance" in the abstract, and "methods" in the introduction\n')
else:
    for page in matches:
        print('The page with the following title has "eye" in the title, "performance" in the abstract, and "methods" in the introduction:\n{}\n'.format(parsed_pages[page]['title']))


# ## Calculate the weighted zone score of each document for the Boolean query 'eye' AND 'tracking'

# In[28]:


score_df = zone_index[['eye', 'tracking']].transpose()



# In[35]:


score_df = score_df.applymap(lambda x: 1 if x > 0 else 0)



# In[51]:


score_df.loc[:,(slice(None), 'abstract')] 


# In[52]:


score_df.loc[:,(slice(None), 'title')] = score_df.loc[:,(slice(None), 'title')] * .45
score_df.loc[:,(slice(None), 'abstract')] = score_df.loc[:,(slice(None), 'abstract')] * .30
score_df.loc[:,(slice(None), 'introduction')] = score_df.loc[:,(slice(None), 'introduction')] * .25


# In[58]:


score_df.transpose()



# In[59]:


score_df = score_df.transpose().groupby("page").sum()
score_df['weighted_zone_score'] = score_df['eye'] + score_df['tracking']


# In[61]:


score_df = score_df.sort_values(by="weighted_zone_score", ascending=False)


# In[64]:


score_df = score_df.drop(['eye', 'tracking'], axis=1)


# In[70]:


score_df_idx = [parsed_pages[page]['title'] for page in score_df.index]
score_df.index = score_df_idx


# In[71]:


print(score_df)

