from carApi import get_makes
from database import insert_car_data

def main():
    print("Please enter the year between 1990 to 2025 to get the car data:")
    year = int(input())
    if year == "":
        print("Please enter a valid year")
    elif (year>2025 or year<1990):
        print("Please enter a year between 1990 to 2025")
    else:
        car_data = get_makes(str(year))
        if car_data:
            insert_car_data(car_data)
        else:
            print("No car data found for the given year")

if __name__ == "__main__":
    main()