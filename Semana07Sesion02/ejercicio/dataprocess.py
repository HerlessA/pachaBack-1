from conexion import Conexion


class Orders:
    def __init__(
        self,
        orderId,
        orderDate,
        shipDate,
        shipMode,
        customer,
        product,
        sales,
        quantity,
        discount,
        profit,
    ):
        self.orderId = orderId
        self.orderDate = orderDate
        self.shipDate = shipDate
        self.shipMode = shipMode
        self.customer = customer
        self.product = product
        self.customer = customer
        self.sales = sales
        self.quantity = quantity
        self.discount = discount
        self.profit = profit


class Customers:
    def __init__(
        self, idCustomer, name, segment, country, city, state, postalCode, region
    ):
        self.idCustomer = idCustomer
        self.name = name
        self.segment = segment
        self.country = country
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.region = region


class Products:
    def __init__(self, idProduct, category, subcategory, name):
        self.idProduct = idProduct
        self.category = category
        self.subcategory = subcategory
        self.name = name


products = list()
product1 = Products(4747, "Office", "Enceres", "Perforadora")
product2 = Products(4748, "Office", "Enceres", "Lápices")
product3 = Products(4749, "Office", "Enceres", "Borradores")

products.append(product1.__dict__)
products.append(product2.__dict__)
products.append(product3.__dict__)

customer = Customers(
    988,
    "Mari R",
    "industrial",
    "Perú",
    "Lima",
    "Santa Anita",
    "14587",
    "South",
)
orden = Orders(
    123,
    "2023-01-01",
    "2023-02-01",
    "Standart",
    customer=customer.__dict__,
    product=products,
    sales=123,
    quantity=99,
    discount=45,
    profit=99,
)

print(f"{orden.__dict__}")

conn = Conexion("mongodb://localhost:27017", "Ventas")
conn.insertar_registro("Ordenes", orden.__dict__)
