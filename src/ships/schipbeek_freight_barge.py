import global_constants
from ship import GeneralCargoVessel

ship = GeneralCargoVessel(id = 'schipbeek_freight_barge',
            numeric_id = 2140,
            title = 'Schipbeek [Freight Barge]',
            capacity_cargo_holds = 560,
            extra_parts = 1,
            refit_part_name = 'fore_aft_holds',
            replacement_id = '-none',
            buy_cost = 29,
            fixed_run_cost_factor = 4.0,
            fuel_run_cost_factor = 1.1,
            speed = 20.0,
            speed_factor_unladen = 1.1,
            inland_capable = True,
            sea_capable = False,
            offsets = [[-14, -42], [-61, -28], [-55, -29], [-10, -28], [-14, -54], [-61, -28], [-55, -29], [-9, -28]],
            buy_menu_width = 109,
            loading_speed = 20,
            intro_date = 1915,
            buy_menu_bb_xy = [624, 21],
            str_type_info = 'CARGO_VESSEL_INLAND',
            vehicle_life = 60,
            gross_tonnage = 560)

ship.add_model_variant(intro_date=0,
                       end_date=1960,
                       spritesheet_suffix=0)

ship.add_model_variant(intro_date=1950,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=1)

ship.add_model_variant(intro_date=1950,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=2)

ship.add_model_variant(intro_date=1960,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=3)
