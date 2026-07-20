from typing import TYPE_CHECKING, Dict, List
from worlds.generic.Rules import add_rule, set_rule, forbid_item, add_item_rule
from BaseClasses import CollectionState

from .options import ACTGameOptions
from .names import location_names as lname
from .names import item_names as iname
from .names import region_names as rname
from .names import shell_names as sname
from . import logic

if TYPE_CHECKING:
    from . import ACTWorld


def set_region_rules(world: "ACTWorld") -> None:
  multiworld = world.multiworld
  player = world.player
  options = world.options
  #logic.set_options(world.options)

  multiworld.get_entrance("Central Shallows -> Central Shallows - Items Behind Grapple", player).access_rule = \
    lambda state: logic.can_skip_some_grapples(options, state, player)
    
  multiworld.get_entrance("Central Shallows -> Fort Slacktide - Before Destruction", player).access_rule = \
    lambda state: logic.is_slacktide_before_accessible(options, state, player)

  multiworld.get_entrance("Fort Slacktide - Before Destruction -> Moon Snail's Cave", player).access_rule = \
    lambda state: logic.is_moonsnail_accessible(options, state, player)
   
  multiworld.get_entrance("Moon Snail's Cave -> Fort Slacktide - After Destruction", player).access_rule = \
    lambda state: state.has(iname.pristine_pearl, player)  
    
  multiworld.get_entrance("Fort Slacktide - Before Destruction -> Reef's Edge", player).access_rule = \
    lambda state: logic.can_magista_skip(options, state, player)
    
  multiworld.get_entrance("Fort Slacktide - After Destruction -> Reef's Edge", player).access_rule = \
    lambda state: (options.goal == "magista") or logic.is_reefs_edge_accessible_vanilla(state, player)
    
  multiworld.get_entrance("Reef's Edge -> Reef's Edge - Items Behind Grapple", player).access_rule = \
    lambda state: (options.goal == "magista") or logic.can_skip_some_grapples(options, state, player)
    
  multiworld.get_entrance("The Sands Between -> Secluded Ridge", player).access_rule = \
    lambda state: (options.goal == "magista") or logic.is_secluded_ridge_accessible(options, state, player)
        
  multiworld.get_entrance("Secluded Ridge -> Secluded Ridge - Past Eelectrocute", player).access_rule = \
    lambda state: (options.goal == "magista") or logic.is_secluded_ridge_eel_accessible(options, state, player)
    
  multiworld.get_entrance("The Sands Between -> Trashbin Plateau", player).access_rule = \
    lambda state: (options.goal == "magista") or state.has(iname.mantis_punch, player)
    
  multiworld.get_entrance("The Sands Between -> The Sands Between - Grapple to East of Grove",player).access_rule = \
    lambda state: (options.goal == "magista") or state.has_all({iname.fishing_line, iname.eelectrocute}, player)
    
  multiworld.get_entrance("The Sands Between -> Southern Town Ridge", player).access_rule = \
    lambda state: (options.goal == "magista") or logic.is_southern_town_ridge_accessible(options, state, player)
    
  multiworld.get_entrance("Expired Grove - Main -> Flotsam Vale - Consortium Arena",player).access_rule = \
    lambda state: (options.goal == "magista") or logic.is_consortium_accessible_grove(options, state, player)
    
  multiworld.get_entrance("Expired Grove - Main -> Expired Grove - Village", player).access_rule = \
    lambda state: (options.goal == "magista") or state.can_reach_location(lname.heikea,player)
    
  multiworld.get_entrance("Expired Grove - Main -> Expired Grove - Raised Platforms",player).access_rule = \
    lambda state: (options.goal == "magista") or logic.is_consortium_accessible_grove(options, state, player)
  
  multiworld.get_entrance("Flotsam Vale -> Flotsam Vale - Post Ceviche Sisters", player).access_rule = \
    lambda state: (options.goal == "magista") or logic.is_post_ceviche_accessible(options, state, player)
    
  multiworld.get_entrance("Flotsam Vale -> Flotsam Vale - Consortium Arena", player).access_rule = \
    lambda state: (options.goal == "magista") or logic.is_consortium_accessible_vale(options, state, player)
    
  multiworld.get_entrance("Flotsam Vale -> Plug Fuse Pipes",player).access_rule = \
    lambda state: (options.goal == "magista") or logic.has_all_maps(state,player)
    
  multiworld.get_entrance("Flotsam Vale -> Flotsam Vale - Voltai Skip Spot",player).access_rule = \
    lambda state: (options.goal == "magista") or state.has(iname.fishing_line,player)
    
  multiworld.get_entrance("Expired Grove - Village -> Flotsam Vale - Voltai Skip Spot", player).access_rule = \
    lambda state: (options.goal == "magista") or logic.can_razor_CAL(options,state,player)
    
  multiworld.get_entrance("Flotsam Vale -> Scuttleport - Entrance",player).access_rule = \
    lambda state: (options.goal == "magista") or logic.can_access_scuttleport(options, state, player)
    
  multiworld.get_entrance("Scuttleport - Entrance -> Scuttleport - Main",player).access_rule = \
    lambda state: (options.goal == "magista") or logic.can_traverse_scuttleport_vanilla(state, player)
    
  multiworld.get_entrance("Flotsam Vale - Voltai Skip Spot -> Scuttleport - Main",player).access_rule = \
    lambda state: (options.goal == "magista") or (logic.can_voltai_skip(options, state, player) and state.has(iname.fishing_line, player))
  
  multiworld.get_entrance("Scuttleport - Main -> Dump Truck", player).access_rule = \
    lambda state: (options.goal == "magista") or logic.has_magnetic_shells(state, player)

  multiworld.get_entrance("Scuttleport - Main -> Plug Fuse Pipes",player).access_rule = \
    lambda state: (options.goal == "magista") or logic.has_all_maps(state, player)
    
  multiworld.get_entrance("Flotsam Vale - Voltai Skip Spot -> Scuttleport - Voltai Arena",player).access_rule = \
    lambda state: (options.goal == "magista") or logic.can_voltai_skip(options, state, player)
        
  multiworld.get_entrance("Scuttleport - Main -> Scuttleport - Tower 2 Roof and Tower 3",player).access_rule = \
    lambda state: (options.goal == "magista") or logic.can_traverse_scuttleport_vanilla(state, player) or logic.can_traverse_scuttleport_boost_jump(options, state, player)
    
  multiworld.get_entrance("Flotsam Vale -> Pinbarge", player).access_rule = \
    lambda state: (options.goal == "magista") or (logic.has_all_maps(state,player) and state.has(iname.eelectrocute, player))
  

