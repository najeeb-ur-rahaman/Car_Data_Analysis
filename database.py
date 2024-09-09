import psycopg2
import os
from dotenv import load_dotenv

conn = None
cur = None

# Load environment variables from.env file
load_dotenv()

def insert_car_data(car_data):
    try:
        print("Establishing connection to the PostgreSQL database...")
        conn = psycopg2.connect(
            host = os.getenv('hostname'),
            dbname = os.getenv('database'),
            user = os.getenv('username'),
            password = os.getenv('password'),
            port = os.getenv('port'))

        cur = conn.cursor()

        cur.execute('DROP TABLE IF EXISTS car_data')

        create_table_query = """ CREATE TABLE IF NOT EXISTS car_data(
                                    id INT,
                                    make_model_id INT,
                                    year INT,
                                    msrp DECIMAL(10,2),
                                    invoice DECIMAL(10,2),
                                    created TIMESTAMP,
                                    modified TIMESTAMP,
                                    make_id INT,
                                    make_name VARCHAR(25),
                                    mileage_fuel_tank_capacity DECIMAL(5,2),
                                    mileage_combined_mpg INT,
                                    mileage_epa_city_mpg INT,
                                    mileage_epa_highway_mpg INT,
                                    mileage_range_city INT,
                                    mileage_range_highway INT,
                                    engine_size DECIMAL(5,2),
                                    engine_horsepower_hp INT,
                                    engine_horsepower_rpm INT,
                                    engine_torque_ft_lbs INT,
                                    engine_torque_rpm INT,
                                    engine_valves INT,
                                    body_doors INT,
                                    body_length VARCHAR(10),
                                    body_width VARCHAR(10),
                                    body_seats INT,
                                    body_height VARCHAR(10),
                                    body_wheel_base VARCHAR(10)
                                    )"""

        cur.execute(create_table_query)
        print("Table created successfully")

        # Execute the query
        insert_query = """ INSERT INTO car_data(
                            id,
                            make_model_id,
                            year,
                            msrp,
                            invoice,
                            created,
                            modified,
                            make_id,
                            make_name,
                            mileage_fuel_tank_capacity,
                            mileage_combined_mpg,
                            mileage_epa_city_mpg,
                            mileage_epa_highway_mpg,
                            mileage_range_city,
                            mileage_range_highway,
                            engine_size,
                            engine_horsepower_hp,
                            engine_horsepower_rpm,
                            engine_torque_ft_lbs,
                            engine_torque_rpm,
                            engine_valves,
                            body_doors,
                            body_length,
                            body_width,
                            body_seats,
                            body_height,
                            body_wheel_base
                        ) VALUES (
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                        )"""

        # Insert data into the table
        for value in car_data:
            if value is not None:
                data = (value["id"],
                        value["make_model_id"],
                        value["year"],
                        value["msrp"],
                        value["invoice"],
                        value["created"],
                        value["modified"],
                        value["make_model"]["make"]["id"],
                        value["make_model"]["make"]["name"],
                        value["make_model_trim_mileage"]["fuel_tank_capacity"],
                        value["make_model_trim_mileage"]["combined_mpg"],
                        value["make_model_trim_mileage"]["epa_city_mpg"],
                        value["make_model_trim_mileage"]["epa_highway_mpg"],
                        value["make_model_trim_mileage"]["range_city"],
                        value["make_model_trim_mileage"]["range_highway"],
                        value["make_model_trim_engine"]["size"],
                        value["make_model_trim_engine"]["horsepower_hp"],
                        value["make_model_trim_engine"]["horsepower_rpm"],
                        value["make_model_trim_engine"]["torque_ft_lbs"],
                        value["make_model_trim_engine"]["torque_rpm"],
                        value["make_model_trim_engine"]["valves"],
                        value["make_model_trim_body"]["doors"],
                        value["make_model_trim_body"]["length"],
                        value["make_model_trim_body"]["width"],
                        value["make_model_trim_body"]["seats"],
                        value["make_model_trim_body"]["height"],
                        value["make_model_trim_body"]["wheel_base"]
                        )
                cur.execute(insert_query, data)
            else:
                print("Skipping row with missing values.")

        conn.commit()
        print("Data inserted successfully into the database.")

    except Exception as e:
        print(e)
        print(value)
        print("Error occurred while inserting data into the database.")
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()