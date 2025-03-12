from datetime import datetime
class FlightDataProcessor:

    def __init__(self, flight_data):
        """
        To setup the flight data in format of list of dict
        """

        self.flight_data = flight_data if flight_data else []

    def add_flight(self , new_record):
        """
        To add new flight detail to flight data
        """
        if new_record:
            for flights in self.flight_data:
                if flights['flight_number'] == new_record['flight_number']:
                    raise ValueError(f"Flight {new_record['flight_number']} already exists.")
            self.flight_data.append(new_record)
            return self.flight_data
    
    def remove_flight(self, flight_number):
        """
        To remove the flight by flight number
        """
        flight_data = [ flights  for flights in self.flight_data if flights['flight_number'] != flight_number]
        return flight_data
    
    def flights_by_status(self, flight_status):
        """
        To fi;ter the flight status
        """
        flight_data = [flight for flight in self.flight_data if flight['status'] == flight_status]
        return flight_data
    
    def get_longest_flight(self):
        """
        To get longest flight details from flight data
        """
        if not self.flight_data:
            return None
        for flight in self.flight_data:
            dep_time = datetime.strptime(flight["departure_time"], "%Y-%m-%d %H:%M")
            arr_time = datetime.strptime(flight["arrival_time"], "%Y-%m-%d %H:%M")
            flight["duration_minutes"] = int((arr_time - dep_time).total_seconds() // 60)
        longest_flight = self.flight_data[0]
        for long in self.flight_data[1:]:
            if long["duration_minutes"] > longest_flight["duration_minutes"]:
                longest_flight = long
        return longest_flight
    
    def update_flight_status(self, flight_number, status):
        """
        To Update the flight status using on given flight number
        """
        for flight in self.flight_data:
            if flight['flight_number']==flight_number:
                flight['status']= status
            return self.flight_data
        raise ValueError(f"Flight {flight_number} not found.")







# # Testing FlightDataProcessor class

# # Initialize test data with a default flight record
# test_data = [
#     {"flight_number": "AZ001", "departure_time": "2025-02-19 15:30",
#      "arrival_time": "2025-02-20 03:45", "status": "ON_TIME"}
# ]

# # Create an instance of FlightDataProcessor with test data
# flight = FlightDataProcessor(test_data)

# # New flight record to be added
# new_flight_data = {
#     "flight_number": "AZ002", "departure_time": "2025-02-21 11:00",
#     "arrival_time": "2025-02-21 16:00", "status": "DELAYED"
# }

# # Adding a new flight record
# print("#" * 5 + " Adding a New Flight " + "#" * 15)
# print(flight.add_flight(new_flight_data))

# # Removing a flight record
# print("#" * 5 + " Removing a Flight " + "#" * 15) 
# flight_number = 'AZ001'  # Set the flight number to remove
# print(flight.remove_flight(flight_number))

# # Finding the longest flight based on duration
# print("#" * 5 + " Finding the Longest Flight " + "#" * 15)
# print(flight.get_longest_flight())

# # Updating the status of a flight
# print("#" * 5 + " Updating Flight Status " + "#" * 15)

# # Define the flight number and the new status to be updated
# flight_number = 'AZ001'
# status = 'CANCELLED'

# print(flight.update_flight_status(flight_number, status))