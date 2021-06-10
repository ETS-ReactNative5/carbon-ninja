import os
from flask import jsonify
import mysql.connector as mariadb

class MariaDBService():
  def __init__(self):
    self.conn = mariadb.connect(
      user=os.environ.get("MYSQL_USER", "admin"),
   #   password=os.environ["MYSQL_PASSWORD"],
      password='pw'
   #  host=os.environ.get("MYSQL_HOST", "mariadb"),
      host='localhost'
      port=3306,
      database=os.environ.get("MYSQL_DATABASE", "db")
    )

  def get_all_foods(self):
    try:
      # Get cursor and query MariaDB - eager loading
      cur = self.conn.cursor(buffered=True)
      cur.execute("SELECT food_product FROM food_production;")
      
      # Add each row to list
      foods = []
      for food_product in cur:
          foods.append(food_product[0])
      
      # return results
      return foods

    except mariadb.Error as e:
      print(f"Error while connection to Mariadb: {e}")
    except Exception as e:
      print(f"Error retrieving foods: {e}")

    return []

  def get_food_emissions(self, food_names):
    try:

      dict = {} # empty dict
      total_emissions # keep track of total emissions
      for food_name in food_names:
        print("Getting emissions for food: " + food_name)
        cur = self.conn.cursor()
        query = "SELECT Total_emissions FROM food_production WHERE Food_product = %s;"
        cur.execute(query, (food_name,))
        emissions = cur.fetchone()
        emissions = (float(emissions[0]))        
        total_emissions = total_emissions + emissions
        print(food_name + " emissions: " + emissions)
        print("Total emissions: " + total_emissions)
        dict[food_name] = emissions

      # return emissions
      print(dict)
      return emissions

    except mariadb.Error as e:
      print(f"Error while connection to Mariadb: {e}")
    except Exception as e:
      print(f"Error retrieving emissions: {e}")

    # error
    return []

