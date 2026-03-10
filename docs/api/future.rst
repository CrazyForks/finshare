期货数据
========

get_future_kline
----------------

获取期货历史K线数据。

函数签名
~~~~~~~~

.. code-block:: python

    def get_future_kline(
        code: str,
        start_date: str = None,
        end_date: str = None,
        adjustment: str = "none",
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
     - 期货合约代码，如 ``cu0``、``IF2409``、``au0``
   * - start_date
     - str
     - 开始日期，格式 ``YYYY-MM-DD``
   * - end_date
     - str
     - 结束日期，格式 ``YYYY-MM-DD``
   * - adjustment
     - str
     - 复权类型（期货不支持，默认none）

返回值
~~~~~~

返回 ``List[HistoricalData]``，每个元素包含以下属性：

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 说明
   * - code
     - str
     - 期货合约代码
   * - trade_date
     - date
     - 交易日期
   * - open_price
     - float
     - 开盘价
   * - high_price
     - float
     - 最高价
   * - low_price
     - float
     - 最低价
   * - close_price
     - float
     - 收盘价
   * - volume
     - float
     - 成交量(手)

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取沪铜连续合约K线
    data = fs.get_future_kline('cu0', '2024-06-01', '2024-07-17')

    for item in data:
        print(f"{item.trade_date}: 开盘={item.open_price}, 收盘={item.close_price}")

输出结果：

::

    2024-06-03: 开盘=81510.0, 收盘=78500.0
    2024-06-04: 开盘=78320.0, 收盘=79230.0
    ...

支持品种
~~~~~~~~

.. code-block:: python

    # 金属期货
    'cu0'      # 沪铜连续
    'cu2409'   # 沪铜2409合约
    'au0'      # 沪金连续
    'ag0'      # 沪银连续

    # 股指期货
    'if0'      # 沪深300连续
    'ih0'      # 上证50连续
    'ic0'      # 中证500连续

    # 能源化工
    'ru0'      # 橡胶连续
    'sc0'      # 原油连续
    'ta0'      # PTA连续

    # 农产品
    'm0'       # 豆粕连续
    'y0'        # 豆油连续
    'p0'        # 棕榈油连续

连续合约说明
~~~~~~~~~~~~

- ``cu0`` - 当月连续
- ``cu1`` - 下月连续
- ``cu2`` - 下下月连续
- 以此类推

get_future_snapshot
-------------------

获取期货实时快照。

函数签名
~~~~~~~~

.. code-block:: python

    def get_future_snapshot(code: str)

返回值
~~~~~~

返回 ``FutureSnapshotData`` 对象。

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取期货快照
    snapshot = fs.get_future_snapshot('cu0')

    print(f"最新价: {snapshot.last_price}")
    print(f"涨跌额: {snapshot.change}")
    print(f"涨跌幅: {snapshot.change_pct}%")
    print(f"持仓量: {snapshot.open_interest}")
    print(f"成交量: {snapshot.volume}")

输出结果：

::

    最新价: 78500.0
    涨跌额: -3020.0
    涨跌幅: -3.70%
    持仓量: 123456.0
    成交量: 98765.0

get_batch_future_snapshots
--------------------------

批量获取期货快照。

函数签名
~~~~~~~~

.. code-block:: python

    def get_batch_future_snapshots(codes: list)

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 批量获取期货快照
    results = fs.get_batch_future_snapshots(['cu0', 'au0', 'ru0'])

    for code, snapshot in results.items():
        print(f"{code}: {snapshot.last_price} ({snapshot.change_pct:+.2f}%)")
