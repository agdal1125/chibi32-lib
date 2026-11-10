"""kit32_gaps: 50 assets that fill holes found when reviewing the whole set:
friendly animals, buildings, spell effects, UI and status icons, missing equipment, indoor furniture.
Imported by kit32 at the end of its module; registers into kit32.SPECS."""
from kit32 import section, SHIELD, Recipe, centered, item, layer, meta, recolor, rows_of, spec


def prop(aid, desc, title, grid, *maps, bottom=28):
    spec(aid, desc, lambda: item(aid, title, grid, *maps, bottom=bottom))


def fx(aid, desc, title, g0, g1, ms=110, bottom=24, maps0=(), maps1=()):
    """Two-frame looping effect. Both grids are centered and share the same bottom row."""
    def build():
        r0, r1 = recolor(g0, *maps0), recolor(g1, *maps1)
        (x0, y0), (x1, y1) = centered(r0, bottom), centered(r1, bottom)
        layers = [layer("f0", r0, x0, y0), layer("f1", r1, x1, y1)]
        return Recipe(meta=meta(aid, title, (16, bottom)), layers=layers,
                      frames={"base": [("f0", 0, 0)], "alt": [("f1", 0, 0)]},
                      anims={"loop": [("base", ms), ("alt", ms)]})
    spec(aid, desc, build)


def roll(grid: str) -> str:
    rows = rows_of(grid)
    return "\n".join(rows[1:] + rows[:1])


def mirror(grid: str) -> str:
    return "\n".join(row[::-1] for row in rows_of(grid))


# ---------------------------------------------------------------- friendly animals (10)
section("animals")
CAT = """
A..........A.A
A..........AAA
A.........AAKA
AAAAAAAAAAAAAA
.AAAAAAAAAApA.
.AAAAAAAAAAA..
.Aa.Aa..Aa.Aa.
.aa.aa..aa.aa.
"""
DOG = """
............OO..
N..........OOOO.
N.........NOOKOO
NOOOOOOOOOOOOOOK
.OOOOOOOOOOOOO..
.OOOOOOOOOOOO...
.Oo.Oo...Oo.Oo..
.oo.oo...oo.oo..
"""
CHICKEN = """
......RR..
.....WWW..
.....WKWA.
W...WWWWR.
WW.WWWWW..
WWWWWWWW..
.WWWWWWw..
..WWWWw...
...A.A....
...A.A....
"""
COW = """
............M..M
...........WWWW.
WWWWWWWWWWWWKWW.
WDDWWWWDDWWWWPP.
WDDWWWWDDWWWWPP.
WWWWWDDWWWWWW...
WWWWWDDWWWWW....
.Ww.Ww...Ww.Ww..
.Dd.Dd...Dd.Dd..
"""
PIG = """
..........P.P.
.PPPPPPPPPPPP.
PPPPPPPPPPKPPx
PPPPPPPPPPPPxx
PPPPPPPPPPPPP.
.PPPPPPPPPPP..
.Px.Px..Px.Px.
"""
HORSE = """
...........OOo..
..........OOOOo.
..........OOKOOo
n.........OOOOOo
nOOOOOOOOOOOOo..
nOOOOOOOOOOOO...
.OOOOOOOOOOOO...
.OOOOOOOOOOOo...
.Oo.Oo...Oo.Oo..
.Oo.Oo...Oo.Oo..
.DD.DD...DD.DD..
"""
DEER = "...........N.N..\n..........NN.NN.\n" + HORSE.strip("\n")
RABBIT = """
.....W.W.
.....W.W.
.....WWW.
....WWKWW
WWWWWWWWP
WWWWWWWW.
.WWWWWWW.
.Ww..Ww..
"""
SHEEP = """
..WWWWWWWW....
.WWWWWWWWWWDD.
WWWWWWWWWWDKD.
WWWWWWWWWWDDD.
WWWWWWWWWWW...
.WWWWWWWWW....
..D.D..D.D....
..D.D..D.D....
"""
BIRD = "...LLL...\n..LLKLA..\nLLLLLLL..\n.LLLLBB..\n..LLBB...\n...A.A..."

