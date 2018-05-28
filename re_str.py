# -*- coding:utf-8 -*-
import re

str1 = """序号 股东 持股比例 认缴出资额（万元） 认缴出资日期 股东类型 # 1  陈炳文 他关联 2 家公司 >   |                16.6667%|             |                  10000万元                  |                 -              自然人股东 # 2  陈家锋 他关联 6 家公司 >   |                16.6667%|             |                  10000万元                  |                 -              自然人股东 # 3  陈春满 他关联 3 家公司 >   |                16.6667%|             |                  10000万元                  |                 -              自然人股东 # 4  陈景桂 他关联 2 家公司 >   |                16.6667%|             |                  10000万元                  |                 -              自然人股东 # 5  陈永安 他关联 4 家公司 >   |                16.6667%|             |                  10000万元                  |                 -              自然人股东 # 6  陈建宏 他关联 2 家公司 >   |                16.6667%|             |                  10000万元                  |                 -              自然人股东
 序号 股东 持股比例 认缴出资额（万元） 认缴出资日期 股东类型 # 1  辽宁禾丰牧业股份有限公司   |                70.0%|             |                  700                  |                  2006-08-29                  其他投资者 # 2  北京首都农业集团有限公司  |                30.0%|             |                  300                  |                  2006-08-29                  其他投资者
 序号 股东 持股比例 认缴出资额（万元） 认缴出资日期 股东类型 # 1  英属维尔京群岛天时农业控股有限公司  |                100%|             |                  9999                  |                 -              法人股东
 序号 股东 持股比例 认缴出资额（万元） 认缴出资日期 股东类型 # 1  罗海燕  他关联 1 家公司 >   |                60.0%|             |                  1200                  |                 -              自然人股东 # 2  祝华茂 他关联 3 家公司 >   |                40.0%|             |                  800                  |                 -              自然人股东
 序号 股东 持股比例 认缴出资额（万元） 认缴出资日期 股东类型 # 1  沈世兵 他关联 4 家公司 >   |                -|             |                 -              |                 -              自然人股东 # 2  王玉清 他关联 2 家公司 >   |                -|             |                 -              |                 -              自然人股东 # 3  孙贤友 他关联 5 家公司 >   |                -|             |                 -              |                 -              自然人股东
 序号 股东 持股比例 认缴出资额（万元） 认缴出资日期 股东类型 # 1  王建峰  他关联 6 家公司 >   |                90.0%|             |                  2430                  |                  2014-03-08                  自然人股东 # 2  马莲莲 他关联 3 家公司 >   |                10.0%|             |                  270                  |                  2014-03-08                  自然人股东
 序号 股东 持股比例 认缴出资额（万元） 认缴出资日期 股东类型 # 1  李喜红  他关联 2 家公司 >   |                40.0%|             |                  480.000000                  |                 -              自然人股东 # 2  蒲冰 他关联 2 家公司 >   |                30.0%|             |                  360.000000                  |                 -              自然人股东 # 3  李巧怀 他关联 1 家公司 >   |                10.0%|             |                  120.000000                  |                 -              自然人股东 # 4  曹红琴 他关联 1 家公司 >   |                10.0%|             |                  120.000000                  |                 -              自然人股东 # 5  吴文平 他关联 2 家公司 >   |                10.0%|             |                  120.000000                  |                 -              自然人股东
 序号 股东 持股比例 认缴出资额（万元） 认缴出资日期 股东类型 # 1  沈连英等  他关联 1 家公司 >   |                70.4379%|             |                  899.2571,                  899.2571                  |                  2009-04-02,                  2009-04-02                  自然人股东 # 2  北京市昌平区城南街道山侠社区居委会  |                29.5621%|             |                  377.4096                  |                  2009-04-02                  其他投资者
 序号 股东 持股比例 认缴出资额（万元） 认缴出资日期 股东类型 # 1  仵天富  他关联 2 家公司 >   |                66.6667%|             |                  800.000000 万元                  |                  2009-07-03                  - # 2  闫德华 他关联 1 家公司 >   |                8.3333%|             |                  100.000000 万元                  |                  2009-07-03                  - # 3  杨涛 他关联 2 家公司 >   |                8.3333%|             |                  100.000000 万元                  |                  2009-07-03                  - # 4  闫振 他关联 1 家公司 >   |                8.3333%|             |                  100.000000 万元                  |                  2009-07-03                  - # 5  刘国贤 他关联 1 家公司 >   |                8.3333%|             |                  100.000000 万元                  |                  2009-07-03                  -
 序号 股东 持股比例 认缴出资额（万元） 认缴出资日期 股东类型 # 1  秦皇岛宝硕商贸集团有限公司   |                90.0%|             |                  900                  |                 -              企业法人 # 2  沈静 他关联 7 家公司 >   |                10.0%|             |                  100                  |                 -              自然人股东"""

str2 = """序号 股东 持股比例 认缴出资额（万元） 认缴出资日期 股东类型 # 1  王建峰  他关联 6 家公司 >   |                90.0%|             |                  2430                  |                  2014-03-08                  自然人股东 # 2  马莲莲 他关联 3 家公司 >   |                10.0%|             |                  270                  |                  2014-03-08                  自然人股东
 序号 股东 持股比例 认缴出资额（万元） 认缴出资日期 股东类型 # 1  李喜红  他关联 2 家公司 >   |                40.0%|             |                  480.000000                  |                 -              自然人股东 # 2  蒲冰 他关联 2 家公司 >   |                30.0%|             |                  360.000000                  |                 -              自然人股东 # 3  李巧怀 他关联 1 家公司 >   |                10.0%|             |                  120.000000                  |                 -              自然人股东 # 4  曹红琴 他关联 1 家公司 >   |                10.0%|             |                  120.000000                  |                 -              自然人股东 # 5  吴文平 他关联 2 家公司 >   |                10.0%|             |                  120.000000                  |                 -              自然人股东"""

pt = re.compile(r"#(.*?)东")
group = pt.findall(str1)
print group


# print group[5]

# print group[1].split("|")[3]

# def check_digit(str1):
#     for char in str1:
#         if char.isdigit():
#             return True
#     return False

for line in group:
    line = line.strip()
    # print line
    item = line.split("|")
    queries = item[0]
    list1 = queries.split(" ")
    query = list1[0]
    StockName = list1[2]
    CompLinkNum = list1[4]
    # print query
    # print StockName
    # print  CompLinkNum
    CapiRate = item[1].strip()
    Unit = item[3].strip()
    # StockType = item[-1].replace(" ","").replace("-","")
    item6 = item[-1].replace(" ", "")
    # print item6
    m = re.search(r"\d{4}-\d{2}-\d{2}",item6)
    if m is not None:
        ShoudDate = item6[0:10]
        StockType = item6[10:]
        # print StockType
        # print ShoudDate
    else:
        ShoudDate = "-"
        StockType = item6.replace("-", "")
    # print query
    # print CapiRate
    # print Unit
    # print StockType
    # print ShoudDate