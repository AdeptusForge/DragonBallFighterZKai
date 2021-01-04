@State
def dmy():
    sprite('null', 1)

@State
def okasi():

    def upon_IMMEDIATE():
        callSubroutine('cmn_okasi')
    sprite('null', 2147483647)
    Unknown450('frn_okasi')

@State
def frn_kidan_end():

    def upon_IMMEDIATE():
        Unknown450('cmn_bomb_s3')
        Unknown295(1)
        Unknown1801(1)
    sprite('null', 7)
    Unknown615('ARC_BTL_FRN_DThsTm_Expl')
    Unknown2136('000000000000000000000000f4010000000000003c0000001e000000')
    sprite('null', 51)
    Unknown1801(0)

@State
def frn_reversalkidan():

    def upon_IMMEDIATE():
        Unknown476('66726e5f726576657273616c5f6b6964616e0000000000000000000000000000')
        Unknown176(1)
    sprite('null', 2147483647)
    ActivateEffScript('cmn_reversal_mazzle', 100)

@State
def __5A3rd_shot():

    def upon_IMMEDIATE():
        Unknown243()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        callSubroutine('cmnNormalShot_AtkInit')
        damage1(0)
        Unknown1079(1)
        or_standhit(8)
        or_launchhit(8)
        Unknown1059(1)
        mod_hitstop(5)
        Unknown1118('dammyName')
        Unknown1119('ARC_BTL_CMN_Guard_Kidan')
        Unknown1954(1)
        Unknown98(200000)
        Unknown450('frn404_EnemyAura')

        def upon_87():
            Unknown23(87)
            ActivateEffScript('cmn_reversal_mazzle', 101)
            Unknown19(23)

        def upon_47():
            Unknown23(47)
            Unknown295(1)
            beginRecovery()
            storeValue(2, 46, 0, 1)

        def upon_89():
            Unknown23(89)
            if SLOT_16:
                if SLOT_263:
                    if (not SLOT_46):
                        if Unknown2033(3, 'NmlAtk5A3rd'):
                            damage1(0)
                            Unknown1095(0)
                            Unknown1059(1)
                            Unknown2040(3, 'NmlAtk5A3rd_Hit', 0)
                            Unknown615('ARC_BTL_FRN_DThsTm_Catch')

        def upon_8():
            storeValue(2, 52, 0, 1)
            if SLOT_275:
                damage1(0)
                Unknown1095(0)
            else:
                damage1(400)
                Unknown1095(500)

        def upon_3():
            if SLOT_52:
                Unknown54('0000000002000000340000000000000001000000')
            if (SLOT_52 > 5):
                storeValue(2, 52, 0, 0)
                if Unknown2033(3, 'NmlAtk5A3rd'):
                    Unknown53(3, 2, 52, 3, 0, 1)
    sprite('5a3rd', 3)
    makeActive()
    sprite('null', 20)
    beginRecovery()

@State
def frn202_mazzle():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown450('frn237_mazzle')
        Unknown1731(150000)
    sprite('null', 60)

@State
def frn202_EnemyAura():

    def upon_IMMEDIATE():
        Unknown454(22)
        Unknown457(2)
        Unknown450('frn404_EnemyAura')
        Unknown289(300)
    sprite('null', 2147483647)

@State
def __5A3rd_exe_shot():

    def upon_IMMEDIATE():
        Unknown178(22)
        Unknown295(1)
        Unknown1801(1)
        Unknown99(150000)
        Unknown188(850)
    sprite('null', 20)
    Unknown615('ARC_BTL_FRN_DThsTm_Expl')
    Unknown450('cmn_bomb_s2')
    sprite('null', 40)
    Unknown1801(0)

@Subroutine
def iwa_init():
    Unknown243()
    callSubroutine('cmnAtkLevel_3_AtkInit')
    callSubroutine('cmnNormalShot_AtkInit')
    Unknown1121(1)
    damage1(100)
    Unknown1117(100)
    Unknown1143(0)
    mod_hitstop(3)
    untech_Override(30)
    Unknown1023(11)
    airHitPushbackX(40000)
    airHitPushbackY(10000)
    Unknown1051(0)
    Unknown1058(1)
    Unknown1112(0)
    Unknown1152(1)
    Unknown1045('04000000636d6e5f6869745f730000000000000000000000000000000000000000000000')
    Unknown1183(1)
    if Unknown2033(3, 'AssistAttack3'):
        storeValue(2, 47, 0, 1)
        damage1(60)
        or_standhit(11)
        or_launchhit(11)
        Unknown790(0)
        mod_opphitstop(0, 13, 13)
        airHitPushbackX(100000)
        airHitPushbackY(21000)
        untech_Override(60)
        Unknown1128(1)
        callSubroutine('cmn_AssistHosei')

        def upon_90():
            Unknown23(90)
            if Unknown2033(3, 'AssistAttack3'):
                Unknown53(3, 2, 51, 23, 0, 1)
    Unknown1118('ARC_BTL_CMN_Hit_Midle-A')
    Unknown1954(1)
    Unknown2292(1)
    Unknown58(1)
    Unknown450('bg_frn204rock')
    Unknown454(2)
    ActivateEffScript('5C_rock_dust', 100)
    ActivateEffScript('5C_rock_aura', 100)

    def upon_3():
        if Unknown2033(3, 'NmlAtk5C'):
            Unknown53(23, 2, 45, 2, 2, 45)
            if SLOT_45:
                or_launchhit(11)
                Unknown790(0)
                airHitPushbackX(90000)
                airHitPushbackY(15000)
                untech_Override(60)
        if Unknown2033(3, 'CmnActMikiwameMove'):
            Unknown2208(23)
        if (SLOT_105 == 4):
            Unknown176(1)
            Unknown454(0)
            Unknown2216(0)
        if SLOT_47:
            if (SLOT_105 == 12):
                physicsImpulseX(8000)
                Unknown2229(101)
                Unknown1152(0)
                Unknown2217(0)
        elif (SLOT_105 == 17):
            physicsImpulseX(8000)
            Unknown2229(101)
            Unknown1152(0)
            Unknown2217(0)
        if SLOT_52:
            Unknown54('0000000002000000340000000000000001000000')
        if (SLOT_52 > 3):
            storeValue(2, 52, 0, 0)
            if Unknown2033(2, 'NmlAtk5C'):
                Unknown53(2, 2, 52, 2, 0, 1)
    Unknown2210()
    Unknown2211(1)
    Unknown2215(1)
    Unknown2217(1)
    Unknown2216(1)
    Unknown2223(1)
    Unknown2225(1)

    def upon_45():
        Unknown448('cmn_hit_s', 100)
        Unknown14('Koware')

    def upon_8():
        Unknown14('Koware')
        storeValue(2, 52, 0, 1)

@State
def __5C_first():

    def upon_IMMEDIATE():
        Unknown243()
        callSubroutine('cmnAtkLevel_3_AtkInit')
        Unknown1028(0)
        damage1(150)
        Unknown1117(600)
        Unknown1079(1)
        airHitPushbackX(14000)
        airHitPushbackY(12000)
        mod_hitstop(3)
        mod_opphitstop(0, 11, 11)
        Unknown1023(11)
        grHitPushbackX(20)
        untech_Override(60)
        or_standhit(1)
        Unknown1051(0)
        Unknown1058(1)
        Unknown1183(1)
        Unknown2292(1)
        Unknown1954(1)
        Unknown2209(1)
        Unknown457(2)
        Unknown454(2)
        if Unknown2033(3, 'AssistAttack3'):
            damage1(60)
            Unknown1128(1)
            callSubroutine('cmn_AssistHosei')

            def upon_90():
                Unknown23(90)
                if Unknown2033(3, 'AssistAttack3'):
                    pass
        if SLOT_283:
            storeValue(2, 283, 0, 2)

        def upon_89():
            Unknown23(89)
            if SLOT_16:
                if Unknown53(23, 2, 0, 3, 2, 263):
                    Unknown53(23, 2, 283, 3, 2, 283)
                    if (not SLOT_283):
                        Unknown1067(4, 0, -200000)
                        mod_hitstop(0)
                        mod_opphitstop(0, 0, 0)
                        damage1(300)

                        def upon_95():
                            Unknown23(95)
                            Unknown69(0)
                            Unknown2077('ShakeTateYoko', 1000, 0, 18, 1)
                            Unknown271('00000000640000001900000019000000')
                    Unknown2040(2, 'CameraCombo_5C', 0)
            endIf()
    sprite('5c_first', 4)
    physicsImpulseY(60000)
    sprite('5c_first0', 1)
    makeActive()
    Unknown176(1)
    sprite('5c_first', 4)

@State
def __5C_iwa():

    def upon_IMMEDIATE():
        callSubroutine('iwa_init')
        Unknown188(1400)
        Unknown1731(-150000)
        Unknown670('01000000e80300000000000000000000')
    sprite('5c', 4)
    physicsImpulseY(50000)
    makeActive()
    sprite('5c', 13)
    Unknown26(8, 2, 47)
    sprite('5c', 2)
    sprite('5c', 7)
    sprite('5c', 600)
    physicsImpulseX(60000)
    label('Koware')
    sprite('null', 5)
    Unknown176(1)
    Unknown294(1)
    Unknown450('')

@State
def __5C_iwa1():

    def upon_IMMEDIATE():
        callSubroutine('iwa_init')
        Unknown1731(150000)
    sprite('5c', 4)
    physicsImpulseY(90000)
    makeActive()
    sprite('5c', 13)
    Unknown26(8, 2, 47)
    sprite('5c', 2)
    sprite('5c', 6)
    sprite('5c', 600)
    physicsImpulseX(55000)
    physicsImpulseY(3000)
    label('Koware')
    sprite('null', 5)
    Unknown176(1)
    Unknown294(1)
    Unknown450('')

@State
def __5C_iwa2():

    def upon_IMMEDIATE():
        callSubroutine('iwa_init')
        Unknown188(1200)
        Unknown1731(150000)
    sprite('5c', 4)
    physicsImpulseY(30000)
    makeActive()
    sprite('5c', 13)
    Unknown26(8, 2, 47)
    sprite('5c', 2)
    sprite('5c', 5)
    sprite('5c', 600)
    physicsImpulseX(55000)
    physicsImpulseY(-3000)
    label('Koware')
    sprite('null', 5)
    Unknown176(1)
    Unknown294(1)
    Unknown450('')

@State
def __5C_iwa3():

    def upon_IMMEDIATE():
        callSubroutine('iwa_init')
        Unknown188(1500)
    sprite('5c', 4)
    physicsImpulseY(70000)
    makeActive()
    sprite('5c', 13)
    Unknown26(8, 2, 47)
    sprite('5c', 2)
    sprite('5c', 4)
    sprite('5c', 600)
    physicsImpulseX(55000)
    physicsImpulseY(1000)
    label('Koware')
    sprite('null', 5)
    Unknown176(1)
    Unknown294(1)
    Unknown450('')

