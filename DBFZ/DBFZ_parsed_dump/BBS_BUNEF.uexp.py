@State
def dmy():
    sprite('null', 1)

@State
def okasi():

    def upon_IMMEDIATE():
        callSubroutine('cmn_okasi')
    sprite('null', 2147483647)
    Unknown450('bun_okasi')

@State
def bun_600_step0():

    def upon_IMMEDIATE():
        Unknown94(-600000)
        Unknown1732(-120000)
    sprite('null', 1)
    Unknown448('bg_bun600_step', 100)

@State
def bun_600_step1():

    def upon_IMMEDIATE():
        Unknown94(-275000)
        Unknown1732(-120000)
    sprite('null', 1)
    Unknown448('bg_bun600_step', 100)

@State
def bun_600_step2():
    sprite('null', 1)
    Unknown448('bg_bun600_step2', 100)

@State
def bun_600Eff():
    sprite('null', 4)
    sprite('null', 82)
    Unknown450('cmn_syutyusen')

@State
def bun610cs_01_manpu():

    def upon_IMMEDIATE():
        Unknown454(3)
        Unknown456(3)
        Unknown457(3)
        Unknown294(1)
        Unknown451('4d4e5000000000000000000000000000000000000000000000000000000000004d4e505f42554e36313063735f30310000000000000000000000000000000000')
    sprite('null', 600)

@State
def bun_201Eff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
    sprite('null', 60)
    Unknown450('bun_201_kick')

@State
def bun_202Eff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown294(1)
        Unknown99(350000)
        Unknown94(250000)
    sprite('null', 60)
    Unknown450('bun_202_punch')

@State
def bun_203Eff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
    sprite('null', 60)
    Unknown450('bun_203_heading')

@State
def bun_204Eff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 60)
    Unknown450('bun_204_kick')

@State
def bun_204Eff_smoke():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown471('62675f62756e3230345f736d6f6b650000000000000000000000000000000000')
        Unknown188(1200)
        Unknown94(15000)
    sprite('null', 6)
    sprite('null', 60)
    Unknown454(0)

@State
def bun_204Eff_strike():

    def upon_IMMEDIATE():
        Unknown164(90000)
        Unknown99(300000)
        Unknown94(180000)
    sprite('null', 60)
    Unknown450('cmn_strike00')

@State
def bun_231Eff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 60)
    Unknown450('bun_231_swing')

@State
def bun_232Eff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 60)
    Unknown450('bun_232_upper')

@State
def bun_232Eff_strike():

    def upon_IMMEDIATE():
        Unknown164(-25000)
        Unknown99(275000)
        Unknown94(230000)
    sprite('null', 60)
    Unknown450('cmn_strike00')

@State
def bun_261Eff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
        Unknown99(-60000)
    sprite('null', 60)
    Unknown450('bun_261_punch')
    Unknown612('ARC_BTL_CMN_Hit_Small_Set')

@State
def bun_262Eff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
        Unknown164(-10000)
    sprite('null', 60)
    Unknown450('bun_262_punch')

@State
def bun_262Eff_strike():

    def upon_IMMEDIATE():
        Unknown164(60000)
        Unknown99(250000)
        Unknown94(425000)
    sprite('null', 60)
    Unknown450('cmn_strike00')

@State
def bun_263Eff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
        Unknown164(10000)
    sprite('null', 60)
    Unknown450('bun_263_punch')

@State
def bun_263Eff_strike():

    def upon_IMMEDIATE():
        Unknown164(90000)
        Unknown99(360000)
        Unknown94(300000)
    sprite('null', 60)
    Unknown450('cmn_strike00')

@State
def bun_hajiki():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 30)
    Unknown450('bun_hajiki')

