#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# datetime

# 获取当前日期和时间
import re
from datetime import datetime, timedelta, timezone

print("\n获取当前日期和时间")
now = datetime.now()
print("now:", now)

# 获取指定日期时间
print("\n获取指定日期时间")
target_datetime = datetime(2019, 10, 1, 8)
print(target_datetime)

# datetime转换为timestamp
# 返回结果单位为秒
print("\ndatetime转换为timestamp")
timestamp = target_datetime.timestamp()
print(timestamp)

# timestamp转换为datetime
# datetime是有时区的
print("\ntimestamp转换为datetime")
target_datetime = datetime.fromtimestamp(timestamp)
print(target_datetime)

utc_target_datetime = datetime.utcfromtimestamp(timestamp)
print(utc_target_datetime)

# str转datetime
print("\nstr转datetime")
date_str = "2019-10-10 10:10:10"
target_datetime = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(target_datetime)

# datetime转str
print("\ndatetime转str")
now_time_str = now.strftime(" %a, %b %d %H:%M")
print(now_time_str)

# datetime加减
print("\ndatetime加减")
change_now = now + timedelta(hours=5)
print("now + 5 hours:", change_now)
change_now = now + timedelta(hours=-5)
print("now - 5 hours:", change_now)
change_now = now + timedelta(days=1, hours=5)
print("now + 1 days 5 hours:", change_now)

# 本地时间转换为UTC时间
print("\n本地时间转换为UTC时间")
tz_utc_8 = timezone(timedelta(hours=8))
zone_time = now.replace(tzinfo=tz_utc_8)
print(zone_time)

# 时区转换
print("\n时区转换")
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_datetime = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_datetime)
# astimezone()将转换时区为北京时间:
beijing_time = utc_datetime.astimezone(timezone(timedelta(hours=8)))
print(beijing_time)
# astimezone()将bj_dt转换时区为东京时间:
tokyo_time = beijing_time.astimezone(timezone(timedelta(hours=9)))
print(tokyo_time)

# 练习
# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，
# 以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
print("\n练习")

tz_re = re.compile(r"^(UTC|utc)[\+,-]\d+:00$")
tz_hours_re = re.compile(r"[\+,-][0-9]+")


def to_timestamp(dt_str, tz_str):
    try:
        # 先用正则表达式验证dt_str和tz_str的合法性
        tz = tz_re.match(tz_str)
        if not tz:
            raise ValueError("tz")
        tz_hours = tz_hours_re.findall(tz_str)
        if not tz_hours or len(tz_hours) < 1:
            raise ValueError("tz_hours:%s" % tz_hours)
        # 将dt_str转为datetime并强制设置时区
        dt_time = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
        hours = int(tz_hours[0])
        return dt_time.replace(tzinfo=timezone(timedelta(hours=hours)))
        # datetime转timestamp
    except ValueError as err:
        print("输入的 日期或时区格式错误: (%s, %s, %s)" % (dt_str, tz_str, err))


if __name__ == '__main__':
    date_str = now.strftime("%Y-%m-%d %H:%M:%S")
    result = to_timestamp(date_str, "UTC-1:00")
    print(result)
