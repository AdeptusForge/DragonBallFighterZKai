@State
def dmy():
    sprite('null', 1)

@State
def okasi():

    def upon_IMMEDIATE():
        callSubroutine('cmn_okasi')
    sprite('null', 2147483647)
    Unknown450('tnn_okasi')

@State
def czn600cs():

    def upon_IMMEDIATE():
        Unknown454(3)
        Unknown456(2)
        Unknown457(2)
        Unknown294(1)
        Unknown2189(0, 2)
        Unknown451('435a4e0000000000000000000000000000000000000000000000000000000000435a4e3630306373000000000000000000000000000000000000000000000000')
    sprite('null', 1200)
    Unknown3()

@State
def tnn_hajiki():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 30)
    Unknown450('tnn301_hajiki')
    Unknown188(400)
    Unknown99(260000)
    Unknown94(160000)
    Unknown615('ARC_BTL_TNN_ShotHajiki_Flash')

@State
def tnn_hajiki_Smoke():

    def upon_IMMEDIATE():
        Unknown456(2)
    sprite('null', 180)
    Unknown471('62675f756e646572736d6f6b6530300000000000000000000000000000000000')

@State
def __202Eff():

    def upon_IMMEDIATE():
        Unknown450('tnn202_punch01')
        Unknown454(2)
        Unknown457(2)
    sprite('null', 30)
    Unknown3()

@State
def __202Eff2():

    def upon_IMMEDIATE():
        Unknown450('tnn202_punch02')
        Unknown454(2)
        Unknown457(2)
    sprite('null', 30)
    Unknown3()

@State
def __202Eff3():

    def upon_IMMEDIATE():
        Unknown450('tnn202_punch03')
        Unknown454(2)
        Unknown457(2)
    sprite('null', 30)
    Unknown3()

@State
def __202Eff4():

    def upon_IMMEDIATE():
        Unknown450('tnn202_punch04')
        Unknown454(2)
        Unknown457(2)
    sprite('null', 30)
    Unknown3()

@State
def kidan_start():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown457(2)
        ActivateEffScript('kidan_start_aura', 100)

        def upon_12():
            Unknown2036(2, 0)
    sprite('null', 1)
    Unknown1732(150000)
    sprite('null', 14)
    Unknown612('ARC_BTL_CMN_kidan_Chrg')

@State
def jumpkidan_start():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown457(2)
        ActivateEffScript('kidan_start_aura', 100)

        def upon_12():
            Unknown2036(2, 0)
    sprite('null', 4)
    Unknown1732(150000)
    sprite('null', 2)
    Unknown612('ARC_BTL_CMN_kidan_Chrg')
    sprite('null', 2)
    Unknown1732(-270000)
    sprite('null', 2)
    Unknown1732(-50000)
    sprite('null', 4)
    Unknown1732(30000)

@State
def kidan_start_aura():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown457(2)
        Unknown454(2)
        Unknown450('cmn_kidan_throw')
    sprite('null', 10)
    Unknown188(100)
    Unknown191(60)
    sprite('null', 2147483647)
    Unknown188(700)
    Unknown191(0)

@State
def kidan_smoke():

    def upon_IMMEDIATE():
        Unknown94(-27000)
    sprite('null', 1)
    Unknown448('bg_undersmoke00', 100)

@State
def kidan_5D():

    def upon_IMMEDIATE():
        Unknown243()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        callSubroutine('cmn5DKidan_AtkInit')
        callSubroutine('cmnKidan_Init')
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
        Unknown2229(102)
        Unknown450('cmn_kidan')
        damage1(750)
        Unknown882(8)
        Unknown894(8)
        airHitPushbackX(20000)
        airHitPushbackY(22500)
        Unknown830(24)
    sprite('kidan', 1)
    makeActive()
    Unknown338(0)
    Unknown3()
    sprite('kidan', 600)
    Unknown338(255)
    Unknown58(1)
    Unknown202(70000, 0)
    label('Koware')
    sprite('null', 10)
    Unknown450('')
    Unknown176(1)

@State
def jumpkidan():

    def upon_IMMEDIATE():
        Unknown243()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        callSubroutine('cmnAir5DKidan_AtkInit')
        callSubroutine('cmnKidan_Init')
        damage1(750)
        Unknown882(8)
        Unknown894(8)
        airHitPushbackX(12000)
        airHitPushbackY(22500)
        Unknown830(23)
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
        Unknown164(-34000)
        Unknown2229(102)
        Unknown2230(102)
        Unknown1731(80000)
        Unknown450('cmn_kidan')
    sprite('kidan_nanamesita0', 1)
    makeActive()
    Unknown2055(0)
    sprite('kidan_nanamesita', 600)
    Unknown58(1)
    Unknown2055(1)
    Unknown202(70000, 0)
    Unknown3()
    label('Koware')
    sprite('null', 10)
    Unknown450('')
    Unknown176(1)

@State
def __402_Eff():

    def upon_IMMEDIATE():
        Unknown450('tnn402_Toss')
        Unknown457(2)
        Unknown99(480000)
    sprite('null', 60)
    Unknown3()