def set_location_rules(world: "ACTWorld") -> None:
  multiworld = world.multiworld
  player = world.player
  options = world.options

# ---- Forkless Logic ----

  #Forkless Disabled, ensures player has fork for bosses
  if options.allow_forkless == "disabled":
    set_rule(multiworld.get_location(lname.bloodstar_shallows_help,player),
           lambda state: state.has(iname.fork,player))

    set_rule(multiworld.get_location(lname.nephro, player),
           lambda state: state.has(iname.fork,player))
    
    set_rule(multiworld.get_location(lname.platoon_pathfinder, player),
           lambda state: state.has(iname.fork,player))
    
    set_rule(multiworld.get_location(lname.royal_shellsplitter, player),
           lambda state: state.has(iname.fork,player))
    
    set_rule(multiworld.get_location(lname.magista, player),
           lambda state: state.has(iname.fork,player))

    if options.ngplus_bosses:
        set_rule(multiworld.get_location(lname.extremely_rude_snail, player),
           lambda state: state.has(iname.fork, player))
    
    if options.goal != "magista":
        set_rule(multiworld.get_location(lname.pagurus, player),
                lambda state: (state.has(iname.fork,player) or logic.can_pagurus_quick_kill(options,state,player))) #allow pagurus quick kill if not vanilla
        
        set_rule(multiworld.get_location(lname.lichenthrope, player),
                lambda state: state.has(iname.fork,player))
        
        set_rule(multiworld.get_location(lname.carbonara_connoisseur, player),
                lambda state: state.has(iname.fork,player))
        
        set_rule(multiworld.get_location(lname.heikea, player),
                lambda state: (state.has(iname.fork,player) or logic.can_heikia_quick_kill(options,state,player)))
        
        set_rule(multiworld.get_location(lname.topoda, player),
                lambda state: state.has(iname.fork,player))
        
        set_rule(multiworld.get_location(lname.consortium, player),
                lambda state: state.has(iname.fork,player))
        
        set_rule(multiworld.get_location(lname.sludge_steamroller, player),
                lambda state: state.has(iname.fork,player))
        
        set_rule(multiworld.get_location(lname.ceviche_sisters, player),
                lambda state: state.has(iname.fork,player))

        set_rule(multiworld.get_location(lname.voltai, player),
                lambda state: state.has(iname.fork,player))
                
        if options.goal != "voltai":        
                set_rule(multiworld.get_location(lname.roland, player),
                        lambda state: state.has(iname.fork,player))
                
                if options.goal != "roland":
                        set_rule(multiworld.get_location(lname.petroch, player),
                                lambda state: state.has(iname.fork,player))
                        
                        set_rule(multiworld.get_location(lname.inkerton, player),
                                lambda state: state.has(iname.fork,player))
                        
                        set_rule(multiworld.get_location(lname.camtscha, player),
                                lambda state: state.has(iname.fork,player))
                        
                        set_rule(multiworld.get_location(lname.praya_dubia, player),
                                lambda state: state.has(iname.fork,player))
                        
                        set_rule(multiworld.get_location(lname.firth, player),
                                lambda state: state.has(iname.fork,player))
                        
                        

    #Forkless Enabled, ensures player has some means of dealing damage for bosses
  elif options.allow_forkless == "forkless_easy":
    set_rule(multiworld.get_location(lname.bloodstar_shallows_help,player),
            lambda state: logic.can_deal_damage_easy(state,player))
    
    set_rule(multiworld.get_location(lname.nephro, player),
            lambda state: logic.can_deal_damage_easy(state,player))
    
    set_rule(multiworld.get_location(lname.royal_shellsplitter, player),
            lambda state: logic.can_deal_damage_easy(state,player))
    
    set_rule(multiworld.get_location(lname.platoon_pathfinder, player),
            lambda state: logic.can_deal_damage_easy(state,player))
      
    set_rule(multiworld.get_location(lname.magista, player),
            lambda state: logic.can_deal_damage_easy(state,player))

    if options.ngplus_bosses:
        set_rule(multiworld.get_location(lname.extremely_rude_snail, player),
           lambda state: logic.can_deal_damage_easy(state, player))
    
    if options.goal != "magista":
        set_rule(multiworld.get_location(lname.pagurus, player),
                lambda state: (logic.can_deal_damage_easy(state,player) or logic.can_pagurus_quick_kill(options,state,player)))
        
        set_rule(multiworld.get_location(lname.lichenthrope, player),
                lambda state: logic.can_deal_damage_easy(state,player))
        
        set_rule(multiworld.get_location(lname.carbonara_connoisseur, player),
                lambda state: logic.can_deal_damage_easy(state,player))
        
        set_rule(multiworld.get_location(lname.heikea, player),
                lambda state: (logic.can_deal_damage_easy(state,player) or logic.can_heikia_quick_kill(options,state,player)))
        
        set_rule(multiworld.get_location(lname.topoda, player),
                lambda state: logic.can_deal_damage_easy(state,player))
        
        set_rule(multiworld.get_location(lname.consortium, player),
                lambda state: logic.can_deal_damage_easy(state,player))
        
        set_rule(multiworld.get_location(lname.sludge_steamroller, player),
                lambda state: logic.can_deal_damage_easy(state,player))
        
        set_rule(multiworld.get_location(lname.ceviche_sisters, player),
                lambda state: logic.can_deal_damage_easy(state,player))
        
        set_rule(multiworld.get_location(lname.voltai, player),
                lambda state: logic.can_deal_damage_easy(state,player))
        
        if options.goal != "voltai":
                set_rule(multiworld.get_location(lname.roland, player),
                        lambda state: logic.can_deal_damage_easy(state,player))
                
                if options.goal != "roland":
                        set_rule(multiworld.get_location(lname.petroch, player),
                                lambda state: logic.can_deal_damage_easy(state,player))
                        
                        set_rule(multiworld.get_location(lname.inkerton, player),
                                lambda state: logic.can_deal_damage_easy(state,player)) 
                        
                        set_rule(multiworld.get_location(lname.camtscha, player),
                                lambda state: logic.can_deal_damage_easy(state,player))
                        
                        set_rule(multiworld.get_location(lname.praya_dubia, player),
                                lambda state: logic.can_deal_damage_easy(state,player))
                        
                        set_rule(multiworld.get_location(lname.firth, player),
                                lambda state: logic.can_deal_damage_easy(state,player))
  
  else:
    set_rule(multiworld.get_location(lname.bloodstar_shallows_help,player),
           lambda state: logic.can_deal_damage_hard(state,player))
    
    set_rule(multiworld.get_location(lname.nephro, player),
            lambda state: logic.can_deal_damage_hard(state,player))
    
    set_rule(multiworld.get_location(lname.royal_shellsplitter, player),
            lambda state: logic.can_deal_damage_hard(state,player))
    
    set_rule(multiworld.get_location(lname.platoon_pathfinder, player),
            lambda state: logic.can_deal_damage_hard(state,player))
      
    set_rule(multiworld.get_location(lname.magista, player),
            lambda state: logic.can_deal_damage_hard(state,player))

    if options.ngplus_bosses:
        set_rule(multiworld.get_location(lname.extremely_rude_snail, player),
           lambda state: logic.can_deal_damage_hard(state, player))
    
    if options.goal != "magista":
        set_rule(multiworld.get_location(lname.pagurus, player),
                lambda state: (logic.can_deal_damage_hard(state,player) or logic.can_pagurus_quick_kill(options,state,player)))
        
        set_rule(multiworld.get_location(lname.lichenthrope, player),
                lambda state: logic.can_deal_damage_hard(state,player))
        
        set_rule(multiworld.get_location(lname.carbonara_connoisseur, player),
                lambda state: logic.can_deal_damage_hard(state,player))
        
        set_rule(multiworld.get_location(lname.heikea, player),
                lambda state: (logic.can_deal_damage_hard(state,player) or logic.can_heikia_quick_kill(options,state,player)))
        
        set_rule(multiworld.get_location(lname.topoda, player),
                lambda state: logic.can_deal_damage_hard(state,player))
        
        set_rule(multiworld.get_location(lname.consortium, player),
                lambda state: logic.can_deal_damage_hard(state,player))
        
        set_rule(multiworld.get_location(lname.sludge_steamroller, player),
                lambda state: logic.can_deal_damage_hard(state,player))
        
        set_rule(multiworld.get_location(lname.ceviche_sisters, player),
                lambda state: logic.can_deal_damage_hard(state,player))
        
        set_rule(multiworld.get_location(lname.voltai, player),
                lambda state: logic.can_deal_damage_hard(state,player))
        
        if options.goal !="voltai":
                set_rule(multiworld.get_location(lname.roland, player),
                        lambda state: logic.can_deal_damage_hard(state,player))
                
                if options.goal != "roland":
                        set_rule(multiworld.get_location(lname.petroch, player),
                                lambda state: logic.can_deal_damage_hard(state,player))
                        
                        set_rule(multiworld.get_location(lname.inkerton, player),
                                lambda state: logic.can_deal_damage_hard(state,player))
                        
                        set_rule(multiworld.get_location(lname.camtscha, player),
                                lambda state: logic.can_deal_damage_hard(state,player))
                        
                        set_rule(multiworld.get_location(lname.praya_dubia, player),
                                lambda state: logic.can_deal_damage_hard(state,player))
                        
                        set_rule(multiworld.get_location(lname.firth, player),
                                lambda state: logic.can_deal_damage_hard(state,player))
  
    