@State
def __5C_iwa4():

    def upon_IMMEDIATE():
        callSubroutine('iwa_init')
        Unknown188(1300)
        Unknown1731(-100000)
    sprite('5c', 4)
    physicsImpulseY(100000)
    makeActive()
    sprite('5c', 13)
    Unknown26(8, 2, 47)
    sprite('5c', 2)
    sprite('5c', 3)
    sprite('5c', 600)
    physicsImpulseX(43000)
    physicsImpulseY(4000)
    label('Koware')
    sprite('null', 5)
    Unknown176(1)
    Unknown294(1)
    Unknown450('')

@State
def __5C_iwa5():

    def upon_IMMEDIATE():
        callSubroutine('iwa_init')
        Unknown188(1500)
        Unknown1731(-130000)
    sprite('5c', 4)
    physicsImpulseY(40000)
    makeActive()
    sprite('5c', 13)
    Unknown26(8, 2, 47)
    sprite('5c', 2)
    sprite('5c', 2)
    sprite('5c', 600)
    physicsImpulseX(45000)
    physicsImpulseY(-5000)
    label('Koware')
    sprite('null', 5)
    Unknown176(1)
    Unknown294(1)
    Unknown450('')

@State
def __5C_iwa6():

    def upon_IMMEDIATE():
        callSubroutine('iwa_init')
        Unknown188(1200)
    sprite('5c', 4)
    physicsImpulseY(90000)
    makeActive()
    sprite('5c', 13)
    Unknown26(8, 2, 47)
    sprite('5c', 2)
    sprite('5c', 1)
    sprite('5c', 600)
    physicsImpulseX(45000)
    physicsImpulseY(4000)
    label('Koware')
    sprite('null', 5)
    Unknown176(1)
    Unknown294(1)
    Unknown450('')

@State
def __5C_iwa7():

    def upon_IMMEDIATE():
        callSubroutine('iwa_init')
        Unknown1731(130000)
    sprite('5c', 4)
    physicsImpulseY(50000)
    makeActive()
    sprite('5c', 13)
    Unknown26(8, 2, 47)
    sprite('5c', 2)
    sprite('5c', 600)
    physicsImpulseX(45000)
    physicsImpulseY(-1000)
    Unknown2229(102)
    label('Koware')
    sprite('null', 5)
    Unknown176(1)
    Unknown294(1)
    Unknown450('')

@State
def __5C_rock_dust():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown460(2)
        Unknown450('bg_frn204dust')
    sprite('null', 20)

@State
def __5C_rock_aura():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('frn204_rockaura')
        Unknown460(2)
    sprite('null', 2147483647)

@State
def __5C_smoke():

    def upon_IMMEDIATE():
        Unknown94(206000)
    sprite('null', 1)
    Unknown448('bg_frn204smoke', 100)

@State
def __2C_shot():

    def upon_IMMEDIATE():
        Unknown243()
        callSubroutine('cmnAtkLevel_4_AtkInit')
        Unknown1121(3)
        Unknown1028(1)
        damage1(850)
        Unknown1183(1)
        or_standhit(1)
        airHitPushbackY(70000)
        Unknown1108(90)
        Unknown1112(0)
        Unknown1966(1)
        Unknown1954(1)
        Unknown1099(1)
        Unknown457(3)
        Unknown670('01000000e80300000000000000000000')
        if SLOT_283:
            storeValue(2, 283, 0, 2)

        def upon_89():
            Unknown23(89)
            if SLOT_16:
                if Unknown53(23, 2, 0, 2, 2, 263):
                    Unknown53(23, 2, 283, 2, 2, 283)
                    if (not SLOT_283):
                        mod_hitstop(0)
                        damage1(1000)
                        untech_Override(40)

                        def upon_95():
                            Unknown23(95)
                            Unknown69(0)
                            Unknown271('00000000640000001900000019000000')
                            Unknown2077('ShakeTateYoko', 1000, 0, 18, 1)
                    Unknown2040(2, 'CameraCombo_2C', 0)
                    Unknown1803('frn232_Eff', 23)
            endIf()
    sprite('2c', 3)
    makeActive()
    ActivateEffScript('frn232_Eff', 100)
    Unknown2136('000000000000000000000000f4010000000000003c0000001e000000')

@State
def frn232_Eff():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown450('bg_frn232_smoke')
        Unknown1801(1)
        Unknown295(1)

        def upon_23():
            storeValue(2, 45, 0, 1)
    sprite('null', 10)
    Unknown632('000000004152435f42544c5f46524e5f447452747a6e5f4669726541420000000000000064000000')
    sprite('null', 20)
    if SLOT_45:
        Unknown295(0)
    Unknown1801(0)
    sprite('null', 30)
    Unknown633(0, 30)

@State
def frn232_BodyAuraEff():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('frn232_bodyaura')
    sprite('null', 17)
    sprite('null', 30)
    Unknown450('frn232_bodyaura_end')
    Unknown457(0)
    Unknown295(1)
    Unknown1801(1)

@State
def frn232_HandAuraEff():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('frn232_handaura')
        Unknown99(170000)
        Unknown94(50000)
        Unknown1732(150000)
        Unknown35('17000000456e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)
    Unknown188(250)
    sprite('null', 2)
    Unknown188(500)
    sprite('null', 2)
    Unknown188(750)
    sprite('null', 2)
    Unknown188(1000)
    sprite('null', 2147483647)
    label('End')
    sprite('null', 20)
    Unknown99(170000)
    Unknown450('frn232_handaura_end')

@State
def frn_hajiki():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 30)
    Unknown450('frn_hajiki')

@State
def __5D_shot():

    def upon_IMMEDIATE():
        Unknown243()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        callSubroutine('cmn5DKidan_AtkInit')
        callSubroutine('cmnKidan_Init')
        Unknown99(10000)
        Unknown1731(150000)
        Unknown2229(102)
        damage1(300)
        airHitPushbackY(6000)
        Unknown2221(0)
        Unknown2212(0)
        Unknown2213(0)
        Unknown2214(0)
        Unknown1202('4152435f42544c5f434d4e5f4869745f4d69646c652d41000000000000000000')
        Unknown1119('')
        Unknown1119('ARC_BTL_CMN_Guard_Beam')

        def upon_8():
            storeValue(2, 52, 0, 1)

        def upon_87():
            Unknown23(87)
            Unknown450('')
            ActivateEffScript('frn_reversalkidan', 100)
            storeValue(2, 52, 0, 1)
            Unknown2208(23)

        def upon_49():
            if Unknown2041('5D_shot'):
                Unknown23(49)
                Unknown23(3)
                Unknown23(8)
        if Unknown2033(3, 'NmlAtk5D'):
            if (not 
            Unknown53(23, 2, 0, 3, 2, 45)):
                or_standhit(1)
                Unknown842(1)
                Unknown790(40)
                Unknown937(3)
                untech_Override(22)
                airHitPushbackX(35000)
                airHitPushbackY(20000)
    sprite('kidan', 1)
    makeActive()
    sprite('kidan', 600)
    Unknown58(1)
    Unknown202(90000, 0)
    Unknown450('frn_beam')
    label('Koware')
    sprite('null', 10)
    Unknown176(1)
    Unknown450('')

@State
def __5D_beam_start0():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('frn_beam_start')
    sprite('null', 3)
    Unknown612('ARC_BTL_CMN_kidan_Chrg')
    Unknown188(100)
    Unknown191(200)
    Unknown1731(100000)
    sprite('null', 3)
    Unknown188(400)
    Unknown191(-100)

@State
def __5D_beam_start():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('frn_beam_start')
    sprite('null', 6)
    Unknown612('ARC_BTL_CMN_kidan_Chrg')
    Unknown188(100)
    Unknown191(100)
    Unknown1731(100000)
    sprite('null', 3)
    Unknown188(400)
    Unknown191(-100)

@State
def frn_beam_mazzle():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('frn_beam_mazzle')
        Unknown1731(100000)
    sprite('null', 60)

@State
def frn233_core():

    def upon_IMMEDIATE():
        Unknown453(2)
        Unknown1731(50000)
        Unknown2210()
        Unknown2211(1)
        Unknown2216(1)
        Unknown35('2d000000656e640000000000000000000000000000000000000000000000000000000000')
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 600)
    Unknown450('frn233_core00')
    label('end')
    sprite('null', 20)
    Unknown23(45)
    Unknown23(23)
    Unknown294(1)
    Unknown450('frn233_core01')

@State
def frn233_beam():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown453(2)
        Unknown1731(50000)
        Unknown58(1)
    sprite('null', 1)
    sprite('null', 600)
    Unknown450('frn_beam')

@State
def __1D_shot():

    def upon_IMMEDIATE():
        Unknown243()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        callSubroutine('cmn2DKidan_AtkInit')
        callSubroutine('cmnKidan_Init')
        damage1(700)
        airHitPushbackY(36000)
        Unknown164(10000)
        Unknown202(90000, 0)
        Unknown2229(102)
        Unknown2230(102)
        Unknown2221(0)
        Unknown2212(0)
        Unknown2213(0)
        Unknown2214(0)

        def upon_8():
            storeValue(2, 52, 0, 1)

        def upon_87():
            Unknown23(87)
            Unknown450('')
            ActivateEffScript('frn_reversalkidan', 100)
            storeValue(2, 52, 0, 1)
            Unknown2208(23)

        def upon_3():
            if SLOT_52:
                Unknown54('0000000002000000340000000000000001000000')
            if (SLOT_52 > 5):
                storeValue(2, 52, 0, 0)
                if Unknown2033(3, 'NmlAtk1D'):
                    Unknown53(3, 2, 52, 3, 0, 1)
    sprite('kidan_nanameue', 600)
    makeActive()
    Unknown2193(100, -10000, 0)
    ActivateEffScript('frn233_core', 130)
    ActivateEffScript('frn233_beam', 130)
    Unknown2193(100, 10000, 0)
    ActivateEffScript('frn233_core', 130)
    ActivateEffScript('frn233_beam', 130)
    label('Koware')
    sprite('null', 10)
    Unknown176(1)
    Unknown450('')

@State
def __2D_shot():

    def upon_IMMEDIATE():
        Unknown243()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        callSubroutine('cmn2DKidan_AtkInit')
        callSubroutine('cmnKidan_Init')
        damage1(700)
        airHitPushbackY(36000)
        Unknown164(30000)
        Unknown202(90000, 0)
        Unknown2229(102)
        Unknown2230(102)
        Unknown2221(0)
        Unknown2212(0)
        Unknown2213(0)
        Unknown2214(0)

        def upon_8():
            storeValue(2, 52, 0, 1)

        def upon_87():
            Unknown23(87)
            Unknown450('')
            ActivateEffScript('frn_reversalkidan', 100)
            storeValue(2, 52, 0, 1)
            Unknown2208(23)
    sprite('kidan_nanameue', 600)
    makeActive()
    Unknown2193(100, -10000, 0)
    ActivateEffScript('frn233_core', 130)
    ActivateEffScript('frn233_beam', 130)
    Unknown2193(100, 10000, 0)
    ActivateEffScript('frn233_core', 130)
    ActivateEffScript('frn233_beam', 130)
    label('Koware')
    sprite('null', 10)
    Unknown176(1)
    Unknown450('')

