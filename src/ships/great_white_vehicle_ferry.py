import global_constants
from ship import PacketBoat

ship = PacketBoat(id = 'great_white_vehicle_ferry',
            numeric_id = 2032,
            title = 'Great White [Ferry]',
            capacity_pax = 1250,
            capacity_cargo_holds = 655,
            capacity_mail = 1250,
            extra_parts = 3,
            extra_part_cargo_fraction = 20.8,
            refit_part_name = 'decks',
            replacement_id = '-none',
            buy_cost = 105,
            fixed_run_cost_factor = 15.0,
            fuel_run_cost_factor = 1.0,
            speed = 30.0,
            speed_factor_unladen = 1.0,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -47], [-73, -22], [-57, -29], [-20, -22], [-14, -47], [-73, -22], [-57, -29], [-20, -22]],
            buy_menu_width = 138,
            loading_speed = 30,
            intro_date = 1990,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'VEHICLE_FERRY',
            vehicle_life = 40,
            gross_tonnage = 1300)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