@State
def kidan_5D():

    def upon_IMMEDIATE():
        Unknown243()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        callSubroutine('cmn5DKidan_AtkInit')
        callSubroutine('cmnKidan_Init')
        damage1(300)
        airHitPushbackY(8000)
        Unknown1143(1)
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
        Unknown2229(102)
        Unknown450('bun_kidan')

        def upon_49():
            if Unknown2041('Kidan_5D'):
                Unknown23(49)
                Unknown23(3)

                def upon_8():
                    ActivateEffScript('cmn_kidan_end', 100)
        if Unknown2033(3, 'NmlAtk5D'):
            if (not 
            Unknown53(23, 2, 0, 3, 2, 45)):
                or_standhit(8)
                or_launchhit(8)
                airHitPushbackX(20000)
                airHitPushbackY(18000)
    sprite('kidan', 1)
    makeActive()
    Unknown338(0)
    sprite('kidan', 2147483647)
    Unknown338(255)
    Unknown58(1)
    Unknown202(80000, 0)
    label('Koware')
    sprite('null', 10)
    Unknown176(1)
    Unknown450('')

@State
def kidan_smoke():

    def upon_IMMEDIATE():
        Unknown94(-150000)
    sprite('null', 1)
    Unknown448('bg_undersmoke00', 100)

@State
def crouchkidan():

    def upon_IMMEDIATE():
        Unknown243()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        callSubroutine('cmn2DKidan_AtkInit')
        callSubroutine('cmnKidan_Init')
        untech_Override(27)
        airHitPushbackX(5000)
        airHitPushbackY(32000)
        Unknown1117(800)
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
        Unknown99(10000)
        Unknown1731(-50000)
        Unknown164(38000)
        Unknown2230(102)
        Unknown2229(102)
        Unknown450('bun_kidan')
    sprite('kidan_nanameue0', 1)
    makeActive()
    Unknown338(0)
    sprite('kidan_nanameue1', 2147483647)
    Unknown58(1)
    Unknown338(255)
    Unknown202(90000, 0)
    label('Koware')
    sprite('null', 10)
    Unknown176(1)
    Unknown450('')

@State
def kidan_Air():

    def upon_IMMEDIATE():
        Unknown243()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        callSubroutine('cmnAir5DKidan_AtkInit')
        callSubroutine('cmnKidan_Init')
        damage1(300)
        untech_Override(20)
        Unknown1143(1)
        airHitPushbackY(10000)
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
        Unknown2229(102)
        Unknown2230(102)
        Unknown164(-30000)
        Unknown450('bun_kidan')

        def upon_49():
            if Unknown2041('kidan_Air'):
                Unknown23(49)
                Unknown23(3)

                def upon_8():
                    ActivateEffScript('cmn_kidan_end', 100)
        if Unknown2033(3, 'NmlAtkAir5D'):
            if (not 
            Unknown53(23, 2, 0, 3, 2, 45)):
                or_standhit(8)
                or_launchhit(8)
                airHitPushbackY(15000)

        def upon_23():
            Unknown164(-20000)

        def upon_24():
            Unknown164(-40000)
    sprite('kidan_nanamesita', 1)
    makeActive()
    Unknown338(0)
    sprite('kidan_nanamesita', 2147483647)
    Unknown338(255)
    Unknown58(1)
    Unknown202(80000, 0)
    label('Koware')
    sprite('null', 10)
    Unknown176(1)
    Unknown450('')

@State
def Mountdive_Shock():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkLevel_1_AtkInit')
        callSubroutine('cmnSpecialShot_AtkInit')
        damage1(700)
        mod_hitstop(6)
        untech_Override(30)
        airHitPushbackY(13000)
        or_standhit(10)
        or_launchhit(10)
        Unknown1190(1)
        Unknown911(0)
        Unknown1954(1)
        Unknown458(3)
        Unknown454(3)
        Unknown289(60)

        def upon_23():
            callSubroutine('cmnSpecialAttackEx_ShotInit')

        def upon_8():
            Unknown2040(3, 'Mount_Shock_Hit', 0)
    sprite('mountdive_shock', 3)
    makeActive()
    Unknown469('62675f62756e3430305f7374616d70000000000000000000000000000000000064000000')

@State
def bun400_JumpSmoke():
    sprite('null', 1)
    Unknown448('bg_jump_default', 100)

@State
def bun_401Eff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 30)
    Unknown450('bun_401_kick')

