"""kit32_nature: the third hundred rpg specs, natural scenery and outdoor props.
Imported by kit32 at the end of its module; registers into kit32.SPECS."""
from kit32 import (section, BUSH, PINE, ROCK, TREE, Recipe, bricks, checker, item, layer, meta, planks, rows_of, spec, tile,
                   waves)


def prop(aid, desc, title, grid, *maps, bottom=28):
    spec(aid, desc, lambda: item(aid, title, grid, *maps, bottom=bottom))


# ---------------------------------------------------------------- trees and large plants
WILLOW = """
.....EEEEEEE....
...EEEEEEEEEEE..
..EEEEEEEEEEEEe.
.EEEEEEEEEEEEEee
.EEEEEEEEEEEEEee
EEeEEEeEEEeEEeee
EEeEEEeEEEeEEeee
.EeEEEeEEEeEEee.
.Ee.EEe.Ee.Eee..
.e..Ee..Ee..e...
....Ee..e.......
.....OOo........
.....OOo........
....oOOoo.......
"""
PALM = """
EEEE......EEEE..
.EEEEe..EEEEe...
..EEEEeEEEEe....
EEEEEEEEEEEEEEe.
.EEEEEEEEEEEEe..
...EEEqOoEEe....
..EEe.qOo.EEe...
.Ee...qOo...Ee..
......qOo.......
......qOo.......
......qOo.......
.....qOOo.......
.....qOOoo......
"""
BIRCH = """
.....EEEEE......
...EEEEEEEEE....
..EEEEEEEEEEe...
.EEEEEEEEEEEEe..
.EEEEEEEEEEEEe..
..EEEEEEEEEEe...
...EEEEEEEEe....
.....WWWw.......
.....WDWw.......
.....WWWw.......
.....WWDw.......
.....WWWw.......
.....WDWw.......
....wWWWww......
"""
BAMBOO = """
.....Ee....Ee...
.Ee..Ee.Ee.Ee...
.Ee..Eq.Ee.Eq...
.Eq..Ee.Eq.Ee...
.Ee..Ee.Ee.Ee...
.Ee..Eq.Ee.Eq.E.
.Eq..Ee.Eq.Ee.Ee
.Ee..Ee.Ee.Ee.Ee
.Ee..Eq.Eq.Eq.Eq
.Eq..Ee.Ee.Ee.Ee
.Ee..Ee.Ee.Ee.Ee
.Ee..Ee.Ee.Ee.Ee
"""
FERN = """
.....E....E.....
....EE.E..EE....
.E..EEE.E.EE..E.
.EE..EEEEEEE.EE.
..EEEEEEEEEEEE..
...EEEEEEEEEE...
.....eEEEEe.....
.......Ee.......
.......ee.......
"""
TALL_GRASS = "E..E....E..E\nE.EE.E..EE.E\nEEEE.EE.EEEE\n.EEEEEEEEEE.\n.eEEeEEeEEe.\n..eeeeeeee.."
REEDS = "..Nn....Nn..\n..Nn.Nn.Nn..\n.EEe.Nn.EEe.\n.EEe.EEeEEe.\n.EEe.EEe.Ee.\n..Ee.EEe.Ee.\n..Ee..Ee.Ee.\n..Ee..Ee.Ee.\n..ee..ee.ee."
LILY_PAD = "...EEEEEE...\n.EEEEEEEEEE.\nEEEEEEP.EEEe\nEEEEEPP..EEe\nEEEEEE.EEEEe\n.EEEEEEEEEe.\n...eeeeee..."
SUNFLOWER = "...YYYY...\n..YYooYY..\n.YYooooYY.\n.YYooooYY.\n..YYooYY..\n...YYYY...\n....Ee....\n..E.Ee.E..\n..EEEeEE..\n....Ee....\n....Ee....\n....ee...."
FLOWER_RED = "..R...R...\n.RYR.RYR..\n..R...R...\n..Ee.Ee...\n.E.EeE.E..\n.EEEEEEE..\n...eee...."
TULIPS = ".P..R..Y.\nPPPRRRYYY\nPPPRRRYYY\n.P..R..Y.\n.Ee.Ee.Ee\nEEeEEeEEe\n.Ee.Ee.Ee\n.ee.ee.ee"
VINE = "Ee......\nEEe.....\n.EEe....\n..EEe.E.\n...EEEEe\n....EEe.\n...EEe..\n..EEe...\n.EEe....\nEEe.....\nEe......"
IVY_WALL = "mMMMMMMMMMMMMd\nmMEEMMMMMEMMMd\nmMEEEMMMEEEMMd\nmMMEEEMEEEEMMd\nmMMMEEEEEEMMMd\nmMMMMEEEMMMMMd\nmMMMMEEMMMMMMd\nmMMMMEEEMMMMMd\nmmmmmEEmmmmmmd\n.....ee......."
BERRY_BUSH = "....EEEE....\n..EEEREEEE..\n.EEEEEEERRe.\nEEREEEEEEEee\nEEEEEREEEeee\n.EEEEEEEeee.\n..eeeeeeee.."
FLOWER_BUSH = "....EEEE....\n..EEEPEEEE..\n.EPEEEEEPEe.\nEEEEEEPEEEee\nEEPEEEEEEeee\n.EEEEEPEeee.\n..eeeeeeee.."
HEDGE = "EEEEEEEEEEEEEEEe\nEEEEEEEEEEEEEEee\nEEEEEEEEEEEEEeee\nEEEEEEEEEEEEeeee\nEEEEEEEEEEEeeeee\neeeeeeeeeeeeeeee"
SAPLING = "..EEe..\n.EEEEe.\n..EEe..\n...Oo..\n...Oo..\n.nnnnn.\nnnnnnnn"
LOG_MOSS = "..OOOOEEOOOOo\n.OEEOOOOEEOOo\nOmOOOOOOOOEOo\nOOoOOOOEEOOOo\n.ooooooooooo."
MUSHROOM_GLOW = "...CCCC...\n..CCYYCC..\n.CCCCCCCc.\n.cccccccc.\n...WWWw...\n...WWWw...\n...WWWw...\n..wwwwww.."
MUSHROOM_GIANT = """
.....RRRRRRR....
...RRRRMMRRRRR..
..RRRRRMMRRRRRr.
.RRMMRRRRRRRMMrr
.RRMMRRRRRRRMMrr
RRRRRRRRRRRRRRrr
RRRRRRRMMRRRRRrr
rrrrrrrrrrrrrrrr
.....SSSSSSs....
.....SSSSSSs....
.....SSSSSSs....
.....SSSSSSs....
.....SSSSSSs....
....ssssssssss..
"""
MUSHROOM_BLUE = "...LLLL...\n..LLMLLLb.\n.LLLLLMLLb\n.bbbbbbbbb\n....SSs...\n....SSs...\n....SSs...\n...sssss.."
CATTAIL = "...Oo..Oo...\n...Oo..Oo...\n...Oo..Oo...\n...oo..oo...\n.E.Ee..Ee.E.\n.EEEe..Ee.E.\n..EEe..EeEe.\n..EEe..EEe..\n...Ee..Ee...\n...ee..ee..."
CLOVER = "..EE.EE..\n.EEEEEEE.\n..EEEEE..\n.EEE.EEE.\n....Ee...\n....Ee..."
THORNS = "D..D....D..D\nDD.DD..DD.DD\n.DDDDDDDDDD.\n..DDDDDDDD..\n.DDDDDDDDDD.\nDD.DD..DD.DD\nD..D....D..D"

