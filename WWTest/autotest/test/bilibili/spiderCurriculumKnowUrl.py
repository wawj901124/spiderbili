#爬取课程

from WWTest.base.activeBrowser import ActiveBrowser
from WWTest.autotest.config.bilibili.page.loginPage import lpf
from WWTest.autotest.config.bilibili.page.indexSearch import indexpage,indexpagefunction
from WWTest.autotest.config.bilibili.page.detailvideo import detailvideopage,detailvideopagefunction
from WWTest.util.makeHtml import MakeHtml


ac = ActiveBrowser()

video_url = "https://www.bilibili.com/video/BV1eq4y1V7iH"
print("video_url:")
print(video_url)
video_name = "【首发】入门必看，性能测试指标详解，小白从零入门性能测试"
print("video_name:")
print(video_name)
video_curriculum_info_list = detailvideopagefunction.getVideoCurriculumListInfo(activebroser=ac,
                                                                                video_url=video_url)
mk = MakeHtml(video_title=video_name,
              video_url= video_url,
              curriculum_list=video_curriculum_info_list)
mk.makeHtml()
print("写入html完成")