@State
def Sbreath():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkLevel_3_AtkInit')
        callSubroutine('cmnSpecialShot_AtkInit')
        damage1(1100)
        Unknown1117(1500)
        mod_hitstop(5)
        or_standhit(27)
        or_launchhit(27)
        untech_Override(35)
        airHitPushbackX(10000)
        airHitPushbackY(45000)
        Unknown1051(0)
        Unknown717('ShakeYoko', 800, 5, 25, 5)
        Unknown1118('ARC_BTL_CMN_Hit_Kidan')
        Unknown1119('ARC_BTL_CMN_Guard_Kidan')
        if Unknown2033(3, 'AssistAttack'):
            damage1(800)
            Unknown1117(0)
            untech_Override(40)
        callSubroutine('cmn_AssistShotHosei')
        Unknown1954(1)
        Unknown289(300)
        Unknown1732(75000)
        Unknown294(1)
        Unknown454(2)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
        Unknown35('2f000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('sbreath0', 8)
    makeActive()
    Unknown450('bun_402_loop')
    sprite('sbreath1', 6)
    sprite('null', 60)
    label('end')
    sprite('null', 60)
    Unknown23(23)
    Unknown23(47)
    Unknown454(0)
    Unknown450('bun_402_end')

@State
def Air_Sbreath():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkLevel_3_AtkInit')
        callSubroutine('cmnSpecialShot_AtkInit')
        damage1(1100)
        Unknown1117(1500)
        mod_hitstop(5)
        or_standhit(27)
        or_launchhit(27)
        untech_Override(35)
        airHitPushbackX(10000)
        airHitPushbackY(45000)
        Unknown1051(0)
        Unknown717('ShakeYoko', 800, 5, 25, 5)
        Unknown1118('ARC_BTL_CMN_Hit_Kidan')
        Unknown1119('ARC_BTL_CMN_Guard_Kidan')
        Unknown1954(1)
        Unknown289(300)
        Unknown1732(75000)
        Unknown294(1)
        Unknown454(2)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
        Unknown35('2f000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('sbreath0', 8)
    makeActive()
    Unknown450('bun_402_loop')
    sprite('sbreath1', 6)
    sprite('null', 60)
    label('end')
    sprite('null', 60)
    Unknown23(23)
    Unknown23(47)
    Unknown454(0)
    Unknown450('bun_402_end')

@State
def fat_bullet():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkLevel_1_AtkInit')
        callSubroutine('cmnSpecialShot_AtkInit')
        mod_hitstop(7)
        Unknown1059(1)
        if (SLOT_115 >= 2):
            callSubroutine('cmn_AssistHosei')
        Unknown1629(1)
        Unknown458(0)
        Unknown1914(50000)
        Unknown1954(1)
        Unknown289(600)
        Unknown450('bun_404_jizoku')
        Unknown1731(0)
        Unknown2211(1)
        Unknown2217(1)
        Unknown2213(1)
        Unknown2214(1)
        Unknown2215(1)
        Unknown1118('dammyName')

        def upon_89():
            if SLOT_16:
                if SLOT_266:
                    Unknown2208(23)
                else:
                    storeValue(2, 266, 0, 1)
                    Unknown450('bun_404_bind_loop')
                    if Unknown67(0):
                        Unknown188(700)
                    if Unknown67(1):
                        pass
                    if Unknown67(2):
                        Unknown188(1500)
                    if Unknown67(3):
                        Unknown188(1750)
                    callSubroutine('cmnAtkTemplNageExe')
                    grHitPushbackX(0)
                    hitstun_Override(300)
                    untech_Override(300)
                    airHitPushbackX(0)
                    airHitPushbackY(0)
                    Unknown1095(500)
                    Unknown717('ShakeYoko', 400, 5, 30, 5)
                    or_standhit(17)
                    or_launchhit(17)
                    Unknown1149(46)
                    if (SLOT_115 == 1):
                        callSubroutine('cmnSpecialAttackEx_ShotInit')
                        damage1(100)
                        Unknown1095(1000)
                        Unknown1204(1)
                        Unknown296(300)
                    if (SLOT_115 >= 2):
                        callSubroutine('cmn_AssistHosei')
                        damage1(600)
                        if conditionalunk2499(32, 2, 318):
                            if conditionalunk2500(13, 32, 2, 18, 0, 40000):
                                Unknown41(32)
                                Unknown98(40000)
                                Unknown40()
                        if Unknown2033(32, 'CmnActBDownBound'):
                            if conditionalunk2500(13, 32, 2, 18, 0, 40000):
                                Unknown41(32)
                                Unknown98(40000)
                                Unknown40()
                    Unknown2217(0)
                    Unknown23(89)
                    Unknown23(2)

                    def upon_12():
                        Unknown2036(32, 115)
                    Unknown14('hit')
            else:
                Unknown2208(23)

        def upon_45():
            Unknown448('bun_404_End', 0)
            Unknown19(23)
            Unknown615('ARC_BTL_BUN_Fat_End')

        def upon_2():
            Unknown448('bun_404_End', 0)
            Unknown19(23)
            Unknown615('ARC_BTL_BUN_Fat_End')
    sprite('fatshot', 2147483647)
    makeActive()
    Unknown99(-20000)
    Unknown113(36000)
    Unknown127(3000)
    Unknown52('030000000200000068000000000000001e0000000200000007000000')
    if (SLOT_7 <= 1000):
        physicsImpulseX(1000)
    if (SLOT_7 >= 65000):
        physicsImpulseX(65000)
    if (SLOT_115 >= 2):
        physicsImpulseX(55000)
        physicsImpulseY(17000)
        Unknown127(2000)
    label('hit')
    sprite('fatshot', 75)
    Unknown615('ARC_BTL_BUN_Fat_Wrap')
    Unknown23(45)
    Unknown23(6)
    Unknown458(32)
    Unknown176(1)
    if (SLOT_115 >= 2):
        Unknown41(32)
        Unknown2189(0, 5)
        Unknown40()
    else:
        Unknown41(32)
        Unknown2189(0, 5)
        Unknown135()
        Unknown40()

    def upon_1():
        Unknown448('bun_404_bind_End', 100)
        Unknown615('ARC_BTL_BUN_Fat_End')
    sprite('fatshot', 1)
    makeActive()
    callSubroutine('cmnAtkLevel_0_AtkInit')
    damage1(0)
    grHitPushbackX(100)
    Unknown1117(0)
    Unknown1095(500)
    Unknown1142(1)
    Unknown1157(1)
    Unknown1111(1)
    hitstun_Override(1)
    untech_Override(1)
    Unknown717('ShakeYoko', 100, 1, 10, 1)
    or_standhit(8)
    or_launchhit(1)

@State
def kiraida_explosion():

    def upon_IMMEDIATE():
        Unknown245()
        callSubroutine('cmnAtkLevel_4_AtkInit')
        callSubroutine('cmnUltimateShot_AtkInit')
        damage1(140)
        Unknown1086(30)
        or_standhit(1)
        or_launchhit(1)
        airHitPushbackX(5000)
        airHitPushbackY(3000)
        untech_Override(40)
        mod_hitstop(1)
        grHitPushbackX(50)
        Unknown1087('kiraida_explosion')
        Unknown1085('kiraida_explosion')
        Unknown18()
        Unknown1051(2)
        Unknown1079(1)
        Unknown1045('010000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1044(1)
        Unknown1050(1)
        Unknown1198(1, 0)
        Unknown1018(1)
        Unknown1954(1)
        Unknown289(300)
        Unknown457(3)
        Unknown2519(1)
        Unknown1118('dammy')
        Unknown1193('110000004152435f42544c5f434d4e5f4772645f4265616d4c6f6f705f4c50000000000000000000')

        def upon_3():
            if (not 
            Unknown53(23, 2, 0, 22, 2, 36)):
                Unknown633(17, 20)
            if (not 
            Unknown2033(3, 'Kiraida')):
                Unknown633(17, 20)

        def upon_90():
            callSubroutine('cmnUltimate_CameraCombo')
    sprite('kiraida_explosion', 2)
    makeActive()
    Unknown1027(1000000, -1000000, 1000000, 0)
    Unknown612('ARC_BTL_CMN_Expl_BB')
    sprite('kiraida_explosion', 2)
    makeActive()
    Unknown1027(1100000, -1100000, 1100000, 0)
    sprite('kiraida_explosion', 2)
    makeActive()
    Unknown1027(1200000, -1200000, 1200000, 0)
    sprite('kiraida_explosion', 2)
    makeActive()
    Unknown1027(1300000, -1300000, 1300000, 0)
    sprite('kiraida_explosion', 2)
    makeActive()
    Unknown1027(1400000, -1400000, 1400000, 0)
    sprite('kiraida_explosion', 2)
    makeActive()
    Unknown1027(5000000, -5000000, 1500000, 0)
    sprite('kiraida_explosion', 2)
    makeActive()
    Unknown1027(0, 0, 0, 0)
    label('loop')
    sprite('kiraida_explosion', 2)
    makeActive()
    Unknown3()
    Unknown54('00000000020000002d0000000000000001000000')
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000b000000020000002d000000000000000a000000')
    sprite('kiraida_explosion', 1)
    makeActive()
    airHitPushbackX(40000)
    airHitPushbackY(70000)
    untech_Override(40)
    mod_hitstop(3)
    mod_opphitstop(0, 5, 5)
    or_standhit(12)
    or_launchhit(12)
    Unknown477('00000000000000000000000080f0fa02')
    sprite('kiraida_explosion', 1)
    makeActive()
    Unknown670('0100000050c300000000000000000000')
    sprite('kiraida_explosion', 1)
    makeActive()
    sprite('kiraida_explosion', 1)
    makeActive()
    sprite('kiraida_explosion', 1)
    makeActive()
    sprite('kiraida_explosion', 1)
    makeActive()
    sprite('kiraida_explosion', 1)
    makeActive()
    sprite('kiraida_explosion', 1)
    makeActive()
    sprite('kiraida_explosion', 1)
    makeActive()
    sprite('kiraida_explosion', 1)
    makeActive()
    sprite('null', 20)
    beginRecovery()

@State
def Kiraida_ChargeAura():

    def upon_IMMEDIATE():
        Unknown454(3)
        Unknown457(3)
        Unknown294(1)
        Unknown2519(1)
    sprite('null', 100)
    Unknown450('bun_430_charge')

@State
def Kiraida_ChargeAura_b():

    def upon_IMMEDIATE():
        Unknown454(3)
        Unknown457(3)
        Unknown294(1)
        Unknown2519(1)
    sprite('null', 120)
    Unknown450('bun_430_charge2')

@State
def Kiraida_ChargeBlast():

    def upon_IMMEDIATE():
        Unknown454(3)
        Unknown457(3)
        Unknown294(1)
        Unknown2519(1)
    sprite('null', 100)
    Unknown450('bun_430_charge_blast')

@State
def Kiraida_ChargeDust():

    def upon_IMMEDIATE():
        Unknown454(3)
        Unknown457(3)
        Unknown294(1)
        Unknown2519(1)
    sprite('null', 100)
    Unknown471('62675f62756e3433305f6368617267655f647573740000000000000000000000')

@State
def Kiraida_ChargeDust2():

    def upon_IMMEDIATE():
        Unknown454(3)
        Unknown457(3)
        Unknown294(1)
        Unknown2519(1)
    sprite('null', 100)
    Unknown450('bun_430_charge_dust2')

@State
def Kiraida_Bomber():

    def upon_IMMEDIATE():
        Unknown454(3)
        Unknown457(3)
        Unknown294(1)
        Unknown2519(1)
    sprite('null', 60)
    Unknown450('bun_430_explosion')
    ActivateEffScript('bun_430_rock', 100)
    ActivateEffScript('bun_430cutin_Smoke', 100)
    ActivateEffScript('bun_430cutin_Smoke2', 100)
    ActivateEffScript('bun_430cutin_Smoke3', 100)
    ActivateEffScript('bun_430cutin_Smoke4', 100)
    ActivateEffScript('bun_430cutin_Smoke5', 100)

@State
def Kiraida_Bomber_End():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown2519(1)
    sprite('null', 10)
    Unknown448('bun_430_explosion_end', 100)
    sprite('null', 1)
    ActivateEffScript('bun_430cutin_Smoke', 100)
    ActivateEffScript('bun_430cutin_Smoke2', 100)

@State
def bun_430_rock():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown454(2)
        Unknown457(2)
    sprite('null', 60)
    Unknown471('62675f62756e3433305f726f636b000000000000000000000000000000000000')

@State
def bun_430cutin_Smoke():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown454(2)
        Unknown457(2)
        Unknown94(300000)
    label('loop')
    sprite('null', 10)
    Unknown2273(0, 2000)
    Unknown2283(0, 180000)
    Unknown449('bg_undersmoke00', 100)
    labelEnd('loop')

@State
def bun_430cutin_Smoke2():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown454(2)
        Unknown457(2)
        Unknown94(-300000)
    label('loop')
    sprite('null', 10)
    Unknown2273(0, 2000)
    Unknown449('bg_undersmoke00', 100)
    labelEnd('loop')

@State
def bun_430cutin_Smoke3():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown454(2)
        Unknown457(2)
        Unknown94(50000)
        Unknown2519(1)
    label('loop')
    sprite('null', 10)
    Unknown2273(0, 1000)
    Unknown2283(0, -135000)
    Unknown449('bg_undersmoke00', 100)
    labelEnd('loop')

@State
def bun_430cutin_Smoke4():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown454(2)
        Unknown457(2)
        Unknown94(-50000)
        Unknown2519(1)
    label('loop')
    sprite('null', 10)
    Unknown2273(0, 1000)
    Unknown2283(0, -45000)
    Unknown449('bg_undersmoke00', 100)
    labelEnd('loop')

@State
def bun_430cutin_Smoke5():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown454(2)
        Unknown457(2)
        Unknown94(0)
        Unknown2519(1)
    label('loop')
    sprite('null', 10)
    Unknown2273(0, 1000)
    Unknown2283(0, -90000)
    Unknown449('bg_undersmoke00', 100)
    labelEnd('loop')

@State
def okashi_beam():

    def upon_IMMEDIATE():
        Unknown245()
        callSubroutine('cmnAtkLevel_4_AtkInit')
        callSubroutine('cmnUltimateShot_AtkInit')
        damage1(2000)
        Unknown1086(75)
        mod_hitstop(5)
        or_standhit(8)
        or_launchhit(8)
        Unknown1051(0)
        Unknown1059(1)
        Unknown736(1)
        Unknown1179(0)
        Unknown1954(1)
        Unknown454(3)
        Unknown458(3)
        Unknown450('bun_431_beam_top')
        Unknown94(-100000)
        Unknown289(1000)
        Unknown2211(1)
        Unknown2217(1)
        Unknown2221(1)
        Unknown2213(1)
        Unknown35('2d000000656e640000000000000000000000000000000000000000000000000000000000')
        Unknown1118('dammyName')
        Unknown1119('ARC_BTL_CMN_Guard_Kidan')

        def upon_47():
            Unknown23(47)
            storeValue(2, 46, 0, 1)

        def upon_90():
            callSubroutine('cmnUltimate_CameraCombo')
            damage1(0)
            Unknown1095(0)
            if SLOT_16:
                if SLOT_263:
                    if (not SLOT_46):
                        if Unknown2033(3, 'Okashi'):
                            Unknown23(90)
                            Unknown1064('4f6b617368690000000000000000000000000000000000000000000000000000')
                            Unknown2040(3, 'Okashi_Hit', 0)
                            Unknown14('hit')

        def upon_93():
            damage1(200)
            Unknown96()
            Unknown14('sousai')
            Unknown54('00000000020000002d0000000000000001000000')
            if (SLOT_45 >= 16):
                Unknown2208(23)
                if (not SLOT_46):
                    if Unknown2033(3, 'Okashi'):
                        Unknown1798(3, 24)
            elif (not SLOT_46):
                if Unknown2033(3, 'Okashi'):
                    Unknown53(3, 2, 45, 23, 0, 0)
                    Unknown1798(3, 25)

        def upon_3():
            if conditionalunk2498(3, 2, 32):
                if conditionalunk2498(32, 2, 32):
                    Unknown1079(1)
                else:
                    Unknown1079(0)
            if conditionalunk2499(3, 2, 32):
                if conditionalunk2499(32, 2, 32):
                    Unknown1079(1)
                else:
                    Unknown1079(0)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('okasishot', 2)
    makeActive()
    physicsImpulseX(100000)
    label('loop')
    sprite('okasishot', 2)
    ActivateEffScript('bun_431_thunder', 100)
    physicsImpulseX(100000)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d000000000000002c010000')
    labelEnd('end')
    label('sousai')
    sprite('okasishot', 4)
    makeActive()
    damage1(200)
    physicsImpulseX(20000)
    Unknown94(-100000)
    Unknown3()
    Unknown97()
    labelEnd('loop')
    label('hit')
    sprite('null', 100)
    Unknown176(1)
    Unknown450('bun_431_beam_end')
    label('end')
    sprite('null', 40)
    Unknown23(45)
    Unknown23(23)
    Unknown450('bun_431_beam_end')
    Unknown1803('bun_431_thunder', 23)
    Unknown1803('bun_431_beam_head', 23)
    if Unknown2033(3, 'Okashi'):
        Unknown1798(3, 24)
    Unknown176(1)
    Unknown294(1)

@State
def bun_431_thunder():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown454(3)
        Unknown457(2)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 300)
    Unknown450('bun_431_thunder')
    label('end')
    sprite('null', 10)
    Unknown23(23)
    Unknown159(-100)

@State
def bun_431_beam_head():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown454(2)
        Unknown457(2)
        Unknown457(3)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
        Unknown94(0)
    sprite('null', 300)
    Unknown450('bun_431_beam_head')
    label('end')
    sprite('null', 5)
    Unknown23(23)
    sprite('null', 30)
    Unknown450('bun_431_beam_end')

@State
def bun_431_beam_hit():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown457(3)
        Unknown295(1)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 300)
    Unknown450('bun_431_beam_hit')
    ActivateEffScript('bun_431_beam_hit_b', 100)
    label('end')
    sprite('null', 5)
    Unknown23(23)
    sprite('null', 30)
    Unknown450('bun_431_beam_end')

@State
def bun_431_beam_hit_b():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown289(300)
        Unknown295(1)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown450('bun_431_beam_hit_b')
    label('end')

@State
def bun431_Eff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown294(1)
    sprite('null', 31)
    sprite('null', 30)
    ActivateEffScript('bun431cs_smoke', 100)
    sprite('null', 34)
    Unknown450('bun_431cs_anim')
    sprite('null', 32)
    Unknown32('bun431cs_smoke')
    Unknown450('bun_431cs_anim2')
    sprite('null', 4)
    Unknown450('')
    sprite('null', 16)
    Unknown450('bun_431cs_anim3')
    Unknown3()

@State
def bun431cs_smoke():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown294(1)
    sprite('null', 600)
    Unknown450('bun_431cs_smoke')
    Unknown3()

@State
def FinishCamera_NmlAtk2C():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 60)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2076('33d1fdffd8720300cb960000030f0000271c00000000000048000000000000005a0000001e00000001000000')
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def FinishCamera_NmlAtk2D():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 60)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    Unknown2079('0d0000001baefbffe5eb0700e5a80000e9080000651900000000000036000000000000006400000014000000000000000200000002000000')
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def FinishCamera_OkashiExe():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 2)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    sprite('null', 58)
    Unknown2079('0d00000006460000db1c0500e6c40200d4f9ffffc2fcffff0000000036000000140000005000000014000000000000000200000002000000')
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def DUMMYDUMMY():
    sprite('null', 1)