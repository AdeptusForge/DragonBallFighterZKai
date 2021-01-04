@State
def dmy():
    sprite('null', 1)

@State
def okasi():

    def upon_IMMEDIATE():
        callSubroutine('cmn_okasi')
    sprite('null', 2147483647)
    Unknown450('cen_okasi')

@State
def cen232Eff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 30)
    Unknown450('cen_232_strike')

@State
def cen232EffSmoke():

    def upon_IMMEDIATE():
        Unknown94(-75000)
        Unknown1732(75000)
        Unknown239()
    sprite('null', 1)
    Unknown448('bg_land_default', 100)

@State
def cen204Eff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 30)
    Unknown450('cen_204_strike')

@State
def cen207Eff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
    sprite('null', 30)
    Unknown450('cen_207_strike')

@State
def cen261Eff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 20)
    Unknown450('cen_261_strike')

@State
def cen263Eff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 3)
    Unknown450('cen_263_strike')
    sprite('null', 1)
    Unknown450('cen_263_strike2')
    sprite('null', 20)
    Unknown450('cen_263_strike3')

@State
def cen262Eff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 20)
    Unknown450('cen_262_strike')

@State
def cen_5CEff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 60)
    Unknown450('cen_262EFF10')

@State
def cen_2CEff():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown164(62500)
        Unknown99(350000)
        Unknown94(125000)
    sprite('null', 60)
    Unknown450('cmn_strike00')

@State
def cen_hajiki():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 30)
    Unknown450('cen_hajiki')

@State
def __5D_shot():

    def upon_IMMEDIATE():
        Unknown243()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        callSubroutine('cmn5DKidan_AtkInit')
        callSubroutine('cmnKidan_Init')
        airHitPushbackX(14000)
        airHitPushbackY(1500)
        grHitPushbackX(60)
        Unknown2229(102)
        Unknown450('cen_205_beam')
        Unknown202(90000, 0)
        Unknown2221(0)
        Unknown2212(0)
        Unknown2213(0)
        Unknown2214(0)
        Unknown1202('4152435f42544c5f434d4e5f4869745f4b6964616e0000000000000000000000')
        Unknown1119('dammyName')
        Unknown1119('ARC_BTL_CMN_Guard_Beam')

        def upon_8():
            storeValue(2, 52, 0, 1)

        def upon_49():
            if Unknown2041('5D_shot'):
                Unknown23(49)
                Unknown23(3)
                Unknown23(8)
        if Unknown2033(3, 'NmlAtk5D'):
            if (not 
            Unknown53(23, 2, 0, 3, 2, 45)):
                or_standhit(8)
                or_launchhit(8)
                airHitPushbackX(3000)
                airHitPushbackY(30000)
    sprite('kidan0', 1)
    makeActive()
    sprite('kidan1', 600)
    label('Koware')
    sprite('null', 10)
    Unknown176(1)
    Unknown450('')

@State
def __5D_beam_start():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('cmn_kidan_throw')
        Unknown188(500)
    sprite('null', 9)
    Unknown612('ARC_BTL_CMN_kidan_Chrg')

@State
def cen_beam_mazzle():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('cmn_mazzle')
        Unknown1731(100000)
    sprite('null', 60)

@State
def cen_reversalkidan():

    def upon_IMMEDIATE():
        Unknown476('63656e5f726576657273616c5f6b6964616e0000000000000000000000000000')
        Unknown176(1)
    sprite('null', 2147483647)
    ActivateEffScript('cmn_reversal_mazzle', 100)

@State
def kidan_smoke():

    def upon_IMMEDIATE():
        Unknown94(-27000)
    sprite('null', 1)
    Unknown448('bg_undersmoke00', 100)

@State
def jumpkidan_start():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(3)
        Unknown94(50000)
        Unknown99(-90000)
        Unknown1732(400000)
        ActivateEffScript('jumpkidan_start_aura', 100)
    sprite('null', 18)
    Unknown3()

@State
def jumpkidan_start_aura():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown458(0)
        Unknown457(2)
        Unknown454(2)
        Unknown450('cen_265_tame')
        Unknown1732(150000)
        Unknown99(-35000)
    sprite('null', 2)
    Unknown188(100)
    sprite('null', 2)
    Unknown188(300)
    sprite('null', 2)
    Unknown188(600)
    sprite('null', 2)
    Unknown188(800)
    Unknown99(90000)
    Unknown94(50000)
    Unknown1732(-65000)
    sprite('null', 1)
    Unknown99(-40000)
    Unknown94(45000)
    Unknown1732(-250000)
    sprite('null', 1)
    Unknown94(45000)
    Unknown99(-20000)
    Unknown1732(-30000)
    sprite('null', 1)
    Unknown94(-170000)
    Unknown1732(200000)
    Unknown99(-75000)
    sprite('null', 1)
    Unknown450('cen_265_tameZplus')
    Unknown94(100000)
    Unknown99(-90000)
    Unknown1732(65000)

@State
def cen265_Eff():

    def upon_IMMEDIATE():
        Unknown460(2)
        Unknown454(2)
        Unknown457(2)
        Unknown450('cen_265_eff00')
    sprite('null', 4)
    sprite('null', 20)
    Unknown450('cen_265_eff01')

@Subroutine
def jumpkidan_init():
    Unknown243()
    callSubroutine('cmnAtkLevel_2_AtkInit')
    callSubroutine('cmnAir5DKidan_AtkInit')
    callSubroutine('cmnKidan_Init')
    damage1(500)
    or_standhit(8)
    or_launchhit(8)
    airHitPushbackX(3000)
    airHitPushbackY(40000)
    untech_Override(31)
    Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
    Unknown1095(1000)
    Unknown287(1)
    Unknown450('cmn_bomb_g1')
    Unknown670('01000000e80300000000000000000000')
    Unknown2136('000000000000000000000000f4010000000000003c0000001e000000')
    Unknown2077('ShakeTate', 1000, 0, 20, 3)
    Unknown23(45)

    def upon_90():
        storeValue(2, 51, 0, 1)

    def upon_23():
        storeValue(2, 51, 0, 1)
        beginRecovery()

    def upon_87():
        Unknown23(87)
        storeValue(2, 52, 0, 1)
        ActivateEffScript('cmn_reversal_mazzle', 101)

@State
def jumpkidan1():

    def upon_IMMEDIATE():
        Unknown94(500000)

        def upon_1():
            Unknown633(1, 20)
    sprite('null', 3)
    sprite('explosion', 3)
    callSubroutine('jumpkidan_init')
    Unknown448('bg_stone00', 100)
    makeActive()
    Unknown631('010000004152435f42544c5f434d4e5f4869745f4b646e4c6f6f705f4c5000000000000064000000')
    sprite('null', 2)
    sprite('null', 30)
    ActivateEffScript('jumpkidan2', 100)
    if SLOT_51:
        Unknown1798(1, 23)
    sprite('null', 30)
    Unknown633(1, 30)
    Unknown612('ARC_BTL_CMN_Expl_End')

