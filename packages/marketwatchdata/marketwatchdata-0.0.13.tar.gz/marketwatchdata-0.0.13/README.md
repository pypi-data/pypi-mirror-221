# MarketWatchData


[![PyPI](https://img.shields.io/pypi/v/marketwatchdata.svg)](https://pypi.org/project/marketwatchdata/)
[![Downloads](https://pepy.tech/badge/marketwatchdata)](https://pepy.tech/project/marketwatchdata)
[![Documentation Status](https://readthedocs.org/projects/MarketWatchData/badge/?version=latest)](https://MarketWatchData.readthedocs.io/?badge=latest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Actions Status](https://github.com/yacper/MarketWatchData/workflows/build/badge.svg)](https://github.com/yacper/MarketWatchData/actions)
[![MIT Licence](https://camo.githubusercontent.com/14a9abb7e83098f2949f26d2190e04fb1bd52c06/68747470733a2f2f626c61636b2e72656164746865646f63732e696f2f656e2f737461626c652f5f7374617469632f6c6963656e73652e737667)](https://github.com/akfamily/akshare/blob/master/LICENSE)

## Overview

[MarketWathData](https://github.com/yacper/marketwatchdata) retrieve datas from marketwatch.com.

- Documentation: [文档](https://marketwatchdata.readthedocs.io/)


## Installation

### General

```shell
pip install marketwatchdata --upgrade
```

### China

```shell
pip install marketwatchdata -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com  --upgrade
```
#### Test

```python
import marketwatchdata as mw

print(mw.__version__)
```

## Usage

### Data

Code

```python
import marketwatchdata as mw

df = mw.ohlc('STOCK/US/XNAS/AAPL', 'P1D', 'P1Y')
print(df)
```

Output

```
      日期          开盘   收盘    最高  ...  振幅   涨跌幅 涨跌额 换手率
0     2017-03-01   9.49   9.49   9.55  ...  0.84  0.11  0.01  0.21
1     2017-03-02   9.51   9.43   9.54  ...  1.26 -0.63 -0.06  0.24
2     2017-03-03   9.41   9.40   9.43  ...  0.74 -0.32 -0.03  0.20
3     2017-03-06   9.40   9.45   9.46  ...  0.74  0.53  0.05  0.24
4     2017-03-07   9.44   9.45   9.46  ...  0.63  0.00  0.00  0.17
          ...    ...    ...    ...  ...   ...   ...   ...   ...
1100  2021-09-01  17.48  17.88  17.92  ...  5.11  0.45  0.08  1.19
1101  2021-09-02  18.00  18.40  18.78  ...  5.48  2.91  0.52  1.25
1102  2021-09-03  18.50  18.04  18.50  ...  4.35 -1.96 -0.36  0.72
1103  2021-09-06  17.93  18.45  18.60  ...  4.55  2.27  0.41  0.78
1104  2021-09-07  18.60  19.24  19.56  ...  6.56  4.28  0.79  0.84
[1105 rows x 11 columns]
```

### Plot

Code

```python
import marketwatchdata as mw
import mplfinance as mpf  # Please install mplfinance as follows: pip install mplfinance

df = mw.ohlc('STOCK/US/XNAS/AAPL', 'P1D', 'P1Y')
mpf.plot(df, type='candle', mav=(3, 6, 9), volume=True, show_nontrading=False)
```

Output

![](https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/akshare/readme/home/AAPL_candle.png)

## Acknowledgement

Thanks for the data provided by [marketwatch](http://www.marketwatch.com/);