@State
def __3D_shot():

    def upon_IMMEDIATE():
        Unknown243()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        callSubroutine('cmn2DKidan_AtkInit')
        callSubroutine('cmnKidan_Init')
        damage1(700)
        airHitPushbackY(36000)
        Unknown164(70000)
        Unknown202(90000, 0)
        Unknown2229(102)
        Unknown2230(102)
        Unknown2221(0)
        Unknown2212(0)
        Unknown2213(0)
        Unknown2214(0)

        def upon_8():
            storeValue(2, 52, 0, 1)

        def upon_87():
            Unknown23(87)
            Unknown450('')
            ActivateEffScript('frn_reversalkidan', 100)
            storeValue(2, 52, 0, 1)
            Unknown2208(23)

        def upon_3():
            if SLOT_52:
                Unknown54('0000000002000000340000000000000001000000')
            if (SLOT_52 > 5):
                storeValue(2, 52, 0, 0)
                if Unknown2033(3, 'NmlAtk3D'):
                    Unknown53(3, 2, 52, 3, 0, 1)
    sprite('kidan_nanameue', 600)
    makeActive()
    Unknown2193(100, -10000, 0)
    ActivateEffScript('frn233_core', 130)
    ActivateEffScript('frn233_beam', 130)
    Unknown2193(100, 10000, 0)
    ActivateEffScript('frn233_core', 130)
    ActivateEffScript('frn233_beam', 130)
    label('Koware')
    sprite('null', 10)
    Unknown176(1)
    Unknown450('')

@State
def Air_5D_blast():

    def upon_IMMEDIATE():
        Unknown243()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        callSubroutine('cmn_AirAtkHosei')
        Unknown1028(2)
        damage1(400)
        Unknown1117(400)
        Unknown1143(1)
        airHitPushbackX(60000)
        or_standhit(1)
        Unknown1051(0)
        mod_hitstop(2)
        mod_opphitstop(0, 10, 10)
        untech_Override(15)
        Unknown1197(1)
        Unknown1112(0)
        Unknown1190(1)
        Unknown1183(1)
        Unknown1966(1)
        Unknown1954(1)
        Unknown2299(1100)
        Unknown454(2)
        Unknown450('frn_blast')
        if Unknown2033(3, 'NmlAtkAir5D'):
            if (not 
            Unknown53(23, 2, 0, 3, 2, 45)):
                mod_hitstop(10)
                mod_opphitstop(0, 0, 0)
                untech_Override(25)
                airHitPushbackX(80000)
                or_standhit(11)
                or_launchhit(11)
                Unknown790(0)

        def upon_87():
            Unknown23(87)
            ActivateEffScript('cmn_reversal_mazzle', 101)

        def upon_47():
            beginRecovery()
            Unknown454(0)
            Unknown295(1)
    sprite('jd', 6)
    Unknown615('ARC_BTL_FRN_Impact')
    makeActive()
    sprite('null', 30)

@State
def Air_2D_mazzle():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown164(-55000)
        Unknown188(700)
    sprite('null', 60)
    Unknown450('frn_blast')

@State
def Air_2D_shot():

    def upon_IMMEDIATE():
        Unknown243()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        callSubroutine('cmnAir5DKidan_AtkInit')
        callSubroutine('cmnKidan_Init')
        damage1(600)
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
        Unknown94(20000)
        Unknown450('frn_kidan')

        def upon_8():
            storeValue(2, 52, 0, 1)
            ActivateEffScript('frn_kidan_end', 100)

        def upon_87():
            Unknown23(87)
            Unknown450('')
            ActivateEffScript('frn_reversalkidan', 100)
            storeValue(2, 52, 0, 1)
            Unknown2208(23)
    sprite('kidan_nanamesita0', 1)
    Unknown2055(0)
    makeActive()
    sprite('kidan_nanamesita', 600)
    Unknown2055(1)
    Unknown164(-55000)
    Unknown2229(102)
    Unknown2230(102)
    Unknown202(70000, 0)
    label('Koware')
    sprite('null', 10)
    Unknown176(1)
    Unknown450('')

@State
def DieThisTime_Shot_1st():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkLevel_3_AtkInit')
        callSubroutine('cmnSpecialShot_AtkInit')
        damage1(300)
        mod_hitstop(10)
        Unknown1117(300)
        or_standhit(1)
        airHitPushbackX(20000)
        airHitPushbackY(5000)
        untech_Override(25)
        Unknown1051(0)
        if Unknown2033(3, 'AssistAttack2'):
            beginRecovery()
            damage1(250)
            untech_Override(30)
            callSubroutine('cmn_AssistHosei')
        Unknown1954(1)
        Unknown268(1)
        Unknown287(1)
        Unknown454(3)
        Unknown289(600)
        Unknown450('frn402_loop')
        Unknown1118('dammyName')
        Unknown1119('ARC_BTL_CMN_Guard_Beam')

        def upon_24():
            storeValue(2, 49, 0, 1)

        def upon_47():
            Unknown23(47)
            storeValue(2, 46, 0, 1)
            Unknown14('shot')

        def upon_89():
            if conditionalunk2498(3, 2, 263):
                Unknown23(89)
                if (not SLOT_265):
                    if (not SLOT_46):
                        damage1(0)
                        Unknown1095(0)
                        Unknown1059(1)
                        Unknown2040(3, 'DieThisTime_1st', 0)
                        Unknown23(93)
                        Unknown23(8)
                        Unknown615('ARC_BTL_FRN_DThsTm_Catch')

        def upon_8():
            if (not SLOT_46):
                Unknown2040(3, 'DieThisTime_Hit', 0)

        def upon_93():
            makeActive()
            damage1(300)
            Unknown54('00000000020000002d0000000000000001000000')
            if (SLOT_45 >= 4):
                Unknown2208(23)
                if (not SLOT_46):
                    if Unknown2033(3, 'DieThisTime'):
                        Unknown1798(3, 23)
                    if Unknown2033(3, 'AirDieThisTime'):
                        Unknown1798(3, 23)
            elif (not SLOT_46):
                if Unknown2033(3, 'DieThisTime'):
                    Unknown1798(3, 25)
                if Unknown2033(3, 'AirDieThisTime'):
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
        Unknown2210()
        Unknown2211(1)
        Unknown2217(1)

        def upon_45():
            ActivateEffScript('eff402_end', 100)
            Unknown615('ARC_BTL_FRN_DThsTm_Expl')
            Unknown633(19, 20)
            Unknown19(23)
        Unknown35('1700000073686f7400000000000000000000000000000000000000000000000000000000')

        def upon_25():
            Unknown23(23)
            Unknown23(25)
            Unknown23(45)
            Unknown23(47)
            Unknown14('end')
    sprite('236d0', 120)
    Unknown632('130000004152435f42544c5f46524e5f44546873546d5f5374617274000000000000000064000000')
    makeActive()
    label('shot')
    sprite('236d', 5)
    Unknown23(23)
    Unknown23(45)
    Unknown23(47)
    beginRecovery()
    ActivateEffScript('DieThisTime_Shot', 100)
    if SLOT_49:
        Unknown1798(1, 24)
    else:
        Unknown2266('3233366430000000000000000000000000000000000000000000000000000000')
    Unknown19(23)
    label('end')
    sprite('236d', 1)
    beginRecovery()

@State
def DieThisTime_Shot():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkLevel_3_AtkInit')
        callSubroutine('cmnSpecialShot_AtkInit')
        damage1(300)
        untech_Override(15)
        mod_hitstop(3)
        Unknown1023(8)
        Unknown1117(300)
        airHitPushbackX(10000)
        airHitPushbackY(1000)
        or_standhit(1)
        Unknown1051(0)
        Unknown717('ShakeYoko', 1000, 1, 15, 10)
        if Unknown2033(3, 'AssistAttack2'):
            damage1(250)
            untech_Override(20)
            mod_opphitstop(0, 6, 6)
            callSubroutine('cmn_AssistHosei')
            storeValue(2, 50, 0, 1)
        Unknown1202('4152435f42544c5f434d4e5f4869745f4265616d000000000000000000000000')
        Unknown1119('ARC_BTL_CMN_Guard_Beam')
        Unknown1954(1)
        Unknown58(1)
        Unknown289(600)

        def upon_24():
            storeValue(2, 49, 0, 1)

        def upon_47():
            Unknown23(47)
            storeValue(2, 46, 0, 1)

        def upon_8():
            if (not SLOT_46):
                Unknown2040(3, 'DieThisTime_Hit', 0)

        def upon_92():
            Unknown111(1)
            Unknown116(1)
            storeValue(2, 48, 0, 1)
            Unknown54('00000000020000002f0000000000000001000000')
            if (SLOT_47 >= 4):
                makeActive()
                airHitPushbackX(20000)
                airHitPushbackY(20000)
                Unknown1202('64616d6d79000000000000000000000000000000000000000000000000000000')
                if Unknown2033(3, 'AssistAttack2'):
                    airHitPushbackX(13000)
                    airHitPushbackY(28000)
                    untech_Override(30)
                Unknown2208(23)

        def upon_93():
            Unknown54('00000000020000002d0000000000000001000000')
            storeValue(2, 48, 0, 3)
            if SLOT_49:
                Unknown94(-100000)
                Unknown99(50000)
                Unknown111(1)
                Unknown116(1)
            else:
                Unknown94(-100000)
                Unknown111(1)
            if (SLOT_45 >= 4):
                Unknown2208(23)

        def upon_3():
            if SLOT_48:
                Unknown54('0000000002000000300000000000000001000000')
                if (SLOT_48 == 5):
                    makeActive()
                    if (SLOT_104 >= 180000):
                        physicsImpulseX(50000)
                        physicsImpulseY(-25000)
                if (SLOT_48 >= 8):
                    storeValue(2, 48, 0, 0)
                    physicsImpulseX(50000)
                    physicsImpulseY(-25000)
            if (SLOT_18 <= 150000):
                physicsImpulseY(0)
                Unknown670('02000000e80300000000000000000000')
        Unknown2210()
        Unknown2211(1)
        Unknown2213(1)

        def upon_45():
            ActivateEffScript('eff402_end', 100)
            Unknown615('ARC_BTL_FRN_DThsTm_Expl')
            Unknown633(19, 20)
            Unknown19(23)

        def upon_98():
            Unknown23(98)
            Unknown2208(23)
    sprite('236d', 1)
    Unknown450('frn402_loop')
    makeActive()
    Unknown1152(1)
    if (not SLOT_49):
        Unknown2266('3233366430000000000000000000000000000000000000000000000000000000')
    sprite('236d', 5)
    Unknown1152(0)
    if (not SLOT_49):
        Unknown2266('3233366430000000000000000000000000000000000000000000000000000000')
    sprite('236d', 3)
    if (not SLOT_48):
        physicsImpulseX(50000)
        physicsImpulseY(-25000)
    Unknown615('ARC_BTL_FRN_DThsTm_Fire')
    Unknown633(19, 20)
    if (not SLOT_49):
        Unknown2266('3233366430000000000000000000000000000000000000000000000000000000')
    label('loop')
    sprite('236d', 4)
    if (SLOT_18 <= 150000):
        Unknown448('bg_undersmoke00', 104)
        Unknown26(6, 2, 50)
    if (not SLOT_49):
        Unknown2266('3233366430000000000000000000000000000000000000000000000000000000')
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d000000000000002c010000')

