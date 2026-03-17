import os
import json

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'Person',
#                      'attribute': [
#                          ('string', 'firstName', '', ''),
#                          ('string', 'lastName', '', ''),
#                      ]},
#         'entity_1': {'name': 'Customer Account',
#                      'attribute': [
#                          ('string', 'email', '', ''),
#                      ]}
#     },
#
#     'cluster': {
#     },
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': 'has', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or one'},
#     ],
#
#
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'Customer',
#                      'attribute': [
#
#                      ]},
#         'entity_1': {'name': 'Order',
#                      'attribute': [
#                      ]},
#         'entity_2': {'name': 'Delivery-Address',
#                      'attribute': [
#                      ]},
#         'entity_3': {'name': 'Line-item',
#                      'attribute': [
#                      ]}
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_2', 'name': 'uses', 'type': 'non-identifying',
#          'source_cardinality': 'one or more', 'target_cardinality': 'one or more'},
#         {'source': 'entity_0', 'target': 'entity_1', 'name': 'places', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_1', 'target': 'entity_3', 'name': 'places', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'Customer',
#                      'attribute': [
#                          ('string', 'name', '', ''),
#                          ('string', 'custNumber', '', ''),
#                          ('string', 'sector', '', ''),
#                      ]},
#         'entity_1': {'name': 'Order',
#                      'attribute': [
#                          ('int', 'orderNumber', '', ''),
#                          ('string', 'deliveryAddress', '', ''),
#                      ]},
#         'entity_2': {'name': 'Delivery-Address',
#                      'attribute': [
#                          ('string', 'productCode', '', ''),
#                          ('int', 'quantity', '', ''),
#                          ('float', 'pricePerUnit', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': 'places', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': 'contains', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'Car',
#                      'attribute': [
#                      ]},
#         'entity_1': {'name': 'Person',
#                      'attribute': [
#                      ]},
#         'entity_2': {'name': 'Named-Driver',
#                      'attribute': [
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_2', 'name': 'allows', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': 'is', 'type': 'non-identifying',
#          'source_cardinality': 'zero or more', 'target_cardinality': 'one or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'Car',
#                      'attribute': [
#                          ('string', 'registrationNumber', '', ''),
#                          ('string', 'make', '', ''),
#                          ('string', 'model', '', ''),
#                      ]},
#         'entity_1': {'name': 'Person',
#                      'attribute': [
#                          ('string', 'firstName', '', ''),
#                          ('string', 'lastName', '', ''),
#                          ('int', 'age', '', ''),
#                      ]},
#         'entity_2': {'name': 'Named-Driver',
#                      'attribute': [
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_2', 'name': 'allows', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': 'is', 'type': 'identifying',
#          'source_cardinality': 'zero or more', 'target_cardinality': 'zero or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'Manufacturer',
#                      'attribute': [
#                      ]},
#         'entity_1': {'name': 'Car',
#                      'attribute': [
#                          ('string', 'registrationNumber', 'PK', ''),
#                          ('string', 'make', '', ''),
#                          ('string', 'model', '', ''),
#                          ('string[]', 'parts', '', ''),
#                      ]},
#         'entity_2': {'name': 'Person',
#                      'attribute': [
#                          ('string', 'driversLicense', 'PK', 'The license #'),
#                          ('string(99)', 'firstName', '', 'Only 99 characters are allowed'),
#                          ('string', 'lastName', '', ''),
#                          ('string', 'phone', 'UK', ''),
#                          ('int', 'age', '', ''),
#                      ]},
#         'entity_3': {'name': 'Named-Driver',
#                      'attribute': [
#                          ('string', 'carRegistrationNumber', 'PK,FK', ''),
#                          ('string', 'driverLicence', 'PK,FK', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': 'makes', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_1', 'target': 'entity_3', 'name': 'allows', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_2', 'target': 'entity_3', 'name': 'is', 'type': 'identifying',
#          'source_cardinality': 'zero or more', 'target_cardinality': 'zero or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'Customer',
#                      'attribute': [
#                      ]},
#         'entity_1': {'name': 'Delivered-Address',
#                      'attribute': [
#                      ]},
#         'entity_2': {'name': 'Order',
#                      'attribute': [
#                      ]},
#         'entity_3': {'name': 'Invoice',
#                      'attribute': [
#                      ]},
#         'entity_4': {'name': 'Product-Category',
#                      'attribute': [
#                      ]},
#         'entity_5': {'name': 'Product',
#                      'attribute': [
#                      ]},
#         'entity_6': {'name': 'Order-Item',
#                      'attribute': [
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': 'has', 'type': 'non-identifying',
#          'source_cardinality': 'one or more', 'target_cardinality': 'one or more'},
#         {'source': 'entity_0', 'target': 'entity_2', 'name': 'places', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_0', 'target': 'entity_3', 'name': 'liable for', 'type': 'identifying',
#          'source_cardinality': 'zero or more', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': 'receives', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_3', 'target': 'entity_2', 'name': 'covers', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_2', 'target': 'entity_6', 'name': 'includes', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_4', 'target': 'entity_5', 'name': 'contains', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_5', 'target': 'entity_6', 'name': 'ordered in', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'Author',
#                      'attribute': [
#                          ('varchar(255)', 'Name', 'PK', ''),
#                          ('varchar(255)', 'Address', '', ''),
#                          ('varchar(255)', 'URL', '', ''),
#                      ]},
#         'entity_1': {'name': 'Publisher',
#                      'attribute': [
#                          ('varchar(255)', 'Name', 'PK', ''),
#                          ('varchar(255)', 'Address', '', ''),
#                          ('varchar(255)', 'URL', '', ''),
#                          ('integer(10)', 'Phone', '', ''),
#                      ]},
#         'entity_2': {'name': 'Book',
#                      'attribute': [
#                          ('varchar(255)', 'ISBN', 'PK', ''),
#                          ('varchar(255)', 'PublisherName', '', ''),
#                          ('varchar(255)', 'AuthorName', '', ''),
#                          ('varchar(255)', 'AuthorAddress', '', ''),
#                          ('integer(10)', 'Year', '', ''),
#                          ('varchar(255)', 'Title', '', ''),
#                          ('numeric(19,0)', 'Price', '', ''),
#                      ]},
#         'entity_3': {'name': 'Warehouse_Book',
#                      'attribute': [
#                          ('integer(10)', 'WarehouseCode', 'FK', ''),
#                          ('varchar(255)', 'BookISBN', 'FK', ''),
#                          ('integer(10)', 'Count', '', ''),
#                      ]},
#         'entity_4': {'name': 'Warehouse',
#                      'attribute': [
#                          ('integer(10)', 'Code', 'PK', ''),
#                          ('varchar(255)', 'Phone', '', ''),
#                          ('varchar(255)', 'Address', '', ''),
#                      ]},
#         'entity_5': {'name': 'ShoppingBasket_Book',
#                      'attribute': [
#                          ('integer(10)', 'ShoppingBasketID', 'FK', ''),
#                          ('varchar(255)', 'BookISBN', 'FK', ''),
#                          ('integer(10)', 'Count', '', ''),
#                      ]},
#         'entity_6': {'name': 'Customer',
#                      'attribute': [
#                          ('varchar(255)', 'Email', 'PK', ''),
#                          ('varchar(255)', 'Name', 'FK', ''),
#                          ('varchar(255)', 'Phone', 'FK', ''),
#                          ('varchar(255)', 'Address', '', ''),
#                      ]},
#         'entity_7': {'name': 'ShoppingBasket',
#                      'attribute': [
#                          ('varchar(255)', 'ID', 'PK', ''),
#                          ('varchar(255)', 'CustomerEmail', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_2', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_2', 'target': 'entity_5', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_4', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_7', 'target': 'entity_5', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_6', 'target': 'entity_7', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }


# json_object = {
#     'entity': {
#         'entity_0': {'name': 'Shipment',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('date', 'S_Date', '', ''),
#                          ('integer(10)', 'Ship_ID', '', ''),
#                      ]},
#         'entity_1': {'name': 'Courier',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('varchar(255)', 'Name', '', ''),
#                          ('integer(10)', 'Salary', '', ''),
#                          ('varchar(255)', 'Address', '', ''),
#                      ]},
#         'entity_2': {'name': 'Order',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('integer(10)', 'Shipment_ID', '', ''),
#                          ('integer(10)', 'CourierID', '', ''),
#                          ('varchar(255)', 'DeliveryAddress', '', ''),
#                          ('date', 'CreateDate', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_2', 'name': 'ships', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': 'deliver', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'Customer',
#                      'attribute': [
#                          ('integer', 'ID', 'PK', ''),
#                          ('varchar(255)', 'Name', '', ''),
#                          ('varchar(255)', 'Address', '', ''),
#                          ('char(1)', 'Gender', '', ''),
#                          ('date', 'Date_of_Birth', '', ''),
#                      ]},
#         'entity_1': {'name': 'Purchase_Order',
#                      'attribute': [
#                          ('integer', 'ID', 'PK', ''),
#                          ('integer', 'CustomerID', '', ''),
#                          ('integer(10)', 'Date', '', ''),
#                          ('integer(10)', 'Total', '', ''),
#                      ]},
#         'entity_2': {'name': 'Order_Product',
#                      'attribute': [
#                          ('integer', 'OrderID', 'FK', ''),
#                          ('integer', 'ProductID', 'FK', ''),
#                          ('integer(10)', 'qty', '', ''),
#                      ]},
#         'entity_3': {'name': 'Product',
#                      'attribute': [
#                          ('integer', 'ID', 'PK', ''),
#                          ('integer', 'SupplierID', '', ''),
#                          ('varchar(255)', 'Name', '', ''),
#                      ]},
#         'entity_4': {'name': 'Supplier',
#                      'attribute': [
#                          ('integer', 'ID', 'PK', ''),
#                          ('varchar(255)', 'Name', '', ''),
#                          ('integer(10)', 'Contact', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_3', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_4', 'target': 'entity_3', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'Category',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('varchar(25)', 'Name', '', ''),
#                          ('timestamp', 'Last_Update', '', ''),
#                      ]},
#         'entity_1': {'name': 'Film_Category',
#                      'attribute': [
#                          ('integer(10)', 'FilmID', 'PK', ''),
#                          ('integer(10)', 'CategoryID', '', ''),
#                          ('timestamp', 'Last_Update', '', ''),
#                      ]},
#         'entity_2': {'name': 'Film',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('integer(10)', 'LanguageID', '', ''),
#                          ('varchar(255)', 'Title', '', ''),
#                          ('varchar(255)', 'Description', '', ''),
#                          ('integer(4)', 'Release_Year', '', ''),
#                          ('integer(10)', 'Rental_Duration', '', ''),
#                          ('numeric(19,0)', 'Rental_Rate', '', ''),
#                          ('integer(2)', 'Length', '', ''),
#                          ('numeric(19,0)', 'Replacement_Cost', '', ''),
#                          ('integer(10)', 'Rating', '', ''),
#                          ('timestamp', 'Last_Update', '', ''),
#                          ('varchar(255)', 'Special_Features', '', ''),
#                          ('varchar(255)', 'Fulltext', '', ''),
#                      ]},
#         'entity_3': {'name': 'Language',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('varchar(20)', 'Name', '', ''),
#                          ('timestamp', 'Last_Update', '', ''),
#                      ]},
#         'entity_4': {'name': 'Film_Actor',
#                      'attribute': [
#                          ('integer(10)', 'FilmID', '', ''),
#                          ('integer(10)', 'ActorID', '', ''),
#                          ('timestamp', 'Last_Update', '', ''),
#                      ]},
#         'entity_5': {'name': 'Inventory',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('integer(10)', 'FilmID', '', ''),
#                          ('timestamp', 'Last_Update', '', ''),
#                      ]},
#         'entity_6': {'name': 'Rental',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('integer(10)', 'StaffID', '', ''),
#                          ('integer(10)', 'CustomerID', '', ''),
#                          ('integer(10)', 'InventoryID', '', ''),
#                          ('timestamp', 'Rental_Date', '', ''),
#                          ('timestamp', 'Return_Date', '', ''),
#                          ('timestamp', 'Last_Update', '', ''),
#                      ]},
#         'entity_7': {'name': 'Payment',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('integer(10)', 'RentalID', '', ''),
#                          ('integer(10)', 'CustomerID', '', ''),
#                          ('integer(10)', 'StaffID', '', ''),
#                          ('numeric(19,0)', 'Amount', '', ''),
#                          ('timestamp', 'Payment_Date', '', ''),
#                      ]},
#         'entity_8': {'name': 'Staff',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('integer(10)', 'AddressID', '', ''),
#                          ('integer(10)', 'StoreID', '', ''),
#                          ('integer(10)', 'PaymentID', '', ''),
#                          ('varchar(255)', 'First_Name', '', ''),
#                          ('varchar(255)', 'Last_Name', '', ''),
#                          ('varchar(50)', 'Email', '', ''),
#                          ('chat(1)', 'Active', '', ''),
#                          ('varchar(16)', 'Username', '', ''),
#                          ('varchar(40)', 'Password', '', ''),
#                          ('timestamp', 'Last_Update', '', ''),
#                          ('varchar(80)', 'PictureURL', '', ''),
#                      ]},
#         'entity_9': {'name': 'Actor',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('varchar(255)', 'First_Name', '', ''),
#                          ('varchar(255)', 'Last_Name', '', ''),
#                          ('timestamp', 'Last_Update', '', ''),
#                      ]},
#         'entity_10': {'name': 'Customer',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('integer(10)', 'AddressID', '', ''),
#                          ('integer(10)', 'AddressColumn', '', ''),
#                          ('varchar(255)', 'First_Name', '', ''),
#                          ('varchar(255)', 'Last_Name', '', ''),
#                          ('varchar(50)', 'Email', '', ''),
#                          ('char(1)', 'Active', '', ''),
#                          ('timestamp', 'Create_Date', '', ''),
#                          ('timestamp', 'Last_Update', '', ''),
#                      ]},
#         'entity_11': {'name': 'Customer',
#                       'attribute': [
#                           ('integer(10)', 'ID', 'PK', ''),
#                           ('integer(10)', 'AddressID', '', ''),
#                           ('integer(10)', 'AddressColumn', '', ''),
#                           ('varchar(255)', 'First_Name', '', ''),
#                           ('varchar(255)', 'Last_Name', '', ''),
#                           ('varchar(50)', 'Email', '', ''),
#                           ('char(1)', 'Active', '', ''),
#                           ('timestamp', 'Create_Date', '', ''),
#                           ('timestamp', 'Last_Update', '', ''),
#                       ]},
#         'entity_12': {'name': 'Address',
#                       'attribute': [
#                           ('integer(10)', 'ID', 'PK', ''),
#                           ('integer(10)', 'CityID', '', ''),
#                           ('varchar(50)', 'Address', '', ''),
#                           ('varchar(50)', 'Address', '', ''),
#                           ('varchar(20)', 'District', '', ''),
#                           ('varchar(10)', 'Postal_Code', '', ''),
#                           ('varchar(20)', 'Phone', '', ''),
#                           ('timestamp', 'Last_Update', '', ''),
#                       ]},
#         'entity_13': {'name': 'City',
#                       'attribute': [
#                           ('integer(10)', 'ID', 'PK', ''),
#                           ('varchar(50)', 'CountryID', '', ''),
#                           ('timestamp', 'Last_Update', '', ''),
#                       ]},
#         'entity_14': {'name': 'Store',
#                       'attribute': [
#                           ('integer(10)', 'ID', 'PK', ''),
#                           ('integer(10)', 'AddressID', '', ''),
#                           ('timestamp', 'Last_Update', '', ''),
#                       ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_2', 'target': 'entity_1', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_2', 'target': 'entity_4', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_2', 'target': 'entity_5', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_3', 'target': 'entity_2', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_5', 'target': 'entity_6', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_6', 'target': 'entity_7', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_8', 'target': 'entity_7', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_8', 'target': 'entity_6', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_9', 'target': 'entity_4', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_10', 'target': 'entity_6', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_10', 'target': 'entity_7', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_11', 'target': 'entity_10', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_11', 'target': 'entity_8', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_11', 'target': 'entity_14', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or one'},
#         {'source': 'entity_12', 'target': 'entity_11', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_13', 'target': 'entity_12', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_14', 'target': 'entity_8', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#     'difficulty': 'difficult',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'Loan_Request',
#                      'attribute': [
#                          ('date', 'Date', 'PK', ''),
#                          ('integer(10)', 'BorrowerID', '', ''),
#                          ('date', 'Deadline', '', ''),
#                          ('numeric(19,0)', 'Amount', '', ''),
#                          ('varchar(255)', 'Description', '', ''),
#                          ('date', 'Payday', '', ''),
#                      ]},
#         'entity_1': {'name': 'Loan_Request_Lender',
#                      'attribute': [
#                          ('date', 'Loan_Request_Date', 'FK', ''),
#                          ('integer(10)', 'LenderID', 'FK', ''),
#                          ('numeric(19,0)', 'Amount', '', ''),
#                      ]},
#         'entity_2': {'name': 'Payment',
#                      'attribute': [
#                          ('date', 'Date', 'PK', ''),
#                          ('numeric(19,0)', 'Amount', '', ''),
#                      ]},
#         'entity_3': {'name': 'Borrower',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('integer(10)', 'AddresseeID', '', ''),
#                      ]},
#         'entity_4': {'name': 'Lender_Borrower',
#                      'attribute': [
#                          ('integer(10)', 'BorrowerID', 'FK', ''),
#                          ('integer(10)', 'LenderID', 'FK', ''),
#                          ('date', 'LoanDate', '', ''),
#                          ('integer(10)', 'Percentage', '', ''),
#                      ]},
#         'entity_5': {'name': 'Loan',
#                      'attribute': [
#                          ('date', 'Date', 'PK', ''),
#                          ('date', 'DeadlineAgreed_Date', '', ''),
#                          ('date', 'RepaymentDate', '', ''),
#                      ]},
#         'entity_6': {'name': 'Addressee',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('varchar(255)', 'Name', '', ''),
#                          ('varchar(255)', 'Address', '', ''),
#                      ]},
#         'entity_7': {'name': 'Lender',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('integer(10)', 'AddresseeID', '', ''),
#                      ]},
#         'entity_8': {'name': 'Deadline',
#                      'attribute': [
#                          ('date', 'Agreed_Date', 'PK', ''),
#                      ]},
#         'entity_9': {'name': 'Intermediary',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('integer(10)', 'AddresseeID', '', ''),
#                          ('date', 'LoanDate', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_2', 'target': 'entity_5', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_3', 'target': 'entity_0', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_3', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_3', 'target': 'entity_6', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'exactly one'},
#         {'source': 'entity_5', 'target': 'entity_4', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_5', 'target': 'entity_9', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'exactly one'},
#         {'source': 'entity_6', 'target': 'entity_7', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'exactly one'},
#         {'source': 'entity_6', 'target': 'entity_9', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'exactly one'},
#         {'source': 'entity_7', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_7', 'target': 'entity_1', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_8', 'target': 'entity_5', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#     'difficulty': 'difficult',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'Productline',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('varchar(255)', 'DescInText', '', ''),
#                          ('varchar(255)', 'DescInHTML', '', ''),
#                          ('varchar(100)', 'Image', '', ''),
#                      ]},
#         'entity_1': {'name': 'Employee',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('integer(10)', 'OfficeCode', '', ''),
#                          ('integer(10)', 'reportsTo', '', ''),
#                          ('varchar(255)', 'FirstName', '', ''),
#                          ('varchar(255)', 'LastName', '', ''),
#                          ('varchar(255)', 'Extension', '', ''),
#                          ('varchar(255)', 'Email', '', ''),
#                          ('varchar(100)', 'JobTitle', '', ''),
#                      ]},
#         'entity_2': {'name': 'Office',
#                      'attribute': [
#                          ('integer(10)', 'Code', 'PK', ''),
#                          ('varchar(255)', 'City', '', ''),
#                          ('varchar(255)', 'Phone', '', ''),
#                          ('varchar(255)', 'Address1', '', ''),
#                          ('varchar(255)', 'Address2', '', ''),
#                          ('varchar(255)', 'State', '', ''),
#                          ('varchar(255)', 'Country', '', ''),
#                          ('integer(10)', 'PostalCode', '', ''),
#                          ('varchar(200)', 'Territory', '', ''),
#                      ]},
#         'entity_3': {'name': 'Product',
#                      'attribute': [
#                          ('integer(10)', 'Code', 'PK', ''),
#                          ('integer(10)', 'ProductlineID', '', ''),
#                          ('varchar(255)', 'Name', '', ''),
#                          ('integer(10)', 'Scale', '', ''),
#                          ('varchar(255)', 'Vendor', '', ''),
#                          ('varchar(255)', 'PdtDescription', '', ''),
#                          ('integer(10)', 'QtyInStock', '', ''),
#                          ('numeric(19,0)', 'BuyPrice', '', ''),
#                          ('varchar(255)', 'MSRP', '', ''),
#                      ]},
#         'entity_4': {'name': 'Customer',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('integer(10)', 'salesRepEmployeeNum', '', ''),
#                          ('varchar(255)', 'Name', '', ''),
#                          ('varchar(255)', 'FirstName', '', ''),
#                          ('varchar(255)', 'LastName', '', ''),
#                          ('varchar(255)', 'Phone', '', ''),
#                          ('varchar(255)', 'Address1', '', ''),
#                          ('varchar(255)', 'Address2', '', ''),
#                          ('varchar(255)', 'City', '', ''),
#                          ('varchar(255)', 'State', '', ''),
#                          ('integer(10)', 'PostalCode', '', ''),
#                          ('varchar(255)', 'Country', '', ''),
#                          ('numeric(19,0)', 'CreditLimit', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     # 7
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_3', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_1', 'target': 'entity_4', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_2', 'target': 'entity_1', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_3', 'target': 'entity_5', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_4', 'target': 'entity_6', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_4', 'target': 'entity_7', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_6', 'target': 'entity_5', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#     'difficulty': 'difficult',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'Customer',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('varchar(255)', 'Name', '', ''),
#                          ('varchar(255)', 'Address', '', ''),
#                          ('float(10)', 'Balance', '', ''),
#                          ('char(1)', 'Type', '', ''),
#                      ]},
#         'entity_1': {'name': 'Broker',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('varchar(255)', 'Name', '', ''),
#                          ('integer(10)', 'Salary', '', ''),
#                          ('date', 'Date_Employed', '', ''),
#                      ]},
#         'entity_2': {'name': 'Transaction',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('integer(10)', 'CustomerID', '', ''),
#                          ('integer(10)', 'BrokerID', '', ''),
#                          ('char(1)', 'Type', '', ''),
#                          ('timestamp', 'Create_Time', '', ''),
#                          ('timestamp', 'Execution_Time', '', ''),
#                          ('timestamp', 'Cancellation_Time', '', ''),
#                      ]},
#         'entity_3': {'name': 'Stock',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('integer(10)', 'TransactionalID', '', ''),
#                          ('varchar(10)', 'Code', '', ''),
#                          ('varchar(255)', 'Name', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_2', 'target': 'entity_3', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#     'difficulty': 'difficult',
#     'diagram_type': 'ER'
# }


