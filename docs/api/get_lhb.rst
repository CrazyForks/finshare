get_lhb
=======

获取龙虎榜数据。

函数签名
~~~~~~~~

.. code-block:: python

    def get_lhb(start_date: str = None, end_date: str = None)

参数说明
~~~~~~~~

.. list-table::
   :header-rows: 1

   * - 参数
     - 类型
     - 说明
   * - start_date
     - str
     - 开始日期，格式 ``YYYYMMDD``，默认最近30天
   * - end_date
     - str
     - 结束日期，格式 ``YYYYMMDD``，默认今天

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
     - 上榜日期
   * - close_price
     - 收盘价
   * - change_rate
     - 涨跌幅
   * - net_buy_amount
     - 龙虎榜净买额
   * - buy_amount
     - 龙虎榜买入额
   * - sell_amount
     - 龙虎榜卖出额
   * - turnover_rate
     - 换手率
   * - reason
     - 上榜原因

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取最近30天龙虎榜
    df = fs.get_lhb()
    print(df[['fs_code', 'trade_date', 'net_buy_amount', 'reason']].head(10))

    # 指定日期范围
    df = fs.get_lhb('20241001', '20241018')
