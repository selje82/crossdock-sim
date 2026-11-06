# Class for a pallet
class Pallet:
    def __init__(self, pallet_id: str, destination_warehouse: str, weight_kg: float, temp_zone: str):
        if weight_kg <= 0:
            raise ValueError("Weight must be positive")
        self.__pallet_id = pallet_id
        self.__destination_wh = destination_warehouse
        self.__weight_kg = weight_kg
        self.__temp_zone = temp_zone

    def get_id(self) -> str:
        return self.__pallet_id

    def get_destination(self) -> str:
        return self.__destination_wh

    def get_weight(self) -> float:
        return self.__weight_kg

    def get_temp_zone(self) -> str:
        return self.__temp_zone

class Truck:
    def __init__(self, truck_id: str, route_name: str, max_weight_kg: float, is_refrigerated: bool):
        self.__truck_id = truck_id
        self.__route_name = route_name
        self.__max_weight_kg = max_weight_kg
        self.__is_refrigerated = is_refrigerated
        self.__pallets = []

    def get_id(self) -> str:
        return self.__truck_id

    def get_route(self) -> str:
        return self.__route_name

    def get_current_weight(self) -> float:
        pass

    def load_pallet(self, pallet: Pallet) -> None:
        if pallet.__temp_zone != "dry" and not self.__is_refrigerated:
            raise ValueError("Cannot load chilled pallet into non-refrigerated truck")
        
            