# json_object = {
#     'entity': {
#         'entity_0': {'name': 'Customer',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('varchar(255)', 'Name', '', ''),
#                          ('varchar(25)', 'Encrypted_Password', '', ''),
#                          ('varchar(255)', 'Address', '', ''),
#                          ('char(1)', 'Type', '', ''),
#                      ]},
#         'entity_1': {'name': 'Purchase_Order',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('timestamp', 'Create_Date', '', ''),
#                          ('integer(10)', 'Three_Gallon', '', ''),
#                          ('integer(10)', 'Five_Gallon_int', '', ''),
#                          ('integer(10)', 'Cup', '', ''),
#                          ('float(10)', 'Amount', '', ''),
#                          ('integer(10)', 'StaffID', '', ''),
#                          ('integer(10)', 'CustomerID', '', ''),
#                          ('integer(10)', 'DeliveryID', '', ''),
#                      ]},
#         'entity_2': {'name': 'Staff',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('varchar(255)', 'Name', '', ''),
#                          ('integer(255)', 'Address', '', ''),
#                          ('varchar(15)', 'Contact', '', ''),
#                      ]},
#         'entity_3': {'name': 'Staff_Delivery',
#                      'attribute': [
#                          ('integer(10)', 'StaffID', 'FK', ''),
#                          ('integer(10)', 'DeliveryID', 'FK', ''),
#                      ]},
#         'entity_4': {'name': 'Delivery',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('date', 'Date', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_2', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_4', 'target': 'entity_1', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_4', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'PlayoffRound',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('integer(10)', 'tema1ID', '', ''),
#                          ('integer(10)', 'tema2ID', '', ''),
#                          ('date', 'startTime', '', ''),
#                          ('date', 'endTime', '', ''),
#                          ('integer(10)', 'roundNum', '', ''),
#                      ]},
#         'entity_1': {'name': 'RoundStats',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('integer(10)', 'numShutouts', '', ''),
#                          ('integer(10)', 'goalLeaderID', '', ''),
#                          ('integer(10)', 'penaltyLeaderID', '', ''),
#                          ('integer(10)', 'plusMinusLeaderID', '', ''),
#                          ('integer(10)', 'faceoffsWonLeaderID', '', ''),
#                          ('integer(10)', 'sogLeaderID', '', ''),
#                      ]},
#         'entity_2': {'name': 'UserStatsPicks',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('integer(10)', 'roundID', '', ''),
#                          ('integer(10)', 'goalLeaderID', '', ''),
#                          ('integer(10)', 'assistLeaderID', '', ''),
#                          ('integer(10)', 'penaltyLeaderID', '', ''),
#                          ('integer(10)', 'plusMinusLeaderID', '', ''),
#                          ('integer(10)', 'faceoffsWonLeaderID', '', ''),
#                          ('integer(10)', 'sogLeaderID', '', ''),
#                          ('integer(10)', 'numShutouts', '', ''),
#                          ('integer(10)', 'userID', '', ''),
#                      ]},
#         'entity_3': {'name': 'HockeyGame',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('integer(10)', 'roundID', '', ''),
#                          ('date', 'startTime', '', ''),
#                          ('varchar(255)', 'description', '', ''),
#                          ('integer(10)', 'tema1ID', '', ''),
#                          ('integer(10)', 'tema2ID', '', ''),
#                      ]},
#         'entity_4': {'name': 'HockeyTeam',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('varchar(255)', 'name', '', ''),
#                          ('varchar(255)', 'logo', '', ''),
#                      ]},
#         'entity_5': {'name': 'User',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('varchar(255)', 'username', '', ''),
#                          ('varchar(255)', 'password', '', ''),
#                      ]},
#         'entity_6': {'name': 'UserScorePicks',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('integer(10)', 'hockGameID', '', ''),
#                          ('integer(10)', 'team1score', '', ''),
#                          ('integer(10)', 'team2score', '', ''),
#                          ('integer(10)', 'userID', '', ''),
#                      ]},
#         'entity_7': {'name': 'GameScores',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('integer(10)', 'team1score', '', ''),
#                          ('integer(10)', 'team2score', '', ''),
#                      ]},
#         'entity_8': {'name': 'HockeyTeamPlayer',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('integer(10)', 'hockGameID', '', ''),
#                          ('varchar(255)', 'firstName', '', ''),
#                          ('varchar(255)', 'lastName', '', ''),
#                          ('integer(10)', 'jerseyNum', '', ''),
#                          ('integer(10)', 'position', '', ''),
#                      ]},
#         'entity_9': {'name': 'UserInfo',
#                      'attribute': [
#                          ('integer(10)', 'ID', 'PK', ''),
#                          ('varchar(255)', 'firstName', '', ''),
#                          ('varchar(255)', 'lastName', '', ''),
#                          ('varchar(255)', 'email', '', ''),
#                          ('integer(10)', 'round1Points', '', ''),
#                          ('integer(10)', 'round2Points', '', ''),
#                          ('integer(10)', 'round3Points', '', ''),
#                          ('integer(10)', 'round4Points', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     # 10
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'one or more', 'target_cardinality': 'one or more'},
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'one or more', 'target_cardinality': 'one or more'},
#         {'source': 'entity_0', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_3', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'one or more', 'target_cardinality': 'one or more'},
#         {'source': 'entity_3', 'target': 'entity_6', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'one or more', 'target_cardinality': 'one or more'},
#         {'source': 'entity_4', 'target': 'entity_8', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_5', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_5', 'target': 'entity_6', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_7', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_9', 'target': 'entity_5', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }


# json_object = {
#     'entity': {
#         'entity_0': {'name': 'Marks',
#                      'attribute': [
#                          ('integer', 'markID', 'PK', ''),
#                          ('integer', 'studentID', '', ''),
#                          ('integer', 'subjectID', '', ''),
#                          ('date', 'date', '', ''),
#                          ('integer', 'mark', '', ''),
#                      ]},
#         'entity_1': {'name': 'Students',
#                      'attribute': [
#                          ('integer', 'studentID', 'PK', ''),
#                          ('varchar', 'firstName', '', ''),
#                          ('varchar', 'lastName', '', ''),
#                          ('integer', 'groupID', '', ''),
#                      ]},
#         'entity_2': {'name': 'Groups',
#                      'attribute': [
#                          ('integer', 'groupID', 'PK', ''),
#                          ('varchar', 'name', '', ''),
#                      ]},
#         'entity_3': {'name': 'Subjects',
#                      'attribute': [
#                          ('integer', 'subjectID', 'PK', ''),
#                          ('varchar', 'title', '', ''),
#                      ]},
#         'entity_4': {'name': 'Subject/teacher',
#                      'attribute': [
#                          ('integer', 'subjectID', 'FK', ''),
#                          ('integer', 'teacherID', 'FK', ''),
#                          ('integer', 'groupID', 'FK', ''),
#                      ]},
#         'entity_5': {'name': 'Teachers',
#                      'attribute': [
#                          ('integer', 'teacherID', 'PK', ''),
#                          ('varchar', 'firstName', '', ''),
#                          ('varchar', 'lastName', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     # 10
#     'relation': [
#         {'source': 'entity_1', 'target': 'entity_0', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_2', 'target': 'entity_1', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_2', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_3', 'target': 'entity_0', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_3', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_5', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'Supplier',
#                      'attribute': [
#                          ('integer', 'supplierID', 'PK', ''),
#                          ('varchar', 'companyName', '', ''),
#                          ('varchar', 'address', '', ''),
#                          ('varchar', 'postcode', '', ''),
#                          ('varchar', 'contactEmail', '', ''),
#                      ]},
#         'entity_1': {'name': 'Item',
#                      'attribute': [
#                          ('integer', 'itemID', 'PK', ''),
#                          ('varchar', 'description', '', ''),
#                          ('varchar', 'category', '', ''),
#                          ('float', 'price', '', ''),
#                          ('integer', 'stockLevel', '', ''),
#                          ('integer', 'supplierID', 'FK', ''),
#                      ]},
#         'entity_2': {'name': 'OrderItem',
#                      'attribute': [
#                          ('integer', 'orderID', 'FK', ''),
#                          ('integer', 'itemID', 'FK', ''),
#                          ('integer', 'quantity', '', ''),
#                      ]},
#         'entity_3': {'name': 'Order',
#                      'attribute': [
#                          ('integer', 'orderID', 'PK', ''),
#                          ('integer', 'customerID', 'FK', ''),
#                          ('integer', 'orderDate', '', ''),
#                      ]},
#         'entity_4': {'name': 'Customer',
#                      'attribute': [
#                          ('integer', 'customerID', 'PK', ''),
#                          ('varchar', 'forename', '', ''),
#                          ('varchar', 'surname', '', ''),
#                          ('varchar', 'address', '', ''),
#                          ('varchar', 'postcode', '', ''),
#                          ('date', 'DOB', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_3', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_4', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }


# json_object = {
#     'entity': {
#         'entity_0': {'name': 'baggage_check',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('varchar(50)', 'check_result', '', ''),
#                          ('bigint', 'create_at', '', ''),
#                          ('bigint', 'update_at', '', ''),
#                          ('bigint', 'booking_id', 'FK', ''),
#                          ('bigint', 'passenger_id', 'FK', ''),
#                      ]},
#         'entity_1': {'name': 'no_fly_list',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('date', 'active_from', '', ''),
#                          ('date', 'active_to', '', ''),
#                          ('varchar(255)', 'no_fly_reason', '', ''),
#                          ('timestamp', 'created_at', '', ''),
#                          ('timestamp', 'updated_at', '', ''),
#                          ('bigint', 'psgnr_id', 'FK', ''),
#                      ]},
#         'entity_2': {'name': 'airport',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('varchar(50)', 'airport_name', '', ''),
#                          ('varchar(50)', 'country', '', ''),
#                          ('varchar(50)', 'state', '', ''),
#                          ('varchar(50)', 'city', '', ''),
#                          ('timestamp', 'created_at', '', ''),
#                          ('timestamp', 'updated_at', '', ''),
#                      ]},
#         'entity_3': {'name': 'security_check',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('varchar(20)', 'check_result', '', ''),
#                          ('varchar(65535)', 'comments', '', ''),
#                          ('timestamp', 'created_at', '', ''),
#                          ('timestamp', 'updated_at', '', ''),
#                          ('bigint', 'passenger_id', 'FK', ''),
#                      ]},
#         'entity_4': {'name': 'passengers',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('varchar(50)', 'first_name', '', ''),
#                          ('varchar(50)', 'last_name', '', ''),
#                          ('date', 'date_of_birth', '', ''),
#                          ('varchar(50)', 'country_of_citizenship', '', ''),
#                          ('varchar(50)', 'country_of_residence', '', ''),
#                          ('varchar(20)', 'passport_number', '', ''),
#                          ('timestamp', 'created_at', '', ''),
#                          ('timestamp', 'updated_at', '', ''),
#                      ]},
#         'entity_5': {'name': 'flights',
#                      'attribute': [
#                          ('bigint', 'flight_id', 'PK', ''),
#                          ('varchar(20)', 'departing_gate', '', ''),
#                          ('varchar(20)', 'arriving_gate', '', ''),
#                          ('timestamp', 'created_at', '', ''),
#                          ('timestamp', 'updated_at', '', ''),
#                          ('bigint', 'airline_id', 'FK', ''),
#                          ('bigint', 'departing_airport_id', 'FK', ''),
#                          ('bigint', 'arriving_airport_id', 'FK', ''),
#                      ]},
#         'entity_6': {'name': 'booking',
#                      'attribute': [
#                          ('bigint', 'bookingid', 'PK', ''),
#                          ('bigint', 'flight_id', 'FK', ''),
#                          ('varchar(20)', 'status', '', ''),
#                          ('varchar(20)', 'booking_platform', '', ''),
#                          ('timestamp', 'created_at', '', ''),
#                          ('timestamp', 'updated_at', '', ''),
#                          ('bigint', 'passenger_id', 'FK', ''),
#                      ]},
#         'entity_7': {'name': 'baggage',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('decimal(4,2)', 'weight_in_kg', '', ''),
#                          ('timestamp', 'created_date', '', ''),
#                          ('timestamp', 'updated_date', '', ''),
#                          ('bigint', 'booking_id', 'FK', ''),
#                      ]},
#         'entity_8': {'name': 'flight_manifest',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('timestamp', 'created_at', '', ''),
#                          ('timestamp', 'updated_at', '', ''),
#                          ('bigint', 'booking_id', 'FK', ''),
#                          ('bigint', 'flight_id', 'FK', ''),
#                      ]},
#         'entity_9': {'name': 'airline',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('varchar', 'airline_code', '', ''),
#                          ('bigint', 'airline_name', '', ''),
#                          ('varchar(50)', 'airline_country', '', ''),
#                          ('timestamp', 'created_at', '', ''),
#                          ('timestamp', 'updated_at', '', ''),
#                      ]},
#         'entity_10': {'name': 'boarding_pass',
#                       'attribute': [
#                           ('bigint', 'id', 'PK', ''),
#                           ('varchar(65535)', 'qr_code', '', ''),
#                           ('timestamp', 'created_at', '', ''),
#                           ('timestamp', 'updated_at', '', ''),
#                           ('bigint', 'booking_id', 'FK', ''),
#                       ]},
#     },
#     'cluster': {
#     },
#     # 11
#     'relation': [
#         {'source': 'entity_2', 'target': 'entity_5', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_4', 'target': 'entity_0', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_4', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_4', 'target': 'entity_1', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_4', 'target': 'entity_6', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_5', 'target': 'entity_8', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_6', 'target': 'entity_0', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_6', 'target': 'entity_8', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_6', 'target': 'entity_10', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_6', 'target': 'entity_7', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }


