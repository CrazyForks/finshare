get_future_kline
=================

获取期货历史K线数据。

函数签名
~~~~~~~~

.. code-block:: python

    def get_future_kline(
        code: str,
        start_date: str = None,
        end_date: str = None,
        adjustment: str = "none",
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
     - 期货合约代码，如 ``IF2409``、``CU0``、``AU2409``
   * - start_date
     - str
     - 开始日期，格式 ``YYYY-MM-DD``
   * - end_date
     - str
     - 结束日期，格式 ``YYYY-MM-DD``
   * - adjustment
     - str
     - 复权类型（期货不支持，默认none）

返回值
~~~~~~

返回 ``List[HistoricalData]``，每个元素包含以下属性：

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 说明
   * - code
     - str
     - 期货合约代码
   * - trade_date
     - date
     - 交易日期
   * - open_price
     - float
     - 开盘价
   * - high_price
     - float
     - 最高价
   * - low_price
     - float
     - 最低价
   * - close_price
     - float
     - 收盘价
   * - volume
     - float
     - 成交量(手)

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取股指期货K线
    data = fs.get_future_kline('IF2409', '2024-01-01', '2024-07-17')

    for item in data:
        print(f"{item.trade_date}: 开盘={item.open_price}, 收盘={item.close_price}")

输出结果：

::

    2024-01-02: 开盘=3421.0, 收盘=3450.0
    2024-01-03: 开盘=3450.0, 收盘=3480.0
    ...

支持的交易所和品种
~~~~~~~~~~~~~~~~

**CFFEX（中金所）**：IF、IH、IC

**SHFE（上期所）**：CU、AL、AU、AG、SC 等

**DCE（大商所）**：M、Y、P、J、I、RB 等

**CZCE（郑商所）**：SR、CF、TA、MA 等

连续合约说明
~~~~~~~~~~~~

- ``IF0`` - 沪深300当月连续
- ``CU0`` - 沪铜当月连续
- ``AU0`` - 沪金当月连续