@State
def jumpkidan2():

    def upon_IMMEDIATE():
        callSubroutine('jumpkidan_init')
        Unknown94(200000)
    sprite('explosion', 3)
    makeActive()
    sprite('null', 2)
    sprite('null', 60)
    ActivateEffScript('jumpkidan3', 100)
    if SLOT_51:
        Unknown1798(1, 23)

@State
def jumpkidan3():

    def upon_IMMEDIATE():
        callSubroutine('jumpkidan_init')
        Unknown94(200000)
    sprite('explosion', 3)
    Unknown448('bg_stone00', 100)
    makeActive()
    sprite('null', 2)
    sprite('null', 60)
    ActivateEffScript('jumpkidan4', 100)
    if SLOT_51:
        Unknown1798(1, 23)

@State
def jumpkidan4():

    def upon_IMMEDIATE():
        callSubroutine('jumpkidan_init')
        Unknown94(200000)
    sprite('explosion', 3)
    makeActive()
    sprite('null', 2)
    sprite('null', 60)
    ActivateEffScript('jumpkidan5', 100)
    if SLOT_51:
        Unknown1798(1, 23)

@State
def jumpkidan5():

    def upon_IMMEDIATE():
        callSubroutine('jumpkidan_init')
        Unknown287(0)
        Unknown94(200000)
    sprite('explosion', 3)
    Unknown448('bg_stone00', 100)
    makeActive()
    sprite('null', 60)

@State
def crouchkidan():

    def upon_IMMEDIATE():
        Unknown243()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        callSubroutine('cmn2DKidan_AtkInit')
        callSubroutine('cmnKidan_Init')
        damage1(400)
        mod_opphitstop(0, -1, -1)
        or_standhit(8)
        airHitPushbackX(30000)
        airHitPushbackY(4000)
        Unknown1208('01000000640000006079feff102700006400000000000000')
        grHitPushbackX(300)
        Unknown831()
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
        Unknown99(30000)
        Unknown164(-15000)
        Unknown2230(102)
        Unknown2229(102)
        Unknown1914(0)
        Unknown450('cmn_kidan_throw')
        Unknown2299(600)
        if SLOT_115:
            airHitPushbackX(15000)
            airHitPushbackY(20000)
            Unknown1208('000000006400000000000000000000006400000000000000')
        Unknown1202('4152435f42544c5f434d4e5f4869745f4b6964616e0000000000000000000000')
        Unknown1119('dammyName')
        Unknown1119('ARC_BTL_CMN_Guard_Kidan')

        def upon_87():
            Unknown23(87)
            ActivateEffScript('cmn_reversalkidan', 100)
            storeValue(2, 52, 0, 1)
            Unknown2208(23)
            Unknown450('')

        def upon_49():
            if Unknown2041('crouchkidan'):
                Unknown23(49)
                Unknown23(3)

                def upon_8():
                    ActivateEffScript('cmn_kidan_end', 100)
    sprite('kidan_nanamesita0', 1)
    makeActive()
    Unknown338(0)
    sprite('kidan_nanamesita', 2)
    Unknown58(1)
    Unknown338(255)
    Unknown202(90000, 0)
    sprite('kidan_nanamesita', 60)
    Unknown450('cmn_kidan')
    label('Koware')
    sprite('null', 10)
    Unknown176(1)
    Unknown450('')

@State
def crouchkidan_start():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('cmn_kidan_throw')
        Unknown1731(50000)
    sprite('null', 3)
    Unknown612('ARC_BTL_CMN_kidan_Chrg')
    sprite('null', 3)
    sprite('null', 3)
    Unknown94(30000)
    Unknown99(50000)

@State
def cen_400StrikeEff00():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown450('cen_400_eff00')
    sprite('null', 3)
    sprite('null', 15)
    Unknown450('cen_400_eff00End')

@State
def cen_400StrikeEff01():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown450('cen_400_eff01')
    sprite('null', 3)
    sprite('null', 15)
    Unknown450('cen_400_eff01End')

@State
def cen_400StrikeEff02():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown450('cen_400_eff02')
    sprite('null', 3)
    sprite('null', 15)
    Unknown450('cen_400_eff02End')

@State
def cen_RollAtkEff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
        Unknown450('cen_401_rollAtk00')
        Unknown99(250000)
    sprite('null', 2147483647)

@State
def cen_RollAtkEffAir():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
        Unknown450('cen_401_rollAtk00')
        Unknown99(250000)
        Unknown165(-45000)
    sprite('null', 2147483647)

@State
def cen401_AddEff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 4)
    Unknown450('cen_401_AddAtk00')
    sprite('null', 12)
    Unknown450('cen_401_AddAtk01')
    Unknown457(0)
    Unknown454(0)

@State
def kamehameha_tame():

    def upon_IMMEDIATE():

        def upon_3():
            if Unknown2033(3, 'CmnActMikiwameMove'):
                Unknown19(23)
        Unknown458(2)
        Unknown454(2)
        Unknown450('cen_403_tame00')
    sprite('null', 2)
    Unknown188(300)
    Unknown1731(-50000)
    sprite('null', 2)
    Unknown188(400)
    sprite('null', 2)
    Unknown188(500)
    sprite('null', 2)
    sprite('null', 2)
    Unknown1731(-70000)
    sprite('null', 2)
    Unknown1731(-80000)

@State
def kamehameha_shadow():

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
def VSAir_kamehameha_shadow():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown164(45000)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 600)
    Unknown450('cmn_shadowLine_loop')
    Unknown3()
    label('end')
    sprite('null', 1)
    Unknown3()

@State
def VSLand_kamehameha_shadow():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown164(-25000)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown450('cmn_shadowLine_loop')
    Unknown3()
    label('end')
    sprite('null', 1)
    Unknown3()

@State
def groundSmoke():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown94(150000)
    label('loop')
    sprite('null', 10)
    Unknown448('bg_undersmoke00', 100)
    Unknown3()
    labelEnd('loop')

@State
def Kamehameha_Core():

    def upon_IMMEDIATE():
        Unknown456(3)
        Unknown454(3)
        Unknown289(300)
        Unknown450('cen_403_core00')
        Unknown632('000000004152435f42544c5f43454e5f4b616d6568616d655f466972650000000000000064000000')
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
        Unknown35('2f000000656e640000000000000000000000000000000000000000000000000000000000')

        def upon_35():
            Unknown454(0)
            Unknown456(0)
            Unknown295(1)

        def upon_24():
            Unknown23(24)
            storeValue(2, 45, 0, 0)
            Unknown1803('Kamehameha_Atk', 29)
            if Unknown2033(3, 'Kamehameha'):
                Unknown53(3, 2, 45, 23, 0, 0)
                Unknown1798(3, 25)
            storeValue(2, 47, 0, 1)
            storeValue(2, 51, 0, 1)

            def upon_24():
                Unknown54('00000000020000002f0000000000000001000000')
                if (SLOT_47 >= 4):
                    if Unknown2033(3, 'Kamehameha'):
                        Unknown1798(3, 24)
                elif Unknown2033(3, 'Kamehameha'):
                    Unknown1798(3, 25)

        def upon_3():
            if (not SLOT_46):
                Unknown1804('4b616d6568616d6568615f41746b00000000000000000000000000000000000017000000')
    label('loop')
    sprite('null', 2)
    Unknown54('0000000002000000300000000000000001000000')
    Unknown2279('02000000300000000200000033000000')
    Unknown445('4b616d6568616d6568615f41746b00000000000000000000000000000000000064000000')
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
    ActivateEffScript('Kamehameha_Atk', 100)
    Unknown1803('Kamehameha_Atk', 30)
    if Unknown2033(3, 'Kamehameha'):
        Unknown1798(3, 24)
    Unknown454(0)
    Unknown456(0)
    Unknown294(1)
    sprite('null', 1)
    Unknown32('Kamehameha_Atk')
    sprite('null', 13)
    Unknown450('cen_403_core01')
    sprite('null', 35)
    Unknown633(0, 35)

