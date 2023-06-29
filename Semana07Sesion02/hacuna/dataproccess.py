from conexion import Conexion

class Orders:
    def __init__(self, orderId, orderDate, shipDate, shipMode, custumer, product, sales, quantity, discount, profit): 
        self.orderId = orderId
        self.orderDate = orderDate
        self.shipDate = shipDate
        self.shipMode = shipMode
        self.custumer = custumer
        self.product = product
        self.sales = sales
        self.quantity = quantity
        self.discount = discount
        self.profit = profit

class Custumers:
    def __init__(self, idCustumer, name, segment, country, city, state, postalCode, region):
        self.idCustumer = idCustumer
        self.name = name
        self.segment = segment
        self.country = country
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.region = region