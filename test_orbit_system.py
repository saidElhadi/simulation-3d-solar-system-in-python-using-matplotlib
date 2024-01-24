from solar_system_3d import SolarSystem, Planet, Sun, Moon

solar_system = SolarSystem(400, projection_2d=True)


planet = (
    Planet(
        solar_system,
        1000,
        position=(100, 50, 0),
        velocity=(0, 0, 0),
    ),
)

moons = (
    Moon(
        solar_system,
        .001,
        position=(10, 50, 0),
        velocity=(0, 5.5, 5.5),
    ),
)

while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()
    solar_system.draw_all()