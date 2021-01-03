# -*- coding: utf-8 -*-


class SeqList:
    """
    顺序表的3种操作：初始化，插入元素，求指定位置元素
    """
    @staticmethod
    def init():
        """
        初始化一个空顺序表
        :return: 空列表
        """
        return []

    @staticmethod
    def insert(seq_list, index, value):
        """
        向顺序表指定位置插入元素
        :param seq_list: 待操作的顺序表
        :param index: 插入位置
        :param value: 待插入元素
        :return: 插入新元素后的顺序表
        """
        seq_len = len(seq_list)
        if index < 0 or index > seq_len:
            return None
        seq_list.insert(index, value)
        return seq_list

    @staticmethod
    def find(seq_list, index):
        if index not in range(len(seq_list)):
            value = None
        else:
            value = seq_list[index]
        return value


def main():
    # 创建一个顺序表对象
    seq_obj = SeqList()
    print(f"seq_obj: {seq_obj}")

    # 初始化一个空顺序表
    seq_list = seq_obj.init()
    print(f"初始化一个空顺序表: {seq_list}")
    # 向顺序表插入元素
    for i in range(5):
        seq_list = seq_obj.insert(seq_list, i, 2 * i)
    print(f"插入5个值后，顺序表为：{seq_list}")

    # index = -10
    # value = 50
    # seq_list = seq_obj.insert(seq_list, -10, 50)
    # print(f"在顺序表索引{index}处插入元素{value}后，顺序表变为：{seq_list}")

    # 获取指定位置元素
    index = 6
    index_2_elem = seq_obj.find(seq_list, index)
    if index_2_elem is None:
        print(f"输入的索引{index}无效")
    else:
        print(f"顺序表中索引{index}处的元素为：{index_2_elem}")


if __name__ == "__main__":
    main()