@State
def DieThisTime_Shot_Lock():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkLevel_3_AtkInit')
        callSubroutine('cmnAtkTemplNageExe')
        callSubroutine('cmnSpecialShot_AtkInit')
        mod_hitstop(3)
        Unknown1117(600)
        airHitPushbackY(25000)
        untech_Override(30)
        Unknown1018(1)
        Unknown1073(1)
        Unknown717('ShakeTate', 2000, 1, 35, 1)
        Unknown1128(0)
        Unknown1118('ARC_BTL_CMN_Hit_Beam')
        Unknown1119('ARC_BTL_CMN_Guard_Beam')
        Unknown1954(1)
        Unknown268(1)
        Unknown287(1)
        Unknown294(1)
        Unknown454(32)
        Unknown450('frn402_loop')
        Unknown32('DieThisTime_Shot_1st')
        if Unknown2033(3, 'AirDieThisTimeExe'):
            storeValue(2, 49, 0, 1)
        if Unknown67(0):
            Unknown188(900)
        if Unknown67(1):
            pass
        if Unknown67(2):
            Unknown188(1300)
        if Unknown67(3):
            Unknown188(1300)
        Unknown35('1700000073686f7400000000000000000000000000000000000000000000000000000000')
        Unknown35('2f000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('236d', 60)
    label('shot')
    sprite('236d', 1)
    Unknown23(23)
    Unknown294(0)
    Unknown615('ARC_BTL_FRN_DThsTm_Fire')
    Unknown633(19, 20)
    sprite('236d', 2)
    Unknown458(32)

    def upon_1():
        ActivateEffScript('eff402_end', 100)
    sprite('236d', 3)

    def upon_6():
        if SLOT_49:
            if SLOT_45:
                Unknown23(6)
                Unknown14('end')
        else:
            Unknown23(6)
            Unknown14('end')

    def upon_3():
        if (not SLOT_263):
            Unknown14('end')
        if (not SLOT_45):
            if SLOT_49:
                if conditionalunk2500(13, 32, 2, 18, 0, 150000):
                    storeValue(2, 45, 0, 1)
                    if conditionalunk2498(32, 2, 24):
                        Unknown41(32)
                        Unknown98(5000)
                        physicsImpulseX(-50000)
                        physicsImpulseY(0)
                        Unknown127(1)
                        Unknown40()
        if (SLOT_18 <= 220000):
            Unknown670('02000000e80300000000000000000000')
    label('loop')
    sprite('236d', 4)
    if (SLOT_18 <= 220000):
        Unknown448('bg_undersmoke00', 104)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000096000000')
    label('end')
    sprite('236d', 5)
    Unknown23(23)
    Unknown23(6)
    Unknown23(47)
    Unknown23(3)
    Unknown23(1)
    Unknown458(0)
    makeActive()
    Unknown450('')
    Unknown176(1)
    ActivateEffScript('eff402_end', 100)
    Unknown615('ARC_BTL_FRN_DThsTm_Expl')
    Unknown1202('64616d6d79000000000000000000000000000000000000000000000000000000')

@State
def eff402_end():

    def upon_IMMEDIATE():
        Unknown450('cmn_bomb_s2')
        Unknown294(1)
        Unknown1801(1)
        if (SLOT_18 <= 400000):
            Unknown670('01000000e80300000000000000000000')
    sprite('null', 20)
    physicsImpulseX(3000)
    physicsImpulseY(1500)
    Unknown2136('000000000000000000000000f4010000000000003c0000001e000000')
    sprite('null', 40)
    Unknown1801(0)

@State
def DeathSaucer_Pre1():

    def upon_IMMEDIATE():
        Unknown454(3)
        Unknown456(3)

        def upon_47():
            Unknown23(47)
            Unknown456(0)
            Unknown454(0)
            Unknown295(1)
            Unknown14('end')
    sprite('214d', 15)
    Unknown450('frn403_start')
    Unknown188(600)
    Unknown164(-25000)
    sprite('214d', 45)
    Unknown450('frn403_loop')
    label('end')
    sprite('null', 15)
    Unknown450('frn403_end')

@State
def DeathSaucer_Pre2():

    def upon_IMMEDIATE():
        Unknown454(3)
        Unknown456(3)

        def upon_47():
            Unknown23(47)
            Unknown456(0)
            Unknown454(0)
            Unknown295(1)
            Unknown14('end')
    sprite('214d', 15)
    Unknown450('frn403_start')
    Unknown188(600)
    Unknown164(25000)
    sprite('214d', 45)
    Unknown188(650)
    Unknown450('frn403_loop')
    label('end')
    sprite('null', 15)
    Unknown450('frn403_end')

@State
def DeathSaucer_Shot():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkLevel_3_AtkInit')
        callSubroutine('cmnSpecialShot_AtkInit')
        damage1(700)
        Unknown1143(1)
        Unknown1095(1000)
        or_standhit(1)
        untech_Override(30)
        mod_hitstop(3)
        mod_opphitstop(0, 12, 12)
        airHitPushbackX(30000)
        airHitPushbackY(15000)
        Unknown1117(600)
        Unknown1203(15)
        Unknown1051(0)
        Unknown1045('04000000636d6e5f736c6173685f73000000000000000000000000000000000000000000')
        Unknown717('ShakeYoko', 600, 5, 20, 5)
        Unknown1118('ARC_BTL_CMN_Hit_FRN_DthScr')
        Unknown1119('ARC_BTL_CMN_Guard_Large')
        Unknown1954(1)
        Unknown1629(1)
        Unknown450('frn403_loop')
        Unknown2210()
        Unknown2211(1)
        Unknown2217(1)

        def upon_45():
            Unknown295(1)
            Unknown14('end')
        physicsImpulseX(50000)
        physicsImpulseY(-5000)

        def upon_23():
            Unknown23(23)
            physicsImpulseX(25000)
            Unknown42('17000000050000000300000005000000')
            storeValue(2, 51, 0, 1)

        def upon_47():
            Unknown23(47)
            storeValue(2, 46, 0, 1)

        def upon_90():
            Unknown23(90)
            damage1(700)

        def upon_93():
            Unknown23(92)
            if (not SLOT_45):
                Unknown109()
                Unknown114()
                storeValue(2, 48, 0, 1)
            storeValue(2, 47, 0, 0)

            def upon_77():
                if (not SLOT_81):
                    Unknown54('00000000020000002f0000000000000001000000')
                    Unknown2315(1)
                    if (SLOT_47 >= 5):
                        Unknown23(77)
                        Unknown176(1)
                        Unknown110()
                        Unknown115()
                        if (SLOT_7 <= 70000):
                            physicsImpulseX(70000)
                        storeValue(2, 48, 0, 0)
            damage1(200)
            physicsImpulseX(30000)
            Unknown94(-50000)
            makeActive()
            Unknown54('00000000020000002d0000000000000001000000')
            if (SLOT_45 >= 2):
                Unknown2208(23)
                if (not SLOT_46):
                    if SLOT_51:
                        if Unknown2033(3, 'DeathSaucer'):
                            Unknown1798(3, 23)
            elif (not SLOT_46):
                if Unknown2033(3, 'DeathSaucer'):
                    Unknown1798(3, 25)

        def upon_3():
            callSubroutine('cmnNotMainPlayer_ObjectDelete')
            if (not SLOT_48):
                Unknown200(0)
            if Unknown51(5):
                Unknown53(23, 2, 49, 5, 2, 21)
                if (SLOT_21 >= SLOT_49):
                    Unknown94(-50000)
            if SLOT_52:
                if (not SLOT_312):
                    Unknown2208(23)
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
    sprite('null', 1)
    Unknown615('ARC_BTL_FRN_DthScr_Fire')
    sprite('214d', 12)
    if (not SLOT_51):
        makeActive()
        storeValue(2, 52, 0, 1)
    sprite('214d', 3)
    if SLOT_51:
        makeActive()
        storeValue(2, 52, 0, 1)
    sprite('214d', 6)
    physicsImpulseX(70000)
    sprite('214d', 1)
    Unknown127(-4000)
    sprite('214d', 19)
    Unknown127(-4000)
    sprite('214d', 10)
    sprite('214d', 5)
    storeValue(2, 48, 0, 1)
    Unknown176(1)
    sprite('214d', 5)
    if SLOT_16:
        if Unknown51(5):
            Unknown53(23, 2, 49, 5, 2, 21)
            Unknown54('0100000002000000310000000200000015000000')
            if (SLOT_49 >= (-200000)):
                if (SLOT_49 <= 200000):
                    Unknown94(-200000)
        ActivateEffScript('DeathSaucer_Shot_Back', 100)
    Unknown19(23)
    label('end')
    sprite('null', 15)
    Unknown450('frn403_end')
    Unknown23(23)
    Unknown23(45)
    Unknown23(3)
    Unknown23(77)
    Unknown176(1)
    Unknown295(1)

@State
def DeathSaucer_Shot_Back():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkLevel_3_AtkInit')
        callSubroutine('cmnSpecialShot_AtkInit')
        damage1(700)
        Unknown1143(1)
        Unknown1095(1000)
        or_standhit(1)
        untech_Override(30)
        mod_hitstop(3)
        mod_opphitstop(0, 15, 15)
        airHitPushbackX(30000)
        airHitPushbackY(15000)
        Unknown1117(600)
        Unknown2311(2)
        Unknown1203(15)
        Unknown1051(0)
        Unknown1079(1)
        Unknown1045('04000000636d6e5f736c6173685f73000000000000000000000000000000000000000000')
        Unknown717('ShakeYoko', 600, 5, 20, 5)
        Unknown1118('ARC_BTL_CMN_Hit_FRN_DthScr')
        Unknown1119('ARC_BTL_CMN_Guard_Large')
        Unknown1954(1)
        Unknown1629(1)
        Unknown239()
        Unknown450('frn403_loop')
        Unknown2210()
        Unknown2211(1)
        Unknown2217(1)
        Unknown2215(1)
        Unknown35('2d000000656e640000000000000000000000000000000000000000000000000000000000')

        def upon_3():
            callSubroutine('cmnNotMainPlayer_ObjectDelete')
            Unknown200(0)
            if (SLOT_18 <= 300000):
                Unknown98(300000)
                Unknown164(0)
            if SLOT_52:
                if (not SLOT_312):
                    Unknown2208(23)

        def upon_9():
            Unknown53(23, 2, 45, 25, 2, 93)
            Unknown53(23, 2, 46, 3, 2, 93)
            if (SLOT_45 == SLOT_46):
                Unknown941(0)
                mod_opphitstop(0, 0, 0)
                Unknown1803('DeathSaucer_Shot_Back', 25)
            else:
                mod_opphitstop(0, 15, 15)
                Unknown941(45)

        def upon_25():
            Unknown2217(0)

        def upon_12():
            Unknown2217(1)
    sprite('214d', 25)
    makeActive()
    storeValue(2, 52, 0, 1)
    Unknown98(1780000)
    physicsImpulseY(-110000)
    physicsImpulseX(70000)
    Unknown127(-4300)
    Unknown615('ARC_BTL_FRN_DthScr_Return')
    sprite('214d', 14)
    Unknown127(0)
    Unknown98(30000)
    Unknown116(0)
    sprite('214d', 10)
    Unknown127(-2000)
    sprite('214d', 600)
    Unknown1630(1)
    Unknown58(1)
    label('end')
    sprite('null', 15)
    Unknown450('frn403_end')
    Unknown23(45)
    Unknown176(1)
    Unknown295(1)

@State
def DeathWave_shot():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkLevel_3_AtkInit')
        callSubroutine('cmnSpecialShot_AtkInit')
        damage1(1100)
        or_standhit(27)
        or_launchhit(27)
        airHitPushbackX(8000)
        airHitPushbackY(42000)
        untech_Override(25)
        mod_hitstop(14)
        mod_opphitstop(-6, 0, 0)
        Unknown1108(90)
        Unknown1051(0)
        Unknown1954(1)
        Unknown287(1)
        Unknown1731(0)
        Unknown450('bg_frn400_smoke')
        Unknown1118('ARC_BTL_CMN_Hit_FRN_DtRtzn')
        Unknown1119('ARC_BTL_CMN_Guard_Large')

        def upon_23():

            def upon_78():
                Unknown1051(2)
                if (not SLOT_14):
                    Unknown1094(1)
        if Unknown2033(3, 'AssistAttack'):
            damage1(800)
            Unknown1117(0)
            untech_Override(30)
        callSubroutine('cmn_AssistShotHosei')

        def upon_8():
            Unknown295(1)

        def upon_47():
            Unknown23(47)
            storeValue(2, 46, 0, 1)

        def upon_9():
            if (not SLOT_46):
                if Unknown2033(3, 'DeathWave_A'):
                    Unknown2040(3, 'DeathWave_Atk', 0)
                if Unknown2033(3, 'DeathWave_B'):
                    Unknown2040(3, 'DeathWave_Atk', 0)
    sprite('236a', 3)
    Unknown2136('000000000000000000000000e8030000000000003c0000001e000000')
    makeActive()
    Unknown670('01000000e80300000000000000000000')
    Unknown2136('000000000000000000000000e803000000000000640000001e000000')
    callSubroutine('cmnShakeRushFinish')
    Unknown615('ARC_BTL_FRN_DtRtzn_FireAB')
    sprite('236a1', 2)
    sprite('null', 60)
    beginRecovery()
    Unknown1801(1)
    Unknown295(1)

@State
def DeathWave_C_shot1():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkLevel_3_AtkInit')
        callSubroutine('cmnSpecialShot_AtkInit')
        callSubroutine('cmnSpecialAttackEx_ShotInit')
        damage1(1000)
        or_standhit(27)
        or_launchhit(27)
        airHitPushbackX(8000)
        airHitPushbackY(42000)
        untech_Override(30)
        mod_hitstop(14)
        mod_opphitstop(-6, 0, 0)
        Unknown1108(90)
        Unknown1051(0)
        Unknown1954(1)
        Unknown287(1)
        Unknown1731(0)
        Unknown450('bg_frn400_smoke')
        Unknown1118('ARC_BTL_CMN_Hit_FRN_DtRtzn')
        Unknown1119('ARC_BTL_CMN_Guard_Large')

        def upon_8():
            Unknown295(1)

        def upon_47():
            Unknown23(47)
            storeValue(2, 46, 0, 1)

        def upon_9():
            if (not SLOT_46):
                if Unknown2033(3, 'DeathWave_C'):
                    Unknown2040(3, 'DeathWave_Atk', 0)
    sprite('236a', 3)
    makeActive()
    Unknown670('01000000e80300000000000000000000')
    Unknown2136('000000000000000000000000e803000000000000640000001e000000')
    callSubroutine('cmnShakeRushFinish')
    Unknown615('ARC_BTL_FRN_DtRtzn_FireC')
    sprite('236a1', 2)
    sprite('null', 60)
    beginRecovery()
    Unknown1801(1)
    Unknown295(1)

@State
def DeathWave_C_shot2():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkLevel_3_AtkInit')
        callSubroutine('cmnSpecialShot_AtkInit')
        callSubroutine('cmnSpecialAttackEx_ShotInit')
        damage1(1000)
        or_standhit(27)
        or_launchhit(27)
        airHitPushbackX(8000)
        airHitPushbackY(42000)
        untech_Override(30)
        mod_hitstop(14)
        mod_opphitstop(-6, 0, 0)
        Unknown1108(90)
        Unknown1051(0)
        Unknown1954(1)
        Unknown1731(0)
        Unknown450('bg_frn400_smoke')
        Unknown1118('ARC_BTL_CMN_Hit_FRN_DtRtzn')
        Unknown1119('ARC_BTL_CMN_Guard_Large')

        def upon_8():
            Unknown295(1)

        def upon_47():
            Unknown23(47)
            storeValue(2, 46, 0, 1)

        def upon_9():
            if (not SLOT_46):
                if Unknown2033(3, 'DeathWave_C'):
                    Unknown2040(3, 'DeathWave_Atk', 0)
    sprite('236a', 3)
    makeActive()
    Unknown670('01000000e80300000000000000000000')
    Unknown2136('000000000000000000000000e803000000000000640000001e000000')
    callSubroutine('cmnShakeRushFinish')
    sprite('236a1', 2)
    sprite('null', 60)
    beginRecovery()
    Unknown1801(1)
    Unknown295(1)

@State
def DeathWave_action():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
    sprite('null', 20)
    Unknown450('frn400_action00')

@State
def WarpSmash_shot():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        callSubroutine('cmnSpecialShot_AtkInit')
        damage1(900)
        untech_Override(40)
        hitstun_Override(20)
        mod_hitstop(11)
        airHitPushbackX(4000)
        airHitPushbackY(-50000)
        Unknown854(1)
        Unknown806(35000)
        Unknown802(100)
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
        Unknown1183(0)
        callSubroutine('cmn_KuzushiHosei')
        if Unknown2033(3, 'AssistAttack3'):
            callSubroutine('cmn_AssistHosei')
            callSubroutine('cmnAssist3LastAtk')
            Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
            damage1(1000)
        Unknown1914(0)
        Unknown1954(1)
        Unknown458(0)
        Unknown58(1)
        Unknown289(300)
        Unknown450('frn_kidan')
        Unknown1118('ARC_BTL_CMN_Hit_Kidan')
        Unknown1119('ARC_BTL_CMN_Guard_Kidan')
        Unknown2211(1)
        Unknown2221(1)
        Unknown2212(1)
        Unknown2213(1)
        Unknown2214(1)
        Unknown2215(1)

        def upon_45():
            Unknown19(23)

        def upon_8():
            ActivateEffScript('frn_kidan_end', 100)
            Unknown19(23)

        def upon_87():
            Unknown23(87)
            Unknown450('')
            ActivateEffScript('frn_reversalkidan', 100)
            Unknown19(23)

        def upon_2():
            Unknown448('bg_groundsmokeS', 123)
            Unknown670('00000000e80300000000000000000000')
            Unknown19(23)
    sprite('kidan_nanamesita0', 1)
    Unknown2055(0)
    makeActive()
    sprite('kidan_nanamesita', 600)
    Unknown2055(1)
    Unknown164(-55000)
    Unknown202(100000, 0)
    Unknown2229(102)
    Unknown2230(102)

@State
def DeathBall_start():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown457(2)
        Unknown454(2)
        Unknown450('frn430_loop')
    sprite('null', 10)
    Unknown2136('000000000000000000000000e803000000000000aa0000001e000000')
    ActivateEffScript('DeathBall_Tame', 100)
    Unknown188(100)
    Unknown1732(-40000)
    Unknown615('ARC_BTL_FRN_DeathBall_Chrg')
    sprite('null', 5)
    Unknown188(200)
    Unknown99(30000)
    Unknown2077('ShakeTateYoko', 300, 10, 120, 30)
    sprite('null', 5)
    Unknown188(300)
    Unknown99(30000)
    sprite('null', 5)
    Unknown188(400)
    Unknown99(30000)
    sprite('null', 5)
    Unknown188(500)
    Unknown99(30000)
    sprite('null', 5)
    Unknown188(600)
    Unknown99(30000)
    sprite('null', 5)
    Unknown188(700)
    Unknown99(30000)
    sprite('null', 5)
    Unknown188(800)
    Unknown99(30000)
    sprite('null', 5)
    Unknown188(900)
    Unknown99(30000)
    sprite('null', 40)
    Unknown188(1000)
    Unknown99(30000)
    sprite('null', 1)

@Subroutine
def DeathBall_Init():
    Unknown245()
    callSubroutine('cmnAtkLevel_4_AtkInit')
    callSubroutine('cmnUltimateShot_AtkInit')
    damage1(20)
    Unknown1086(20)
    mod_hitstop(2)
    untech_Override(50)
    airHitPushbackX(1000)
    airHitPushbackY(1000)
    Unknown1207('0100000064000000f0490200803801006400000000000000')
    Unknown1208('0100000064000000a033faff803801006400000000000000')
    grHitPushbackX(80)
    Unknown1051(0)
    Unknown941(20)
    Unknown1059(1)
    Unknown717('ShakeTateYoko', 300, 0, 15, 10)
    Unknown1108(-45)
    Unknown1143(1)

    def upon_91():
        Unknown23(91)
        Unknown1143(0)
    Unknown1192('100000004152435f42544c5f434d4e5f4869745f4265616d4c6f6f705f4c50000000000000000000')
    Unknown1193('110000004152435f42544c5f434d4e5f4772645f4265616d4c6f6f705f4c50000000000000000000')
    Unknown1198(1, 0)
    Unknown287(1)
    Unknown294(1)
    physicsImpulseX(33000)
    physicsImpulseY(-15000)
    Unknown289(600)
    Unknown1914(0)
    Unknown450('frn430_loop')

    def upon_1():
        Unknown633(16, 10)
        Unknown633(17, 10)

    def upon_3():
        if (not 
        Unknown53(23, 2, 0, 22, 2, 36)):
            Unknown633(16, 20)
            Unknown633(17, 20)
        if SLOT_48:
            Unknown1079(1)
        else:
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

    def upon_2():
        Unknown23(2)
        Unknown23(90)
        Unknown633(16, 20)
        Unknown633(17, 20)
        Unknown633(21, 25)
        makeActive()
        Unknown176(1)
        Unknown268(0)
        Unknown32('DeathBall_Air')
        Unknown14('landing')

    def upon_47():
        Unknown23(47)
        storeValue(2, 46, 0, 1)

    def upon_90():
        callSubroutine('cmnUltimate_CameraCombo')
        Unknown268(1)
        if (not SLOT_46):
            if SLOT_16:
                if Unknown2489('02000000000000000200000007010000'):
                    Unknown2079('2000000035d9fffff5d70c00b6c20100c70100000000000000000000360000000a0000000a0000000a000000000000000000000000000000')

    def upon_9():
        physicsImpulseX(10000)
        physicsImpulseY(-40000)
        if Unknown2033(23, 'DeathBall_Shot'):
            physicsImpulseX(40000)

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
        makeActive()
        physicsImpulseX(10000)
        physicsImpulseY(-20000)
        Unknown94(-50000)
        Unknown99(80000)
        if Unknown2033(23, 'DeathBall_Shot'):
            Unknown94(-10000)
        Unknown54('00000000020000002d0000000000000001000000')
        if (SLOT_45 >= 8):
            Unknown19(23)
            ActivateEffScript('cmn_kidan_end_L', 100)
            if (SLOT_18 <= 500000):
                Unknown670('01000000e80300000000000000000000')
            if (not SLOT_46):
                if Unknown2033(3, 'DeathBall'):
                    Unknown1798(3, 24)
                if Unknown2033(3, 'DeathBall_CD'):
                    Unknown1798(3, 24)
                if Unknown2033(3, 'AirDeathBall'):
                    Unknown1798(3, 24)
                if Unknown2033(3, 'AirDeathBall_CD'):
                    Unknown1798(3, 24)
        elif (not SLOT_46):
            if Unknown2033(3, 'DeathBall'):
                Unknown1798(3, 25)
            if Unknown2033(3, 'DeathBall_CD'):
                Unknown1798(3, 25)
            if Unknown2033(3, 'AirDeathBall'):
                Unknown1798(3, 25)
            if Unknown2033(3, 'AirDeathBall_CD'):
                Unknown1798(3, 25)

    def upon_23():
        Unknown23(23)
        Unknown23(9)
        Unknown23(92)
        Unknown23(93)
        Unknown23(77)
        Unknown164(0)
        Unknown1801(1)
        Unknown2136('000000000000000000000000e803000000000000640000001e000000')
        Unknown477('00000000000000000000000010270000')
        storeValue(2, 48, 0, 1)
        makeActive()
        damage1(2100)
        Unknown1086(36)
        untech_Override(30)
        mod_hitstop(5)
        mod_opphitstop(0, 5, 5)
        or_standhit(12)
        or_launchhit(12)
        airHitPushbackX(15000)
        airHitPushbackY(45000)
        Unknown941(0)
        Unknown1207('000000006400000000000000000000000000000000000000')
        Unknown1208('000000006400000000000000000000000000000000000000')
        Unknown1059(0)
        Unknown1108(90)
        Unknown717('ShakeTateYoko', 1500, 0, 50, 10)

        def upon_9():
            if conditionalunk2498(25, 2, 24):
                damage1(2600)
                Unknown1086(29)
            else:
                damage1(2100)
                Unknown1086(36)

        def upon_89():
            callSubroutine('cmnUltimate_CameraCombo')
            if (not SLOT_46):
                if SLOT_16:
                    if Unknown2489('02000000000000000200000007010000'):
                        Unknown1067(4, 0, 100000)

                        def upon_95():
                            Unknown23(95)
                            Unknown69(0)
                            Unknown271('03000000640000000f0000000f000000')
                    Unknown2079('2000000035d9fffff5d70c00b6c20100c70100000000000000000000360000000a000000140000000a000000000000000000000000000000')
            endIf()
        if (not SLOT_46):
            if Unknown2033(3, 'DeathBall'):
                Unknown1798(3, 24)
            if Unknown2033(3, 'DeathBall_CD'):
                Unknown1798(3, 24)
            if Unknown2033(3, 'AirDeathBall'):
                Unknown1798(3, 24)
            if Unknown2033(3, 'AirDeathBall_CD'):
                Unknown1798(3, 24)

@State
def DeathBall_Short_Shot():

    def upon_IMMEDIATE():
        callSubroutine('DeathBall_Init')
        Unknown164(-60000)
    sprite('null', 6)
    sprite('236ab', 6)
    makeActive()
    physicsImpulseX(30000)
    physicsImpulseY(-50000)
    ActivateEffScript('DeathBall_Air', 100)
    Unknown2229(101)
    Unknown2230(101)
    Unknown632('150000004152435f42544c5f46524e5f446561746842616c6c5f4669726500000000000064000000')
    label('loop')
    sprite('236ab', 6)
    makeActive()
    Unknown2077('ShakeTateYoko', 200, 0, 18, 1)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000058020000')
    Unknown18()
    label('landing')
    sprite('236ab_end0', 4)
    Unknown2077('ShakeTate', 1500, 0, 50, 10)
    Unknown450('frn430_end')
    Unknown1798(23, 23)
    Unknown615('ARC_BTL_FRN_DeathBall_Expl')
    sprite('236ab_end0', 3)
    Unknown633(16, 20)
    Unknown633(17, 20)
    Unknown670('01000000d00700000000000000000000')
    sprite('236ab_end1', 4)
    Unknown23(89)
    sprite('null', 13)
    Unknown295(1)
    Unknown633(16, 20)
    Unknown633(17, 20)
    sprite('null', 25)
    Unknown1801(0)

@State
def DeathBall_Shot():

    def upon_IMMEDIATE():
        callSubroutine('DeathBall_Init')
        Unknown164(-40000)
    sprite('null', 6)
    sprite('236ab', 4)
    makeActive()
    physicsImpulseX(60000)
    physicsImpulseY(-50000)
    ActivateEffScript('DeathBall_Air', 100)
    Unknown2229(101)
    Unknown2230(101)
    Unknown632('150000004152435f42544c5f46524e5f446561746842616c6c5f4669726500000000000064000000')
    label('loop')
    sprite('236ab', 6)
    makeActive()
    Unknown2077('ShakeTateYoko', 200, 0, 18, 1)

    def upon_46():
        Unknown23(46)
        Unknown116(150)
        airHitPushbackY(-35000)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000058020000')
    Unknown18()
    label('landing')
    sprite('236ab_end0', 4)
    Unknown23(46)
    Unknown2077('ShakeTate', 1500, 0, 50, 10)
    Unknown450('frn430_end')
    Unknown1798(23, 23)
    Unknown615('ARC_BTL_FRN_DeathBall_Expl')
    sprite('236ab_end0', 3)
    Unknown633(16, 20)
    Unknown633(17, 20)
    Unknown670('01000000d00700000000000000000000')
    sprite('236ab_end1', 4)
    Unknown23(89)
    sprite('null', 13)
    Unknown295(1)
    Unknown633(16, 20)
    Unknown633(17, 20)
    sprite('null', 25)
    Unknown1801(0)

@State
def DeathBall_Air():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown2519(1)
    label('loop')
    sprite('null', 10)
    Unknown2275(0, 10000)
    Unknown449('cmn_strike00', 100)
    labelEnd('loop')

@State
def DeathBall_Tame():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown457(2)
        Unknown454(2)
        Unknown2519(1)
    sprite('null', 2147483647)
    Unknown1955('66726e3433305f74616d65303000000000000000000000000000000000000000')

@State
def NovaStrike_StartEff():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown1801(1)
        Unknown295(1)
        Unknown2519(1)
        Unknown188(650)
        Unknown99(100000)
        Unknown289(600)
        Unknown35('170000006c6f6f7000000000000000000000000000000000000000000000000000000000')
    sprite('null', 15)
    Unknown450('frn431_sparkstart')
    sprite('null', 2147483647)
    Unknown450('frn431_spark')
    Unknown3()
    label('loop')
    sprite('null', 2147483647)
    Unknown23(23)
    Unknown188(700)
    Unknown450('frn431_start')
    Unknown3()

@State
def NovaStrike_Eff():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown2519(1)
        Unknown232(20000)
        Unknown164(-40000)
        Unknown99(150000)
        Unknown289(600)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown450('frn431_loop')
    Unknown3()
    label('end')
    sprite('null', 30)
    Unknown23(23)
    Unknown450('frn431_end')
    Unknown454(0)
    Unknown457(0)
    Unknown295(1)
    Unknown1801(1)
    Unknown3()

@State
def frn432_HandAura():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown295(1)
        Unknown2519(1)
        Unknown188(500)
        Unknown450('frn432_eff08')
    sprite('null', 6)
    Unknown1731(-120000)
    Unknown94(10000)
    Unknown99(-10000)
    sprite('null', 6)
    Unknown1731(-90000)
    Unknown94(-40000)
    sprite('null', 6)
    Unknown1731(-50000)
    Unknown94(-35000)
    Unknown99(0)
    sprite('null', 21)
    sprite('null', 6)
    Unknown1731(-100000)
    Unknown99(15000)
    Unknown94(70000)
    Unknown3()

@State
def frn432_BodyAura():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown2519(1)
        Unknown295(1)
        Unknown450('frn432_eff07')
        Unknown99(10000)
    sprite('null', 90)

@State
def frn432_BeamAura():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown295(1)
        Unknown2519(1)
        Unknown450('frn432_eff06')
        Unknown99(10000)
    sprite('null', 90)

@State
def frn432_BeamAura_End():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown2519(1)
        Unknown99(10000)
    sprite('null', 1)
    Unknown448('frn432_eff09', 100)

@State
def frn432_Smokes():

    def upon_IMMEDIATE():
        Unknown239()
        Unknown457(2)
        Unknown454(2)
        Unknown295(1)
        Unknown2519(1)
        Unknown289(40)
    sprite('null', 5)
    label('loop')
    sprite('null', 15)
    ActivateEffScript('frn432_smoke', 100)
    labelEnd('loop')

@State
def frn432_Smoke():
    sprite('null', 60)
    Unknown450('cmn_dash_default_def')
    Unknown94(50000)
    Unknown148(1030)
    Unknown156(875)

@State
def frn432_Smokes2():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown295(1)
        Unknown2519(1)
        Unknown289(45)
    label('loop')
    sprite('null', 15)
    ActivateEffScript('frn432_smoke2', 100)
    labelEnd('loop')

@State
def frn432_Smoke2():
    sprite('null', 60)
    Unknown450('cmn_dash_default_def')
    Unknown94(450000)
    Unknown188(1500)

@State
def YouWillDie_Core():

    def upon_IMMEDIATE():
        Unknown456(3)
        Unknown454(3)
        Unknown164(45000)
        Unknown289(300)
        Unknown450('frn432_eff00')
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
        Unknown35('2f000000656e640000000000000000000000000000000000000000000000000000000000')

        def upon_35():
            Unknown456(0)
            Unknown454(0)
            Unknown295(1)

        def upon_24():
            Unknown23(24)
            storeValue(2, 45, 0, 0)
            Unknown1803('YouWillDie_Atk', 29)
            if Unknown2033(3, ' YouWillDie'):
                Unknown53(3, 2, 45, 23, 0, 0)
                Unknown1798(3, 25)
            storeValue(2, 47, 0, 1)
            storeValue(2, 51, 0, 1)

            def upon_24():
                Unknown54('00000000020000002f0000000000000001000000')
                if (SLOT_47 >= 8):
                    if Unknown2033(3, 'YouWillDie'):
                        Unknown1798(3, 24)
                elif Unknown2033(3, 'YouWillDie'):
                    Unknown1798(3, 25)

        def upon_3():
            if (not SLOT_46):
                Unknown1804('596f7557696c6c4469655f41746b00000000000000000000000000000000000017000000')
    label('loop')
    sprite('null', 2)
    Unknown54('0000000002000000300000000000000001000000')
    Unknown2279('02000000300000000000000000000000')
    Unknown445('596f7557696c6c4469655f41746b00000000000000000000000000000000000064000000')
    if (SLOT_45 >= 8):
        Unknown53(1, 2, 45, 23, 0, 1)
    sprite('null', 2)
    Unknown3()
    Unknown54('00000000020000002d0000000000000001000000')
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000002d000000000000000a000000')
    label('end')
    sprite('null', 1)
    Unknown23(23)
    Unknown23(24)
    Unknown23(47)
    Unknown23(3)
    storeValue(2, 49, 0, 1)
    ActivateEffScript('YouWillDie_Atk', 100)
    Unknown1803('YouWillDie_Atk', 30)
    if Unknown2033(3, 'YouWillDie'):
        Unknown1798(3, 24)
    Unknown454(0)
    Unknown456(0)
    Unknown294(1)
    sprite('null', 1)
    Unknown32('YouWillDie_Atk')
    sprite('null', 9)
    Unknown450('frn432_eff01')
    Unknown633(16, 20)
    Unknown633(17, 20)
    sprite('null', 10)

@State
def YouWillDie_Atk():

    def upon_IMMEDIATE():
        Unknown245()
        callSubroutine('cmnAtkLevel_4_AtkInit')
        callSubroutine('cmnUltimateShot_AtkInit')
        damage1(480)
        Unknown1086(40)
        mod_hitstop(2)
        or_standhit(12)
        or_launchhit(12)
        airHitPushbackX(35000)
        airHitPushbackY(35000)
        untech_Override(100)
        Unknown1027(50000000, -300000, 0, 0)
        Unknown1187(0)
        Unknown716(1)
        Unknown733(1)
        Unknown734(1)
        Unknown1191(1)
        Unknown736(1)
        Unknown1192('100000004152435f42544c5f434d4e5f4869745f4265616d4c6f6f705f4c50000000000000000000')
        Unknown1193('110000004152435f42544c5f434d4e5f4772645f4265616d4c6f6f705f4c50000000000000000000')

        def upon_30():
            airHitPushbackX(45000)
            airHitPushbackY(60000)
            Unknown1208('000000006400000000000000000000000000000000000000')
            Unknown1064('436d6e4e65757472616c00000000000000000000000000000000000000000000')
            makeActive()
            if conditionalunk2499(3, 2, 24):
                makeActive()
            else:
                beginRecovery()
            if conditionalunk2500(12, 2, 2, 47, 0, 8):
                beginRecovery()
        Unknown456(2)
        Unknown454(2)
        Unknown457(2)
        Unknown453(2)
        Unknown289(60)
        Unknown1954(1)
        Unknown58(1)
        Unknown450('frn432_eff02')

        def upon_23():
            Unknown23(23)
            ActivateEffScript('YouWillDie_End', 100)
            storeValue(2, 46, 0, 1)
            Unknown53(2, 2, 46, 23, 0, 1)

        def upon_93():
            Unknown53(2, 2, 115, 23, 2, 115)
            Unknown19(23)
            Unknown1798(2, 24)

        def upon_29():
            storeValue(2, 45, 0, 0)

        def upon_90():
            callSubroutine('cmnUltimate_CameraCombo')
            if SLOT_116:
                if Unknown2033(3, 'YouWillDie'):
                    Unknown53(3, 2, 45, 23, 0, 0)

        def upon_8():
            if SLOT_45:
                Unknown1798(2, 23)

        def upon_3():
            if conditionalunk2498(2, 2, 47):
                if conditionalunk2499(2, 2, 49):
                    Unknown53(23, 2, 0, 2, 2, 115)
                    if (SLOT_115 <= SLOT_0):
                        Unknown19(23)
            if (not 
            Unknown53(23, 2, 0, 22, 2, 36)):
                Unknown633(16, 20)
                Unknown633(17, 20)
            if (not 
            Unknown2033(3, 'YouWillDie')):
                Unknown633(16, 20)
                Unknown633(17, 20)

        def upon_1():
            if SLOT_46:
                storeValue(2, 46, 0, 0)
                Unknown53(2, 2, 46, 23, 2, 46)
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('frn432_eff03', 100)
    sprite('youwilldie0', 1)
    makeActive()
    Unknown202(100000, 0)
    Unknown1208('01000000670000006079feffa08601006400000000000000')
    sprite('youwilldie0', 1)
    Unknown734(0)
    label('loop')
    sprite('youwilldie1', 2)
    Unknown2301(1200)
    sprite('youwilldie1', 2)
    Unknown2301(1000)
    Unknown1208('010000006700000000000000a08601006400000000000000')
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def YouWillDie_End():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown457(2)
        Unknown164(45000)
        Unknown289(60)
        Unknown2036(2, 0)
        Unknown58(1)
        Unknown450('frn432_eff04')

        def upon_3():
            if Unknown51(2):
                Unknown2488('02000000190100000200000019010000')
                Unknown2036(2, 0)

        def upon_1():
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('frn432_eff05', 100)
    label('loop')
    sprite('null', 2)
    Unknown2301(1000)
    sprite('null', 2)
    Unknown2301(1200)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def frn433_GoldenAura():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown1801(1)
        Unknown454(2)
        Unknown457(2)
        Unknown450('frn433_GoldenAura')
        Unknown35('17000000456e640000000000000000000000000000000000000000000000000000000000')
        Unknown294(1)
        Unknown2523('0300000001000000')
    sprite('null', 37)
    ActivateEffScript('frn433_GoldenRay', 100)
    label('End')
    sprite('null', 10)
    sprite('null', 60)
    Unknown450('frn433_GoldenAuraEnd')
    Unknown454(0)
    Unknown457(0)

@State
def frn433_GoldenRay():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown1801(1)
        Unknown454(2)
        Unknown457(2)
        Unknown450('frn433_GoldenRay')
        Unknown294(1)
        Unknown2523('0300000001000000')
        Unknown188(400)
    sprite('null', 20)
    Unknown191(30)
    sprite('null', 20)
    Unknown191(60)

@State
def frn433_CutInRay():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown454(2)
        Unknown457(2)
        Unknown450('frn_433_CutinRay')
        Unknown294(1)
    sprite('null', 120)
    Unknown3()

@State
def frn433_CutInRockMatome():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown454(2)
        Unknown457(2)
        Unknown294(1)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    ActivateEffScript('frn433_CutInRock', 100)
    Unknown41(1)
    Unknown94(150000)
    Unknown40()
    ActivateEffScript('frn433_CutInRock', 100)
    Unknown41(1)
    Unknown94(-150000)
    Unknown40()
    ActivateEffScript('frn433_CutInRock', 100)
    Unknown41(1)
    Unknown1732(150000)
    Unknown40()
    ActivateEffScript('frn433_CutInRock', 100)
    Unknown41(1)
    Unknown1732(-150000)
    Unknown40()
    ActivateEffScript('frn433_CutInRock', 100)
    Unknown41(1)
    Unknown94(225000)
    Unknown1732(-225000)
    Unknown40()
    ActivateEffScript('frn433_CutInRock', 100)
    Unknown41(1)
    Unknown94(-225000)
    Unknown1732(-225000)
    Unknown40()
    ActivateEffScript('frn433_CutInRock', 100)
    Unknown41(1)
    Unknown94(150000)
    Unknown1732(150000)
    Unknown40()
    ActivateEffScript('frn433_CutInRock', 100)
    Unknown41(1)
    Unknown94(-150000)
    Unknown1732(150000)
    Unknown40()
    ActivateEffScript('frn433_CutInRock', 100)
    Unknown41(1)
    Unknown94(375000)
    Unknown1732(-375000)
    Unknown40()
    ActivateEffScript('frn433_CutInRock', 100)
    Unknown41(1)
    Unknown94(-375000)
    Unknown1732(-375000)
    Unknown40()
    ActivateEffScript('frn433_CutInRock', 100)
    Unknown41(1)
    Unknown1732(-375000)
    Unknown40()
    label('end')
    sprite('null', 20)
    Unknown1803('frn433_CutInRock', 23)

@State
def frn433_CutInRock():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown454(2)
        Unknown457(2)
        Unknown450('bg_debris00')
        Unknown294(1)
        Unknown188(2000)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown99(75000)
    Unknown166(250)
    physicsImpulseY(300)
    label('end')
    sprite('null', 4)
    sprite('null', 10)
    Unknown191(-200)
    Unknown103(-30000, 0)
    Unknown118(6000, 12000)

@State
def frn433_GoldenAuraCutin():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown1801(1)
        Unknown454(2)
        Unknown457(2)
        Unknown450('frn_433_CutinAura_Loop')
        Unknown35('17000000456e640000000000000000000000000000000000000000000000000000000000')
        Unknown294(1)
        Unknown99(180000)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    label('end')
    sprite('null', 30)
    Unknown450('frn_433_CutinAura_End')

@State
def Sorbet_shot():

    def upon_IMMEDIATE():
        Unknown245()
        callSubroutine('cmnAtkLevel_4_AtkInit')
        callSubroutine('cmnUltimateShot_AtkInit')
        callSubroutine('cmn_MutekiHosei')
        damage1(1200)
        Unknown1086(70)
        mod_hitstop(5)
        or_standhit(2)
        or_launchhit(8)
        airHitPushbackX(1000)
        airHitPushbackY(1000)
        untech_Override(100)
        Unknown842(0)
        Unknown941(60)
        Unknown810(5000)
        Unknown1079(1)
        Unknown1051(0)
        Unknown736(1)
        Unknown948(1)
        Unknown1118('ARC_BTL_CMN_Hit_Midle-A')
        Unknown1119('ARC_BTL_CMN_Guard_Beam')
        Unknown1920(-20)
        Unknown98(250000)
        Unknown294(1)
        Unknown450('frn_solveshot')

        def upon_90():
            callSubroutine('cmnUltimate_CameraCombo')

        def upon_78():
            or_standhit(2)
            if Unknown2033(25, 'CmnActSlidedown'):
                or_standhit(8)
                or_launchhit(8)
                Unknown842(0)
                mod_opphitstop(0, 20, 20)
                Unknown1187(1)
    sprite('null', 25)
    sprite('kidan', 100)
    Unknown612('ARC_BTL_CMN_Kdn_Fire_L')
    makeActive()
    Unknown202(90000, 0)

@State
def frn600_Aura():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown454(2)
        Unknown457(2)
        Unknown450('frn_600_aura00')
    sprite('null', 2147483647)
    ActivateEffScript('frn600_Syutyusen', 100)

@State
def frn600_Speed():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown454(2)
        Unknown457(2)
        Unknown450('frn_600_speed')
        Unknown239()
    sprite('null', 50)

@State
def frn600_Syutyusen():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown454(2)
        Unknown457(2)
        Unknown450('cmn_syutyusen')
    sprite('null', 50)

@State
def frn600_RockMatome():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown454(2)
        Unknown457(2)
        Unknown294(1)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    ActivateEffScript('frn600_Rock', 100)
    Unknown41(1)
    Unknown94(150000)
    Unknown1732(150000)
    Unknown99(75000)
    Unknown40()
    ActivateEffScript('frn600_Rock', 100)
    Unknown41(1)
    Unknown94(150000)
    Unknown1732(-150000)
    Unknown99(50000)
    Unknown40()
    ActivateEffScript('frn600_Rock', 100)
    Unknown41(1)
    Unknown94(100000)
    Unknown99(30000)
    Unknown188(1000)
    Unknown40()
    ActivateEffScript('frn600_Rock', 100)
    Unknown41(1)
    Unknown94(-150000)
    Unknown1732(250000)
    Unknown99(300000)
    Unknown188(3000)
    Unknown40()
    ActivateEffScript('frn600_Rock', 100)
    Unknown41(1)
    Unknown94(-150000)
    Unknown1732(-250000)
    Unknown99(250000)
    Unknown188(3000)
    Unknown40()

@State
def frn600_Rock():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown454(2)
        Unknown457(2)
        Unknown450('bg_debris00')
        Unknown294(1)
        Unknown188(2000)
        Unknown166(250)
        Unknown118(100, 500)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    label('loop')
    sprite('null', 2)
    Unknown1732(500)
    sprite('null', 2)
    Unknown1732(-500)
    labelEnd('loop')

@State
def FRN600_groundsmoke():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown454(2)
        Unknown457(2)
        Unknown94(-300000)
        Unknown1732(-150000)
    label('loop')
    sprite('null', 10)
    Unknown2273(0, 1500)
    Unknown2283(0, 75000)
    Unknown449('bg_undersmoke00', 100)
    labelEnd('loop')

@State
def FRN600_groundsmoke2():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown454(2)
        Unknown457(2)
        Unknown94(-300000)
        Unknown1732(150000)
    label('loop')
    sprite('null', 10)
    Unknown2273(0, 1500)
    Unknown2283(0, -75000)
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
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2076('e6bcfdffe62b0500cf3c01001e0200008e1a00000000000036000000000000005a0000001e00000001000000')
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def FinishCamera_NmlAtk1D():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 60)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    Unknown2079('0d000000b2cffbffe5eb0700f0060100570700006a1d00000000000036000000000000006400000014000000000000000200000002000000')
    sprite('null', 60)
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
    sprite('null', 60)
    Unknown32('cmn_syutyusen')

