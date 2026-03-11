get_fund_nav
============

获取基金净值数据。

函数签名
~~~~~~~~

.. code-block:: python

    def get_fund_nav(
        code: str,
        start_date: str = None,
        end_date: str = None,
    )

参数说明
~~~~~~~~

.. list-table::
   :header-rows: 1

   * - 参数
     - 类型
     - 说明
   * - code
     - str
     - 基金代码，如 ``161039``、``000001``
   * - start_date
     - str
     - 开始日期，格式 ``YYYY-MM-DD``
   * - end_date
     - str
     - 结束日期，格式 ``YYYY-MM-DD``

返回值
~~~~~~

返回 ``List[FundData]``，每个元素包含以下属性：

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 说明
   * - code
     - str
     - 基金代码
   * - name
     - str
     - 基金名称
   * - nav
     - float
     - 单位净值
   * - nav_acc
     - float
     - 累计净值
   * - change
     - float
     - 涨跌额
   * - change_pct
     - float
     - 涨跌幅(%)
   * - nav_date
     - date
     - 净值日期

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取基金净值
    data = fs.get_fund_nav('161039', '2024-01-01', '2024-12-31')

    for item in data:
        print(f"{item.nav_date}: nav={item.nav:.4f}, change_pct={item.change_pct:+.2f}%")

输出结果：

::

    2024-01-02: nav=1.8222, change_pct=-0.35%
    2024-01-03: nav=1.8356, change_pct=+0.74%
    ...
