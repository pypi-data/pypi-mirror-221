from loguru import logger

class shioaji_position_management:
    __slots__ = ["api", "stock", "future", "option", "ordering", "acc", "logger"]

    def __init__(self, api, acc):
        self.api = api
        assert len(api.list_accounts()) > 0
        self.acc = api.list_accounts()[0] 
        for account in api.list_accounts():
            if account["broker_id"] + "-" + account["account_id"] == acc:
                self.acc = account
        api.set_order_callback(self.cb)

        self.stock = []
        self.future = []
        self.option = []
        self.ordering = []

        logger.add(f"./shioaji_position_management_{datetime.datetime.today().strftime('%Y-%m-%d')}.log", encoding="utf-8", enqueue=True)
        logger.info(f"-----Seperate Line-----")
        logger.info(f"shioaji_position_management Start at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info(f"Start monitoring {self.acc}")

    def cb(self, stat, msg):
        logger.info(f"Callback status {stat}")
        logger.info(f"msg {msg}")
        if "DEAL" in stat:
            self.future.append(msg)

    def close_all_position(self):
        for p in self.future:
            self.order(self, api.Contracts.Futures.MXF[p.code], "S" if p.action == "Buy" else "B", p.price, p.quantity, "MKT", "IOC", "Auto")

    def order(self, obj, action, price, qty, price_type, order_type, oc_type):
        assert action in ["B", "Buy", "BUY", "L", "Long", "LONG", "S", "Sell", "SELL", "Short", "SHORT"]
        if action in ["B", "Buy", "BUY", "L", "Long", "LONG"]:
            action = sj.constant.Action.Buy
        elif action in ["S", "Sell", "SELL", "Short", "SHORT"]:
            action = sj.constant.Action.Sell

        assert price_type in ["LMT", "MKT", "MKP"]
        if price_type == "LMT":
            price_type = sj.constant.FuturesPriceType.LMT
        elif price_type == "MKT":
            price_type = sj.constant.FuturesPriceType.MKT
        elif price_type == "MKP":
            price_type = sj.constant.FuturesPriceType.MKP

        assert order_type in ["ROD", "IOC", "FOK"]
        if order_type == "ROD":
            order_type = sj.constant.OrderType.ROD
        elif order_type == "IOC":
            order_type = sj.constant.OrderType.IOC
        elif order_type == "FOK":
            order_type = sj.constant.OrderType.FOK

        assert oc_type in ["Auto", "New", "Cover", "DayTrade"]
        if oc_type == "Auto":
            oc_type = sj.constant.FuturesOCType.Auto
        elif oc_type == "New":
            oc_type = sj.constant.FuturesOCType.New
        elif oc_type == "Cover":
            oc_type = sj.constant.FuturesOCType.Cover
        elif oc_type == "DayTrade":
            oc_type = sj.constant.FuturesOCType.DayTrade

        order = api.Order(
                action = action,
                price = price,
                quantity = qty,
                price_type = price_type,
                order_type = order_type, 
                octype = oc_type,
                account = self.acc
            )
        trade = api.place_order(obj, order)