@State
def FinishCamera_NmlAtk3D():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 60)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    Unknown2079('0d0000001baefbffe5eb0700e5a8000013090000b31500000000000036000000000000006400000014000000000000000200000002000000')
    sprite('null', 60)
    Unknown32('cmn_syutyusen')

@State
def FinishCamera_YouWillDie():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 10)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    Unknown2079('0d0000003171feffc9ae050033e60000ec040000891000000000000036000000000000000a00000000000000000000000200000002000000')
    sprite('null', 50)
    Unknown2079('0d000000017cfbff18930400a6e5000056040000ff220000000000003600000050000000140000000a000000000000000200000002000000')
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def FinishCamera_NovaStrike():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 10)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    Unknown2079('0d000000e58801005cc40700114b01001b0100000afcffff0000000036000000000000000a00000000000000000000000200000002000000')
    sprite('null', 50)
    Unknown2079('0d000000dbc6feff54be0700114b01001d020000c3070000000000003600000050000000140000000a000000000000000200000002000000')
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def FRN610_MoveFingerBall():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('frn_610_scranim')
        Unknown239()
    sprite('null', 30)

@State
def FRN610_FingerBall():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('frn_610_finger00')
        Unknown239()
    sprite('null', 2147483647)

@State
def FRN610_FingerBall2():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('frn_610_finger01')
        Unknown239()
    sprite('null', 2147483647)

