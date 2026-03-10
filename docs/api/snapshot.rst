实时快照
========

get_snapshot_data
----------------

获取单只股票的实时行情快照。

函数签名
~~~~~~~~

.. code-block:: python

    def get_snapshot_data(code: str)

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

返回 :class:`SnapshotData` 对象，属性说明：

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 说明
   * - code
     - str
     - 股票代码
   * - last_price
     - float
     - 最新价
   * - change
     - float
     - 涨跌额
   * - change_pct
     - float
     - 涨跌幅(%)
   * - volume
     - float
     - 成交量
   * - amount
     - float
     - 成交额
   * - open
     - float
     - 开盘价
   * - high
     - float
     - 最高价
   * - low
     - float
     - 最低价
   * - prev_close
     - float
     - 昨收价

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取单只股票快照
    snapshot = fs.get_snapshot_data('000001.SZ')

    print(f"股票代码: {snapshot.code}")
    print(f"最新价: {snapshot.last_price}")
    print(f"涨跌额: {snapshot.change}")
    print(f"涨跌幅: {snapshot.change_pct}%")
    print(f"成交量: {snapshot.volume}")
    print(f"成交额: {snapshot.amount}")

输出结果：

::

    股票代码: 000001.SZ
    最新价: 12.35
    涨跌额: 0.25
    涨跌幅: 2.07%
    成交量: 45678900.0
    成交额: 558123456.0

get_batch_snapshots
-------------------

批量获取多只股票的实时行情快照。

函数签名
~~~~~~~~

.. code-block:: python

    def get_batch_snapshots(codes: list)

参数说明
~~~~~~~~

.. list-table::
   :header-rows: 1

   * - 参数
     - 类型
     - 说明
   * - codes
     - list
     - 股票代码列表

返回值
~~~~~~

返回 ``Dict[str, SnapshotData]``，key为股票代码，value为快照对象。

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 批量获取快照
    codes = ['000001.SZ', '600519.SH', '510300', '159915']
    results = fs.get_batch_snapshots(codes)

    for code, snapshot in results.items():
        print(f"{code}: {snapshot.last_price} ({snapshot.change_pct:+.2f}%)")

输出结果：

::

    000001.SZ: 12.35 (+2.07%)
    600519.SH: 1688.00 (+1.25%)
    510300: 3.892 (+0.85%)
    159915: 2.156 (-0.32%)

支持的市场类型
~~~~~~~~~~~~~~

.. code-block:: python

    # A股
    snapshot = fs.get_snapshot_data('000001.SZ')   # 深圳
    snapshot = fs.get_snapshot_data('600519.SH')   # 上海

    # 港股
    snapshot = fs.get_snapshot_data('00700.HK')    # 腾讯控股

    # 美股
    snapshot = fs.get_snapshot_data('AAPL.US')     # 苹果

    # ETF
    snapshot = fs.get_snapshot_data('510300')      # 沪深300ETF
