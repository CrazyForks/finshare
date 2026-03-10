# 分享一个完全免费的中国A股数据获取库

## 简介

大家好！今天想分享一个我开源的金融数据获取库 **finshare**，完全免费，无需 API Key。

GitHub: https://github.com/finvfamily/finshare
Discord: https://discord.gg/XT5f8ZGB

## 特性

- **完全免费**：无需 API Key，无调用次数限制
- **多数据源**：东方财富、腾讯、新浪、通达信、BaoStock
- **自动故障切换**：数据源失败时自动切换备用源
- **高性能**：支持异步批量获取
- **内置缓存**：减少重复请求

## 安装

```bash
pip install finshare
```

## 快速开始

```python
import finshare as fs

# 获取历史K线数据
df = fs.get_historical_data('000001.SZ', start='2024-01-01', end='2024-12-31', adjust='qfq')

# 获取实时快照
snapshot = fs.get_snapshot_data('000001.SZ')

# 批量获取快照
snapshots = fs.get_batch_snapshots(['000001.SZ', '600519.SH'])

# 财务数据
df = fs.get_income('000001.SZ')  # 利润表
df = fs.get_balance('000001.SZ')  # 资产负债表

# 特色数据
df = fs.get_money_flow('000001.SZ')  # 资金流向
df = fs.get_lhb()                     # 龙虎榜
df = fs.get_margin('000001.SZ')       # 融资融券
```

## 数据字段

```
K线数据: code, trade_date, open_price, high_price, low_price, close_price, volume, amount
快照数据: code, last_price, change, change_pct, volume, amount, turnover_rate
```

## 征集想法

我正在开发 **finquant** 开源量化交易框架，想收集大家的想法：

- 你想要什么样的交易系统？
- 需要哪些功能？（回测、实盘、因子库、风控等）
- 有什么好的策略思路？

欢迎加入 Discord 社群一起讨论：**https://discord.gg/XT5f8ZGB**

也欢迎 Star 和 PR！

---

原帖地址: https://github.com/finvfamily/finshare
