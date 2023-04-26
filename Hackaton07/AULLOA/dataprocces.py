from conexion import Conexion

class Orders:
    def __init__(self,orderId,orderDate, shipDate, shipMode, custumer, product, sales, quantity, discount, profit):
        self.orderId = orderId
        self.orderDate =orderDate
        self.shipDate = shipDate
        self.shipMode = shipMode
        self.custumer = custumer
        self.product = product
        self.sales = sales
        self.quantity = quantity
        self.discount = discount
        self.profit = profit

class Custumers:
    def __init__(self,idCustumer, name, segment, country, city, state, postalCode, region ):
        self.idCustumer = idCustumer
        self.name = name
        self.segment = segment
        self.country = country
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.region = region

class Products:
    def __init__(self, idProduct, category, subCategory, name):
        self.idProduct =idProduct
        self.category = category
        self.subCategory = subCategory
        self.name = name

products = list()
product1=Products(4747,"Office","Enceres","Perforadora")
product2=Products(4748,"Office","Enceres","Lapices")
product3=Products(4749,"Office","Enceres","Hojas")

products.append(product1.__dict__)
products.append(product2.__dict__)
products.append(product3.__dict__)

custumer= Custumers(988,"Roberto Pineda","Industrial","Ecuador","Quito", "Pichincha","17098","South")
orden = Orders(123, '2023-01-01','2023-02-01',"Standart",custumer=custumer.__dict__,product= products,sales=123,quantity=99,discount=45,profit=99)

print(f"{orden.__dict__}")

conn = Conexion("mongodb://localhost:27017", "Ventas")
conn.insertar_registro("Ordenes",orden.__dict__)