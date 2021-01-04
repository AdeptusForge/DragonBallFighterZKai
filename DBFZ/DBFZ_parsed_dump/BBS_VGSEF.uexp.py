@State
def dmy():
    sprite('null', 1)

@State
def okasi():

    def upon_IMMEDIATE():
        callSubroutine('cmn_okasi')
    sprite('null', 2147483647)
    Unknown450('vgs_okasi')

@State
def kidan_5D():

    def upon_IMMEDIATE():
        Unknown243()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        callSubroutine('cmn5DKidan_AtkInit')
        callSubroutine('cmnKidan_Init')
        damage1(250)
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
        Unknown2229(102)
        Unknown450('cmn_kidan')

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
                airHitPushbackY(20000)
    sprite('kidan', 1)
    makeActive()
    Unknown338(0)
    Unknown3()
    sprite('kidan', 2147483647)
    Unknown338(255)
    physicsImpulseX(70000)
    Unknown58(1)
    label('Koware')
    sprite('null', 10)
    Unknown176(1)
    Unknown450('')

@State
def kidan_smoke():

    def upon_IMMEDIATE():
        Unknown94(-260000)
        Unknown98(0)
    sprite('null', 1)
    Unknown448('bg_undersmoke00', 100)

@State
def kidan_start():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(2)
        ActivateEffScript('kidan_start_aura', 100)
    sprite('kidan', 3)
    Unknown1731(40000)
    sprite('keep', 1)
    Unknown1731(-60000)
    Unknown94(-10000)
    Unknown99(-10000)
    sprite('keep', 2)
    Unknown612('ARC_BTL_CMN_kidan_Chrg')
    sprite('keep', 3)
    Unknown1731(-120000)
    Unknown94(-60000)
    Unknown99(30000)
    sprite('keep', 3)
    Unknown1731(-100000)
    Unknown94(50000)
    Unknown99(-10000)
    Unknown3()

@State
def kidan_start_aura():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(2)
        Unknown450('cmn_kidan_throw')
    sprite('null', 9)
    Unknown188(150)
    Unknown191(50)
    sprite('null', 2147483647)
    Unknown188(600)
    Unknown191(0)

@State
def kidan_start2():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(2)
        Unknown94(40000)
        ActivateEffScript('kidan_start2_aura', 100)
    sprite('null', 3)
    Unknown1731(30000)
    sprite('null', 3)
    Unknown1731(40000)
    Unknown94(10000)
    Unknown99(10000)
    Unknown3()

@State
def kidan_start2_aura():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(2)
        Unknown450('cmn_kidan_throw')
    sprite('null', 3)
    Unknown188(300)
    Unknown191(66)
    sprite('null', 2147483647)
    Unknown188(500)
    Unknown191(0)

@State
def kidan_start3():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(2)
        Unknown94(40000)
        ActivateEffScript('kidan_start3_aura', 100)
    sprite('kidan', 3)
    Unknown1731(-90000)
    sprite('keep', 3)
    Unknown1731(-100000)
    Unknown94(40000)
    Unknown99(-10000)
    Unknown3()

@State
def kidan_start3_aura():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(2)
        Unknown450('cmn_kidan_throw')
    sprite('null', 3)
    Unknown188(300)
    Unknown191(66)
    sprite('null', 2147483647)
    Unknown188(500)
    Unknown191(0)

@State
def Multikidan():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        callSubroutine('cmnSpecialShot_AtkInit')
        Unknown1028(1)
        damage1(100)
        Unknown1117(200)
        untech_Override(30)
        mod_hitstop(5)
        mod_opphitstop(-1, 0, 0)
        or_launchhit(10)
        airHitPushbackX(12500)
        airHitPushbackY(0)
        Unknown778(4000)
        Unknown941(10)
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
        Unknown1183(0)
        Unknown717('ShakeYoko', 600, 1, 15, 0)
        Unknown2229(102)
        Unknown1914(0)
        Unknown1954(1)
        Unknown58(1)
        Unknown458(0)
        Unknown289(300)
        Unknown2210()
        Unknown2211(1)
        Unknown2221(1)
        Unknown2212(1)
        Unknown2213(1)
        Unknown2214(1)
        Unknown2215(1)

        def upon_45():
            Unknown19(23)

        def upon_2():
            Unknown448('bg_groundsmokeS', 123)
            Unknown670('00000000e80300000000000000000000')
            Unknown19(23)

        def upon_8():
            ActivateEffScript('cmn_kidan_end', 100)
            Unknown19(23)

        def upon_87():
            Unknown23(87)
            ActivateEffScript('cmn_reversalkidan', 100)
            Unknown19(23)
            Unknown450('')
        physicsImpulseX(90000)
        Unknown99(40000)

        def upon_23():
            Unknown99(-60000)
            airHitPushbackY(24000)
            Unknown941(0)
            or_launchhit(8)
            Unknown779()

        def upon_24():
            Unknown99(10000)
            untech_Override(26)
            airHitPushbackY(24000)
            or_standhit(8)
            or_launchhit(8)
            Unknown779()
        Unknown1118('ARC_BTL_CMN_Hit_Kidan')
        Unknown1119('ARC_BTL_CMN_Guard_Kidan')

        def upon_3():
            pass
        Unknown450('cmn_kidan')
    sprite('kidan', 2147483647)
    makeActive()

