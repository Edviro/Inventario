from .connection import DatabaseConnection

class BaseModel:
    """Clase base para todos los modelos"""
    def __init__(self):
        self.db = DatabaseConnection()

class Categoria(BaseModel):
    def __init__(self, id=None, nombre=None, descripcion=None):
        super().__init__()
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
    
    def save(self):
        """Guarda o actualiza una categoría en la base de datos"""
        if self.id is None:
            # Insertar nueva categoría
            query = "INSERT INTO Categoria (NombreCat, Descripcion) VALUES (?, ?)"
            cursor = self.db.execute_query(query, (self.nombre, self.descripcion))
            self.id = cursor.lastrowid
        else:
            # Actualizar categoría existente
            query = "UPDATE Categoria SET NombreCat = ?, Descripcion = ? WHERE idCategoria = ?"
            self.db.execute_query(query, (self.nombre, self.descripcion, self.id))
        return self.id
    
    def delete(self):
        """Elimina una categoría de la base de datos"""
        if self.id:
            query = "DELETE FROM Categoria WHERE idCategoria = ?"
            self.db.execute_query(query, (self.id,))
            return True
        return False
    
    @classmethod
    def get_by_id(cls, id):
        """Obtiene una categoría por su ID"""
        db = DatabaseConnection()
        query = "SELECT * FROM Categoria WHERE idCategoria = ?"
        row = db.fetch_one(query, (id,))
        if row:
            return cls(id=row['idCategoria'], nombre=row['NombreCat'], descripcion=row['Descripcion'])
        return None
    
    @classmethod
    def get_all(cls):
        """Obtiene todas las categorías"""
        db = DatabaseConnection()
        query = "SELECT * FROM Categoria ORDER BY NombreCat"
        rows = db.fetch_all(query)
        return [cls(id=row['idCategoria'], nombre=row['NombreCat'], descripcion=row['Descripcion']) for row in rows]

class Producto(BaseModel):
    def __init__(self, id=None, nombre=None, precio=None, stock=None, id_categoria=None):
        super().__init__()
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.id_categoria = id_categoria
    
    def save(self):
        """Guarda o actualiza un producto en la base de datos"""
        if self.id is None:
            # Insertar nuevo producto
            query = "INSERT INTO Producto (NombrePro, Precio, Stock, idCategoria) VALUES (?, ?, ?, ?)"
            cursor = self.db.execute_query(query, (self.nombre, self.precio, self.stock, self.id_categoria))
            self.id = cursor.lastrowid
        else:
            # Actualizar producto existente
            query = "UPDATE Producto SET NombrePro = ?, Precio = ?, Stock = ?, idCategoria = ? WHERE idProducto = ?"
            self.db.execute_query(query, (self.nombre, self.precio, self.stock, self.id_categoria, self.id))
        return self.id
    
    def delete(self):
        """Elimina un producto de la base de datos"""
        if self.id:
            query = "DELETE FROM Producto WHERE idProducto = ?"
            self.db.execute_query(query, (self.id,))
            return True
        return False
    
    def update_stock(self, cantidad):
        """Actualiza el stock de un producto"""
        if self.id:
            self.stock += cantidad
            query = "UPDATE Producto SET Stock = ? WHERE idProducto = ?"
            self.db.execute_query(query, (self.stock, self.id))
            return True
        return False
    
    @classmethod
    def get_by_id(cls, id):
        """Obtiene un producto por su ID"""
        db = DatabaseConnection()
        query = "SELECT * FROM Producto WHERE idProducto = ?"
        row = db.fetch_one(query, (id,))
        if row:
            return cls(id=row['idProducto'], nombre=row['NombrePro'], precio=row['Precio'], 
                       stock=row['Stock'], id_categoria=row['idCategoria'])
        return None
    
    @classmethod
    def get_all(cls):
        """Obtiene todos los productos"""
        db = DatabaseConnection()
        query = "SELECT * FROM Producto ORDER BY NombrePro"
        rows = db.fetch_all(query)
        return [cls(id=row['idProducto'], nombre=row['NombrePro'], precio=row['Precio'], 
                   stock=row['Stock'], id_categoria=row['idCategoria']) for row in rows]
    
    @classmethod
    def get_by_categoria(cls, id_categoria):
        """Obtiene productos por categoría"""
        db = DatabaseConnection()
        query = "SELECT * FROM Producto WHERE idCategoria = ? ORDER BY NombrePro"
        rows = db.fetch_all(query, (id_categoria,))
        return [cls(id=row['idProducto'], nombre=row['NombrePro'], precio=row['Precio'], 
                   stock=row['Stock'], id_categoria=row['idCategoria']) for row in rows]

# Implementación similar para Cliente, Empleado, Venta y DetalleVenta
# Estos modelos seguirán la misma estructura que los anteriores

class Cliente(BaseModel):
    def __init__(self, id=None, nombre=None, telefono=None, dni=None, direccion=None):
        super().__init__()
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.dni = dni
        self.direccion = direccion
    
    def save(self):
        if self.id is None:
            query = "INSERT INTO Cliente (NombreCli, TelefonoCli, Dni, DireccionClie) VALUES (?, ?, ?, ?)"
            cursor = self.db.execute_query(query, (self.nombre, self.telefono, self.dni, self.direccion))
            self.id = cursor.lastrowid
        else:
            query = "UPDATE Cliente SET NombreCli = ?, TelefonoCli = ?, Dni = ?, DireccionClie = ? WHERE idCliente = ?"
            self.db.execute_query(query, (self.nombre, self.telefono, self.dni, self.direccion, self.id))
        return self.id
    
    # Métodos adicionales similares a los anteriores...

class Empleado(BaseModel):
    def __init__(self, id=None, nombre=None, correo=None, telefono=None, direccion=None):
        super().__init__()
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
    
    def save(self):
        if self.id is None:
            query = "INSERT INTO Empleado (NombreEmp, CorreoEmp, Telefono, DireccionEmp) VALUES (?, ?, ?, ?)"
            cursor = self.db.execute_query(query, (self.nombre, self.correo, self.telefono, self.direccion))
            self.id = cursor.lastrowid
        else:
            query = "UPDATE Empleado SET NombreEmp = ?, CorreoEmp = ?, Telefono = ?, DireccionEmp = ? WHERE idEmpleado = ?"
            self.db.execute_query(query, (self.nombre, self.correo, self.telefono, self.direccion, self.id))
        return self.id
    
    # Métodos adicionales similares a los anteriores...