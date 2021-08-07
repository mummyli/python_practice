from xml.etree.ElementTree import iterparse

def parse_and_remove(filename, path):
    path_parts = path.split("/")

    # 事件列表： start , end, start-ns 和 end-ns 
    # start 事件在某个元素第一次被创建并且还没有被插入其他数据(如子元素)时被创建。 
    # end 事件在某个元素已经完成时被创建
    # start-ns 和 end-ns 事件被用来处理XML文档命名空间的声明。
    doc = iterparse(filename, ("start", "end"))

    # kip root
    next(doc)

    tag_stack = []
    elem_stack = []

    for even, elem in doc:
        if even == "start":
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif even == "end":
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


from collections import Counter

potholes_by_zip = Counter()

data = parse_and_remove("./testfiles/potholes.xml", "row/row")

for pothole in data:
    potholes_by_zip[pothole.findtext("zip")] += 1
for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)