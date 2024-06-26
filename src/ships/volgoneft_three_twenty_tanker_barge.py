import global_constants
from ship import Tanker

# http://en.wikipedia.org/wiki/Vandal_(tanker)

ship = Tanker(id = 'volgoneft_three_twenty_tanker_barge',
            numeric_id = 2251,
            title = 'Volgoneft 320 [Tanker Barge]',
            capacity_cargo_holds = 0,
            capacity_tanks = 320,
            replacement_id = '-none',
            buy_cost = 23,
            fixed_run_cost_factor = 6.5,
            fuel_run_cost_factor = 1.1,
            speed = 21.0,
            speed_factor_unladen = 1.1,
            inland_capable = True,
            sea_capable = False,
            offsets = [[-14, -42], [-61, -28], [-55, -29], [-10, -28], [-14, -54], [-61, -28], [-55, -29], [-9, -28]],
            buy_menu_width = 94,
            loading_speed = 40,
            intro_date = 1922,
            buy_menu_bb_xy = [620, 21],
            str_type_info = 'SMALL_TANKER_INLAND',
            effects = ['EFFECT_SPRITE_DIESEL, 6, 0, 13'],
            vehicle_life = 45,
            gross_tonnage = 320)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
