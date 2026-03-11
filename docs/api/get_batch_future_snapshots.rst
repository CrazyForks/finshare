get_batch_future_snapshots
===========================

批量获取期货实时快照。

函数签名
~~~~~~~~

.. code-block:: python

    def get_batch_future_snapshots(codes: list)

返回值
~~~~~~

返回 ``Dict[str, FutureSnapshotData]``。

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 批量获取期货快照
    results = fs.get_batch_future_snapshots(['IF2409', 'CU2409', 'AU2409', 'SC2409'])

    for code, snapshot in results.items():
        print(f"{code}: {snapshot.last_price} ({snapshot.change_pct:+.2f}%)")

输出结果：

::

    IF2409: 3450.0 (+0.88%)
    CU2409: 78500.0 (-1.20%)
    AU2409: 580.0 (+0.50%)
    SC2409: 620.0 (-2.15%)
