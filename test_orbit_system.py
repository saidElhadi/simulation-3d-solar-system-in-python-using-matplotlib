from solar_system_3d import SolarSystem, Planet, Sun

solar_system = SolarSystem(400, projection_2d=True)

suns = (
    Sun(solar_system, position=(40, 40, 40), velocity=(0, 0, 0)),)

Planet = (
    Planet(
        solar_system,
        10,
        position=(100, 50, 0),
        velocity=(0, 5.5, 5.5),
    ),
)

while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()
    solar_system.draw_all()