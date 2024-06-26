import global_constants
from ship import PacketBoat

ship = PacketBoat(id = 'stornoway_vehicle_ferry',
            numeric_id = 78,
            title = 'Stornoway [Ferry]',
            capacity_pax = 600,
            capacity_cargo_holds = 300,
            capacity_mail = 600,
            extra_parts = 2,
            extra_part_cargo_fraction = 16.7,
            refit_part_name = 'decks',
            replacement_id = '-none',
            buy_cost = 47,
            fixed_run_cost_factor = 11.0,
            fuel_run_cost_factor = 1.0,
            speed = 23.0,
            speed_factor_unladen = 1.0,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -41], [-67, -25], [-59, -29], [-15, -26], [-14, -45], [-67, -26], [-59, -29], [-15, -25]],
            buy_menu_width = 96,
            loading_speed = 30,
            intro_date = 1956,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'VEHICLE_FERRY',
            vehicle_life = 45,
            gross_tonnage = 950)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
