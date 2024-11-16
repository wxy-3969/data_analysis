'''
All the data in this project are created randomly and have no practical value.
They are for learning reference only.
'''

import pandas as pd
import numpy as np
import random
import string
from datetime import datetime, timedelta

# 生成随机订单编号
def generate_order_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

# 生成随机顾客ID
def generate_customer_id():
    return 'CUST' + ''.join(random.choices(string.digits, k=5))

# 生成随机商品ID
def generate_product_id():
    return 'PROD' + ''.join(random.choices(string.digits, k=5))

# 生成随机购买时间（过去一年内）
import datetime
import random
def generate_purchase_time():
    date = datetime.datetime.now() - datetime.timedelta(days = 365)
    random_days = random.randint(0, 364)
    random_seconds = random.randint(0, 86399)  # 一天中的秒数范围是0 - 86399
    new_date = date + datetime.timedelta(days = random_days, seconds = random_seconds)
    return new_date.strftime('%Y-%m-%d %H:%M:%S')

# 生成随机购买数量（1 - 10）
def generate_quantity():
    return random.randint(1, 10)

# 生成随机商品价格（10 - 1000）
def generate_price():
    return round(random.uniform(10, 1000), 2)

data = {
    '订单编号': [generate_order_id() for _ in range(2000)],
    '顾客ID': [generate_customer_id() for _ in range(2000)],
    '商品ID': [generate_product_id() for _ in range(2000)],
    '购买时间': [generate_purchase_time() for _ in range(2000)],
    '购买数量': [generate_quantity() for _ in range(2000)],
    '商品价格': [generate_price() for _ in range(2000)]
}

df = pd.DataFrame(data)
df.to_csv('Github\pandas\电商数据分析\data.csv', index=False)