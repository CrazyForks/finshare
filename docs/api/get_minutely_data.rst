get_minutely_data
=================

获取股票的分钟K线数据。

函数签名
~~~~~~~~

.. code-block:: python

    def get_minutely_data(
        code: str,
        start: str = None,
        end: str = None,
        freq: int = 5,
        adjust: str = None,
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
     - 股票代码
   * - start
     - str
     - 开始时间，格式 ``YYYY-MM-DD`` 或 ``YYYY-MM-DD HH:MM:SS``
   * - end
     - str
     - 结束时间，格式 ``YYYY-MM-DD`` 或 ``YYYY-MM-DD HH:MM:SS``
   * - freq
     - int
     - 频率：``1``、``5``、``15``、``30``、``60`` 分钟
   * - adjust
     - str
     - 复权类型：``qfq``、``hfq``、``None``

返回值
~~~~~~

返回 :class:`pandas.DataFrame`。

使用示例
~~~~~~~~

.. code-block:: python

    import finshare as fs

    # 获取5分钟K线（当日）
    df = fs.get_minutely_data(
        code='000001.SZ',
        freq=5
    )

    # 获取指定时间范围的15分钟K线
    df = fs.get_minutely_data(
        code='000001.SZ',
        start='2024-01-15 09:30:00',
        end='2024-01-15 15:00:00',
        freq=15
    )
