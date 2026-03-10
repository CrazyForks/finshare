证券列表
========

get_stock_list
-------------

获取A股股票列表。

函数签名
~~~~~~~~

.. code-block:: python

    def get_stock_list(market: str = "all")

参数说明
~~~~~~~~

.. list-table::
   :header-rows: 1

   * - 参数
     - 类型
     - 说明
   * - market
     - str
     - 市场类型：``all``(全部)、``sh``(上海)、``sz``(深圳)

返回值
~~~~~~

返回 ``List[dict]``，每只股票包含：

.. list-table::
   :header-rows: 1

   * - 键
     - 类型
     - 说明
   * - code
     - str
     - 股票代码
   * - name
     - str
     - 股票名称
   * - price
     - float
     - 最新价
   * - change_pct
     - float
     - 涨跌幅(%)
   * - volume
     - float
     - 成交量
   * - amount
     - float
     - 成交额

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取全部A股列表
    stocks = fs.get_stock_list()

    # 获取上海A股
    sh_stocks = fs.get_stock_list('sh')

    # 获取深圳A股
    sz_stocks = fs.get_stock_list('sz')

    # 打印前10只
    for stock in stocks[:10]:
        print(f"{stock['code']}: {stock['name']} - {stock['price']} ({stock['change_pct']:+.2f}%)")

输出结果：

::

    300629: 新劲刚 - 28.91 (+20.01%)
    300936: 中英科技 - 58.54 (+20.01%)
    688655: 迅捷兴 - 29.40 (+20.00%)
    ...

get_etf_list
------------

获取ETF基金列表。

函数签名
~~~~~~~~

.. code-block:: python

    def get_etf_list()

返回值
~~~~~~

返回 ``List[dict]``，每只ETF包含实时行情。

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取ETF列表
    etfs = fs.get_etf_list()

    print(f"共有 {len(etfs)} 只ETF")
    print(f"前10只ETF:")

    for etf in etfs[:10]:
        print(f"  {etf['code']}: {etf['name']} - {etf['price']}")

输出结果：

::

    共有 100 只ETF
    前10只ETF:
      589780: 科创200ETF富国 - 1.24
      588140: 科创200ETF广发 - 1.22
      ...

常用ETF代码
~~~~~~~~~~~

.. code-block:: python

    # 宽基ETF
    '510300'  # 沪深300ETF
    '510500'  # 中证500ETF
    '159919'  # 创业板ETF
    '510050'  # 上证50ETF

    # 行业ETF
    '512880'  # 证券ETF
    '512690'  # 消费ETF
    '159995'  # 券商ETF

get_lof_list
------------

获取LOF基金列表。

函数签名
~~~~~~~~

.. code-block:: python

    def get_lof_list()

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取LOF列表
    lofs = fs.get_lof_list()

    print(f"共有 {len(lofs)} 只LOF")

    for lof in lofs[:10]:
        print(f"  {lof['code']}: {lof['name']}")

输出结果：

::

    共有 100 只LOF
      520500: 恒生创新药ETF
      159217: 港股通创新药ETF工银
      ...

get_future_list
---------------

获取期货列表。

函数签名
~~~~~~~~

.. code-block:: python

    def get_future_list()

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取期货列表
    futures = fs.get_future_list()

    print(f"共有 {len(futures)} 个期货合约")

    for future in futures[:10]:
        print(f"  {future['code']}: {future['name']}")