prop("cat", "고양이. 주황 줄무늬 없는 단색.", "Cat", CAT)
prop("dog", "개. 처진 귀의 갈색 개.", "Dog", DOG)
prop("chicken", "닭.", "Chicken", CHICKEN)
prop("cow", "젖소.", "Cow", COW)
prop("pig", "돼지.", "Pig", PIG)
prop("horse", "말.", "Horse", HORSE)
prop("deer", "사슴. 뿔 달린 수사슴.", "Deer", DEER, ("n", "W"))
prop("rabbit", "토끼.", "Rabbit", RABBIT)
prop("sheep", "양.", "Sheep", SHEEP)
prop("bird", "파랑새.", "Bluebird", BIRD, bottom=24)

# ---------------------------------------------------------------- buildings (8)
section("buildings")
HOUSE = """
.........RR.........
.......RRRRRR.......
.....RRRRRRRRRR.....
...RRRRRRRRRRRRRR...
.RRRRRRRRRRRRRRRRRR.
rrrrrrrrrrrrrrrrrrrr
.WWWWWWWWWWWWWWWWWw.
.WCCCWWWWWWWWCCCWWw.
.WCCCWWOOOOWWCCCWWw.
.WWWWWWOOOOWWWWWWWw.
.WWWWWWOOGOWWWWWWWw.
.WWWWWWOOOOWWWWWWWw.
.wwwwwwoooowwwwwwww.
"""
TOWER = """
m.mm.mm.mm.m
mMMMMMMMMMMd
mMMMMMMMMMMd
.mMMMMMMMMd.
.mMMMDDMMMd.
.mMMMDDMMMd.
.mMMMMMMMMd.
.mMMMMMMMMd.
.mMMMDDMMMd.
.mMMMDDMMMd.
.mMMMMMMMMd.
.mMMMMMMMMd.
.mMMMOOMMMd.
.mMMOOOOMMd.
.mMMOOOOMMd.
.mmmoooommd.
"""
CHURCH = """
.......GG.......
......GGGG......
.......GG.......
.......WW.......
......WWWw......
.....WWCCWw.....
....LLLLLLLL....
...LLLLLLLLLL...
..LLLLLLLLLLLL..
.bbbbbbbbbbbbbb.
.WWWWWWWWWWWWWw.
.WCCWWWOOWWCCWw.
.WCCWWOOOOWCCWw.
.WWWWWOOOOWWWWw.
.wwwwwoooowwwww.
"""
BARN = """
.......RRRRRR.......
.....RRRRRRRRRR.....
...RRRRRRRRRRRRRR...
..RRRRRRRWWRRRRRRR..
.RRRRRRRRWWRRRRRRRR.
.rrrrrrrrrrrrrrrrrr.
.RRRRRWWWWWWWWRRRRr.
.RRRRRWOOWWOOWRRRRr.
.RRRRRWOWOOWOWRRRRr.
.RRRRRWOOWWOOWRRRRr.
.RRRRRWOWOOWOWRRRRr.
.rrrrrwwwwwwwwrrrrr.
"""
CASTLE_WALL = """
mMMd..mMMd..mMMd..mMMd..
mMMd..mMMd..mMMd..mMMd..
mMMMMMMMMMMMMMMMMMMMMMMd
mMMMMMmMMMMMmMMMMMmMMMMd
mMMMMMMMMMMMMMMMMMMMMMMd
mMMmMMMMMmMMMMMmMMMMMmMd
mMMMMMMMMMMMMMMMMMMMMMMd
mMMMMMmMMMMMmMMMMMmMMMMd
mmmmmmmmmmmmmmmmmmmmmmdd
"""
CASTLE_GATE = """
mMd.mMd.mMMd.mMd.mMd
mMMMMMMMMMMMMMMMMMMd
mMMMMMMMMMMMMMMMMMMd
mMMMMMDDDDDDDDMMMMMd
mMMMMDDOOOOOODDMMMMd
mMMMMDOOOOOOOODMMMMd
mMMMMDOoOOooOoDMMMMd
mMMMMDOoOOooOoDMMMMd
mMMMMDOoOOooOoDMMMMd
mmmmmDOoOOooOoDmmmmd
"""
prop("house", "붉은 지붕 집.", "House (red roof)", HOUSE, bottom=29)
prop("house_blue", "푸른 지붕 집.", "House (blue roof)", HOUSE, ("Rr", "Lb"), bottom=29)
prop("shop", "상점. 초록 지붕, 불 켜진 창.", "Shop", HOUSE, ("Rr", "Eq"), ("C", "Y"), bottom=29)
prop("tower", "돌 망루.", "Stone tower", TOWER, ("Mm", "md"), bottom=29)
prop("church", "교회. 금 십자가.", "Church", CHURCH, bottom=29)
prop("barn", "붉은 헛간.", "Barn", BARN, bottom=29)
prop("castle_wall", "성벽 조각.", "Castle wall", CASTLE_WALL, ("Mm", "md"), bottom=29)
prop("castle_gate", "성문.", "Castle gate", CASTLE_GATE, ("Mm", "md"), bottom=29)