@State
def vgs_Multikidan_Mazzle():
    sprite('null', 1)
    Unknown448('vgs_Multikidan_Mazzle', 100)

@State
def Multikidan_start():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(2)
        ActivateEffScript('Multikidan_start_aura', 100)
    sprite('null', 3)
    Unknown1731(40000)
    sprite('null', 3)
    Unknown1731(-60000)
    Unknown94(-10000)
    Unknown99(-10000)
    sprite('null', 2)
    Unknown1731(-120000)
    Unknown94(-60000)
    Unknown99(30000)
    sprite('null', 2)
    Unknown1731(-100000)
    Unknown94(50000)
    Unknown99(-10000)
    Unknown3()

@State
def Multikidan_start_aura():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(2)
        Unknown450('cmn_kidan_throw')
    sprite('null', 24)
    Unknown188(150)
    Unknown191(18)
    sprite('null', 2147483647)
    Unknown188(600)
    Unknown191(0)

@State
def Multikidan_start2():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(2)
        Unknown94(40000)
        ActivateEffScript('Multikidan_start2_aura', 100)
    sprite('kidan', 1)
    Unknown1731(30000)
    sprite('keep', 1)
    Unknown1731(40000)
    Unknown94(10000)
    Unknown99(10000)
    Unknown3()

@State
def Multikidan_start2_aura():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(2)
        Unknown450('cmn_kidan_throw')
    sprite('null', 2)
    Unknown188(300)
    Unknown191(100)
    sprite('null', 2147483647)
    Unknown188(500)
    Unknown191(0)

@State
def Multikidan_start3():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(2)
        Unknown94(40000)
        ActivateEffScript('Multikidan_start3_aura', 100)
    sprite('null', 1)
    Unknown1731(-90000)
    sprite('null', 1)
    Unknown1731(-100000)
    Unknown94(40000)
    Unknown99(-10000)
    Unknown3()

@State
def Multikidan_start3_aura():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(2)
        Unknown450('cmn_kidan_throw')
    sprite('null', 2)
    Unknown188(300)
    Unknown191(100)
    sprite('null', 2147483647)
    Unknown188(500)
    Unknown191(0)

@State
def kidan_Air():

    def upon_IMMEDIATE():
        Unknown243()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        callSubroutine('cmnAir5DKidan_AtkInit')
        callSubroutine('cmnKidan_Init')
        damage1(250)
        airHitPushbackX(5000)
        airHitPushbackY(5000)
        Unknown2229(102)
        Unknown2230(102)
        Unknown1914(0)
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')

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
                airHitPushbackX(20000)
                airHitPushbackY(20000)

        def upon_23():
            physicsImpulseY(-27000)

        def upon_24():
            physicsImpulseY(-30000)
        Unknown450('cmn_kidan')
    sprite('kidan_nanamesita0', 1)
    makeActive()
    Unknown2055(0)
    sprite('kidan_nanamesita', 100)
    Unknown2055(1)
    Unknown164(-30000)
    physicsImpulseX(60000)
    label('Koware')
    sprite('null', 10)
    Unknown176(1)
    Unknown450('')

@State
def jumpkidan_start():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(3)
        ActivateEffScript('jumpkidan_start_aura', 100)
    sprite('null', 2)
    Unknown1731(-80000)
    sprite('null', 2)
    Unknown1731(-110000)
    Unknown94(-50000)
    Unknown99(50000)
    sprite('null', 2)
    Unknown612('ARC_BTL_CMN_kidan_Chrg')
    sprite('null', 2)
    Unknown1731(-110000)
    Unknown94(10000)
    Unknown99(50000)
    sprite('null', 3)
    Unknown1731(80000)
    Unknown94(130000)
    Unknown99(-180000)
    Unknown3()

@State
def jumpkidan_start_aura():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(2)
        Unknown450('cmn_kidan_throw')
    sprite('null', 8)
    Unknown188(350)
    Unknown191(50)
    sprite('null', 2147483647)
    Unknown188(750)
    Unknown191(0)

@State
def jumpkidan2_start():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(3)
        ActivateEffScript('jumpkidan2_start_aura', 100)
    sprite('null', 2)
    Unknown1731(80000)
    sprite('null', 2)
    Unknown1731(110000)
    Unknown94(60000)
    Unknown99(-10000)
    sprite('null', 2)
    Unknown1731(60000)
    Unknown94(140000)
    Unknown99(-120000)

@State
def jumpkidan2_start_aura():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(2)
        Unknown450('cmn_kidan_throw')
    sprite('null', 4)
    Unknown188(400)
    Unknown191(87)
    sprite('null', 2147483647)
    Unknown188(750)
    Unknown191(0)

@State
def jumpkidan3_start():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(3)
        ActivateEffScript('jumpkidan3_start_aura', 100)
    sprite('null', 2)
    Unknown1731(-160000)
    sprite('null', 2)
    Unknown1731(-90000)
    Unknown94(50000)
    Unknown99(-110000)
    sprite('null', 2)
    Unknown1731(90000)
    Unknown94(70000)
    Unknown99(-70000)