@State
def Kamehameha_Atk():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkLevel_3_AtkInit')
        callSubroutine('cmnSpecialShot_AtkInit')
        damage1(262)
        Unknown1117(240)
        mod_hitstop(2)
        or_standhit(11)
        or_launchhit(11)
        airHitPushbackX(60000)
        airHitPushbackY(10000)
        Unknown1186('0100000088130000e09304006400000000000000')
        Unknown842(0)
        untech_Override(25)
        Unknown1027(50000000, -350000, 0, 0)
        Unknown716(1)
        Unknown733(1)
        Unknown734(1)
        Unknown1192('100000004152435f42544c5f434d4e5f4869745f4265616d4c6f6f705f4c50000000000000000000')
        Unknown1193('110000004152435f42544c5f434d4e5f4772645f4265616d4c6f6f705f4c50000000000000000000')
        Unknown717('ShakeYoko', 1000, 1, 20, 0)
        Unknown719(1)

        def upon_30():
            airHitPushbackX(120000)
            Unknown1186('0000000000000000000000000000000000000000')
            Unknown842(1)
            Unknown790(0)
            if conditionalunk2499(3, 2, 24):
                makeActive()
            else:
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
        Unknown450('cen_403_naka00')

        def upon_23():
            Unknown23(23)
            ActivateEffScript('Kamehameha_End', 100)
            storeValue(2, 46, 0, 1)
            Unknown53(2, 2, 46, 23, 0, 1)

        def upon_93():
            Unknown53(2, 2, 115, 23, 2, 115)
            Unknown19(23)
            Unknown1798(2, 24)

        def upon_29():
            storeValue(2, 45, 0, 0)

        def upon_90():
            if SLOT_116:
                if Unknown2033(3, 'Kamehameha'):
                    Unknown53(3, 2, 45, 23, 0, 0)

        def upon_8():
            if SLOT_45:
                Unknown1798(2, 23)
            if Unknown2033(3, 'Kamehameha'):
                Unknown53(3, 2, 46, 23, 0, 1)

        def upon_3():
            if conditionalunk2498(2, 2, 47):
                if conditionalunk2499(2, 2, 49):
                    Unknown53(23, 2, 0, 2, 2, 115)
                    if (SLOT_115 <= SLOT_0):
                        Unknown19(23)
            Unknown670('02000000e80300000000000000000000')

        def upon_1():
            if SLOT_46:
                storeValue(2, 46, 0, 0)
                Unknown53(2, 2, 46, 23, 0, 0)
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('cen_403_naka01', 100)
            Unknown633(16, 20)
            Unknown633(17, 20)
    sprite('kamehameha0', 1)
    makeActive()
    Unknown202(100000, 0)
    sprite('kamehameha0', 1)
    Unknown734(0)
    label('loop')
    sprite('kamehameha0', 2)
    Unknown2301(1200)
    sprite('kamehameha0', 2)
    Unknown2301(1000)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def Kamehameha_End():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown457(2)
        Unknown289(60)
        Unknown2036(2, 0)
        Unknown2488('02000000190100000200000019010000')
        Unknown58(1)
        Unknown450('cen_403_end00')

        def upon_3():
            if Unknown51(2):
                Unknown2488('02000000190100000200000019010000')
                Unknown2036(2, 0)

        def upon_1():
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('cen_403_end01', 100)
    label('loop')
    sprite('null', 2)
    Unknown2301(1000)
    sprite('null', 2)
    Unknown2301(1200)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def Kamehameha_Naname_Core():

    def upon_IMMEDIATE():
        Unknown456(3)
        Unknown454(3)
        Unknown164(45000)
        Unknown289(300)
        Unknown450('cen_403_core00')
        Unknown632('000000004152435f42544c5f43454e5f4b616d6568616d655f466972650000000000000064000000')
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
        Unknown35('2f000000656e640000000000000000000000000000000000000000000000000000000000')

        def upon_35():
            Unknown454(0)
            Unknown456(0)
            Unknown295(1)

        def upon_24():
            Unknown23(24)
            storeValue(2, 45, 0, 0)
            Unknown1803('Kamehameha_Naname_Atk', 29)
            if Unknown2033(3, 'Kamehameha_Naname'):
                Unknown53(3, 2, 45, 23, 0, 0)
                Unknown1798(3, 25)
            storeValue(2, 47, 0, 1)
            storeValue(2, 51, 0, 1)

            def upon_24():
                Unknown54('00000000020000002f0000000000000001000000')
                if (SLOT_47 >= 4):
                    if Unknown2033(3, 'Kamehameha_Naname'):
                        Unknown1798(3, 24)
                elif Unknown2033(3, 'Kamehameha_Naname'):
                    Unknown1798(3, 25)

        def upon_3():
            if (not SLOT_46):
                Unknown1804('4b616d6568616d6568615f4e616e616d655f41746b000000000000000000000017000000')
    label('loop')
    sprite('null', 2)
    Unknown54('0000000002000000300000000000000001000000')
    Unknown2279('02000000300000000200000033000000')
    Unknown445('4b616d6568616d6568615f4e616e616d655f41746b000000000000000000000064000000')
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
    ActivateEffScript('Kamehameha_Naname_Atk', 100)
    Unknown1803('Kamehameha_Naname_Atk', 30)
    if Unknown2033(3, 'Kamehameha_Naname'):
        Unknown1798(3, 24)
    Unknown454(0)
    Unknown456(0)
    Unknown454(0)
    Unknown294(1)
    sprite('null', 1)
    Unknown32('Kamehameha_Naname_Atk')
    sprite('null', 13)
    Unknown450('cen_403_core01')
    sprite('null', 35)
    Unknown633(0, 35)

