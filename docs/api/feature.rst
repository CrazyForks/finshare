特色数据
=========

get_money_flow
--------------

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
     - 类型
     - 说明
   * - fs_code
     - str
     - 股票代码
   * - trade_date
     - str
     - 交易日期
   * - net_inflow_main
     - float
     - 主力净流入(元)
   * - net_inflow_super
     - float
     - 超大单净流入(元)
   * - net_inflow_large
     - float
     - 大单净流入(元)
   * - net_inflow_medium
     - float
     - 中单净流入(元)
   * - net_inflow_small
     - float
     - 小单净流入(元)
   * - net_inflow_main_ratio
     - float
     - 主力净流入占比(%)

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取个股资金流向
    df = fs.get_money_flow('000001.SZ')
    print(df[['fs_code', 'trade_date', 'net_inflow_main', 'net_inflow_main_ratio']].head(10))

输出结果：

::

       fs_code  trade_date  net_inflow_main  net_inflow_main_ratio
    0  000001.SZ   20241018  -15236800.0              -15.23
    1  000001.SZ   20241017    8345600.0                8.34
    ...

get_money_flow_industry
-----------------------

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
     - 类型
     - 说明
   * - industry
     - str
     - 行业名称
   * - net_inflow
     - float
     - 净流入(元)
   * - net_inflow_ratio
     - float
     - 净流入占比(%)
   * - change_rate
     - float
     - 涨跌幅(%)

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取行业资金流向
    df = fs.get_money_flow_industry()
    print(df[['industry', 'net_inflow', 'change_rate']].head(10))

输出结果：

::

              industry     net_inflow  change_rate
    0        酿酒行业  1.234567e+09         2.35
    1        银行   8.765432e+08        -0.45
    ...

get_lhb
-------

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
     - 类型
     - 说明
   * - fs_code
     - str
     - 股票代码
   * - trade_date
     - str
     - 上榜日期
   * - close_price
     - float
     - 收盘价
   * - change_rate
     - float
     - 涨跌幅
   * - net_buy_amount
     - float
     - 龙虎榜净买额
   * - buy_amount
     - float
     - 龙虎榜买入额
   * - sell_amount
     - float
     - 龙虎榜卖出额
   * - turnover_rate
     - float
     - 换手率
   * - reason
     - str
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
    print(df)

输出结果：

::

       fs_code  trade_date  net_buy_amount     reason
    0  000001.SZ   20241018    12345678.0   日涨幅偏离值达7%
    ...

get_lhb_detail
--------------

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
     - 类型
     - 说明
   * - fs_code
     - str
     - 股票代码
   * - trade_date
     - str
     - 交易日期
   * - broker_name
     - str
     - 营业部名称
   * - buy_amount
     - float
     - 买入金额
   * - sell_amount
     - float
     - 卖出金额
   * - net_amount
     - float
     - 净买额

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取个股龙虎榜明细
    df = fs.get_lhb_detail('000001.SZ')
    print(df[['broker_name', 'buy_amount', 'sell_amount', 'net_amount']])

输出结果：

::

        broker_name   buy_amount   sell_amount   net_amount
    0   机构专用    12345678.0    2345678.0  10000000.0
    ...

get_margin
----------

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
     - 类型
     - 说明
   * - fs_code
     - str
     - 股票代码
   * - trade_date
     - str
     - 交易日期
   * - rzye
     - float
     - 融资余额(元)
   * - rqyl
     - float
     - 融券余量(股)
   * - rzje
     - float
     - 融资买入额(元)
   * - rqmcl
     - float
     - 融券卖出量(股)
   * - rzrqye
     - float
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

输出结果：

::

       trade_date         rzye       rqyl       rzrqye
    0   20241018  1234567890.0  1234567.0  1358023456.0
    ...

get_margin_detail
-----------------

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
     - 类型
     - 说明
   * - fs_code
     - str
     - 股票代码
   * - trade_date
     - str
     - 交易日期
   * - rzye
     - float
     - 融资余额(元)
   * - rqyl
     - float
     - 融券余量(股)
   * - rzrqye
     - float
     - 融资融券余额(元)

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取个股融资融券明细
    df = fs.get_margin_detail('000001.SZ')
    print(df)

输出结果：

::

       fs_code  trade_date         rzye       rqyl       rzrqye
    0  000001.SZ   20241018  123456789.0  123456.0  135802345.0
    ...
