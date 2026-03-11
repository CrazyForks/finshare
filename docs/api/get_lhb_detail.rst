get_lhb_detail
===============

获取龙虎榜明细数据。

函数签名
~~~~~~~~

.. code-block:: python

    def get_lhb_detail(code: str, trade_date: str = None)

参数说明
~~~~~~~~

.. list-table::
   :header-rows: 1

   * - 参数
     - 类型
     - 说明
   * - code
     - str
     - 股票代码，如 ``000001.SZ``
   * - trade_date
     - str
     - 交易日期，格式 ``YYYYMMDD``，默认今天

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
   * - broker_name
     - 营业部名称
   * - buy_amount
     - 买入金额
   * - sell_amount
     - 卖出金额
   * - net_amount
     - 净买额

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取个股龙虎榜明细
    df = fs.get_lhb_detail('000001.SZ')
    print(df[['broker_name', 'buy_amount', 'sell_amount', 'net_amount']])