# json_object = {
#     'entity': {
#         'entity_0': {'name': 'passenger_1',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('varchar(50)', 'first_name', '', ''),
#                          ('varchar(50)', 'last_name', '', ''),
#                          ('date', 'date_of_birth', '', ''),
#                      ]},
#         'entity_1': {'name': 'no_fly_list',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('date', 'active_from', '', ''),
#                          ('date', 'active_to', '', ''),
#                          ('varchar(255)', 'no_fly_reason', '', ''),
#                          ('timestamp', 'created_at', '', ''),
#                          ('timestamp', 'updated_at', '', ''),
#                          ('bigint', 'passenger_id', 'FK', ''),
#                      ]},
#         'entity_2': {'name': 'flight',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('varchar(20)', 'departing_gate', '', ''),
#                          ('varchar(20)', 'arriving_gate', '', ''),
#                          ('timestamp', 'created_at', '', ''),
#                          ('timestamp', 'updated_at', '', ''),
#                          ('bigint', 'airline_id', 'FK', ''),
#                          ('bigint', 'departing_airport_id', 'FK', ''),
#                          ('bigint', 'arriving_airport_id', 'FK', ''),
#                      ]},
#         'entity_3': {'name': 'airport',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('varchar(50)', 'airport_name', '', ''),
#                          ('varchar(50)', 'country', '', ''),
#                          ('varchar(50)', 'state', '', ''),
#                          ('varchar(50)', 'city', '', ''),
#                          ('timestamp', 'created_at', '', ''),
#                          ('timestamp', 'updated_at', '', ''),
#                      ]},
#         'entity_4': {'name': 'security_check',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('varchar(20)', 'check_result', '', ''),
#                          ('varchar(65535)', 'comments', '', ''),
#                          ('timestamp', 'created_at', '', ''),
#                          ('timestamp', 'updated_at', '', ''),
#                          ('bigint', 'passenger_id', 'FK', ''),
#                      ]},
#         'entity_5': {'name': 'baggage_check',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('varchar(50)', 'check_result', '', ''),
#                          ('bigint', 'created_at', '', ''),
#                          ('bigint', 'updated_at', '', ''),
#                          ('bigint', 'booking_id', 'FK', ''),
#                          ('bigint', 'passenger_id', 'FK', ''),
#                      ]},
#         'entity_6': {'name': 'flight_manifest',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('timestamp', 'created_at', '', ''),
#                          ('timestamp', 'updated_at', '', ''),
#                          ('bigint', 'booking_id', 'FK', ''),
#                          ('bigint', 'flight_id', 'FK', ''),
#                      ]},
#         'entity_7': {'name': 'airline',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('bigint', 'airline_code', '', ''),
#                          ('bigint', 'airline_name', '', ''),
#                          ('varchar(50)', 'airline_country', '', ''),
#                          ('timestamp', 'created_at', '', ''),
#                          ('timestamp', 'updated_at', '', ''),
#                      ]},
#         'entity_8': {'name': 'passenger_2',
#                       'attribute': [
#                           ('bigint', 'id', 'PK', ''),
#                           ('varchar(50)', 'first_name', '', ''),
#                           ('varchar(50)', 'last_name', '', ''),
#                           ('date', 'date_of_birth', '', ''),
#                           ('varchar(50)', 'country_of_citizenship', '', ''),
#                           ('varchar(50)', 'country_of_residence', '', ''),
#                           ('varchar(20)', 'passport_number', '', ''),
#                           ('timestamp', 'created_at', '', ''),
#                           ('timestamp', 'updated_at', '', ''),
#                       ]},
#         'entity_9': {'name': 'booking',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('bigint', 'flight_id', 'FK', ''),
#                          ('varchar(20)', 'status', '', ''),
#                          ('varchar(20)', 'booking_platform', '', ''),
#                          ('timestamp', 'created_at', '', ''),
#                          ('timestamp', 'updated_at', '', ''),
#                          ('bigint', 'passenger_id', 'FK', ''),
#                      ]},
#         'entity_10': {'name': 'baggage',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('decimal(4,2)', 'weight_in_kg', '', ''),
#                          ('timestamp', 'created_at', '', ''),
#                          ('timestamp', 'updated_at', '', ''),
#                          ('bigint', 'booking_id', 'FK', ''),
#                      ]},
#         'entity_11': {'name': 'boarding_pass',
#                       'attribute': [
#                           ('bigint', 'id', 'PK', ''),
#                           ('varchar(65535)', 'qr_code', '', ''),
#                           ('timestamp', 'created_at', '', ''),
#                           ('timestamp', 'updated_at', '', ''),
#                           ('bigint', 'booking_id', 'FK', ''),
#                       ]},
#     },
#     'cluster': {
#     },
#     # 11
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_0', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_0', 'target': 'entity_5', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_2', 'target': 'entity_6', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_3', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_7', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_8', 'target': 'entity_9', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_9', 'target': 'entity_5', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_9', 'target': 'entity_6', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_9', 'target': 'entity_10', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_9', 'target': 'entity_11', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'asset_types',
#                      'attribute': [
#                          ('varchar(20)', 'asset_type_code', 'PK', ''),
#                          ('varchar(100)', 'asset_type_description', '', ''),
#                      ]},
#         'entity_1': {'name': 'it_assets',
#                      'attribute': [
#                          ('bigint', 'asset_id', 'PK', ''),
#                          ('varchar(20)', 'asset_type_code', 'FK', ''),
#                          ('varchar(255)', 'description', '', ''),
#                          ('varchar(255)', 'other_details', '', ''),
#                      ]},
#         'entity_2': {'name': 'it_asset_inventory',
#                      'attribute': [
#                          ('bigint', 'it_asset_inventory_id', 'PK', ''),
#                          ('bigint', 'asset_id', 'FK', ''),
#                          ('date', 'inventory_date', '', ''),
#                          ('int', 'number_assigned', '', ''),
#                          ('int', 'number_in_stock', '', ''),
#                          ('varchar(255)', 'other_details', '', ''),
#                      ]},
#         'entity_3': {'name': 'employee_assets',
#                      'attribute': [
#                          ('bigint', 'asset_id', 'FK', ''),
#                          ('bigint', 'employee_id', 'FK', ''),
#                          ('date', 'date_out', '', ''),
#                          ('date', 'date_returned', '', ''),
#                          ('varchar(50)', 'condition_out', '', ''),
#                          ('varchar(50)', 'condition_returned', '', ''),
#                          ('varchar(255)', 'other_details', '', ''),
#                      ]},
#
#         'entity_4': {'name': 'employees',
#                      'attribute': [
#                          ('bigint', 'employee_id', 'PK', ''),
#                          ('varchar(50)', 'first_name', '', ''),
#                          ('varchar(50)', 'last_name', '', ''),
#                          ('varchar(50)', 'department', '', ''),
#                          ('varchar(20)', 'extension', '', ''),
#                          ('varchar(100)', 'email_address', '', ''),
#                          ('varchar(255)', 'other_details', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_1', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_3', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }


# json_object = {
#     'entity': {
#         'entity_0': {'name': 'products',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('varchar(50)', 'sku', '', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('decimal(10,2)', 'price', '', ''),
#                          ('decimal(10,2)', 'weight', '', ''),
#                          ('text', 'descriptions', '', ''),
#                          ('varchar(255)', 'thumbnail', '', ''),
#                          ('varchar(255)', 'image', '', ''),
#                          ('varchar(100)', 'category', '', ''),
#                          ('timestamp', 'create_date', '', ''),
#                          ('int', 'stock', '', ''),
#                      ]},
#         'entity_1': {'name': 'order_details',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('bigint', 'order_id', 'FK', ''),
#                          ('bigint', 'product_id', 'FK', ''),
#                          ('decimal(10,2)', 'price', '', ''),
#                          ('varchar(50)', 'sku', '', ''),
#                          ('int', 'quantity', '', ''),
#                      ]},
#         'entity_2': {'name': 'product_options',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('bigint', 'option_id', 'FK', ''),
#                          ('bigint', 'product_id', 'FK', ''),
#                      ]},
#         'entity_3': {'name': 'product_categories',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('bigint', 'product_id', 'FK', ''),
#                          ('bigint', 'category_id', 'FK', ''),
#                      ]},
#
#         'entity_4': {'name': 'orders',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('bigint', 'customer_id', 'FK', ''),
#                          ('decimal(10,2)', 'amount', '', ''),
#                          ('varchar(255)', 'shipping_address', '', ''),
#                          ('varchar(255)', 'order_address', '', ''),
#                          ('varchar(100)', 'order_email', '', ''),
#                          ('timestamp', 'order_date', '', ''),
#                          ('varchar(50)', 'order_status', '', ''),
#                      ]},
#         'entity_5': {'name': 'options',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('varchar(100)', 'option_name', '', ''),
#                      ]},
#         'entity_6': {'name': 'categories',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('text', 'description', '', ''),
#                          ('varchar(255)', 'thumbnail', '', ''),
#                      ]},
#         'entity_7': {'name': 'customers',
#                      'attribute': [
#                          ('bigint', 'id', 'PK', ''),
#                          ('varchar(100)', 'email', '', ''),
#                          ('varchar(100)', 'password', '', ''),
#                          ('varchar(100)', 'full_name', '', ''),
#                          ('varchar(255)', 'billing_address', '', ''),
#                          ('varchar(255)', 'default_shipping_address', '', ''),
#                          ('varchar(50)', 'country', '', ''),
#                          ('varchar(20)', 'phone', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_3', 'target': 'entity_0', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_4', 'target': 'entity_1', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_5', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_6', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_7', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }


# json_object = {
#     'entity': {
#         'entity_0': {'name': 'Person.ContactType',
#                      'attribute': [
#                          ('int', 'ContactTypeID', 'PK', ''),
#                          ('varchar(50)', 'Name', '', ''),
#                          ('datetime', 'ModifiedDate', '', ''),
#                      ]},
#         'entity_1': {'name': 'Person.Address',
#                      'attribute': [
#                          ('int', 'AddressID', 'PK', ''),
#                          ('varchar(60)', 'AddressLine1', '', ''),
#                          ('varchar(60)', 'AddressLine2', '', ''),
#                          ('varchar(30)', 'City', '', ''),
#                          ('int', 'StateProvinceID', 'FK', ''),
#                          ('varchar(15)', 'PostalCode', '', ''),
#                          ('uniqueidentifier', 'rowguid', '', ''),
#                          ('datetime', 'ModifiedDate', '', ''),
#                      ]},
#         'entity_2': {'name': 'Person.BusinessEntityContact',
#                      'attribute': [
#                          ('int', 'BusinessEntityID', 'FK', ''),
#                          ('int', 'PersonID', 'FK', ''),
#                          ('int', 'ContactTypeID', 'FK', ''),
#                          ('uniqueidentifier', 'rowguid', '', ''),
#                          ('datetime', 'ModifiedDate', '', ''),
#                      ]},
#         'entity_3': {'name': 'Person.BusinessEntity',
#                      'attribute': [
#                          ('int', 'BusinessEntityID', 'PK', ''),
#                          ('uniqueidentifier', 'rowguid', '', ''),
#                          ('datetime', 'ModifiedDate', '', ''),
#                      ]},
#
#         'entity_4': {'name': 'Person.BusinessEntityAddress',
#                      'attribute': [
#                          ('int', 'BusinessEntityID', 'FK', ''),
#                          ('int', 'AddressID', 'FK', ''),
#                          ('int', 'AddressTypeID', 'FK', ''),
#                          ('uniqueidentifier', 'rowguid', '', ''),
#                          ('datetime', 'ModifiedDate', '', ''),
#                      ]},
#         'entity_5': {'name': 'Person.StateProvince',
#                      'attribute': [
#                          ('int', 'StateProvinceID', 'PK', ''),
#                          ('varchar(3)', 'StateProvinceCode', '', ''),
#                          ('int', 'CountryRegionCode', 'FK', ''),
#                          ('bit', 'IsOnlyStateProvinceFlag', '', ''),
#                          ('varchar(50)', 'Name', '', ''),
#                          ('uniqueidentifier', 'rowguid', '', ''),
#                          ('datetime', 'ModifiedDate', '', ''),
#                      ]},
#         'entity_6': {'name': 'Person.Person',
#                      'attribute': [
#                          ('int', 'BusinessEntityID', 'PK', ''),
#                          ('varchar(2)', 'PersonType', '', ''),
#                          ('bit', 'NameStyle', '', ''),
#                          ('varchar(8)', 'Title', '', ''),
#                          ('varchar(50)', 'FirstName', '', ''),
#                          ('varchar(50)', 'MiddleName', '', ''),
#                          ('varchar(50)', 'LastName', '', ''),
#                          ('varchar(10)', 'Suffix', '', ''),
#                          ('int', 'EmailPromotion', '', ''),
#                          ('varchar(max)', 'AdditionalContactInfo', '', ''),
#                          ('varchar(max)', 'Demographics', '', ''),
#                          ('uniqueidentifier', 'rowguid', '', ''),
#                          ('datetime', 'ModifiedDate', '', ''),
#                      ]},
#         'entity_7': {'name': 'Person.AddressType',
#                      'attribute': [
#                          ('int', 'AddressTypeID', 'PK', ''),
#                          ('varchar(50)', 'Name', '', ''),
#                          ('uniqueidentifier', 'rowguid', '', ''),
#                          ('datetime', 'ModifiedDate', '', ''),
#                      ]},
#         'entity_8': {'name': 'Person.CountryRegion',
#                      'attribute': [
#                          ('varchar(3)', 'CountryRegionCode', 'PK', ''),
#                          ('varchar(50)', 'Name', '', ''),
#                          ('datetime', 'ModifiedDate', '', ''),
#                      ]},
#         'entity_9': {'name': 'Person.EmailAddress',
#                      'attribute': [
#                          ('int', 'BusinessEntityID', 'FK', ''),
#                          ('int', 'EmailAddressID', 'PK', ''),
#                          ('varchar(50)', 'EmailAddress', '', ''),
#                          ('varchar(50)', 'EmailAddressText', '', ''),
#                          ('uniqueidentifier', 'rowguid', '', ''),
#                          ('datetime', 'ModifiedDate', '', ''),
#                      ]},
#         'entity_10': {'name': 'Person.PersonPhone',
#                       'attribute': [
#                           ('int', 'BusinessEntityID', 'FK', ''),
#                           ('varchar(25)', 'PhoneNumber', '', ''),
#                           ('int', 'PhoneNumberTypeID', 'FK', ''),
#                           ('datetime', 'ModifiedDate', '', ''),
#                       ]},
#         'entity_11': {'name': 'Person.Password',
#                       'attribute': [
#                           ('int', 'BusinessEntityID', 'FK', ''),
#                           ('varchar(128)', 'PasswordHash', '', ''),
#                           ('varchar(10)', 'PasswordSalt', '', ''),
#                           ('uniqueidentifier', 'rowguid', '', ''),
#                           ('datetime', 'ModifiedDate', '', ''),
#                       ]},
#         'entity_12': {'name': 'Person.PhoneNumberType',
#                       'attribute': [
#                           ('int', 'PhoneNumberTypeID', 'PK', ''),
#                           ('varchar(50)', 'Name', '', ''),
#                           ('datetime', 'ModifiedDate', '', ''),
#                       ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_1', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_3', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_3', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_3', 'target': 'entity_6', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'exactly one'},
#         {'source': 'entity_5', 'target': 'entity_1', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_6', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_6', 'target': 'entity_9', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_6', 'target': 'entity_10', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_6', 'target': 'entity_11', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'exactly one'},
#         {'source': 'entity_7', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_8', 'target': 'entity_5', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_12', 'target': 'entity_10', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }


# json_object = {
#     'entity': {
#         'entity_0': {'name': 'film_actor',
#                      'attribute': [
#                          ('smallint', 'actor_id', 'PK,FK', ''),
#                          ('smallint', 'film_id', 'PK,FK', ''),
#                          ('timestamp', 'last_update', '', ''),
#                      ]},
#         'entity_1': {'name': 'actor',
#                      'attribute': [
#                          ('smallint', 'actor_id', 'PK', ''),
#                          ('varchar(45)', 'first_name', '', ''),
#                          ('varchar(45)', 'last_name', '', ''),
#                          ('timestamp', 'last_update', '', ''),
#                      ]},
#
#         'entity_2': {'name': 'film_category',
#                      'attribute': [
#                          ('smallint', 'film_id', 'PK,FK', ''),
#                          ('tinyint', 'category_id', 'PK,FK', ''),
#                          ('timestamp', 'last_update', '', ''),
#                      ]},
#         'entity_3': {'name': 'category',
#                      'attribute': [
#                          ('smallint', 'category_id', 'PK', ''),
#                          ('varchar(25)', 'name', '', ''),
#                          ('timestamp', 'last_update', '', ''),
#                      ]},
#         'entity_4': {'name': 'film',
#                      'attribute': [
#                          ('smallint', 'film_id', 'PK', ''),
#                          ('varchar(255)', 'title', '', ''),
#                          ('varchar(255)', 'description', '', ''),
#                          ('YEAR', 'release_year', '', ''),
#                          ('tinyint', 'language_id', 'FK', ''),
#                          ('tinyint', 'original_language_id', 'FK', ''),
#                          ('tinyint', 'rental_duration', '', ''),
#                          ('decimal(4,2)', 'rental_rate', '', ''),
#                          ('smallint', 'length', '', ''),
#                          ('decimal(5,2)', 'replacement_cost', '', ''),
#                          ('enum', 'rating', '', ''),
#                          ('varchar(255)', 'special_features', '', ''),
#                          ('timestamp', 'last_update', '', ''),
#                      ]},
#         'entity_5': {'name': 'language',
#                      'attribute': [
#                          ('tinyint', 'language_id', 'PK', ''),
#                          ('char(20)', 'name', '', ''),
#                          ('timestamp', 'last_update', '', ''),
#                      ]},
#         'entity_6': {'name': 'staff',
#                       'attribute': [
#                           ('tinyint', 'staff_id', 'PK', ''),
#                           ('varchar(45)', 'first_name', '', ''),
#                           ('varchar(45)', 'last_name', '', ''),
#                           ('varchar(50)', 'email', '', ''),
#                           ('tinyint', 'store_id', 'FK', ''),
#                           ('boolean', 'active', '', ''),
#                           ('varchar(16)', 'username', '', ''),
#                           ('varchar(40)', 'password', '', ''),
#                           ('timestamp', 'last_update', '', ''),
#                       ]},
#         'entity_7': {'name': 'inventory',
#                      'attribute': [
#                          ('mediumint', 'inventory_id', 'PK', ''),
#                          ('smallint', 'film_id', 'FK', ''),
#                          ('tinyint', 'store_id', 'FK', ''),
#                          ('timestamp', 'last_update', '', ''),
#                      ]},
#         'entity_8': {'name': 'store',
#                       'attribute': [
#                           ('tinyint', 'store_id', 'PK', ''),
#                           ('tinyint', 'manager_staff_id', 'FK', ''),
#                           ('timestamp', 'last_update', '', ''),
#                       ]},
#         'entity_9': {'name': 'payment',
#                      'attribute': [
#                          ('smallint', 'payment_id', 'PK', ''),
#                          ('smallint', 'customer_id', 'FK', ''),
#                          ('tinyint', 'staff_id', 'FK', ''),
#                          ('INT', 'rental_id', 'FK', ''),
#                          ('decimal(5,2)', 'amount', '', ''),
#                          ('datetime', 'payment_date', '', ''),
#                          ('timestamp', 'last_update', '', ''),
#                      ]},
#         'entity_10': {'name': 'rental',
#                      'attribute': [
#                          ('INT', 'rental_id', 'PK', ''),
#                          ('datetime', 'rental_date', '', ''),
#                          ('mediumint', 'inventory_id', 'FK', ''),
#                          ('smallint', 'customer_id', 'FK', ''),
#                          ('datetime', 'return_date', '', ''),
#                          ('tinyint', 'staff_id', 'FK', ''),
#                          ('timestamp', 'last_update', '', ''),
#                      ]},
#         'entity_11': {'name': 'customer',
#                       'attribute': [
#                           ('smallint', 'customer_id', 'PK', ''),
#                           ('tinyint', 'store_id', 'FK', ''),
#                           ('varchar(45)', 'first_name', '', ''),
#                           ('varchar(45)', 'last_name', '', ''),
#                           ('varchar(50)', 'email', '', ''),
#                           ('boolean', 'active', '', ''),
#                           ('datetime', 'create_date', '', ''),
#                           ('timestamp', 'last_update', '', ''),
#                       ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_1', 'target': 'entity_0', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_3', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_4', 'target': 'entity_0', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_4', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_4', 'target': 'entity_7', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_5', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_6', 'target': 'entity_9', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_6', 'target': 'entity_10', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_6', 'target': 'entity_8', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'exactly one'},
#         {'source': 'entity_7', 'target': 'entity_10', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_8', 'target': 'entity_6', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_8', 'target': 'entity_7', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_8', 'target': 'entity_11', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_10', 'target': 'entity_9', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_11', 'target': 'entity_9', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_11', 'target': 'entity_10', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }


# json_object = {
#     'entity': {
#         'entity_0': {'name': 'invoice_items',
#                      'attribute': [
#                          ('integer', 'InvoiceLineId', 'PK', ''),
#                          ('integer', 'InvoiceId', 'FK', ''),
#                          ('integer', 'TrackId', 'FK', ''),
#                          ('numeric', 'UnitPrice', '', ''),
#                          ('integer', 'Quantity', '', ''),
#                      ]},
#         'entity_1': {'name': 'playlist_track',
#                       'attribute': [
#                           ('integer', 'PlaylistId', 'PK,FK', ''),
#                           ('integer', 'TrackId', 'PK,FK', ''),
#                       ]},
#         'entity_2': {'name': 'playlists',
#                      'attribute': [
#                          ('integer', 'PlaylistId', 'PK', ''),
#                          ('varchar', 'Name', '', ''),
#                      ]},
#         'entity_3': {'name': 'invoices',
#                      'attribute': [
#                          ('integer', 'InvoiceId', 'PK', ''),
#                          ('integer', 'CustomerId', 'FK', ''),
#                          ('datetime', 'InvoiceDate', '', ''),
#                          ('varchar', 'BillingAddress', '', ''),
#                          ('varchar', 'BillingCity', '', ''),
#                          ('varchar', 'BillingState', '', ''),
#                          ('varchar', 'BillingCountry', '', ''),
#                          ('varchar', 'BillingPostalCode', '', ''),
#                          ('numeric', 'Total', '', ''),
#                      ]},
#         'entity_4': {'name': 'tracks',
#                      'attribute': [
#                          ('integer', 'TrackId', 'PK', ''),
#                          ('integer', 'AlbumId', 'FK', ''),
#                          ('varchar', 'Name', '', ''),
#                          ('integer', 'MediaTypeId', 'FK', ''),
#                          ('integer', 'GenreId', 'FK', ''),
#                          ('varchar', 'Composer', '', ''),
#                          ('integer', 'Milliseconds', '', ''),
#                          ('integer', 'Bytes', '', ''),
#                          ('numeric', 'UnitPrice', '', ''),
#                      ]},
#
#         'entity_5': {'name': 'customers',
#                      'attribute': [
#                          ('integer', 'CustomerId', 'PK', ''),
#                          ('varchar', 'FirstName', '', ''),
#                          ('varchar', 'LastName', '', ''),
#                          ('varchar', 'Company', '', ''),
#                          ('varchar', 'Address', '', ''),
#                          ('varchar', 'City', '', ''),
#                          ('varchar', 'State', '', ''),
#                          ('varchar', 'Country', '', ''),
#                          ('varchar', 'PostalCode', '', ''),
#                          ('varchar', 'Phone', '', ''),
#                          ('varchar', 'Fax', '', ''),
#                          ('varchar', 'Email', '', ''),
#                          ('integer', 'SupportRepId', 'FK', ''),
#                      ]},
#         'entity_6': {'name': 'albums',
#                      'attribute': [
#                          ('integer', 'AlbumId', 'PK', ''),
#                          ('varchar', 'Title', '', ''),
#                          ('integer', 'ArtistId', 'FK', ''),
#                      ]},
#
#         'entity_7': {'name': 'media_types',
#                      'attribute': [
#                          ('integer', 'MediaTypeId', 'PK', ''),
#                          ('varchar', 'Name', '', ''),
#                      ]},
#         'entity_8': {'name': 'genres',
#                      'attribute': [
#                          ('integer', 'GenreId', 'PK', ''),
#                          ('varchar', 'Name', '', ''),
#                      ]},
#         'entity_9': {'name': 'employees',
#                      'attribute': [
#                          ('integer', 'EmployeeId', 'PK', ''),
#                          ('varchar', 'LastName', '', ''),
#                          ('varchar', 'FirstName', '', ''),
#                          ('varchar', 'Title', '', ''),
#                          ('integer', 'ReportsTo', 'FK', ''),
#                          ('datetime', 'BirthDate', '', ''),
#                          ('datetime', 'HireDate', '', ''),
#                          ('varchar', 'Address', '', ''),
#                          ('varchar', 'City', '', ''),
#                          ('varchar', 'State', '', ''),
#                          ('varchar', 'Country', '', ''),
#                          ('varchar', 'PostalCode', '', ''),
#                          ('varchar', 'Phone', '', ''),
#                          ('varchar', 'Fax', '', ''),
#                          ('varchar', 'Email', '', ''),
#                      ]},
#         'entity_10': {'name': 'artists',
#                      'attribute': [
#                          ('integer', 'ArtistId', 'PK', ''),
#                          ('varchar', 'Name', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_2', 'target': 'entity_1', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_3', 'target': 'entity_0', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_4', 'target': 'entity_0', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_4', 'target': 'entity_1', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_5', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_6', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_7', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_8', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_9', 'target': 'entity_5', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_10', 'target': 'entity_6', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }


# json_object = {
#     'entity': {
#         'entity_0': {'name': 'stop',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('varchar(10)', 'code', '', ''),
#                          ('varchar(100)', 'name', '', ''),
#                      ]},
#
#         'entity_1': {'name': 'job_category',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('varchar(10)', 'code', '', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('varchar(255)', 'description', '', ''),
#                      ]},
#         'entity_2': {'name': 'job_platform',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('varchar(10)', 'code', '', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('varchar(255)', 'desc', '', ''),
#                      ]},
#         'entity_3': {'name': 'process_step',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('int', 'step_id', 'FK', ''),
#                          ('int', 'process_id', 'FK', ''),
#                          ('varchar', 'status', '', ''),
#                          ('int', 'priority', '', ''),
#                      ]},
#         'entity_4': {'name': 'job',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('varchar(10)', 'code', '', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('varchar(255)', 'description', '', ''),
#                          ('datetime', 'date_published', '', ''),
#                          ('datetime', 'job_start_date', '', ''),
#                          ('int', 'no_of_vacancies', '', ''),
#                          ('int', 'job_category_id', 'FK', ''),
#                          ('int', 'position_id', 'FK', ''),
#                          ('int', 'job_platform_id', 'FK', ''),
#                          ('int', 'org_id', 'FK', ''),
#                          ('int', 'process_id', 'FK', ''),
#                      ]},
#         'entity_5': {'name': 'job_position',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('varchar(10)', 'code', '', ''),
#                          ('varchar(100)', 'position_name', '', ''),
#                          ('varchar(255)', 'description', '', ''),
#                      ]},
#         'entity_6': {'name': 'process',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('varchar(255)', 'code', '', ''),
#                          ('varchar(255)', 'description', '', ''),
#                          ('int', 'recruiter_id', '', ''),
#                      ]},
#         'entity_7': {'name': 'organization',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('varchar(100)', 'code', '', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('varchar(255)', 'description', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_1', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_2', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_5', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_6', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_6', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_7', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }


# json_object = {
#     'entity': {
#         'entity_0': {'name': 'tblCATEGORIES',
#                      'attribute': [
#                          ('int', 'category_id', 'PK', ''),
#                          ('varchar', 'category_name', '', ''),
#                          ('varchar', 'category_description', '', ''),
#                          ('varchar', 'category_type', '', ''),
#                      ]},
#         'entity_1': {'name': 'tblEQUIP_CAT',
#                      'attribute': [
#                          ('int', 'equip_cat_id', 'PK', ''),
#                          ('int', 'category_id', 'FK', ''),
#                          ('int', 'equipment_id', 'FK', ''),
#                      ]},
#         'entity_2': {'name': 'tblEQUIPMENT',
#                      'attribute': [
#                          ('int', 'equipment_id', 'PK', ''),
#                          ('varchar', 'equipment_name', '', ''),
#                          ('varchar', 'equipment_description', '', ''),
#                          ('int', 'equipment_status_id', 'FK', ''),
#                          ('varchar', 'status_id', 'FK', ''),
#                      ]},
#         'entity_3': {'name': 'tblSTATUS',
#                       'attribute': [
#                           ('int', 'status_id', 'PK', ''),
#                           ('varchar', 'status_name', '', ''),
#                           ('varchar', 'status_notes', '', ''),
#                       ]},
#         'entity_4': {'name': 'tblCONTACT_CAT',
#                      'attribute': [
#                          ('int', 'contact_cat_id', 'PK', ''),
#                          ('int', 'category_id', 'FK', ''),
#                          ('int', 'contact_id', 'FK', ''),
#                          ('int', 'project_hr_id', 'FK', ''),
#                      ]},
#         'entity_5': {'name': 'tblCALENDAR',
#                       'attribute': [
#                           ('int', 'calendar_id', 'PK', ''),
#                           ('datetime', 'calendar_date', '', ''),
#                           ('int', 'project_hr_id', 'FK', ''),
#                           ('int', 'project_equip_id', 'FK', ''),
#                           ('int', 'invoice_id', 'FK', ''),
#                           ('bit', 'calendar_date_confirmed', '', ''),
#                       ]},
#         'entity_6': {'name': 'tblEQUIP_HIRE_RATES',
#                      'attribute': [
#                          ('int', 'equip_hire_rate_id', 'PK', ''),
#                          ('int', 'equipment_id', 'FK', ''),
#                          ('int', 'hire_rate_id', 'FK', ''),
#                      ]},
#         'entity_7': {'name': 'tblCONTACTS',
#                      'attribute': [
#                          ('int', 'contact_id', 'PK', ''),
#                          ('int', 'type_id', 'FK', ''),
#                          ('varchar', 'contact_name', '', ''),
#                      ]},
#
#         'entity_8': {'name': 'tblPROJECT_HR',
#                      'attribute': [
#                          ('int', 'project_hr_id', 'PK', ''),
#                          ('int', 'project_id', 'FK', ''),
#                          ('varchar', 'project_testimonial', '', ''),
#                      ]},
#         'entity_9': {'name': 'tblHIRE_RATES',
#                       'attribute': [
#                           ('int', 'hire_rate_id', 'PK', ''),
#                           ('decimal', 'hire_rate_rate', '', ''),
#                           ('varchar', 'hire_rate_period', '', ''),
#                       ]},
#         'entity_10': {'name': 'tblTYPE',
#                      'attribute': [
#                          ('int', 'type_id', 'PK', ''),
#                          ('varchar', 'type_name', '', ''),
#                      ]},
#         'entity_11': {'name': 'tblPROJECTS',
#                      'attribute': [
#                          ('int', 'project_id', 'PK', ''),
#                          ('varchar', 'project_name', '', ''),
#                          ('varchar', 'project_description', '', ''),
#                          ('datetime', 'project_start_date', '', ''),
#                          ('datetime', 'project_end_date', '', ''),
#                          ('int', 'project_owner_id', '', ''),
#                          ('int', 'contact_id', 'FK', ''),
#                      ]},
#         'entity_12': {'name': 'tblPROJECT_EQUIPMENT',
#                      'attribute': [
#                          ('int', 'project_equip_id', 'PK', ''),
#                          ('int', 'project_id', 'FK', ''),
#                          ('int', 'equip_id', 'FK', ''),
#                          ('decimal', 'proj_equip_booking_rate', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_0', 'target': 'entity_4', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_2', 'target': 'entity_1', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_2', 'target': 'entity_6', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_2', 'target': 'entity_12', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_3', 'target': 'entity_2', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_7', 'target': 'entity_4', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_7', 'target': 'entity_11', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_8', 'target': 'entity_4', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_8', 'target': 'entity_5', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_9', 'target': 'entity_6', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_10', 'target': 'entity_7', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_11', 'target': 'entity_8', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_11', 'target': 'entity_12', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_12', 'target': 'entity_5', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'zero or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'person',
#                      'attribute': [
#                          ('int', 'person_id', 'PK', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('date', 'date_of_birth', '', ''),
#                          ('varchar(100)', 'email_address', '', ''),
#                      ]},
#         'entity_1': {'name': 'account',
#                      'attribute': [
#                          ('int', 'account_id', 'PK', ''),
#                          ('int', 'person_id', 'FK', ''),
#                          ('varchar(50)', 'account_number', '', ''),
#                          ('datetime', 'created_date', '', ''),
#                          ('varchar(20)', 'status', '', ''),
#                          ('varchar(255)', 'shipping_address', '', ''),
#                          ('varchar(100)', 'payment_method', '', ''),
#                      ]},
#         'entity_2': {'name': 'cart',
#                      'attribute': [
#                          ('int', 'cart_id', 'PK', ''),
#                          ('int', 'account_id', 'FK', ''),
#                          ('varchar(20)', 'status', '', ''),
#                          ('datetime', 'created_date', '', ''),
#                          ('datetime', 'purchased_date', '', ''),
#                          ('varchar(50)', 'payment_type', '', ''),
#                          ('varchar(255)', 'delivery_address', '', ''),
#                      ]},
#
#         'entity_3': {'name': 'item',
#                      'attribute': [
#                          ('int', 'item_id', 'PK', ''),
#                          ('int', 'cart_id', 'FK', ''),
#                          ('int', 'category_id', 'FK', ''),
#                          ('varchar(100)', 'item_name', '', ''),
#                          ('text', 'description', '', ''),
#                          ('varchar(255)', 'image', '', ''),
#                          ('varchar(100)', 'supplier', '', ''),
#                      ]},
#
#         'entity_4': {'name': 'offer',
#                      'attribute': [
#                          ('int', 'offer_id', 'PK', ''),
#                          ('int', 'item_id', 'FK', ''),
#                          ('varchar(50)', 'offer_type', '', ''),
#                          ('datetime', 'valid_from_date', '', ''),
#                          ('datetime', 'valid_to_date', '', ''),
#                          ('decimal(10,2)', 'discount', '', ''),
#                          ('text', 'terms_conditions', '', ''),
#                      ]},
#
#         'entity_5': {'name': 'category',
#                      'attribute': [
#                          ('int', 'category_id', 'PK', ''),
#                          ('varchar(100)', 'category_name', '', ''),
#                          ('varchar(50)', 'category_type', '', ''),
#                          ('text', 'category_description', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_2', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'zero or more', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_3', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'zero or more', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_4', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_4', 'target': 'entity_5', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'zero or more', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_5', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'one or more', 'target_cardinality': 'zero or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'groups',
#                      'attribute': [
#                          ('int', 'id_group', 'PK', ''),
#                          ('varchar(150)', 'title', '', ''),
#                      ]},
#
#         'entity_1': {'name': 'topics',
#                      'attribute': [
#                          ('int', 'id_topic', 'PK', ''),
#                          ('int', 'id_user', 'FK', ''),
#                          ('datetime', 'date_modified', '', ''),
#                          ('varchar(200)', 'title', '', ''),
#                      ]},
#
#         'entity_2': {'name': 'schedule',
#                      'attribute': [
#                          ('int', 'id_sch', 'PK', ''),
#                          ('time', 'time_start', '', ''),
#                          ('time', 'time_end', '', ''),
#                          ('varchar(20)', 'weekday', '', ''),
#                          ('varchar(200)', 'title', '', ''),
#                      ]},
#
#         'entity_3': {'name': 'users',
#                      'attribute': [
#                          ('int', 'id_user', 'PK', ''),
#                          ('int', 'id_group', 'FK', ''),
#                          ('varchar(100)', 'first_name', '', ''),
#                          ('varchar(100)', 'fam_name', '', ''),
#                          ('varchar(255)', 'email', '', ''),
#                          ('varchar(255)', 'pass', '', ''),
#                          ('text', 'about', '', ''),
#                      ]},
#
#         'entity_4': {'name': 'posts',
#                      'attribute': [
#                          ('int', 'id_post', 'PK', ''),
#                          ('int', 'id_topic', 'FK', ''),
#                          ('int', 'id_user', 'FK', ''),
#                          ('datetime', 'date_created', '', ''),
#                          ('text', 'body', '', ''),
#                      ]},
#
#         'entity_5': {'name': 'calendar',
#                      'attribute': [
#                          ('int', 'id_cal', 'PK', ''),
#                          ('date', 'date_start', '', ''),
#                          ('date', 'date_end', '', ''),
#                          ('varchar(200)', 'title', '', ''),
#                      ]},
#
#         'entity_6': {'name': 'pages',
#                      'attribute': [
#                          ('int', 'id_page', 'PK', ''),
#                          ('int', 'id_user', 'FK', ''),
#                          ('datetime', 'date_modified', '', ''),
#                          ('varchar(200)', 'title', '', ''),
#                          ('text', 'body', '', ''),
#                          ('boolean', 'is_home', '', ''),
#                      ]},
#
#         'entity_7': {'name': 'files',
#                      'attribute': [
#                          ('int', 'id_file', 'PK', ''),
#                          ('int', 'id_user', 'FK', ''),
#                          ('datetime', 'date_modified', '', ''),
#                          ('varchar(200)', 'title', '', ''),
#                          ('varchar(255)', 'filename', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_1', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_2', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'zero or more', 'target_cardinality': 'exactly one'},
#         {'source': 'entity_3', 'target': 'entity_0', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_4', 'target': 'entity_1', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_4', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_5', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'zero or more', 'target_cardinality': 'exactly one'},
#         {'source': 'entity_6', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_7', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'zero or one', 'target_cardinality': 'zero or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'wbs',
#                      'attribute': [
#                          ('int', 'wbs_id', 'PK', ''),
#                          ('varchar(50)', 'wbs_no', '', ''),
#                          ('int', 'parent_wbs_id', 'FK', ''),  # self-reference -> wbs.wbs_id
#                          ('varchar(150)', 'name', '', ''),
#                          ('int', 'project_id', 'FK', ''),  # -> projects.project_id
#                      ]},
#         'entity_1': {'name': 'statuses',
#                      'attribute': [
#                          ('int', 'status_id', 'PK', ''),
#                          ('varchar(60)', 'name', '', ''),
#                          ('boolean', 'is_open', '', ''),
#                      ]},
#         'entity_2': {'name': 'activities_relationships',
#                      'attribute': [
#                          ('int', 'activity_relationship_id', 'PK', ''),
#                          ('int', 'activity_id', 'FK', ''),  # -> activities.activity_id
#                          ('int', 'preceding_activity_id', 'FK', ''),  # -> activities.activity_id
#                      ]},
#         'entity_3': {'name': 'programs',
#                      'attribute': [
#                          ('int', 'program_id', 'PK', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('int', 'manager_id', 'FK', ''),  # -> people.person_id
#                          ('varchar(50)', 'status', '', ''),
#                      ]},
#         'entity_4': {'name': 'projects',
#                      'attribute': [
#                          ('int', 'project_id', 'PK', ''),
#                          ('varchar(50)', 'project_number', '', ''),
#                          ('int', 'program_id', 'FK', ''),  # -> programs.program_id
#                          ('varchar(150)', 'name', '', ''),
#                      ]},
#         'entity_5': {'name': 'activities',
#                      'attribute': [
#                          ('int', 'activity_id', 'PK', ''),
#                          ('varchar(50)', 'activity_no', '', ''),
#                          ('varchar(150)', 'name', '', ''),
#                          ('int', 'project_id', 'FK', ''),  # -> projects.project_id
#                          ('varchar(255)', 'description', '', ''),
#                          ('int', 'wbs_id', 'FK', ''),  # -> wbs.wbs_id
#                      ]},
#         'entity_6': {'name': 'project_roles',
#                      'attribute': [
#                          ('int', 'project_role_id', 'PK', ''),
#                          ('int', 'project_id', 'FK', ''),  # -> projects.project_id
#                          ('int', 'person_id', 'FK', ''),  # -> people.person_id
#                          ('date', 'valid_from', '', ''),
#                          ('date', 'valid_to', '', ''),
#                      ]},
#         'entity_7': {'name': 'people',
#                      'attribute': [
#                          ('int', 'person_id', 'PK', ''),
#                          ('varchar(60)', 'first_name', '', ''),
#                          ('varchar(120)', 'middle_names', '', ''),
#                          ('int', 'department_id', 'FK', ''),  # -> departments.department_id
#                      ]},
#         'entity_8': {'name': 'departments',
#                      'attribute': [
#                          ('int', 'department_id', 'PK', ''),
#                          ('varchar(100)', 'name', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_1', 'target': 'entity_0', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_1', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_1', 'target': 'entity_5', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_3', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_4', 'target': 'entity_0', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_4', 'target': 'entity_5', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_4', 'target': 'entity_6', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_7', 'target': 'entity_6', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_8', 'target': 'entity_7', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }


# json_object = {
#     'entity': {
#         'entity_0': {'name': 'professor',
#                      'attribute': [
#                          ('integer', 'prof_id', 'PK', ''),
#                          ('varchar(50)', 'prof_lname', '', ''),
#                          ('varchar(50)', 'prof_fname', '', ''),
#                      ]},
#         'entity_1': {'name': 'class',
#                      'attribute': [
#                          ('integer', 'class_id', 'PK', ''),
#                          ('varchar(255)', 'class_name', '', ''),
#                          ('integer', 'prof_id', 'FK', ''),  # professor
#                          ('integer', 'course_id', 'FK', ''),  # course
#                          ('integer', 'room_id', 'FK', ''),  # room
#                      ]},
#         'entity_2': {'name': 'course',
#                      'attribute': [
#                          ('integer', 'course_id', 'PK', ''),
#                          ('varchar(255)', 'course_name', '', ''),
#                      ]},
#         'entity_3': {'name': 'student',
#                      'attribute': [
#                          ('integer', 'stud_id', 'PK', ''),
#                          ('varchar(50)', 'stud_fname', '', ''),
#                          ('varchar(50)', 'stud_lname', '', ''),
#                          ('varchar(255)', 'stud_street', '', ''),
#                          ('varchar(50)', 'stud_city', '', ''),
#                          ('varchar(10)', 'stud_zip', '', ''),
#                      ]},
#
#         'entity_4': {'name': 'enroll',
#                      'attribute': [
#                          ('integer', 'stud_id', 'PK,FK', ''),  # student
#                          ('integer', 'class_id', 'PK,FK', ''),  # class
#                          ('varchar(3)', 'grade', '', ''),
#                      ]},
#
#         'entity_5': {'name': 'room',
#                      'attribute': [
#                          ('integer', 'room_id', 'PK', ''),
#                          ('varchar(50)', 'room_loc', '', ''),
#                          ('varchar(50)', 'room_cap', '', ''),
#                          ('integer', 'class_id', 'FK', ''),  # optional ref
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_1', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_1', 'target': 'entity_5', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'exactly one'},
#         {'source': 'entity_2', 'target': 'entity_1', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_3', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }


# json_object = {
#     'entity': {
#         'entity_0': {'name': 'Person.ContactType',
#                      'attribute': [
#                          ('int', 'ContactTypeID', 'PK', ''),
#                          ('varchar(50)', 'Name', '', ''),
#                      ]},
#
#         'entity_1': {'name': 'HumanResources.Employee',
#                      'attribute': [
#                          ('int', 'BusinessEntityID', 'PK', ''),
#                          ('varchar(15)', 'NationalIDNumber', '', ''),
#                          ('varchar(256)', 'LoginID', '', ''),
#                          ('varchar(50)', 'OrganizationNode', '', ''),
#                          ('int', 'OrganizationLevel', '', ''),
#                          ('varchar(50)', 'JobTitle', '', ''),
#                      ]},
#         'entity_2': {'name': 'Person.Password',
#                      'attribute': [
#                          ('int', 'BusinessEntityID', 'FK', ''),
#                          ('varchar(128)', 'PasswordHash', '', ''),
#                      ]},
#         'entity_3': {'name': 'Person.BusinessEntityContact',
#                      'attribute': [
#                          ('int', 'BusinessEntityID', 'FK', ''),
#                          ('int', 'PersonID', 'FK', ''),
#                          ('int', 'ContactTypeID', 'FK', ''),
#                      ]},
#         'entity_4': {'name': 'Person.Person',
#                      'attribute': [
#                          ('int', 'BusinessEntityID', 'PK', ''),
#                          ('varchar(2)', 'PersonType', '', ''),
#                          ('varchar(50)', 'FirstName', '', ''),
#                          ('varchar(50)', 'LastName', '', ''),
#                      ]},
#         'entity_5': {'name': 'Person.PersonPhone',
#                      'attribute': [
#                          ('int', 'BusinessEntityID', 'FK', ''),
#                          ('varchar(25)', 'PhoneNumber', '', ''),
#                          ('int', 'PhoneNumberTypeID', 'FK', ''),
#                      ]},
#         'entity_6': {'name': 'Person.BusinessEntity',
#                      'attribute': [
#                          ('int', 'BusinessEntityID', 'PK', ''),
#                      ]},
#         'entity_7': {'name': 'Person.EmailAddress',
#                      'attribute': [
#                          ('int', 'BusinessEntityID', 'FK', ''),
#                          ('int', 'EmailAddressID', 'PK', ''),
#                          ('varchar(50)', 'EmailAddress', '', ''),
#                      ]},
#
#         'entity_8': {'name': 'Person.PhoneNumberType',
#                      'attribute': [
#                          ('int', 'PhoneNumberTypeID', 'PK', ''),
#                          ('varchar(50)', 'Name', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_4', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_4', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_4', 'target': 'entity_5', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_4', 'target': 'entity_7', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_6', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_6', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_8', 'target': 'entity_5', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'order_products',
#                      'attribute': [
#                          ('serial', 'id', 'PK', ''),
#                          ('integer', 'order_id', 'FK', ''),
#                          ('integer', 'product_id', 'FK', ''),
#                          ('integer', 'quantity', '', ''),
#                      ]},
#
#         'entity_1': {'name': 'orders',
#                      'attribute': [
#                          ('serial', 'id', 'PK', ''),
#                          ('integer', 'user_id', 'FK', ''),
#                          ('date', 'date', '', ''),
#                      ]},
#
#         'entity_2': {'name': 'addresses',
#                      'attribute': [
#                          ('serial', 'id', 'PK', ''),
#                          ('integer', 'user_id', 'FK', ''),
#                          ('varchar(255)', 'street_address', '', ''),
#                          ('varchar(255)', 'city', '', ''),
#                          ('varchar(255)', 'state', '', ''),
#                          ('varchar(10)', 'zip', '', ''),
#                      ]},
#
#         'entity_3': {'name': 'products',
#                      'attribute': [
#                          ('serial', 'id', 'PK', ''),
#                          ('varchar(255)', 'name', '', ''),
#                          ('varchar(255)', 'description', '', ''),
#                          ('numeric(10,2)', 'price', '', ''),
#                      ]},
#
#         'entity_4': {'name': 'users',
#                      'attribute': [
#                          ('serial', 'id', 'PK', ''),
#                          ('varchar(50)', 'name', '', ''),
#                          ('varchar(100)', 'email', '', ''),
#                          ('varchar(100)', 'password', '', ''),
#                      ]},
#
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_4', 'target': 'entity_1', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#         {'source': 'entity_4', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_1', 'target': 'entity_0', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_3', 'target': 'entity_0', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'}
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'customer',
#                      'attribute': [
#                          ('int(11)', 'id', 'PK', ''),
#                          ('varchar(150)', 'name', '', ''),
#                          ('varchar(150)', 'surname', '', ''),
#                          ('enum', 'category', '', ''),
#                          ('int(11)', 'billing_address_id', 'FK', ''),
#                          ('int(11)', 'shipping_address_id', 'FK', ''),
#                      ]},
#
#         'entity_1': {'name': 'cart',
#                      'attribute': [
#                          ('int(11)', 'id', 'PK', ''),
#                          ('int(11)', 'customer_id', 'FK', ''),
#                          ('timestamp', 'created', '', ''),
#                          ('decimal(10,2)', 'total_value', '', ''),
#                          ('longtext', 'products', '', ''),
#                      ]},
#
#         'entity_2': {'name': 'order',
#                      'attribute': [
#                          ('int(11)', 'id', 'PK', ''),
#                          ('int(11)', 'customer_id', 'FK', ''),
#                          ('timestamp', 'placed', '', ''),
#                          ('timestamp', 'paid', '', ''),
#                          ('decimal(10,2)', 'total_value', '', ''),
#                          ('enum', 'status', '', ''),
#                      ]},
#         'entity_3': {'name': 'address',
#                      'attribute': [
#                          ('int(11)', 'id', 'PK', ''),
#                          ('varchar(150)', 'street', '', ''),
#                          ('varchar(150)', 'city', '', ''),
#                          ('varchar(20)', 'zip_code', '', ''),
#                          ('varchar(150)', 'country', '', ''),
#                      ]},
#         'entity_4': {'name': 'ordered_products',
#                      'attribute': [
#                          ('int(11)', 'product_id', 'FK', ''),
#                          ('int(11)', 'order_id', 'FK', ''),
#                          ('decimal(10,2)', 'price', '', ''),
#                          ('decimal(10,2)', 'discount', '', ''),
#                      ]},
#         'entity_5': {'name': 'product',
#                      'attribute': [
#                          ('int(11)', 'id', 'PK', ''),
#                          ('int(11)', 'vendor_id', 'FK', ''),
#                          ('varchar(150)', 'name', '', ''),
#                          ('text', 'description', '', ''),
#                          ('varchar(100)', 'sku', '', ''),
#                          ('decimal(10,2)', 'price', '', ''),
#                          ('int(11)', 'stock_qty', '', ''),
#                      ]},
#
#         'entity_6': {'name': 'vendor',
#                      'attribute': [
#                          ('int(11)', 'id', 'PK', ''),
#                          ('varchar(150)', 'company_name', '', ''),
#                          ('varchar(250)', 'email', '', ''),
#                          ('enum', 'category', '', ''),
#                          ('tinyint(1)', 'is_active', '', ''),
#                          ('int(11)', 'contact_address_id', 'FK', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_2', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_3', 'target': 'entity_0', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_3', 'target': 'entity_6', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_5', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#         {'source': 'entity_6', 'target': 'entity_5', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'student',
#                      'attribute': [
#                          ('int', 'student_id', 'PK', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('varchar(20)', 'contact_number', '', ''),
#                          ('varchar(100)', 'email', '', ''),
#                          ('varchar(100)', 'password', '', ''),
#                          ('varchar(10)', 'year', '', ''),
#                          ('text', 'additional_info', '', ''),
#                      ]},
#
#         'entity_1': {'name': 'book',
#                      'attribute': [
#                          ('int', 'book_id', 'PK', ''),
#                          ('varchar(255)', 'title', '', ''),
#                          ('varchar(100)', 'edition', '', ''),
#                          ('varchar(150)', 'author', '', ''),
#                          ('varchar(100)', 'category', '', ''),
#                          ('decimal(10,2)', 'price', '', ''),
#                          ('varchar(50)', 'status', '', ''),
#                          ('text', 'additional_info', '', ''),
#                      ]},
#
#         'entity_2': {'name': 'users',
#                      'attribute': [
#                          ('int', 'staff_id', 'PK', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('varchar(20)', 'contact_number', '', ''),
#                          ('varchar(100)', 'email', '', ''),
#                          ('varchar(100)', 'password', '', ''),
#                          ('varchar(50)', 'role', '', ''),
#                          ('text', 'additional_info', '', ''),
#                      ]},
#
#         'entity_3': {'name': 'borrowers_record',
#                      'attribute': [
#                          ('int', 'borrow_id', 'PK', ''),
#                          ('int', 'book_id', 'FK', ''),
#                          ('int', 'student_id', 'FK', ''),
#                          ('date', 'issue_date', '', ''),
#                          ('date', 'return_date', '', ''),
#                          ('decimal(10,2)', 'fine', '', ''),
#                          ('text', 'notes', '', ''),
#                      ]},
#
#         'entity_4': {'name': 'bookreturn_record',
#                      'attribute': [
#                          ('int', 'return_id', 'PK', ''),
#                          ('int', 'borrow_id', 'FK', ''),
#                          ('int', 'book_id', 'FK', ''),
#                          ('int', 'student_id', 'FK', ''),
#                          ('date', 'return_date', '', ''),
#                          ('decimal(10,2)', 'late_fee', '', ''),
#                          ('text', 'notes', '', ''),
#                      ]},
#
#         'entity_5': {'name': 'reports',
#                      'attribute': [
#                          ('int', 'report_id', 'PK', ''),
#                          ('varchar(100)', 'report_type', '', ''),
#                          ('text', 'description', '', ''),
#                          ('date', 'generated_date', '', ''),
#                          ('text', 'student_records', '', ''),
#                          ('text', 'book_records', '', ''),
#                          ('text', 'additional_info', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_3', 'name': 'student_borrows_books', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_0', 'target': 'entity_4', 'name': 'student_return_records', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_1', 'target': 'entity_3', 'name': 'book_in_borrowers_record', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_1', 'target': 'entity_4', 'name': 'book_return_records', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_3', 'target': 'entity_4', 'name': 'borrow_return_record', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or one'},
#
#         {'source': 'entity_0', 'target': 'entity_1', 'name': 'student_to_book_via_borrows', 'type': 'non-identifying',
#          'source_cardinality': 'zero or more', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_0', 'target': 'entity_1', 'name': 'student_to_book_via_returns', 'type': 'non-identifying',
#          'source_cardinality': 'zero or more', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_4', 'target': 'entity_5', 'name': 'print_return_book_records', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_3', 'target': 'entity_5', 'name': 'print_borrowed_book_records', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }


# json_object = {
#     'entity': {
#         'entity_0': {'name': 'products',
#                      'attribute': [
#                          ('int', 'product_id', 'PK', ''),
#                          ('int', 'category_id', 'FK', ''),
#                          ('varchar(150)', 'product_name', '', ''),
#                      ]},
#
#         'entity_1': {'name': 'categories',
#                      'attribute': [
#                          ('int', 'category_id', 'PK', ''),
#                          ('varchar(150)', 'category_name', '', ''),
#                          ('varchar(100)', 'category_type', '', ''),
#                      ]},
#
#         'entity_2': {'name': 'seller',
#                      'attribute': [
#                          ('int', 'seller_id', 'PK', ''),
#                          ('int', 'product_id', 'FK', ''),
#                          ('varchar(150)', 'name', '', ''),
#                          ('varchar(150)', 'contact_add', '', ''),
#                      ]},
#
#         'entity_3': {'name': 'shopping_order',
#                      'attribute': [
#                          ('int', 'order_id', 'PK', ''),
#                          ('int', 'customer_id', 'FK', ''),
#                          ('date', 'date', '', ''),
#                      ]},
#
#         'entity_4': {'name': 'customer',
#                      'attribute': [
#                          ('int', 'customer_id', 'PK', ''),
#                          ('varchar(150)', 'name', '', ''),
#                          ('varchar(150)', 'contact_add', '', ''),
#                          ('varchar(255)', 'address', '', ''),
#                      ]},
#
#         'entity_5': {'name': 'payment',
#                      'attribute': [
#                          ('int', 'payment_id', 'PK', ''),
#                          ('int', 'customer_id', 'FK', ''),
#                          ('date', 'date', '', ''),
#                      ]},
#
#         'entity_6': {'name': 'deliveries',
#                      'attribute': [
#                          ('int', 'delivery_id', 'PK', ''),
#                          ('int', 'order_id', 'FK', ''),
#                          ('int', 'customer_id', 'FK', ''),
#                          ('int', 'product_id', 'FK', ''),
#                          ('date', 'date', '', ''),
#                      ]},
#
#         'entity_7': {'name': 'transaction_reports',
#                      'attribute': [
#                          ('int', 'report_id', 'PK', ''),
#                          ('int', 'customer_id', 'FK', ''),
#                          ('int', 'order_id', 'FK', ''),
#                          ('int', 'product_id', 'FK', ''),
#                          ('int', 'payment_id', 'FK', ''),
#                          ('date', 'date', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_1', 'target': 'entity_0', 'name': 'category_has_products', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         # Products → Seller
#         {'source': 'entity_0', 'target': 'entity_2', 'name': 'product_has_sellers', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         # Customer → Shopping Order
#         {'source': 'entity_4', 'target': 'entity_3', 'name': 'customer_places_orders', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         # Customer → Payment
#         {'source': 'entity_4', 'target': 'entity_5', 'name': 'customer_makes_payments', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         # Order → Deliveries
#         {'source': 'entity_3', 'target': 'entity_6', 'name': 'order_has_deliveries', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         # Customer → Deliveries
#         {'source': 'entity_4', 'target': 'entity_6', 'name': 'customer_receives_deliveries', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         # Product → Deliveries
#         {'source': 'entity_0', 'target': 'entity_6', 'name': 'product_in_deliveries', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         # Customer → Transaction Reports
#         {'source': 'entity_4', 'target': 'entity_7', 'name': 'customer_in_reports', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         # Order → Transaction Reports
#         {'source': 'entity_3', 'target': 'entity_7', 'name': 'order_in_reports', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         # Product → Transaction Reports
#         {'source': 'entity_0', 'target': 'entity_7', 'name': 'product_in_reports', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         # Payment → Transaction Reports
#         {'source': 'entity_5', 'target': 'entity_7', 'name': 'payment_in_reports', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'department',
#                      'attribute': [
#                          ('int', 'department_id', 'PK', ''),
#                          ('int', 'dept_code', '', ''),
#                          ('varchar(150)', 'name', '', ''),
#                      ]},
#
#         'entity_1': {'name': 'term',
#                      'attribute': [
#                          ('int', 'term_id', 'PK', ''),
#                          ('varchar(50)', 'name', '', ''),
#                      ]},
#
#         'entity_2': {'name': 'student',
#                      'attribute': [
#                          ('int', 'student_id', 'PK', ''),
#                          ('float', 'cgpa', '', ''),
#                          ('int', 'credits_earned', '', ''),
#                          ('float', 'grade_points_earned', '', ''),
#                          ('varchar(150)', 'name', '', ''),
#                          ('varchar(20)', 'reg_no', '', ''),
#                          ('varchar(20)', 'roll_no', '', ''),
#                          ('varchar(50)', 'section', '', ''),
#                          ('int', 'semester', '', ''),
#                          ('int', 'department_id', 'FK', ''),
#                      ]},
#
#         'entity_3': {'name': 'user',
#                      'attribute': [
#                          ('int', 'user_id', 'PK', ''),
#                          ('varchar(200)', 'password_digest', '', ''),
#                          ('varchar(50)', 'section', '', ''),
#                          ('int', 'semester', '', ''),
#                          ('varchar(50)', 'user_type', '', ''),
#                          ('varchar(100)', 'username', '', ''),
#                          ('int', 'department_id', 'FK', ''),
#                      ]},
#
#         'entity_4': {'name': 'subject',
#                      'attribute': [
#                          ('int', 'subject_id', 'PK', ''),
#                          ('varchar(20)', 'abbreviation', '', ''),
#                          ('int', 'credits', '', ''),
#                          ('int', 'semester', '', ''),
#                          ('varchar(150)', 'name', '', ''),
#                          ('varchar(20)', 'subject_code', '', ''),
#                          ('varchar(50)', 'subject_type', '', ''),
#                          ('int', 'department_id', 'FK', ''),
#                      ]},
#
#         'entity_5': {'name': 'exam',
#                      'attribute': [
#                          ('int', 'exam_id', 'PK', ''),
#                          ('datetime', 'date', '', ''),
#                          ('varchar(150)', 'name', '', ''),
#                          ('int', 'semester', '', ''),
#                      ]},
#
#         'entity_6': {'name': 'uniexam',
#                      'attribute': [
#                          ('int', 'uniexam_id', 'PK', ''),
#                          ('int', 'batch', '', ''),
#                          ('varchar(50)', 'exam_type', '', ''),
#                          ('int', 'semester', '', ''),
#                          ('int', 'students_sem', '', ''),
#                          ('int', 'total_credits', '', ''),
#                          ('int', 'department_id', 'FK', ''),
#                      ]},
#
#         'entity_7': {'name': 'attendance_report',
#                      'attribute': [
#                          ('int', 'attendance_report_id', 'PK', ''),
#                          ('int', 'no_absent_days', '', ''),
#                          ('int', 'total_working_days', '', ''),
#                          ('int', 'term_id', 'FK', ''),
#                          ('int', 'student_id', 'FK', ''),
#                      ]},
#
#         'entity_8': {'name': 'attendance',
#                      'attribute': [
#                          ('int', 'attendance_id', 'PK', ''),
#                          ('datetime', 'date', '', ''),
#                          ('int', 'present', '', ''),  # count
#                          ('boolean', 'present_bool', '', ''),  # flag
#                          ('int', 'attendance_report_id', 'FK', ''),
#                      ]},
#
#         'entity_9': {'name': 'attendance_remark',
#                      'attribute': [
#                          ('int', 'attendance_remark_id', 'PK', ''),
#                          ('varchar(255)', 'remarks', '', ''),
#                          ('int', 'attendance_id', 'FK', ''),
#                      ]},
#
#         'entity_10': {'name': 'result',
#                       'attribute': [
#                           ('int', 'result_id', 'PK', ''),
#                           ('int', 'no_failed', '', ''),
#                           ('float', 'percentage', '', ''),
#                           ('int', 'rank', '', ''),
#                           ('varchar(50)', 'result', '', ''),
#                           ('varchar(50)', 'section', '', ''),
#                           ('int', 'total', '', ''),
#                           ('int', 'student_id', 'FK', ''),
#                           ('int', 'exam_id', 'FK', ''),
#                       ]},
#
#         'entity_11': {'name': 'uniexam_performance',
#                       'attribute': [
#                           ('int', 'uniexam_performance_id', 'PK', ''),
#                           ('float', 'gpa', '', ''),
#                           ('int', 'semester', '', ''),
#                           ('int', 'student_id', 'FK', ''),
#                           ('int', 'uniexam_id', 'FK', ''),
#                       ]},
#
#         'entity_12': {'name': 'mark',
#                       'attribute': [
#                           ('int', 'mark_id', 'PK', ''),
#                           ('int', 'marks', '', ''),
#                           ('varchar(5)', 'result', '', ''),
#                           ('int', 'student_id', 'FK', ''),
#                           ('int', 'subject_id', 'FK', ''),
#                           ('int', 'exam_id', 'FK', ''),
#                       ]},
#
#         'entity_13': {'name': 'backlog',
#                       'attribute': [
#                           ('int', 'backlog_id', 'PK', ''),
#                           ('boolean', 'cleared', '', ''),
#                           ('int', 'cleared_sem', '', ''),
#                           ('float', 'grade_points', '', ''),
#                           ('int', 'student_id', 'FK', ''),
#                           ('int', 'subject_id', 'FK', ''),
#                       ]},
#
#         'entity_14': {'name': 'uniresult',
#                       'attribute': [
#                           ('int', 'uniresult_id', 'PK', ''),
#                           ('float', 'gpa', '', ''),
#                           ('int', 'credits_earned', '', ''),
#                           ('int', 'credit_rank', '', ''),
#                           ('float', 'grade_points_earned', '', ''),
#                           ('varchar(50)', 'result', '', ''),
#                           ('varchar(50)', 'section', '', ''),
#                           ('int', 'section_rank', '', ''),
#                           ('int', 'student_id', 'FK', ''),
#                           ('int', 'uniexam_id', 'FK', ''),
#                       ]},
#
#         'entity_15': {'name': 'unimark',
#                       'attribute': [
#                           ('int', 'unimark_id', 'PK', ''),
#                           ('boolean', 'current', '', ''),
#                           ('varchar(5)', 'grad_sgpi', '', ''),
#                           ('float', 'grade_points', '', ''),
#                           ('varchar(5)', 'result', '', ''),
#                           ('int', 'student_id', 'FK', ''),
#                           ('int', 'subject_id', 'FK', ''),
#                           ('int', 'uniexam_id', 'FK', ''),
#                       ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#     # Department ownership
#     {'source': 'entity_0', 'target': 'entity_2', 'name': 'department_has_students', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     {'source': 'entity_0', 'target': 'entity_3', 'name': 'department_has_users', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     {'source': 'entity_0', 'target': 'entity_4', 'name': 'department_has_subjects', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     {'source': 'entity_0', 'target': 'entity_6', 'name': 'department_runs_uniexams', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     # Attendance chain
#     {'source': 'entity_1', 'target': 'entity_7', 'name': 'term_has_attendance_reports', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     {'source': 'entity_2', 'target': 'entity_7', 'name': 'student_has_attendance_report', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     {'source': 'entity_7', 'target': 'entity_8', 'name': 'report_has_attendance_rows', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     {'source': 'entity_8', 'target': 'entity_9', 'name': 'attendance_has_remarks', 'type': 'non-identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     # Exams / results
#     {'source': 'entity_5', 'target': 'entity_10', 'name': 'exam_has_results', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     {'source': 'entity_2', 'target': 'entity_10', 'name': 'student_exam_results', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     # Marks per subject & exam
#     {'source': 'entity_2', 'target': 'entity_12', 'name': 'student_marks', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     {'source': 'entity_4', 'target': 'entity_12', 'name': 'subject_has_marks', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     {'source': 'entity_5', 'target': 'entity_12', 'name': 'exam_has_marks', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     # Backlogs per student & subject
#     {'source': 'entity_2', 'target': 'entity_13', 'name': 'student_backlogs', 'type': 'non-identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     {'source': 'entity_4', 'target': 'entity_13', 'name': 'subject_in_backlog', 'type': 'non-identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     # University exam aggregates
#     {'source': 'entity_6', 'target': 'entity_11', 'name': 'uniexam_performances', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     {'source': 'entity_2', 'target': 'entity_11', 'name': 'student_uniexam_performance', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_6', 'target': 'entity_14', 'name': 'uniexam_results', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     {'source': 'entity_2', 'target': 'entity_14', 'name': 'student_uniexam_results', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_6', 'target': 'entity_15', 'name': 'uniexam_marks', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     {'source': 'entity_4', 'target': 'entity_15', 'name': 'subject_unimarks', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     {'source': 'entity_2', 'target': 'entity_15', 'name': 'student_unimarks', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
# ],
#
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }


