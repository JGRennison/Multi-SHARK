import global_constants
from ship import Tanker

ship = Tanker(id = 'volgoneft_six_thirty_tanker_barge',
            numeric_id = 2260,
            title = 'Volgoneft 630 [Tanker Barge]',
            capacity_cargo_holds = 0,
            capacity_tanks = 630,
            extra_parts = 2,
            refit_part_name = 'tanks',
            replacement_id = '-none',
            buy_cost = 29,
            fixed_run_cost_factor = 9.5,
            fuel_run_cost_factor = 1.1,
            speed = 21.0,
            speed_factor_unladen = 1.1,
            inland_capable = True,
            sea_capable = False,
            offsets = [[-14, -42], [-61, -28], [-55, -29], [-10, -28], [-14, -54], [-61, -28], [-55, -29], [-9, -28]],
            buy_menu_width = 114,
            loading_speed = 40,
            intro_date = 1926,
            buy_menu_bb_xy = [620, 21],
            str_type_info = 'LARGE_TANKER_COASTAL_INLAND',
            vehicle_life = 45,
            gross_tonnage = 630)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
