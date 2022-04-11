from WWTest.base.activeBrowser import ActiveBrowser
from WWTest.autotest.config.bilibili.page.loginPage import lpf

class IndexPage(object):
    index_search_input_selector = "#nav-searchform > div.nav-search-content > input"
    index_search_icon_selector = "#nav-searchform > div.nav-search-btn > svg"

    more_filter_button_selector = "#i_cecream > div:nth-child(1) > div:nth-child(1) > div.search-header > div:nth-child(4) > div > div.conditions-order.flex_between > button"
    qunbushichang_selector = "#i_cecream > div:nth-child(1) > div:nth-child(1) > div.search-header > div:nth-child(4) > div > div.more-conditions > div:nth-child(1) > button:nth-child(1)"
    more_than_sixty_minutes_button_selector = "#i_cecream > div:nth-child(1) > div:nth-child(1) > div.search-header > div:nth-child(4) > div > div.more-conditions > div:nth-child(1) > button:nth-child(5)"


    second_search_button_selector = "#i_cecream > div:nth-child(1) > div:nth-child(1) > div.search-header > div.search-input > div > div > div > svg.search-icon > use"

    #搜索结果页中正文的div层
    search_result_div_selector = "#i_cecream > div:nth-child(1) > div:nth-child(1) > div.search-content > div > div"

    #下一页按钮可点击时的selecor
    next_page_able_selector = "#i_cecream > div:nth-child(1) > div:nth-child(1) > div.search-content > div > div > div.flex_center.mt_x50.mb_lg > div > div > button:nth-child(5)"
    # 下一页按钮不能点击时的selecor
    next_page_unable_selector = "#i_cecream > div:nth-child(1) > div:nth-child(1) > div.search-content > div > div > div.flex_center.mt_x50.mb_lg > div > div > button.vui_button.vui_button--disabled.vui_pagenation--btn.vui_pagenation--btn-side"


indexpage =IndexPage()

