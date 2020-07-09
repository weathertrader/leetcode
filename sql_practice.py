
# have done all easy and medium 

# questions
# https://docs.google.com/document/d/1Zr1NUSMARY99XpqLwySaRkIz9yiYhvbxZgBgCCD430w/edit#
# answers
# https://docs.google.com/document/d/1clrrkrwFUvm8LyZ4Qvxjrb3FQG03C1WuViR1xpdYehY/edit#


11. Show all Customers who have never placed an order with Employee 4.(16 rows)



SELECT 
  customers.customerid
FROM customers
LEFT JOIN orders ON orders.customerid = customers.customerid
WHERE orders.employeeid != 4
UNION
SELECT DISTINCT customerid
FROM orders
WHERE customerid NOT IN 
(SELECT DISTINCT customerid FROM orders WHERE employeeid=4);

GROUP BY orders.customerid
ORDER BY customers.customerid;

SELECT
  orderdetails.orderid,
  orderdetails.quantity,
  products.productname,
  orders.employeeid,
  employees.lastname
FROM orders
JOIN orderdetails ON orders.orderid = orderdetails.orderid
JOIN products ON orderdetails.productid = products.productid
JOIN employees ON orders.employeeid = employees.employeeid
ORDER BY orderid DESC
LIMIT 5;

ecommerce=> \d products
                                           Table "public.products"
     Column      |         Type          | Collation | Nullable |                   Default                   
-----------------+-----------------------+-----------+----------+---------------------------------------------
 productid       | integer               |           | not null | nextval('products_productid_seq'::regclass)
 productname     | character varying(40) |           | not null | 
 supplierid      | integer               |           |          | 
 categoryid      | integer               |           |          | 
 quantityperunit | character varying(20) |           |          | 
 unitprice       | money                 |           |          | 
 unitsinstock    | smallint              |           |          | 
 unitsonorder    | smallint              |           |          | 
 reorderlevel    | smallint              |           |          | 
 discontinued    | boolean               |           | not null | 





ecommerce=> \d orders
                                             Table "public.orders"
     Column     |            Type             | Collation | Nullable |                 Default                 
----------------+-----------------------------+-----------+----------+-----------------------------------------
 orderid        | integer                     |           | not null | nextval('orders_orderid_seq'::regclass)
 customerid     | character(5)                |           | not null | 
 employeeid     | integer                     |           |          | 
 orderdate      | timestamp without time zone |           |          | 
 requireddate   | timestamp without time zone |           |          | 
 shippeddate    | timestamp without time zone |           |          | 
 shipvia        | integer                     |           |          | 
 freight        | money                       |           |          | 
 shipname       | character varying(40)       |           |          | 
 shipaddress    | character varying(60)       |           |          | 
 shipcity       | character varying(15)       |           |          | 
 shipregion     | character varying(15)       |           |          | 
 shippostalcode | character varying(10)       |           |          | 
 shipcountry    | character varying(15)       |           |          | 



ecommerce=> \d customers
                       Table "public.customers"
    Column    |         Type          | Collation | Nullable | Default 
--------------+-----------------------+-----------+----------+---------
 customerid   | character(5)          |           | not null | 
 companyname  | character varying(40) |           | not null | 
 contactname  | character varying(30) |           |          | 
 contacttitle | character varying(30) |           |          | 
 address      | character varying(60) |           |          | 
 city         | character varying(15) |           |          | 
 region       | character varying(15) |           |          | 
 postalcode   | character varying(10) |           |          | 
 country      | character varying(15) |           |          | 
 phone        | character varying(24) |           |          | 
 fax          | character varying(24) |           |          | 




SELECT customerid,
  CASE 
    WHEN region is NULL THEN 0
    ELSE 1
  END AS "hasregion",
  region
FROM customers
ORDER BY region, "hasregion";




categories                | table    | postgres
categories_categoryid_seq | sequence | postgres
customergroupthresholds   | table    | postgres
customers                 | table    | postgres
employees                 | table    | postgres
employees_employeeid_seq  | sequence | postgres
orderdetails              | table    | postgres
orders                    | table    | postgres
orders_orderid_seq        | sequence | postgres
products                  | table    | postgres
products_productid_seq    | sequence | postgres
shippers                  | table    | postgres
shippers_shipperid_seq    | sequence | postgres
suppliers                 | table    | postgres
test                      | table    | sqlpractice_edit

ecommerce=> \d categories
                                          Table "public.categories"
    Column    |         Type          | Collation | Nullable |                    Default                     
--------------+-----------------------+-----------+----------+------------------------------------------------
 categoryid   | integer               |           | not null | nextval('categories_categoryid_seq'::regclass)
 categoryname | character varying(15) |           | not null | 
 description  | text                  |           |          | 



SELECT
  shipcountry, AVG(freight::numeric) as avgfreight
FROM orders
WHERE orderdate BETWEEN '2015-01-01' AND '2016-01-01'
GROUP BY shipcountry
ORDER BY avgfreight DESC
LIMIT 3;




 
FROM customers
CASE
  region IS NULL hasregion=0 
CASE 
  region IS NOT NULL  hasregion=1
WHERE region IS NOT NULL
ORDER BY region;


SELECT customerid,region 
FROM customers
WHERE region IS NOT NULL
ORDER BY region;



WHERE NOT NULL



WHERE (unitsonorder+unitsinstock) <= reorderlevel
AND discontinued IS FALSE
ORDER BY productid;




SELECT productid, unitsinstock, discontinued
FROM products
WHERE (unitsonorder+unitsinstock) <= reorderlevel
AND discontinued IS FALSE
ORDER BY productid;

AND discontinued='f'

SELECT city,country, COUNT(*) AS 'numofcustomers'
FROM
  customers
GROUP BY city,county
ORDER BY 'numofcustomers' DESC;


SELECT
  categories.categoryname,
  COUNT(products.productid) AS totalnumber
FROM
  categories
JOIN products ON categories.categoryid = products.categoryid
GROUP BY categories.categoryname
ORDER BY totalnumber DESC;



