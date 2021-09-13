# -*- coding: utf-8 -*-
from pywebio.input import *

# 文本输入
input("What's your name?")

# 下拉选择
select('Select', ['A', 'B'])

# 多选
checkbox("Checkbox", options=['Check me'])

# 单选
radio("Radio", options=['A', 'B', 'C'])

# 多行文本输入
textarea('Text', placeholder='Some text')

# 文件上传
file_upload("Select a file:")

# 代码编辑
textarea('Code Edit', code={
    'mode': "python",
    'theme': 'darcula',
}, value='import ...')

# 输入组
input_group("Basic info", [
    input('Name', name='name'),
    input('Age', name='age'),
])


# 输入校验
def check(p):
    if p != 2:
        return 'Wrong!'


input("1+1=?", type=NUMBER, validate=check)