@State
def jumpkidan3_start_aura():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(2)
        Unknown450('cmn_kidan_throw')
    sprite('null', 4)
    Unknown188(300)
    Unknown191(112)
    sprite('null', 2147483647)
    Unknown188(750)
    Unknown191(0)

@State
def Multikidan_Air():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        callSubroutine('cmnSpecialShot_AtkInit')
        Unknown1028(1)
        damage1(100)
        Unknown1117(200)
        callSubroutine('cmn_AssistShotHosei')
        mod_hitstop(7)
        mod_opphitstop(-3, 0, 0)
        or_standhit(8)
        or_launchhit(8)
        airHitPushbackX(15000)
        airHitPushbackY(20000)
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
        Unknown1183(0)
        Unknown717('ShakeYoko', 600, 1, 15, 0)
        if Unknown2033(3, 'AssistAttack'):
            damage1(130)
            Unknown1095(1000)
        Unknown2229(102)
        Unknown2230(102)
        Unknown1914(0)
        Unknown1954(1)
        Unknown58(1)
        Unknown458(0)
        Unknown289(300)
        Unknown2210()
        Unknown2211(1)
        Unknown2221(1)
        Unknown2212(1)
        Unknown2213(1)
        Unknown2214(1)
        Unknown2215(1)

        def upon_45():
            Unknown19(23)

        def upon_2():
            Unknown23(2)
            Unknown448('bg_groundsmokeS', 123)
            Unknown670('00000000e80300000000000000000000')
            Unknown14('Koware')

        def upon_8():
            ActivateEffScript('cmn_kidan_end', 100)
            Unknown19(23)

        def upon_87():
            Unknown23(87)
            ActivateEffScript('cmn_reversalkidan', 100)
            Unknown19(23)
            Unknown450('')

        def upon_23():
            physicsImpulseY(-45000)

        def upon_24():
            physicsImpulseY(-50000)
        Unknown1118('ARC_BTL_CMN_Hit_Kidan')
        Unknown1119('ARC_BTL_CMN_Guard_Kidan')

        def upon_3():
            pass
        Unknown450('cmn_kidan')
    sprite('multi_kidan_nanamesita0', 1)
    makeActive()
    Unknown2055(0)
    sprite('multi_kidan_nanamesita', 100)
    Unknown2055(1)
    Unknown164(-30000)
    physicsImpulseX(80000)
    label('Koware')
    sprite('null', 5)
    Unknown450('')
    Unknown176(1)

@State
def vgs_AirMultikidan_Mazzle():

    def upon_IMMEDIATE():
        Unknown454(0)
        Unknown164(-30000)
    sprite('null', 100)
    Unknown450('vgs_Multikidan_Mazzle')

@State
def AssistMultikidan_start():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(3)
        ActivateEffScript('jumpkidan_start_aura', 100)
    sprite('null', 3)
    Unknown1731(-80000)
    sprite('null', 3)
    Unknown1731(-110000)
    Unknown94(-50000)
    Unknown99(50000)
    sprite('null', 3)
    sprite('null', 3)
    Unknown1731(-110000)
    Unknown94(10000)
    Unknown99(50000)
    sprite('null', 3)
    Unknown1731(80000)
    Unknown94(130000)
    Unknown99(-180000)
    Unknown3()

@State
def AirMultikidan_start():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(3)
        ActivateEffScript('jumpkidan_start_aura', 100)
    sprite('null', 2)
    Unknown1731(-80000)
    sprite('null', 2)
    Unknown1731(-110000)
    Unknown94(-50000)
    Unknown99(50000)
    sprite('null', 2)
    sprite('null', 2)
    Unknown1731(-110000)
    Unknown94(10000)
    Unknown99(50000)
    sprite('null', 2)
    Unknown1731(80000)
    Unknown94(130000)
    Unknown99(-180000)
    Unknown3()

@State
def AirMultikidan_start_aura():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(2)
        Unknown450('cmn_kidan_throw')
    sprite('null', 12)
    Unknown188(350)
    Unknown191(33)
    sprite('null', 2147483647)
    Unknown188(750)
    Unknown191(0)

@State
def AirMultikidan2_start():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(3)
        ActivateEffScript('AirMultikidan2_start_aura', 100)
    sprite('null', 1)
    Unknown1731(80000)
    sprite('null', 1)
    Unknown1731(110000)
    Unknown94(60000)
    Unknown99(-10000)
    sprite('null', 1)
    Unknown1731(60000)
    Unknown94(140000)
    Unknown99(-120000)

@State
def AirMultikidan2_start_aura():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(2)
        Unknown450('cmn_kidan_throw')
    sprite('null', 2)
    Unknown188(400)
    Unknown191(175)
    sprite('null', 2147483647)
    Unknown188(750)
    Unknown191(0)

@State
def AirMultikidan3_start():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(3)
        ActivateEffScript('AirMultikidan3_start_aura', 100)
    sprite('null', 1)
    Unknown1731(-160000)
    sprite('null', 1)
    Unknown1731(-90000)
    Unknown94(50000)
    Unknown99(-110000)
    sprite('null', 2)
    Unknown1731(90000)
    Unknown94(70000)
    Unknown99(-70000)