# ---------------------------------------------------------------- rocks, terrain features, water
BOULDER = """
......mmmmm.....
....mmMMMMMmd...
...mMMMMMMMmmd..
..mMMMMMMMMmmdd.
.mMMMMMMMmmmmdd.
.mMMMMMMmmmmddd.
mMMMMMmmmmmmdddd
mMMMmmmmmmmdddd.
.mmmmmmmmddddd..
..ddddddddddd...
"""
ROCK_MOSS = "...EEmm...\n..EMMMmd..\n.mMMMMmdd.\nmMMMMmmddE\nmMMMmmmdEE\n.mmmmmEEe.\n..ddddee.."
ROCK_PILE = "......mmm.....\n..mm.mMMmd.mm.\n.mMMmMMMmdmMmd\nmMMMmMMmmdMMmd\nmMMmmmmmddmmdd\n.mmmddmmmdddd.\n..dddd.dddd..."
PEBBLES = "..mm....mm..\n.mMmd..mMmd.\n.mmdd..mmdd.\n......mm....\n..mm.mMmd...\n.mMmdmmdd.mm\n.mmdd....mMd\n.........mdd"
ORE_IRON = "...mmmm...\n..mMMDmd..\n.mMDDMmdd.\nmMMMMDmddd\nmMDDMmmddd\n.mmmmDddd.\n..dddddd.."
ORE_GOLD = "...mmmm...\n..mMMGmd..\n.mMGYMmdd.\nmMMMMGmddd\nmMGYMmmddd\n.mmmmGddd.\n..dddddd.."
ORE_CRYSTAL = "...mmmm...\n..mMMVmd..\n.mMVVMmdd.\nmMMMMVmddd\nmMVVMmmddd\n.mmmmVddd.\n..dddddd.."
STALAGMITE = "....mm....\n....Mm....\n...mMmd...\n...mMmd...\n..mMMmdd..\n..mMMmdd..\n.mMMMmddd.\n.mMMMmddd.\nmMMMMmdddd\nmmmmmmdddd"
STALACTITE = "mmmmmmdddd\nmMMMMmdddd\n.mMMMmddd.\n.mMMMmddd.\n..mMMmdd..\n..mMMmdd..\n...mMmd...\n...mMmd...\n....Mm....\n....mm...."
CAVE_MOUTH = """
.....DDDDDDDD.....
...DDmmmmmmmmDD...
..DmmMMMMMMMMmmD..
.DmMMMmKKKKmMMMmD.
.DmMMmKKKKKKmMMmD.
DmMMmKKKKKKKKmMMmD
DmMMmKKKKKKKKmMMmD
DmMMmKKKKKKKKmMMmD
DmMmKKKKKKKKKKmMmD
dddddddddddddddddd
"""
LAVA_ROCK = "...DDDD...\n..DDRDDD..\n.DDDDRRDD.\nDDRDDDDDDD\nDDDDDRDDDD\n.DDDDDDDD.\n..DDRDDD.."
ICE_SPIKE = "....CC....\n....CC....\n...CCCc...\n...CMCc...\n..CCMCcc..\n..CCMCcc..\n.CCCMCccc.\n.CCCCCccc.\nCCCCCCcccc\ncccccccccc"
ICE_BLOCK = "CCCCCCCCCCCc\nCMMCCCCCCCCc\nCMCCCCCCCCcc\nCCCCCCCCCCcc\nCCCCCCCCCCcc\nCCCCCCCCCCcc\nCCCCCCCCCCcc\ncccccccccccc"
SNOW_PILE = ".....WWWW.....\n...WWWWWWWW...\n..WWWWWWWWWw..\n.WWWWWWWWWWww.\nWWWWWWWWWWWwww\n.wwwwwwwwwwww."
SAND_DUNE = "........SSSS........\n.....SSSSSSSSSs.....\n...SSSSSSSSSSSSss...\n.SSSSSSSSSSSSSSSsss.\nSSSSSSSSSSSSSSSSssss\nssssssssssssssssssss"
CLIFF = """
mMMMMMMMMMMMMMMd
mEEEEEEEEEEEEEEd
mMMMMMMMMMMMMMMd
mMMMMMMMMMMMMMMd
mmMMMMMmmMMMMMmd
mdmMMMmddmMMMmdd
mdmMMMmddmMMMmdd
mddmmmdddmmmmddd
dddddddddddddddd
"""
PUDDLE = "....LLLL....\n..LLCCCLLL..\n.LCCCCCCCLL.\n.LCCCCCCCLB.\n..LLCCCLLB..\n....BBBB...."
POND = """
.....LLLLLL.....
...LLCCCCCCLL...
..LCCCCCCCCCCL..
.LCCCCMMCCCCCCL.
.LCCCCCCCCCCCCB.
.LCCCCCCCCCCCCB.
..LCCCCCCCCCCB..
...LLCCCCCCBB...
.....BBBBBB.....
"""
WATERFALL_0 = "mMCCCCCCMd\nmMCCCMCCMd\nmMCMCCCCMd\nmMCCCCMCMd\nmMCCCCCCMd\nmMCMCCCCMd\nmMCCCMCCMd\nmMCCCCCCMd\nmMCCCCMCMd\nmMCCCCCCMd\nWWWWWWWWWW\n.WCWCWCWW."
WATERFALL_1 = "mMCCCCCCMd\nmMCCCCMCMd\nmMCCCMCCMd\nmMCMCCCCMd\nmMCCCCMCMd\nmMCCCCCCMd\nmMCMCCCCMd\nmMCCCMCCMd\nmMCCCCCCMd\nmMCCCCMCMd\nWWWWWWWWWW\n.WWCWCWCW."
GEYSER_0 = "....WW....\n...WWWW...\n...WWWW...\n....WW....\n....WW....\n..mmWWmm..\n.mMMMMMMd.\nmMMMMMMMMd\nmmmmmmmmdd"
GEYSER_1 = "....WW....\n...WWWW...\n..WWWWWW..\n..WWWWWW..\n...WWWW...\n..mmWWmm..\n.mMMMMMMd.\nmMMMMMMMMd\nmmmmmmmmdd"
CORAL = "..P....P..\n.PPP.PPPP.\n.PxP..PxP.\n..Px.PPx..\nPPPPxPxPPP\n.PxPPxPPx.\n..xxxxxx.."
SEASHELL = "..PPPP..\n.PWPWPP.\nPWPWPWPx\nPPPPPPPx\n.PxPxPx.\n..xxxx.."
STARFISH = "...AA...\n...AA...\nAAAAAAAA\n.AAAAAA.\n..AAAA..\n.AA..AA.\nAA....AA"
DRIFTWOOD = "..........Oo..\n.......OOOOo..\n..OOOOOOOoo...\nOOOOOOOooo....\noooooooo......"
ANCHOR = "....mm....\n...mMMd...\n....mm....\n....Md....\n.mm.Md.mm.\n.MmmMdmMd.\n..MMMMMd..\n...mmmd..."
BUOY = "....R.....\n...RRr....\n..RRRRr...\n..WWWWw...\n..RRRRr...\n..RRRRr...\n...rrr....\n..LLLLLL..\n.LLLLLLLB.\n..LLLLLB.."
ROWBOAT = "O..............O\nOo............Oo\nOOOOOOOOOOOOOOOo\n.OOooooooooooOo.\n..OOOOOOOOOOOo..\n...ooooooooo...."
DOCK = "OOOOOOOOOOOOOOOOOOOOOOOO\nOoOoOoOoOoOoOoOoOoOoOoOo\nOOOOOOOOOOOOOOOOOOOOOOOO\nnn....nn....nn....nn....\nnn....nn....nn....nn...."
CLOUD = "......WWWW......\n....WWWWWWWW....\n..WWWWWWWWWWWW..\n.WWWWWWWWWWWWWw.\nWWWWWWWWWWWWWWww\n.wwwwwwwwwwwwww."
RAIN_CLOUD = "......mmmm......\n....mmmmmmmm....\n..mmmmmmmmmmmm..\n.mmmmmmmmmmmmmd.\nmmmmmmmmmmmmmmdd\n.dddddddddddddd.\n..L..L..L..L....\n.L..L..L..L.....\n..L..L..L..L...."
SUN = "....Y.......\n.Y..Y..Y....\n..YYYYY.....\n.YYYYYYY....\nYYYYGYYYY...\n.YYYYYYY....\n..YYYYY.....\n.Y..Y..Y....\n....Y......."
MOON = "...YYYY...\n..YYYYYY..\n.YYYY..YY.\n.YYY....Y.\n.YYY......\n.YYY....Y.\n.YYYY..YY.\n..YYYYYY..\n...YYYY..."
TORNADO = "mmmmmmmmmmmm\n.mmmmmmmmmm.\n..mmmmmmmm..\n...mmmmmm...\n....mmmm....\n....mmmm....\n.....mm.....\n.....mm.....\n......m....."

