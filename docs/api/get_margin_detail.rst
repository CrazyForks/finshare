get_margin_detail
=================

获取个股融资融券明细。

函数签名
~~~~~~~~

.. code-block:: python

    def get_margin_detail(code: str, trade_date: str = None)

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
   * - rzye
     - 融资余额(元)
   * - rqyl
     - 融券余量(股)
   * - rzrqye
     - 融资融券余额(元)

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取个股融资融券明细
    df = fs.get_margin_detail('000001.SZ')
    print(df)
