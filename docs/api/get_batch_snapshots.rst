get_batch_snapshots
===================

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
