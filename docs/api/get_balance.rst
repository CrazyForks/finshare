get_balance
===========

获取资产负债表数据。

函数签名
~~~~~~~~

.. code-block:: python

    def get_balance(
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
   * - total_assets
     - 总资产(元)
   * - total_liab
     - 总负债(元)
   * - total_equity
     - 股东权益(元)
   * - current_assets
     - 流动资产(元)
   * - current_liab
     - 流动负债(元)

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    df = fs.get_balance('600519.SH')
    print(df.head())
