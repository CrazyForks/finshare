"""
示例 8: 港股数据获取

演示如何获取港股数据：实时行情、历史K线。
"""

import finshare as fs


def main():
    """运行港股数据获取示例"""

    fs.logger.info("=" * 60)
    fs.logger.info("finshare 港股数据获取示例")
    fs.logger.info("=" * 60)

    # 港股代码示例
    hk_codes = [
        "00700.HK",  # 腾讯控股
        "09988.HK",  # 阿里巴巴-SW
        "09999.HK",  # 中国平安
        "00981.HK",  # 中芯国际
    ]

    # 1. 批量获取港股实时快照
    fs.logger.info("\n=== 获取港股实时快照 ===")
    try:
        results = fs.get_batch_snapshots(hk_codes)
        fs.logger.info(f"成功获取 {len(results)} 只港股的快照")

        fs.logger.info("\n港股实时行情:")
        fs.logger.info("-" * 60)
        fs.logger.info(f"{'代码':<12} {'名称':<15} {'最新价':<10} {'涨跌幅':<10}")
        fs.logger.info("-" * 60)

        for code, snapshot in results.items():
            change_pct = snapshot.change_pct if snapshot.change_pct else 0
            fs.logger.info(
                f"{code:<12} {'港股':<15} {snapshot.last_price:<10.2f} {change_pct:>+9.2f}%"
            )
    except Exception as e:
        fs.logger.error(f"获取港股快照失败: {e}")

    # 2. 获取单只港股历史K线
    fs.logger.info("\n=== 获取港股历史K线 ===")
    code = "00700.HK"  # 腾讯控股

    try:
        df = fs.get_historical_data(
            code=code,
            start="2026-01-01",
            end="2026-01-31"
        )

        if df is not None and len(df) > 0:
            fs.logger.info(f"✓ 成功获取 {code} {len(df)} 条日K线数据")

            # 计算涨跌幅
            first_price = df.iloc[0]['close_price']
            last_price = df.iloc[-1]['close_price']
            change = (last_price - first_price) / first_price * 100

            fs.logger.info(f"  日期范围: {df.iloc[0]['trade_date']} 至 {df.iloc[-1]['trade_date']}")
            fs.logger.info(f"  起始价: {first_price:.2f} 港元")
            fs.logger.info(f"  结束价: {last_price:.2f} 港元")
            fs.logger.info(f"  月涨跌幅: {change:+.2f}%")

            # 统计
            fs.logger.info(f"  最高价: {df['high_price'].max():.2f} 港元")
            fs.logger.info(f"  最低价: {df['low_price'].min():.2f} 港元")
            fs.logger.info(f"  成交量: {df['volume'].sum():,.0f} 股")
        else:
            fs.logger.warning(f"未获取到 {code} 的历史数据")

    except Exception as e:
        fs.logger.error(f"获取港股历史数据失败: {e}")

    # 3. 提示
    fs.logger.info("\n" + "=" * 60)
    fs.logger.info("💡 提示:")
    fs.logger.info("  - 港股代码格式: 00700.HK, 09988.HK")
    fs.logger.info("  - 港股价格单位: 港元 (HKD)")
    fs.logger.info("  - 交易时间: 9:30-12:00, 13:00-16:00")
    fs.logger.info("  - T+0 交易制度")


if __name__ == "__main__":
    main()