class IndexPageFunction(object):

    def __init__(self):
        self.all_page_video_info_list = []


    def isExist(self,activebrowser,x_selector,check_text):
        try:
            ele = activebrowser.driver.find_element_by_css_selector(x_selector)
            acture_text = ele.text
            print("acture_text:")
            print(acture_text)
            if acture_text == check_text:
                return '1'   #1-表示存在
            else:
                return '2'  #2-表示不存在
        except:
            return '2'   #2-表示不存在

    # def isExistLoginButton(self,activebrowser):
    #     return self.isExist(activebrowser,indexpage.login_button_xpath)

    #主要输入要搜索的内容，然后跳转到搜索结果页
    def indexSearch(self,activebroser,search_text):
        # activebroser = ActiveBrowser()
        activebroser = activebroser
        activebroser.findEleAndInputNum(num=0,
                                        findstyle="css_selector",
                                        findstylevalue=indexpage.index_search_input_selector,
                                        inputcontent=search_text)
        #点击搜索图标
        activebroser.findEleAndClickNoDelayTime(num=0,
                                                findstyle ="css_selector" ,
                                                findstylevalue=indexpage.index_search_icon_selector)

        activebroser.onlyCloseBrowse()  #关闭当前浏览器界面

        #切换到新窗口
        activebroser.switchNewWindows()

    #点击更多筛选，筛选60分钟以上的内容
    def filterSixtyMinutes(self,activebroser):
        #模拟鼠标悬停在某个元素
        activebroser.mockHoverEle(num=0,
                                  findstyle = "css_selector",
                                  findstylevalue = indexpage.second_search_button_selector)

        activebroser.delayTime(2)
        #点击更多筛选
        activebroser.findEleAndClickNoDelayTime(num=0,
                                                findstyle ="css_selector" ,
                                                findstylevalue=indexpage.more_filter_button_selector)

        #向上滑动到页面顶端
        activebroser.slideToTopByJS()
        activebroser.delayTime(2)

        #点击60分钟以上按钮
        activebroser.findEleAndClickNoDelayTimeNoNum(
                                                findstyle ="css_selector" ,
                                                findstylevalue=indexpage.more_than_sixty_minutes_button_selector)
        activebroser.delayTime(5)


    #获取一页中视频名字和链接地址
    def getOnePageVideoInfo(self,activebroser):
        one_page_all_video_info_list = []

        #获取一页中有多少个视频
        findstylevalue = "#i_cecream > div:nth-child(1) > div:nth-child(1) > div.search-content > div > div > div.video-list.row"
        son_div_ele_list = activebroser.getFatherSonElesList(fatherfindstyle="css_selector",
                                                             fatherfindstylevalue=findstylevalue,
                                                             sonfindstyle="class_name",
                                                             sonfindstylevalue="video-list-item")  # 子元素路径相对父元素
        son_div_ele_list_len = len(son_div_ele_list)
        print("son_div_ele_list_len:")
        print(son_div_ele_list_len)
        print(son_div_ele_list)

        if son_div_ele_list_len >36:
            for_num = 37
        else:
            for_num = son_div_ele_list_len+1
        for i in range(1,for_num):
            try:
                one_video_info_list = []
                print("处理第%s个元素" % str(i))
                #处理一个页面上的36个视频文件
                findstylevalue = "#i_cecream > div:nth-child(1) > div:nth-child(1) > div.search-content > div > div > div.video-list.row > div:nth-child(%s)" % str(i)
                print("findstylevalue:")
                print(findstylevalue)
                one_ele_father = activebroser.findELe(findstyle="css_selector",
                                                      findstylevalue=findstylevalue)
                #获取视频网址
                son_url_ele_list = activebroser.getFatherSonElesList(fatherfindstyle="css_selector",
                                                                fatherfindstylevalue = findstylevalue,
                                                                sonfindstyle="xpath",
                                                                sonfindstylevalue="div/div[2]/a")  #子元素路径相对父元素
                son_url_ele_list_len = len(son_url_ele_list)
                for j in range(0,son_url_ele_list_len):
                    try:
                        print("获取第%s个元素" % str(j+1))
                        son_url_ele = son_url_ele_list[j]
                        print("son_url_ele:")
                        print(son_url_ele)
                        video_url = son_url_ele.get_attribute('href')
                        print("video_url:")
                        print(video_url)
                        one_video_info_list.append(video_url)
                    except Exception as e:
                        one_video_info_list.append("")
                        print("获取元素失败，继续下个：%s" % str(e))
                        continue


                #获取视频名称
                son_name_ele_list = activebroser.getFatherSonElesList(fatherfindstyle="css_selector",
                                                                fatherfindstylevalue = findstylevalue,
                                                                sonfindstyle="xpath",
                                                                sonfindstylevalue="div/div[2]/a/div/div[1]/picture/img")  #子元素路径相对父元素
                son_name_ele_list_len = len(son_name_ele_list)
                for j in range(0,son_name_ele_list_len):
                    try:
                        print("获取第%s个元素" % str(j+1))
                        son_name_ele = son_name_ele_list[j]
                        print("son_name_ele:")
                        print(son_name_ele)
                        video_name = son_name_ele.get_attribute('alt')
                        print("video_name:")
                        print(video_name)
                        one_video_info_list.append(video_name)
                    except Exception as e:
                        one_video_info_list.append("")
                        print("获取元素失败，继续下个：%s" % str(e))
                        continue

                print("one_video_info_list:")
                print(one_video_info_list)
                one_page_all_video_info_list.append(one_video_info_list)
            except Exception as e:
                print("处理失败，继续下个：%s" % str(e))
                continue
        print("one_page_all_video_info_list:")
        print(one_page_all_video_info_list)
        return one_page_all_video_info_list

    #获取下一页的按钮，查看是否可点击
    def getNextIsClick(self,activebroser):
        #滑动到底部
        activebroser.slideToBottomByJS()
        #是否存在下一页置灰的按钮
        is_exist_gray_next_page =self.isExist(activebrowser=activebroser,
                                              x_selector=indexpage.next_page_unable_selector,
                                              check_text="下一页")
        print("is_exist_gray_next_page:")
        print(is_exist_gray_next_page)
        if is_exist_gray_next_page == '1':
            print("已经是最后一页")
            return is_exist_gray_next_page
        else:
            print("下一页可以点击")

        #滑动到页面的顶部
        activebroser.slideToTopByJS()
        return is_exist_gray_next_page

    #点击下一页
    def clickNextPage(self,activebroser):
        #滑动到底部
        activebroser.slideToBottomByJS()

        #获取下一页所在行的所有父元素的button元素
        findstylevalue = "#i_cecream > div:nth-child(1) > div:nth-child(1) > div.search-content > div > div > div.flex_center.mt_x50.mb_lg > div > div"
        son_button_ele_list = activebroser.getFatherSonElesList(fatherfindstyle="css_selector",
                                                             fatherfindstylevalue=findstylevalue,
                                                             sonfindstyle="xpath",
                                                             sonfindstylevalue="button")  # 子元素路径相对父元素
        son_button_ele_list_len = len(son_button_ele_list)
        print("son_button_ele_list:")
        print(son_button_ele_list_len)
        print(son_button_ele_list)

        #点击下一页
        next_page_able_selector = findstylevalue + "> button:nth-child(%s)" % son_button_ele_list_len
        activebroser.findEleAndClickNoDelayTimeNoNum(
                                                findstyle ="css_selector" ,
                                                findstylevalue=next_page_able_selector)
        activebroser.delayTime(5)





    #获取所有页面的数据
    def getAllData(self,activebroser):

        while(True):
            # 获取一页数据
            one_page_all_video_info_list = self.getOnePageVideoInfo(activebroser=activebroser)
            for one_list in one_page_all_video_info_list:
                self.all_page_video_info_list.append(one_list)
            #查看下一页是否可以点击
            is_exist_gray_next_page = self.getNextIsClick(activebroser=activebroser)
            if is_exist_gray_next_page == '1':
                break   #终止循环
            else:
                #点击下一页
                self.clickNextPage(activebroser=activebroser)
                continue  #继续循环

        print("self.all_page_video_info_list:")
        print(self.all_page_video_info_list)
        return self.all_page_video_info_list








indexpagefunction = IndexPageFunction()

if __name__ == '__main__':
    print("hello world")
    ac = ActiveBrowser()
    lpf.login(activebroser=ac)
    indexpagefunction.indexSearch(activebroser=ac,
                                  search_text="常见漏洞")
    indexpagefunction.filterSixtyMinutes(activebroser=ac)
    # indexpagefunction.getNextIsClick(activebroser=ac)
    # indexpagefunction.clickNextPage(activebroser=ac)
    # indexpagefunction.getNextIsClick(activebroser=ac)
    all_data_list = indexpagefunction.getAllData(activebroser=ac)
    print("all_data_list:")
    print(len(all_data_list))
    print(all_data_list)
    ac.closeBrowse()

