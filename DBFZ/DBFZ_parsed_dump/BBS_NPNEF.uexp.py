@State
def dmy():
    sprite('null', 1)

@State
def test():
    sprite('null', 60)
    Unknown2095(0, 5)

@State
def okasi():

    def upon_IMMEDIATE():
        callSubroutine('cmn_okasi')
    sprite('null', 2147483647)
    Unknown450('npn_okasi')

@State
def npn_2CEff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 30)
    Unknown450('npn_232_smash')
    Unknown612('ARC_BTL_CMN_Hit_Midle-A')

@State
def npn_263Eff1():

    def upon_IMMEDIATE():
        Unknown458(2)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 60)
    Unknown450('npn_263_wind')

@State
def npn_263Eff2():

    def upon_IMMEDIATE():
        Unknown458(2)
        Unknown456(2)
    sprite('null', 60)
    Unknown450('npn_263_wind2')

@State
def kidan_start_aura():

    def upon_IMMEDIATE():
        Unknown457(3)
        Unknown450('cmn_kidan_throw')
        Unknown289(600)

        def upon_12():
            Unknown2036(2, 0)

        def upon_23():
            Unknown23(23)
            Unknown1731(-150000)

        def upon_24():
            Unknown23(24)
            Unknown1731(-200000)

        def upon_25():
            Unknown23(25)
            Unknown1731(-100000)
        Unknown612('ARC_BTL_CMN_kidan_Chrg')
    sprite('null', 2)
    Unknown188(600)
    sprite('null', 4)
    Unknown188(690)
    sprite('null', 2147483647)
    Unknown188(800)

@State
def jumpkidan_start():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown457(2)
        ActivateEffScript('jumpkidan_start_aura', 100)

        def upon_12():
            Unknown2036(2, 0)

        def upon_23():
            Unknown23(23)
            Unknown94(-20000)
            Unknown99(60000)
            Unknown1731(-70000)

        def upon_24():
            Unknown23(24)
            Unknown94(150000)
            Unknown99(-80000)
            Unknown1731(100000)
    sprite('null', 30)
    Unknown612('ARC_BTL_CMN_kidan_Chrg')
    Unknown3()

@State
def jumpkidan_start_aura():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(2)
        Unknown450('cmn_kidan_throw')
        Unknown289(600)
    sprite('null', 10)
    Unknown188(100)
    Unknown191(65)
    sprite('null', 2147483647)
    Unknown188(750)
    Unknown191(0)

@State
def npn_hajiki():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 30)
    Unknown450('npn_hajiki')

@State
def npn_205Eff_Swing00():

    def upon_IMMEDIATE():
        Unknown458(3)
        Unknown457(3)
        Unknown454(3)
        Unknown456(3)
        Unknown239()
        Unknown450('npn_205_blow00')
    sprite('null', 60)

@State
def npn_205Eff_Swing01():

    def upon_IMMEDIATE():
        Unknown458(3)
        Unknown457(3)
        Unknown454(3)
        Unknown456(3)
        Unknown239()
        Unknown450('npn_205_blow01')
    sprite('null', 60)

@State
def kidan_5D():

    def upon_IMMEDIATE():
        Unknown243()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        callSubroutine('cmn5DKidan_AtkInit')
        callSubroutine('cmnKidan_Init')
        damage1(800)
        or_standhit(8)
        or_launchhit(8)
        airHitPushbackX(28000)
        airHitPushbackY(24100)
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
        untech_Override(26)
        grHitPushbackX(200)
        mod_hitstop(6)
        mod_opphitstop(0, 1, 1)
        Unknown1051(0)
        if Unknown2033(3, 'AssistAttack3'):
            damage1(400)
            Unknown1128(1)
            Unknown1143(0)
            callSubroutine('cmn_AssistHosei')

            def upon_90():
                Unknown23(90)
                if Unknown2033(3, 'AssistAttack3'):
                    Unknown53(3, 2, 51, 23, 0, 1)
        Unknown450('cmn_kidan')
        Unknown2299(1500)
        Unknown2229(102)
        Unknown2211(2)
        Unknown2221(2)
        Unknown2212(2)
        Unknown2213(2)
        Unknown2214(1)
        Unknown2215(1)

        def upon_93():
            makeActive()
    sprite('kidan1f', 1)
    makeActive()
    Unknown338(0)
    Unknown3()
    sprite('kidan', 100)
    Unknown338(255)
    Unknown58(1)
    Unknown202(70000, 0)
    label('Koware')
    sprite('null', 10)
    Unknown176(1)
    Unknown450('')

@State
def kidan_smoke():

    def upon_IMMEDIATE():
        Unknown94(-27000)
    sprite('null', 1)
    Unknown448('bg_undersmoke00', 100)

@State
def jumpkidan():

    def upon_IMMEDIATE():
        Unknown243()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        callSubroutine('cmnAir5DKidan_AtkInit')
        callSubroutine('cmnKidan_Init')
        damage1(800)
        or_standhit(8)
        or_launchhit(8)
        airHitPushbackX(21000)
        airHitPushbackY(25000)
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
        untech_Override(24)
        Unknown1095(1000)
        Unknown450('cmn_kidan_homing')
        Unknown2299(1500)
        Unknown1731(80000)
        Unknown2230(114)
        Unknown2211(2)
        Unknown2221(2)
        Unknown2212(2)
        Unknown2213(2)
        Unknown2214(1)
        Unknown2215(1)

        def upon_93():
            makeActive()

        def upon_2():
            Unknown448('bg_groundsmokeS', 123)
            Unknown670('01000000e80300000000000000000000')
            Unknown2208(23)

        def upon_12():
            Unknown200(0)
    sprite('kidan_nanamesita', 1)
    makeActive()
    Unknown338(0)
    sprite('kidan_nanamesita', 100)
    Unknown58(1)
    Unknown338(255)
    physicsImpulseX(60000)
    physicsImpulseY(-10000)
    Unknown3()
    label('Koware')
    sprite('null', 10)
    Unknown176(1)
    Unknown450('')

@State
def npn_400eff_Punch():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
        Unknown450('npn_400_punch')
    sprite('null', 1)
    sprite('null', 60)
    Unknown456(0)

@State
def npn_400eff_Punch_add():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
        Unknown450('npn_400_punch_add')
    sprite('null', 1)
    sprite('null', 60)
    Unknown456(0)

@State
def npn_400eff_Punch2nd():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
        Unknown450('npn_400_punch2nd')
    sprite('null', 1)
    sprite('null', 60)
    Unknown456(0)

@State
def npn_400eff_Punch2nd_add():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
        Unknown450('npn_400_punch2nd_add')
    sprite('null', 1)
    sprite('null', 60)
    Unknown456(0)

@State
def npn_404Eff():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown458(2)
        Unknown450('npn_404_atemi')
    sprite('null', 60)