# ---------------------------------------------------------------- spell and combat effects (10)
section("effects")
FIREBALL_0 = ".....RRRR...\n..RRRAAAAR..\nRRAAAAYYYAR.\n.RRAAYYYYAR.\nRRAAAAYYYAR.\n..RRRAAAAR..\n.....RRRR..."
FIREBALL_1 = ".....RRRR...\n.RRRRAAAAR..\n..RAAAYYYAR.\nRRRAAYYYYAR.\n..RAAAYYYAR.\n.RRRRAAAAR..\n.....RRRR..."
LIGHTNING = "....YY..\n...YY...\n..YY....\n.YYYYY..\n...YY...\n..YY....\n.YY.....\nYYYY....\n..YY....\n.YY.....\nYY......"
HEAL = "....E.....\n...EEE....\n....E...E.\n.......EEE\n.E......E.\nEEE.......\n.E...E....\n....EEE...\n.....E...."
SLASH = ".......WWW..\n.....WWWWWW.\n...WWWW..WWW\n..WWW......W\n.WWW........\n.WW.........\nWW..........\nW..........."
BOOM_0 = "...RRRR...\n.RRAAAARR.\nRAAYYYYAAR\nRAYYWWYYAR\nRAYYWWYYAR\nRAAYYYYAAR\n.RRAAAARR.\n...RRRR..."
BOOM_1 = "R...RRRR...R\n.RRRAAAARRR.\n.RAAAYYAAAR.\nRAAYYYYYYAAR\nRAYYYWWYYYAR\nRAYYWWWWYYAR\nRAYYYWWYYYAR\nRAAYYYYYYAAR\n.RAAAYYAAAR.\n.RRRAAAARRR.\nR...RRRR...R"
CLOUD_P = "...VVVV.....\n.VVVVVVV.VV.\nVVVEVVVVVVVV\nVVVVVVVEVVVv\n.VVVVVVVVVv.\n..vvVVVvvv.."
BUBBLE = "....CCCCCC....\n..CC......CC..\n.C..M.......C.\n.C.M........C.\nC............C\nC............C\nC............C\nC............C\n.C..........c.\n.C..........c.\n..CC......cc..\n....CCcccc...."
SPARK_0 = "....Y....\n....Y....\n...YWY...\nYYYWWWYYY\n...YWY...\n....Y....\n....Y...."
SPARK_1 = "....Y....\n...YWY...\n..YWWWY..\n...YWY...\n....Y...."
SMOKE = "...mmm....\n..mMMMm...\n.mMMMMMm.m\nmMMMMMMmmM\n.mMMMMmmMm\n..mmmm.mm."

fx("fireball", "화염구. 오른쪽으로 날아간다.", "Fireball", FIREBALL_0, FIREBALL_1, bottom=20)
fx("ice_bolt", "얼음 화살.", "Ice bolt", FIREBALL_0, FIREBALL_1, bottom=20,
   maps0=(("RAY", "cCW"),), maps1=(("RAY", "cCW"),))
fx("lightning", "번개. 노랑과 흰색으로 번쩍인다.", "Lightning", LIGHTNING, LIGHTNING, ms=80, bottom=26, maps1=(("Y", "W"),))
fx("heal_fx", "치유 효과. 초록 십자가 떠오른다.", "Heal effect", HEAL, roll(HEAL), ms=140)
fx("slash_fx", "베기 궤적.", "Slash effect", SLASH, SLASH, ms=70, maps1=(("W", "m"),))
fx("explosion", "폭발. 작게, 크게.", "Explosion", BOOM_0, BOOM_1, ms=100)
fx("poison_cloud", "독구름.", "Poison cloud", CLOUD_P, mirror(CLOUD_P), ms=220)
prop("shield_bubble", "보호막. 캐릭터 위에 겹쳐 쓴다.", "Shield bubble", BUBBLE, bottom=27)
fx("sparkle", "반짝임. 아이템 강조용.", "Sparkle", SPARK_0, SPARK_1, ms=160, bottom=22)
fx("smoke", "연기.", "Smoke puff", SMOKE, mirror(SMOKE), ms=200)

