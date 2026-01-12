from itertools import groupby
from typing import Dict, List, Set, NamedTuple
from BaseClasses import ItemClassification, Item

from .names import item_names as iname, shell_names as sname

class ACTItem(Item):
    game: str = "Another Crabs Treasure"

item_base_id: int = 483021700

class ACTItemData(NamedTuple):
    classification: ItemClassification
    quantity_in_item_pool: int
    item_id_offset: int
    item_group: str = ""


# a lot of quantities here will need to be adjusted later
item_table: Dict[str, ACTItemData] = {
    # progression
    iname.fork: ACTItemData(ItemClassification.progression, 1, 1, "Progression"), 
    #iname.heartkelp_pod: ACTItemData(ItemClassification.progression, 1, 2, "Progression"), #throwing this into the progression items because the average player will definitely need heals to beat the game.
    iname.fishing_line: ACTItemData(ItemClassification.progression, 1, 3, "Progression"),
    iname.pristine_pearl: ACTItemData(ItemClassification.progression, 1, 4, "Progression"),
    iname.map_piece_fv: ACTItemData(ItemClassification.progression, 1, 5, "Progression"),
    iname.map_piece_heikea: ACTItemData(ItemClassification.progression, 1, 6, "Progression"), 
    iname.map_piece_pagurus: ACTItemData(ItemClassification.progression, 1, 7, "Progression"), 

    # upgrade
    iname.bloodstar_limb: ACTItemData(ItemClassification.useful, 20, 8, "Upgrades"), # total in game: 25
    iname.heartkelp_sprout: ACTItemData(ItemClassification.useful, 7, 9, "Upgrades"), # total in game: 7
    iname.old_whorl: ACTItemData(ItemClassification.useful, 11, 10, "Upgrades"),
    iname.stainless_relic: ACTItemData(ItemClassification.useful, 11, 11, "Upgrades"), # supposed to be 16 total
    iname.tackle_pouch: ACTItemData(ItemClassification.useful, 5, 12, "Upgrades"),

    # stowaways
    iname.anemone: ACTItemData(ItemClassification.useful, 10, 13, "Stowaways"),
    iname.anemone_plus: ACTItemData(ItemClassification.useful, 4, 14, "Stowaways"),
    iname.anemone_plus_plus: ACTItemData(ItemClassification.useful, 1, 15, "Stowaways"),
    iname.another_crab: ACTItemData(ItemClassification.useful, 5, 16, "Stowaways"),
    iname.barnacle: ACTItemData(ItemClassification.useful, 6, 17, "Stowaways"),
    iname.barnacle_plus: ACTItemData(ItemClassification.useful, 2, 18, "Stowaways"),
    iname.barnacle_plusplus: ACTItemData(ItemClassification.useful, 1, 19, "Stowaways"),
    #iname.bleached_phytoplankton: ACTItemData(ItemClassification.useful, 1, 20, "Stowaways"), #Not used in base game
    iname.bobber: ACTItemData(ItemClassification.useful, 1, 21, "Stowaways"),
    iname.chum: ACTItemData(ItemClassification.progression, 1, 22, "Stowaways"),
    iname.cockle: ACTItemData(ItemClassification.useful, 3, 23, "Stowaways"),
    iname.cockle_plus: ACTItemData(ItemClassification.useful, 1, 113, "Stowaways"), #missed on first pass oops
    iname.contact_lens: ACTItemData(ItemClassification.useful, 1, 24, "Stowaways"),
    iname.cotton_ball: ACTItemData(ItemClassification.useful, 1, 25, "Stowaways"),
    iname.earthworm: ACTItemData(ItemClassification.useful, 1, 114, "Stowaways"), #missed on first pass oops
    iname.fredrick: ACTItemData(ItemClassification.progression, 1, 26, "Stowaways"),
    iname.fruit_sticker: ACTItemData(ItemClassification.useful, 2, 27, "Stowaways"),
    iname.fruit_sticker_plus: ACTItemData(ItemClassification.useful, 1, 28, "Stowaways"),
    iname.googly_eye: ACTItemData(ItemClassification.useful, 3, 29, "Stowaways"),
    iname.lil_isopod: ACTItemData(ItemClassification.progression,3, 147,"Stowaways"),#missed on first pass and also second pass lmao
    iname.lamprey: ACTItemData(ItemClassification.useful, 1, 30, "Stowaways"),
    iname.lamprey_plus: ACTItemData(ItemClassification.useful, 1, 31, "Stowaways"),
    iname.lanternfish: ACTItemData(ItemClassification.progression, 1, 32, "Stowaways"),
    iname.limpet: ACTItemData(ItemClassification.useful, 11, 33, "Stowaways"),
    iname.limpet_plus: ACTItemData(ItemClassification.useful, 2, 34, "Stowaways"),
    iname.limpet_plus_plus: ACTItemData(ItemClassification.useful, 2, 35, "Stowaways"),
    iname.lugnut: ACTItemData(ItemClassification.useful, 1, 36, "Stowaways"),
    iname.lumpsucker: ACTItemData(ItemClassification.useful, 3, 37, "Stowaways"),
    iname.lumpsucker_plus: ACTItemData(ItemClassification.useful, 1, 38, "Stowaways"),
    iname.mussel: ACTItemData(ItemClassification.useful, 10, 39, "Stowaways",),
    iname.mussel_plus: ACTItemData(ItemClassification.useful, 5, 40, "Stowaways",),
    iname.mussel_plus_plus: ACTItemData(ItemClassification.useful, 1, 41, "Stowaways",),
    iname.oyster: ACTItemData(ItemClassification.useful, 3, 42, "Stowaways"),
    iname.packing_peanut: ACTItemData(ItemClassification.useful, 1, 43, "Stowaways"),
    iname.phytoplankton: ACTItemData(ItemClassification.progression, 1, 44, "Stowaways"),
    iname.phytoplankton_plus: ACTItemData(ItemClassification.progression, 2, 45, "Stowaways"),
    iname.puffer_quill: ACTItemData(ItemClassification.useful, 3, 46, "Stowaways"),
    iname.razor_blade: ACTItemData(ItemClassification.useful, 1, 47, "Stowaways"),
    iname.rubber_band: ACTItemData(ItemClassification.useful, 1, 48, "Stowaways"),
    iname.rusty_nail: ACTItemData(ItemClassification.useful, 6, 49, "Stowaways"),
    iname.rusty_nail_plus: ACTItemData(ItemClassification.useful, 3, 50, "Stowaways"),
    iname.salp: ACTItemData(ItemClassification.useful, 3, 51, "Stowaways"),
    iname.salp_plus: ACTItemData(ItemClassification.useful, 2, 52, "Stowaways"),
    iname.sand_dollar: ACTItemData(ItemClassification.useful, 9, 53, "Stowaways"),
    iname.sea_cucumber: ACTItemData(ItemClassification.useful, 2, 54, "Stowaways"),
    iname.seaslug: ACTItemData(ItemClassification.useful, 1, 55, "Stowaways"),
    iname.seastar: ACTItemData(ItemClassification.useful, 7, 56, "Stowaways"),
    iname.seastar_plus: ACTItemData(ItemClassification.useful, 4, 57, "Stowaways"),
    iname.seastar_plus_plus: ACTItemData(ItemClassification.useful, 1, 58, "Stowaways"),
    iname.shark_tooth: ACTItemData(ItemClassification.useful, 1, 59, "Stowaways"),
    iname.shark_tooth_plus: ACTItemData(ItemClassification.useful, 1, 60, "Stowaways"),
    iname.sinker: ACTItemData(ItemClassification.useful, 2, 61, "Stowaways"),
    iname.sinker_plus: ACTItemData(ItemClassification.useful, 3, 62, "Stowaways"),
    iname.sinker_plus_plus: ACTItemData(ItemClassification.useful, 1, 63, "Stowaways"),
    iname.siphonophore: ACTItemData(ItemClassification.useful, 2, 64, "Stowaways"),
    iname.siphonophore_plus: ACTItemData(ItemClassification.useful, 3, 65, "Stowaways"),
    iname.small_battery: ACTItemData(ItemClassification.useful, 1, 66, "Stowaways"),
    iname.small_battery_plus: ACTItemData(ItemClassification.useful, 1, 67, "Stowaways"),
    iname.sponge: ACTItemData(ItemClassification.progression, 3, 68, "Stowaways"),
    iname.sponge_plus: ACTItemData(ItemClassification.progression, 1, 69, "Stowaways"),
    iname.turtle_shell_shard: ACTItemData(ItemClassification.useful, 2, 70, "Stowaways"),
    #iname.ur: ACTItemData(ItemClassification.useful, 1, 71, "Stowaways"), #Not used in base game
    iname.used_bandage: ACTItemData(ItemClassification.useful, 1, 72, "Stowaways"),
    iname.used_bandage_plus: ACTItemData(ItemClassification.useful, 1, 73, "Stowaways"),
    iname.wad_of_gum: ACTItemData(ItemClassification.useful, 1, 74, "Stowaways"),
    iname.whelk: ACTItemData(ItemClassification.useful, 3, 75, "Stowaways"),
    iname.whelk_plus: ACTItemData(ItemClassification.useful, 2, 76, "Stowaways"),
    iname.whelk_plus_plus: ACTItemData(ItemClassification.useful, 2, 77, "Stowaways"),
    iname.zooplankton: ACTItemData(ItemClassification.progression, 1, 78, "Stowaways"),
    iname.zooplankton_plus: ACTItemData(ItemClassification.progression, 1, 79, "Stowaways"),

    #NG+ stowaways
    iname.streakers_sigil: ACTItemData(ItemClassification.progression, 1, 148, "StowawaysNGPlus"),
    iname.sentinels_sigil: ACTItemData(ItemClassification.progression, 1, 149, "StowawaysNGPlus"),
    iname.sickos_sigil: ACTItemData(ItemClassification.progression, 1, 150, "StowawaysNGPlus"),
    iname.shadows_sigil: ACTItemData(ItemClassification.progression, 1, 151, "StowawaysNGPlus"),
    iname.sorcerers_sigil: ACTItemData(ItemClassification.progression, 1, 152, "StowawaysNGPlus"),
    iname.anemone_plus_plus_plus: ACTItemData(ItemClassification.progression, 1, 153, "StowawaysNGPlus"),
    iname.barnacle_plus_plus_plus: ACTItemData(ItemClassification.progression, 1, 154, "StowawaysNGPlus"),
    iname.cockle_plus_plus: ACTItemData(ItemClassification.progression, 1, 155, "StowawaysNGPlus"),
    iname.fruit_sticker_plus_plus: ACTItemData(ItemClassification.progression, 1, 156, "StowawaysNGPlus"),
    iname.fruit_sticker_plus_plus_plus: ACTItemData(ItemClassification.progression, 1, 157, "StowawaysNGPlus"),
    iname.lamprey_plus_plus: ACTItemData(ItemClassification.progression, 1, 158, "StowawaysNGPlus"),
    iname.lamprey_plus_plus_plus: ACTItemData(ItemClassification.progression, 1, 159, "StowawaysNGPlus"),
    iname.limpet_plus_plus_plus: ACTItemData(ItemClassification.progression, 1, 160, "StowawaysNGPlus"),
    iname.mussel_plus_plus_plus: ACTItemData(ItemClassification.progression, 1, 161, "StowawaysNGPlus"),
    iname.oyster_plus: ACTItemData(ItemClassification.progression, 1, 162, "StowawaysNGPlus"),
    iname.oyster_plus_plus: ACTItemData(ItemClassification.progression, 1, 163, "StowawaysNGPlus"),
    iname.puffer_quill_plus: ACTItemData(ItemClassification.progression, 1, 164, "StowawaysNGPlus"),
    iname.rusty_nail_plus_plus: ACTItemData(ItemClassification.progression, 1, 165, "StowawaysNGPlus"),
    iname.rusty_nail_plus_plus_plus: ACTItemData(ItemClassification.progression, 1, 166, "StowawaysNGPlus"),
    iname.sea_cucumber_plus: ACTItemData(ItemClassification.progression, 1, 167, "StowawaysNGPlus"),
    iname.seastar_plus_plus_plus: ACTItemData(ItemClassification.progression, 1, 168, "StowawaysNGPlus"),
    iname.shark_tooth_plus_plus: ACTItemData(ItemClassification.progression, 1, 169, "StowawaysNGPlus"),
    iname.sinker_plus_plus_plus: ACTItemData(ItemClassification.progression, 1, 170, "StowawaysNGPlus"),
    iname.siphonophore_plus_plus: ACTItemData(ItemClassification.progression, 1, 171, "StowawaysNGPlus"),
    iname.siphonophore_plus_plus_plus: ACTItemData(ItemClassification.progression, 1, 172, "StowawaysNGPlus"),
    iname.used_bandage_plus_plus: ACTItemData(ItemClassification.progression, 1, 173, "StowawaysNGPlus"),
    iname.wad_of_gum_plus: ACTItemData(ItemClassification.progression, 1, 174, "StowawaysNGPlus"),
    iname.whelk_plus_plus_plus: ACTItemData(ItemClassification.progression, 1, 175, "StowawaysNGPlus"),

    # currency
    iname.breadclaw: ACTItemData(ItemClassification.filler, 5, 80, "Currency"), 
    iname.chipclaw: ACTItemData(ItemClassification.filler, 5, 81, "Currency"), 
    iname.hairclaw: ACTItemData(ItemClassification.filler, 5, 82, "Currency"), 
    iname.clothesclaw: ACTItemData(ItemClassification.filler, 4, 83, "Currency"),
    iname.paperclaw: ACTItemData(ItemClassification.filler, 3, 84, "Currency"),
    iname.stapleclaw: ACTItemData(ItemClassification.filler, 2, 85, "Currency"),
    iname.carclaw: ACTItemData(ItemClassification.filler, 1, 86, "Currency"),

    # consumable
    iname.barbed_hook: ACTItemData(ItemClassification.filler, 10, 87, "Consumable"), #113 in game
    iname.shark_egg: ACTItemData(ItemClassification.filler, 4, 135, "Consumable"), #4 in game

    # costume
    #iname.plastic_poncho: ACTItemData(ItemClassification.filler, 1, 88, "Costume"),
    iname.captain_costume: ACTItemData(ItemClassification.filler, 1, 89, "Costume"),
    iname.dr_kril: ACTItemData(ItemClassification.filler, 1, 90, "Costume"),
    iname.exiled_flame: ACTItemData(ItemClassification.filler, 1, 91, "Costume"),
    #iname.blackout_poncho: ACTItemData(ItemClassification.filler, 1, 92, "Costume"),
    #iname.ivory_poncho: ACTItemData(ItemClassification.filler, 1, 93, "Costume"),
    iname.intern: ACTItemData(ItemClassification.filler, 1, 94, "Costume"),
    iname.sunlight: ACTItemData(ItemClassification.filler, 1, 95, "Costume"),
    iname.krillionaire: ACTItemData(ItemClassification.filler, 1, 96, "Costume"),
    #iname.midnight: ACTItemData(ItemClassification.filler, 1, 97, "Costume"),
    #iname.maid_kril: ACTItemData(ItemClassification.filler, 1, 98, "Costume"),
    #iname.rainbow_crabitalism: ACTItemData(ItemClassification.filler, 1, 99, "Costume"),
    #iname.mr_kril: ACTItemData(ItemClassification.filler, 1, 100, "Costume"),
    iname.cowfishboy: ACTItemData(ItemClassification.filler, 1, 101, "Costume"),
    #iname.cult_leader: ACTItemData(ItemClassification.filler, 1, 102, "Costume"),
    iname.blue_collar: ACTItemData(ItemClassification.filler, 1, 103, "Costume"),
    iname.clown: ACTItemData(ItemClassification.filler, 1, 104, "Costume"),

    # adaptations
    iname.royal_wave: ACTItemData(ItemClassification.progression, 1, 105, "Adapations"),
    iname.bobbit_trap: ACTItemData(ItemClassification.useful, 1, 106, "Adapations"),
    iname.bubble_bullet: ACTItemData(ItemClassification.progression, 1, 107, "Adapations"),
    iname.eelectrocute: ACTItemData(ItemClassification.progression, 1, 108, "Adapations"),
    iname.mantis_punch: ACTItemData(ItemClassification.progression, 1, 109, "Adapations"),
    iname.snail_sanctum: ACTItemData(ItemClassification.useful, 1, 110, "Adapations"),
    iname.spectral_tentacle: ACTItemData(ItemClassification.useful, 1, 111, "Adapations"),
    iname.urchin_toss: ACTItemData(ItemClassification.progression, 1, 112, "Adapations"),

    iname.shelleport: ACTItemData(ItemClassification.progression, 1, 133, "Skills"),
    iname.parry: ACTItemData(ItemClassification.useful, 1, 136, "Skills"),
    iname.riposte: ACTItemData(ItemClassification.useful, 1, 137, "Skills"),
    iname.natural_defenses: ACTItemData(ItemClassification.useful, 1, 115, "Skills"),
    iname.aggravation: ACTItemData(ItemClassification.useful, 1, 116, "Skills"),
    iname.self_repair: ACTItemData(ItemClassification.useful, 1, 117, "Skills"),
    iname.kintsugi: ACTItemData(ItemClassification.useful, 1, 118, "Skills"),
    iname.skewer: ACTItemData(ItemClassification.useful, 1, 119, "Skills"),
    iname.plunge: ACTItemData(ItemClassification.useful, 1, 120, "Skills"),
    iname.scrap_hammer: ACTItemData(ItemClassification.useful, 1, 121, "Skills"),
    iname.dispatch: ACTItemData(ItemClassification.useful, 1, 122, "Skills"),
    iname.spearfishing: ACTItemData(ItemClassification.progression, 1, 123, "Skills"),
    iname.wave_breaker: ACTItemData(ItemClassification.useful, 1, 124, "Skills"),
    iname.streamline: ACTItemData(ItemClassification.useful, 1, 125, "Skills"),
    iname.housewarming: ACTItemData(ItemClassification.useful, 1, 126, "Skills"),
    iname.circle_of_life: ACTItemData(ItemClassification.useful, 1, 127, "Skills"),
    iname.elusive_prey: ACTItemData(ItemClassification.useful, 1, 128, "Skills"),
    iname.skeddadle: ACTItemData(ItemClassification.useful, 1, 134, "Skills"),
    iname.ebb_and_flow: ACTItemData(ItemClassification.useful, 1, 129, "Skills"),
    iname.umami_training1: ACTItemData(ItemClassification.useful, 1, 130, "Skills"),
    iname.umami_training2: ACTItemData(ItemClassification.useful, 1, 131, "Skills"),
    iname.umami_training3: ACTItemData(ItemClassification.useful, 1, 132, "Skills"),

    # traps
    iname.gunk_trap: ACTItemData(ItemClassification.trap, 0, 138, "Traps"),
    iname.scour_trap: ACTItemData(ItemClassification.trap, 0, 139, "Traps"),
    iname.bleached_trap: ACTItemData(ItemClassification.trap, 0, 140, "Traps"),
    iname.fear_trap: ACTItemData(ItemClassification.trap, 0, 141, "Traps"),
    iname.clutz_trap: ACTItemData(ItemClassification.trap, 0, 142, "Traps"),
    iname.text_trap: ACTItemData(ItemClassification.trap, 0, 143, "Traps"),
    iname.shell_shatter_trap: ACTItemData(ItemClassification.trap, 0, 144, "Traps"),
    iname.poison_cocktail_trap: ACTItemData(ItemClassification.trap, 0, 145, "Traps"),
    iname.taser_trap: ACTItemData(ItemClassification.trap, 0, 146, "Traps"),

    # shells
    # might be worth trying to use event items for these
    sname.soda_can: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.bottle_cap: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.tin_can: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.shot_glass: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.banana_peel: ACTItemData(ItemClassification.filler, 0, None, "Shells"),
    sname.party_hat: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.coconut: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.teacup: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.sauce_nozzle: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.thimble: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.bebop_cup: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.tennis_ball: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.f_key: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.mason_jar: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.salt_shaker: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.conchiglie: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.bartholomew: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.disco_ball: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.baby_shoe: ACTItemData(ItemClassification.filler, 0, None, "Shells"),
    sname.lil_bro: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.matryoshka_large: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    #sname.matryoshka_medium: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    #sname.matryoshka_small: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.shuttlecock: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.felix_cube: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.piggy_bank: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.trophy: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.imposter: ACTItemData(ItemClassification.filler, 0, None, "Shells"),
    sname.lil_red_cup: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.wafer_cone: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.yoccult: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.coffee_pod: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.egg_shell: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.coffee_mug: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.cascadia_roll: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.ham_tin: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.skull: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.crab_husk: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.legal_brick: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.spring: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.shotgun_shell: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.rubber_duck: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.boxing_glove: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.cardboard_box: ACTItemData(ItemClassification.filler, 0, None, "Shells"),
    sname.tissue_box: ACTItemData(ItemClassification.filler, 0, None, "Shells"),
    sname.valve: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.dumptruck: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.ink_cartridge: ACTItemData(ItemClassification.filler, 0, None, "Shells"),
    sname.gacha_capsule: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.lightbulb: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.mouse: ACTItemData(ItemClassification.filler, 0, None, "Shells"),
    sname.going_under_64: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.sock: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.doll_head: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.service_bell: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.party_popper: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.scrub_aggie: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.dentures: ACTItemData(ItemClassification.filler, 0, None, "Shells"),
    sname.pill_bottle: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.detergent_cap: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.ultrasoft: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.champagne_flute: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.dish_scrubber: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.snow_globe: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.knights_helmet: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    #sname.spirit_conch: ACTItemData(ItemClassification.filler, 0, None, "Shells"),
    sname.plug_fuse: ACTItemData(ItemClassification.progression, 0, None, "Shells")

}

item_name_to_id: Dict[str, int] ={}#= {name: combine_item_id(data) for name, data in item_table.items()}

for name, data in item_table.items():
    if data.item_id_offset != None:
        item_name_to_id.update({name:data.item_id_offset + item_base_id})

def get_item_group(item_name: str) -> str:
    return item_table[item_name].item_group

filler_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.filler]

trap_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.trap]

costume_items: List[str] = [name for name in filler_items if get_item_group(name) == "Costume"]

shell_items: List[str] = [name for name,data in item_table.items() if get_item_group(name) == "Shells"]

item_name_groups: Dict[str, Set[str]] = {
    group: set(item_names) for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group) if group != ""
}

item_limited_group = [iname.umami_training1,iname.umami_training2,iname.umami_training3,iname.googly_eye,iname.used_bandage]