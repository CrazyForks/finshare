get_future_list
===============

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