# ---- Cave of Respite ----
 # spearfishing
  set_rule(multiworld.get_location(lname.clothesclaw_caveofrespite_entrancefishing, player),
            lambda state: state.has_all({iname.spearfishing, iname.fishing_line}, player))
  
  set_rule(multiworld.get_location(lname.chipclaw_caveofrespite_forkroomfishing, player),
            lambda state: state.has_all({iname.spearfishing, iname.fishing_line}, player))
  
  set_rule(multiworld.get_location(lname.mussel_caveofrespite_crabfightfishing, player),
            lambda state: state.has_all({iname.spearfishing, iname.fishing_line}, player))
  
  set_rule(multiworld.get_location(lname.sanddollar_caveofrespite_pathfishing, player),
            lambda state: state.has_all({iname.spearfishing, iname.fishing_line}, player))

# ---- Central Shallows ----
 # grapple   
  set_rule(multiworld.get_location(lname.chipclaw_shallows_sandcastle, player),
            lambda state: state.has(iname.fishing_line, player))
    
  set_rule(multiworld.get_location(lname.bloodstar_shallows_clam, player),
            lambda state: state.has(iname.fishing_line, player))
    
  set_rule(multiworld.get_location(lname.anothercrab_shallows_pillar, player),
            lambda state: state.has(iname.fishing_line, player) or logic.can_CAL(options,state,player))
    
  set_rule(multiworld.get_location(lname.sanddollar_shallows_arch, player),
            lambda state: state.has(iname.fishing_line, player))
            
  set_rule(multiworld.get_location(lname.clothesclaw_shallows_southwestfort ,player),
            lambda state: (state.has(iname.fishing_line, player) and state.can_reach_location(lname.nephro, player)) or logic.are_skips_allowed(options))
            
 
 # spearfishing
  set_rule(multiworld.get_location(lname.mussel_shallows_southwestcastlefish, player),
            lambda state: state.has_all({iname.spearfishing, iname.fishing_line}, player))
    
  set_rule(multiworld.get_location(lname.breadclaw_shallows_slacktidesouthfish, player),
            lambda state: state.has_all({iname.spearfishing, iname.fishing_line}, player))
    
  set_rule(multiworld.get_location(lname.anemone_shallows_southwestcastlehiddenfishing, player),
            lambda state: state.has_all({iname.spearfishing, iname.fishing_line}, player))
    
  set_rule(multiworld.get_location(lname.razorblade_shallows_slacktidebottlefishing, player),
            lambda state: state.has_all({iname.spearfishing, iname.fishing_line}, player))
    
  set_rule(multiworld.get_location(lname.anemone_shallows_umbrellafishing, player),
            lambda state: state.has_all({iname.spearfishing, iname.fishing_line}, player))

