基金数据
========

get_fund_nav
------------

获取基金净值数据。

函数签名
~~~~~~~~

.. code-block:: python

    def get_fund_nav(
        code: str,
        start_date: str = None,
        end_date: str = None,
    )

参数说明
~~~~~~~~

.. list-table::
   :header-rows: 1

   * - 参数
     - 类型
     - 说明
   * - code
     - str
     - 基金代码，如 ``161039``、``000001``
   * - start_date
     - str
     - 开始日期，格式 ``YYYY-MM-DD``
   * - end_date
     - str
     - 结束日期，格式 ``YYYY-MM-DD``

返回值
~~~~~~

返回 ``List[FundData]``，每个元素包含以下属性：

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 说明
   * - code
     - str
     - 基金代码
   * - name
     - str
     - 基金名称
   * - nav
     - float
     - 单位净值
   * - nav_acc
     - float
     - 累计净值
   * - change
     - float
     - 涨跌额
   * - change_pct
     - float
     - 涨跌幅(%)
   * - nav_date
     - date
     - 净值日期

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取基金净值
    data = fs.get_fund_nav('161039', '2024-01-01', '2024-12-31')

    for item in data:
        print(f"{item.nav_date}: nav={item.nav:.4f}, change_pct={item.change_pct:+.2f}%")

输出结果：

::

    2024-01-02: nav=1.8222, change_pct=-0.35%
    2024-01-03: nav=1.8356, change_pct=+0.74%
    ...

获取最新净值
~~~~~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取最近30天数据
    data = fs.get_fund_nav('161039')

    # 最新净值
    latest = data[-1]
    print(f"最新净值: {latest.nav}")
    print(f"最新日期: {latest.nav_date}")

get_fund_info
-------------

获取基金基本信息。

函数签名
~~~~~~~~

.. code-block:: python

    def get_fund_info(code: str)

返回值
~~~~~~

返回 ``dict``，包含基金基本信息。

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    info = fs.get_fund_info('161039')
    print(info)

输出结果：

::

    {'code': '161039', 'name': '富国中证1000指数增强(LOF)A', ...}

get_fund_list
--------------

获取基金列表。

函数签名
~~~~~~~~

.. code-block:: python

    def get_fund_list(market: str = "all")

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

返回 ``List[dict]``，基金列表。

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取基金列表
    funds = fs.get_fund_list()
    print(f"共有 {len(funds)} 只基金")

常见基金代码
~~~~~~~~~~~~

.. code-block:: python

    # 货币基金
    '000001'  # 平安财富宝货币A

    # 股票基金
    '110011'  # 易方达消费行业股票

    # 指数基金
    '161039'  # 富国中证1000指数增强(LOF)A

    # QDII基金
    '110022'  # 易方达恒生ETF联接(QDII)
