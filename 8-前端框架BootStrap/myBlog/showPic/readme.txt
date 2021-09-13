检查项目是否安装成功
1. 终端执行：python manage.py runserver
根据提示网址如 http://127.0.0.1:8000/ 打开网页
提示“The install worked successfully! Congratulations!” 则表示安装成功

2. 创建app：showGirl，会生成一个 showGirl 目录
python manage.py startapp showGirl

3. 在 INSTALLED_APPS 下新增 showGirl

4. 项目启动测试
python manage.py runserver