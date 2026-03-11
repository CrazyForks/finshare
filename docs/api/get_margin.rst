get_margin
==========

获取融资融券数据。

函数签名
~~~~~~~~

.. code-block:: python

    def get_margin(code: str = None)

参数说明
~~~~~~~~

.. list-table::
   :header-rows: 1

   * - 参数
     - 类型
     - 说明
   * - code
     - str
     - 股票代码，如 ``000001.SZ``、``600519.SH``，不传则获取市场汇总

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
   * - rzye
     - 融资余额(元)
   * - rqyl
     - 融券余量(股)
   * - rzje
     - 融资买入额(元)
   * - rzrqye
     - 融资融券余额(元)

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取个股融资融券
    df = fs.get_margin('000001.SZ')
    print(df[['trade_date', 'rzye', 'rqyl', 'rzrqye']].head(10))

    # 获取市场汇总
    df = fs.get_margin()
    print(df.head())