# ---------------------------------------------------------------- outdoor and village props
STALL = """
RRRRWWWWRRRRWWWWRRRR
.RRRWWWWRRRRWWWWRRR.
.Oo..............Oo.
.Oo..............Oo.
.OOOOOOOOOOOOOOOOOo.
.OAAOORROOYYOOEEOOo.
.OAAOORROOYYOOEEOOo.
.OOOOOOOOOOOOOOOOOo.
.Oo..............Oo.
.oo..............oo.
"""
BARREL_APPLES = "..RR.RRR..\n.RRRRRRRR.\nmmmmmmmmmm\nOOOOOOOOoo\nOOOOOOOOoo\nmmmmmmmmmm\nOOOOOOOOoo\nOOOOOOOOoo\nmmmmmmmmmm\n.oooooooo."
FLOWER_BED = "P.R.Y.P.R.Y.P.\nPPRRYYPPRRYYPP\nEEEEEEEEEEEEEE\nOOOOOOOOOOOOOo\nnOOOOOOOOOOOOn\nnnnnnnnnnnnnnn"
LAMP_STONE = "...YY...\n..mYYd..\n..mYYd..\n..mMMd..\n...Md...\n...Md...\n...Md...\n...Md...\n..mMMd..\n.mMMMMd.\n.dddddd."
BIRDHOUSE = "...OOo...\n..OOOOo..\n.OOOOOOo.\nOOOOOOOOo\n.OOOKOOo.\n.OOOKOOo.\n.OOOOOOo.\n.ooooooo.\n....Oo...\n....Oo...\n....Oo...\n....Oo..."
BEEHIVE = "...GGGG...\n.GGGGGGGg.\nGgggggggGg\nGGGGGGGGGg\nGgggggggGg\nGGGGKGGGGg\n.GGGGGGGg.\n..gggggg.."
NEST = "...CC.CC..\n..CCCCCCC.\nOOooOOooOo\nOOOOOOOOOo\n.oOOOOOOo.\n..oooooo.."
COBWEB = "W.......W\n.W..W..W.\n..W.W.W..\n...WWW...\nWWWWWWWWW\n...WWW...\n..W.W.W..\n.W..W..W.\nW.......W"
HANGING_SIGN = "nnnnnnnnnnnn\n.....Nn.....\n.OOOOOOOOOo.\n.OhhhhhhhOo.\n.OOOOOOOOOo.\n.OhhhhOOOOo.\n.ooooooooo.."
WHEELBARROW = ".............Oo\n............Oo.\nOOOOOOOOOOOOo..\nOGGGGGGGGGOo...\n.OOOOOOOOOo....\n..DDD..oo......\n.DDMDD.........\n..DDD.........."
FIREWOOD = "...OoOoOo...\n..OoOoOoOo..\n.OoOoOoOoOo.\nOoOoOoOoOoOo"
TROUGH = "OOOOOOOOOOOOOo\nOCCCCCCCCCCCOo\nOCCCCCCCCCCCOo\nOOOOOOOOOOOOOo\n.Oo........Oo.\n.oo........oo."
HITCHING = "Oo.........Oo\nOOOOOOOOOOOOo\nOo.........Oo\nOo.........Oo\nOo.........Oo\noo.........oo"
MILESTONE = "..mMMMd..\n.mMMMMMd.\n.mMKMMMd.\n.mMMMMMd.\n.mMKKMMd.\n.mMMMMMd.\n.mMMMMMd.\nmmmmmmmdd"
OBELISK = "....Y....\n...mMd...\n...mMd...\n...mMd...\n...mMd...\n..mMMMd..\n..mMMMd..\n..mMMMd..\n..mMMMd..\n..mMMMd..\n.mMMMMMd.\n.ddddddd."
RUNE_STONE = "...mmmm...\n..mMMMMmd.\n.mMMCMMmdd\n.mMCCCMmdd\n.mMMCMMmdd\n.mMMCMMmdd\n.mMCMCMmdd\n.mMMMMMmdd\n.mmmmmmddd\n..dddddd.."
SHRINE = "......RRr......\n.RRRRRRRRRRRRr.\n..rrrrrrrrrrr..\n...Rr.....Rr...\n...Rr.....Rr...\n...Rr.YYY.Rr...\n...Rr.YGY.Rr...\n...Rr.YYY.Rr...\n..mmmmmmmmmmd..\n..dddddddddddd."
WOOD_GATE = "OOOOOOOOOOOOOOo\nOo...........Oo\nOo...........Oo\nOo.OOOOOOOOO.Oo\nOo.OoOoOoOoO.Oo\nOo.OOOOOOOOO.Oo\nOo.OoOoOoOoO.Oo\nOo.OOOOOOOOO.Oo\noo.ooooooooo.oo"
ARCH = "....mMMMMMMd....\n..mMMMMMMMMMMd..\n.mMMMmddddmMMMd.\nmMMMd......mMMMd\nmMMMd......mMMMd\nmMMMd......mMMMd\nmMMMd......mMMMd\nmMMMd......mMMMd\nmMMMd......mMMMd\nmmmmd......dmmmd"
BROKEN_PILLAR = "..mMMd.M..\n..mMMMd...\n..mMMMMd..\n..mMMMMd..\n..mMMMMd..\n..mMMMMd..\n.mMMMMMMd.\n.mmmmmmmd."
RUIN_WALL = "mMMMd.........\nmMMMMMd.......\nmMMMMMMMMd....\nmMMMMMMMMMMd..\nmMMMMMMMMMMMMd\nmMMMMMMMMMMMMd\nmmmmmmmmmmmmmd"
GRAVE_MOUND = "....OOOO....\n..OOOOOOOO..\n.OOOOOOOOOo.\nOOOOOOOOOOoo\noooooooooooo"
TOTEM = "..RRRRr..\n.RRKRKRr.\n.RRRRRRr.\n.RRKKKRr.\n..YYYYG..\n.YYKYKYG.\n.YYYYYYG.\n.YYKKKYG.\n..LLLLb..\n.LLKLKLb.\n.LLLLLLb.\n.LLKKKLb.\n.nnnnnnn."
FIRE_RING = "..mm.mm.mm..\n.mMMMMMMMMd.\nmMMnnnnnnMMd\nmMMnOoOonMMd\nmMMnnnnnnMMd\n.mmmmmmmmmd.\n..dd.dd.dd.."
STONE_CIRCLE = "...mMd....mMd...\n...mMd....mMd...\n...mMd....mMd...\nmMd.........mMd.\nmMd.........mMd.\nmMd.........mMd.\n...mMd....mMd...\n...mMd....mMd...\n...dddd...dddd.."
CRYSTAL_BALL = "...CCCC...\n..CMCCCc..\n.CMCCCCCc.\n.CCCCCCCc.\n..CCCCcc..\n...cccc...\n..mMMMMd..\n..dddddd.."
HOURGLASS = "mMMMMMMd\n.mSSSSd.\n.mSSSSd.\n..mSSd..\n...md...\n..m..d..\n.m.SS.d.\n.mSSSSd.\nmMMMMMMd"
TELESCOPE = ".........mMd\n........mMMd\n.......mMMd.\n......mMMd..\n.....mMMd...\n....mMMd....\n...mMMd.....\n...Oo.......\n..Oo.Oo.....\n.Oo...Oo...."
GLOBE = "...GGGG...\n..GLLCCGg.\n.GLECCCEGg\n.GCCEECCGg\n.GCECCCEGg\n..GCCEEGg.\n...GGGGg..\n....Gg....\n..GGGGGg.."
CANDELABRA = "Y...Y...Y\nA...A...A\nW...W...W\nWGGGWGGGW\n....G....\n....G....\n...GGG...\n..GGGGG.."
RUG = "RRRRRRRRRRRRRRRRRR\nRYYYYYYYYYYYYYYYYR\nRYRRRRRRRRRRRRRRYR\nRYRRYYYYYYYYYYRRYR\nRYRRRRRRRRRRRRRRYR\nRYYYYYYYYYYYYYYYYR\nrrrrrrrrrrrrrrrrrr"
CUSHION = "..VVVVVV..\n.VVVVVVVVv\nVVVVYVVVVv\nVVVVVVVVvv\n.vvvvvvvv."
FISH_RACK = "Oo.........Oo\nOOOOOOOOOOOOo\nOo.C..C..C.Oo\nOo.CC.CC.CCOo\nOo.c..c..c.Oo\nOo.........Oo\noo.........oo"
NET = "n..n..n..n\n.nn.nn.nn.\nn..n..n..n\n.nn.nn.nn.\nn..n..n..n\n.nn.nn.nn."
SCYTHE = "mMMMMMMMMd..\n.mmmmmmMMMd.\n.......mMMd.\n........Oo..\n........Oo..\n........Oo..\n........Oo..\n........Oo..\n........Oo..\n........oo.."
BASKET = "..NNNNNN..\n.NnNnNnNn.\nNNNNNNNNNn\nNnNnNnNnNn\nNNNNNNNNNn\n.nnnnnnnn."
PLANTER = "..E.P.E..\n.EEEPEEE.\n..EEEEE..\nmMMMMMMMd\nmMMMMMMMd\nmmmmmmmmd"
WINDMILL_BLADE = "WWWw......\n.WWWw.....\n..WWWw....\n...WWWw...\n....OOo...\n...wWWWW..\n..wWWW....\n.wWWW.....\nwWWW......"
HAY_BALE = ".GGGGGGGGGGGg.\nGGGGGGGGGGGGGg\nGGgggggggggGGg\nGGGGGGGGGGGGGg\nGGgggggggggGGg\nGGGGGGGGGGGGGg\n.ggggggggggg.."
WATER_LILY = "....P.....\n...PWP....\n..PPPPP...\n.EEEEEEEE.\nEEEEEE.EEE\nEEEEEEEEEe\n.EEEEEEEe.\n..eeeeee.."
FROZEN_POND = """
.....MMMMMM.....
...MMCCCCCCMM...
..MCCCCCCCCCCM..
.MCCCCMMCCCCCCM.
.MCCCCCCCCCCCCc.
.MCCCCCCCCCCCCc.
..MCCCCCCCCCCc..
...MMCCCCCCcc...
.....cccccc.....
"""
MUD_POOL = "....OOOO....\n..OOooooOO..\n.OooooooooO.\n.Ooooooooon.\n..OOooooon..\n....nnnn...."

