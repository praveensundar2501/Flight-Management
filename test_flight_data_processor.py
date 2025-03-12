import unittest
from flight_data_processor import FlightDataProcessor



class TestFlightDataProcessing(unittest.TestCase):
    """
    Testcase Flight Processing Data
    """

    def setUp(self):
        """
        Setup  a flight data.
        """
        self.flight_data = [
                        {"flight_number": "AZ001", "departure_time": "2025-02-19 15:30",
                        "arrival_time": "2025-02-20 03:45", "status": "ON_TIME"},
                        {"flight_number": "AZ002", "departure_time": "2025-02-21 11:00",
                        "arrival_time": "2025-02-21 16:00", "status": "DELAYED"},]
        self.processor = FlightDataProcessor(self.flight_data)
    
    def test_add_flight(self):

        """
        Test adding a flight.
        """
        new_flight = {"flight_number": "AZ003", "departure_time": "2025-02-22 10:00", 
                       "arrival_time": "2025-02-22 12:00", "status": "ON_TIME"}
        
        result = self.processor.add_flight(new_flight)
        self.assertEqual(len(result), 3)

    def test_remove_flight(self):
        """
        Test removing a flight.
        """
        result =self.processor.remove_flight("AZ001")
        self.assertEqual(len(result), 1)

    def test_flights_by_status(self):
        """
        Test filtering flights by status.
        """
        on_time_flights = self.processor.flights_by_status("ON_TIME")
        self.assertEqual(len(on_time_flights), 1)
        self.assertEqual(on_time_flights[0]["flight_number"], "AZ001")

    def test_get_longest_flight(self):
        """
        Test getting the longest flight.
        """
        longest_flight = self.processor.get_longest_flight()
        self.assertEqual(longest_flight["flight_number"], "AZ001")
    
    def test_update_flight_status(self):
        """
        Test updating the status of a flight.
        """
        result = self.processor.update_flight_status("AZ001", "CANCELLED")
        updated_flight = [flight for flight in result if flight["flight_number"] == "AZ001"]
        self.assertEqual(updated_flight[0]["status"], "CANCELLED")


if __name__ == "__main__":
    unittest.main()