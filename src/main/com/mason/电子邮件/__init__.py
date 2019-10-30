#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 电子邮件
# MUA：Mail User Agent——邮件用户代理
# MTA：Mail Transfer Agent——邮件传输代理
# MDA：Mail Delivery Agent——邮件投递代理
# 发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人
# 发邮件时，MUA和MTA使用的协议就是SMTP：Simple Mail Transfer Protocol
# 收邮件时，MUA和MDA使用的协议有两种：POP：Post Office Protocol，目前版本是3，俗称POP3；
# IMAP：Internet Message Access Protocol，目前版本是4，优点是不但能取邮件，
# 还可以直接操作MDA上存储的邮件，比如从收件箱移到垃圾箱，等等