# json_object = {
#     'entity': {
#         'entity_0': {'name': 'department',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('varchar(100)', 'name', '', ''),
#                      ]},
#
#         'entity_1': {'name': 'employees',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('int', 'department_id', 'FK', ''),
#                          ('int', 'supervisor', 'FK', ''),  # self-reference
#                          ('date', 'anniversary_date', '', ''),
#                      ]},
#
#         'entity_2': {'name': 'assessments',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('int', 'department_id', 'FK', ''),
#                          ('varchar(100)', 'title', '', ''),
#                      ]},
#
#         'entity_3': {'name': 'assessment_versions',
#                      'attribute': [
#                          ('int', 'assessment_id', 'FK', ''),
#                          ('int', 'version', 'PK', ''),
#                          ('int', 'frequency_id', '', ''),
#                      ]},
#
#         'entity_4': {'name': 'sections',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('int', 'assessment_id', 'FK', ''),
#                          ('int', 'version', 'FK', ''),
#                          ('varchar(100)', 'title', '', ''),
#                      ]},
#
#         'entity_5': {'name': 'questions',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('int', 'section_id', 'FK', ''),
#                          ('text', 'text', '', ''),
#                      ]},
#
#         'entity_6': {'name': 'employee_assessments',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('int', 'employee_id', 'FK', ''),
#                          ('int', 'assessment_id', 'FK', ''),
#                          ('int', 'version', 'FK', ''),
#                          ('date', 'date_completed', '', ''),
#                      ]},
#
#         'entity_7': {'name': 'responses',
#                      'attribute': [
#                          ('int', 'instance_id', 'PK,FK', ''),
#                          ('int', 'question_id', 'PK,FK', ''),
#                          ('varchar(255)', 'value', '', ''),
#                          ('text', 'comment', '', ''),
#                          ('int', 'id', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#     {'source': 'entity_0', 'target': 'entity_1', 'name': 'department_has_employees', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_1', 'target': 'entity_1', 'name': 'employee_supervisor_relationship', 'type': 'non-identifying',
#      'source_cardinality': 'zero or one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_0', 'target': 'entity_2', 'name': 'department_has_assessments', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_2', 'target': 'entity_3', 'name': 'assessment_has_versions', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_3', 'target': 'entity_4', 'name': 'version_has_sections', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_4', 'target': 'entity_5', 'name': 'section_has_questions', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_1', 'target': 'entity_6', 'name': 'employee_takes_assessments', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_2', 'target': 'entity_6', 'name': 'assessment_instances', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_6', 'target': 'entity_7', 'name': 'employee_responses', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_5', 'target': 'entity_7', 'name': 'question_responses', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
# ],
#
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'tournament',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('date', 'start_date', '', ''),
#                          ('date', 'end_date', '', ''),
#                          ('varchar(100)', 'location', '', ''),
#                          ('text', 'description', '', ''),
#                      ]},
#
#         'entity_1': {'name': 'match',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('int', 'tournament_id', 'FK', ''),
#                          ('date', 'match_date', '', ''),
#                          ('varchar(50)', 'round', '', ''),
#                          ('varchar(20)', 'status', '', ''),
#                      ]},
#
#         'entity_2': {'name': 'standing',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('int', 'tournament_id', 'FK', ''),
#                          ('int', 'team_id', 'FK', ''),
#                          ('int', 'played', '', ''),
#                          ('int', 'won', '', ''),
#                          ('int', 'drawn', '', ''),
#                          ('int', 'lost', '', ''),
#                          ('int', 'goals_for', '', ''),
#                          ('int', 'goals_against', '', ''),
#                          ('int', 'points', '', ''),
#                      ]},
#
#         'entity_3': {'name': 'team',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('varchar(100)', 'coach', '', ''),
#                          ('int', 'founded_year', '', ''),
#                      ]},
#
#         'entity_4': {'name': 'player',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('varchar(50)', 'first_name', '', ''),
#                          ('varchar(50)', 'last_name', '', ''),
#                          ('date', 'date_of_birth', '', ''),
#                          ('varchar(50)', 'nationality', '', ''),
#                          ('varchar(50)', 'position', '', ''),
#                          ('int', 'team_id', 'FK', ''),
#                      ]},
#
#         'entity_5': {'name': 'match_team',
#                      'attribute': [
#                          ('int', 'match_id', 'FK', ''),
#                          ('int', 'team_id', 'FK', ''),
#                          ('boolean', 'is_home', '', ''),
#                          ('int', 'score', '', ''),
#                      ]},
#
#         'entity_6': {'name': 'referee',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('varchar(50)', 'first_name', '', ''),
#                          ('varchar(50)', 'last_name', '', ''),
#                          ('varchar(50)', 'nationality', '', ''),
#                      ]},
#
#         'entity_7': {'name': 'match_referee',
#                      'attribute': [
#                          ('int', 'match_id', 'FK', ''),
#                          ('int', 'referee_id', 'FK', ''),
#                          ('varchar(50)', 'role', '', ''),
#                      ]},
#
#         'entity_8': {'name': 'match_player_stats',
#                      'attribute': [
#                          ('int', 'match_id', 'FK', ''),
#                          ('int', 'player_id', 'FK', ''),
#                          ('int', 'minutes_played', '', ''),
#                          ('int', 'goals', '', ''),
#                          ('int', 'yellow_cards', '', ''),
#                          ('int', 'red_cards', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#     {'source': 'entity_0', 'target': 'entity_1', 'name': 'tournament_has_matches', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_0', 'target': 'entity_2', 'name': 'tournament_has_standings', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_3', 'target': 'entity_2', 'name': 'team_in_standings', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_1', 'target': 'entity_5', 'name': 'match_has_teams', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#
#     {'source': 'entity_3', 'target': 'entity_5', 'name': 'team_participates_in_match', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_3', 'target': 'entity_4', 'name': 'team_has_players', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_1', 'target': 'entity_7', 'name': 'match_has_referees', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#
#     {'source': 'entity_6', 'target': 'entity_7', 'name': 'referee_in_matches', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_1', 'target': 'entity_8', 'name': 'match_has_player_stats', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_4', 'target': 'entity_8', 'name': 'player_has_match_stats', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
# ],
#
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'controlheader',
#                      'attribute': [
#                          ('int', 'control_id', 'PK', ''),
#                          ('varchar(50)', 'depot_code', '', ''),
#                          ('varchar(50)', 'machine_code', '', ''),
#                      ]},
#
#         'entity_1': {'name': 'depotcodes',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('varchar(50)', 'depot_code', '', ''),
#                          ('varchar(255)', 'description', '', ''),
#                      ]},
#
#         'entity_2': {'name': 'duty',
#                      'attribute': [
#                          ('int', 'duty_id', 'PK', ''),
#                          ('date', 'duty_date', '', ''),
#                          ('int', 'control_id', 'FK', ''),
#                          ('int', 'duty_year', '', ''),
#                          ('int', 'duty_month', '', ''),
#                          ('int', 'duty_day', '', ''),
#                          ('int', 'duty_wday', '', ''),
#                          ('int', 'duty_week', '', ''),
#                      ]},
#
#         'entity_3': {'name': 'routes',
#                      'attribute': [
#                          ('int', 'route_id', 'PK', ''),
#                          ('varchar(50)', 'from', '', ''),
#                          ('varchar(50)', 'to', '', ''),
#                          ('int', 'stages', '', ''),
#                      ]},
#
#         'entity_4': {'name': 'journey',
#                      'attribute': [
#                          ('int', 'journey_id', 'PK', ''),
#                          ('int', 'duty_id', 'FK', ''),
#                          ('int', 'route_id', 'FK', ''),
#                          ('varchar(10)', 'direction', '', ''),
#                          ('time', 'actual_start_time', '', ''),
#                          ('time', 'scheduled_start_time', '', ''),
#                          ('time', 'finish_time', '', ''),
#                          ('varchar(50)', 'start_stage', '', ''),
#                          ('varchar(50)', 'finish_stage', '', ''),
#                          ('time', 'total_time', '', ''),
#                          ('time', 'start_hour', '', ''),
#                      ]},
#
#         'entity_5': {'name': 'stage',
#                      'attribute': [
#                          ('int', 'stage_id', 'PK', ''),
#                          ('int', 'stage_no', '', ''),
#                          ('time', 'stage_time', '', ''),
#                          ('int', 'journey_id', 'FK', ''),
#                      ]},
#
#         'entity_6': {'name': 'transaction',
#                      'attribute': [
#                          ('int', 'trans_id', 'PK', ''),
#                          ('varchar(50)', 'ticket_id', '', ''),
#                          ('int', 'ticket_type_id', 'FK', ''),
#                          ('int', 'stage_id', 'FK', ''),
#                          ('int', 'prev_mode', 'FK', ''),
#                          ('int', 'prev_route', '', ''),
#                          ('int', 'prev_stage', '', ''),
#                          ('varchar(50)', 'new_ticket_id', '', ''),
#                      ]},
#
#         'entity_7': {'name': 'validations',
#                      'attribute': [
#                          ('int', 'validator_id', 'PK', ''),
#                          ('varchar(50)', 'mcv_id', '', ''),
#                          ('int', 'journey_id', 'FK', ''),
#                          ('int', 'num_of_validations', '', ''),
#                          ('int', 'num_of_retries', '', ''),
#                          ('int', 'num_of_rejections', '', ''),
#                      ]},
#
#         'entity_8': {'name': 'ticketcategory',
#                      'attribute': [
#                          ('varchar(50)', 'category', 'PK', ''),
#                          ('varchar(255)', 'description', '', ''),
#                      ]},
#
#         'entity_9': {'name': 'tickettype',
#                      'attribute': [
#                          ('int', 'ticket_type_id', 'PK', ''),
#                          ('varchar(100)', 'ticket_type_name', '', ''),
#                          ('varchar(50)', 'category', 'FK', ''),
#                          ('int', 'duration', '', ''),
#                      ]},
#
#         'entity_10': {'name': 'mode',
#                       'attribute': [
#                           ('int', 'mode_id', 'PK', ''),
#                           ('varchar(100)', 'mode_name', '', ''),
#                       ]},
#
#         'entity_11': {'name': 'rawdata',
#                       'attribute': [
#                           ('int', 'id', 'PK', ''),
#                           ('varchar(255)', 'string', '', ''),
#                           ('date', 'date', '', ''),
#                           ('int', 'rown', '', ''),
#                       ]},
#
#         'entity_12': {'name': 'import',
#                       'attribute': [
#                           ('varchar(255)', 'filename', 'PK', ''),
#                           ('int', 'num_of_dataset', '', ''),
#                           ('int', 'num_of_control_header', '', ''),
#                           ('int', 'num_of_duty', '', ''),
#                           ('int', 'num_of_journey_start', '', ''),
#                           ('int', 'num_of_journey_end', '', ''),
#                           ('int', 'num_of_stage', '', ''),
#                           ('int', 'num_of_trans', '', ''),
#                           ('int', 'num_of_mcv', '', ''),
#                           ('int', 'num_of_error', '', ''),
#                       ]},
#
#         'entity_13': {'name': 'error',
#                       'attribute': [
#                           ('int', 'error_id', 'PK', ''),
#                           ('text', 'data_string', '', ''),
#                           ('varchar(255)', 'filename', '', ''),
#                       ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_1', 'target': 'entity_0', 'name': 'depotcode_in_controlheader', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_0', 'target': 'entity_2', 'name': 'controlheader_has_duties', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_2', 'target': 'entity_4', 'name': 'duty_has_journeys', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_3', 'target': 'entity_4', 'name': 'route_has_journeys', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_4', 'target': 'entity_5', 'name': 'journey_has_stages', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_4', 'target': 'entity_7', 'name': 'journey_has_validations', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_5', 'target': 'entity_6', 'name': 'stage_has_transactions', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_9', 'target': 'entity_6', 'name': 'tickettype_in_transactions', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_10', 'target': 'entity_6', 'name': 'mode_in_transactions', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_8', 'target': 'entity_9', 'name': 'ticketcategory_has_types', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }


# json_object = {
#     'entity': {
#         'entity_0': {'name': 'student',
#                      'attribute': [
#                          ('int', 'stud_id', 'PK', ''),
#                          ('varchar(100)', 'stfname', '', ''),
#                          ('varchar(100)', 'stlname', '', ''),
#                          ('varchar(100)', 'stcourse', '', ''),
#                          ('varchar(20)', 'styear', '', ''),
#                          ('varchar(15)', 'stcontact', '', ''),
#                          ('varchar(50)', 'stage', '', ''),
#                          ('date', 'stbirthdate', '', ''),
#                          ('varchar(10)', 'stgender', '', ''),
#                      ]},
#
#         'entity_1': {'name': 'courses_offered',
#                      'attribute': [
#                          ('int', 'course_id', 'PK', ''),
#                          ('varchar(255)', 'course_desc', '', ''),
#                          ('int', 'units', '', ''),
#                          ('varchar(255)', 'course_remarks', '', ''),
#                      ]},
#
#         'entity_2': {'name': 'staff',
#                      'attribute': [
#                          ('int', 'staff_id', 'PK', ''),
#                          ('varchar(100)', 'fname', '', ''),
#                          ('varchar(100)', 'lname', '', ''),
#                          ('varchar(15)', 'contact', '', ''),
#                          ('varchar(255)', 'address', '', ''),
#                          ('varchar(10)', 'gender', '', ''),
#                      ]},
#
#         'entity_3': {'name': 'staff_department',
#                      'attribute': [
#                          ('int', 'staff_id', 'PK,FK', ''),
#                          ('varchar(100)', 'course_line', '', ''),
#                      ]},
#
#         'entity_4': {'name': 'reports',
#                      'attribute': [
#                          ('int', 'report_id', 'PK', ''),
#                          ('varchar(100)', 'reports_name', '', ''),
#                          ('varchar(255)', 'student_records', '', ''),
#                          ('varchar(255)', 'transaction_reports', '', ''),
#                      ]},
#
#         'entity_5': {'name': 'student_registration',
#                      'attribute': [
#                          ('int', 'registration_id', 'PK', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('text', 'content', '', ''),
#                          ('date', 'registration_date', '', ''),
#                          ('int', 'stud_id', 'FK', ''),
#                      ]},
#
#         'entity_6': {'name': 'project_transactions',
#                      'attribute': [
#                          ('int', 'transaction_id', 'PK', ''),
#                          ('varchar(100)', 'transaction_name', '', ''),
#                          ('int', 'stud_id', 'FK', ''),
#                          ('int', 'staff_id', 'FK', ''),
#                          ('date', 'transaction_date', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#     {'source': 'entity_0', 'target': 'entity_5', 'name': '', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_0', 'target': 'entity_6', 'name': '', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_2', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or one'},
#
#     {'source': 'entity_2', 'target': 'entity_6', 'name': '', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_1', 'target': 'entity_3', 'name': '', 'type': 'non-identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_0', 'target': 'entity_4', 'name': '', 'type': 'non-identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_5', 'target': 'entity_4', 'name': '', 'type': 'non-identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_6', 'target': 'entity_4', 'name': '', 'type': 'non-identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'customer',
#                      'attribute': [
#                          ('int', 'customer_id', 'PK', ''),
#                          ('varchar(100)', 'first_name', '', ''),
#                          ('varchar(100)', 'last_name', '', ''),
#                          ('varchar(100)', 'company_name', '', ''),
#                          ('varchar(15)', 'phone', '', ''),
#                          ('varchar(100)', 'email', '', ''),
#                          ('varchar(255)', 'address', '', ''),
#                          ('varchar(100)', 'city', '', ''),
#                          ('varchar(50)', 'state', '', ''),
#                          ('varchar(20)', 'zip', '', ''),
#                          ('varchar(100)', 'country', '', ''),
#                      ]},
#
#         'entity_1': {'name': 'employee',
#                      'attribute': [
#                          ('int', 'employee_id', 'PK', ''),
#                          ('varchar(100)', 'first_name', '', ''),
#                          ('varchar(100)', 'last_name', '', ''),
#                          ('varchar(100)', 'email', '', ''),
#                          ('varchar(15)', 'phone', '', ''),
#                          ('varchar(100)', 'job_title', '', ''),
#                          ('decimal(10,2)', 'salary', '', ''),
#                          ('int', 'department_id', 'FK', ''),
#                      ]},
#
#         'entity_2': {'name': 'department',
#                      'attribute': [
#                          ('int', 'department_id', 'PK', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('varchar(255)', 'location', '', ''),
#                      ]},
#
#         'entity_3': {'name': 'project',
#                      'attribute': [
#                          ('int', 'project_id', 'PK', ''),
#                          ('varchar(100)', 'project_name', '', ''),
#                          ('date', 'start_date', '', ''),
#                          ('date', 'end_date', '', ''),
#                          ('varchar(255)', 'status', '', ''),
#                          ('int', 'department_id', 'FK', ''),
#                      ]},
#
#         'entity_4': {'name': 'product',
#                      'attribute': [
#                          ('int', 'product_id', 'PK', ''),
#                          ('varchar(100)', 'product_name', '', ''),
#                          ('varchar(255)', 'description', '', ''),
#                          ('decimal(10,2)', 'unit_price', '', ''),
#                          ('int', 'stock_qty', '', ''),
#                      ]},
#
#         'entity_5': {'name': 'service',
#                      'attribute': [
#                          ('int', 'service_id', 'PK', ''),
#                          ('varchar(100)', 'service_name', '', ''),
#                          ('varchar(255)', 'description', '', ''),
#                          ('decimal(10,2)', 'hourly_rate', '', ''),
#                      ]},
#
#         'entity_6': {'name': 'contract',
#                      'attribute': [
#                          ('int', 'contract_id', 'PK', ''),
#                          ('date', 'contract_date', '', ''),
#                          ('varchar(255)', 'details', '', ''),
#                          ('int', 'customer_id', 'FK', ''),
#                          ('int', 'department_id', 'FK', ''),
#                      ]},
#
#         'entity_7': {'name': 'quote',
#                      'attribute': [
#                          ('int', 'quote_id', 'PK', ''),
#                          ('date', 'quote_date', '', ''),
#                          ('varchar(255)', 'details', '', ''),
#                          ('int', 'customer_id', 'FK', ''),
#                          ('int', 'employee_id', 'FK', ''),
#                      ]},
#
#         'entity_8': {'name': 'sale',
#                      'attribute': [
#                          ('int', 'sale_id', 'PK', ''),
#                          ('date', 'sale_date', '', ''),
#                          ('decimal(10,2)', 'amount', '', ''),
#                          ('int', 'customer_id', 'FK', ''),
#                          ('int', 'product_id', 'FK', ''),
#                      ]},
#
#         'entity_9': {'name': 'invoice',
#                      'attribute': [
#                          ('int', 'invoice_id', 'PK', ''),
#                          ('date', 'invoice_date', '', ''),
#                          ('decimal(10,2)', 'total_amount', '', ''),
#                          ('int', 'customer_id', 'FK', ''),
#                          ('int', 'sale_id', 'FK', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_2', 'target': 'entity_1', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_2', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_2', 'target': 'entity_6', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_0', 'target': 'entity_6', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_0', 'target': 'entity_7', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_1', 'target': 'entity_7', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_0', 'target': 'entity_8', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_4', 'target': 'entity_8', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_0', 'target': 'entity_9', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_8', 'target': 'entity_9', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'exactly one'},
#
#         {'source': 'entity_3', 'target': 'entity_5', 'name': '', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }


