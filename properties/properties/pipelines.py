# coding:utf-8
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class SomePipeline(object):

    def __init__(self):
        self.file = open('item.jl', 'ab')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), sort_keys=True,
                          indent=4, ensure_ascii=False) + '\n'
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()
