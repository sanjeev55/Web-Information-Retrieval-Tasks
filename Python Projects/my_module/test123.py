fileNames = ['Document1.html','Document2.html','Document3.html','Document4.html','Document5.html']

count = 0
documents = {}
for filename in fileNames:
    with open(filename, 'r') as f:
        documents['d'+str(count)] = f.read()
        count = count + 1

print(documents)
def zone_parser(pages):

    tags = ['<br>', '\n', '<p>', '</p>', '</b>', '<i>','</i>', '<r>', '</h2>', '<h3>', '</h3>']
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


    #parse the abstract\n",
        abstract_start = page.lower().find("abstract")
        abstract = page[abstract_start+14:]
        abstract_end = abstract.find("")
        abstract = abstract[:abstract_end]
        for tag in tags:
            abstract = abstract.replace(tag,"")
        abstract = abstract.replace("r>","")
        parsed_page['abstract'] = abstract
    #parse the introduction\n",
        intro_start = page.lower().find("<h2>")
        intro = page[intro_start:]
        intro_heading_end = intro.find("</h2>")
        intro = intro[intro_heading_end:]
        intro_end = intro.lower().find("<h2>",10)
        intro = intro[:intro_end]
        for tag in tags:
            intro = intro.replace(tag,"")
        parsed_page['introduction'] = intro

    #add it to the parsed_pages dict\n",
        parsed_pages['page_'+str(idx)] = parsed_page
        idx+=1

    return parsed_pages

parsed_pages = zone_parser(pages)


token_counts = {}
for key in parsed_pages.keys():
    page_counts = {}
    for k, v in parsed_pages[key].items():
        #replace punctuation\n",
        punct = [".", "?", "!", ":", ";", ",", "(", ")","-"]
        v = v.lower()
        for p in punct:
            v = v.replace(p, " ")
        tokens = v.split(" ")
        cnt = Counter(tokens)
        page_counts[k] = cnt
    token_counts[key] = page_counts

zone_index = pd.DataFrame.from_dict({(i,j): token_counts[i][j] for i in token_counts.keys() for j in token_counts[i].keys()}, orient='index').fillna(0)

print(zone_index.head(10))


zone_index.index.names = ['page', 'zone']


title_eye = zone_index.query('(zone == "title" & eye > 0)')['eye']
abstract_performance = zone_index.query('(zone == "abstract" & performance > 0)')['performance']
intro_methods = zone_index.query('(zone == "introduction" & methods > 0)')['methods']