@State
def Kamehameha_Naname_Atk():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkLevel_3_AtkInit')
        callSubroutine('cmnSpecialShot_AtkInit')
        damage1(280)
        Unknown1117(240)
        mod_hitstop(2)
        or_standhit(12)
        or_launchhit(12)
        airHitPushbackX(15000)
        airHitPushbackY(25000)
        untech_Override(35)
        Unknown1027(50000000, -240000, 0, 0)
        Unknown716(1)
        Unknown733(1)
        Unknown734(1)
        Unknown1192('100000004152435f42544c5f434d4e5f4869745f4265616d4c6f6f705f4c50000000000000000000')
        Unknown1193('110000004152435f42544c5f434d4e5f4772645f4265616d4c6f6f705f4c50000000000000000000')
        Unknown717('ShakeYoko', 1000, 1, 20, 0)
        Unknown719(1)

        def upon_30():
            airHitPushbackX(30000)
            airHitPushbackY(45000)
            Unknown1186('0000000000000000000000000000000000000000')
            if conditionalunk2499(3, 2, 24):
                makeActive()
            else:
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
        Unknown450('cen_403_naka00')

        def upon_23():
            Unknown23(23)
            ActivateEffScript('Kamehameha_Naname_End', 100)
            storeValue(2, 46, 0, 1)
            Unknown53(2, 2, 46, 23, 0, 1)

        def upon_93():
            Unknown53(2, 2, 115, 23, 2, 115)
            Unknown19(23)
            Unknown1798(2, 24)

        def upon_29():
            storeValue(2, 45, 0, 0)

        def upon_90():
            if SLOT_116:
                if Unknown2033(3, 'Kamehameha_Naname'):
                    Unknown53(3, 2, 45, 23, 0, 0)

        def upon_8():
            if SLOT_45:
                Unknown1798(2, 23)
                if Unknown2033(3, 'Kamehameha_Naname'):
                    Unknown53(3, 2, 46, 23, 0, 1)

        def upon_3():
            if conditionalunk2498(2, 2, 47):
                if conditionalunk2499(2, 2, 49):
                    Unknown53(23, 2, 0, 2, 2, 115)
                    if (SLOT_115 <= SLOT_0):
                        Unknown19(23)

        def upon_1():
            if SLOT_46:
                storeValue(2, 46, 0, 0)
                Unknown53(2, 2, 46, 23, 0, 0)
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('cen_403_naka01', 100)
            Unknown633(16, 20)
            Unknown633(17, 20)
    sprite('kamehameha1', 1)
    Unknown1186('010000003057050090d003006400000000000000')
    makeActive()
    Unknown202(100000, 0)
    sprite('kamehameha1', 1)
    Unknown734(0)
    sprite('kamehameha1', 2)
    Unknown1186('010000007064080090d003006400000000000000')
    Unknown2301(1200)
    sprite('kamehameha1', 2)
    Unknown1186('01000000b0710b0090d003006400000000000000')
    Unknown2301(1000)
    sprite('kamehameha1', 2)
    Unknown1186('01000000f07e0e0090d003006400000000000000')
    Unknown2301(1200)
    sprite('kamehameha1', 2)
    Unknown1186('01000000308c110090d003006400000000000000')
    Unknown2301(1000)
    sprite('kamehameha1', 2)
    Unknown1186('010000007099140090d003006400000000000000')
    Unknown2301(1200)
    label('loop')
    sprite('kamehameha1', 2)
    Unknown2301(1200)
    sprite('kamehameha1', 2)
    Unknown2301(1000)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def Kamehameha_Naname_End():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown457(2)
        Unknown164(45000)
        Unknown289(60)
        Unknown2036(2, 0)
        Unknown2488('02000000190100000200000019010000')
        Unknown58(1)
        Unknown450('cen_403_end00')

        def upon_3():
            if Unknown51(2):
                Unknown2488('02000000190100000200000019010000')
                Unknown2036(2, 0)

        def upon_1():
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('cen_403_end01', 100)
    label('loop')
    sprite('null', 2)
    Unknown2301(1000)
    sprite('null', 2)
    Unknown2301(1200)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def Airkamehameha_tame():

    def upon_IMMEDIATE():

        def upon_3():
            if Unknown2033(3, 'CmnActMikiwameMove'):
                Unknown19(23)
        Unknown458(2)
        Unknown454(2)
        Unknown450('cen_403_tame00')
    sprite('null', 2)
    Unknown188(300)
    Unknown1731(-75000)
    sprite('null', 2)
    Unknown188(400)
    sprite('null', 2)
    Unknown188(500)
    sprite('null', 2)
    sprite('null', 2)
    sprite('null', 2)

@State
def Airkamehameha_tame_Assist():

    def upon_IMMEDIATE():

        def upon_3():
            if Unknown2033(3, 'CmnActMikiwameMove'):
                Unknown19(23)
        Unknown458(2)
        Unknown454(2)
        Unknown450('cen_kmhm_tame_Assist')
    sprite('null', 2)
    Unknown188(300)
    Unknown1732(-160000)
    sprite('null', 2)
    Unknown188(400)
    sprite('null', 2)
    Unknown188(500)
    sprite('null', 2)
    sprite('null', 2)
    sprite('null', 10)

@State
def AirKamehameha_Naname_Core():

    def upon_IMMEDIATE():
        Unknown456(3)
        Unknown454(3)
        Unknown164(-25000)
        Unknown289(300)
        Unknown450('cen_403_core00')
        Unknown632('000000004152435f42544c5f43454e5f4b616d6568616d655f466972650000000000000064000000')
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
        Unknown35('2f000000656e640000000000000000000000000000000000000000000000000000000000')

        def upon_35():
            Unknown454(0)
            Unknown456(0)
            Unknown295(1)

        def upon_24():
            Unknown23(24)
            storeValue(2, 45, 0, 0)
            Unknown1803('AirKamehameha_Naname_Atk', 29)
            if Unknown2033(3, 'AirKamehameha_Naname'):
                Unknown53(3, 2, 45, 23, 0, 0)
                Unknown1798(3, 25)
            if Unknown2033(3, 'AssistAttack'):
                Unknown53(3, 2, 45, 23, 0, 0)
            storeValue(2, 47, 0, 1)
            storeValue(2, 51, 0, 1)

            def upon_24():
                Unknown54('00000000020000002f0000000000000001000000')
                if (SLOT_47 >= 4):
                    if Unknown2033(3, 'AirKamehameha_Naname'):
                        Unknown1798(3, 24)
                    if Unknown2033(3, 'AssistAttack'):
                        Unknown1798(3, 24)
                elif Unknown2033(3, 'AirKamehameha_Naname'):
                    Unknown1798(3, 25)

        def upon_3():
            if (not SLOT_46):
                Unknown1804('4169724b616d6568616d6568615f4e616e616d655f41746b000000000000000017000000')
    label('loop')
    sprite('null', 2)
    Unknown54('0000000002000000300000000000000001000000')
    Unknown2279('02000000300000000200000033000000')
    Unknown445('4169724b616d6568616d6568615f4e616e616d655f41746b000000000000000064000000')
    if (SLOT_45 >= 3):
        Unknown53(1, 2, 45, 23, 0, 1)
    if (not SLOT_50):
        storeValue(2, 50, 0, 1)
        Unknown53(1, 2, 50, 23, 0, 1)
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
    ActivateEffScript('AirKamehameha_Naname_Atk', 100)
    Unknown1803('AirKamehameha_Naname_Atk', 30)
    if Unknown2033(3, 'AirKamehameha_Naname'):
        Unknown1798(3, 24)
    if Unknown2033(3, 'AssistAttack'):
        Unknown1798(3, 24)
    Unknown456(0)
    Unknown454(0)
    Unknown294(1)
    sprite('null', 1)
    Unknown32('AirKamehameha_Naname_Atk')
    sprite('null', 13)
    Unknown450('cen_403_core01')
    sprite('null', 35)
    Unknown633(0, 35)

