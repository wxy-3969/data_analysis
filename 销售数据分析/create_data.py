import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# 生成示例数据
def generate_sales_data():
    num_records = 1000
    order_ids = [f"ORDER_{i}" for i in range(1, num_records + 1)]
    # 生成指定格式的下单日期
    order_dates = [(datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d') for _ in range(num_records)]
    # 生成随机商品编号
    product_ids = [f"PRODUCT_{random.randint(1000, 9999)}" for _ in range(num_records)]
    # 生成随机商品名称
    product_names = [f"Product_Name_{random.randint(1, 100)}" for _ in range(num_records)]
    # 生成随机单价
    unit_prices = [round(random.uniform(10, 500), 2) for _ in range(num_records)]
    # 生成随机数量
    quantities = [random.randint(1, 100) for _ in range(num_records)]
    # 生成随机客户编号
    customer_ids = [f"CUST_{random.randint(100, 999)}" for _ in range(num_records)]
    # 生成随机客户地区
    customer_regions = [random.choice(["North", "South", "East", "West", "Central"]) for _ in range(num_records)]
    # 创建数据字典
    data = {
        "订单编号": order_ids,
        "下单日期": order_dates,
        "商品编号": product_ids,
        "商品名称": product_names,
        "单价": unit_prices,
        "数量": quantities,
        "客户编号": customer_ids,
        "客户地区": customer_regions
    }
    return pd.DataFrame(data)
# 生成数据并保存为CSV文件
sales_data = generate_sales_data()
sales_data.to_csv("Github\pandas\销售数据分析\sales_data.csv", index=False)