@State
def FRN812_bdn():

    def upon_IMMEDIATE():
        Unknown92(0)
        Unknown98(0)
        Unknown1731(0)
        Unknown454(2)
        Unknown2494('62646e000000000000000000000000000000000000000000000000000000000062646e5f46524e38313263730000000000000000000000000000000000000000')
        Unknown2057('626f647900000000000000000000000000000000000000000000000000000000')
        Unknown2058('626f647900000000000000000000000000000000000000000000000000000000')
        Unknown2059()
        Unknown457(2)
        Unknown2189(0, 5)
        Unknown35('170000005279756861690000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown2060('626f647900000000000000000000000000000000000000000000000000000000')
    label('Ryuhai')
    sprite('null', 2147483647)
    ActivateEffScript('frn_812_EnemyRyuhai', 100)

@State
def FRN812_Manp01_01():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown451('4d4e5000000000000000000000000000000000000000000000000000000000004d4e505f46524e38313263735f30310000000000000000000000000000000000')
        Unknown2189(0, 5)
        Unknown370()
    sprite('null', 2147483647)

@State
def bdn812_SubCharacter():

    def upon_IMMEDIATE():
        Unknown92(0)
        Unknown98(0)
        Unknown1731(0)
        Unknown454(2)
        Unknown457(2)
        Unknown2189(0, 5)
        Unknown451('56535f62646e5f474b4e00000000000000000000000000000000000000000000474b4e5f46524e38313263730000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown3()

@State
def FRN812_zuzaa():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown454(2)
        Unknown457(2)
        physicsImpulseX(200000)
        Unknown94(-2100000)
        Unknown1732(-150000)
        Unknown289(63)
    label('loop')
    sprite('null', 2)
    ActivateEffScript('FRN812_zuzaaKo', 100)
    labelEnd('loop')

@State
def FRN812_zuzaaKo():

    def upon_IMMEDIATE():
        Unknown457(2)
    sprite('null', 120)
    Unknown450('frn_812_zuzaa')

@State
def FRN812_zuzaa2():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown454(2)
        Unknown457(2)
        physicsImpulseX(200000)
        Unknown94(-2100000)
        Unknown1732(300000)
        Unknown289(63)
        Unknown232(180000)
    label('loop')
    sprite('null', 2)
    ActivateEffScript('FRN812_zuzaaKo2', 100)
    labelEnd('loop')

@State
def FRN812_zuzaaKo2():

    def upon_IMMEDIATE():
        Unknown457(2)
    sprite('null', 120)
    Unknown450('frn_812_zuzaa2')

@State
def FRN812_YoinSmoke():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('frn_812_yoinSmoke')
        Unknown94(2000000)
    sprite('null', 120)

@State
def FRN812_PowerBallThrow():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('frn_812_throwPowerball')
        Unknown94(1250000)
        Unknown99(250000)
        Unknown289(120)
        Unknown232(4500)
    sprite('null', 1)
    ActivateEffScript('FRN812_Syutyusen', 100)
    label('Loop')
    sprite('null', 15)
    physicsImpulseX(-20000)
    sprite('null', 2)
    physicsImpulseX(-1000)
    sprite('null', 2)
    physicsImpulseX(-500)
    sprite('null', 2)
    physicsImpulseX(-250)
    sprite('null', 2)
    physicsImpulseX(-125)
    sprite('null', 1000)
    physicsImpulseX(0)

@State
def FRN812_Syutyusen():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('frn_812_syutyusen')
    sprite('null', 120)

@State
def FRN812_PowerBallWait():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('frn_812_MinePowerball3')
        Unknown99(450000)
        Unknown94(-2200000)
        Unknown188(5000)
    sprite('null', 60)

@State
def FRN812_PowerBall():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('frn_812_MinePowerball4')
        Unknown99(750000)
        Unknown94(-1000000)
        Unknown188(5000)
        Unknown191(7)
    sprite('null', 40)
    sprite('null', 4)
    Unknown94(40000)
    sprite('null', 4)
    Unknown94(40000)
    sprite('null', 4)
    Unknown94(40000)
    sprite('null', 4)
    Unknown94(40000)
    sprite('null', 4)
    Unknown94(40000)
    sprite('null', 4)
    Unknown94(20000)
    sprite('null', 4)
    Unknown94(20000)
    sprite('null', 4)
    Unknown94(20000)
    sprite('null', 4)
    Unknown94(20000)
    sprite('null', 4)
    Unknown94(20000)
    sprite('null', 4)
    Unknown94(20000)
    sprite('null', 4)
    Unknown94(20000)

@State
def FRN812_GroundBomb():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('frn_812cs_groundBomb')
        Unknown188(2500)
        Unknown94(-2500000)
        Unknown1732(500000)
        Unknown232(-8000)
    sprite('null', 2147483647)
    Unknown191(40)

@State
def FRN812_HitRyuhai():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('frn_812_HitRyuhai')
        Unknown188(2000)
        Unknown94(2000000)
        Unknown164(-15000)
    sprite('null', 2147483647)
    Unknown191(50)

@State
def FRN812_WhiteOut():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('frn_812_WhiteOut')
    sprite('null', 2147483647)

@State
def FRN812_WhiteBG():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('frn_812_WhiteBG')
    sprite('null', 2147483647)

@State
def FRN812_NamekkuBG():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('frn_812_NamekkuBG')
        Unknown1732(-550000)
        Unknown99(-100000)
    sprite('null', 2147483647)

@State
def FRN812_WhiteOut2():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('frn_812_WhiteOut2')
    sprite('null', 2147483647)

@State
def frn_812_EnemyRyuhai():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown457(2)
        Unknown450('frn_812_EnemyRyuhai')
        Unknown164(-85000)
        Unknown99(150000)
        Unknown35('170000005279756861694368616e67650000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    label('RyuhaiChange')
    sprite('null', 2147483647)
    Unknown450('frn_812_EnemyRyuhai2')
    Unknown188(3000)
    Unknown99(-100000)
    Unknown164(-90000)
    Unknown94(2000000)

@State
def FRN812_Earth():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('frn_812_Earth')
        Unknown94(-4000000)
        Unknown1732(-8000000)
        Unknown99(-6000000)
        Unknown188(6000)
        Unknown180(7500)
    sprite('null', 2147483647)

@State
def FRN812_FinalBomb():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('frn_812_FinalBomb')
        Unknown94(-8000000)
        Unknown99(3150000)
        Unknown188(2000)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 2147483647)
    Unknown1732(-150000)

@State
def FRN812_ShadowMatome():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown458(2)
        Unknown457(2)
        Unknown454(2)
        Unknown1976(1)
        Unknown289(10000)
    sprite('null', 2147483647)
    Unknown479('46524e3831325f536861646f7700000000000000000000000000000000000000ff1f000001000000')

@State
def FRN812_Shadow():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown458(2)
        Unknown457(2)
        Unknown450('frn_812_shadow')
        Unknown289(10000)
    sprite('null', 2147483647)

@State
def DUMMYDUMMY():
    sprite('null', 1)