@State
def AirMultikidan3_start_aura():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(2)
        Unknown450('cmn_kidan_throw')
    sprite('null', 2)
    Unknown188(300)
    Unknown191(225)
    sprite('null', 2147483647)
    Unknown188(750)
    Unknown191(0)

@State
def vgs_hajiki():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 30)
    Unknown450('vgs_hajiki')

@State
def VGS_202Eff():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown99(62000)
        Unknown94(62000)
        Unknown164(45000)
        Unknown188(750)
    sprite('null', 60)
    Unknown2275(0, 45000)
    Unknown449('vgs_202Eff00', 100)
    ActivateEffScript('VGS_202Eff_smoke', 100)
    ActivateEffScript('VGS_202Eff_smoke2', 100)
    ActivateEffScript('VGS_202Eff_smoke3', 100)
    ActivateEffScript('VGS_202Eff_smoke4', 100)

@State
def VGS_202Eff_smoke():

    def upon_IMMEDIATE():
        Unknown94(-200000)
        Unknown98(0)
    sprite('null', 1)
    Unknown2273(0, 750)
    Unknown449('bg_undersmoke00', 100)

@State
def VGS_202Eff_smoke2():

    def upon_IMMEDIATE():
        Unknown94(-200000)
        Unknown98(0)
    sprite('null', 1)
    Unknown2273(0, 1250)
    Unknown449('bg_undersmoke00', 100)

@State
def VGS_202Eff_smoke3():

    def upon_IMMEDIATE():
        Unknown239()
        Unknown94(50000)
        Unknown98(0)
    sprite('null', 1)
    Unknown2273(0, 400)
    Unknown449('bg_undersmoke00', 100)

@State
def VGS_202Eff_smoke4():

    def upon_IMMEDIATE():
        Unknown239()
        Unknown94(150000)
        Unknown98(0)
    sprite('null', 1)
    Unknown2273(0, 800)
    Unknown449('bg_undersmoke00', 100)

@State
def VGS_5CEff():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown164(80000)
        Unknown99(75000)
        Unknown94(200000)
    sprite('null', 60)
    Unknown450('cmn_strike00')

@State
def VGS_2CEff():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown99(250000)
        Unknown164(-8000)
    sprite('null', 60)
    Unknown450('cmn_strike00')

@State
def VGS_Air5CEff():

    def upon_IMMEDIATE():
        Unknown295(1)
    sprite('null', 60)
    Unknown450('cmn_strike00')

@State
def VGS_Air2CEff():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown99(250000)
        Unknown164(-10000)
    sprite('null', 60)
    Unknown450('cmn_strike00')

