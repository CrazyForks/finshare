get_lof_list
============

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