# ---------------------------------------------------------------- UI and status icons (11)
section("ui")
CURSOR = "W.......\nWW......\nWMW.....\nWMMW....\nWMMMW...\nWMMMMW..\nWMMMMMW.\nWMMWWWWW\nWMW.....\nWW......"
SPEECH = ".WWWWWWWWWWWWWW.\nWWWWWWWWWWWWWWWW\nWWDDDDDDDDDDWWWW\nWWWWWWWWWWWWWWWW\nWWDDDDDDDWWWWWWW\nWWWWWWWWWWWWWWWW\n.WWWWWWWWWWWWWW.\n...WWW..........\n...WW...........\n...W............"
EXCLAIM = ".YY.\nYYYY\nYYYY\nYYYY\n.YY.\n.YY.\n....\n.YY.\n.YY."
QUESTION = ".YYYYY.\nYYY.YYY\nYY...YY\n....YYY\n...YYY.\n...YY..\n.......\n...YY..\n...YY.."
BAR = "MMMMMMMMMMMMMMMMMMMM\nMRRRRRRRRRRRRRKKKKKM\nMrrrrrrrrrrrrrKKKKKM\nMMMMMMMMMMMMMMMMMMMM"
DROP = "...VV...\n...VV...\n..VVVV..\n..VVVV..\n.VMVVVv.\nVMVVVVVv\nVVVVVVVv\nVVVVVVvv\n.VVVVvv.\n..vvvv.."
ZZZ = ".......WWWWW\n..........W.\n.........W..\n........W...\n.......WWWWW\n.WWWW.......\n...W........\n..W.........\n.WWWW......."
SKULL = "..MMMMMM..\n.MMMMMMMM.\nMMMMMMMMMm\nMKKMMMKKMm\nMKKMMMKKMm\nMMMMKMMMMm\n.MMMMMMMm.\n..MKMKMm..\n..MMMMMm.."
TARGET = "....RRR....\n..RR.R.RR..\n.R...R...R.\n.R...R...R.\nR....R....R\nRRRRR.RRRRR\nR....R....R\n.R...R...R.\n.R...R...R.\n..RR.R.RR..\n....RRR...."
LEVEL_UP = "....E....\n...EEE...\n..EEEEE..\n.EEEEEEE.\nEEEEEEEEE\n...EEE...\n...EEE...\n...EEE...\n...eee..."

prop("cursor", "커서. 메뉴 선택용 화살표.", "Cursor", CURSOR, bottom=22)
prop("speech_bubble", "말풍선.", "Speech bubble", SPEECH, bottom=22)
prop("exclaim", "느낌표. 퀘스트 알림.", "Exclamation mark", EXCLAIM, bottom=22)
prop("question", "물음표. 퀘스트 완료 대기.", "Question mark", QUESTION, bottom=22)
prop("hp_bar", "체력 바. 70% 찬 상태.", "HP bar", BAR, bottom=18)
prop("mp_bar", "마나 바.", "MP bar", BAR, ("Rr", "LB"), bottom=18)
prop("icon_poison", "중독 상태 아이콘.", "Poison status", DROP, bottom=22)
prop("icon_sleep", "수면 상태 아이콘.", "Sleep status", ZZZ, bottom=22)
prop("icon_skull", "즉사·위험 아이콘.", "Skull icon", SKULL, bottom=22)
prop("target", "조준 표식.", "Target marker", TARGET, bottom=22)
prop("level_up", "레벨 업 화살표.", "Level-up arrow", LEVEL_UP, bottom=22)

