"""
Flight Search API - A simple Python application for searching flights
"""

class FlightSearch:
    def __init__(self):
        # Sample flight database
        self.flights = [
            {
                "id": "FL001",
                "origin": "NYC",
                "destination": "LAX",
                "departure_time": "08:00",
                "arrival_time": "11:30",
                "price": 350.00,
                "available_seats": 45,
                "airline": "SkyWings"
            },
            {
                "id": "FL002",
                "origin": "LAX",
                "destination": "NYC",
                "departure_time": "14:00",
                "arrival_time": "22:30",
                "price": 375.00,
                "available_seats": 32,
                "airline": "SkyWings"
            },
            {
                "id": "FL003",
                "origin": "CHI",
                "destination": "MIA",
                "departure_time": "10:15",
                "arrival_time": "14:00",
                "price": 280.00,
                "available_seats": 58,
                "airline": "AirGlobe"
            },
            {
                "id": "FL004",
                "origin": "NYC",
                "destination": "LON",
                "departure_time": "19:45",
                "arrival_time": "08:30",
                "price": 620.00,
                "available_seats": 12,
                "airline": "TransAtlantic"
            },
            {
                "id": "FL005",
                "origin": "NYC",
                "destination": "LAX",
                "departure_time": "16:30",
                "arrival_time": "20:00",
                "price": 410.00,
                "available_seats": 0,
                "airline": "AirGlobe"
            }
        ]
    
    def search_flights(self, origin=None, destination=None, max_price=None):
        """
        Search for flights based on origin, destination, and maximum price
        
        Args:
            origin (str): Origin airport code
            destination (str): Destination airport code
            max_price (float): Maximum price for the flight
            
        Returns:
            list: List of flights matching the search criteria
        """
        results = []
        
        for flight in self.flights:
            match = True
            
            if origin and flight["origin"] != origin:
                match = False
            
            if destination and flight["destination"] != destination:
                match = False
            
            if max_price and flight["price"] > max_price:
                match = False
            
            if match:
                results.append(flight)
        
        return results
    
    def get_flight_by_id(self, flight_id):
        """
        Get flight details by flight ID
        
        Args:
            flight_id (str): Flight ID to search for
            
        Returns:
            dict: Flight details if found, None otherwise
        """
        for flight in self.flights:
            if flight["id"] == flight_id:
                return flight
        return None
    
    def check_availability(self, flight_id):
        """
        Check if a flight has available seats
        
        Args:
            flight_id (str): Flight ID to check
            
        Returns:
            bool: True if seats are available, False otherwise
        """
        flight = self.get_flight_by_id(flight_id)
        if flight and flight["available_seats"] > 0:
            return True
        return False
    
    def get_airlines(self):
        """
        Get a list of all airlines
        
        Returns:
            list: List of unique airline names
        """
        airlines = set()
        for flight in self.flights:
            airlines.add(flight["airline"])
        return list(airlines)


# Example usage
if __name__ == "__main__":
    search = FlightSearch()
    
    # Search for flights from NYC to LAX
    results = search.search_flights(origin="NYC", destination="LAX")
    print(f"Found {len(results)} flights from NYC to LAX:")
    for flight in results:
        print(f"Flight {flight['id']}: {flight['departure_time']} - {flight['arrival_time']}, ${flight['price']}, {flight['airline']}")
    
    # Check availability
    print(f"\nFlight FL001 availability: {search.check_availability('FL001')}")
    print(f"Flight FL005 availability: {search.check_availability('FL005')}")
    
    # Get airlines
    print(f"\nAirlines: {', '.join(search.get_airlines())}")
