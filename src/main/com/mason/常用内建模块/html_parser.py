#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# html
import re
from abc import ABC
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser, ABC):

    def __init__(self):
        super(MyHTMLParser, self).__init__()
        self.__parsedata = ""

    def handle_starttag(self, tag, attrs):
        if ("class", "event-title") in attrs:
            self.__parsedata = "name"  # 通过属性判断如果该标签是我们要找的标签，设置标志位
        if tag == "time":
            self.__parsedata = "time"
        if ("class", "say-no-more") in attrs:
            self.__parsedata = "year"
        if ("class", "event-location") in attrs:
            self.__parsedata = "location"

    def handle_endtag(self, tag):
        return

    def handle_startendtag(self, tag, attrs):
        return

    def handle_data(self, data: str):
        if data and len(data.strip()) > 0:
            if self.__parsedata == 'name':
                print('会议名称:%s' % data)  # 通过标志位判断，输出打印标签内容

            if self.__parsedata == 'time':
                print('会议时间:%s' % data)

            if self.__parsedata == 'year':
                if re.match(r'\s\d{4}', data):  # 因为后面还有两组 say-no-more 后面的data却不是年份信息,所以用正则检测一下
                    print('会议年份:%s' % data.strip())

            if self.__parsedata == 'location':
                print('会议地点:%s' % data)
                print('----------------------------------')

    def handle_comment(self, data):
        return

    def handle_entityref(self, name):
        return

    def handle_charref(self, name):
        return


parser = MyHTMLParser()
parser.feed("""        <div class="most-recent-events">
            <div class="shrubbery">
                <h2 class="widget-title"><span aria-hidden="true" class="icon-calendar"></span>Upcoming Events</h2>
                
                <p class="give-me-more"><a href="?page=2" title="More Events">More</a></p>
                
                <ul class="list-recent-events menu">
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/865/">PyCon Sweden 2019</a></h3>
                        <p>
                            
                            
<time datetime="2019-10-31T00:00:00+00:00">31 Oct. &ndash; 01 Nov. <span class="say-no-more"> 2019</span></time>

                            

                            
                            <span class="event-location">Stockholm, Sweden</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/853/">PyCon Fr</a></h3>
                        <p>
                            
                            
<time datetime="2019-10-31T00:00:00+00:00">31 Oct. &ndash; 03 Nov. <span class="say-no-more"> 2019</span></time>

                            

                            
                            <span class="event-location">Bordeaux, France</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/852/">PiterPy 2019</a></h3>
                        <p>
                            
                            
<time datetime="2019-11-01T00:00:00+00:00">01 Nov.<span class="say-no-more"> 2019</span></time>

                            

                            
                            <span class="event-location">Saint Petersburg, St Petersburg, Russia</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/861/">PyCascades 2020</a></h3>
                        <p>
                            
                            
<time datetime="2020-02-08T00:00:00+00:00">08 Feb. &ndash; 09 Feb. <span class="say-no-more"> 2020</span></time>

                            

                            
                            <span class="event-location">Portland, Oregon, USA</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/825/">SciPy 2020</a></h3>
                        <p>
                            
                            
<time datetime="2020-07-06T00:00:00+00:00">06 July &ndash; 12 July <span class="say-no-more"> 2020</span></time>

                            

                            
                            <span class="event-location">Austin, TX, US</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/875/">EuroPython 2020</a></h3>
                        <p>
                            
                            
<time datetime="2020-07-20T00:00:00+00:00">20 July &ndash; 26 July <span class="say-no-more"> 2020</span></time>

                            

                            
                            <span class="event-location">TBA</span>
                            
                        </p>
                    </li>
                
                </ul>
            </div>

            
            <h3 class="widget-title just-missed">You just missed...</h3>
            <ul class="list-recent-events menu">
                
                <li>
                    <h3 class="event-title"><a href="/events/python-events/866/">Python Brasil 2019</a></h3>
                    <p>
                        
                        
<time datetime="2019-10-23T00:00:00+00:00">23 Oct. &ndash; 28 Oct. <span class="say-no-more"> 2019</span></time>

                        

                        
                        <span class="event-location">Ribeirão Preto, São Paulo, Brazil</span>
                        
                    </p>
                </li>
                
                <li>
                    <h3 class="event-title"><a href="/events/python-events/871/">PyCon China 2019 Beijing Branch</a></h3>
                    <p>
                        
                        
<time datetime="2019-10-19T00:00:00+00:00">19 Oct.<span class="say-no-more"> 2019</span></time>

                        

                        
                        <span class="event-location">Beijing, People&#39;s Republic of China</span>
                        
                    </p>
                </li>
                
            </ul>
            
        </div>""")