# ---------------------------------------------------------------- register: trees and plants (28)
section("nature")
prop("tree_autumn", "단풍 든 나무. 주황 잎.", "Autumn tree", TREE, ("Eeq", "AAa"), bottom=29)
prop("tree_cherry", "벚나무. 분홍 꽃.", "Cherry tree", TREE, ("Eeq", "PPx"), bottom=29)
prop("tree_snowy", "눈 덮인 나무.", "Snowy tree", TREE, ("Eeq", "WwM"), bottom=29)
prop("tree_dark", "어두운 숲의 나무.", "Dark forest tree", TREE, ("Eeq", "eqq"), bottom=29)
prop("pine_snowy", "눈 덮인 소나무.", "Snowy pine", PINE, ("Eeq", "WwM"), bottom=29)
prop("willow", "버드나무. 늘어진 가지.", "Willow", WILLOW, bottom=29)
prop("palm", "야자수.", "Palm tree", PALM, bottom=29)
prop("birch", "자작나무. 흰 줄기.", "Birch", BIRCH, bottom=29)
prop("bamboo", "대나무 숲.", "Bamboo", BAMBOO, bottom=29)
prop("fern", "고사리.", "Fern", FERN)
prop("tall_grass", "키 큰 풀.", "Tall grass", TALL_GRASS)
prop("reeds", "갈대.", "Reeds", REEDS)
prop("cattail", "부들.", "Cattails", CATTAIL)
prop("lily_pad", "연잎.", "Lily pad", LILY_PAD, bottom=26)
prop("water_lily", "연꽃.", "Water lily", WATER_LILY, bottom=26)
prop("sunflower", "해바라기.", "Sunflower", SUNFLOWER, bottom=29)
prop("flower_red", "빨간 꽃 두 송이.", "Red flowers", FLOWER_RED)
prop("flower_blue", "파란 꽃.", "Blue flowers", FLOWER_RED, ("R", "L"))
prop("flower_white", "흰 꽃.", "White flowers", FLOWER_RED, ("R", "W"))
prop("tulips", "튤립 세 송이.", "Tulips", TULIPS)
prop("vine", "덩굴.", "Vine", VINE, bottom=27)
prop("ivy_wall", "담쟁이 덮인 벽.", "Ivy wall", IVY_WALL)
prop("berry_bush", "열매 덤불.", "Berry bush", BERRY_BUSH)
prop("flower_bush", "꽃 덤불.", "Flower bush", FLOWER_BUSH)
prop("bush_autumn", "가을 덤불.", "Autumn bush", BUSH, ("Eeq", "AAa"))
prop("hedge", "울타리 생울타리.", "Hedge", HEDGE)
prop("sapling", "묘목.", "Sapling", SAPLING)
prop("log_moss", "이끼 낀 통나무.", "Mossy log", LOG_MOSS)
prop("mushroom_glow", "발광 버섯.", "Glowing mushroom", MUSHROOM_GLOW)
prop("mushroom_giant", "거대 버섯.", "Giant mushroom", MUSHROOM_GIANT, bottom=29)
prop("mushroom_blue", "파란 버섯.", "Blue mushroom", MUSHROOM_BLUE)
prop("clover", "클로버.", "Clover", CLOVER, bottom=26)
prop("thorns", "가시덤불.", "Thorns", THORNS)

