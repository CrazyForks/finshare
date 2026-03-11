get_future_snapshot
===================

获取期货实时快照。

函数签名
~~~~~~~~

.. code-block:: python

    def get_future_snapshot(code: str)

返回值
~~~~~~

返回 ``FutureSnapshotData`` 对象，包含以下属性：

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 说明
   * - code
     - str
     - 合约代码
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
     - 成交量(手)
   * - open_interest
     - float
     - 持仓量(手)
   * - amount
     - float
     - 成交额(元)

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取期货快照
    snapshot = fs.get_future_snapshot('IF2409')

    print(f"合约: {snapshot.code}")
    print(f"最新价: {snapshot.last_price}")
    print(f"涨跌额: {snapshot.change}")
    print(f"涨跌幅: {snapshot.change_pct}%")
    print(f"持仓量: {snapshot.open_interest}")
