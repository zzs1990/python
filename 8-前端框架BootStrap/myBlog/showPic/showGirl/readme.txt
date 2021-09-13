1. 新建模板：
新建目录  templates

2. 定义首页的视图函数:
打开 views.py 文件，新建一个 show_girl 函数，参数是 request

3. 准备URL -- 给函数分配一个 url :
返回到showPic目录下，编辑urls.py 文件，
从 showGirl.views 中导入 show_girl 函数，然后在 urlpatterns 中进行设置