# rocks, terrain, water, sky (36)
prop("boulder", "큰 바위.", "Boulder", BOULDER)
prop("rock_moss", "이끼 낀 바위.", "Mossy rock", ROCK_MOSS)
prop("rock_pile", "돌무더기.", "Rock pile", ROCK_PILE)
prop("pebbles", "조약돌.", "Pebbles", PEBBLES)
prop("rock_dark", "검은 바위.", "Dark rock", ROCK, ("Mmd", "mdD"))
prop("rock_sand", "사암 바위.", "Sandstone rock", ROCK, ("Mmd", "SsN"))
prop("ore_iron", "철광석.", "Iron ore", ORE_IRON)
prop("ore_gold", "금광석.", "Gold ore", ORE_GOLD)
prop("ore_crystal", "수정 광석.", "Crystal ore", ORE_CRYSTAL)
prop("stalagmite", "석순.", "Stalagmite", STALAGMITE)
prop("stalactite", "종유석. 천장에 매단다.", "Stalactite", STALACTITE, bottom=12)
prop("cave_mouth", "동굴 입구.", "Cave mouth", CAVE_MOUTH, bottom=29)
prop("lava_rock", "용암 바위.", "Lava rock", LAVA_ROCK)
prop("ice_spike", "얼음 기둥.", "Ice spike", ICE_SPIKE)
prop("ice_block", "얼음 덩어리.", "Ice block", ICE_BLOCK)
prop("snow_pile", "눈 더미.", "Snow pile", SNOW_PILE)
prop("sand_dune", "모래 언덕.", "Sand dune", SAND_DUNE)
prop("cliff", "절벽 조각. 위에 풀.", "Cliff piece", CLIFF, bottom=29)
prop("puddle", "물웅덩이.", "Puddle", PUDDLE)
prop("pond", "작은 연못.", "Pond", POND)
prop("frozen_pond", "언 연못.", "Frozen pond", FROZEN_POND)
prop("mud_pool", "진흙 웅덩이.", "Mud pool", MUD_POOL)
prop("coral", "산호.", "Coral", CORAL)
prop("seashell", "조개껍데기.", "Seashell", SEASHELL, bottom=26)
prop("starfish", "불가사리.", "Starfish", STARFISH, bottom=26)
prop("driftwood", "유목.", "Driftwood", DRIFTWOOD)
prop("anchor", "닻.", "Anchor", ANCHOR)
prop("buoy", "부표.", "Buoy", BUOY, bottom=26)
prop("rowboat", "나룻배.", "Rowboat", ROWBOAT)
prop("dock", "부두 조각.", "Dock piece", DOCK)
prop("cloud", "구름.", "Cloud", CLOUD, bottom=20)
prop("rain_cloud", "비구름.", "Rain cloud", RAIN_CLOUD, bottom=22)
prop("sun", "해.", "Sun", SUN, bottom=20)
prop("moon", "초승달.", "Moon", MOON, bottom=20)
prop("tornado", "회오리.", "Tornado", TORNADO, bottom=28)


