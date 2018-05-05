"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""


def get_spent_time(in_calls):
    """
    取得每个号码所用的总计通话时间
    :param in_calls: list 通话记录集 
    :return: dict 通话时间最多的记录
    """
    spent_time = {}
    max_call = {'number': '', 'sum_time': 0}
    for item in in_calls:
        if item[0] not in spent_time:
            spent_time[item[0]] = int(item[3])
        else:
            spent_time[item[0]] += int(item[3])

        if item[1] not in spent_time:
            spent_time[item[1]] = int(item[3])
        else:
            spent_time[item[1]] += int(item[3])

    return max(spent_time.items(), key=lambda x: x[1])


call = get_spent_time(calls)
print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(call[0], call[1]))