@State
def AirKamehameha_Naname_Atk():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkLevel_3_AtkInit')
        callSubroutine('cmnSpecialShot_AtkInit')
        damage1(262)
        Unknown1117(240)
        callSubroutine('cmn_AssistShotHosei')
        mod_hitstop(0)
        mod_opphitstop(2, 0, 0)
        or_standhit(8)
        or_launchhit(8)
        airHitPushbackX(5000)
        airHitPushbackY(10000)
        Unknown842(0)
        untech_Override(25)
        Unknown1208('0100000064000000c0f2fcff50c300006400000000000000')
        Unknown1027(50000000, -325000, 0, 0)
        Unknown716(1)
        Unknown733(1)
        Unknown734(1)
        Unknown854(1)
        Unknown802(100)
        Unknown808(8000)
        Unknown806(40000)
        Unknown1192('100000004152435f42544c5f434d4e5f4869745f4265616d4c6f6f705f4c50000000000000000000')
        Unknown1193('110000004152435f42544c5f434d4e5f4772645f4265616d4c6f6f705f4c50000000000000000000')
        Unknown717('ShakeYoko', 1000, 1, 20, 0)
        Unknown719(1)

        def upon_30():
            or_standhit(12)
            or_launchhit(12)
            airHitPushbackX(25000)
            airHitPushbackY(35000)
            mod_opphitstop(2, 5, 5)
            Unknown1208('000000006400000000000000000000000000000000000000')
            Unknown854(0)
            if conditionalunk2499(3, 2, 24):
                makeActive()
            else:
                beginRecovery()
            if conditionalunk2500(12, 2, 2, 47, 0, 4):
                beginRecovery()
        if Unknown2033(3, 'AssistAttack'):
            damage1(200)
            untech_Override(33)
        Unknown456(2)
        Unknown454(2)
        Unknown457(2)
        Unknown453(2)
        Unknown289(60)
        Unknown1954(1)
        Unknown58(1)
        Unknown450('cen_403_naka00')

        def upon_23():
            Unknown23(23)
            ActivateEffScript('AirKamehameha_Naname_End', 100)
            storeValue(2, 46, 0, 1)
            Unknown53(2, 2, 46, 23, 0, 1)

        def upon_93():
            Unknown53(2, 2, 115, 23, 2, 115)
            Unknown19(23)
            Unknown1798(2, 24)

        def upon_29():
            storeValue(2, 45, 0, 0)

        def upon_90():
            if SLOT_116:
                if Unknown2033(3, 'AirKamehameha_Naname'):
                    Unknown53(3, 2, 45, 23, 0, 0)

        def upon_8():
            if SLOT_45:
                Unknown1798(2, 23)
                if Unknown2033(3, 'AirKamehameha_Naname'):
                    Unknown53(3, 2, 46, 23, 0, 1)

        def upon_3():
            if conditionalunk2498(2, 2, 47):
                if conditionalunk2499(2, 2, 49):
                    Unknown53(23, 2, 0, 2, 2, 115)
                    if (SLOT_115 <= SLOT_0):
                        Unknown19(23)
            if (SLOT_18 <= 0):
                if SLOT_50:
                    Unknown23(3)
                    Unknown2193(123, 400000, 0)
                    Unknown448('bg_groundsmokeS', 130)
                    Unknown2193(123, -400000, 0)
                    Unknown2277(1)
                    Unknown449('bg_groundsmokeS', 130)
                    Unknown670('00000000e80300000000000000000000')

        def upon_1():
            if SLOT_46:
                storeValue(2, 46, 0, 0)
                Unknown53(2, 2, 46, 23, 0, 0)
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('cen_403_naka01', 100)
            Unknown633(16, 20)
            Unknown633(17, 20)
    sprite('kamehameha_nanamesita', 1)
    makeActive()
    Unknown202(100000, 0)
    sprite('kamehameha_nanamesita', 1)
    Unknown734(0)
    label('loop')
    sprite('kamehameha_nanamesita', 2)
    Unknown2301(1200)
    sprite('kamehameha_nanamesita', 2)
    Unknown2301(1000)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def AirKamehameha_Naname_End():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown457(2)
        Unknown164(-25000)
        Unknown289(60)
        Unknown2036(2, 0)
        Unknown2488('02000000190100000200000019010000')
        Unknown58(1)
        Unknown450('cen_403_end00')

        def upon_3():
            if Unknown51(2):
                Unknown2488('02000000190100000200000019010000')
                Unknown2036(2, 0)

        def upon_1():
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('cen_403_end01', 100)
    label('loop')
    sprite('null', 2)
    Unknown2301(1000)
    sprite('null', 2)
    Unknown2301(1200)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def __214D_Attack():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkTemplNageLand')
        callSubroutine('cmnSpecialShot_AtkInit')
        Unknown1027(200000, -200000, 450000, 0)
        Unknown1028(2)
        damage1(150)
        Unknown1117(200)
        mod_hitstop(9)
        Unknown1095(500)
        Unknown1019(0)
        Unknown1157(0)
        Unknown1075(0)
        Unknown1142(0)
        callSubroutine('cmn_KuzushiHosei')
        or_standhit(8)
        airHitPushbackX(0)
        airHitPushbackY(35000)
        Unknown778(1500)
        untech_Override(60)
        Unknown1064('323134445f41747461636b000000000000000000000000000000000000000000')
        Unknown717('ShakeYoko', 1000, 1, 20, 0)
        Unknown1118('dammyName')
        Unknown1119('ARC_BTL_CMN_Guard_Beam')
        Unknown457(2)
        Unknown287(1)

        def upon_89():
            Unknown23(89)
            Unknown23(23)
            Unknown2040(3, 'Psychokinesis_Hit', 0)
            Unknown1803('214D_YugamiEff', 23)
            if (not SLOT_283):
                storeValue(2, 286, 0, 1)
            storeValue(2, 283, 0, 1)

        def upon_3():
            if (not SLOT_16):
                Unknown1915()
            if SLOT_266:
                Unknown1915()
        Unknown35('17000000456e640000000000000000000000000000000000000000000000000000000000')
        Unknown35('1800000041746b0000000000000000000000000000000000000000000000000000000000')
        Unknown35('1900000046696e6973680000000000000000000000000000000000000000000000000000')
        if (SLOT_104 >= 1000000):
            Unknown2036(32, 104)
        else:
            Unknown94(800000)
    sprite('psychokinesisclash', 1)
    makeActive()
    Unknown615('ARC_BTL_CEN_Psychknss_Atk1')
    sprite('psychokinesisclash', 2)
    ActivateEffScript('214D_YugamiEff', 100)
    sprite('null', 100)
    Unknown1915()
    Unknown18()
    label('Atk')
    sprite('psychokinesisclash', 7)
    Unknown23(3)
    Unknown23(24)
    Unknown2036(32, 100)
    Unknown1108(45)
    Unknown1027(0, 0, 0, 0)
    mod_hitstop(1)
    airHitPushbackX(0)
    airHitPushbackY(0)
    Unknown778(0)
    Unknown1095(0)
    makeActive()
    Unknown1045('02000000323134445f536c61736845666600000000000000000000000000000000000000')
    Unknown615('ARC_BTL_CEN_Psychknss_Atk2')
    sprite('psychokinesisclash', 7)
    makeActive()
    Unknown1045('02000000323134445f536c61736845666632000000000000000000000000000000000000')
    sprite('psychokinesisclash', 7)
    Unknown1108(0)
    makeActive()
    Unknown1045('02000000323134445f536c61736845666600000000000000000000000000000000000000')
    sprite('psychokinesisclash', 7)
    Unknown1108(45)
    makeActive()
    Unknown1045('02000000323134445f536c61736845666632000000000000000000000000000000000000')
    sprite('psychokinesisclash', 7)
    makeActive()
    Unknown1045('02000000323134445f536c61736845666600000000000000000000000000000000000000')
    sprite('psychokinesisclash', 7)
    makeActive()
    Unknown1045('02000000323134445f536c61736845666632000000000000000000000000000000000000')
    sprite('psychokinesisclash', 7)
    Unknown1108(0)
    makeActive()
    Unknown1045('02000000323134445f536c61736845666600000000000000000000000000000000000000')
    sprite('null', 60)
    label('Finish')
    sprite('psychokinesisclash', 2)
    Unknown1108(0)
    damage1(800)
    airHitPushbackX(60000)
    airHitPushbackY(15000)
    Unknown779()
    or_standhit(8)
    or_launchhit(8)
    untech_Override(40)
    Unknown1059(0)
    Unknown1045('000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1197(1)
    Unknown1064('0000000000000000000000000000000000000000000000000000000000000000')
    Unknown1954(1)
    makeActive()
    Unknown615('ARC_BTL_CEN_Psychknss_Atk3')
    label('End')
    sprite('null', 10)
    Unknown23(89)
    Unknown23(23)
    Unknown23(24)
    Unknown23(25)
    Unknown1803('214D_YugamiEff', 23)

@State
def __214D_YugamiEff():

    def upon_IMMEDIATE():
        Unknown450('cen_404Eff00')
        Unknown457(2)
        Unknown454(2)
        Unknown450('cen_406_loop')
        Unknown99(300000)
        Unknown35('17000000456e640000000000000000000000000000000000000000000000000000000000')
        Unknown289(200)
    sprite('null', 2147483647)
    Unknown448('cen_406_aura', 100)
    label('End')
    sprite('null', 10)
    Unknown2273(0, 600)
    Unknown449('cen_406_aura', 100)
    Unknown454(0)
    Unknown457(0)
    Unknown191(-80)
    Unknown341(-13)
    Unknown3()

@State
def __214D_SlashEff():

    def upon_IMMEDIATE():
        Unknown450('cen_404Eff00')
        Unknown450('cen_406_Line')
        Unknown164(30000)
        Unknown169(-1500, 1500)
    sprite('null', 40)
    Unknown448('cen_406_aura', 100)

@State
def __214D_SlashEff2():

    def upon_IMMEDIATE():
        Unknown450('cen_404Eff00')
        Unknown450('cen_406_Line')
        Unknown164(120000)
        Unknown232(180000)
        Unknown169(-1500, 1500)
        Unknown239()
    sprite('null', 40)
    Unknown448('cen_406_aura', 100)

@State
def energyfield_Tame():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('cen_430_Tame')
        Unknown294(1)
    sprite('null', 2147483647)

@State
def energyfield_BodyAura():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('cen_430_bodyAura')
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown632('000000004152435f42544c5f43454e5f456e657267794669656c645f466972650000000064000000')
    label('end')
    sprite('null', 10)
    Unknown454(0)
    Unknown457(0)
    sprite('null', 20)
    Unknown450('cen_430_bodyAuraEnd')
    sprite('null', 20)
    Unknown633(0, 30)
    Unknown3()

@State
def energyfield_atk():

    def upon_IMMEDIATE():
        Unknown245()
        callSubroutine('cmnAtkLevel_4_AtkInit')
        callSubroutine('cmnUltimateShot_AtkInit')
        damage1(450)
        Unknown1086(30)
        mod_hitstop(2)
        mod_opphitstop(0, 5, 5)
        airHitPushbackX(40000)
        airHitPushbackY(45000)
        untech_Override(45)
        grHitPushbackX(150)
        or_standhit(12)
        or_launchhit(12)
        Unknown1192('100000004152435f42544c5f434d4e5f4869745f4265616d4c6f6f705f4c50000000000000000000')
        Unknown1193('110000004152435f42544c5f434d4e5f4772645f4265616d4c6f6f705f4c50000000000000000000')
        Unknown454(2)
        Unknown456(2)
        Unknown457(2)
        Unknown450('cen_430_bariya')

        def upon_23():
            Unknown23(23)
            Unknown2193(123, 400000, 0)
            Unknown2273(0, 800)
            Unknown449('bg_groundsmokeL', 130)
            Unknown2193(123, -400000, 0)
            Unknown2277(1)
            Unknown2273(0, 800)
            Unknown449('bg_groundsmokeL', 130)
            Unknown670('01000000102700000000000000000000')

        def upon_90():
            callSubroutine('cmnUltimate_CameraCombo')

        def upon_3():
            if (not 
            Unknown53(23, 2, 0, 22, 2, 36)):
                Unknown633(16, 20)
                Unknown633(17, 20)

        def upon_1():
            Unknown633(16, 20)
            Unknown633(17, 20)
    sprite('energyfield', 3)
    makeActive()
    Unknown188(1000)
    Unknown2299(2000)
    sprite('energyfield', 3)
    makeActive()
    Unknown188(1200)
    sprite('energyfield', 3)
    makeActive()
    Unknown188(1400)
    sprite('energyfield', 3)
    makeActive()
    Unknown188(1600)
    sprite('energyfield', 3)
    makeActive()
    Unknown188(1800)
    sprite('energyfield', 3)
    makeActive()
    mod_opphitstop(0, 10, 10)
    untech_Override(35)
    Unknown188(2000)
    sprite('null', 30)
    Unknown450('cen_430_bariyaEnd')
    Unknown454(0)
    Unknown456(0)
    Unknown457(0)
    Unknown295(1)
    Unknown633(16, 20)
    Unknown633(17, 20)
    sprite('null', 30)
    Unknown23(1)

@State
def SDestroy_Kamehameha_tame():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown450('cmn_kidan_throw')
        Unknown294(1)
    sprite('null', 80)
    Unknown3()

@State
def SDestroy_Kamehameha_BodyAura():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown457(2)
        Unknown458(2)
        Unknown454(2)
        Unknown455(3)
        Unknown188(1500)
        Unknown1955('636d6e5f5361757261596f6b6f5f6c6f6f700000000000000000000000000000')
        Unknown35('17000000456e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    label('End')
    sprite('null', 30)
    Unknown450('cmn_SauraYoko_end')
    Unknown3()

@State
def SDestroy_Kamehameha_Core():

    def upon_IMMEDIATE():
        Unknown456(3)
        Unknown454(3)
        Unknown289(300)
        Unknown450('cen_431_core00')
        Unknown294(1)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
        Unknown35('2f000000656e640000000000000000000000000000000000000000000000000000000000')

        def upon_35():
            Unknown454(0)
            Unknown456(0)
            Unknown295(1)

        def upon_24():
            Unknown23(24)
            storeValue(2, 45, 0, 0)
            Unknown1803('SDestroy_Kamehameha_Atk', 29)
            if Unknown2033(3, 'SDestroy_Kamehameha'):
                Unknown53(3, 2, 45, 23, 0, 0)
                Unknown1798(3, 25)
            storeValue(2, 47, 0, 1)
            storeValue(2, 51, 0, 1)

            def upon_24():
                Unknown54('00000000020000002f0000000000000001000000')
                if (SLOT_47 >= 16):
                    if Unknown2033(3, 'SDestroy_Kamehameha'):
                        Unknown1798(3, 24)
                elif Unknown2033(3, 'SDestroy_Kamehameha'):
                    Unknown1798(3, 25)

        def upon_3():
            if (not SLOT_46):
                Unknown1804('5344657374726f795f4b616d6568616d6568615f41746b00000000000000000017000000')
    label('loop')
    sprite('null', 2)
    Unknown54('0000000002000000300000000000000001000000')
    Unknown2279('02000000300000000200000033000000')
    Unknown445('5344657374726f795f4b616d6568616d6568615f41746b00000000000000000064000000')
    if (SLOT_45 <= 12):
        Unknown41(1)
        Unknown1199(1, 0)
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
    ActivateEffScript('SDestroy_Kamehameha_Atk', 100)
    Unknown1803('SDestroy_Kamehameha_Atk', 30)
    if Unknown2033(3, 'SDestroy_Kamehameha'):
        Unknown1798(3, 24)
    Unknown454(0)
    Unknown456(0)
    Unknown294(1)
    sprite('null', 1)
    Unknown32('SDestroy_Kamehameha_Atk')
    sprite('null', 10)
    Unknown450('cen_431_core01')
    sprite('null', 20)

@State
def SDestroy_Kamehameha_Atk():

    def upon_IMMEDIATE():
        Unknown245()
        callSubroutine('cmnAtkLevel_4_AtkInit')
        callSubroutine('cmnUltimateShot_AtkInit')
        damage1(220)
        Unknown1086(37)
        Unknown1095(500)
        mod_hitstop(2)
        or_standhit(11)
        or_launchhit(11)
        airHitPushbackX(60000)
        airHitPushbackY(10000)
        grHitPushbackX(10)
        Unknown1186('0100000010270000400d03006400000000000000')
        Unknown842(0)
        untech_Override(60)
        Unknown1027(50000000, -500000, 0, 0)
        Unknown1187(0)
        Unknown736(1)
        Unknown716(1)
        Unknown733(1)
        Unknown734(1)
        Unknown1191(1)
        Unknown1192('100000004152435f42544c5f434d4e5f4869745f4265616d4c6f6f705f4c50000000000000000000')
        Unknown1193('110000004152435f42544c5f434d4e5f4772645f4265616d4c6f6f705f4c50000000000000000000')
        Unknown719(1)

        def upon_30():
            or_standhit(12)
            or_launchhit(12)
            damage1(360)
            airHitPushbackX(40000)
            airHitPushbackY(38000)
            Unknown1186('0000000000000000000000006400000000000000')
            Unknown1064('436d6e4e65757472616c00000000000000000000000000000000000000000000')
            if conditionalunk2499(3, 2, 24):
                makeActive()
            else:
                beginRecovery()
            if conditionalunk2500(12, 2, 2, 47, 0, 16):
                beginRecovery()
        Unknown456(2)
        Unknown454(2)
        Unknown457(2)
        Unknown453(2)
        Unknown289(60)
        Unknown1954(1)
        Unknown58(1)
        Unknown450('cen_431_naka00')

        def upon_23():
            Unknown23(23)
            ActivateEffScript('SDestroy_Kamehameha_End', 100)
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
                if Unknown2033(3, 'SDestroy_Kamehameha'):
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
            Unknown670('03000000e80300000000000000000000')
            if (not 
            Unknown53(23, 2, 0, 22, 2, 36)):
                Unknown633(16, 20)
                Unknown633(17, 20)
            if (not 
            Unknown2033(3, 'SDestroy_Kamehameha')):
                Unknown633(16, 20)
                Unknown633(17, 20)

        def upon_1():
            if SLOT_46:
                storeValue(2, 46, 0, 0)
                Unknown53(2, 2, 46, 23, 0, 0)
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('cen_431_naka01', 100)
    sprite('sdestroy_Kamehameha', 1)
    makeActive()
    Unknown202(100000, 0)
    sprite('sdestroy_Kamehameha', 1)
    Unknown734(0)
    label('loop')
    sprite('sdestroy_Kamehameha', 2)
    Unknown2301(1200)
    sprite('sdestroy_Kamehameha', 2)
    Unknown2301(1000)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def SDestroy_Kamehameha_End():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown457(2)
        Unknown289(60)
        Unknown2036(2, 0)
        Unknown2488('02000000190100000200000019010000')
        Unknown58(1)
        Unknown450('cen_431_end00')

        def upon_3():
            if Unknown51(2):
                Unknown2488('02000000190100000200000019010000')
                Unknown2036(2, 0)

        def upon_1():
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('cen_431_end01', 100)
    label('loop')
    sprite('null', 2)
    Unknown2301(1000)
    sprite('null', 2)
    Unknown2301(1200)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def SDestroy_Kamehameha_CSBodyAura():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown99(32500)
    sprite('null', 60)
    Unknown1955('63656e5f3433315f4353426f6479417572610000000000000000000000000000')
    Unknown338(0)
    sprite('null', 40)
    Unknown338(255)
    sprite('null', 38)
    Unknown189(800)
    sprite('null', 2147483647)
    Unknown189(3400)

@State
def SDestroy_Kamehameha_CSTameSpher():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown454(2)
        Unknown457(2)
    sprite('null', 2147483647)
    Unknown450('cen_431_tame')

@State
def groundSmoke_EXtame():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown454(2)
        Unknown458(2)
    label('loop')
    sprite('null', 10)
    Unknown2273(0, 1200)
    Unknown449('bg_undersmoke00', 100)
    Unknown3()
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
    Unknown2076('063cfeffff970300adc80000cf0f0000c21b00000000000048000000000000005a0000001e00000001000000')
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def FinishCamera_TKamehameha():

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
def cen600Flash():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown450('cen600_scrFlash')
    sprite('null', 6)
    Unknown3()

@State
def cen600Eff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown450('cen600_scranime')
    sprite('null', 60)
    Unknown3()

@State
def cen600BodyAura():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown232(-450000)
        Unknown1955('636d6e5f53617572615f6c6f6f70000000000000000000000000000000000000')
        Unknown35('170000004d6f766500000000000000000000000000000000000000000000000000000000')
    sprite('null', 8)
    Unknown188(2000)
    sprite('null', 4)
    Unknown188(1500)
    sprite('null', 2147483647)
    Unknown188(1000)
    Unknown3()
    label('Move')
    sprite('null', 2147483647)
    ActivateEffScript('cen600BodyAuraDust', 100)
    Unknown94(-350000)
    Unknown1732(-400000)
    Unknown99(80000)
    Unknown232(450000)
    Unknown188(1200)
    Unknown3()

@State
def cen600BodyAuraDust():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown1955('63656e3630305f61757261647573740000000000000000000000000000000000')
        Unknown188(80)
    sprite('null', 2147483647)
    Unknown99(215000)
    Unknown94(400000)
    Unknown1732(450000)
    Unknown3()

@State
def cencs600_groundsmoke():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown454(2)
        Unknown457(2)
        Unknown94(-300000)
    label('loop')
    sprite('null', 10)
    Unknown2273(0, 1500)
    Unknown2283(0, 75000)
    Unknown449('bg_undersmoke00', 100)
    labelEnd('loop')

@State
def cencs600_groundsmoke2():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown454(2)
        Unknown457(2)
        Unknown94(-300000)
    label('loop')
    sprite('null', 10)
    Unknown2273(0, 1500)
    Unknown2283(0, -75000)
    Unknown449('bg_undersmoke00', 100)
    labelEnd('loop')

@State
def cencs600_Speed():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('cen_600_speed')
    sprite('null', 2147483647)

@State
def cencs600_ShockLoop():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('cen_600_shocking')
        Unknown94(-170000)
    sprite('null', 4)
    Unknown188(600)
    sprite('null', 4)
    Unknown188(800)
    ActivateEffScript('cen600_RockMatome', 100)
    sprite('null', 12)
    Unknown188(1000)
    ActivateEffScript('cen600_RockMatome2', 100)
    sprite('null', 5)
    ActivateEffScript('cencs600_smokeLoop1', 100)
    ActivateEffScript('cencs600_smokeLoop2', 100)
    sprite('null', 2147483647)
    ActivateEffScript('cencs600_MoveSmoke', 100)

@State
def cencs600_smokeLoop1():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown94(510000)
        Unknown1732(190000)
    label('loop')
    sprite('null', 10)
    Unknown2273(0, 1500)
    Unknown2283(0, -95000)
    Unknown449('bg_undersmoke00', 100)
    Unknown3()
    labelEnd('loop')

@State
def cencs600_smokeLoop2():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown94(510000)
        Unknown1732(-10000)
    label('loop')
    sprite('null', 10)
    Unknown2273(0, 1500)
    Unknown2283(0, 95000)
    Unknown449('bg_undersmoke00', 100)
    Unknown3()
    labelEnd('loop')

@State
def cencs600_MoveSmoke():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown232(450000)
        Unknown1955('62675f736d6f6b654c6f6f703030000000000000000000000000000000000000')
        Unknown94(-100000)
        Unknown99(-300000)
    sprite('null', 5)
    physicsImpulseY(50000)
    physicsImpulseX(25000)
    sprite('null', 25)
    physicsImpulseY(0)
    sprite('null', 2147483647)
    physicsImpulseX(75000)

@State
def cen600_RockMatome():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
        Unknown94(680000)
        Unknown1732(100000)
    sprite('null', 60)
    ActivateEffScript('cen600_Rock', 100)
    Unknown41(1)
    Unknown94(150000)
    Unknown1732(200000)
    Unknown99(75000)
    Unknown40()
    ActivateEffScript('cen600_Rock', 100)
    Unknown41(1)
    Unknown94(-150000)
    Unknown1732(300000)
    Unknown99(300000)
    Unknown188(3000)
    Unknown40()
    ActivateEffScript('cen600_Rock', 100)
    Unknown41(1)
    Unknown94(150000)
    Unknown1732(-200000)
    Unknown99(50000)
    Unknown40()
    ActivateEffScript('cen600_Rock', 100)
    Unknown41(1)
    Unknown94(-150000)
    Unknown1732(-300000)
    Unknown99(250000)
    Unknown188(3000)
    Unknown40()

@State
def cen600_RockMatome2():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
        Unknown94(170000)
        Unknown99(250000)
    sprite('null', 60)
    ActivateEffScript('cen600_Rock', 100)
    Unknown41(1)
    Unknown1732(250000)
    Unknown99(300000)
    Unknown188(3000)
    Unknown40()
    ActivateEffScript('cen600_Rock', 100)
    Unknown41(1)
    Unknown1732(400000)
    Unknown99(75000)
    Unknown40()
    ActivateEffScript('cen600_Rock', 100)
    Unknown41(1)
    Unknown1732(-250000)
    Unknown99(300000)
    Unknown188(3000)
    Unknown40()
    ActivateEffScript('cen600_Rock', 100)
    Unknown41(1)
    Unknown1732(-250000)
    Unknown99(75000)
    Unknown40()

@State
def cen600_Rock():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('bg_debris00')
        Unknown188(2000)
        Unknown166(250)
        Unknown118(100, 500)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    label('loop')
    sprite('null', 2)
    Unknown1732(500)
    sprite('null', 2)
    Unknown1732(-500)
    Unknown3()
    labelEnd('loop')

@State
def cencs600_WipeSmoke():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown1955('62675f736d6f6b654c6f6f703030000000000000000000000000000000000000')
        Unknown99(350000)
        Unknown1732(125000)
        Unknown188(300)
    sprite('null', 30)
    physicsImpulseX(7500)
    physicsImpulseY(-1250)

@State
def cencs600_HimoSmoke():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown1955('62675f68696d6f736d6f6b653030000000000000000000000000000000000000')
        Unknown99(385000)
        Unknown188(450)
        Unknown164(-20000)
    sprite('null', 240)
    physicsImpulseY(-25)

@State
def cencs600_HimoSmoke2():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown1955('62675f68696d6f736d6f6b653030000000000000000000000000000000000000')
        Unknown99(420000)
        Unknown188(450)
        Unknown164(-20000)
    sprite('null', 240)
    physicsImpulseY(25)

@State
def DUMMYDUMMY():
    sprite('null', 1)