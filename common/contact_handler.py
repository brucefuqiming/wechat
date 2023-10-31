import csv
from common.base_setting import BaseSetting


class ContactHandler(object):
    def __init__(self):
        # 当前要写入的路径
        self.current_contact_path = BaseSetting().current_contact_path
        print(f"# 通讯录保存路径: {self.current_contact_path}")
        # csv header
        self.header = ['remark', 'nickname', 'account', 'region', 'name', 'state', 'desc']
        # 文件流
        self.file_stream = None
        self.csv_writer = None
        self.init()

        # 滑动的每一页数据
        self.list_element = []

    def init(self):
        """
        初始化文件流
        :return:
        """
        self.file_stream = open(self.current_contact_path, 'w', encoding='utf-8', newline='')
        self.csv_writer = csv.DictWriter(self.file_stream, self.header)
        self.csv_writer.writeheader()

    def write_row(self, data):
        """
        写入本地csv
        :param data:
        :return:
        """
        if data is not None and not all(value is None for value in data.values()):
            self.csv_writer.writerow(data)

    def close_stream(self):
        """
        关闭文件流
        :return:
        """
        if self.file_stream is not None:
            self.file_stream.close()

    def append_element(self, element):
        """
        记录element用于判断是否点击过
        :param element:
        :return:
        """
        self.list_element.append(element)
        if len(self.list_element) > 15:
            self.list_element = self.list_element[-15:]

    def element_is_exists(self, element):
        """
        匹配
        :param element:
        :return:
        """
        # if element in self.list_element:
        #     index = self.list_element.index(element)
        #     print(f"list_element 数量为 {len(self.list_element)}, 当前在索引{index}")

        if element in self.list_element:
            return True
        return False
