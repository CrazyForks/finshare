财务数据
=========

get_income
----------

获取利润表数据。

函数签名
~~~~~~~~

.. code-block:: python

    def get_income(code: str, start_date: str = None, end_date: str = None)

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取利润表
    df = fs.get_income('000001.SZ')
    print(df.head())

输出结果：

::

         fs_code  report_date  total_revenue  total_cost  ...
    0  000001.SZ   20240630      1234567890    987654321
    ...

get_balance
-----------

获取资产负债表数据。

函数签名
~~~~~~~~

.. code-block:: python

    def get_balance(code: str, start_date: str = None, end_date: str = None)

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    df = fs.get_balance('000001.SZ')
    print(df.head())

get_cashflow
------------

获取现金流量表数据。

函数签名
~~~~~~~~

.. code-block:: python

    def get_cashflow(code: str, start_date: str = None, end_date: str = None)

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    df = fs.get_cashflow('000001.SZ')
    print(df.head())

get_financial_indicator
-----------------------

获取财务指标数据。

函数签名
~~~~~~~~

.. code-block:: python

    def get_financial_indicator(code: str, ann_date: str = None)

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    df = fs.get_financial_indicator('000001.SZ')
    print(df.head())

输出结果：

::

         fs_code  report_date  eps   roe  gross_margin  debt_to_assets
    0  000001.SZ   20240630  0.85  10.2          25.3           93.5
    ...

get_dividend
------------

获取分红送转数据。

函数签名
~~~~~~~~

.. code-block:: python

    def get_dividend(code: str)

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    df = fs.get_dividend('000001.SZ')
    print(df.head())
