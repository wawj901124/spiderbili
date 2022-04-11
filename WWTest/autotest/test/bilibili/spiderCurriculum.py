#爬取课程

from WWTest.base.activeBrowser import ActiveBrowser
from WWTest.autotest.config.bilibili.page.loginPage import lpf
from WWTest.autotest.config.bilibili.page.indexSearch import indexpage,indexpagefunction
from WWTest.autotest.config.bilibili.page.detailvideo import detailvideopage,detailvideopagefunction
from WWTest.util.makeHtml import MakeHtml

search_text="常见漏洞"

ac = ActiveBrowser()
lpf.login(activebroser=ac)
indexpagefunction.indexSearch(activebroser=ac,
                              search_text=search_text)
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
                  video_url= video_url,
                  curriculum_list=video_curriculum_info_list)
    mk.makeHtml()
    print("写入html完成")