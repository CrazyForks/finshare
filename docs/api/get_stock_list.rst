get_stock_list
===============

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
