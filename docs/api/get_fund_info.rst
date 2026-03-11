get_fund_info
=============

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
