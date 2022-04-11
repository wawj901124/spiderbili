from WWTest.base.activeBrowser import ActiveBrowser
from WWTest.autotest.config.bilibili.page.loginPage import lpf
from WWTest.autotest.config.bilibili.page.indexSearch import indexpage,indexpagefunction

class DetailVideoPage(object):
    fanju_selector = "#internationalHeader > div > div > div.nav-link > ul > li:nth-child(2) > a"
    video_total_num_selector = "#multi_page > div.head-con > div.head-left > span"
    video_list_ul_selector = "#multi_page > div.cur-list > ul"




detailvideopage =DetailVideoPage()

class DetailVideoPageFunction(object):

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


    #获取视频中有多少课程
    def getCurriculumNum(self,activebroser):
        video_num_yuan = activebroser.findEleAndReturnText(num=0,
                                          findstyle="css_selector",
                                          findstylevalue=detailvideopage.video_total_num_selector)
        print("video_num_yuan:")
        print(video_num_yuan)
        video_num_yuan_list = video_num_yuan.split("/")
        print(video_num_yuan_list)
        video_num_yuan_list_one = video_num_yuan_list[1]
        print(video_num_yuan_list_one)
        video_num = video_num_yuan_list_one.strip(")")
        print("video_num:")
        print(video_num)
        #滑动到页面的顶部
        activebroser.slideToTopByJS()
        return video_num


    #获取视频中课程列表
    def getVideoCurriculumListInfo(self,activebroser,video_url):
        video_curriculum_info_list = []
        activebroser.getUrl(video_url)

        activebroser.delayTime(5)


        activebroser.delayTime(2)
        video_num = self.getCurriculumNum(activebroser=activebroser)
        print(video_num)


        #获取视频有多少个课程
        first_curriculum_info_list=[]
        #获取第一个视频
        first_curriculum_selector = detailvideopage.video_list_ul_selector+" > li.watched.on > a"
        first_curriculum_ele = activebroser.findELe(findstyle = "css_selector",
                                                    findstylevalue=first_curriculum_selector)
        curriculum_url = first_curriculum_ele.get_attribute('href')
        print("curriculum_url:")
        print(curriculum_url)
        first_curriculum_info_list.append(curriculum_url)

        curriculum_name = first_curriculum_ele.get_attribute('title')
        print("curriculum_name:")
        print(curriculum_name)
        first_curriculum_info_list.append(curriculum_name)

        video_curriculum_info_list.append(first_curriculum_info_list)

        for i in range(2,int(video_num)+1):
            one_curriculum_info_list = []

            one_curriculum_selector = detailvideopage.video_list_ul_selector + " > li:nth-child(%s) > a" % i
            one_curriculum_ele = activebroser.findELe(findstyle="css_selector",
                                                        findstylevalue=one_curriculum_selector)
            curriculum_url = one_curriculum_ele.get_attribute('href')
            print("curriculum_url:")
            print(curriculum_url)
            one_curriculum_info_list.append(curriculum_url)
            curriculum_name = one_curriculum_ele.get_attribute('title')
            print("curriculum_name:")
            print(curriculum_name)
            one_curriculum_info_list.append(curriculum_name)

            video_curriculum_info_list.append(one_curriculum_info_list)

        print("video_curriculum_info_list:")
        print(len(video_curriculum_info_list))
        print(video_curriculum_info_list)
        return video_curriculum_info_list











detailvideopagefunction = DetailVideoPageFunction()

if __name__ == '__main__':
    from WWTest.util.makeHtml import MakeHtml
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

    print("开始写入html")
    for one_video_list in all_data_list:
        video_url = one_video_list[0]
        print("video_url:")
        print(video_url)
        video_name = one_video_list[1]
        print("video_name:")
        print(video_name)
        video_curriculum_info_list = detailvideopagefunction.getVideoCurriculumListInfo(activebroser=ac,
                                                           video_url=video_url)
        mk = MakeHtml(video_title=video_name,
                      video_url=video_url,
                      curriculum_list=video_curriculum_info_list)
        mk.makeHtml()
        print("写入html完成")
        # break



    # ac.closeBrowse()

