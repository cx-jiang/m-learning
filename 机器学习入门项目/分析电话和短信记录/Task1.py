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
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."""


def get_phones_count(in_texts, in_calls):
    """
    统计短信和通话记录中电话号码的数量
    :param in_texts: list 短信记录集
    :param in_calls: list 电话记录集
    :return: int 号码合计数量
    """
    sum_numbers = set()
    for text in in_texts:
        if text[0] not in sum_numbers:
            sum_numbers.add(text[0])
        if text[1] not in sum_numbers:
            sum_numbers.add(text[1])

    for call in in_calls:
        if call[0] not in sum_numbers:
            sum_numbers.add(call[0])
        if call[1] not in sum_numbers:
            sum_numbers.add(call[1])

    return len(sum_numbers)


rtn_number = get_phones_count(texts, calls)
print("There are {} different telephone numbers in the records.".format(rtn_number))
