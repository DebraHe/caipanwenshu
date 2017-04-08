import scrapy,re,random,json
from panjueshu.items import PanjueshuItem
import mysql.connector
class PanjueshuSpider(scrapy.Spider):
    name='caipanwenshu'
    allowed_domains=['wenshu.court.gov.cn']
    start_urls=['http://wenshu.court.gov.cn/Index']
    user_agents=['Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
             'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
             'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
             'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
             'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
             'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
             'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
             'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
             'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
             'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
             'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
             'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
             'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
             'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
             'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
             'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
             'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
             'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
             'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11']
    #def start_requests(self):
        #return [scrapy.FormRequest('http://wenshu.court.gov.cn/List/ListContent',formdata={'Param':'裁判年份:2016','Page':'20','Order':'法院层级','Index':'1','Direction':'asc'},headers={'X-Requested-With': 'XMLHttpRequest','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0','Connection': 'keep-alive','Host': 'wenshu.court.gov.cn'},callback=self.parse_id)]
    def parse(self,response):
        for index in range(1,20):
            yield scrapy.FormRequest('http://wenshu.court.gov.cn/List/ListContent',formdata={'Param':'裁判年份:2016','Page':'20','Order':'法院层级','Index':str(index),'Direction':'asc'},headers={'X-Requested-With': 'XMLHttpRequest','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': random.choice(self.user_agents),'Connection': 'keep-alive','Host': 'wenshu.court.gov.cn'},callback=self.parse_info,meta = {'index':str(index)})

    def parse_info(self,response):
        try:
            list_inf=json.loads(json.loads(response.body.decode('utf-8')))
            list_info = list_inf[1:]
        except:
            index = response.meta['index']
            return scrapy.FormRequest('http://wenshu.court.gov.cn/List/ListContent',formdata={'Param':'裁判年份:2016','Page':'20','Order':'法院层级','Index':index,'Direction':'asc'},headers={'X-Requested-With': 'XMLHttpRequest','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': random.choice(self.user_agents),'Connection': 'keep-alive','Host': 'wenshu.court.gov.cn'},callback=self.parse_info,meta = {'index':index})         
        #print(id_list)
        for info in list_info:
            item = PanjueshuItem()
            try:
                item['yiju'] = info['裁判要旨段原文']
            except:
                item['yiju'] = '无'
            item['type'] = info['案件类型']
            item['date'] = info['裁判日期']
            item['name'] = info['案件名称']
            item['docid'] = info['文书ID']
            item['produce'] = info['审判程序']
            item['num'] = info['案号']
            item['court'] = info['法院名称']
            item['url'] = 'http://wenshu.court.gov.cn/content/content?DocID=%s'%info['文书ID']
            url_content = 'http://wenshu.court.gov.cn/CreateContentJS/CreateContentJS.aspx?DocID=%s'%info['文书ID']
            yield scrapy.Request(url_content,callback=self.parse_content,meta={'item':item})

    def parse_content(self,response):
        item=response.meta['item']
        pattern = re.compile(r'jsonHtmlData = "(.*?)";')
        try:
            content = re.findall(pattern,response.body.decode('utf-8'))[0]
        except:
            url_content = 'http://wenshu.court.gov.cn/CreateContentJS/CreateContentJS.aspx?DocID=%s'%item['docid']
            return scrapy.Request(url_content,callback=self.parse_content,meta={'item':item})   
        item['content'] = content
        conn = mysql.connector.connect(user='root', password='', database='caipan')
        cursor = conn.cursor()
        cursor.execute('insert into panjueshu (name,yiju,docid,produce,type,url,num,court,date,content) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', [item['name'],item['yiju'],item['docid'],item['produce'],item['type'],item['url'],item['num'],item['court'],item['date'],item['content']])
        conn.commit()
        conn.close()
        return item
