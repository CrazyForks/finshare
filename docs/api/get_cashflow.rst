get_cashflow
============

获取现金流量表数据。

函数签名
~~~~~~~~

.. code-block:: python

    def get_cashflow(
        code: str,
        start_date: str = None,
        end_date: str = None,
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
   * - operate_cashflow
     - 经营活动现金流(元)
   * - invest_cashflow
     - 投资活动现金流(元)
   * - finance_cashflow
     - 筹资活动现金流(元)

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    df = fs.get_cashflow('600519.SH')
    print(df.head())
