from product import Product
def simple_data():
  product_list = []
  data = [['Smartphone A', '0.194', '15.09', '7.59', '0.83', '3799', '4'],
          ['Smartphone B', '0.237', '17.09', '6.59', '0.8', '2599', '2'],
          ['Smartphone C', '0.196', '16.49', '7.79', '0.9', '649', '5'],
          ['TV 55', '16', '123.2', '74.6', '22.9', '2799', '5'],
          ['TV 65', '22', '145.1', '87.1', '28.2', '2999', '3'],
          ['TV 43', '9', '96.6', '60', '20.6', '2299', '6'],
          ['Washing machine A', '76', '54', '63', '88', '1799', '2'],
          ['Washing machine B', '60', '50', '64', '88', '1099', '4'],
          ['Washing machine C', '72', '64', '64', '87', '1399', '7'],
          ['Hairdryer A', '1.77', '34.5', '36', '11.5', '1129', '1'],
          ['Hairdryer B', '1.1', '33.2', '10.6', '24.7', '369', '4'],
          ['Hairdryer C', '2.4', '36', '30', '12', '649', '6'],
          ['Dryer A', '52', '69', '65', '88', '2649', '3'],
          ['Dryer B', '51', '68', '63', '89', '1999', '5'],
          ['Dryer C', '51', '71', '64', '89', '2099', '8'],
          ['Headphones A', '0.223', '19', '17', '3.5', '469', '2'],
          ['Headphones B', '0.51', '20', '18', '2', '199', '3'],
          ['Headphones C', '0.33', '20', '21', '5', '259', '5'],
          ['Console A', '4.5', '39', '10.4', '26', '3109', '4'],
          ['Console B', '4.45', '15.1', '30.6', '15.9', '2599', '7'],
          ['Console C', '8', '23.2', '54.6', '22.9', '2199', '9'],
          ['Camera A', '0.451', '11.2', '8.6', '5.9', '4219', '2'],
          ['Camera B', '0.851', '11.6', '8.8', '5.9', '3089', '3'],
          ['Camera C', '0.591', '13.2', '9.6', '6.9', '2799', '3'],
          ['Loudspeaker A', '2.5', '14.6', '24.6', '15.5', '1199', '4'],
          ['Loudspeaker B', '1.85', '16.2', '12', '12', '999', '5'],
          ['Loudspeaker C', '0.97', '14', '11.6', '11', '1679', '6']]
  
  for product in data:
      product_list.append(Product(product[0], float(product[1]), float(product[2]), float(product[3]), float(product[4]), int(product[5])))
  return product_list