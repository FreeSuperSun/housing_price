# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import re


class PythonSpiderPipeline:

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('描述1'):
            content1 = adapter['描述1']
            content1_list2 = content1[1]
            content1_list2_split = content1_list2.split(' ')
            adapter['区域'] = content1_list2_split[0]
            adapter['小区'] = content1_list2_split[1]
            content1_list1 = content1[0]
            content1_list1_split = content1_list1.split('，')
            adapter['户型'] = content1_list1_split[0].partition('：')[-1]
            adapter['面积'] = content1_list1_split[1].partition(' ')[0]
            adapter['类型'] = content1_list1_split[2].partition('：')[-1]
            adapter['楼层'] = content1_list1_split[3].partition('(')[0][3:]
            adapter['总层'] = content1_list1_split[3].partition('(')[-1][1:-2]
            adapter.pop('描述1')
        if adapter.get('单价'):
            adapter['单价'] = re.findall(r'^\d+', adapter['单价'])[0]
        if adapter.get('更新时间'):
            adapter['更新时间'] = adapter['更新时间'].partition('：')[-1].strip()
        return item
