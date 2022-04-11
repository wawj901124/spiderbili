import os

class MakeHtml(object):

    def __init__(self,video_title,video_url,curriculum_list):
        self.video_title = video_title
        self.video_url = video_url
        self.curriculum_list = curriculum_list
        self.curriculum_list_len = len(curriculum_list)


    def makeHtml(self):
        moban_tou = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>%s</title>
</head>
<body> 
<table border = "1">
    <tr>
        <th>课程</th>
        <th>章节</th>
    </tr>
    <tr>
        <td rowspan = "%s"><a href="%s">%s</a></td> """ % (self.video_title,
                                          self.curriculum_list_len,
                                          self.video_url,
                                          self.video_title)
        moban_content = ""

        moban_first_curriculum = """
        <td><a href="%s">%s</a></td>
    </tr>""" % (self.curriculum_list[0][0],self.curriculum_list[0][1])
        moban_content = moban_content + moban_first_curriculum

        for i  in range(2,self.curriculum_list_len):
            moban_other_curriculum = """
    <tr>
        <td><a href="%s">%s</a></td>
    </tr>
            """ % (self.curriculum_list[i][0],self.curriculum_list[i][1])
            moban_content = moban_content + moban_other_curriculum

        moban_wei = """
</table>
</body>
</html>
        """

        moban = moban_tou+moban_content+moban_wei

        print("moban:")
        print(moban)

        #将内容写入文件
        with open (file="%s.html" % self.video_title,
                   mode="w",
                   encoding="utf-8") as f1:
            f1.write(moban)

        return moban

if __name__ == '__main__':
    pass
