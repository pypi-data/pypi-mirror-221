from services.FoxPayService import FoxPayService

#创建订单
orderCreateParam = {
    'subject' : 'test2334',
    'order_no' : 'test2334',
    'amount' : '1.2',
    'notify_url' : '',
    'redirect_url' : '',
    'time_out' : 1000,
    'locale' : 'zh-CN',
    'remark' : 'test'
}

#查询订单
queryParam = {
    'trade_no' : 'AP2023071310442022925526694',
    'order_no' : ''
}

#关闭订单
closeOrderParam = {
    'trade_no' : '',
    'order_no' : 'test23'
}

#提现凭证获取
transParamPrepareParam = {
    'order_no' : 'test233',
    'amount' : '1.2',
    'to_address' : '0x3810fe9f57f2f792a1522088c1a62d14cd5b86c4',
    'notify_url' : '',
    'remark' : ''
}

#提现确认
transParam = {
    'trans_token' : '8f230fa553b9434f9d19848d1e7ac42dwpg9ym',
}

#提现记录查询
getTransParam = {
    'trade_no' : '',
    'order_no' : 'test233'
}

service = FoxPayService()

#创建订单
# data = service.orderCreate(orderCreateParam)

#查询订单
data = service.orderQuery(queryParam)

#关闭订单
# data = service.closeOrder(closeOrderParam)

#查询资产
# data = service.getBalance()

#提现凭证获取
# data = service.transPrepare(transParamPrepareParam)

#提现确认
# data = service.trans(transParam)

#提现记录查询
# data = service.getTrans(getTransParam)

print(data)