@State
def VGS_400Eff():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown456(2)
        Unknown99(220000)
        Unknown94(260000)
        Unknown35('17000000456e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown450('vgs_400Eff00')
    Unknown448('vgs_400Eff_nokosi', 100)
    ActivateEffScript('VGS_400_groundSmoke', 100)
    label('End')
    sprite('null', 15)
    Unknown450('vgs_400Eff01')
    Unknown32('VGS_400_groundSmoke')
    Unknown454(0)
    Unknown456(0)
    Unknown3()

@State
def VGS_400_Assist_Eff():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown456(2)
        Unknown99(220000)
        Unknown94(260000)
        Unknown35('17000000456e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown450('vgs_400Eff00_Assist')
    Unknown448('vgs_400Eff_nokosi_Assist', 100)
    label('End')
    sprite('null', 15)
    Unknown450('vgs_400Eff01_Assist')
    Unknown454(0)
    Unknown456(0)
    Unknown3()

@State
def VGS_400_groundSmoke():

    def upon_IMMEDIATE():
        Unknown98(0)
        Unknown456(2)
        Unknown454(2)
        Unknown457(2)
        Unknown94(-75000)
    label('loop')
    sprite('null', 3)
    Unknown449('bg_undersmoke00', 100)
    Unknown3()
    labelEnd('loop')

@State
def VGS_400EffAir():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown456(2)
        Unknown99(220000)
        Unknown94(260000)
        Unknown35('17000000456e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown450('vgs_400Eff00')
    Unknown448('vgs_400Eff_nokosi', 100)
    label('End')
    sprite('null', 15)
    Unknown450('vgs_400Eff01')
    Unknown454(0)
    Unknown456(0)
    Unknown3()

@State
def VGS_400B1Eff():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown456(2)
        Unknown35('17000000456e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown450('vgs_400Effb1_00')
    label('End')
    sprite('null', 15)
    Unknown450('vgs_400Effb1_01')
    Unknown454(0)
    Unknown456(0)
    Unknown3()

@State
def VGS_400B2Eff():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown456(2)
        Unknown35('17000000456e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown450('vgs_400Effb2_00')
    label('End')
    sprite('null', 15)
    Unknown450('vgs_400Effb2_01')
    Unknown456(0)
    Unknown3()

@State
def VGS_402Eff():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown94(62500)
        Unknown99(125000)
    sprite('null', 2147483647)
    Unknown450('vgs_402_speedEff')

@State
def BigbangLand():

    def upon_IMMEDIATE():
        Unknown245()
        callSubroutine('cmnAtkLevel_4_AtkInit')
        callSubroutine('cmnUltimateShot_AtkInit')
        damage1(2200)
        Unknown1086(37)
        mod_hitstop(15)
        or_standhit(12)
        or_launchhit(12)
        airHitPushbackX(48000)
        airHitPushbackY(40000)
        untech_Override(40)
        Unknown1051(0)
        Unknown1045('010000002000000000000000000000000000000000000000000000000000000000000000')
        Unknown717('ShakeTateYoko', 1000, 0, 45, 10)
        Unknown1112(0)
        Unknown1966(1)
        Unknown1954(1)
        physicsImpulseX(100000)
        Unknown58(1)
        Unknown458(0)
        Unknown289(120)

        def upon_47():
            Unknown23(47)
            storeValue(2, 46, 0, 1)

        def upon_45():
            Unknown19(23)
            if (SLOT_18 <= 500000):
                Unknown670('01000000e80300000000000000000000')
            ActivateEffScript('Bigbang_end', 100)
            if (not SLOT_46):
                if Unknown2033(3, 'BigBangAttack'):
                    Unknown1798(3, 23)
                if Unknown2033(3, 'BigBangAttack_Air_Yoko'):
                    Unknown1798(3, 23)

        def upon_92():
            Unknown23(92)
            Unknown2208(23)

        def upon_90():
            Unknown23(90)
            callSubroutine('cmnUltimate_CameraCombo')
            damage1(2200)

        def upon_93():
            if (not SLOT_45):
                Unknown109()
                Unknown114()
            storeValue(2, 47, 0, 0)

            def upon_77():
                if (not SLOT_81):
                    Unknown54('00000000020000002f0000000000000001000000')
                    if (SLOT_47 >= 5):
                        Unknown23(77)
                        Unknown176(1)
                        Unknown110()
                        Unknown115()
            damage1(200)
            physicsImpulseX(30000)
            Unknown94(-150000)
            Unknown2229(110)
            makeActive()
            Unknown54('00000000020000002d0000000000000001000000')
            if (SLOT_45 >= 8):
                Unknown2208(23)
                if (not SLOT_46):
                    if Unknown2033(3, 'BigBangAttack'):
                        Unknown1798(3, 23)
                    if Unknown2033(3, 'BigBangAttack_Air_Yoko'):
                        Unknown1798(3, 23)
            elif (not SLOT_46):
                if Unknown2033(3, 'BigBangAttack'):
                    Unknown1798(3, 25)
                if Unknown2033(3, 'BigBangAttack_Air_Yoko'):
                    Unknown1798(3, 25)

        def upon_3():
            if (SLOT_18 <= 0):
                Unknown448('bg_groundsmokeL', 100)
                Unknown670('00000000e80300000000000000000000')
                Unknown19(23)
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
    sprite('bigbangattack', 100)
    Unknown450('vgs_430Jizoku')
    ActivateEffScript('BigBangNokosiEff', 100)
    makeActive()
    if (SLOT_18 <= 400000):
        ActivateEffScript('groundSmoke', 100)

@State
def Bigbang_end():

    def upon_IMMEDIATE():
        Unknown450('cmn_bomb_sp')
        Unknown2077('ShakeTate', 1500, 5, 45, 20)
        Unknown1801(1)
    sprite('null', 10)
    Unknown612('ARC_BTL_CMN_Expl_BB')
    Unknown2136('000000000000000000000000e803000000000000640000001e000000')
    Unknown477('00000000000000000000000010270000')
    sprite('null', 120)
    Unknown1801(0)

@State
def BigBangNokosiEff():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
    label('loop')
    sprite('null', 4)
    ActivateEffScript('BigBangNokosi', 100)
    Unknown3()
    labelEnd('loop')

@State
def BigBangNokosi():

    def upon_IMMEDIATE():
        Unknown450('vgs_430nokosi')
    sprite('null', 30)
    Unknown3()

@State
def groundSmoke():

    def upon_IMMEDIATE():
        Unknown98(0)
        Unknown454(2)
        Unknown457(2)
        Unknown94(150000)
    label('loop')
    sprite('null', 3)
    Unknown2274(0, 1100)
    Unknown449('bg_undersmoke00', 100)
    Unknown3()
    labelEnd('loop')

@State
def BigbangTame():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown457(2)
        Unknown450('vgs_430Tame')
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown3()
    label('end')
    sprite('null', 15)
    Unknown188(600)
    Unknown94(-100000)
    Unknown450('vgs_430TameEnd')
    Unknown3()

@State
def Bigbang_shadow():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown295(1)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown450('cmn_shadowLine_loop')
    Unknown3()
    label('end')
    sprite('null', 1)
    Unknown3()

@State
def BigbangAir():

    def upon_IMMEDIATE():
        Unknown245()
        callSubroutine('cmnAtkLevel_4_AtkInit')
        callSubroutine('cmnUltimateShot_AtkInit')
        damage1(2200)
        Unknown1086(35)
        mod_hitstop(15)
        or_standhit(11)
        or_launchhit(11)
        airHitPushbackX(35000)
        airHitPushbackY(-40000)
        untech_Override(45)
        Unknown842(0)
        Unknown854(1)
        Unknown806(25000)
        Unknown808(20000)
        Unknown802(100)
        Unknown1051(0)
        Unknown1045('010000002000000000000000000000000000000000000000000000000000000000000000')
        Unknown717('ShakeTateYoko', 1000, 0, 45, 10)
        Unknown1112(0)
        Unknown1966(1)
        Unknown1954(1)
        Unknown164(-30000)
        Unknown202(100000, 0)
        Unknown58(1)
        Unknown458(0)
        Unknown289(120)

        def upon_47():
            Unknown23(47)
            storeValue(2, 46, 0, 1)

        def upon_45():
            Unknown19(23)
            if (SLOT_18 <= 500000):
                Unknown670('01000000e80300000000000000000000')
            ActivateEffScript('Bigbang_end', 100)
            if (not SLOT_46):
                if Unknown2033(3, 'BigBangAttack_Air_Shita'):
                    if (not SLOT_45):
                        Unknown1798(3, 23)

        def upon_92():
            Unknown23(92)
            Unknown2208(23)

        def upon_90():
            Unknown23(90)
            callSubroutine('cmnUltimate_CameraCombo')
            damage1(2200)

        def upon_93():
            if (not SLOT_45):
                Unknown109()
                Unknown114()
            storeValue(2, 47, 0, 0)

            def upon_77():
                if (not SLOT_81):
                    Unknown54('00000000020000002f0000000000000001000000')
                    if (SLOT_47 >= 5):
                        Unknown23(77)
                        Unknown176(1)
                        Unknown110()
                        Unknown115()
            damage1(200)
            Unknown94(-100000)
            Unknown99(50000)
            Unknown202(30000, 0)
            makeActive()
            Unknown54('00000000020000002d0000000000000001000000')
            if (SLOT_45 >= 8):
                Unknown2208(23)
                if (not SLOT_46):
                    if Unknown2033(3, 'BigBangAttack_Air_Shita'):
                        Unknown1798(3, 23)
            elif (not SLOT_46):
                if Unknown2033(3, 'BigBangAttack_Air_Shita'):
                    Unknown1798(3, 25)

        def upon_3():
            if (SLOT_18 <= 0):
                Unknown448('bg_groundsmokeL', 100)
                Unknown670('00000000e80300000000000000000000')
                Unknown19(23)
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
    sprite('bigbangattack', 100)
    Unknown450('vgs_430Jizoku')
    ActivateEffScript('BigBangNokosiEff2', 100)
    makeActive()

@State
def BigBangNokosiEff2():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
    label('loop')
    sprite('null', 4)
    ActivateEffScript('BigBangNokosi2', 100)
    Unknown3()
    labelEnd('loop')

@State
def BigBangNokosi2():

    def upon_IMMEDIATE():
        Unknown450('vgs_430nokosi')
        Unknown164(-30000)
        Unknown99(75000)
    sprite('null', 30)
    Unknown3()

@State
def AirBigbang_shadow():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown295(1)
        Unknown164(-30000)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown450('cmn_shadowLine_loop')
    Unknown3()
    label('end')
    sprite('null', 1)
    Unknown3()

@State
def FinalFlash_Core():

    def upon_IMMEDIATE():
        Unknown456(3)
        Unknown454(3)
        Unknown289(300)
        Unknown450('vgs_432_core00')
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
        Unknown35('2f000000656e640000000000000000000000000000000000000000000000000000000000')

        def upon_35():
            Unknown454(0)
            Unknown295(1)

        def upon_24():
            Unknown23(24)
            storeValue(2, 45, 0, 0)
            Unknown1803('FinalFlash_Atk', 29)
            if Unknown2033(3, 'FinalFlash'):
                Unknown53(3, 2, 45, 23, 0, 0)
                Unknown1798(3, 25)
            if Unknown2033(3, 'AirFinalFlash'):
                Unknown53(3, 2, 45, 23, 0, 0)
                Unknown1798(3, 25)
            storeValue(2, 47, 0, 1)
            storeValue(2, 51, 0, 1)

            def upon_24():
                Unknown54('00000000020000002f0000000000000001000000')
                if (SLOT_47 >= 16):
                    if Unknown2033(3, 'FinalFlash'):
                        Unknown1798(3, 24)
                    if Unknown2033(3, 'AirFinalFlash'):
                        Unknown1798(3, 24)
                else:
                    if Unknown2033(3, 'FinalFlash'):
                        Unknown1798(3, 25)
                    if Unknown2033(3, 'AirFinalFlash'):
                        Unknown1798(3, 25)
    label('loop')
    sprite('null', 2)
    Unknown54('0000000002000000300000000000000001000000')
    Unknown2279('02000000300000000200000033000000')
    Unknown445('46696e616c466c6173685f41746b00000000000000000000000000000000000064000000')
    if (SLOT_45 <= 9):
        Unknown41(1)
        Unknown1199(1, 0)
        Unknown1191(1)
        Unknown40()
    if (SLOT_45 >= 18):
        Unknown53(1, 2, 45, 23, 0, 1)
    sprite('null', 2)
    Unknown3()
    Unknown54('00000000020000002d0000000000000001000000')
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000002d0000000000000014000000')
    label('end')
    sprite('null', 1)
    Unknown23(23)
    Unknown23(24)
    Unknown23(47)
    Unknown23(3)
    storeValue(2, 49, 0, 1)
    ActivateEffScript('FinalFlash_Atk', 100)
    Unknown1803('FinalFlash_Atk', 30)
    if Unknown2033(3, 'FinalFlash'):
        Unknown1798(3, 24)
    if Unknown2033(3, 'AirFinalFlash'):
        Unknown1798(3, 24)
    Unknown454(0)
    Unknown456(0)
    Unknown294(1)
    sprite('null', 1)
    Unknown32('FinalFlash_Atk')
    sprite('null', 10)
    Unknown450('vgs_432_core01')
    sprite('null', 30)

@State
def FinalFlash_Atk():

    def upon_IMMEDIATE():
        Unknown245()
        callSubroutine('cmnAtkLevel_4_AtkInit')
        callSubroutine('cmnUltimateShot_AtkInit')
        damage1(220)
        Unknown1086(38)
        Unknown1095(500)
        mod_hitstop(1)
        or_standhit(11)
        or_launchhit(11)
        airHitPushbackX(80000)
        airHitPushbackY(10000)
        grHitPushbackX(10)
        Unknown1186('010000003075000090d003006400000000000000')
        Unknown842(0)
        untech_Override(150)
        Unknown1027(50000000, -320000, 0, 0)
        Unknown1187(0)
        Unknown736(1)
        Unknown716(1)
        Unknown733(1)
        Unknown734(1)
        Unknown1192('100000004152435f42544c5f434d4e5f4869745f4265616d4c6f6f705f4c50000000000000000000')
        Unknown1193('110000004152435f42544c5f434d4e5f4772645f4265616d4c6f6f705f4c50000000000000000000')

        def upon_30():
            or_standhit(12)
            or_launchhit(12)
            airHitPushbackX(20000)
            airHitPushbackY(48000)
            Unknown778(2500)
            Unknown1186('0000000000000000000000000000000000000000')
            Unknown1064('436d6e4e65757472616c00000000000000000000000000000000000000000000')
            if conditionalunk2499(3, 2, 24):
                makeActive()
            else:
                beginRecovery()
        Unknown456(2)
        Unknown454(2)
        Unknown457(2)
        Unknown289(60)
        Unknown1954(1)
        Unknown58(1)
        Unknown450('vgs_432_naka00')

        def upon_93():
            Unknown53(2, 2, 115, 23, 2, 115)
            Unknown19(23)
            Unknown1798(2, 24)

        def upon_29():
            storeValue(2, 45, 0, 0)

        def upon_90():
            callSubroutine('cmnUltimate_CameraCombo')
            if SLOT_116:
                if Unknown2033(3, 'FinalFlash'):
                    Unknown53(3, 2, 45, 23, 0, 0)
                if Unknown2033(3, 'AirFinalFlash'):
                    Unknown53(3, 2, 45, 23, 0, 0)

        def upon_8():
            if SLOT_45:
                Unknown1798(2, 23)

        def upon_3():
            if conditionalunk2498(2, 2, 47):
                if conditionalunk2499(2, 2, 49):
                    Unknown53(23, 2, 0, 2, 2, 115)
                    if (SLOT_115 <= SLOT_0):
                        if (not SLOT_47):
                            Unknown19(23)
            if (SLOT_18 <= 600000):
                Unknown670('03000000e80300000000000000000000')
            if (not 
            Unknown53(23, 2, 0, 22, 2, 36)):
                Unknown633(16, 20)
                Unknown633(17, 20)
            if (not 
            Unknown2033(3, 'FinalFlash')):
                if (not 
                Unknown2033(3, 'AirFinalFlash')):
                    Unknown633(16, 20)
                    Unknown633(17, 20)

        def upon_1():
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('vgs_432_naka01', 100)
    sprite('finalflash', 1)
    makeActive()
    Unknown94(-100000)
    Unknown202(100000, 0)
    sprite('finalflash', 1)
    Unknown734(0)
    label('loop')
    sprite('finalflash', 2)
    Unknown2301(1200)
    sprite('finalflash', 2)
    Unknown2301(1000)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def finalflash_shadow():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown450('cmn_shadowLine_loop')
    Unknown3()
    label('end')
    sprite('null', 1)
    Unknown3()

@State
def __404Eff():

    def upon_IMMEDIATE():
        Unknown450('vgs_401Eff00')
        Unknown454(2)
        Unknown456(2)
        Unknown457(2)
        Unknown35('17000000456e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown448('vgs_401EffNokosi', 100)
    Unknown3()
    label('End')
    sprite('null', 15)
    Unknown450('vgs_401Eff01')
    Unknown456(0)
    Unknown3()

@State
def __404Eff2():

    def upon_IMMEDIATE():
        Unknown450('vgs_401Eff02')
        Unknown454(2)
        Unknown456(2)
        Unknown457(2)
        Unknown35('17000000456e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown3()
    label('End')
    sprite('null', 15)
    Unknown450('vgs_401Eff03')
    Unknown456(0)
    Unknown3()

@State
def FinalFlash_aura00():

    def upon_IMMEDIATE():
        Unknown1801(1)
        Unknown295(1)
        Unknown454(2)
        Unknown457(2)
        Unknown450('vgs_432_bodyaura00')
        Unknown99(250000)
        Unknown188(1200)
        Unknown35('17000000456e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    label('End')
    sprite('null', 10)
    Unknown3()

@State
def FF_groundSmokeMatome():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown295(1)
    label('loop')
    sprite('null', 10)
    ActivateEffScript('FF_groundSmoke_R', 100)
    ActivateEffScript('FF_groundSmoke_L', 100)
    labelEnd('loop')

@State
def FF_groundSmoke_R():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown232(130000)
        Unknown188(3000)
        Unknown94(150000)
        Unknown99(-75000)
        Unknown1732(-300000)
        Unknown295(1)
    sprite('null', 40)
    Unknown1955('62675f756e646572736d6f6b6530300000000000000000000000000000000000')
    Unknown3()

@State
def FF_groundSmoke_L():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown232(-130000)
        Unknown188(3000)
        Unknown94(150000)
        Unknown99(-75000)
        Unknown1732(300000)
        Unknown295(1)
    sprite('null', 40)
    Unknown1955('62675f756e646572736d6f6b6530300000000000000000000000000000000000')
    Unknown3()

@State
def FF_SyutyuLine():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown295(1)
        Unknown450('cmn_syutyusen')
    sprite('null', 2147483647)

@State
def FF_tameShere():

    def upon_IMMEDIATE():
        Unknown1801(1)
        Unknown295(1)
        Unknown454(2)
        Unknown457(2)
        Unknown450('vgs_432_tamesphere')
        Unknown99(300000)
        Unknown94(250000)
        Unknown188(350)
    sprite('null', 2147483647)

@State
def FF_Flash():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown295(1)
        Unknown450('vgs_432_flash00')
    sprite('null', 2147483647)

@State
def FF_groundSmokeMatome2():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown295(1)
        Unknown98(0)
        Unknown94(300000)
    label('loop')
    sprite('null', 10)
    ActivateEffScript('FF_groundSmoke2', 100)
    labelEnd('loop')

@State
def FF_groundSmoke2():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown232(185000)
        Unknown188(1600)
        Unknown1732(350000)
        Unknown295(1)
        Unknown1801(1)
    sprite('null', 30)
    Unknown1955('62675f756e646572736d6f6b6530300000000000000000000000000000000000')
    Unknown3()

@State
def vgs600_scrFlash():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown454(2)
        Unknown457(2)
        Unknown450('vgs_600scranim01')
        Unknown239()
    sprite('null', 2147483647)

@State
def vgs600_scranim00():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown454(2)
        Unknown457(2)
        Unknown450('vgs_600scranim00')
        Unknown239()
    sprite('null', 79)

@State
def vgs600_BodyAura():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown457(2)
        Unknown454(2)
        Unknown232(-450000)
        Unknown1955('636d6e5f53617572615f6c6f6f70000000000000000000000000000000000000')
        Unknown35('17000000617572616d6f7665000000000000000000000000000000000000000000000000')
    sprite('null', 4)
    Unknown188(500)
    sprite('null', 4)
    Unknown188(600)
    sprite('null', 4)
    Unknown188(650)
    sprite('null', 4)
    Unknown188(700)
    sprite('null', 4)
    Unknown188(750)
    label('loop')
    sprite('null', 3)
    Unknown188(800)
    sprite('null', 3)
    Unknown188(850)
    labelEnd('loop')
    label('auramove')
    sprite('null', 2147483647)
    Unknown94(-100000)
    Unknown1732(-100000)
    Unknown157(200)

@State
def vgs600_AuraPlus():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown457(2)
        Unknown454(2)
        Unknown1955('7667735f36303061757261706c75730000000000000000000000000000000000')
    sprite('null', 2147483647)

@State
def vgs600_Speed():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown1955('7667735f36303073706565643030000000000000000000000000000000000000')
        Unknown232(-450000)
    sprite('null', 24)

@State
def vgs600_groundsmoke():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown454(2)
        Unknown457(2)
        Unknown94(150000)
        Unknown1732(-75000)
    label('loop')
    sprite('null', 10)
    Unknown2273(0, 1400)
    Unknown2283(0, 90000)
    Unknown449('bg_undersmoke00', 100)
    labelEnd('loop')

@State
def vgs600_groundsmoke2():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown454(2)
        Unknown457(2)
        Unknown94(150000)
        Unknown1732(75000)
    label('loop')
    sprite('null', 10)
    Unknown2273(0, 1400)
    Unknown2283(0, -90000)
    Unknown449('bg_undersmoke00', 100)
    labelEnd('loop')

@State
def FinishCamera_NmlAtk2C():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 60)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    Unknown2076('2751feff40dd01002ccbffffbb1b0000a32100000000000048000000000000005a0000001e00000001000000')
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def FinishCamera_NmlAtkAir2C():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 60)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    Unknown2076('852afffff84e020073c7ffff6e1d0000891400000000000048000000000000005a0000001e00000001000000')
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def DUMMYDUMMY():
    sprite('null', 1)