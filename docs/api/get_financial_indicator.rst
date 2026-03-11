get_financial_indicator
=========================

获取财务指标数据。

函数签名
~~~~~~~~

.. code-block:: python

    def get_financial_indicator(
        code: str,
        ann_date: str = None,
    )

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
   * - eps
     - 每股收益(元)
   * - roe
     - 净资产收益率(%)
   * - gross_margin
     - 毛利率(%)
   * - netprofit_margin
     - 净利率(%)
   * - current_ratio
     - 流动比率
   * - quick_ratio
     - 速动比率
   * - debt_to_assets
     - 资产负债率(%)

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    df = fs.get_financial_indicator('600519.SH')
    print(df.head())

输出结果：

::

         fs_code  ann_date  report_date    eps    roe  gross_margin  netprofit_margin  current_ratio  quick_ratio  debt_to_assets
    0  600519.SH  20240830    20240630   52.18   25.63        52.18             31.25           1.82         1.45           28.5
    ...
