import global_constants
from ship import PacketBoat

ship = PacketBoat(id = 'lantau_ferry',
            numeric_id = 2001,
            title = 'Lantau [Ferry]',
            capacity_pax = 54,
            capacity_cargo_holds = 27,
            capacity_mail = 54,
            disallow_vehicles = True,
            extra_parts = 1,
            extra_part_cargo_fraction = 10,
            refit_part_name = 'main_aux_decks',
            replacement_id = '-none',
            buy_cost = 8,
            fixed_run_cost_factor = 1.5,
            fuel_run_cost_factor = 1.0,
            speed = 20.0,
            speed_factor_unladen = 1.15,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -40], [-78, -21], [-68, -21], [-30, -21], [-14, -40], [-78, -24], [-68, -21], [-32, -21]],
            buy_menu_width = 29,
            loading_speed = 15,
            intro_date = 1860,
            buy_menu_bb_xy = [673, 23],
            str_type_info = 'SMALL_FERRY',
            vehicle_life = 40,
            gross_tonnage = 30)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)