def waterfall():
    layers = [layer("w0", rows_of(WATERFALL_0), 11, 16), layer("w1", rows_of(WATERFALL_1), 11, 16)]
    return Recipe(meta=meta("waterfall", "Waterfall", (16, 27)), layers=layers,
                  frames={"base": [("w0", 0, 0)], "flow": [("w1", 0, 0)]}, anims={"flow": [("base", 120), ("flow", 120)]})


def geyser():
    layers = [layer("g0", rows_of(GEYSER_0), 11, 20), layer("g1", rows_of(GEYSER_1), 11, 20)]
    return Recipe(meta=meta("geyser", "Geyser", (16, 28)), layers=layers,
                  frames={"base": [("g0", 0, 0)], "spout": [("g1", 0, 0)]}, anims={"spout": [("base", 200), ("spout", 200)]})


spec("waterfall", "폭포. 2프레임 흐름.", waterfall)
spec("geyser", "간헐천. 2프레임 분출.", geyser)

# outdoor and village props (40)
section("props")
prop("stall", "시장 좌판. 줄무늬 차양.", "Market stall", STALL, bottom=29)
prop("barrel_apples", "사과 담긴 통.", "Apple barrel", BARREL_APPLES)
prop("flower_bed", "화단.", "Flower bed", FLOWER_BED)
prop("lamp_stone", "돌 가로등.", "Stone lamp", LAMP_STONE, bottom=29)
prop("birdhouse", "새집.", "Birdhouse", BIRDHOUSE, bottom=29)
prop("beehive", "벌집.", "Beehive", BEEHIVE, bottom=24)
prop("nest", "알이 든 둥지.", "Nest", NEST, bottom=26)
prop("cobweb", "거미줄.", "Cobweb", COBWEB, bottom=20)
prop("hanging_sign", "매단 간판.", "Hanging sign", HANGING_SIGN, bottom=22)
prop("wheelbarrow", "외바퀴 손수레.", "Wheelbarrow", WHEELBARROW)
prop("firewood", "장작 더미.", "Firewood", FIREWOOD)
prop("trough", "물통.", "Water trough", TROUGH)
prop("hitching_post", "말 매는 기둥.", "Hitching post", HITCHING)
prop("milestone", "이정석.", "Milestone", MILESTONE)
prop("obelisk", "오벨리스크.", "Obelisk", OBELISK, bottom=29)
prop("rune_stone", "룬 돌.", "Rune stone", RUNE_STONE)
prop("shrine", "작은 사당.", "Shrine", SHRINE, bottom=29)
prop("wood_gate", "나무 대문.", "Wooden gate", WOOD_GATE, bottom=29)
prop("arch", "돌 아치.", "Stone arch", ARCH, bottom=29)
prop("broken_pillar", "부서진 기둥.", "Broken pillar", BROKEN_PILLAR)
prop("ruin_wall", "폐허 벽.", "Ruin wall", RUIN_WALL)
prop("grave_mound", "봉분.", "Grave mound", GRAVE_MOUND)
prop("totem", "토템 기둥.", "Totem pole", TOTEM, bottom=29)
prop("fire_ring", "돌 화덕. 불 꺼짐.", "Fire ring", FIRE_RING)
prop("stone_circle", "환상열석.", "Stone circle", STONE_CIRCLE)
prop("crystal_ball", "수정구.", "Crystal ball", CRYSTAL_BALL, bottom=26)
prop("hourglass", "모래시계.", "Hourglass", HOURGLASS, bottom=26)
prop("telescope", "망원경.", "Telescope", TELESCOPE)
prop("globe", "지구본.", "Globe", GLOBE, bottom=26)
prop("candelabra", "촛대.", "Candelabra", CANDELABRA, bottom=26)
prop("rug", "양탄자.", "Rug", RUG)
prop("cushion", "방석.", "Cushion", CUSHION)
prop("fish_rack", "생선 건조대.", "Fish rack", FISH_RACK)
prop("net", "그물.", "Fishing net", NET)
prop("scythe", "낫.", "Scythe", SCYTHE)
prop("basket", "바구니.", "Basket", BASKET)
prop("planter", "돌 화분.", "Stone planter", PLANTER)
prop("windmill_blade", "풍차 날개.", "Windmill blades", WINDMILL_BLADE, bottom=24)
prop("hay_bale", "둥근 건초 더미.", "Hay bale", HAY_BALE)

