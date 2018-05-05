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
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


def get_record_texts(in_texts, no):
    """
    从短信记录集中读取指定记录
    :param in_texts: list 短信记录集
    :param no: int 指定记录号
    :return: 指定短信记录
    """
    return in_texts[no]


def get_record_calls(in_calls, no):
    """
    从短信记录集中读取指定记录
    :param in_calls: list 电话记录集
    :param no: int 指定记录号
    :return: 指定电话记录
    """
    return in_calls[no]


text = get_record_texts(texts, 0)
call = get_record_calls(calls, len(calls) - 1)
print('First record of texts, {} texts {} at time {}'.format(text[0], text[1], text[2]))
print('Last record of calls, {} calls {} at time {}, lasting {} seconds'.format(call[0], call[1], call[2], call[3]))