@State
def HaikyukenS():

    def upon_IMMEDIATE():
        Unknown2493('544e4e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown456(3)
        Unknown289(300)
        Unknown249(155000)
        Unknown250(260000)
        Unknown1975(-70000)

        def upon_23():
            Unknown23(23)
            Unknown23(12)
            Unknown14('koware')

        def upon_1():
            Unknown448('cmn_Warp', 103)
            Unknown615('ARC_BTL_TNN_Chnryk_CHZ_TLP')

        def upon_12():
            if (not 
            Unknown2033(3, 'Haikyuken_TossC')):
                if (not 
                Unknown2033(3, 'Haikyuken_AttackC')):
                    Unknown19(23)
    sprite('tnn400_06', 2)
    Unknown1698(6)
    physicsImpulseX(60000)
    Unknown2229(80)
    sprite('tnn400_04', 2)
    sprite('tnn400_05', 2)
    sprite('tnn400_06', 2)
    sprite('tnn400_07', 3)
    beginRecovery()
    sprite('tnn400_08', 3)
    Unknown1700(0)
    sprite('tnn400_09', 3)
    sprite('tnn400_10', 3)
    Unknown176(1)
    sprite('tnn400_11', 2)
    sprite('tnn400_12', 3)
    sprite('tnn400_13', 3)
    sprite('tnn001_00', 3)
    sprite('tnn001_01', 3)
    sprite('tnn000_00', 6)
    Unknown239()
    sprite('tnn000_01', 6)
    sprite('tnn000_02', 6)
    sprite('tnn000_03', 6)
    sprite('tnn000_04', 6)
    sprite('tnn000_05', 6)
    sprite('tnn000_06', 6)
    sprite('tnn000_07', 6)
    sprite('tnn000_08', 6)
    sprite('tnn000_09', 6)
    sprite('tnn000_10', 6)
    sprite('tnn000_11', 6)
    sprite('tnn000_00', 6)
    sprite('tnn000_01', 6)
    sprite('tnn000_02', 6)
    sprite('tnn000_03', 6)
    sprite('tnn000_04', 6)
    sprite('tnn000_05', 6)
    sprite('tnn000_06', 6)
    sprite('tnn000_07', 6)
    sprite('tnn000_08', 6)
    sprite('tnn000_09', 6)
    sprite('tnn000_10', 6)
    sprite('tnn000_11', 6)
    label('koware')
    sprite('tnn000_00', 6)
    sprite('tnn000_01', 6)
    sprite('tnn000_02', 6)

@State
def HaikyukenS2():

    def upon_IMMEDIATE():
        Unknown2493('544e4e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown456(3)
        Unknown268(1)
        Unknown289(300)
        Unknown249(155000)
        Unknown250(260000)
        Unknown1975(-70000)
        Unknown251(1)

        def upon_23():
            storeValue(2, 45, 0, 1)
            Unknown19(23)

        def upon_1():
            if (not SLOT_45):
                Unknown448('cmn_Warp', 103)

        def upon_12():
            if (not 
            Unknown2033(3, 'Haikyuken_TossC')):
                if (not 
                Unknown2033(3, 'Haikyuken_AttackC')):
                    Unknown19(23)
    sprite('tnn402_04', 3)
    Unknown1700(4)
    makeActive()
    sprite('tnn402_05', 2)
    beginRecovery()
    Unknown1698(6)
    sprite('tnn402_06', 2)
    sprite('tnn402_07', 2)
    Unknown1700(0)
    sprite('tnn402_08', 3)
    sprite('tnn402_09', 3)
    sprite('tnn402_10', 3)
    sprite('tnn402_11', 3)
    sprite('tnn000_00', 6)
    sprite('tnn000_01', 6)
    sprite('tnn000_02', 6)
    sprite('tnn000_03', 6)
    sprite('tnn000_04', 6)
    sprite('tnn000_05', 6)
    sprite('tnn000_06', 6)
    sprite('tnn000_07', 6)
    sprite('tnn000_08', 6)
    sprite('tnn000_09', 6)
    sprite('tnn000_10', 6)
    sprite('tnn000_11', 6)
    sprite('tnn000_00', 6)
    sprite('tnn000_01', 6)
    sprite('tnn000_02', 6)
    sprite('tnn000_03', 6)
    sprite('tnn000_04', 6)
    sprite('tnn000_05', 6)
    sprite('tnn000_06', 6)
    sprite('tnn000_07', 6)
    sprite('tnn000_08', 6)
    sprite('tnn000_09', 6)
    sprite('tnn000_10', 6)
    sprite('tnn000_11', 6)

@State
def __403_Eff():

    def upon_IMMEDIATE():
        Unknown450('tnn403_Attack')
        Unknown454(2)
        Unknown456(2)
        Unknown457(2)

        def upon_23():
            Unknown454(0)
            Unknown457(0)
    sprite('null', 30)
    Unknown92(30000)
    Unknown3()

@State
def HaikyukenS3():

    def upon_IMMEDIATE():
        Unknown2493('544e4e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown457(3)
        Unknown456(3)
        Unknown289(60)
        Unknown249(155000)
        Unknown250(260000)
        Unknown1975(-70000)

        def upon_12():
            Unknown2489('02000000120000000200000012000000')

        def upon_1():
            Unknown448('cmn_Warp', 103)
            Unknown615('ARC_BTL_TNN_Chnryk_CHZ_TLP')

        def upon_23():
            Unknown23(12)
            Unknown457(0)
    sprite('tnn032_00ex', 2)
    Unknown1698(6)
    physicsImpulseX(80000)
    Unknown127(2000)
    sprite('tnn032_01ex', 2)
    sprite('tnn403_00', 2)
    Unknown240()
    Unknown2230(85)
    sprite('tnn403_01', 2)
    physicsImpulseX(0)
    sprite('tnn403_02', 2)
    sprite('tnn403_03', 4)
    sprite('tnn403_04', 2)
    sprite('tnn403_05', 3)
    Unknown1700(4)
    ActivateEffScript('403_Eff', 100)
    makeActive()
    sprite('tnn403_06', 2)
    beginRecovery()
    sprite('tnn403_07', 2)
    Unknown1700(0)
    sprite('tnn403_08', 3)
    Unknown2230(100)
    Unknown135()
    sprite('tnn403_09', 3)
    sprite('tnn403_10', 3)
    sprite('tnn403_11', 3)

@State
def HaikyukenS4():

    def upon_IMMEDIATE():
        Unknown2493('544e4e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown456(3)
        Unknown289(60)
        Unknown249(155000)
        Unknown250(260000)
        Unknown1975(-70000)
        Unknown2489('02000000080000000200000008000000')

        def upon_1():
            Unknown448('cmn_Warp', 103)
    sprite('tnn403_06', 2)
    beginRecovery()
    Unknown127(2000)
    sprite('tnn403_07', 2)
    Unknown1700(0)
    sprite('tnn403_08', 3)
    Unknown2230(100)
    Unknown135()
    sprite('tnn403_09', 3)
    sprite('tnn403_10', 3)
    sprite('tnn403_11', 3)

@State
def HaikyukenS_Assist():

    def upon_IMMEDIATE():
        Unknown244()
        Unknown2493('544e4e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown456(3)
        Unknown268(1)
        Unknown289(300)
        Unknown249(155000)
        Unknown250(260000)
        Unknown1975(-70000)
        Unknown251(0)

        def upon_24():
            Unknown23(24)
            Unknown268(0)
            Unknown251(0)

        def upon_1():
            Unknown448('cmn_Warp', 103)
            Unknown615('ARC_BTL_TNN_Chnryk_CHZ_TLP')

        def upon_12():
            if (not 
            Unknown2033(3, 'AssistAttack3')):
                if (not 
                Unknown2033(3, 'AssistAttack3')):
                    Unknown19(23)
    sprite('tnn032_00', 2)
    Unknown2036(32, 123)
    Unknown94(-120000)
    Unknown448('cmn_Warp', 103)
    physicsImpulseX(60000)
    sprite('tnn032_01', 2)
    sprite('tnn402_00', 2)
    Unknown1698(5)
    Unknown239()
    sprite('tnn402_01', 2)
    Unknown176(1)
    sprite('tnn402_02', 2)
    sprite('tnn402_03', 2)
    sprite('tnn402_03', 3)
    Unknown615('ARC_BTL_TNN_Haikyu_TossFuri')
    sprite('tnn402_04', 3)
    Unknown1700(4)
    ActivateEffScript('402_Eff', 100)
    sprite('tnn402_05', 6)
    Unknown251(0)
    Unknown268(0)
    sprite('tnn402_06', 3)
    sprite('tnn402_07', 3)
    Unknown1700(0)
    sprite('tnn402_08', 3)
    sprite('tnn402_09', 3)
    sprite('tnn402_10', 3)
    sprite('tnn402_11', 3)
    sprite('tnn000_00', 6)
    sprite('tnn000_01', 6)
    sprite('tnn000_02', 6)
    sprite('tnn000_03', 6)
    sprite('tnn000_04', 6)
    sprite('tnn000_05', 6)
    sprite('tnn000_06', 6)

@State
def HaikyukenS_Assist2():

    def upon_IMMEDIATE():
        Unknown244()
        Unknown2493('544e4e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown456(3)
        Unknown268(1)
        Unknown289(300)
        Unknown249(155000)
        Unknown250(260000)
        Unknown1975(-70000)
        Unknown251(0)

        def upon_24():
            Unknown23(24)
            Unknown268(0)
            Unknown251(0)

        def upon_1():
            Unknown448('cmn_Warp', 103)
            Unknown615('ARC_BTL_TNN_Chnryk_CHZ_TLP')

        def upon_12():
            if (not 
            Unknown2033(3, 'AssistAttack3')):
                if (not 
                Unknown2033(3, 'AssistAttack3')):
                    Unknown19(23)
    sprite('tnn403_01', 1)
    Unknown2036(32, 100)
    if (SLOT_18 <= 10000):
        storeValue(2, 18, 0, 10000)
    Unknown94(250000)
    Unknown99(100000)
    Unknown240()
    Unknown2055(1)
    Unknown251(1)
    Unknown1975(40000)
    Unknown1698(5)
    Unknown612('ARC_BTL_CMN_TLP_Short')
    Unknown448('cmn_Warp', 103)
    sprite('tnn403_02', 2)
    Unknown53(23, 2, 8, 32, 2, 8)
    if (SLOT_8 >= 25000):
        physicsImpulseY(25000)
        Unknown135()
    if (SLOT_8 <= 0):
        physicsImpulseY(0)
    sprite('tnn403_03', 4)
    sprite('tnn403_04', 2)
    sprite('tnn403_05', 3)
    Unknown1700(4)
    ActivateEffScript('403_Eff', 100)
    Unknown2230(70)
    sprite('tnn403_06', 2)
    beginRecovery()
    Unknown251(0)
    Unknown268(0)
    Unknown2230(100)
    Unknown135()
    sprite('tnn403_07', 2)
    Unknown1700(0)
    sprite('tnn403_08', 3)
    sprite('tnn403_09', 3)
    sprite('tnn403_10', 3)
    sprite('tnn403_11', 3)

@State
def HaikyukenS_Assist3():

    def upon_IMMEDIATE():
        Unknown244()
        Unknown2493('544e4e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown456(3)
        Unknown289(300)
        Unknown249(155000)
        Unknown250(260000)
        Unknown1975(-70000)
        Unknown251(0)
        Unknown42('17000000040000000200000007000000')

        def upon_24():
            Unknown23(24)
            Unknown268(0)
            Unknown251(0)

        def upon_1():
            Unknown448('cmn_Warp', 103)
            Unknown615('ARC_BTL_TNN_Chnryk_CHZ_TLP')

        def upon_12():
            if (not 
            Unknown2033(3, 'AssistAttack3')):
                if (not 
                Unknown2033(3, 'AssistAttack3')):
                    Unknown19(23)
    sprite('tnn403_01', 1)
    Unknown2036(4, 100)
    Unknown94(-500000)
    Unknown240()
    Unknown454(4)
    Unknown2055(1)
    Unknown251(1)
    Unknown1975(40000)
    Unknown1698(5)
    Unknown448('cmn_Warp', 103)
    sprite('tnn403_02', 2)
    sprite('tnn403_03', 4)
    sprite('tnn403_04', 2)
    sprite('tnn403_05', 3)
    Unknown1700(4)
    ActivateEffScript('403_Eff', 100)
    sprite('tnn403_06', 2)
    beginRecovery()
    Unknown251(0)
    Unknown268(0)
    sprite('tnn403_07', 2)
    Unknown1700(0)
    sprite('tnn403_08', 3)
    Unknown2230(100)
    Unknown135()
    sprite('tnn403_09', 3)
    sprite('tnn403_10', 3)
    sprite('tnn403_11', 3)

@State
def tnn_sisin_hit():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown457(0)
        Unknown456(0)
        Unknown450('cmn_hit_l')
        Unknown1801(1)
        ActivateEffScript('tnn_sisin_hit2', 100)
    sprite('null', 60)

@State
def tnn_sisin_hit2():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown457(0)
        Unknown454(22)
        Unknown456(0)
        Unknown450('cmn_hit_l')
        Unknown1801(1)
        Unknown239()
        Unknown94(100000)
    sprite('null', 60)

@State
def groundSmoke():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown289(300)
        Unknown94(150000)
    label('loop')
    sprite('null', 10)
    Unknown448('bg_undersmoke00', 100)
    Unknown3()
    labelEnd('loop')

@State
def Dodonpa_shadow():

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
def Dodonpa_Tame():

    def upon_IMMEDIATE():

        def upon_3():
            if Unknown2033(3, 'CmnActMikiwameMove'):
                Unknown19(23)
        Unknown458(2)
        Unknown450('tnn405_tame')

        def upon_12():
            Unknown2036(2, 0)
            if (not SLOT_263):
                Unknown94(50000)
    sprite('null', 17)
    Unknown615('ARC_BTL_TNN_Dodonpa_Chrg')

@State
def Dodonpa_Core():

    def upon_IMMEDIATE():
        Unknown456(3)
        Unknown454(3)
        Unknown289(300)
        Unknown450('tnn405_Beam_core00')
        Unknown632('000000004152435f42544c5f544e4e5f446f646f6e70615f46697265000000000000000064000000')
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
        Unknown35('2f000000656e640000000000000000000000000000000000000000000000000000000000')

        def upon_35():
            Unknown454(0)
            Unknown456(0)
            Unknown295(1)

        def upon_24():
            Unknown23(24)
            storeValue(2, 45, 0, 0)
            Unknown1803('Dodonpa_Atk', 29)
            if Unknown2033(3, 'Dodonpa'):
                Unknown53(3, 2, 45, 23, 0, 0)
                Unknown1798(3, 25)
            if Unknown2033(3, 'AirDodonpa'):
                Unknown53(3, 2, 45, 23, 0, 0)
                Unknown1798(3, 25)
            if Unknown2033(3, 'AssistAttack'):
                Unknown53(3, 2, 45, 23, 0, 0)
            storeValue(2, 47, 0, 1)
            storeValue(2, 51, 0, 1)

            def upon_24():
                Unknown54('00000000020000002f0000000000000001000000')
                if (SLOT_47 >= 4):
                    if Unknown2033(3, 'Dodonpa'):
                        Unknown1798(3, 24)
                    if Unknown2033(3, 'AirDodonpa'):
                        Unknown1798(3, 24)
                    if Unknown2033(3, 'AssistAttack'):
                        Unknown1798(3, 24)
                else:
                    if Unknown2033(3, 'Dodonpa'):
                        Unknown1798(3, 25)
                    if Unknown2033(3, 'AirDodonpa'):
                        Unknown1798(3, 25)

        def upon_3():
            if (not SLOT_46):
                Unknown1804('446f646f6e70615f41746b00000000000000000000000000000000000000000017000000')
    label('loop')
    sprite('null', 2)
    Unknown54('0000000002000000300000000000000001000000')
    Unknown2279('02000000300000000200000033000000')
    Unknown445('446f646f6e70615f41746b00000000000000000000000000000000000000000064000000')
    if (SLOT_45 >= 3):
        Unknown53(1, 2, 45, 23, 0, 1)
    sprite('null', 2)
    Unknown3()
    Unknown54('00000000020000002d0000000000000001000000')
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000002d0000000000000005000000')
    label('end')
    sprite('null', 1)
    Unknown23(23)
    Unknown23(24)
    Unknown23(47)
    Unknown23(3)
    storeValue(2, 49, 0, 1)
    ActivateEffScript('Dodonpa_Atk', 100)
    Unknown1803('Dodonpa_Atk', 30)
    if Unknown2033(3, 'Dodonpa'):
        Unknown1798(3, 24)
    if Unknown2033(3, 'AirDodonpa'):
        Unknown1798(3, 24)
    if Unknown2033(3, 'AssistAttack'):
        Unknown1798(3, 24)
    Unknown454(0)
    Unknown456(0)
    Unknown294(1)
    sprite('null', 1)
    Unknown32('Dodonpa_Atk')
    sprite('null', 13)
    Unknown450('tnn405_Beam_core01')
    sprite('null', 35)
    Unknown633(0, 35)

@State
def Dodonpa_Atk():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkLevel_3_AtkInit')
        callSubroutine('cmnSpecialShot_AtkInit')
        damage1(900)
        callSubroutine('cmn_AssistShotHosei')
        Unknown882(27)
        Unknown894(27)
        airHitPushbackX(1000)
        airHitPushbackY(35000)
        Unknown842(0)
        Unknown830(25)
        Unknown1027(50000000, -490000, 0, 0)
        if Unknown2033(3, 'AssistAttack'):
            damage1(800)
            Unknown830(35)
        Unknown716(1)
        Unknown733(1)
        Unknown734(1)
        Unknown1118('ARC_BTL_CMN_Hit_Beam')
        Unknown1119('ARC_BTL_CMN_Guard_Beam')
        Unknown717('ShakeYoko', 600, 1, 25, 5)

        def upon_30():
            beginRecovery()
            if conditionalunk2500(12, 2, 2, 47, 0, 4):
                beginRecovery()
        Unknown456(2)
        Unknown454(2)
        Unknown457(2)
        Unknown453(2)
        Unknown289(60)
        Unknown1954(1)
        Unknown58(1)
        Unknown450('tnn405_Beam_naka00')

        def upon_23():
            Unknown23(23)
            ActivateEffScript('Dodonpa_End', 100)
            storeValue(2, 46, 0, 1)
            Unknown53(2, 2, 46, 23, 0, 1)

        def upon_37():
            Unknown23(8)
            Unknown53(2, 2, 115, 23, 2, 115)
            Unknown19(23)
            Unknown1798(2, 24)

        def upon_29():
            storeValue(2, 45, 0, 0)

        def upon_90():
            if SLOT_116:
                if Unknown2033(3, 'Dodonpa'):
                    Unknown53(3, 2, 45, 23, 0, 0)
                if Unknown2033(3, 'AirDodonpa'):
                    Unknown53(3, 2, 45, 23, 0, 0)

        def upon_8():
            Unknown53(2, 2, 115, 23, 2, 115)
            ActivateEffScript('cmn_kidan_end_M', 101)
            Unknown612('ARC_BTL_CMN_KidanLast_Expl')
            Unknown1798(2, 23)
            if Unknown2033(3, 'Dodonpa'):
                Unknown53(3, 2, 46, 23, 0, 1)
            if Unknown2033(3, 'AirDodonpa'):
                Unknown53(3, 2, 46, 23, 0, 1)

        def upon_3():
            if conditionalunk2499(2, 2, 49):
                Unknown53(23, 2, 0, 2, 2, 115)
                if (SLOT_115 <= SLOT_0):
                    storeValue(2, 47, 0, 1)
                    Unknown19(23)
            if (SLOT_18 <= 400000):
                Unknown670('02000000e80300000000000000000000')

        def upon_1():
            if SLOT_46:
                storeValue(2, 46, 0, 0)
                Unknown53(2, 2, 46, 23, 0, 0)
            if (not SLOT_47):
                Unknown2274(0, 1000)
                Unknown2276(0, 0)
                Unknown449('tnn405_Beam_naka01', 100)
    sprite('dodonpa0', 1)
    makeActive()
    Unknown202(100000, 0)
    label('loop')
    sprite('dodonpa0', 1)
    Unknown734(0)
    sprite('dodonpa0', 2)
    Unknown2301(1200)
    sprite('dodonpa0', 1)
    Unknown2301(1000)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def Dodonpa_End():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown457(2)
        Unknown289(60)
        Unknown2036(2, 0)
        Unknown2488('02000000190100000200000019010000')
        Unknown58(1)
        Unknown450('tnn405_Beam_end00')

        def upon_3():
            if Unknown51(2):
                Unknown2488('02000000190100000200000019010000')
                Unknown2036(2, 0)

        def upon_1():
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('tnn405_Beam_end01', 100)
    label('loop')
    sprite('null', 2)
    Unknown2301(1000)
    sprite('null', 2)
    Unknown2301(1200)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def __404Eff():

    def upon_IMMEDIATE():
        Unknown450('tnn404_wind01')
        Unknown454(2)
        Unknown457(2)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 100)
    Unknown3()
    Unknown18()
    label('end')
    sprite('null', 30)
    Unknown23(23)
    Unknown454(0)
    Unknown450('tnn404_wind02')
    Unknown3()

@State
def __404_Line_Eff():

    def upon_IMMEDIATE():
        Unknown450('tnn404_Line01')
        Unknown454(2)
        Unknown457(2)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 100)
    Unknown3()
    Unknown18()
    label('end')
    sprite('null', 30)
    Unknown23(23)
    Unknown454(0)
    Unknown450('tnn404_Line02')
    Unknown3()

@Subroutine
def czn_start():
    Unknown451('637a6e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown2189(0, 4)
    Unknown1731(-100000)
    Unknown1629(1)
    Unknown268(1)
    Unknown267(1)
    Unknown287(1)
    Unknown1058(1)
    Unknown2225(1)
    Unknown2211(1)
    Unknown2217(1)

    def upon_45():
        Unknown23(45)
        Unknown268(0)
        Unknown14('czn_koware')

    def upon_56():
        if Unknown2033(32, 'CmnActFuttobiFinish'):
            Unknown23(45)
            Unknown23(23)
            Unknown19(23)
            Unknown2193(103, 0, 150000)
            Unknown448('cmn_Warp', 130)
            Unknown615('ARC_BTL_TNN_Chnryk_CHZ_TLP')
            Unknown451('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@Subroutine
def czn_end():
    Unknown451('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown2193(103, 0, 150000)
    Unknown448('cmn_Warp', 130)
    Unknown615('ARC_BTL_TNN_Chnryk_CHZ_TLP')
    Unknown2315(5)
    Unknown176(1)

@State
def S_Chaozu():

    def upon_IMMEDIATE():
        callSubroutine('czn_start')
        Unknown289(300)
        if Unknown2033(3, 'AssistAttack2'):
            storeValue(2, 47, 0, 1)

            def upon_85():
                Unknown23(85)
                Unknown2208(23)

        def upon_23():
            Unknown23(23)
            Unknown23(24)
            Unknown23(25)
            Unknown451('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown2193(103, 0, 150000)
            Unknown448('cmn_Warp', 130)
            Unknown2208(23)

        def upon_24():
            Unknown2266('637a6e3430375f30360000000000000000000000000000000000000000000000')

            def upon_12():
                if (not 
                Unknown2031('20000000637a6e5f63686f756e6f7572796f6b7500000000000000000000000000000000')):
                    Unknown23(12)
                    Unknown14('atk_end')
            Unknown23(24)
            Unknown14('atk_loop')
        Unknown35('1900000073746f7000000000000000000000000000000000000000000000000000000000')
        if SLOT_115:
            Unknown178(32)
            Unknown94(150000)
            Unknown99(250000)
            Unknown239()
        else:
            Unknown178(2)
            Unknown94(-100000)
            Unknown53(23, 2, 18, 32, 2, 18)
            if conditionalunk2500(9, 32, 2, 31, 0, 1):
                Unknown99(300000)
            elif conditionalunk2500(9, 32, 2, 18, 0, 400000):
                Unknown99(150000)
    sprite('czn407_00', 1)
    Unknown2193(103, 0, 150000)
    Unknown448('cmn_Warp', 130)
    Unknown615('ARC_BTL_TNN_Chnryk_CHZ_TLP')
    Unknown2055(0)
    sprite('czn407_00', 1)
    Unknown2055(1)
    Unknown240()
    Unknown268(0)
    Unknown267(0)
    sprite('czn407_01', 3)
    Unknown1697(501)
    Unknown1700(0)
    physicsImpulseY(2000)
    sprite('czn407_02', 3)
    sprite('czn407_03', 3)
    sprite('czn407_02', 3)
    sprite('czn407_03', 3)
    sprite('czn407_02', 3)
    sprite('czn407_03', 1)
    sprite('czn407_03', 2)
    if SLOT_47:
        if (not SLOT_115):
            ActivateEffScript('czn_chounouryoku', 132)
    sprite('czn407_02', 3)
    sprite('czn407_03', 3)
    Unknown606(1)
    Unknown618('76637a6e3030340000000000000000006400000076637a6e3030360000000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('czn407_04', 2)
    Unknown176(1)
    sprite('czn407_05', 3)
    Unknown1700(4)
    if (not SLOT_47):
        ActivateEffScript('czn_chounouryoku', 132)
    ActivateEffScript('czn_Aura_Eff', 100)
    physicsImpulseX(-4000)
    Unknown2229(90)
    physicsImpulseY(2000)
    Unknown2230(90)
    Unknown3()
    labelEnd('atk_end')
    label('atk_loop')
    sprite('czn407_06', 2)
    sprite('czn407_07', 2)
    sprite('czn407_08', 2)
    Unknown3()
    Unknown54('00000000020000002e0000000000000001000000')
    Unknown13('61746b5f6c6f6f700000000000000000000000000000000000000000000000000d000000020000002e0000000000000005000000')
    label('atk_end')
    sprite('czn407_06', 4)
    Unknown23(24)
    Unknown23(25)
    Unknown23(12)
    sprite('czn407_07', 4)
    sprite('czn407_08', 4)
    Unknown32('czn_Aura_Eff')
    sprite('czn407_06', 4)
    sprite('czn407_07', 4)
    sprite('czn407_08', 4)
    callSubroutine('czn_end')
    Unknown18()
    label('stop')
    sprite('czn407_09', 4)
    Unknown1697(500)
    Unknown23(24)
    Unknown23(25)
    Unknown23(12)
    Unknown176(1)
    Unknown2077('ShakeTate', 300, 5, 20, 5)
    Unknown32('czn_chounouryoku')
    Unknown32('czn_Aura_Eff')
    sprite('czn407_10', 4)
    sprite('czn407_11', 4)
    sprite('czn407_12', 4)
    sprite('czn407_10', 4)
    sprite('czn407_11', 4)
    sprite('czn407_12', 4)
    Unknown606(1)
    Unknown618('76637a6e3030370000000000000000006400000076637a6e3030380000000000000000006400000076637a6e303039000000000000000000640000000000000000000000000000000000000000000000')
    sprite('czn407_10', 4)
    sprite('czn407_11', 4)
    sprite('czn407_12', 4)
    callSubroutine('czn_end')
    Unknown18()
    label('czn_koware')
    sprite('keep', 1)
    Unknown32('czn_Aura_Eff')
    Unknown1803('czn_chounouryoku', 23)
    callSubroutine('czn_end')

@State
def czn_chounouryoku():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkLevel_1_AtkInit')
        callSubroutine('cmnSpecialShot_AtkInit')
        Unknown1028(1)
        damage1(0)
        Unknown818(20)
        Unknown830(20)
        Unknown995(9)
        Unknown996(20, 30, 30)
        Unknown1103(0)
        Unknown1073(1)
        Unknown1079(1)
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
        Unknown717('ShakeTate', 600, 0, 20, 0)
        Unknown287(1)
        if Unknown2033(3, 'AssistAttack2'):
            callSubroutine('cmn_AssistHosei')
            Unknown996(20, 31, 31)
            storeValue(2, 47, 0, 1)

            def upon_85():
                Unknown23(85)
                Unknown2208(23)
        Unknown1118('dammy')
        Unknown1119('ARC_BTL_CMN_Guard_Beam')
        Unknown2211(1)
        Unknown2217(1)
        Unknown2212(1)
        Unknown2213(1)
        Unknown35('2d000000656e640000000000000000000000000000000000000000000000000000000000')

        def upon_90():
            Unknown23(90)
            Unknown1798(2, 24)
            Unknown615('ARC_BTL_TNN_Chnryk_CHZ_Hit')
    Unknown615('ARC_BTL_TNN_Chnryk_CHZ_Fire')
    goto('atk', 2, 214)
    setupLoop('atk', 2, 47)
    sprite('null', 10)
    Unknown450('')
    label('atk')
    sprite('czn_Satk', 3)
    Unknown450('tnn407_chounou')
    makeActive()
    label('end')
    sprite('null', 50)
    beginRecovery()
    Unknown23(45)
    Unknown23(90)

@State
def czn_Aura_Eff():

    def upon_IMMEDIATE():
        Unknown450('tnn407_Aura01')
        Unknown454(2)
        Unknown457(2)
    sprite('null', 240)
    Unknown99(155000)
    Unknown3()

@State
def U_Chaozu():

    def upon_IMMEDIATE():
        Unknown245()
        callSubroutine('czn_start')
        callSubroutine('cmnAtkLevel_1_AtkInit')
        callSubroutine('cmnUltimateShot_AtkInit')
        callSubroutine('cmnAtkTemplNageLand')
        Unknown1019(0)
        Unknown1027(250000, 0, 450000, -200000)
        Unknown1051(3)
        Unknown736(1)
        Unknown1040(0)
        Unknown1056(1)
        Unknown1079(1)
        Unknown717('ShakeYoko', 600, 0, 20, 10)
        damage1(610)
        Unknown1086(100)
        Unknown289(800)
        Unknown294(1)
        Unknown35('1800000061746b0000000000000000000000000000000000000000000000000000000000')

        def upon_47():
            Unknown23(47)
            storeValue(2, 49, 0, 1)

        def upon_71():
            Unknown23(71)
            storeValue(2, 49, 0, 1)
            Unknown2208(23)

        def upon_90():
            if (not SLOT_49):
                Unknown23(3)
                Unknown23(45)
                Unknown23(24)
                Unknown23(90)
                callSubroutine('cmnUltimate_CameraCombo')
                Unknown996(0, 100, 100)
                Unknown882(16)
                Unknown894(16)
                Unknown1094(1)
                Unknown1149(11)
                Unknown298(1)
                Unknown305()
                Unknown306()
                Unknown299()
                Unknown176(1)
                Unknown1064('555f4368616f7a755f6578706c6f73696f6e0000000000000000000000000000')
                if Unknown2033(3, 'SayonaraTensan'):
                    Unknown1803('SayonaraTensan', 25)
                if Unknown47('gtl'):
                    Unknown1149(7)
                if Unknown47('cen'):
                    Unknown1149(8)
                if Unknown47('ton'):
                    Unknown1149(8)
                if Unknown47('toa'):
                    Unknown1149(8)
                if Unknown47('toz'):
                    Unknown1149(8)
                Unknown14('hit')

        def upon_3():
            if SLOT_46:
                if (SLOT_114 >= 1):
                    if SLOT_32:
                        if (SLOT_306 <= (-500000)):
                            Unknown268(0)
                            Unknown267(0)
                            Unknown287(0)
                            if Unknown2033(3, 'SayonaraTensan'):
                                Unknown23(3)
                                Unknown1803('SayonaraTensan', 26)
                                beginRecovery()
                                Unknown14('czn_koware')
                    elif (SLOT_305 >= 500000):
                        Unknown268(0)
                        Unknown267(0)
                        Unknown287(0)
                        if Unknown2033(3, 'SayonaraTensan'):
                            Unknown23(3)
                            Unknown1803('SayonaraTensan', 26)
                            beginRecovery()
                            Unknown14('czn_koware')
            if (not SLOT_16):
                beginRecovery()
    sprite('czn432_00', 1)
    Unknown2189(2, 5)
    Unknown1697(501)
    Unknown239()
    Unknown268(0)
    Unknown267(0)
    Unknown287(0)
    Unknown178(32)
    Unknown94(-500000)
    ActivateEffScript('chaoz_enter', 103)
    Unknown606(1)
    Unknown618('76637a6e3031300000000000000000006400000076637a6e3031310000000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label('loop')
    sprite('czn432_00', 2)
    sprite('czn432_01', 2)
    sprite('czn432_02', 2)
    Unknown3()
    Unknown54('00000000020000002d0000000000000001000000')
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000002d0000000000000014000000')
    labelEnd('czn_koware')
    Unknown18()
    label('atk')
    sprite('czn432_00', 2)
    Unknown32('chaoz_enter')
    physicsImpulseX(25000)
    Unknown2229(110)
    sprite('czn432_01', 2)
    sprite('czn432_02', 2)
    if (not SLOT_46):

        def upon_36():
            if SLOT_32:
                if (SLOT_306 <= 160000):
                    Unknown23(36)
                    makeActive()
                if (SLOT_305 <= 100000):
                    Unknown23(36)
                    beginRecovery()
            else:
                if (SLOT_305 >= (-160000)):
                    Unknown23(36)
                    makeActive()
                if (SLOT_306 >= (-100000)):
                    Unknown23(36)
                    beginRecovery()
    sprite('czn432_00', 2)
    sprite('czn432_01', 2)
    sprite('czn432_02', 2)
    Unknown3()
    Unknown268(1)
    Unknown267(1)
    Unknown287(1)
    Unknown54('00000000020000002e0000000000000001000000')
    Unknown13('61746b00000000000000000000000000000000000000000000000000000000000d000000020000002e0000000000000032000000')
    labelEnd('czn_koware')
    Unknown18()
    label('hit')
    sprite('czn432_03', 6)
    Unknown23(36)
    Unknown1697(11)
    Unknown1700(4)
    Unknown267(0)
    Unknown35('190000006578706c6f73696f6e0000000000000000000000000000000000000000000000')
    if conditionalunk2500(13, 3, 2, 21, 0, 1200000):
        if conditionalunk2500(13, 3, 2, 104, 0, 1200000):
            Unknown454(25)
            Unknown41(25)
            Unknown94(1200001)
            Unknown40()
    if conditionalunk2500(12, 25, 2, 18, 0, 300000):
        storeValue(2, 50, 0, 1)
        Unknown454(25)
        Unknown41(25)
        Unknown98(800000)
        Unknown40()
    Unknown1911()
    Unknown2189(2, 4)
    Unknown2250('19000000000000001700000000000000')
    Unknown1732(100000)
    if Unknown47('gtl'):
        storeValue(2, 51, 0, 1)
        Unknown1732(45000)
    if Unknown47('ton'):
        Unknown1732(22000)
    if Unknown47('toa'):
        Unknown1732(22000)
    if Unknown47('toz'):
        Unknown1732(22000)
    label('hit_loop')
    sprite('czn432_04', 4)
    Unknown450('tnn_jibaku_charge')
    sprite('czn432_05', 4)
    if SLOT_51:
        if (SLOT_47 == 1):
            if SLOT_50:
                Unknown1736(-2333)
                physicsImpulseY(-3333)
                physicsImpulseX(1333)
            else:
                Unknown1736(-833)
    sprite('czn432_06', 4)
    Unknown1984(0)
    Unknown1990(0)
    Unknown1996(0)
    Unknown1987(5)
    Unknown1993(20)
    Unknown1999(25)
    sprite('czn432_04', 4)
    sprite('czn432_05', 4)
    sprite('czn432_06', 4)
    if SLOT_51:
        if (SLOT_47 == 1):
            Unknown1736(0)
            physicsImpulseY(0)
            physicsImpulseX(0)
    sprite('czn432_04', 4)
    sprite('czn432_05', 4)
    sprite('czn432_06', 4)
    Unknown3()
    Unknown54('00000000020000002f0000000000000001000000')
    Unknown13('6869745f6c6f6f700000000000000000000000000000000000000000000000000d000000020000002f0000000000000032000000')
    labelEnd('czn_koware')
    Unknown18()
    label('explosion')
    sprite('czn432_04', 4)
    Unknown23(25)
    sprite('czn432_05', 4)
    sprite('czn432_06', 4)
    sprite('czn432_04', 4)
    ActivateEffScript('U_Chaozu_explosion', 100)
    Unknown2055(0)
    Unknown18()
    label('czn_koware')
    sprite('keep', 1)
    callSubroutine('czn_end')
    Unknown23(36)
    beginRecovery()

@State
def chaoz_enter():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown294(1)
    sprite('explosion', 60)
    Unknown450('tnn_chaoz_enter')

@State
def U_Chaozu_explosion():

    def upon_IMMEDIATE():
        Unknown245()
        callSubroutine('cmnAtkLevel_4_AtkInit')
        callSubroutine('cmnUltimateShot_AtkInit')
        damage1(3031)
        Unknown1086(66)
        Unknown1095(500)
        Unknown995(0)
        Unknown882(9)
        Unknown894(9)
        airHitPushbackX(0)
        airHitPushbackY(0)
        Unknown778(0)
        grHitPushbackX(0)
        Unknown830(500)
        Unknown1187(0)
        Unknown1079(1)
        Unknown1051(1)
        Unknown1018(1)
        Unknown294(1)
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
        Unknown2077('ShakeTateYoko', 2000, 0, 35, 10)
        Unknown1118('dammy')
        storeValue(2, 4, 0, 1)

        def upon_23():
            Unknown23(23)
            Unknown178(3)
            Unknown94(800000)
            Unknown99(300000)
            Unknown14('end_atk')

        def upon_24():
            Unknown23(24)
            Unknown14('end_atk2')

        def upon_90():
            Unknown23(90)
            if Unknown2033(3, 'SayonaraTensan'):
                Unknown41(32)
                Unknown2055(0)
                Unknown40()

                def upon_1():
                    Unknown41(32)
                    Unknown2055(1)
                    Unknown40()
    sprite('explosion', 30)
    Unknown615('ARC_BTL_TNN_Sayonara_Expl')
    Unknown450('cmn_bomb_s2')
    Unknown2136('000000000000000000000000e803000000000000640000001e000000')
    Unknown477('00000000000000000000000010270000')
    if (SLOT_18 <= 400000):
        Unknown670('01000000e80300000000000000000000')
    makeActive()
    sprite('null', 600)
    Unknown18()
    label('end_atk')
    sprite('explosion', 3)
    damage1(0)
    Unknown995(0)
    Unknown1067(4, 1, 1)
    Unknown1142(1)
    Unknown1075(1)
    Unknown1157(1)
    makeActive()
    sprite('null', 600)
    Unknown41(32)
    Unknown2055(1)
    Unknown40()
    Unknown18()
    label('end_atk2')
    sprite('explosion', 3)
    damage1(0)
    Unknown995(0)
    Unknown1067(0, 0, 0)
    Unknown882(8)
    Unknown894(8)
    airHitPushbackX(6000)
    airHitPushbackY(-60000)
    Unknown778(4000)
    Unknown830(30)
    Unknown1142(1)
    Unknown1075(1)
    Unknown1157(1)
    Unknown1064('436d6e4e65757472616c00000000000000000000000000000000000000000000')
    makeActive()

@State
def Kikouho_shot():

    def upon_IMMEDIATE():
        Unknown245()
        callSubroutine('cmnAtkLevel_4_AtkInit')
        callSubroutine('cmnUltimateShot_AtkInit')
        damage1(2400)
        Unknown1086(43)
        Unknown882(11)
        Unknown894(11)
        airHitPushbackX(20000)
        airHitPushbackY(-80000)
        Unknown830(33)
        Unknown996(0, 5, 5)
        Unknown842(0)
        Unknown854(1)
        Unknown806(30000)
        Unknown802(100)
        Unknown1079(1)
        Unknown1051(0)
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
        Unknown717('ShakeTate', 2000, 0, 30, 10)
        Unknown1118('ARC_BTL_CMN_Hit_Large-A')
        Unknown1119('ARC_BTL_CMN_Guard_Beam')
        Unknown99(300000)
        Unknown289(60)
        if conditionalunk2500(13, 3, 2, 18, 0, 400000):
            ActivateEffScript('tnn_430_Hole', 123)
            Unknown41(1)
            Unknown94(450000)
            Unknown40()
        elif conditionalunk2500(13, 3, 2, 18, 0, 600000):
            ActivateEffScript('tnn_430_Hole', 123)
            Unknown41(1)
            Unknown94(600000)
            Unknown40()
        elif conditionalunk2500(13, 3, 2, 18, 0, 800000):
            ActivateEffScript('tnn_430_Hole', 123)
            Unknown41(1)
            Unknown94(800000)
            Unknown40()
        elif conditionalunk2500(13, 3, 2, 18, 0, 1000000):
            ActivateEffScript('tnn_430_Hole', 123)
            Unknown41(1)
            Unknown94(1000000)
            Unknown40()
        elif conditionalunk2500(10, 3, 2, 18, 0, 1000001):
            ActivateEffScript('tnn_430_Hole', 123)
            Unknown41(1)
            Unknown94(1200000)
            Unknown40()
        Unknown670('01000000b80b00000000000000000000')

        def upon_90():
            Unknown23(90)
            callSubroutine('cmnUltimate_CameraCombo')
    sprite('kikouho', 3)
    Unknown615('ARC_BTL_TNN_Kikouho_Fire')
    Unknown2136('000000000000000000000000e803000000000000aa0000001e000000')
    makeActive()

@Subroutine
def Kikouhou_S_Init():
    Unknown2493('544e4e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown456(3)
    Unknown289(65)
    Unknown249(155000)
    Unknown250(260000)
    Unknown1975(-70000)
    Unknown251(0)
    Unknown1698(5)
    ActivateEffScript('430_Aura_Eff', 100)

    def upon_3():
        onFrame(0, 10)
        Unknown251(1)
        Unknown255(1)
        endIf()
        onFrame(0, 25)
        Unknown251(0)
        Unknown255(0)
        endIf()
        if conditionalunk2499(3, 2, 263):
            Unknown19(23)

    def upon_1():
        Unknown448('cmn_Warp', 114)
        ActivateEffScript('430_AuraEnd_Eff_S', 100)
    Unknown457(3)

@State
def Kikouho_S1():

    def upon_IMMEDIATE():
        callSubroutine('Kikouhou_S_Init')
    sprite('tnn430_22', 4)
    physicsImpulseX(60000)
    physicsImpulseY(20000)
    sprite('tnn430_23', 4)
    Unknown176(1)
    sprite('tnn430_24', 4)
    sprite('tnn430_21', 4)
    sprite('tnn430_22', 4)
    sprite('tnn430_23', 4)
    sprite('tnn430_24', 4)
    sprite('tnn430_25', 3)
    Unknown1698(6)
    Unknown2279('00000000000000000000000001000000')
    Unknown445('4b696b6f75686f5f535f73686f7400000000000000000000000000000000000064000000')
    ActivateEffScript('430_Beam_S_Eff', 100)
    ActivateEffScript('430_Mazzle_S_Eff', 100)
    ActivateEffScript('cmn_bigSmokeEff', 100)
    physicsImpulseX(-35000)
    Unknown2229(80)
    physicsImpulseY(45000)
    Unknown2230(80)
    sprite('tnn430_26', 3)
    sprite('tnn430_27', 3)
    sprite('tnn430_28', 3)
    sprite('tnn430_29', 3)
    sprite('tnn430_30', 3)
    sprite('tnn430_26', 3)
    sprite('tnn430_27', 3)
    sprite('tnn430_28', 3)
    sprite('tnn430_29', 3)
    sprite('tnn430_30', 3)
    sprite('tnn430_26', 3)
    sprite('tnn430_27', 3)
    sprite('tnn430_28', 3)
    sprite('tnn430_29', 3)
    sprite('tnn430_30', 3)

@State
def Kikouho_S2():

    def upon_IMMEDIATE():
        callSubroutine('Kikouhou_S_Init')
    sprite('tnn430_22', 4)
    physicsImpulseX(60000)
    physicsImpulseY(20000)
    sprite('tnn430_23', 4)
    sprite('tnn430_24', 4)
    Unknown176(1)
    sprite('tnn430_21', 4)
    sprite('tnn430_22', 4)
    sprite('tnn430_23', 4)
    sprite('tnn430_24', 4)
    sprite('tnn430_25', 3)
    Unknown1698(6)
    callSubroutine('tnn_430_Hole_Create')
    ActivateEffScript('430_Beam_S_Eff', 100)
    ActivateEffScript('430_Mazzle_S_Eff', 100)
    ActivateEffScript('cmn_bigSmokeEff', 100)
    physicsImpulseX(-35000)
    Unknown2229(80)
    physicsImpulseY(45000)
    Unknown2230(80)
    sprite('tnn430_26', 3)
    sprite('tnn430_27', 3)
    sprite('tnn430_28', 3)
    sprite('tnn430_29', 3)
    sprite('tnn430_30', 3)
    sprite('tnn430_26', 3)
    sprite('tnn430_27', 3)
    sprite('tnn430_28', 3)
    sprite('tnn430_29', 3)
    sprite('tnn430_30', 3)
    sprite('tnn430_26', 3)
    sprite('tnn430_27', 3)
    sprite('tnn430_28', 3)
    sprite('tnn430_29', 3)
    sprite('tnn430_30', 3)

@State
def Kikouho_S3():

    def upon_IMMEDIATE():
        callSubroutine('Kikouhou_S_Init')
    sprite('tnn430_22', 4)
    physicsImpulseX(60000)
    physicsImpulseY(20000)
    sprite('tnn430_23', 4)
    sprite('tnn430_24', 4)
    sprite('tnn430_21', 4)
    Unknown176(1)
    sprite('tnn430_22', 4)
    sprite('tnn430_23', 4)
    sprite('tnn430_24', 4)
    sprite('tnn430_21', 4)
    sprite('tnn430_22', 4)
    sprite('tnn430_23', 4)
    sprite('tnn430_24', 1)
    sprite('tnn430_25', 3)
    Unknown1698(6)
    callSubroutine('tnn_430_Hole_Create')
    ActivateEffScript('430_Beam_S_Eff', 100)
    ActivateEffScript('430_Mazzle_S_Eff', 100)
    ActivateEffScript('cmn_bigSmokeEff', 100)
    physicsImpulseX(-35000)
    Unknown2229(80)
    physicsImpulseY(45000)
    Unknown2230(80)
    sprite('tnn430_26', 3)
    sprite('tnn430_27', 3)
    sprite('tnn430_28', 3)
    sprite('tnn430_29', 3)
    sprite('tnn430_30', 3)
    sprite('tnn430_26', 3)
    sprite('tnn430_27', 3)
    sprite('tnn430_28', 3)
    sprite('tnn430_29', 3)
    sprite('tnn430_30', 3)

@State
def Kikouho_S1_C():

    def upon_IMMEDIATE():
        callSubroutine('Kikouhou_S_Init')
    sprite('tnn430_22', 4)
    physicsImpulseX(-25000)
    physicsImpulseY(-10000)
    sprite('tnn430_23', 4)
    sprite('tnn430_24', 2)
    sprite('tnn430_24', 2)
    Unknown176(1)
    sprite('tnn430_21', 4)
    sprite('tnn430_22', 4)
    sprite('tnn430_23', 4)
    sprite('tnn430_24', 4)
    sprite('tnn430_25', 3)
    Unknown1698(6)
    Unknown2279('00000000010000000000000001000000')
    Unknown445('4b696b6f75686f5f535f73686f7400000000000000000000000000000000000064000000')
    ActivateEffScript('430_Beam_S_Eff', 100)
    ActivateEffScript('430_Mazzle_S_Eff', 100)
    ActivateEffScript('cmn_bigSmokeEff', 100)
    physicsImpulseX(-35000)
    Unknown2229(80)
    physicsImpulseY(45000)
    Unknown2230(80)
    sprite('tnn430_26', 3)
    sprite('tnn430_27', 3)
    sprite('tnn430_28', 3)
    sprite('tnn430_29', 3)
    sprite('tnn430_30', 3)
    sprite('tnn430_26', 3)
    sprite('tnn430_27', 3)
    sprite('tnn430_28', 3)
    sprite('tnn430_29', 3)
    sprite('tnn430_30', 3)
    sprite('tnn430_26', 3)
    sprite('tnn430_27', 3)
    sprite('tnn430_28', 3)
    sprite('tnn430_29', 3)
    sprite('tnn430_30', 3)

@State
def Kikouho_S2_C():

    def upon_IMMEDIATE():
        callSubroutine('Kikouhou_S_Init')
    sprite('tnn430_22', 2)
    Unknown239()
    physicsImpulseX(-50000)
    sprite('tnn430_22', 2)
    physicsImpulseX(-100000)
    sprite('tnn430_23', 2)
    sprite('tnn430_23', 2)
    Unknown176(1)
    sprite('tnn430_24', 2)
    sprite('tnn430_24', 2)
    sprite('tnn430_21', 4)
    sprite('tnn430_22', 4)
    sprite('tnn430_23', 4)
    sprite('tnn430_24', 4)
    sprite('tnn430_25', 3)
    Unknown1698(6)
    callSubroutine('tnn_430_Hole_Create')
    ActivateEffScript('430_Beam_S_Eff', 100)
    ActivateEffScript('430_Mazzle_S_Eff', 100)
    ActivateEffScript('cmn_bigSmokeEff', 100)
    physicsImpulseX(-35000)
    Unknown2229(80)
    physicsImpulseY(45000)
    Unknown2230(80)
    sprite('tnn430_26', 3)
    sprite('tnn430_27', 3)
    sprite('tnn430_28', 3)
    sprite('tnn430_29', 3)
    sprite('tnn430_30', 3)
    sprite('tnn430_26', 3)
    sprite('tnn430_27', 3)
    sprite('tnn430_28', 3)
    sprite('tnn430_29', 3)
    sprite('tnn430_30', 3)
    sprite('tnn430_26', 3)
    sprite('tnn430_27', 3)
    sprite('tnn430_28', 3)
    sprite('tnn430_29', 3)
    sprite('tnn430_30', 3)

@State
def Kikouho_S3_C():

    def upon_IMMEDIATE():
        callSubroutine('Kikouhou_S_Init')
    sprite('tnn430_22', 2)
    Unknown239()
    physicsImpulseX(-50000)
    sprite('tnn430_22', 2)
    physicsImpulseX(-100000)
    sprite('tnn430_23', 2)
    sprite('tnn430_23', 2)
    physicsImpulseX(-50000)
    physicsImpulseY(-20000)
    sprite('tnn430_24', 3)
    sprite('tnn430_24', 1)
    Unknown176(1)
    sprite('tnn430_21', 4)
    sprite('tnn430_22', 4)
    sprite('tnn430_23', 4)
    sprite('tnn430_24', 4)
    sprite('tnn430_21', 4)
    sprite('tnn430_22', 4)
    sprite('tnn430_23', 4)
    sprite('tnn430_24', 1)
    sprite('tnn430_25', 3)
    Unknown1698(6)
    callSubroutine('tnn_430_Hole_Create')
    ActivateEffScript('430_Beam_S_Eff', 100)
    ActivateEffScript('430_Mazzle_S_Eff', 100)
    ActivateEffScript('cmn_bigSmokeEff', 100)
    physicsImpulseX(-35000)
    Unknown2229(80)
    physicsImpulseY(45000)
    Unknown2230(80)
    sprite('tnn430_26', 3)
    sprite('tnn430_27', 3)
    sprite('tnn430_28', 3)
    sprite('tnn430_29', 3)
    sprite('tnn430_30', 3)
    sprite('tnn430_26', 3)
    sprite('tnn430_27', 3)
    sprite('tnn430_28', 3)
    sprite('tnn430_29', 3)
    sprite('tnn430_30', 3)

@Subroutine
def tnn_430_Hole_Create():
    if conditionalunk2500(13, 2, 2, 18, 0, 400000):
        ActivateEffScript('tnn_430_Hole', 123)
        Unknown41(1)
        Unknown94(450000)
        Unknown40()
    elif conditionalunk2500(13, 2, 2, 18, 0, 600000):
        ActivateEffScript('tnn_430_Hole', 123)
        Unknown41(1)
        Unknown94(600000)
        Unknown40()
    elif conditionalunk2500(13, 2, 2, 18, 0, 800000):
        ActivateEffScript('tnn_430_Hole', 123)
        Unknown41(1)
        Unknown94(800000)
        Unknown40()
    elif conditionalunk2500(13, 2, 2, 18, 0, 1000000):
        ActivateEffScript('tnn_430_Hole', 123)
        Unknown41(1)
        Unknown94(1000000)
        Unknown40()
    elif conditionalunk2500(10, 2, 2, 18, 0, 1000001):
        ActivateEffScript('tnn_430_Hole', 123)
        Unknown41(1)
        Unknown94(1200000)
        Unknown40()

@State
def tnn_430_Hole():

    def upon_IMMEDIATE():
        Unknown450('tnn_430_Hole')
        Unknown477('00000000000000000000000010270000')
        Unknown670('01000000b80b00000000000000000000')
    sprite('null', 60)

@State
def Kikouho_S_shot():

    def upon_IMMEDIATE():
        Unknown245()
        callSubroutine('cmnAtkLevel_4_AtkInit')
        callSubroutine('cmnUltimateShot_AtkInit')
        damage1(1699)
        Unknown1086(42)
        Unknown882(11)
        Unknown894(11)
        airHitPushbackX(20000)
        airHitPushbackY(-80000)
        Unknown830(33)
        Unknown995(0)
        Unknown996(5, 10, 10)
        Unknown1191(1)
        Unknown842(0)
        Unknown854(1)
        Unknown806(25000)
        Unknown802(100)
        Unknown1079(1)
        Unknown1051(0)
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
        Unknown717('ShakeTate', 2000, 0, 30, 10)
        if SLOT_116:
            Unknown882(12)
            Unknown894(12)
            airHitPushbackX(20000)
            airHitPushbackY(40000)
            Unknown854(0)
            Unknown830(40)
            Unknown996(5, 3, 3)
        if SLOT_115:
            Unknown1094(1)
            airHitPushbackX(0)
            if SLOT_116:
                Unknown882(11)
                Unknown894(11)
                airHitPushbackY(-80000)
                Unknown854(1)
                Unknown830(35)
                Unknown996(5, 8, 8)
        Unknown1118('ARC_BTL_CMN_Hit_Large-A')
        Unknown1119('ARC_BTL_CMN_Guard_Beam')
        Unknown99(300000)
        Unknown289(60)
        callSubroutine('tnn_430_Hole_Create')

        def upon_90():
            Unknown23(90)
            callSubroutine('cmnUltimate_CameraCombo')
        Unknown42('17000000090000000300000009000000')
        if Unknown51(9):
            Unknown2196('09000000640000000000000000000000')
            if SLOT_115:
                Unknown2279('00000000010000000000000000000000')
                Unknown445('4b696b6f75686f5f535f4566660000000000000000000000000000000000000082000000')
            else:
                Unknown445('4b696b6f75686f5f535f4566660000000000000000000000000000000000000082000000')
            Unknown467(1)
    sprite('kikouho', 3)
    Unknown615('ARC_BTL_TNN_Kikouho_Fire')
    Unknown2136('000000000000000000000000e803000000000000aa0000001e000000')
    makeActive()

@State
def Kikouho_S_Eff():

    def upon_IMMEDIATE():
        if SLOT_115:
            Unknown239()
        Unknown99(300000)
        Unknown289(60)
    sprite('kikouho', 3)

@State
def __430_Tame_Eff():

    def upon_IMMEDIATE():
        Unknown450('tnn430_tame')
        Unknown454(2)
        Unknown457(2)
        Unknown294(1)
        Unknown92(15000)
        Unknown98(270000)
    sprite('null', 25)
    Unknown92(20000)
    sprite('null', 5)
    Unknown92(36000)
    Unknown3()

@State
def __430_TameSpark_Eff():

    def upon_IMMEDIATE():
        Unknown450('tnn430_tame_hand')
        Unknown454(2)
        Unknown457(2)
        Unknown294(1)
        Unknown92(120000)
        Unknown98(280000)
        Unknown1731(150000)
    sprite('null', 30)
    Unknown615('ARC_BTL_TNN_Kikouho_Chrg')
    Unknown3()

@State
def __430_TameSpark2_Eff():

    def upon_IMMEDIATE():
        Unknown450('tnn430_tame_hand')
        Unknown454(2)
        Unknown457(2)
        Unknown294(1)
        Unknown92(120000)
        Unknown98(280000)
        Unknown1731(250000)
    sprite('null', 30)
    Unknown3()

@State
def __430_Mazzle_Eff():

    def upon_IMMEDIATE():
        Unknown450('tnn430_Mazzle')
        Unknown454(2)
        Unknown457(2)
        Unknown99(300000)
        Unknown94(27000)
    sprite('null', 60)
    Unknown3()

@State
def __430_Mazzle_S_Eff():

    def upon_IMMEDIATE():
        Unknown450('tnn430_Mazzle2')
        Unknown454(2)
        Unknown457(2)
        Unknown99(300000)
        Unknown94(27000)
    sprite('null', 60)
    Unknown3()

@State
def __430_Beam_Eff():

    def upon_IMMEDIATE():
        Unknown450('tnn430_burst')
        Unknown454(2)
        Unknown457(2)
        Unknown99(300000)
        Unknown164(38000)
    sprite('null', 60)
    Unknown3()

@State
def __430_Beam_S_Eff():

    def upon_IMMEDIATE():
        Unknown450('tnn430_burst2')
        Unknown454(2)
        Unknown457(2)
        Unknown99(300000)
        Unknown164(38000)
    sprite('null', 60)
    Unknown3()

@State
def __430_Aura_Eff():

    def upon_IMMEDIATE():
        Unknown450('tnn430_Aura')
        Unknown454(2)
        Unknown457(2)
        Unknown294(1)
        Unknown99(200000)
        Unknown164(-30000)
    sprite('null', 240)
    Unknown3()

@State
def __430_AuraEnd_Eff():

    def upon_IMMEDIATE():
        Unknown450('tnn430_AuraEnd')
        Unknown454(2)
        Unknown457(2)
        Unknown294(1)
        Unknown99(200000)
    sprite('null', 60)
    Unknown3()

@State
def __430_AuraEnd_Eff_S():

    def upon_IMMEDIATE():
        Unknown450('tnn430_AuraEnd')
        Unknown295(1)
        Unknown99(200000)
    sprite('null', 60)

@State
def Sinkikouho_shot():

    def upon_IMMEDIATE():
        Unknown245()
        callSubroutine('cmnAtkLevel_4_AtkInit')
        callSubroutine('cmnUltimateShot_AtkInit')
        damage1(3600)
        Unknown1203(30)
        Unknown1086(52)
        Unknown1095(500)
        Unknown1143(1)
        Unknown995(0)
        Unknown996(30, 23, 23)
        Unknown882(11)
        Unknown894(11)
        airHitPushbackX(30000)
        airHitPushbackY(-150000)
        Unknown830(100)
        Unknown778(0)
        Unknown1067(3, 0, 10)
        Unknown842(0)
        Unknown806(35000)
        Unknown808(10000)
        Unknown854(1)
        Unknown802(100)
        Unknown941(25)
        Unknown810(8000)
        Unknown1187(0)
        Unknown1079(1)
        Unknown736(1)
        Unknown1051(2)
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
        Unknown1064('53696e6b696b6f75686f5f73686f740000000000000000000000000000000000')
        Unknown1118('ARC_BTL_CMN_Hit_Large-A')
        Unknown1119('ARC_BTL_CMN_Guard_Beam')
        Unknown289(60)
        Unknown94(-300000)
        ActivateEffScript('shinkikou_Beam_Eff', 100)
        if (SLOT_115 >= 2):
            damage1(1000)
            Unknown1086(60)

        def upon_47():
            Unknown23(47)
            storeValue(2, 46, 0, 1)

        def upon_90():
            Unknown23(90)
            callSubroutine('cmnUltimate_CameraCombo')
            if (not SLOT_46):
                if Unknown2033(3, 'Sinkikouho'):
                    Unknown2040(3, 'Sinkikouho_Hit', 0)
                if Unknown2033(3, 'AirSinkikouho'):
                    Unknown2040(3, 'Sinkikouho_Hit', 0)
        Unknown2193(123, 400000, 0)
        Unknown2273(0, 800)
        Unknown449('bg_groundsmokeL', 130)
        Unknown2193(123, -400000, 0)
        Unknown2277(1)
        Unknown2273(0, 1200)
        Unknown449('bg_groundsmokeL', 130)
        Unknown670('01000000204e00000000000000000000')
        Unknown477('00000000000000000000000030750000')
    sprite('shinkikouho', 3)
    Unknown615('ARC_BTL_TNN_ShinKikh_Fire')
    Unknown2136('000000000000000000000000e803000000000000640000001e000000')
    makeActive()

@State
def shinkikou_Beam_Eff():

    def upon_IMMEDIATE():
        Unknown456(2)
    sprite('null', 45)
    Unknown450('tnn431_burst')
    Unknown164(35000)
    Unknown94(350000)

@State
def Enemy_Position():

    def upon_IMMEDIATE():

        def upon_3():
            Unknown178(32)
        Unknown457(3)
        Unknown2519(1)
    sprite('null', 1000)

@State
def Tnn_hijump_obj():
    sprite('null', 15)
    Unknown450('cmn_hijump')
    Unknown454(2)
    Unknown456(2)
    Unknown458(2)
    Unknown2519(1)
    Unknown156(3000)

@State
def __431_shot_Eff():

    def upon_IMMEDIATE():
        Unknown450('tnn431_shot')
        Unknown454(2)
        Unknown457(2)
        Unknown294(1)
        Unknown99(360000)
        Unknown94(50000)
        Unknown164(-30000)
    sprite('null', 240)
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
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    Unknown2076('a0c7fcff70530100169e0000bb1100004a3200000000000048000000000000005a0000001e00000001000000')
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
    Unknown2076('5af0feffa96305008ad300001a0d0000830b00000000000036000000000000005a0000001e00000001000000')
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def FinishCamera_Toss():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 60)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    Unknown2076('19e4fdff62350700949c0000a70a0000920b00000000000036000000000000005a0000001e00000001000000')
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def FinishCamera_Attack():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 60)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    Unknown2076('e0c9ffffb5360500b889020046f9ffff5b0900000000000036000000000000005a0000001e00000001000000')
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def FinishCamera_SayonaraTensan():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 3)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2077('ShakeTate', 2000, 3, 50, 10)
    Unknown2079('0e000000604bfbffe85807005dde0200c0f9ffff75180000000000003600000000000000b400000000000000000000000000000000000000')
    sprite('null', 3)
    Unknown2079('0e000000c39dfbff92e00600d0c70200c0f9ffff75180000000000003600000001000000b400000000000000000000000000000000000000')
    sprite('null', 3)
    Unknown2079('0e000000604bfbffe85807005dde0200c0f9ffff75180000000000003600000001000000b400000000000000000000000000000000000000')
    sprite('null', 3)
    Unknown2079('0e000000c39dfbff92e00600d0c70200c0f9ffff75180000000000003600000001000000b400000000000000000000000000000000000000')
    sprite('null', 3)
    Unknown2079('0e000000604bfbffe85807005dde0200c0f9ffff75180000000000003600000001000000b400000000000000000000000000000000000000')
    sprite('null', 3)
    Unknown2079('0e000000c39dfbff92e00600d0c70200c0f9ffff75180000000000003600000001000000b400000000000000000000000000000000000000')
    sprite('null', 42)
    Unknown2079('0e0000004f2afcff4a13060031a10200c0f9ffff75180000000000003600000001000000b400000000000000000000000000000000000000')
    sprite('null', 30)
    Unknown32('cmn_syutyusen')
    Unknown3()

@State
def FinishCamera_Kikouho():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 60)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2077('ShakeTate', 1500, 3, 50, 10)
    Unknown2079('20000000857dfcffa79d0600cd22030006f7ffff7c1500000000000036000000000000006400000014000000000000000200000001000000')
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def FinishCamera_Sinkikouho():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 60)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2077('ShakeTate', 2000, 3, 60, 10)
    Unknown2079('20000000857dfcffa79d0600cd22030006f7ffff7c1500000000000036000000000000006400000014000000000000000200000001000000')
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def DUMMYDUMMY():
    sprite('null', 1)