@State
def npn_404Eff_atk():

    def upon_IMMEDIATE():
        Unknown458(2)
        Unknown454(2)
        Unknown456(2)
        Unknown450('npn_404_elbow')

        def upon_47():
            Unknown454(0)
    sprite('null', 60)
    Unknown188(700)
    Unknown94(60000)
    Unknown99(100000)

@State
def npn_404Eff_spark():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(2)
        Unknown454(2)
        Unknown456(2)
        Unknown450('npn_404_spark')
    sprite('null', 60)

@Subroutine
def sbn_start():
    Unknown244()
    Unknown458(0)
    Unknown451('53424e31500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    if (SLOT_115 == 2):
        Unknown451('53424e33500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    if (SLOT_115 == 3):
        Unknown451('53424e32500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    if SLOT_4:
        Unknown2522(0)
    else:
        Unknown2522(1)
    Unknown2189(0, 1)
    Unknown1731(-100000)
    Unknown1926(1)
    Unknown1928(1)
    Unknown251(0)
    Unknown249(155000)
    Unknown250(220000)
    Unknown268(1)
    Unknown287(1)
    Unknown1914(0)
    callSubroutine('cmnAtkLevel_3_AtkInit')
    callSubroutine('cmnSpecialShot_AtkInit')
    Unknown1028(0)
    Unknown1112(0)
    Unknown1051(0)
    Unknown1954(0)
    Unknown1058(1)
    Unknown1203(0)
    Unknown1117(0)
    Unknown1143(1)
    Unknown1045('04000000636d6e5f6869745f730000000000000000000000000000000000000000000000')
    Unknown1202('4152435f42544c5f434d4e5f4869745f4d69646c652d41000000000000000000')
    Unknown1119('ARC_BTL_CMN_Guard_Midle')
    Unknown36(13, 1800)

    def upon_13():
        callSubroutine('sbn_ClearInterrupt')
        Unknown14('end')
    Unknown2188(0)
    Unknown2209(1)

    def upon_45():
        callSubroutine('sbn_ClearInterrupt')
        Unknown14('koware')
        Unknown295(1)

    def upon_11():
        Unknown606(1)
        Unknown618('7673626e303030000000000000000000640000007673626e303031000000000000000000640000007673626e303032000000000000000000640000007673626e30303300000000000000000064000000')

    def upon_12():
        if (not SLOT_16):
            callSubroutine('sbn_ClearInterrupt')
            Unknown14('end')
        if conditionalunk2499(2, 2, 263):
            callSubroutine('sbn_ClearInterrupt')
            Unknown14('end')
            Unknown295(1)
        if Unknown2033(2, 'CmnActFuttobiFinish'):
            callSubroutine('sbn_ClearInterrupt')
            Unknown14('end')
        if Unknown2033(32, 'CmnActFuttobiFinish'):
            callSubroutine('sbn_ClearInterrupt')
            Unknown14('end')
        if Unknown2033(2, 'CmnActLockWait'):
            callSubroutine('sbn_ClearInterrupt')
            Unknown14('end')
            Unknown295(1)
        if SLOT_24:
            Unknown251(0)
    storeValue(2, 3, 0, 1)

    def upon_1():
        storeValue(2, 3, 0, 0)

@Subroutine
def sbn_ClearInterrupt():
    Unknown23(3)
    Unknown23(12)
    Unknown23(2)
    Unknown23(45)
    Unknown23(23)
    Unknown23(24)
    Unknown23(13)

@Subroutine
def sbn_end():
    Unknown23(45)
    beginRecovery()
    Unknown176(1)
    Unknown251(0)
    Unknown451('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@Subroutine
def sbn_atk():
    Unknown54('00000000020000002d0000000000000001000000')
    storeValue(2, 46, 0, 0)
    if (SLOT_115 == 1):
        if (SLOT_45 == 1):
            storeValue(2, 46, 0, 1)
        if (SLOT_45 == 2):
            storeValue(2, 46, 0, 3)
    if (SLOT_115 == 2):
        if (SLOT_45 == 1):
            storeValue(2, 46, 0, 2)
        if (SLOT_45 == 2):
            storeValue(2, 46, 0, 3)
    if (SLOT_115 == 3):
        if SLOT_54:
            if (SLOT_45 == 1):
                if (not SLOT_51):
                    Unknown52('0300000002000000360000000000000010270000020000002e000000')
                    SLOT_46 = (SLOT_46 * (-10000))
                    Unknown54('0000000002000000360000000200000000000000')
                    storeValue(2, 51, 2, 46)
                storeValue(2, 46, 2, 51)
            if (SLOT_45 == 2):
                if (not SLOT_51):
                    Unknown52('03000000020000003600000000000000e8030000020000002e000000')
                    SLOT_46 = (SLOT_46 * (-1000))
                    Unknown54('0000000002000000360000000200000000000000')
                    storeValue(2, 51, 2, 46)
                storeValue(2, 46, 2, 51)
            if (SLOT_45 == 3):
                if (not SLOT_51):
                    Unknown52('0300000002000000360000000000000064000000020000002e000000')
                    SLOT_46 = (SLOT_46 * (-100))
                    Unknown54('0000000002000000360000000200000000000000')
                    storeValue(2, 51, 2, 46)
                storeValue(2, 46, 2, 51)
            if (SLOT_45 == 4):
                if (not SLOT_51):
                    Unknown52('030000000200000036000000000000000a000000020000002e000000')
                    SLOT_46 = (SLOT_46 * (-10))
                    Unknown54('0000000002000000360000000200000000000000')
                    storeValue(2, 51, 2, 46)
                storeValue(2, 46, 2, 51)
        else:
            if (SLOT_45 == 1):
                storeValue(2, 46, 0, 2)
            if (SLOT_45 == 2):
                storeValue(2, 46, 0, 1)
            if (SLOT_45 == 3):
                storeValue(2, 46, 0, 2)
            if (SLOT_45 == 4):
                storeValue(2, 46, 0, 3)

@Subroutine
def sbn_search():
    if conditionalunk2498(4, 2, 263):
        storeValue(2, 47, 0, 600000)
        if (SLOT_46 == 1):
            storeValue(2, 47, 0, 400000)
        if (SLOT_46 == 2):
            storeValue(2, 47, 0, 800000)
        if (SLOT_46 == 3):
            storeValue(2, 47, 0, 600000)
        Unknown53(23, 2, 48, 4, 2, 83)
        if SLOT_32:
            Unknown52('01000000020000005300000002000000300000000200000030000000')
        else:
            Unknown52('01000000020000003000000002000000530000000200000030000000')
        if (SLOT_48 <= (-1)):
            Unknown176(1)
            Unknown1304()
            Unknown23(3)
            Unknown14('turn')
            Unknown54('01000000020000002d0000000000000001000000')
        elif (SLOT_48 <= SLOT_47):
            Unknown176(1)
            Unknown1304()
            Unknown23(3)
            Unknown14('jibaku')
            if (SLOT_46 == 1):
                Unknown14('rush')
            if (SLOT_46 == 2):
                Unknown14('youkaieki')
            if (SLOT_46 == 3):
                Unknown14('sliding')
        if (SLOT_105 > 60):
            Unknown176(1)
            Unknown1304()
            Unknown23(3)
            Unknown14('jibaku')
            if (SLOT_46 == 1):
                Unknown14('rush')
            if (SLOT_46 == 2):
                Unknown14('youkaieki')
            if (SLOT_46 == 3):
                Unknown14('sliding')
    else:
        Unknown43(4, 32)

@Subroutine
def sbn_jibaku_countdown():
    if (not 
    Unknown2031('2000000053616962616d656e000000000000000000000000000000000000000000000000')):
        Unknown23(12)
        Unknown14('jibaku_explosion')
        Unknown294(1)
    if (not SLOT_16):
        Unknown23(12)
        Unknown14('jibaku_explosion')
    Unknown2037(0, 32, 116)

@State
def Saibamen():

    def upon_IMMEDIATE():

        def upon_23():
            Unknown23(23)
            Unknown19(23)
        storeValue(2, 49, 0, 60)

        def upon_24():
            Unknown23(24)
            Unknown54('000000000200000031000000000000005a000000')
        ActivateEffScript('sbn_marker', 100)
        Unknown42('17000000050000000200000004000000')
        if Unknown51(5):
            if conditionalunk2500(10, 5, 2, 200, 0, 1801):
                Unknown19(5)
                storeValue(2, 3, 0, 0)
        else:
            storeValue(2, 3, 0, 0)
    label('sbn_pre_selection')
    sprite('null', 1)
    Unknown54('0100000002000000310000000000000001000000')
    if SLOT_3:
        Unknown54('0000000002000000310000000000000001000000')
    elif conditionalunk2498(2, 2, 24):
        Unknown54('0000000002000000310000000000000001000000')
    if (SLOT_13 >= 900):
        Unknown19(23)
    Unknown13('73626e5f7072655f73656c656374696f6e0000000000000000000000000000000c00000002000000310000000000000001000000')
    Unknown3()
    label('sbn_selection')
    sprite('null', 1)
    if SLOT_3:
        Unknown2315(1)
    elif conditionalunk2498(2, 2, 24):
        Unknown2315(1)
    else:
        Unknown32('sbn_marker')
        Unknown2055(0)
        Unknown42('02000000040000001700000017000000')
        Unknown23(23)
        Unknown23(24)
        callSubroutine('sbn_start')
        Unknown14('birth')
        Unknown1927(1)
        Unknown53(23, 2, 54, 3, 2, 54)
    Unknown3()
    Unknown13('73626e5f73656c656374696f6e000000000000000000000000000000000000000d000000020000000d0000000000000084030000')
    Unknown18()
    label('birth')
    sprite('sbn200_00', 3)
    Unknown1698(0)
    Unknown1700(2)
    Unknown2055(1)
    Unknown2184(1)
    Unknown268(0)
    Unknown469('62675f6e706e3430315f736d6f6b65320000000000000000000000000000000064000000')
    Unknown615('ARC_BTL_NPN_SaibaPlant_Born')
    sprite('sbn200_01', 3)
    sprite('sbn200_02', 3)
    sprite('sbn200_03', 3)
    Unknown606(1)
    Unknown618('7673626e303037000000000000000000640000007673626e303038000000000000000000640000007673626e303039000000000000000000640000000000000000000000000000000000000000000000')
    sprite('sbn200_04', 3)
    sprite('sbn200_05', 3)
    sprite('sbn200_06', 3)
    sprite('sbn200_07', 3)
    sprite('sbn200_08', 3)
    sprite('sbn200_09', 3)
    sprite('sbn200_10', 3)
    sprite('sbn200_11', 3)
    Unknown2184(0)
    Unknown251(1)
    Unknown1927(0)
    sprite('sbn200_12', 3)
    sprite('sbn200_13', 3)
    sprite('sbn200_14', 3)
    sprite('sbn200_15', 3)
    sprite('sbn200_16', 3)
    sprite('sbn200_17', 3)
    sprite('sbn200_18', 3)
    Unknown3()
    label('start')
    sprite('sbn000_00', 2)
    Unknown176(1)
    Unknown755()
    Unknown767()
    Unknown883()
    Unknown895()
    Unknown831()
    Unknown43(4, 32)
    callSubroutine('sbn_atk')

    def upon_3():
        callSubroutine('sbn_search')
    if (not SLOT_24):
        Unknown251(1)
    sprite('sbn030_00', 5)
    physicsImpulseX(7500)
    Unknown1303(500)
    Unknown3()
    label('walk_loop')
    Unknown1698(0)
    Unknown1700(4)
    physicsImpulseX(7500)
    Unknown1303(500)
    sprite('sbn030_01', 5)
    sprite('sbn030_02', 5)
    sprite('sbn030_03', 5)
    sprite('sbn030_04', 5)
    sprite('sbn030_05', 5)
    sprite('sbn030_06', 5)
    sprite('sbn030_07', 5)
    sprite('sbn030_08', 5)
    Unknown3()
    labelEnd('walk_loop')
    label('turn')
    sprite('sbn001_00', 2)
    sprite('sbn001_01', 2)
    Unknown3()
    Unknown239()
    labelEnd('start')
    label('rush')
    sprite('sbn201_00', 3)
    Unknown1698(0)
    Unknown1700(4)
    sprite('sbn201_01', 3)
    sprite('sbn201_02', 3)
    Unknown606(1)
    Unknown618('7673626e303130000000000000000000640000007673626e303131000000000000000000640000007673626e303132000000000000000000640000000000000000000000000000000000000000000000')
    Unknown615('ARC_BTL_NPN_SaibaPlant_Jump')
    sprite('sbn201_03', 2)
    physicsImpulseX(30000)
    physicsImpulseY(35000)
    Unknown135()
    Unknown1975(-55000)
    Unknown1303(500)

    def upon_2():
        Unknown14('rush_landing')
    sprite('sbn201_04', 2)
    sprite('sbn201_05', 2)
    Unknown615('ARC_BTL_NPN_SaibaPlant_Kick')
    sprite('sbn201_06', 6)
    storeValue(2, 51, 0, 0)
    makeActive()
    if (SLOT_115 == 3):
        callSubroutine('cmnSpecialAttackEx_TimeLagShotI')
    damage1(700)
    untech_Override(30)
    mod_opphitstop(0, 0, 0)
    or_standhit(1)
    ActivateEffScript('saibaiman_claw', 100)
    sprite('sbn201_07', 2)
    sprite('sbn201_08', 2)
    Unknown2229(95)
    Unknown1915()
    Unknown1304()
    sprite('sbn201_09', 2)
    sprite('sbn201_10', 2)
    sprite('sbn201_11', 2)
    sprite('sbn201_12', 2)
    sprite('sbn201_13', 2)
    sprite('sbn201_14', 2)
    sprite('sbn201_15', 30)
    Unknown3()
    label('rush_landing')
    sprite('sbn201_16', 3)
    Unknown2229(50)
    Unknown1975(-1)
    sprite('sbn201_17', 3)
    sprite('sbn201_18', 3)
    sprite('sbn201_19', 3)
    sprite('sbn201_20', 3)
    sprite('sbn201_21', 3)
    Unknown3()
    labelEnd('start')
    label('youkaieki')
    sprite('sbn202_00', 4)
    sprite('sbn202_01', 4)
    sprite('sbn202_02', 4)
    sprite('sbn202_03', 5)
    Unknown606(1)
    Unknown618('7673626e303133000000000000000000640000007673626e303134000000000000000000640000007673626e303134000000000000000000640000000000000000000000000000000000000000000000')
    Unknown632('000000004152435f42544c5f4e504e5f5361696261506c616e745f456b6946697265000064000000')
    sprite('sbn202_04', 6)
    sprite('sbn202_05', 7)
    sprite('sbn202_06', 3)
    Unknown1697(20)
    sprite('sbn202_07', 2)
    storeValue(2, 51, 0, 0)
    if (SLOT_115 == 3):
        Unknown2279('00000000030000000000000000000000')
    Unknown445('73626e5f796f756b6169656b695f61746b00000000000000000000000000000000000000')
    sprite('sbn202_08', 1)
    Unknown1915()
    sprite('sbn202_09', 1)
    sprite('sbn202_10', 2)
    sprite('sbn202_11', 2)
    Unknown1698(0)
    Unknown1700(4)
    sprite('sbn202_12', 2)
    sprite('sbn202_13', 2)
    Unknown3()
    labelEnd('start')
    label('sliding')
    sprite('sbn203_00', 3)
    Unknown1698(0)
    Unknown1700(4)
    sprite('sbn203_01', 3)
    Unknown606(1)
    Unknown618('7673626e303136000000000000000000640000007673626e303137000000000000000000640000007673626e303138000000000000000000640000000000000000000000000000000000000000000000')
    sprite('sbn203_02', 3)
    Unknown615('ARC_BTL_NPN_SaibaPlant_LoKick')
    sprite('sbn203_03', 2)
    physicsImpulseX(10000)
    Unknown250(110000)
    Unknown1303(500)
    sprite('sbn203_04', 2)
    physicsImpulseX(20000)
    sprite('sbn203_05', 2)
    physicsImpulseX(45000)
    storeValue(2, 51, 0, 0)
    makeActive()
    if (SLOT_115 == 3):
        callSubroutine('cmnSpecialAttackEx_TimeLagShotI')
    damage1(600)
    airHitPushbackX(5000)
    airHitPushbackY(22500)
    or_standhit(10)
    or_launchhit(10)
    untech_Override(25)
    mod_opphitstop(3, 3, 3)
    ActivateEffScript('Sliding', 100)
    sprite('sbn203_06', 6)
    sprite('sbn203_07', 3)
    Unknown250(220000)
    Unknown2229(80)
    Unknown1915()
    Unknown1304()
    Unknown32('Sliding')
    sprite('sbn203_08', 3)
    sprite('sbn203_09', 3)
    sprite('sbn203_10', 3)
    sprite('sbn203_11', 3)
    sprite('sbn203_12', 3)
    Unknown3()
    labelEnd('start')
    label('jibaku')
    sprite('sbn204_00', 4)
    Unknown1698(0)
    Unknown1700(4)
    sprite('sbn204_01', 5)
    sprite('sbn204_02', 6)
    sprite('sbn204_03', 2)
    Unknown606(1)
    Unknown618('7673626e303139000000000000000000640000007673626e303230000000000000000000640000007673626e303231000000000000000000640000000000000000000000000000000000000000000000')
    Unknown615('ARC_BTL_NPN_SaibaPlant_Hold')
    sprite('sbn204_04', 2)
    Unknown1697(20)
    Unknown1700(3)
    physicsImpulseX(40000)
    physicsImpulseY(20000)
    Unknown135()
    Unknown1303(500)

    def upon_2():
        Unknown14('jibaku_landing')

    def upon_3():
        if conditionalunk2498(4, 2, 263):
            Unknown53(23, 2, 48, 4, 2, 83)
            if SLOT_32:
                Unknown52('01000000020000005300000002000000300000000200000030000000')
            else:
                Unknown52('01000000020000003000000002000000530000000200000030000000')
            if (SLOT_48 <= 250000):
                Unknown111(90)
        else:
            Unknown43(4, 32)
    sprite('sbn204_05', 3)
    sprite('sbn204_06', 3)
    sprite('sbn204_07', 30)
    Unknown23(3)
    Unknown251(0)
    Unknown1304()
    callSubroutine('cmnAtkLevel_0_AtkInit')
    callSubroutine('cmnSpecialShot_AtkInit')
    if (SLOT_115 == 3):
        callSubroutine('cmnSpecialAttackEx_TimeLagShotI')
    damage1(0)
    Unknown1117(0)
    Unknown1095(0)
    mod_opphitstop(0, 0, 0)
    hitstun_Override(60)
    untech_Override(60)
    grHitPushbackX(25)
    Unknown1027(100000, 0, 150000, -200000)
    or_standhit(4)
    or_launchhit(4)
    Unknown1073(1)

    def upon_89():
        Unknown23(2)
        Unknown23(89)
        Unknown23(45)
        Unknown23(12)
        Unknown23(13)
        Unknown14('jibaku_hit')
        Unknown1142(1)
        Unknown1111(1)
        Unknown1915()
        Unknown176(1)
        Unknown1827(1)
        Unknown251(0)
        Unknown1927(1)
        Unknown1731(100000)
        Unknown2189(2, 5)
        Unknown615('ARC_BTL_NPN_SaibaPlant_HoldHit')
        storeValue(2, 265, 0, 1)
    if (not SLOT_265):
        makeActive()
    Unknown1202('64616d6d79000000000000000000000000000000000000000000000000000000')
    Unknown1119('')
    storeValue(2, 51, 0, 0)
    label('jibaku_landing')
    sprite('sbn204_08', 4)
    Unknown2229(75)
    beginRecovery()
    sprite('sbn204_09', 4)
    sprite('sbn204_10', 4)
    sprite('sbn204_11', 4)
    sprite('sbn204_12', 4)
    sprite('sbn204_13', 4)
    Unknown1698(0)
    Unknown1700(4)
    sprite('sbn000_00', 6)
    sprite('sbn000_01', 6)
    sprite('sbn000_02', 6)
    sprite('sbn000_03', 6)
    sprite('null', 1)
    callSubroutine('sbn_end')
    Unknown2193(103, 0, 150000)
    Unknown448('cmn_Warp', 130)
    Unknown615('ARC_BTL_NPN_SaibaPlant_Gone')
    Unknown3()
    Unknown18()
    label('jibaku_hit')

    def upon_12():
        callSubroutine('sbn_jibaku_countdown')
    Unknown67(3)
    goto('jibaku_countdown_XL', 2, 0)
    sprite('sbn204_16', 5)
    sprite('sbn204_17', 25)
    Unknown3()
    labelEnd('jibaku_explosion')
    label('jibaku_countdown_XL')
    sprite('sbn204_14', 5)
    sprite('sbn204_15', 25)
    Unknown3()
    label('jibaku_explosion')
    sprite('sbn204_explosion', 1)
    ActivateEffScript('cmn_kidan_end_M', 100)
    Unknown338(0)
    Unknown2055(0)
    Unknown448('bg_groundsmokeM', 123)
    Unknown670('00000000b80b00000000000000000000')
    callSubroutine('cmnAtkLevel_3_AtkInit')
    callSubroutine('cmnSpecialShot_AtkInit')
    if (SLOT_115 == 3):
        callSubroutine('cmnSpecialAttackEx_TimeLagShotI')
    damage1(1334)
    Unknown1117(0)
    Unknown1059(0)
    or_standhit(27)
    or_launchhit(27)
    airHitPushbackX(5000)
    airHitPushbackY(50000)
    Unknown1027(-1, -1, -1, -1)
    Unknown854(0)
    untech_Override(50)
    mod_hitstop(5)
    Unknown1079(1)
    Unknown1051(0)
    Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
    Unknown1157(0)
    Unknown717('ShakeTate', 2000, 0, 30, 10)
    Unknown1143(1)
    Unknown1202('64616d6d79000000000000000000000000000000000000000000000000000000')
    Unknown1119('ARC_BTL_CMN_Guard_Kidan')
    makeActive()
    Unknown615('ARC_BTL_NPN_SaibaPlant_Expl')
    sprite('null', 1)
    callSubroutine('sbn_end')
    Unknown3()
    Unknown18()
    label('koware')
    sprite('sbn060_00', 3)
    Unknown23(45)
    Unknown1827(1)
    Unknown176(1)
    sprite('sbn060_03', 5)
    physicsImpulseX(-20000)
    Unknown2229(95)
    physicsImpulseY(20000)
    Unknown127(1000)
    sprite('sbn060_04', 5)
    sprite('sbn060_05', 5)
    sprite('sbn060_06', 5)
    sprite('sbn060_07', 10)
    sprite('null', 1)
    callSubroutine('sbn_end')
    Unknown2193(103, 0, 150000)
    Unknown448('cmn_Warp', 130)
    Unknown615('ARC_BTL_NPN_SaibaPlant_Gone')
    Unknown3()
    Unknown18()
    label('end')
    sprite('null', 1)
    Unknown1698(0)
    Unknown1700(4)
    callSubroutine('sbn_end')
    Unknown2193(103, 0, 150000)
    Unknown448('cmn_Warp', 130)
    Unknown615('ARC_BTL_NPN_SaibaPlant_Gone')
    Unknown3()
    Unknown18()

@State
def npn_401Eff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
        Unknown471('62675f6e706e3430315f736d6f6b650000000000000000000000000000000000')
    sprite('null', 90)

@State
def saibaiman_claw():

    def upon_IMMEDIATE():
        Unknown454(2)
    sprite('null', 60)
    Unknown450('npn_401_claw')

@State
def sbn_marker():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('npn_401_marker')
        Unknown188(1300)
        Unknown289(1200)
    sprite('null', 2147483647)

@State
def sbn_youkaieki_atk():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkLevel_1_AtkInit')
        callSubroutine('cmnSpecialShot_AtkInit')
        if (SLOT_115 == 3):
            callSubroutine('cmnSpecialAttackEx_TimeLagShotI')
        Unknown1028(1)
        damage1(400)
        grHitPushbackX(50)
        airHitPushbackX(0)
        airHitPushbackY(0)
        or_standhit(4)
        or_launchhit(17)
        Unknown1128(1)
        Unknown1149(0)
        Unknown1051(0)
        mod_hitstop(10)
        Unknown1023(20)
        hitstun_Override(20)
        untech_Override(20)
        Unknown1117(0)
        Unknown1183(0)
        Unknown893(1)
        Unknown717('ShakeTate', 600, 0, 20, 10)
        Unknown1118('dammy')
        Unknown1119('ARC_BTL_CMN_Guard_Midle')

        def upon_89():
            Unknown23(89)

            def upon_3():
                if SLOT_214:
                    Unknown41(32)
                    Unknown135()
                    Unknown40()
                else:
                    Unknown23(3)
        Unknown1914(0)
        Unknown289(300)
        Unknown458(0)
        Unknown58(1)
        Unknown1732(75000)
        Unknown2211(1)
        Unknown2221(1)
        Unknown2212(1)
        Unknown2213(1)
        Unknown2214(1)
        Unknown2215(1)
        Unknown35('2d0000004b6f776172650000000000000000000000000000000000000000000000000000')

        def upon_2():
            Unknown2208(23)

        def upon_87():
            Unknown23(87)
            ActivateEffScript('cmn_reversal_mazzle', 101)
            Unknown19(23)
            Unknown450('')
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
        Unknown448('npn_401_splash_shot', 100)
        ActivateEffScript('Youkaieki', 100)
        Unknown43(7, 1)
    sprite('youkaieki', 1)
    makeActive()
    Unknown2055(0)
    Unknown3()
    sprite('youkaieki', 3)
    Unknown2055(1)
    Unknown58(1)
    physicsImpulseX(20000)
    physicsImpulseY(15000)
    Unknown127(750)
    sprite('youkaieki', 600)
    Unknown3()
    label('Koware')
    sprite('null', 10)
    Unknown176(1)
    Unknown448('npn_401_splash_del', 100)
    Unknown615('ARC_BTL_NPN_SaibaPlant_EkiHit')
    if Unknown51(7):
        Unknown19(7)

@State
def Youkaieki():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown450('npn_401_splash')
        Unknown289(100)
    label('Loop')
    sprite('null', 2)
    Unknown448('npn_401_splash_add', 100)
    Unknown3()
    labelEnd('Loop')

@State
def Sliding():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown188(960)
        Unknown450('npn_401_sliding')
        Unknown289(100)
    label('Loop')
    sprite('null', 4)
    Unknown2273(0, 500)
    Unknown470('62675f756e646572736d6f6b653030000000000000000000000000000000000064000000')
    Unknown3()
    labelEnd('Loop')

@Subroutine
def pi_init():
    Unknown244()
    callSubroutine('cmnAtkLevel_3_AtkInit')
    callSubroutine('cmnSpecialShot_AtkInit')
    callSubroutine('cmn_AssistShotHosei')
    damage1(1100)
    Unknown1117(1200)
    or_standhit(27)
    or_launchhit(27)
    airHitPushbackX(5000)
    airHitPushbackY(40000)
    grHitPushbackX(150)
    mod_hitstop(20)
    Unknown1051(0)
    Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
    Unknown1058(1)
    if conditionalunk2499(2, 2, 263):
        damage1(850)
        Unknown1117(0)
        callSubroutine('cmn_AssistHosei')
        if (SLOT_104 >= 400000):
            Unknown94(500000)
    Unknown1118('ARC_BTL_CMN_Hit_Kidan')
    Unknown1119('ARC_BTL_CMN_Guard_Beam')
    Unknown289(300)
    Unknown1954(1)
    Unknown287(1)
    Unknown458(0)
    if Unknown48(28):
        Unknown94(500000)
    Unknown188(1500)
    Unknown1914(0)
    if SLOT_115:
        Unknown2303(1000)
        Unknown450('cmn_bomb_s2')
        Unknown2077('ShakeTate', 1800, 0, 30, 10)
        Unknown53(23, 2, 18, 2, 2, 18)
        Unknown99(-10000)
        untech_Override(15)
    else:
        Unknown450('cmn_bomb_g1')
        Unknown2077('ShakeTate', 1800, 0, 30, 10)
        untech_Override(25)
    if (SLOT_18 <= 150000):
        Unknown2273(0, 800)
        Unknown449('bg_groundsmokeM', 123)
        Unknown670('01000000e80300000000000000000000')
    Unknown2136('000000000000000000000000f4010000000000003c0000001e000000')
    Unknown615('ARC_BTL_NPN_Pi_Expl')

@State
def pi_explosion():

    def upon_IMMEDIATE():
        Unknown458(2)
    goto('air', 2, 115)
    sprite('null', 4)
    sprite('pi_explosion', 10)
    callSubroutine('pi_init')
    makeActive()
    sprite('null', 70)
    beginRecovery()
    Unknown1801(0)
    Unknown18()
    label('air')
    sprite('null', 6)
    sprite('pi_explosion_air', 10)
    callSubroutine('pi_init')
    makeActive()
    sprite('null', 70)
    beginRecovery()
    Unknown1801(0)

@State
def npn_402Eff_finger():

    def upon_IMMEDIATE():
        Unknown458(2)
        Unknown454(2)
        Unknown456(2)
        Unknown450('npn_402_finger')
        Unknown1732(-50000)
        Unknown188(560)
        Unknown289(600)
    sprite('null', 2147483647)

@State
def npn_402Eff_finger2():

    def upon_IMMEDIATE():
        Unknown458(2)
        Unknown454(2)
        Unknown456(2)
        Unknown450('npn_402_finger')
        Unknown1732(-10000)
        Unknown188(750)
        Unknown289(600)
    sprite('null', 2147483647)

@State
def npn_402Eff_finger3():

    def upon_IMMEDIATE():
        Unknown458(2)
        Unknown454(2)
        Unknown456(2)
        Unknown450('npn_402_finger')
        Unknown1732(30000)
        Unknown188(888)
        Unknown289(600)
    sprite('null', 2147483647)

@State
def npn_402Eff_finger_end():

    def upon_IMMEDIATE():
        Unknown458(2)
        Unknown454(2)
        Unknown456(2)
        Unknown1732(-60000)
        Unknown99(0)
    sprite('null', 5)
    Unknown450('npn_402_finger')
    sprite('null', 15)
    Unknown450('npn_402_finger_end')

@State
def npn_402Eff_trail():

    def upon_IMMEDIATE():
        Unknown458(2)
        Unknown454(2)
        Unknown456(2)
        Unknown450('npn_402_trail')
    sprite('null', 60)

@State
def npn_403Eff_finger():

    def upon_IMMEDIATE():
        Unknown458(2)
        Unknown454(2)
        Unknown456(2)
        Unknown450('npn_402_finger')
        Unknown1732(60000)
        Unknown188(560)
        Unknown289(600)
    sprite('null', 2147483647)

@State
def npn_403Eff_finger2():

    def upon_IMMEDIATE():
        Unknown458(2)
        Unknown454(2)
        Unknown456(2)
        Unknown450('npn_402_finger')
        Unknown1732(120000)
        Unknown188(750)
        Unknown289(600)
    sprite('null', 2147483647)

@State
def npn_403Eff_finger3():

    def upon_IMMEDIATE():
        Unknown458(2)
        Unknown454(2)
        Unknown456(2)
        Unknown450('npn_402_finger')
        Unknown1732(180000)
        Unknown188(888)
        Unknown289(600)
    sprite('null', 2147483647)

@State
def npn_403Eff_finger_end():

    def upon_IMMEDIATE():
        Unknown458(2)
        Unknown454(2)
        Unknown456(2)
        Unknown1732(160000)
        Unknown99(-40000)
    sprite('null', 5)
    Unknown450('npn_402_finger')
    sprite('null', 15)
    Unknown450('npn_402_finger_end')

@State
def npn_403Eff_trail():

    def upon_IMMEDIATE():
        Unknown458(2)
        Unknown454(2)
        Unknown456(2)
        Unknown450('npn_403_trail')
    sprite('null', 60)

@State
def npn_430Eff_aura():

    def upon_IMMEDIATE():
        Unknown457(3)
        Unknown458(2)
        Unknown454(2)
        Unknown456(2)
        Unknown450('npn_430_aura')
        Unknown289(600)
    sprite('null', 2147483647)

@State
def npn_430Eff_aura_end():

    def upon_IMMEDIATE():
        Unknown457(3)
        Unknown458(2)
        Unknown454(2)
        Unknown456(2)
        Unknown450('npn_430_aura_end')
        Unknown289(600)
    sprite('null', 2147483647)

@State
def npn_430Eff_aura2():

    def upon_IMMEDIATE():
        Unknown457(3)
        Unknown458(2)
        Unknown454(2)
        Unknown456(2)
        Unknown450('npn_430_aura2')
        Unknown289(600)
    sprite('null', 125)
    sprite('null', 2147483647)
    Unknown450('npn_430_aura2_end')

@State
def kun_explosion():

    def upon_IMMEDIATE():
        Unknown245()
        callSubroutine('cmnAtkLevel_4_AtkInit')
        callSubroutine('cmnUltimateShot_AtkInit')
        damage1(2300)
        Unknown1086(35)
        or_standhit(27)
        or_launchhit(27)
        airHitPushbackX(10000)
        airHitPushbackY(60000)
        untech_Override(35)
        mod_hitstop(20)
        mod_opphitstop(0, 5, 5)
        Unknown1051(0)
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
        if SLOT_115:
            Unknown94(400000)
            airHitPushbackX(-15000)
            grHitPushbackX(-100)
            Unknown1067(3, -100, 0)
        Unknown1966(1)
        Unknown1112(0)
        Unknown1118('ARC_BTL_CMN_Hit_Kidan')
        Unknown1119('ARC_BTL_CMN_Guard_Beam')
        Unknown289(300)
        Unknown94(800000)
        Unknown1954(1)
        Unknown287(1)
        if (SLOT_83 <= (-3100000)):
            storeValue(2, 83, 0, -3100000)
        if (SLOT_83 >= 3100000):
            storeValue(2, 83, 0, 3100000)
        if SLOT_115:
            Unknown287(0)
            if (SLOT_83 <= (-3100000)):
                storeValue(2, 83, 0, -3500000)
            if (SLOT_83 >= 3100000):
                storeValue(2, 83, 0, 3500000)
        ActivateEffScript('npn_430_Bomber', 100)
        Unknown2193(123, 230000, 0)
        Unknown2273(0, 1100)
        Unknown449('bg_groundsmokeL', 130)
        Unknown2193(123, -230000, 0)
        Unknown2277(1)
        Unknown2273(0, 1100)
        Unknown449('bg_groundsmokeL', 130)
        Unknown670('01000000881300000000000000000000')
        Unknown2077('ShakeTateYoko', 3000, 0, 50, 20)
        Unknown477('00000000000000000000000010270000')

        def upon_90():
            callSubroutine('cmnUltimate_CameraCombo')

        def upon_92():
            Unknown23(92)
            if Unknown2033(2, 'Kun'):
                Unknown1803('Kun', 23)
                storeValue(2, 45, 0, 1)

        def upon_3():
            Unknown189(100)
            if (SLOT_99 >= 1000):
                Unknown23(3)
                Unknown188(1000)
    sprite('kun_explosion', 5)
    makeActive()
    sprite('null', 5)
    beginRecovery()
    sprite('null', 55)
    Unknown1801(0)
    Unknown23(92)
    if (not SLOT_45):
        if Unknown2033(2, 'Kun'):
            Unknown1803('Kun', 24)

@State
def npn_430_Bomber():

    def upon_IMMEDIATE():
        Unknown458(2)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 60)
    Unknown448('npn_430_Bomber', 100)
    Unknown615('ARC_BTL_NPN_Kun_Expl')
    Unknown2273(0, 1375)
    Unknown445('636d6e5f626f6d625f67325f656e64000000000000000000000000000000000064000000')

@State
def npn_431_punch():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown295(1)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 1)
    Unknown450('npn_431_punch')
    sprite('null', 60)
    Unknown456(0)

@State
def npn_431_punch_add():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown295(1)
        Unknown454(2)
        Unknown456(2)
        Unknown450('npn_431_punch_add')
    sprite('null', 1)
    sprite('null', 60)
    Unknown456(0)

@State
def npn_431_aura():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown295(1)
        Unknown454(2)
        Unknown289(600)
        Unknown2519(1)
    sprite('null', 2147483647)
    Unknown450('npn_431_aura')

@State
def npn_431_aura_end():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown454(2)
        Unknown2519(1)
    sprite('null', 30)
    Unknown450('npn_431_aura_end')

@State
def npn_431_lines():

    def upon_IMMEDIATE():
        Unknown457(2)
    sprite('null', 60)
    Unknown450('npn_431_lines')

@State
def npn_431_smoke_group():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown295(1)
        Unknown94(195000)
        Unknown98(5000)
        Unknown289(600)
    label('loop')
    sprite('null', 10)
    ActivateEffScript('npn_431_smoke', 100)
    labelEnd('loop')

@State
def npn_431_smoke():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown295(1)
        Unknown1801(1)
        Unknown232(190000)
        Unknown1732(300000)
        Unknown188(1600)
        Unknown148(2100)
    sprite('null', 30)
    Unknown1955('62675f756e646572736d6f6b6530300000000000000000000000000000000000')
    Unknown3()

@State
def kapa_Core():

    def upon_IMMEDIATE():
        Unknown456(3)
        Unknown454(3)
        Unknown289(600)
        Unknown94(134000)
        Unknown99(-6000)
        Unknown450('npn_431_core00')
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
        Unknown35('2f000000656e640000000000000000000000000000000000000000000000000000000000')

        def upon_35():
            Unknown454(0)

        def upon_24():
            Unknown23(24)
            storeValue(2, 45, 0, 0)
            Unknown1803('kapa_Atk', 29)
            if Unknown2033(3, 'Kapa'):
                Unknown53(3, 2, 45, 23, 0, 0)
            storeValue(2, 47, 0, 1)

            def upon_24():
                Unknown54('00000000020000002f0000000000000001000000')
                if (SLOT_47 >= 2):
                    if Unknown2033(3, 'Kapa'):
                        Unknown1798(3, 24)

        def upon_3():
            if (not SLOT_46):
                Unknown1804('6b6170615f41746b00000000000000000000000000000000000000000000000017000000')
    label('loop')
    sprite('null', 2)
    Unknown54('0000000002000000300000000000000001000000')
    Unknown2279('02000000300000000000000000000000')
    Unknown445('6b6170615f41746b00000000000000000000000000000000000000000000000064000000')
    if (SLOT_45 >= 13):
        Unknown53(1, 2, 45, 23, 0, 1)
    sprite('null', 2)
    Unknown3()
    Unknown54('00000000020000002d0000000000000001000000')
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000002d0000000000000010000000')
    label('end')
    sprite('null', 1)
    Unknown23(23)
    Unknown23(24)
    Unknown23(47)
    Unknown23(3)
    ActivateEffScript('kapa_Atk', 100)
    Unknown1803('kapa_Atk', 30)
    if Unknown2033(3, 'Kapa'):
        Unknown1798(3, 24)
    Unknown456(0)
    Unknown294(1)
    sprite('null', 13)
    Unknown32('kapa_Atk')
    Unknown450('npn_431_core01')
    sprite('null', 35)

@State
def kapa_Atk():

    def upon_IMMEDIATE():
        Unknown245()
        callSubroutine('cmnAtkLevel_4_AtkInit')
        callSubroutine('cmnUltimateShot_AtkInit')
        damage1(260)
        Unknown1086(30)
        mod_hitstop(2)
        mod_opphitstop(0, -1, -1)
        or_standhit(8)
        or_launchhit(8)
        airHitPushbackX(15000)
        airHitPushbackY(10000)
        Unknown1186('01000000204e0000f04902006400000000000000')
        Unknown842(1)
        Unknown790(0)
        untech_Override(100)
        Unknown1187(0)
        Unknown1079(1)
        Unknown1064('6b6170615f41746b000000000000000000000000000000000000000000000000')
        Unknown1192('100000004152435f42544c5f434d4e5f4869745f4265616d4c6f6f705f4c50000000000000000000')
        Unknown1193('110000004152435f42544c5f434d4e5f4772645f4265616d4c6f6f705f4c50000000000000000000')
        Unknown717('ShakeYoko', 1500, 0, 40, 10)
        if (SLOT_115 == 13):
            pass
        if (SLOT_115 == 14):
            damage1(238)
            Unknown1086(33)

        def upon_30():
            Unknown1186('0000000000000000000000000000000000000000')
            airHitPushbackX(100000)
            makeActive()
            damage1(269)
            Unknown1086(29)
            Unknown1064('436d6e4e65757472616c00000000000000000000000000000000000000000000')
        Unknown456(2)
        Unknown454(2)
        Unknown457(2)
        Unknown453(2)
        Unknown289(60)
        Unknown450('npn_431_naka00')
        Unknown1954(1)
        Unknown58(1)

        def upon_23():
            Unknown23(23)
            ActivateEffScript('kapa_End', 100)
            storeValue(2, 46, 0, 1)
            Unknown53(2, 2, 46, 23, 0, 1)
            Unknown1199(1, 0)

            def upon_93():
                Unknown19(23)
                Unknown1798(2, 24)

        def upon_29():
            storeValue(2, 45, 0, 0)

        def upon_8():
            if SLOT_45:
                Unknown1798(2, 23)

        def upon_3():
            if (SLOT_18 <= 500000):
                Unknown670('03000000e80300000000000000000000')
            if (not 
            Unknown53(23, 2, 0, 22, 2, 36)):
                Unknown633(16, 20)
                Unknown633(17, 20)
            if (not 
            Unknown2033(3, 'Kapa')):
                Unknown633(16, 20)
                Unknown633(17, 20)

        def upon_1():
            if SLOT_46:
                storeValue(2, 46, 0, 0)
                Unknown53(2, 2, 46, 23, 0, 0)
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('npn_431_naka01', 100)
    sprite('kapa', 1)
    makeActive()
    Unknown202(90000, 0)
    label('loop')
    sprite('kapa', 1)
    sprite('kapa', 2)
    Unknown2301(1200)
    sprite('kapa', 1)
    Unknown2301(1000)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def kapa_End():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown457(2)
        Unknown289(60)
        Unknown2036(2, 0)
        Unknown58(1)
        Unknown450('npn_431_end00')

        def upon_3():
            if Unknown51(2):
                Unknown2488('02000000190100000200000019010000')
                Unknown2036(2, 0)

        def upon_1():
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
    label('loop')
    sprite('null', 2)
    Unknown2301(1000)
    sprite('null', 2)
    Unknown2301(1200)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def kapa_groundSmoke():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown94(-155000)
        Unknown1732(100000)
        Unknown289(600)
    label('loop')
    sprite('null', 10)
    Unknown448('bg_undersmoke00', 100)
    Unknown3()
    labelEnd('loop')

@State
def kapa_shadow():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown289(300)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown450('cmn_shadowLine_loop')
    Unknown3()
    label('end')
    sprite('null', 1)
    Unknown3()

@State
def npn_600_rocks():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
    sprite('null', 216)
    Unknown450('bg_npn600_rocks')

@State
def npn_600cs_Eff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown294(1)
    sprite('null', 20)
    Unknown450('npn_600cs_anim')
    ActivateEffScript('npn_600cs_Eff2_loop', 100)
    Unknown3()

@State
def npn_600cs_Eff2():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown294(1)
    sprite('null', 35)
    ActivateEffScript('npn_600cs_Eff2_loop', 100)
    sprite('null', 35)
    ActivateEffScript('npn_600cs_Eff2_loop', 100)

@State
def npn_600cs_Eff2_loop():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown294(1)
    sprite('null', 10)
    Unknown450('npn_600cs_anim2')
    Unknown3()

@State
def npn_600cs_Eff3():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown294(1)
        Unknown289(600)
    sprite('null', 2147483647)
    Unknown450('npn_600_aura2')
    Unknown3()

@State
def NPN805():

    def upon_IMMEDIATE():
        Unknown92(0)
        Unknown98(0)
        Unknown1731(0)
    sprite('null', 2147483647)
    Unknown2244(1)
    Unknown2083(1900)
    Unknown2425(0, 0)
    Unknown2045('NPN_YMN803cs', 0)
    Unknown2052('NPN803cs', 23, 0, -1)
    ActivateEffScript('NPN803_YMN', 100)
    ActivateEffScript('NPN803_SBN', 100)

    def upon_3():
        onFrame(0, 170)
        ActivateEffScript('NPN803_FlashEff', 150)
        endIf()
        onFrame(0, 199)
        ActivateEffScript('NPN803_bombEff', 150)
        endIf()
        onFrame(0, 308)
        Unknown32('NPN803_bombEff')
        ActivateEffScript('NPN803_crater', 150)
        ActivateEffScript('NPN803_smoke', 100)
        endIf()
    Unknown3()
    Unknown18()

@State
def NPN803_YMN():

    def upon_IMMEDIATE():
        Unknown92(0)
        Unknown98(0)
        Unknown1731(0)
        Unknown454(2)
        Unknown2494('594d4e0000000000000000000000000000000000000000000000000000000000594d4e5f4e504e38303363730000000000000000000000000000000000000000')
        Unknown457(2)
        Unknown2189(0, 5)
    sprite('null', 2147483647)

@State
def NPN803_Manp01_01():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown451('4d4e5000000000000000000000000000000000000000000000000000000000004d4e505f4e504e38303363735f30310000000000000000000000000000000000')
        Unknown2189(0, 5)
    sprite('null', 2147483647)

@State
def NPN803_SBN():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown451('56535f594d4e5f53424e0000000000000000000000000000000000000000000053424e5f4e504e38303363730000000000000000000000000000000000000000')
        Unknown2189(0, 5)
    sprite('null', 2147483647)

@State
def NPN803_shutyusen():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('npn_803_shutyusen')
    sprite('null', 2147483647)

@State
def NPN803_FlashEff():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('npn_803_flash')
    sprite('null', 30)

@State
def NPN803_bombEff():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('npn_803_bomb')
        Unknown94(4500000)
        Unknown99(-300000)
        Unknown188(800)
        Unknown232(90000)
    sprite('null', 120)

@State
def NPN803_crater():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('npn_803_crater')
        Unknown94(2400000)
        Unknown99(-160000)
        Unknown232(-90000)
    sprite('null', 2147483647)

@State
def NPN803_smoke():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('npn_803_smoke')
        Unknown188(1300)
        Unknown1732(125000)
    sprite('null', 2147483647)

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
    Unknown2076('83cdffff4951040077d50000a6130000f60500000000000048000000000000005a0000001e00000001000000')
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def DUMMYDUMMY():
    sprite('null', 1)