# json_object = {
#     'entity': {
#         'entity_0': {'name': 'votergroup',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('varchar(70)', 'name', '', ''),
#                          ('text', 'description', '', ''),
#                          ('int', 'voting_power', '', ''),
#                          ('datetime', 'creation_date', '', ''),
#                          ('bit', 'is_active', '', ''),
#                      ]},
#
#         'entity_1': {'name': 'voter',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('varchar(200)', 'email', '', ''),
#                          ('varchar(70)', 'first_name', '', ''),
#                          ('varchar(70)', 'last_name', '', ''),
#                          ('int', 'voter_group_id', 'FK', ''),
#                          ('datetime', 'registration_date', '', ''),
#                          ('bit', 'is_active', '', ''),
#                      ]},
#
#         'entity_2': {'name': 'voting',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('varchar(140)', 'subject', '', ''),
#                          ('text', 'description', '', ''),
#                          ('datetime', 'active_from', '', ''),
#                          ('datetime', 'active_to', '', ''),
#                          ('bit', 'is_allowed_for_all', '', ''),
#                          ('int', 'status_id', 'FK', ''),
#                      ]},
#
#         'entity_3': {'name': 'votingoption',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('int', 'voting_id', 'FK', ''),
#                          ('varchar(100)', 'text', '', ''),
#                          ('int', 'order_index', '', ''),
#                      ]},
#
#         'entity_4': {'name': 'votervote',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('int', 'voter_id', 'FK', ''),
#                          ('int', 'voting_id', 'FK', ''),
#                          ('int', 'voting_option_id', 'FK', ''),
#                          ('datetime', 'voted_date', '', ''),
#                          ('int', 'weight', '', ''),
#                      ]},
#
#         'entity_5': {'name': 'allowedvotergroup',
#                      'attribute': [
#                          ('int', 'voting_id', 'FK', ''),
#                          ('int', 'voter_group_id', 'FK', ''),
#                      ]},
#
#         'entity_6': {'name': 'votingstatus',
#                      'attribute': [
#                          ('int', 'id', 'PK', ''),
#                          ('varchar(70)', 'name', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_0', 'target': 'entity_5', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_2', 'target': 'entity_5', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_2', 'target': 'entity_3', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#
#         {'source': 'entity_2', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_3', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_1', 'target': 'entity_4', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_6', 'target': 'entity_2', 'name': '', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }


# json_object = {
#     'entity': {
#         'entity_0': {'name': 'books',
#                      'attribute': [
#                          ('int', 'isbn', 'PK', ''),
#                          ('varchar(150)', 'title', '', ''),
#                          ('varchar(100)', 'auth_no', '', ''),
#                          ('decimal(10,2)', 'price', '', ''),
#                          ('varchar(50)', 'category', '', ''),
#                          ('varchar(50)', 'edition', '', ''),
#                          ('int', 'publisher_id', 'FK', ''),
#                      ]},
#
#         'entity_1': {'name': 'publisher',
#                      'attribute': [
#                          ('int', 'publisher_id', 'PK', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('int', 'year_of_publication', '', ''),
#                      ]},
#
#         'entity_2': {'name': 'readers',
#                      'attribute': [
#                          ('int', 'user_id', 'PK', ''),
#                          ('varchar(100)', 'first_name', '', ''),
#                          ('varchar(100)', 'last_name', '', ''),
#                          ('varchar(100)', 'email', '', ''),
#                          ('varchar(15)', 'phone_no', '', ''),
#                          ('varchar(255)', 'address', '', ''),
#                          ('varchar(100)', 'name', '', ''),
#                      ]},
#
#         'entity_3': {'name': 'staff',
#                      'attribute': [
#                          ('int', 'staff_id', 'PK', ''),
#                          ('varchar(100)', 'name', '', ''),
#                      ]},
#
#         'entity_4': {'name': 'reports',
#                      'attribute': [
#                          ('int', 'reg_no', 'PK', ''),
#                          ('int', 'book_no', 'FK', ''),
#                          ('int', 'user_id', 'FK', ''),
#                          ('varchar(50)', 'issue_or_return', '', ''),
#                      ]},
#
#         'entity_5': {'name': 'authentication_system',
#                      'attribute': [
#                          ('varchar(50)', 'login_id', 'PK', ''),
#                          ('varchar(100)', 'password', '', ''),
#                      ]},
#
#         'entity_6': {'name': 'reservation',
#                      'attribute': [
#                          ('int', 'reserve_id', 'PK', ''),
#                          ('int', 'user_id', 'FK', ''),
#                          ('int', 'isbn', 'FK', ''),
#                          ('date', 'reserve_date', '', ''),
#                          ('date', 'return_date', '', ''),
#                          ('date', 'due_date', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_3', 'target': 'entity_4', 'name': 'staff_manages_reports', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_3', 'target': 'entity_5', 'name': 'staff_authentication', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'exactly one'},
#
#         {'source': 'entity_3', 'target': 'entity_0', 'name': 'staff_maintains_books', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_3', 'target': 'entity_2', 'name': 'staff_tracks_readers', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_2', 'target': 'entity_6', 'name': 'reader_reserves_books', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_0', 'target': 'entity_6', 'name': 'book_reserved_in_reservation', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_1', 'target': 'entity_0', 'name': 'publisher_publishes_books', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_2', 'target': 'entity_4', 'name': 'reader_generates_reports', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_0', 'target': 'entity_4', 'name': 'book_in_reports', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }


# json_object = {
#     'entity': {
#         'entity_0': {'name': 'patient',
#                      'attribute': [
#                          ('int', 'p_id', 'PK', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('int', 'age', '', ''),
#                          ('varchar(10)', 'gender', '', ''),
#                          ('varchar(15)', 'mob_no', '', ''),
#                          ('date', 'dob', '', ''),
#                      ]},
#
#         'entity_1': {'name': 'doctor',
#                      'attribute': [
#                          ('int', 'd_id', 'PK', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('varchar(100)', 'dept', '', ''),
#                          ('varchar(100)', 'qualification', '', ''),
#                          ('varchar(15)', 'mob_no', '', ''),
#                          ('varchar(255)', 'address', '', ''),
#                          ('varchar(50)', 'state', '', ''),
#                          ('varchar(50)', 'city', '', ''),
#                          ('varchar(10)', 'pin_no', '', ''),
#                      ]},
#
#         'entity_2': {'name': 'nurse',
#                      'attribute': [
#                          ('int', 'e_id', 'PK', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('varchar(10)', 'sex', '', ''),
#                          ('decimal(10,2)', 'salary', '', ''),
#                          ('varchar(15)', 'mob_no', '', ''),
#                          ('varchar(255)', 'address', '', ''),
#                      ]},
#
#         'entity_3': {'name': 'receptionist',
#                      'attribute': [
#                          ('int', 'e_id', 'PK', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('varchar(10)', 'sex', '', ''),
#                          ('decimal(10,2)', 'salary', '', ''),
#                      ]},
#
#         'entity_4': {'name': 'rooms',
#                      'attribute': [
#                          ('int', 'r_id', 'PK', ''),
#                          ('varchar(50)', 'type', '', ''),
#                          ('int', 'capacity', '', ''),
#                          ('varchar(50)', 'availability', '', ''),
#                      ]},
#
#         'entity_5': {'name': 'test_report',
#                      'attribute': [
#                          ('int', 't_id', 'PK', ''),
#                          ('int', 'p_id', 'FK', ''),
#                          ('int', 'r_id', 'FK', ''),
#                          ('varchar(50)', 'test_type', '', ''),
#                          ('varchar(255)', 'result', '', ''),
#                      ]},
#
#         'entity_6': {'name': 'bills',
#                      'attribute': [
#                          ('int', 'b_id', 'PK', ''),
#                          ('int', 'p_id', 'FK', ''),
#                          ('decimal(10,2)', 'amount', '', ''),
#                      ]},
#
#         'entity_7': {'name': 'records',
#                      'attribute': [
#                          ('int', 'record_no', 'PK', ''),
#                          ('int', 'app_no', '', ''),
#                          ('int', 'p_id', 'FK', ''),
#                      ]},
#
#         'entity_8': {'name': 'employee',
#                      'attribute': [
#                          ('int', 'e_id', 'PK', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('varchar(10)', 'sex', '', ''),
#                          ('decimal(10,2)', 'salary', '', ''),
#                          ('varchar(15)', 'mob_no', '', ''),
#                          ('varchar(255)', 'address', '', ''),
#                          ('varchar(50)', 'state', '', ''),
#                          ('varchar(50)', 'city', '', ''),
#                          ('varchar(10)', 'pin_no', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': 'patient_consults_doctor', 'type': 'non-identifying',
#          'source_cardinality': 'one or more', 'target_cardinality': 'one or more'},
#
#         {'source': 'entity_0', 'target': 'entity_6', 'name': 'patient_pays_bills', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#
#         {'source': 'entity_0', 'target': 'entity_5', 'name': 'patient_has_test_reports', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#
#         {'source': 'entity_1', 'target': 'entity_4', 'name': 'doctor_assigned_to_rooms', 'type': 'non-identifying',
#          'source_cardinality': 'one or more', 'target_cardinality': 'exactly one'},
#
#         {'source': 'entity_0', 'target': 'entity_4', 'name': 'patient_assigned_room', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'exactly one'},
#
#         {'source': 'entity_2', 'target': 'entity_4', 'name': 'nurse_governs_rooms', 'type': 'non-identifying',
#          'source_cardinality': 'one or more', 'target_cardinality': 'one or more'},
#
#         {'source': 'entity_3', 'target': 'entity_7', 'name': 'receptionist_maintains_records', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#
#         {'source': 'entity_8', 'target': 'entity_2', 'name': 'employee_is_nurse', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_8', 'target': 'entity_3', 'name': 'employee_is_receptionist', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }


# json_object = {
#     'entity': {
#         'entity_0': {'name': 'user',
#                      'attribute': [
#                          ('int', 'user_id', 'PK', ''),
#                          ('varchar(100)', 'user_name', '', ''),
#                          ('varchar(100)', 'user_mobile', '', ''),
#                          ('varchar(100)', 'user_email', '', ''),
#                          ('varchar(255)', 'user_address', '', ''),
#                      ]},
#
#         'entity_1': {'name': 'login',
#                      'attribute': [
#                          ('int', 'login_role_id', 'FK', ''),
#                          ('int', 'user_id', 'FK', ''),
#                          ('varchar(100)', 'login_username', '', ''),
#                          ('varchar(100)', 'user_password', '', ''),
#                      ]},
#
#         'entity_2': {'name': 'roles',
#                      'attribute': [
#                          ('int', 'role_id', 'PK', ''),
#                          ('varchar(100)', 'role_name', '', ''),
#                          ('varchar(255)', 'role_desc', '', ''),
#                      ]},
#
#         'entity_3': {'name': 'permission',
#                      'attribute': [
#                          ('int', 'role_id', 'FK', ''),
#                          ('int', 'per_role_id', 'PK', ''),
#                          ('varchar(100)', 'per_name', '', ''),
#                          ('varchar(100)', 'per_module', '', ''),
#                      ]},
#
#         'entity_4': {'name': 'student',
#                      'attribute': [
#                          ('int', 'stu_id', 'PK', ''),
#                          ('varchar(100)', 'stu_name', '', ''),
#                          ('varchar(100)', 'stu_pass', '', ''),
#                          ('varchar(15)', 'stu_mobile', '', ''),
#                          ('varchar(255)', 'stu_add', '', ''),
#                          ('varchar(100)', 'stu_email', '', ''),
#                      ]},
#
#         'entity_5': {'name': 'course',
#                      'attribute': [
#                          ('int', 'crs_id', 'PK', ''),
#                          ('varchar(100)', 'crs_name', '', ''),
#                          ('varchar(255)', 'crs_desc', '', ''),
#                          ('varchar(50)', 'crs_type', '', ''),
#                          ('int', 'crs_stu_id', 'FK', ''),
#                      ]},
#
#         'entity_6': {'name': 'collage',
#                      'attribute': [
#                          ('int', 'col_id', 'PK', ''),
#                          ('varchar(255)', 'col_desc', '', ''),
#                          ('varchar(50)', 'col_type', '', ''),
#                      ]},
#
#         'entity_7': {'name': 'registration',
#                      'attribute': [
#                          ('int', 'reg_id', 'PK', ''),
#                          ('int', 'reg_stu_id', 'FK', ''),
#                          ('varchar(255)', 'reg_desc', '', ''),
#                          ('date', 'reg_date', '', ''),
#                          ('varchar(50)', 'reg_type', '', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': 'user_has_login', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'exactly one'},
#
#         {'source': 'entity_1', 'target': 'entity_2', 'name': 'login_has_role', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'exactly one'},
#
#         {'source': 'entity_2', 'target': 'entity_3', 'name': 'role_has_permissions', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_0', 'target': 'entity_5', 'name': 'user_manages_course', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_5', 'target': 'entity_6', 'name': 'course_belongs_to_collage', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'exactly one'},
#
#         {'source': 'entity_4', 'target': 'entity_5', 'name': 'student_enrolls_in_course', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_4', 'target': 'entity_7', 'name': 'student_has_registration', 'type': 'identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#         {'source': 'entity_5', 'target': 'entity_7', 'name': 'course_linked_to_registration', 'type': 'non-identifying',
#          'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#     ],
#
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'bank',
#                      'attribute': [
#                          ('int', 'bank_code', 'PK', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('varchar(255)', 'address', '', ''),
#                      ]},
#
#         'entity_1': {'name': 'branch',
#                      'attribute': [
#                          ('int', 'branch_id', 'PK', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('varchar(255)', 'address', '', ''),
#                          ('int', 'bank_code', 'FK', ''),
#                      ]},
#
#         'entity_2': {'name': 'customer',
#                      'attribute': [
#                          ('int', 'cust_id', 'PK', ''),
#                          ('varchar(100)', 'name', '', ''),
#                          ('varchar(255)', 'address', '', ''),
#                          ('varchar(15)', 'phone', '', ''),
#                      ]},
#
#         'entity_3': {'name': 'account',
#                      'attribute': [
#                          ('int', 'account_no', 'PK', ''),
#                          ('varchar(50)', 'acc_type', '', ''),
#                          ('decimal(15,2)', 'balance', '', ''),
#                          ('int', 'branch_id', 'FK', ''),
#                          ('int', 'cust_id', 'FK', ''),
#                      ]},
#
#         'entity_4': {'name': 'loan',
#                      'attribute': [
#                          ('int', 'loan_id', 'PK', ''),
#                          ('varchar(50)', 'loan_type', '', ''),
#                          ('decimal(15,2)', 'amount', '', ''),
#                          ('int', 'branch_id', 'FK', ''),
#                          ('int', 'cust_id', 'FK', ''),
#                      ]},
#     },
#     'cluster': {
#     },
#     'relation': [
#     {'source': 'entity_0', 'target': 'entity_1', 'name': 'bank_has_branches', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'one or more'},
#
#     {'source': 'entity_1', 'target': 'entity_3', 'name': 'branch_maintains_accounts', 'type': 'non-identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_1', 'target': 'entity_4', 'name': 'branch_offers_loans', 'type': 'non-identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_2', 'target': 'entity_3', 'name': 'customer_holds_accounts', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
#
#     {'source': 'entity_2', 'target': 'entity_4', 'name': 'customer_availed_loans', 'type': 'identifying',
#      'source_cardinality': 'exactly one', 'target_cardinality': 'zero or more'},
# ],
#
#     'difficulty': 'easy',
#     'diagram_type': 'ER'
# }

# attribute format: type, name, PK or FK, comment
# relation:
#   type: identifying, non-identitfying
#   cardinality: zero or one, zero or more, one or more, exactly one


# count = 1
# save_file = './dataset/SAD/ER/ER_diagram_%s.json' % count
# while os.path.exists(save_file):
#     count += 1
#     save_file = './dataset/SAD/ER/ER_diagram_%s.json' % count
# with open(save_file, 'w') as file:
#     json.dump(json_object, file, indent=4)