# ---- Fort Slacktide ----
 # grapple

  set_rule(multiworld.get_location(lname.magista,player),
            lambda state: state.has(iname.fishing_line, player))
 
  set_rule(multiworld.get_location(lname.limpet_slacktide_stairs, player),
            lambda state: state.has(iname.fishing_line, player))
   
  set_rule(multiworld.get_location(lname.seastar_slacktide_grappleroom, player),
            lambda state: state.has(iname.fishing_line, player))
    
  set_rule(multiworld.get_location(lname.barnacle_slacktide_bigurchin, player),
            lambda state: (state.has(iname.fishing_line, player) or logic.can_boost_jump(options, state, player)))
    
  set_rule(multiworld.get_location(lname.rustynail_slacktide_bigurchin, player),
            lambda state: state.has(iname.fishing_line, player) or ((logic.can_big_boost_jump(options, state, player) and state.can_reach_region(rname.slacktide_after,player))))
    
  set_rule(multiworld.get_location(lname.chipclaw_slacktide_brokenwall, player),
            lambda state: state.has(iname.fishing_line, player))
    
  set_rule(multiworld.get_location(lname.bloodstar_slacktide_clam, player),
            lambda state: state.has(iname.fishing_line, player))
    
 # spearfishing
  set_rule(multiworld.get_location(lname.breadclaw_slacktide_roofhiddenfish, player),
            lambda state: state.has_all({iname.spearfishing, iname.fishing_line}, player))
            
 # Other
  set_rule(multiworld.get_location(lname.breadclaw_slacktide_training, player), 
            lambda state: state.has(iname.pristine_pearl,player) or logic.are_skips_allowed(options))

  if options.goal != "magista":
        # ---- Reef's Edge ----        
        # mantis punch
        set_rule(multiworld.get_location(lname.seastarplus_reefsedge_pole, player),
                lambda state: state.has(iname.mantis_punch, player))
        
        set_rule(multiworld.get_location(lname.hairclaw_reefsedge_sign, player),
                lambda state: state.has(iname.mantis_punch, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_reefsedge_cliff, player),
                lambda state: state.has(iname.mantis_punch, player))
        
        set_rule(multiworld.get_location(lname.whelkplus_reefsedge_sponge, player),
                lambda state: state.has(iname.mantis_punch, player))
        
        # ---- New Carcinia ----
        # grapple
        set_rule(multiworld.get_location(lname.sanddollar_newcarcinia_hammerhead, player),
                lambda state: state.has(iname.fishing_line, player))
        
        # ---- Sands Between ----
        # grapple
        set_rule(multiworld.get_location(lname.barbedhook_sandsbetween_spire, player),
                lambda state: state.has(iname.fishing_line, player))
        
        set_rule(multiworld.get_location(lname.clown_costume_pickup, player),
                lambda state: state.has(iname.fishing_line, player))
        
        # mantis punch
        set_rule(multiworld.get_location(lname.rustynailplus_sandsbetween_centralvista, player),
                lambda state: state.has(iname.mantis_punch, player))
        
        set_rule(multiworld.get_location(lname.seastarplus_sandsbetween_flotsam, player),
                lambda state: state.has(iname.mantis_punch, player))
        
        set_rule(multiworld.get_location(lname.seaslug_sandsbetween_crabrave, player),
                lambda state: state.has(iname.mantis_punch, player))
        
        set_rule(multiworld.get_location(lname.whelk_sandsbetween_crabrave, player),
                lambda state: state.has(iname.mantis_punch, player))
        
        set_rule(multiworld.get_location(lname.sinkerplus_sandsbetween_northridgemantis, player),
                lambda state: state.has(iname.mantis_punch, player))
        
        set_rule(multiworld.get_location(lname.limpetplus_sandsbetween_grovemantis, player),
                lambda state: state.has(iname.mantis_punch, player))
        
        set_rule(multiworld.get_location(lname.oldworldwhorl_sandsbetween_mantispitfall, player),
                lambda state: state.has(iname.mantis_punch, player))
        
        # eelectrocute
        set_rule(multiworld.get_location(lname.lumpsuckerplus_sandsbetween_anchor, player),
                lambda state: state.has(iname.eelectrocute, player))
        
        set_rule(multiworld.get_location(lname.stainlessrelic_sandsbetween_eelectrocute, player),
                lambda state: state.has(iname.eelectrocute, player))
        
        set_rule(multiworld.get_location(lname.tacklepouch_sandsbetween_eelnorthchain, player),
                lambda state: state.has(iname.eelectrocute, player))
        
        set_rule(multiworld.get_location(lname.paperclaw_sandsbetween_southeelshortcut, player),
                lambda state: state.has(iname.eelectrocute, player))
        
        set_rule(multiworld.get_location(lname.sinkerplus_sandsbetween_southeel, player),
                lambda state: state.has(iname.eelectrocute, player))
        
        set_rule(multiworld.get_location(lname.musselplus_sandsbetween_southeel, player),
                lambda state: state.has(iname.eelectrocute, player))
        
        set_rule(multiworld.get_location(lname.hairclaw_sandsbetween_southeel, player),
                lambda state: state.has(iname.eelectrocute, player))
        
        set_rule(multiworld.get_location(lname.kelpsprout_sandsbetween_southeelside, player),
                lambda state: state.has(iname.eelectrocute, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_sandsbetween_southeel, player),
                lambda state: state.has(iname.eelectrocute, player))
        
        set_rule(multiworld.get_location(lname.oyster_sandsbetween_southeelashtray, player),
                lambda state: state.has(iname.eelectrocute, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_sandsbetween_southeelshellsplitter, player),
                lambda state: state.has(iname.eelectrocute, player))
        
        set_rule(multiworld.get_location(lname.paperclaw_sandsbetween_trashanchor, player),
                lambda state: state.has(iname.eelectrocute, player))
        
        # spearfishing
        set_rule(multiworld.get_location(lname.hairclaw_sandsbetween_anchorfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.chipclaw_sandsbetween_northeastchainfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.clothesclaw_sandsbetween_propanefish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.mussel_sandsbetween_bobbitfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.clothesclaw_sandsbetween_anchorcentralfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.barnacle_sandsbetween_bobbitfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.breadclaw_sandsbetween_nailfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.breadclaw_sandsbetween_palletfish, player),
                lambda state: state.has(iname.spearfishing, player))

        # spearfishing + eelectrocute
        set_rule(multiworld.get_location(lname.hairclaw_sandsbetween_southeelfish, player),
                lambda state: state.has_all({iname.spearfishing, iname.eelectrocute}, player))
        
        set_rule(multiworld.get_location(lname.chipclaw_sandsbetween_anchoreelhiddenfish, player),
                lambda state: state.has_all({iname.spearfishing, iname.eelectrocute}, player))

        # grapple + eelectrocute
        set_rule(multiworld.get_location(lname.whelkplusplus_sandsbetween_southeelpeak, player),
                lambda state: state.has_all({iname.fishing_line, iname.eelectrocute}, player))

        # post-pag
        set_rule(multiworld.get_location(lname.bloodstar_postpag_anchorswarm, player),
                lambda state: state.has(iname.map_piece_pagurus, player))
        
        set_rule(multiworld.get_location(lname.stapleclaw_postpag_litter, player),
                lambda state: state.has(iname.map_piece_pagurus, player))
        
        set_rule(multiworld.get_location(lname.hairclaw_postpag_chains, player),
                lambda state: state.has(iname.map_piece_pagurus, player))
        
        set_rule(multiworld.get_location(lname.clothesclaw_postpag_chains, player),
                lambda state: state.has(iname.map_piece_pagurus, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_postpag_echain, player),
                lambda state: state.has(iname.map_piece_pagurus, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_postpag_nechain, player),
                lambda state: state.has(iname.map_piece_pagurus, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_postpag_echainpreserver, player),
                lambda state: state.has(iname.map_piece_pagurus, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_postpag_necentral, player),
                lambda state: state.has(iname.map_piece_pagurus, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_postpag_nwridge, player),
                lambda state: state.has(iname.map_piece_pagurus, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_postpag_neeelpath, player),
                lambda state: state.has(iname.map_piece_pagurus, player))
        
        set_rule(multiworld.get_location(lname.hairclaw_postpag_nridge, player),
                lambda state: state.has(iname.map_piece_pagurus, player))
        
        set_rule(multiworld.get_location(lname.hairclaw_postpag_ecentral, player),
                lambda state: state.has(iname.map_piece_pagurus, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_postpag_wplayground, player),
                lambda state: state.has(iname.map_piece_pagurus, player))
        
        set_rule(multiworld.get_location(lname.chipclaw_postpag_nwpropane, player),
                lambda state: state.has(iname.map_piece_pagurus, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_postpag_ridgeentrance, player),
                lambda state: state.has(iname.map_piece_pagurus, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_postpag_swcentral, player),
                lambda state: state.has(iname.map_piece_pagurus, player))
        
        set_rule(multiworld.get_location(lname.paperclaw_postpag_schain, player),
                lambda state: state.has(iname.map_piece_pagurus, player))


        # ---- Secluded Ridge and Trashbin Plateau ----
        # grapple
        set_rule(multiworld.get_location(lname.sharkegg_ridge_broomspire, player),
                lambda state: state.has(iname.mantis_punch, player) and (logic.can_CAL(options, state, player) or state.has(iname.fishing_line, player)))
                
        set_rule(multiworld.get_location(lname.bobber_ridge_broomspire, player),
                lambda state: state.has_all({iname.mantis_punch,iname.fishing_line}, player))
        
        # spearfishing
        set_rule(multiworld.get_location(lname.clothesclaw_ridge_overlookfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.chipclaw_ridge_southfish, player),
                lambda state: state.has(iname.spearfishing, player))
          
        set_rule(multiworld.get_location(lname.cockle_ridge_eelfish, player),
                lambda state: state.has(iname.spearfishing, player))

        # spearfishing + eelectrocute
        set_rule(multiworld.get_location(lname.stapleclaw_trashbin_eelfish, player),
                lambda state: state.has_all({iname.spearfishing, iname.eelectrocute}, player))

        # grapple + eelectrocute
        set_rule(multiworld.get_location(lname.barbedhook_trashbin_eelgrapple, player),
                lambda state: (state.has_all({iname.fishing_line, iname.eelectrocute}, player) or logic.can_razor_CAL(options,state,player)))
        
        # ---- Expired Grove Main ----
        # grapple        
        set_rule(multiworld.get_location(lname.hairclaw_grovemain_milkurchins, player),
                lambda state: state.has(iname.fishing_line, player))
        
        set_rule(multiworld.get_location(lname.breadclaw_grovemain_oilgrapple, player),
                lambda state: state.has(iname.fishing_line, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_grovemain_oildrum, player),
                lambda state: state.has(iname.fishing_line, player))
        
        set_rule(multiworld.get_location(lname.sharktooth_grovemain_pizza, player),
                lambda state: state.has(iname.fishing_line, player))
        
        set_rule(multiworld.get_location(lname.map_piece_heikea_arena, player),
                lambda state: state.has(iname.fishing_line, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_grovemain_carts, player),
                lambda state: state.has(iname.fishing_line, player))
        
        set_rule(multiworld.get_location(lname.kelpsprout_grovemain_carts, player),
                lambda state: state.has(iname.fishing_line, player))
        
        set_rule(multiworld.get_location(lname.contactlens_grovemain_carts, player),
                lambda state: state.has(iname.fishing_line, player))
        
        # mantis punch
        set_rule(multiworld.get_location(lname.sharkegg_grovemain_mantis, player),
                lambda state: state.has(iname.mantis_punch, player))
        
        set_rule(multiworld.get_location(lname.cottonball_grovemain_mantis, player),
                lambda state: state.has(iname.mantis_punch, player))
        
        # spearfishing
        set_rule(multiworld.get_location(lname.mussel_grovemain_fishing, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.clothesclaw_grovemain_mantisfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.sponge_grovemain_fishing, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.hairclaw_grovemain_fishing, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.oyster_grovemain_fishing, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.limpet_grovemain_fishing, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.clothesclaw_grovemain_riverfish, player),
                lambda state: state.has(iname.spearfishing, player))

        # ---- Expired Grove Village ----
        # grapple
        set_rule(multiworld.get_location(lname.hairclaw_grovevillage_NEcarton, player),
                lambda state: state.has(iname.fishing_line, player))
        
        set_rule(multiworld.get_location(lname.tacklepouch_grovevillage_clam, player),
                lambda state: state.has(iname.fishing_line, player))
        
        set_rule(multiworld.get_location(lname.clothesclaw_grovevillage_upsidedown, player),
                lambda state: state.has(iname.fishing_line, player))
        
        set_rule(multiworld.get_location(lname.phytoplanktonplus_grovevillage_upsidedown, player),
                lambda state: state.has(iname.fishing_line, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_grovevillage_above1, player),
                lambda state: state.has(iname.fishing_line, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_grovevillage_above2, player),
                lambda state: state.has(iname.fishing_line, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_grovevillage_above3, player),
                lambda state: state.has(iname.fishing_line, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_grovevillage_ornament, player),
                lambda state: state.has(iname.fishing_line, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_grovevillage_hammer, player),
                lambda state: state.has(iname.fishing_line, player))
        
        set_rule(multiworld.get_location(lname.wadofgum_grovevillage_gumpile, player),
                lambda state: state.has(iname.fishing_line, player))
        
        set_rule(multiworld.get_location(lname.stainlessrelic_grovevillage_clam, player),
                lambda state: state.has(iname.fishing_line, player))
        
        set_rule(multiworld.get_location(lname.anemone_grovevillage_seahorse, player),
                lambda state: state.has(iname.fishing_line, player))
        
        # spearfishing
        set_rule(multiworld.get_location(lname.barbedhook_grovevillage_cartfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.hairclaw_grovevillage_river, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_grovevillage_riveroil, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.anemone_grovevillage_fishing, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_grovevillage_dock, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.mussel_grovevillage_dock, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.clothesclaw_grovevillage_dock, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.hairclaw_grovevillage_dock, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.earthworm_grovevillage_dock, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.clothesclaw_grovevillage_hidden, player),
                lambda state: state.has(iname.spearfishing, player))

        # mantis punch
        set_rule(multiworld.get_location(lname.oldworldwhorl_grovevillage_topoda, player),
                lambda state: state.has(iname.mantis_punch, player))
        
        # ---- Flotsam Vale ----

        # spearfishing
        set_rule(multiworld.get_location(lname.hairclaw_flotsamvale_APfish,player),
                lambda state: state.has(iname.spearfishing, player))
                
        set_rule(multiworld.get_location(lname.lamprey_flotsamvale_islandfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.mussel_flotsamvale_elevatedfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_flotsamvale_snailfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.siphonophoreplus_flotsamvale_waterfall, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.clothesclaw_flotsamvale_northfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.whelk_flotsamvale_westfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.breadclaw_flotsamvale_westfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.clothesclaw_flotsamvale_northshorefish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.clothesclaw_flotsamvale_southfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_flotsamvale_westfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.anemoneplus_flotsamvale_northwestfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.hairclaw_flotsamvale_gunkfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.breadclaw_flotsamvale_gunkfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.turtleshell_flotsamvale_gunkfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.clothesclaw_flotsamvale_gunkfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_flotsamvale_gunkfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.barbedhook_flotsamvale_sludgefish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.lilisopod_flotsamvale_gunkfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.hairclaw_flotsamvale_gunkfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        
        
        # grapple + spearfishing
        set_rule(multiworld.get_location(lname.chipclaw_flotsamvale_consortiumfish, player),
                lambda state: state.has_all({iname.spearfishing, iname.fishing_line}, player))
        
        # ---- Scuttleport ----

        # grapple + eelectrocute 
        set_rule(multiworld.get_location(lname.oldworldwhorl_scuttleport_eelectrocute, player),
                lambda state: state.has(iname.eelectrocute, player) and (state.has(iname.fishing_line,player) or logic.can_CAL(options,state,player)))
                
        # magnet
        set_rule(multiworld.get_location(lname.barbedhook_scuttleport_magnet, player),
                lambda state: logic.has_magnetic_shells(state,player) or logic.can_CAL(options, state, player))
                
        # grapple and spearfishing
        set_rule(multiworld.get_location(lname.mussel_scuttleport_magnetfish,player),
                lambda state: state.has_all({iname.fishing_line, iname.spearfishing}, player))
                
        set_rule(multiworld.get_location(lname.chipclaw_scuttleport_gunkfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.rustynail_scuttleport_gunkfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        set_rule(multiworld.get_location(lname.barnacle_scuttleport_gunkfish, player),
                lambda state: state.has(iname.spearfishing, player))
        
        if options.goal != "voltai" and options.goal != "roland":
        
                # ---- The Unfathom ----

                # grapple
                set_rule(multiworld.get_location(lname.tacklepouch_plains_grapplesnail,player),
                        lambda state: state.has(iname.fishing_line,player) or logic.can_CAL(options,state,player))
                
                # spearfishing
                set_rule(multiworld.get_location(lname.salp_unfathom_glowstickfish, player),
                        lambda state: state.has(iname.spearfishing, player))
                
                set_rule(multiworld.get_location(lname.barnacleplus_unfathom_pinbargefish, player),
                        lambda state: state.has(iname.spearfishing, player))
                
                # ---- Abyssal Plains ----

                # spearfishing
                set_rule(multiworld.get_location(lname.stapleclaw_plains_fish, player),
                        lambda state: state.has(iname.spearfishing, player))
                
                # ---- The Old Ocean ----

                # mantis punch
                set_rule(multiworld.get_location(lname.whelkplusplus_oldocean_mantis, player),
                        lambda state: state.has(iname.mantis_punch, player))
                        
                # grapple
                set_rule(multiworld.get_location(lname.fruitstickerplus_oldocean_island, player),
                        lambda state: state.has(iname.fishing_line,player))
                        
