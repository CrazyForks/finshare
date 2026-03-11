get_money_flow_industry
=========================

获取行业资金流向数据。

函数签名
~~~~~~~~

.. code-block:: python

    def get_money_flow_industry()

返回值
~~~~~~

返回 ``DataFrame``，包含以下字段：

.. list-table::
   :header-rows: 1

   * - 字段
     - 说明
   * - industry
     - 行业名称
   * - net_inflow
     - 净流入(元)
   * - net_inflow_ratio
     - 净流入占比(%)
   * - change_rate
     - 涨跌幅(%)

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取行业资金流向
    df = fs.get_money_flow_industry()
    print(df[['industry', 'net_inflow', 'change_rate']].head(10))
