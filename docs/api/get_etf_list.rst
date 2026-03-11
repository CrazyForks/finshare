get_etf_list
=============

获取ETF基金列表。

函数签名
~~~~~~~~

.. code-block:: python

    def get_etf_list()

返回值
~~~~~~

返回 ``List[dict]``，每只ETF包含实时行情。

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取ETF列表
    etfs = fs.get_etf_list()

    print(f"共有 {len(etfs)} 只ETF")
    print(f"前10只ETF:")

    for etf in etfs[:10]:
        print(f"  {etf['code']}: {etf['name']} - {etf['price']}")

常用ETF代码
~~~~~~~~~~~

.. code-block:: python

    # 宽基ETF
    '510300'  # 沪深300ETF
    '510500'  # 中证500ETF
    '159919'  # 创业板ETF
    '510050'  # 上证50ETF
