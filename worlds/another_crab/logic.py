from typing import TYPE_CHECKING, Dict, List
from worlds.generic.Rules import set_rule
from BaseClasses import CollectionState

from .options import ACTGameOptions
from .names import location_names as lname
from .names import item_names as iname
from .names import region_names as rname
from .names import shell_names as sname

if TYPE_CHECKING:
    from . import ACTWorld

### Check if regions are accessible based on current glitch category and items (try to only invoke options in rules)
def can_skip_some_grapples(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return state.has(iname.fishing_line, player) or are_skips_allowed(options)

def is_slacktide_before_accessible(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return state.can_reach_location(lname.nephro, player) or are_skips_allowed(options)

def is_reefs_edge_accessible_vanilla(state: CollectionState, player: int) -> bool:
    return state.has_all({iname.fishing_line, iname.pristine_pearl}, player) and state.can_reach_location(lname.magista, player)
 
# This allows I-beam/decoy (skips), or CAL (glitch) to enter cave
def is_moonsnail_accessible(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return can_reach_moonsnail(options, state, player) and can_pink_crab(options, state, player)
    
def can_reach_moonsnail(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return state.has(iname.fishing_line, player) or are_skips_allowed(options)
    
def is_post_ceviche_accessible(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return state.can_reach_location(lname.ceviche_sisters, player) or can_sisters_skip(options, state, player) or can_sisters_skip_glitches(options, state, player)
    
def is_consortium_accessible_vale(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return can_big_boost_jump(options, state, player) 
    
def is_consortium_accessible_grove(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return is_consortium_accessible_grove_vanilla(state,player) or is_consortium_accessible_grove_skips(options,state,player) or can_CAL(options, state, player)
    
def is_consortium_accessible_grove_skips(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return state.has_all({iname.fishing_line, iname.fork},player) and are_skips_allowed(options)

def is_consortium_accessible_grove_vanilla(state: CollectionState, player: int) -> bool:
    return state.has_all({iname.mantis_punch, iname.fishing_line},player)
    
def is_southern_town_ridge_accessible(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return is_southern_town_ridge_accessible_restricted(options, state, player) or state.has(iname.eelectrocute, player)
    
def is_southern_town_ridge_accessible_restricted(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return can_razor_CAL(options, state, player)
    
def is_secluded_ridge_accessible(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return state.has(iname.mantis_punch, player) or are_skips_allowed(options)
    
def is_secluded_ridge_eel_accessible(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return state.has(iname.eelectrocute, player) or can_CAL(options, state, player)
    
def can_access_scuttleport(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return state.has(sname.plug_fuse,player) 
    
def can_traverse_scuttleport_vanilla(state: CollectionState, player: int) -> bool:
    return has_magnetic_shells(state, player) and state.has_all([sname.plug_fuse, iname.fishing_line],player)
    
def can_traverse_scuttleport_boost_jump(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return can_boost_jump(options, state, player) or can_big_boost_jump(options, state, player)
    
def has_all_maps(state: CollectionState, player: int) -> bool:
    return state.has_all({iname.map_piece_fv, iname.map_piece_heikea, iname.map_piece_pagurus}, player)


### Check if specific skips are executable
#Magista skip
def can_magista_skip(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return (can_magista_skip_grapple(options, state, player) or can_magista_skip_grappleless(options, state, player)) and options.goal != "magista" 

def can_magista_skip_grapple(options: ACTGameOptions, state: CollectionState, player: int) -> bool:   
    return state.has(iname.fishing_line, player) and are_skips_allowed(options)
    
def can_magista_skip_grappleless(options: ACTGameOptions, state: CollectionState, player: int) -> bool: #may be possible without CAL
    return can_CAL(options, state, player) and can_shell_clip(options, state, player) 
    
#Sisters skip 
def can_sisters_skip(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return state.has_any([iname.fork, iname.streamline], player) and state.has(iname.fishing_line, player) and are_skips_allowed(options)
    
def can_sisters_skip_glitches(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return can_CAL(options, state, player)
    
#Voltai skip
def can_voltai_skip(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return can_razor_CAL(options, state, player) # no constraint for shell clip as most work - statistically guaranteed to have one that does
    
#Can bypass/kill pink crab by moonsnail (TODO: better implementation of shell rando required for this)
def can_pink_crab(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return can_reach_msg_dmg_shells(state,player) or  has_adaptation(state,player) or can_shell_clip(options, state, player)

def can_pagurus_quick_kill(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return are_skips_allowed(options)

def can_heikia_quick_kill(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return are_glitches_allowed(options) and state.has_all({iname.fishing_line, iname.spearfishing}, player)

#Check if specific tricks are executable
#CAL
def can_CAL(options: ACTGameOptions, state: CollectionState, player: int) ->  bool:
    return state.has(iname.fork, player) and are_glitches_allowed(options)
    
def can_razor_CAL(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return state.has(iname.razor_blade, player) and can_CAL(options, state, player)
    
#Shell Clip (clip may be possible with other shells, need to check)
def can_shell_clip(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return has_shell_clip_shells(state,player) and are_glitches_allowed(options) 
    
#Bombs Away or Decoy
def can_boost_jump(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return (can_bombs_away(state, player) or can_decoy(state, player)) and are_skips_allowed(options)

#Bombs Away or Matrioshka
def can_big_boost_jump(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return (can_bombs_away(state, player) or state.has(sname.matryoshka_large,player)) and are_skips_allowed(options)


### Check which group of glitch categories we are set to
def are_skips_allowed(options: ACTGameOptions) -> bool:
    return options.logic_rules != "vanilla"
    
def are_glitches_allowed(options: ACTGameOptions) -> bool:
    return options.logic_rules == "restricted" or options.logic_rules == "unrestricted"



### Check if metal shells are reachable
def has_magnetic_shells(state: CollectionState, player: int) -> bool:
    magnetic_shells = [sname.valve, sname.service_bell, sname.plug_fuse, sname.thimble, sname.spring, sname.gun, sname.knights_helmet, sname.tin_can, sname.shotgun_shell, sname.soda_can, sname.ham_tin, sname.trophy]
    return state.has_any(magnetic_shells, player)
    
### Check if shell clip shells are accessible
def has_shell_clip_shells(state: CollectionState, player: int) -> bool:
    shell_clip_shells = [sname.soda_can]
    return state.has_any(shell_clip_shells, player)

### Checks to see if the player can logically consistently deal damage
def can_deal_damage_hard(state: CollectionState,player:int) -> bool:
    return can_rolling_attack(state,player) | can_magic_damage(state,player) | can_atk_damage_shell(state,player) | has_summon(state,player)  | state.has(iname.fork,player)

def can_deal_damage_easy(state: CollectionState,player:int) -> bool:
    return can_magic_damage(state,player) | can_atk_damage_shell(state,player) | state.has(iname.fork,player)

def can_rolling_attack(state: CollectionState, player: int) -> bool:
    return can_reach_rolling_shells(state,player) and (state.has(iname.lil_isopod,player,2))

### Checks if the player has any of the summonable fish stowaways
def has_summon(state: CollectionState, player: int) -> bool:
    summon_count: int = 0
    if state.has(iname.chum,player):
        summon_count += 1
    
    if state.has(iname.fredrick,player):
        summon_count += 1

    if state.has(iname.lanternfish,player):
        summon_count += 1

    return summon_count >= 2

### Checks if the player has adaptations
#Skips Snail Sanctum since it needs lvl 2 to deal damage
#Skips Tactical Tentacle since it may need the fork to attack
#Skips Bobbit Trap since it may not do enough dmg at lvl 1
def has_adaptation(state: CollectionState, player: int) -> bool:
    return state.has_any({iname.royal_wave, iname.urchin_toss, iname.mantis_punch, iname.bubble_bullet, iname.eelectrocute},player)

def can_magic_damage(state: CollectionState, player: int) -> bool:
    return (can_reach_magic_shells(state,player) ) and can_regen_umami(state,player) #| has_adaptation(state,player)

def can_regen_umami(state: CollectionState, player: int) -> bool:
    return state.has_any_count({iname.phytoplankton_plus:1,iname.zooplankton:2,iname.zooplankton_plus:1,iname.phytoplankton_plus:2},player)

def can_reach_magic_shells(state: CollectionState, player: int) -> bool:
    return can_twist_top(state,player) | can_pop_off(state,player) | can_rollout(state,player) | can_fizzle(state,player) | can_party_time(state,player) | can_shards(state,player) | can_squash(state,player) | can_twinkle(state,player)

def can_reach_msg_dmg_shells(state: CollectionState, player: int) -> bool:
    return can_fizzle(state,player) | can_party_time(state,player) | can_shards(state,player) | can_squash(state,player) | can_twinkle(state,player)

def can_reach_rolling_shells(state: CollectionState, player: int) -> bool:
    rolling_shells = [sname.soda_can,sname.bottle_cap,sname.lil_red_cup,sname.shuttlecock,sname.bebop_cup,sname.tin_can,sname.shot_glass,sname.party_hat,sname.coconut,sname.teacup,sname.sauce_nozzle,sname.thimble,sname.tennis_ball,sname.mason_jar,sname.salt_shaker,sname.conchiglie,sname.disco_ball,sname.lil_bro,sname.matryoshka_large,sname.wafer_cone,sname.yoccult,sname.coffee_pod,sname.egg_shell,sname.coffee_mug,sname.cascadia_roll,sname.skull,sname.spring,sname.shotgun_shell,sname.dumptruck,sname.gacha_capsule,sname.lightbulb,sname.doll_head,sname.service_bell,sname.party_popper,sname.scrub_aggie,sname.pill_bottle,sname.detergent_cap,sname.ultrasoft,sname.champagne_flute,sname.dish_scrubber,sname.snow_globe,sname.knights_helmet,iname.snail_sanctum,sname.plug_fuse,sname.piggy_bank]
    return state.has_any(rolling_shells,player)

def can_atk_damage_shell(state: CollectionState, player: int) -> bool:
    sponge_val: int = 0
    sponge_val += state.count(iname.sponge,player)
    sponge_val += state.count(iname.sponge_plus,player) * 2
    return can_twist_top(state,player) | (can_pop_off(state,player) and sponge_val >= 3) | (can_rollout(state,player) and sponge_val >= 3) | (can_party_time(state,player) and sponge_val >= 3)

### Check if Shell Spells are Reachable
#Twist Top
def can_twist_top(state: CollectionState, player: int) -> bool:
    twist_top_shells = [sname.sauce_nozzle, sname.shuttlecock,sname.felix_cube,sname.dish_scrubber]
    return state.has_any(twist_top_shells,player)

#Pop Off
def can_pop_off(state: CollectionState, player: int) -> bool:
    pop_off_shells = [sname.bottle_cap,sname.f_key,sname.ham_tin,sname.legal_brick,sname.spring,sname.detergent_cap]
    return state.has_any(pop_off_shells,player)

#Rollout
def can_rollout(state: CollectionState, player: int) -> bool:
    rollout_shells = [sname.coconut,sname.tennis_ball, sname.dumptruck, sname.gacha_capsule, sname.ultrasoft]
    return state.has_any(rollout_shells,player)

#Bombs Away
def can_bombs_away(state: CollectionState, player: int) -> bool:
    bombs_away_shells = [sname.bartholomew,sname.shotgun_shell]
    return state.has_any(bombs_away_shells,player)

#Decoy
def can_decoy(state: CollectionState, player: int) -> bool:
    decoy_shells = [sname.matryoshka_large,sname.piggy_bank,sname.crab_husk,sname.rubber_duck]
    return state.has_any(decoy_shells,player)

#Fizzle
def can_fizzle(state: CollectionState, player: int) -> bool:
    fizzle_shells = [sname.soda_can,sname.valve,sname.going_under_64]
    return state.has_any(fizzle_shells,player)

#Party Time
def can_party_time(state: CollectionState, player: int) -> bool:
    party_time_shells = [sname.party_hat,sname.trophy,sname.party_popper]
    return state.has_any(party_time_shells,player)

#Shards
def can_shards(state: CollectionState, player: int) -> bool:
    shards_shells = [sname.shot_glass,sname.mason_jar,sname.salt_shaker]
    return state.has_any(shards_shells,player)

#Squash
def can_squash(state: CollectionState, player: int) -> bool:
    squash_shells = [sname.boxing_glove,sname.sock]
    return state.has_any(squash_shells,player)

#Twinkle
def can_twinkle(state: CollectionState, player: int) -> bool:
    twinkle_shells = [sname.disco_ball,sname.spirit_conch]
    return state.has_any(twinkle_shells,player)