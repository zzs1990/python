# -*- coding: utf-8 -*-
"""
******************** 人生苦短，我用Python ********************
--- Day 1: ***
--- Notes:
  --1.想了解python的发展历史，请移步链接：
      https://www.cnblogs.com/vamei/archive/2013/02/06/2892628.html
--- Author: zhangzai
--- My Motto:
  --1. 达则兼济天下，穷则独善其身
  --2. 修学储能，先博后渊
******************** 人生苦短，我用Python ********************
"""
# import this
import turtle


def paint_a_triangle():
    turtle.pensize(4)
    turtle.pencolor('red')

    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)

    turtle.mainloop()


def main():
    paint_a_triangle()


if __name__ == "__main__":
    main()
