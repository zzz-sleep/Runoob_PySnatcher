# Python 实现秒表功能

## 题目描述
以下实例使用 time 模块来实现秒表功能：

## 实例
### 代码
```python
importtimeprint('按下回车开始计时，按下 Ctrl + C 停止计时。')whileTrue:input("")# 等待用户按下回车开始计时start_time=time.time()# 记录开始时间print('开始计时...')try:whileTrue:elapsed_time=round(time.time()-start_time,0)# 计算经过的时间print(f'计时: {elapsed_time} 秒',end="\r")# 覆盖上次输出time.sleep(1)exceptKeyboardInterrupt:# 捕捉 Ctrl + C 中断信号end_time=time.time()# 记录结束时间total_time=round(end_time-start_time,2)print(f'\n计时结束，总共时间为: {total_time} 秒')break
```
### 输出结果
```
按下回车开始计时，按下 Ctrl + C 停止计时。

开始计时...
^C时: 3.0 秒
计时结束，总共时间为: 3.77 秒
```
源链接: [https://www.runoob.com/python3/python-simplestopwatch.html](https://www.runoob.com/python3/python-simplestopwatch.html)