# ---------------------------------------------------------------- equipment and food gaps (5)
section("items")
GLOVES = ".NN.....NN..\nNNNN...NNNN.\nNNNNN..NNNNN\nNNNNN..NNNNN\n.NNNn...NNNn\n.nnnn...nnnn"
CAPE = ".GG....GG.\nRRRRRRRRRR\nRRRRRRRRRr\nRRRRRRRRRr\nRRRRRRRRRr\nRRRRRRRRrr\nRRRRRRRRrr\nRRRRRRRrrr\n.RRRRRrrr.\n.Rr.RRr.r."
AMULET = ".G.....G.\nG.......G\nG.......G\n.G.....G.\n..G...G..\n...GGG...\n..GCCCG..\n..GCMCG..\n..GCCCG..\n...GGG..."
CROWN_ITEM = "G....G....G\nGG..GGG..GG\nGGGGGGGGGGG\nGRGGGLGGGRG\nGGGGGGGGGGg\nggggggggggg"
CARROT = "...E.E..\n..EEEE..\n...EE...\n..AAAA..\n..AAAa..\n..AAAa..\n...AAa..\n...AAa..\n....Aa..\n....a..."

prop("gloves", "가죽 장갑.", "Leather gloves", GLOVES, bottom=24)
prop("cape", "붉은 망토.", "Red cape", CAPE, bottom=25)
prop("amulet", "수정 목걸이.", "Crystal amulet", AMULET, bottom=25)
prop("crown_item", "왕관.", "Crown", CROWN_ITEM, bottom=24)
prop("shield_iron", "철 방패.", "Iron shield", SHIELD, ("Oo", "Mm"), ("Gg", "Lb"), bottom=24)
prop("carrot", "당근.", "Carrot", CARROT, bottom=25)

# ---------------------------------------------------------------- indoor furniture (4 + fireplace)
section("props")
FIREPLACE_0 = """
mMMMMMMMMMMMMMMd
mMMMMMMMMMMMMMMd
.mMMMMMMMMMMMMd.
.mMDDDDDDDDDDMd.
.mMDDDDDDDDDDMd.
.mMDDDDRDDDDDMd.
.mMDDDRADDDDDMd.
.mMDDRAYARDDDMd.
.mMDDRAYYARDDMd.
.mMDOOOOOOOODMd.
mMMMMMMMMMMMMMMd
mmmmmmmmmmmmmmdd
"""
FIREPLACE_1 = FIREPLACE_0.replace(".mMDDDDRDDDDDMd.", ".mMDDDDDRDDDDMd.").replace(".mMDDDRADDDDDMd.", ".mMDDDDARDDDDMd.")
CLOCK = ".OOOOOO.\nOOOOOOOo\nOWWWWWOo\nOWWKWWOo\nOWWKKWOo\nOWWWWWOo\nOOOOOOOo\n.OOOOOo.\n.ODDDOo.\n.ODGDOo.\n.ODGDOo.\n.ODGDOo.\n.ODGGOo.\n.ODDDOo.\nOOOOOOOo\noooooooo"
CUPBOARD = "OOOOOOOOOOOOOo\nOCCCCCOOCCCCOo\nOCCCCCOOCCCCOo\nOCCCCCOOCCCCOo\nOOOOOOOOOOOOOo\nOOOOOGOOGOOOOo\nOOOOOOOOOOOOOo\nOOOOOGOOGOOOOo\nOOOOOOOOOOOOOo\noooooooooooooo"
MIRROR = "..GGGGGG..\n.GCCCCCCg.\nGCCMCCCCCg\nGCMCCCCCCg\nGCCCCCCCCg\nGCCCCCCCCg\nGCCCCCCCCg\n.GCCCCCCg.\n..GGGGgg..\n....Gg....\n...GGGg..."
THRONE = "..GG....GG..\n.GRRRRRRRRg.\n.GRRRRRRRRg.\n.GRRYYYYRRg.\n.GRRRRRRRRg.\n.GRRRRRRRRg.\nGGRRRRRRRRgg\nGGRRRRRRRRgg\nGGGGGGGGGGgg\nGGRRRRRRRRgg\nGGGGGGGGGGgg\n.Gg......Gg."

fx("fireplace", "벽난로. 불꽃이 흔들린다.", "Fireplace", FIREPLACE_0, FIREPLACE_1, ms=150, bottom=29)
prop("clock", "괘종시계.", "Grandfather clock", CLOCK, bottom=29)
prop("cupboard", "찬장. 유리문.", "Cupboard", CUPBOARD, bottom=29)
prop("mirror", "전신 거울.", "Mirror", MIRROR, bottom=29)
prop("throne", "왕좌.", "Throne", THRONE, bottom=29)
