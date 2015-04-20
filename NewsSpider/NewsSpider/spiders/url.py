"""
store the url for spider in eastmoney.com
"""

'finance.eastmoney.com/news/(finance).html'
finance = ['ccjdd','cssgs','cywjh','cgnjj','chgjj','cgjjj','cjrzb','czqyw','ccyjj','ccjxw','cgsxw']

'stock.eastmoney.com/news/(stock).html'
stock = ['cgszb','cdpfx','cbkjj','cchjy','csccl','chyyj','cggdj','ccybgsxw']
url2=[]
url1=[]
for i in finance:
    x = 'http://finance.eastmoney.com/news/'+i+'.html'
    url2.append(x)
for i in stock:
    x = 'http://stock.eastmoney.com/news/'+i+'.html'
    url1.append(x)
