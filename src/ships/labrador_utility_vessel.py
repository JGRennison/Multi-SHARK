import global_constants
from ship import UtilityVessel

ship = UtilityVessel(id = 'labrador_utility_vessel',
            numeric_id = 1001,
            title = 'Labrador [Utility Vessel]',
            capacity_pax = 32,
            capacity_cargo_holds = 24,
            capacity_mail = 36,
            replacement_id = '-none',
            buy_cost = 10,
            fixed_run_cost_factor = 2.0,
            fuel_run_cost_factor = 1.6,
            speed = 23.0,
            speed_factor_unladen = 1.15,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -40], [-78, -21], [-68, -21], [-30, -21], [-14, -40], [-78, -24], [-68, -21], [-32, -21]],
            buy_menu_width = 29,
            loading_speed = 15,
            intro_date = 1929,
            buy_menu_bb_xy = [673, 23],
            str_type_info = 'SMALL_GENERAL_PURPOSE_VESSEL',
            effect_spawn_model = 'EFFECT_SPAWN_MODEL_DIESEL',
            effects = ['EFFECT_SPRITE_DIESEL, 0, 0, 8'],
            vehicle_life = 40,
            gross_tonnage = 30)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
