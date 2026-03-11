get_money_flow
===============

获取个股资金流向数据。

函数签名
~~~~~~~~

.. code-block:: python

    def get_money_flow(code: str)

参数说明
~~~~~~~~

.. list-table::
   :header-rows: 1

   * - 参数
     - 类型
     - 说明
   * - code
     - str
     - 股票代码，如 ``000001.SZ``、``600519.SH``

返回值
~~~~~~

返回 ``DataFrame``，包含以下字段：

.. list-table::
   :header-rows: 1

   * - 字段
     - 说明
   * - fs_code
     - 股票代码
   * - trade_date
     - 交易日期
   * - net_inflow_main
     - 主力净流入(元)
   * - net_inflow_super
     - 超大单净流入(元)
   * - net_inflow_large
     - 大单净流入(元)
   * - net_inflow_medium
     - 中单净流入(元)
   * - net_inflow_small
     - 小单净流入(元)
   * - net_inflow_main_ratio
     - 主力净流入占比(%)

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取个股资金流向
    df = fs.get_money_flow('000001.SZ')
    print(df[['fs_code', 'trade_date', 'net_inflow_main', 'net_inflow_main_ratio']])
