#Step 1:pip install fastapi & Also install fastapi on your computer to run it

#Step 2:Importing FastAPI class from fastapi module
from fastapi import FastAPI,Depends  
from fastapi.middleware.cors import CORSMiddleware

from models import Product
import database_model
from database import session,engine
from sqlalchemy.orm import Session  #Importing Session from sqlalchemy.orm (Db purpose)
#Step 3: Creating an Object of FASTAPI
app = FastAPI() 
origins=[
    "http://localhost:3000",  #ReactJS frontend URL
    "http://127.0.0.1:3000" #ReactJS frontend URL
] 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, #To read data from ReactJS frontend
    allow_credentials=True,
    allow_methods=["*"], #To submit something to the server
    allow_headers=["*"], #To read headers
    
)



database_model.Base.metadata.create_all(bind=engine)
#Step 4:pip install "uvicorn[standard]" to run the server

#Step 5:Start the server using the command
#uvicorn main:app --reload


# Use keyword arguments (key=value)
products = [
    Product(id=1, name="Laptop", price=999.99, quantity=10, description="A high-performance laptop"),
    Product(id=2, name="Smartphone", price=499.99, quantity=25, description="A latest model smartphone"),
    Product(id=3, name="Headphones", price=199.99, quantity=15, description="Noise-cancelling headphones")
] 

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db=session()  #Creating the session
    count=db.query(database_model.Product).count()#Counting the number of rows in the table
    if count==0:
        for prod in products:
            db.add(database_model.Product(**prod.model_dump()))#Adding the products to the database
            db.commit()#Committing the changes
    db.close()

init_db()




@app.get("/")  #/ For accessing the home page 
def greet():
    return "Welcome to my page"

'''Product(1, "Laptop", 999.99, 10, "A high-performance laptop"),
    Product(2, "Smartphone", 499.99, 25, "A latest model smartphone"),
    Product(3, "Headphones", 199.99, 15, "Noise-cancelling headphones")
    '''
           

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    db_products=db.query(database_model.Product).all()
    return db_products
   # return products

'''
@app.get("/product/")   #Different endpoint 
def get_product_by_id():
    return products[0]'''   #Returning single product

'''
#Incorrect logic
@app.get("/product/{id}") #Dynamic path parameter (use the same in the function {id})
def get_product_by_id(id:int):  
    return products[id-1]  #Retruning product by id
'''
#Correct Logic
@app.get("/products/{id}")
def get_product_by_id(id:int, db: Session = Depends(get_db)):
    #for i in products:
    db_product=db.query(database_model.Product).filter(database_model.Product.id==id).first()
       # if i.id==id:
        #    return i #Returning the product by id
    if db_product:
        return db_product
    return "product not found"

#Adding the product
@app.post("/products")
def add_product(prod:Product,db: Session = Depends(get_db)):
    db.add(database_model.Product(**prod.model_dump())) #Adding the product to the database
    db.commit()
    #products.append(prod)
    return prod

#Updating the product
@app.put("/products/{id}")
def update_product(id:int , prod:Product,db: Session = Depends(get_db)):
    '''for i in products:
        if i.id==id:
            i=prod'''
    db_product=db.query(database_model.Product).filter(database_model.Product.id==id).first()
    print(db_product)
    if db_product:
            db_product.name=prod.name
            db_product.price=prod.price
            db_product.quantity=prod.quantity
            db_product.description=prod.description
            db.commit()
            return "Product added Sucessfully" 
    else:
        return "Product not found"

#deleting the product
@app.delete("/products/{id}")
def delete_product(id:int,db:Session=Depends(get_db)):
    db_prodyct=db.query(database_model.Product).filter(database_model.Product.id==id).first()
    if db_prodyct:
        db.delete(db_prodyct)
        db.commit()
        return "product deleted"
    else:
        return "Product not found"
    '''for i in products:
        if i.id==id:
            del i'''
            
    
           