# tiles (12)
section("tiles")
spec("tile_mud", "진흙 타일.", lambda: tile("tile_mud", "Mud tile", lambda x, y: "o", ("n", 40), 21))
spec("tile_gravel", "자갈 타일.", lambda: tile("tile_gravel", "Gravel tile", lambda x, y: "m", ("d", 60), 22))
spec("tile_swamp", "늪 물 타일.", lambda: tile("tile_swamp", "Swamp water", waves("q", "e", "D"), ("e", 10), 23))
spec("tile_deep_water", "깊은 물 타일.", lambda: tile("tile_deep_water", "Deep water", waves("B", "L", "b")))
spec("tile_wet_sand", "젖은 모래.", lambda: tile("tile_wet_sand", "Wet sand", lambda x, y: "s", ("N", 20), 24))
spec("tile_meadow", "꽃 핀 풀밭.", lambda: tile("tile_meadow", "Flower meadow", lambda x, y: "e", ("P", 14), 25))
spec("tile_leaves", "낙엽 바닥.", lambda: tile("tile_leaves", "Leaf litter", lambda x, y: "a", ("A", 40), 26))
spec("tile_snow_grass", "눈 섞인 풀.", lambda: tile("tile_snow_grass", "Snowy grass", checker("W", "e"), ("W", 30), 27))
spec("tile_cave_wall", "동굴 벽.", lambda: tile("tile_cave_wall", "Cave wall", bricks("d", "D", "K", "K", 8, 8)))
spec("tile_brick_moss", "이끼 낀 벽돌.", lambda: tile("tile_brick_moss", "Mossy brick wall", bricks("M", "m", "d", "K"), ("e", 24), 28))
spec("tile_wood_wall", "나무 벽.", lambda: tile("tile_wood_wall", "Wooden wall", planks("O", "o", "n")))
spec("tile_thatch", "초가지붕.", lambda: tile("tile_thatch", "Thatch roof", planks("Y", "G", "g"), ("g", 30), 29))
