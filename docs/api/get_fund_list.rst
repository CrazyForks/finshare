get_fund_list
=============

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
