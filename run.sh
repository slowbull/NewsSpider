
#!/bin/bash
# this script is used to run the spider to crawl news and run Dataprocess file to get final ranking.
# author: jonny
# data 2015/1/12

cd ./NewsSpider
python news.py

cd ~/workspace/scrapyTest
export PATH=$PATH:./DataProcess
python ./DataProcess/ProcessNews.py




#:
