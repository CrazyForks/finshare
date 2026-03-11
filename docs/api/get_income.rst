get_income
==========

获取利润表数据。

函数签名
~~~~~~~~

.. code-block:: python

    def get_income(
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
     - 股票代码，如 ``600519.SH``
   * - start_date
     - str
     - 开始日期（暂不支持）
   * - end_date
     - str
     - 结束日期（暂不支持）

返回值
~~~~~~

返回 :class:`pandas.DataFrame`，包含以下列：

.. list-table::
   :header-rows: 1

   * - 列名
     - 说明
   * - fs_code
     - 股票代码
   * - ann_date
     - 公告日期
   * - report_date
     - 报告期
   * - revenue
     - 营业收入(元)
   * - revenue_yoy
     - 营业收入同比(%)
   * - net_profit
     - 净利润(元)
   * - net_profit_yoy
     - 净利润同比(%)
   * - gross_margin
     - 毛利率(%)
   * - roe
     - 净资产收益率(%)

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取利润表
    df = fs.get_income('600519.SH')
    print(df.head())
