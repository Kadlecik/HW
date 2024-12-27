import simpy
import random

# Parametry
default_average_time_passenger = 5  # Průměrný čas mezi příchody cestujících (minuty)
default_average_time_boat = 30  # Průměrný čas mezi příjezdy lodí (minuty)
default_max_people_on_pier = 10  # Maximální počet lidí na molu
boat_capacity = 20  # Kapacita lodě
simulation_time = 300  # Celkový čas simulace (minuty)


class BoatLanding:
    def __init__(self, env, avg_passenger_time, avg_boat_time, max_people_on_pier):
        self.env = env
        self.avg_passenger_time = avg_passenger_time
        self.avg_boat_time = avg_boat_time
        self.max_people_on_pier = max_people_on_pier
        self.people_on_pier = 0  # Počet lidí na molu
        self.total_wait_time = 0  # Celkový čas čekání cestujících
        self.total_passengers = 0  # Celkový počet cestujících
        self.boats_handled = 0  # Počet obsloužených lodí
        self.passengers_left_on_boat = 0  # Počet volných míst na lodi
        self.action = env.process(self.run())

    def run(self):
        while True:
            yield self.env.timeout(random.expovariate(1 / self.avg_boat_time))
            self.handle_boat()

    def handle_boat(self):
        # Zpracování příjezdu lodě
        self.boats_handled += 1
        empty_seats = random.randint(0, boat_capacity)  # Náhodný počet volných míst
        passengers_to_board = min(self.people_on_pier, boat_capacity - empty_seats)

        self.passengers_left_on_boat += empty_seats
        self.people_on_pier -= passengers_to_board
        print(
            f"Loď připlula v čase {self.format_time(self.env.now)}. Volná místa: {empty_seats}. Nastoupilo: {passengers_to_board}. Zůstává na molu: {self.people_on_pier}")

    def passenger_arrival(self):
        while True:
            yield self.env.timeout(random.expovariate(1 / self.avg_passenger_time))
            if self.people_on_pier < self.max_people_on_pier:
                self.people_on_pier += 1
                print(
                    f"Cestující dorazil v čase {self.format_time(self.env.now)}. Počet lidí na molu: {self.people_on_pier}")

    def format_time(self, time):
        hours = int(time) // 60
        minutes = int(time) % 60
        return f"{hours:02d}:{minutes:02d}"


# Hlavní simulace
env = simpy.Environment()
boat_landing = BoatLanding(env, default_average_time_passenger, default_average_time_boat, default_max_people_on_pier)

# Přidání procesu příchodu cestujících
env.process(boat_landing.passenger_arrival())

# Spuštění simulace
env.run(until=simulation_time)

print(f"Simulace dokončena. Celkem obslouženo lodí: {boat_landing.boats_handled}")
print(f"Cestující zůstali na molu: {boat_landing.people_on_pier}")
print(f"Volná místa na lodích: {boat_landing.passengers_left_on_boat}")
