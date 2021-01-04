@State
def dmy():
    sprite('null', 1)

@State
def okasi():

    def upon_IMMEDIATE():
        callSubroutine('cmn_okasi')
    sprite('null', 2147483647)
    Unknown450('gks_okasi')

@State
def GKS_5CEff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 60)
    Unknown450('gks_262EFF10')

@State
def GKS_2CEff():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown164(62500)
        Unknown99(350000)
        Unknown94(125000)
    sprite('null', 60)
    Unknown450('cmn_strike00')

@State
def kidan_start():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown457(2)
        ActivateEffScript('kidan_start_aura', 100)

        def upon_12():
            Unknown2036(2, 0)
    sprite('null', 3)
    Unknown1731(0)
    sprite('null', 1)
    Unknown1731(0)
    sprite('null', 2)
    Unknown612('ARC_BTL_CMN_kidan_Chrg')
    sprite('null', 3)
    Unknown1731(-20000)
    sprite('null', 3)
    Unknown1731(100000)

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
def kidan_renda_start():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown457(2)
        Unknown454(2)
        ActivateEffScript('kidan_renda_start_aura', 100)
    sprite('null', 3)
    Unknown1731(-150000)
    Unknown94(30000)
    sprite('null', 3)
    Unknown94(120000)
    Unknown99(-20000)
    Unknown1731(-100000)

@State
def kidan_renda_start_aura():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown457(2)
        Unknown454(2)
        Unknown450('cmn_kidan_throw')
    sprite('null', 4)
    Unknown188(200)
    Unknown191(100)
    sprite('null', 600)
    Unknown188(600)
    Unknown191(0)

@State
def kidan_renda2_start():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown457(2)
        Unknown454(2)
        ActivateEffScript('kidan_renda2_start_aura', 100)
    sprite('null', 3)
    Unknown1731(-80000)
    sprite('null', 3)
    Unknown1731(100000)

@State
def kidan_renda2_start_aura():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown457(2)
        Unknown454(2)
        Unknown450('cmn_kidan_throw')
    sprite('null', 4)
    Unknown188(200)
    Unknown191(100)
    sprite('null', 600)
    Unknown188(600)
    Unknown191(0)

@State
def crouchkidan_start():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown457(2)
        Unknown454(2)
        ActivateEffScript('crouchkidan_start_aura', 100)
    sprite('null', 2)
    Unknown1731(-40000)
    sprite('null', 2)
    Unknown1731(-130000)
    Unknown94(10000)
    Unknown99(10000)
    sprite('null', 4)
    Unknown612('ARC_BTL_CMN_kidan_Chrg')
    Unknown94(40000)
    Unknown99(30000)
    sprite('null', 2)
    Unknown94(-40000)
    Unknown99(-20000)
    Unknown1731(-110000)
    sprite('null', 2)
    Unknown94(70000)
    Unknown99(70000)
    Unknown1731(70000)
    Unknown3()

@State
def crouchkidan_start_aura():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown457(2)
        Unknown454(2)
        Unknown450('cmn_kidan_throw')
        Unknown1731(50000)
    sprite('null', 10)
    Unknown188(100)
    Unknown191(60)
    sprite('null', 600)
    Unknown188(700)
    Unknown191(0)

@State
def jumpkidan_start():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown457(2)
        Unknown454(3)
        ActivateEffScript('jumpkidan_start_aura', 100)
    sprite('null', 3)
    Unknown1731(-90000)
    sprite('null', 1)
    Unknown94(-20000)
    Unknown99(60000)
    Unknown1731(-70000)
    sprite('null', 3)
    Unknown612('ARC_BTL_CMN_kidan_Chrg')
    sprite('null', 4)
    Unknown94(90000)
    Unknown99(30000)
    Unknown1731(60000)
    Unknown3()

@State
def jumpkidan_start_aura():

    def upon_IMMEDIATE():
        Unknown58(1)
        Unknown457(2)
        Unknown454(2)
        Unknown450('cmn_kidan_throw')
    sprite('null', 10)
    Unknown188(100)
    Unknown191(65)
    sprite('null', 600)
    Unknown188(750)
    Unknown191(0)

@State
def gks_hajiki():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 30)
    Unknown450('gks_hajiki')

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
        damage1(300)
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
    sprite('kidan', 600)
    Unknown338(255)
    Unknown58(1)
    Unknown202(70000, 0)
    label('Koware')
    sprite('null', 10)
    Unknown450('')
    Unknown176(1)

@State
def crouchkidan():

    def upon_IMMEDIATE():
        Unknown243()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        callSubroutine('cmn2DKidan_AtkInit')
        callSubroutine('cmnKidan_Init')
        damage1(600)
        airHitPushbackX(3000)
        airHitPushbackY(40000)
        untech_Override(30)
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
        Unknown99(10000)
        Unknown1731(-50000)
        Unknown164(38000)
        Unknown2230(102)
        Unknown2229(102)
        Unknown450('cmn_kidan')
    sprite('kidan_nanameue', 1)
    makeActive()
    Unknown338(0)
    sprite('kidan_nanameue', 600)
    Unknown58(1)
    Unknown338(255)
    Unknown202(90000, 0)
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
        damage1(600)
        airHitPushbackX(15000)
        airHitPushbackY(15000)
        untech_Override(20)
        Unknown1045('04000000636d6e5f426f6d48697400000000000000000000000000000000000000000000')
        Unknown164(-34000)
        Unknown2229(102)
        Unknown2230(102)
        Unknown1731(80000)
        Unknown1914(0)
        Unknown450('cmn_kidan')
    sprite('kidan_nanamesita0', 1)
    makeActive()
    Unknown338(0)
    sprite('kidan_nanamesita', 600)
    Unknown58(1)
    Unknown338(255)
    Unknown202(70000, 0)
    Unknown3()
    label('Koware')
    sprite('null', 10)
    Unknown450('')
    Unknown176(1)

@State
def __404Eff():

    def upon_IMMEDIATE():
        Unknown450('gks_404Eff00')
        Unknown454(2)
        Unknown456(2)
        Unknown457(2)
    sprite('null', 30)
    Unknown3()

@State
def __404SpeedEff():

    def upon_IMMEDIATE():
        Unknown450('gks_404Eff_tossinAura')
        Unknown94(150000)
        Unknown454(2)
        Unknown457(2)
        Unknown35('17000000456e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown3()
    label('End')
    sprite('null', 15)
    Unknown450('gks_404Eff_tossinAuraEnd')
    Unknown3()

@State
def __404EffAir():

    def upon_IMMEDIATE():
        Unknown450('gks_404Eff00')
        Unknown454(2)
        Unknown456(2)
        Unknown457(2)
        Unknown94(120000)
        Unknown99(-20000)
        Unknown1732(-140000)
        Unknown165(20000)
    sprite('null', 30)
    Unknown3()

@State
def __406Eff():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown456(2)
        Unknown457(2)
    sprite('null', 3)
    Unknown450('gks_406Eff00')
    sprite('null', 3)
    Unknown450('gks_406Eff01')
    sprite('null', 3)
    sprite('null', 3)

@State
def __406Eff_2():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown456(2)
        Unknown457(2)
    sprite('null', 3)
    Unknown450('gks_406Eff02')
    sprite('null', 3)
    Unknown450('gks_406Eff03')
    sprite('null', 3)
    sprite('null', 3)

@State
def ex406Eff():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown456(2)
        Unknown457(2)
    sprite('null', 3)
    Unknown450('gks_406Eff00')
    sprite('null', 2)
    Unknown450('gks_406Eff01')
    sprite('null', 2)
    sprite('null', 2)

@State
def ex406Eff_2():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown456(2)
        Unknown457(2)
    sprite('null', 3)
    Unknown450('gks_406Eff02')
    sprite('null', 2)
    Unknown450('gks_406Eff03')
    sprite('null', 2)
    sprite('null', 2)

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
def kamehameha_shadow():

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
def VSAir_kamehameha_shadow():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown164(45000)
        Unknown289(300)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
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
        Unknown164(-45000)
        Unknown289(300)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown450('cmn_shadowLine_loop')
    Unknown3()
    label('end')
    sprite('null', 1)
    Unknown3()

@State
def Kamehameha_Tame():

    def upon_IMMEDIATE():

        def upon_3():
            if Unknown2033(3, 'CmnActMikiwameMove'):
                Unknown19(23)
        Unknown458(2)
        Unknown450('gks_kmhm_tame00')
        if (not SLOT_263):
            storeValue(2, 45, 0, 1)

        def upon_12():
            Unknown2036(2, 0)
    sprite('null', 2)
    Unknown188(250)
    sprite('null', 5)
    Unknown26(9, 2, 45)
    Unknown188(300)
    sprite('null', 1)
    Unknown26(2, 2, 45)
    Unknown188(400)
    Unknown1732(20000)
    sprite('null', 1)
    Unknown26(2, 2, 45)
    Unknown188(500)
    Unknown1732(20000)
    sprite('null', 2)
    Unknown26(3, 2, 45)
    Unknown188(650)
    Unknown1732(20000)

@State
def Kamehameha_Tame_Assist():

    def upon_IMMEDIATE():

        def upon_3():
            if Unknown2033(3, 'CmnActMikiwameMove'):
                Unknown19(23)
        Unknown458(2)
        Unknown450('gks_kmhm_tame_Assist')
        if (not SLOT_263):
            storeValue(2, 45, 0, 1)

        def upon_12():
            Unknown2036(2, 0)
    sprite('null', 2)
    Unknown188(250)
    sprite('null', 5)
    Unknown26(9, 2, 45)
    Unknown188(300)
    sprite('null', 1)
    Unknown26(2, 2, 45)
    Unknown188(400)
    Unknown1732(20000)
    sprite('null', 1)
    Unknown26(2, 2, 45)
    Unknown188(500)
    Unknown1732(20000)
    sprite('null', 2)
    Unknown26(3, 2, 45)
    Unknown188(650)
    Unknown1732(20000)

@State
def Kamehameha_Core():

    def upon_IMMEDIATE():
        Unknown456(3)
        Unknown454(3)
        Unknown289(300)
        Unknown450('gks_kmhm_core00')
        Unknown632('000000004152435f42544c5f474b535f4b6d686d5f46697265000000000000000000000064000000')
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
        Unknown35('2f000000656e640000000000000000000000000000000000000000000000000000000000')

        def upon_35():
            Unknown456(0)
            Unknown454(0)
            Unknown295(1)

        def upon_24():
            Unknown23(24)
            storeValue(2, 45, 0, 0)
            Unknown1803('Kamehameha_Atk', 29)
            if Unknown2033(3, 'Kamehameha'):
                Unknown53(3, 2, 45, 23, 0, 0)
                Unknown1798(3, 25)
            if Unknown2033(3, 'AirKamehameha'):
                Unknown53(3, 2, 45, 23, 0, 0)
                Unknown1798(3, 25)
            if Unknown2033(3, 'AssistAttack'):
                Unknown53(3, 2, 45, 23, 0, 0)
            storeValue(2, 47, 0, 1)
            storeValue(2, 51, 0, 1)

            def upon_24():
                Unknown54('00000000020000002f0000000000000001000000')
                if (SLOT_47 >= 4):
                    if Unknown2033(3, 'Kamehameha'):
                        Unknown1798(3, 24)
                    if Unknown2033(3, 'AirKamehameha'):
                        Unknown1798(3, 24)
                    if Unknown2033(3, 'AssistAttack'):
                        Unknown1798(3, 24)
                else:
                    if Unknown2033(3, 'Kamehameha'):
                        Unknown1798(3, 25)
                    if Unknown2033(3, 'AirKamehameha'):
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
    if Unknown2033(3, 'AirKamehameha'):
        Unknown1798(3, 24)
    if Unknown2033(3, 'AssistAttack'):
        Unknown1798(3, 24)
    Unknown454(0)
    Unknown456(0)
    Unknown294(1)
    sprite('null', 1)
    Unknown32('Kamehameha_Atk')
    sprite('null', 13)
    Unknown450('gks_kmhm_core01')
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
        callSubroutine('cmn_AssistShotHosei')
        mod_hitstop(2)
        or_standhit(11)
        or_launchhit(11)
        airHitPushbackX(60000)
        airHitPushbackY(10000)
        Unknown1186('01000000983a0000e09304006400000000000000')
        Unknown842(0)
        untech_Override(25)
        Unknown1027(50000000, -410000, 0, 0)
        if Unknown2033(3, 'Kamehameha'):
            Unknown1027(50000000, -410000, 0, 0)
        if Unknown2033(3, 'AirKamehameha'):
            Unknown1027(50000000, -385000, 0, 0)
        if Unknown2033(3, 'AssistAttack'):
            damage1(200)
            Unknown1095(1000)
            Unknown1027(50000000, -410000, 0, 0)
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
        Unknown450('gks_kmhm_naka00')

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
                if Unknown2033(3, 'AirKamehameha'):
                    Unknown53(3, 2, 45, 23, 0, 0)

        def upon_8():
            if SLOT_45:
                Unknown1798(2, 23)
            if Unknown2033(3, 'Kamehameha'):
                Unknown53(3, 2, 46, 23, 0, 1)
            if Unknown2033(3, 'AirKamehameha'):
                Unknown53(3, 2, 46, 23, 0, 1)

        def upon_3():
            if conditionalunk2498(2, 2, 47):
                if conditionalunk2499(2, 2, 49):
                    Unknown53(23, 2, 0, 2, 2, 115)
                    if (SLOT_115 <= SLOT_0):
                        Unknown19(23)
            if (SLOT_18 <= 400000):
                Unknown670('02000000e80300000000000000000000')

        def upon_1():
            if SLOT_46:
                storeValue(2, 46, 0, 0)
                Unknown53(2, 2, 46, 23, 0, 0)
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('gks_kmhm_naka01', 100)
            Unknown633(16, 20)
            Unknown633(17, 20)
    sprite('kamehameha0', 1)
    makeActive()
    Unknown202(100000, 0)
    label('loop')
    sprite('kamehameha0', 1)
    Unknown734(0)
    sprite('kamehameha0', 2)
    Unknown2301(1200)
    sprite('kamehameha0', 1)
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
        Unknown450('gks_kmhm_end00')

        def upon_3():
            if Unknown51(2):
                Unknown2488('02000000190100000200000019010000')
                Unknown2036(2, 0)

        def upon_1():
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('gks_kmhm_end01', 100)
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
        Unknown450('gks_kmhm_core00')
        Unknown632('000000004152435f42544c5f474b535f4b6d686d5f46697265000000000000000000000064000000')
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
        Unknown35('2f000000656e640000000000000000000000000000000000000000000000000000000000')

        def upon_35():
            Unknown456(0)
            Unknown454(0)
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
    Unknown294(1)
    sprite('null', 1)
    Unknown32('Kamehameha_Naname_Atk')
    sprite('null', 13)
    Unknown450('gks_kmhm_core01')
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
        Unknown1027(50000000, -250000, 0, 0)
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
        Unknown450('gks_kmhm_naka00')

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
            Unknown449('gks_kmhm_naka01', 100)
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
    sprite('kamehameha1', 1)
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
        Unknown58(1)
        Unknown450('gks_kmhm_end00')

        def upon_3():
            if Unknown51(2):
                Unknown2488('02000000190100000200000019010000')
                Unknown2036(2, 0)

        def upon_1():
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('gks_kmhm_end01', 100)
    label('loop')
    sprite('null', 2)
    Unknown2301(1000)
    sprite('null', 2)
    Unknown2301(1200)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def AirKamehameha_Naname_Core():

    def upon_IMMEDIATE():
        Unknown456(3)
        Unknown454(3)
        Unknown164(-45000)
        Unknown289(300)
        Unknown450('gks_kmhm_core00')
        Unknown632('000000004152435f42544c5f474b535f4b6d686d5f46697265000000000000000000000064000000')
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
        Unknown35('2f000000656e640000000000000000000000000000000000000000000000000000000000')

        def upon_35():
            Unknown456(0)
            Unknown454(0)
            Unknown295(1)

        def upon_24():
            Unknown23(24)
            storeValue(2, 45, 0, 0)
            Unknown1803('AirKamehameha_Naname_Atk', 29)
            if Unknown2033(3, 'AirKamehameha_Naname'):
                Unknown53(3, 2, 45, 23, 0, 0)
                Unknown1798(3, 25)
            storeValue(2, 47, 0, 1)
            storeValue(2, 51, 0, 1)

            def upon_24():
                Unknown54('00000000020000002f0000000000000001000000')
                if (SLOT_47 >= 4):
                    if Unknown2033(3, 'AirKamehameha_Naname'):
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
    Unknown456(0)
    Unknown454(0)
    Unknown294(1)
    sprite('null', 1)
    Unknown32('AirKamehameha_Naname_Atk')
    sprite('null', 13)
    Unknown450('gks_kmhm_core01')
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
        mod_hitstop(2)
        or_standhit(8)
        or_launchhit(8)
        airHitPushbackX(5000)
        airHitPushbackY(1000)
        Unknown842(0)
        untech_Override(40)
        Unknown1027(50000000, -285000, 0, 0)
        Unknown716(1)
        Unknown733(1)
        Unknown734(1)
        Unknown1192('100000004152435f42544c5f434d4e5f4869745f4265616d4c6f6f705f4c50000000000000000000')
        Unknown1193('110000004152435f42544c5f434d4e5f4772645f4265616d4c6f6f705f4c50000000000000000000')
        Unknown717('ShakeYoko', 1000, 1, 20, 0)
        Unknown854(1)
        Unknown802(100)
        Unknown808(8000)
        Unknown806(40000)
        Unknown719(1)

        def upon_30():
            or_standhit(12)
            or_launchhit(12)
            airHitPushbackX(20000)
            airHitPushbackY(40000)
            Unknown854(0)
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
        Unknown450('gks_kmhm_naka00')

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
                    Unknown448('bg_groundsmokeS', 123)
                    Unknown2193(123, -200000, 0)
                    Unknown2277(1)
                    Unknown449('bg_groundsmokeS', 130)
                    Unknown670('01000000e80300000000000000000000')

        def upon_1():
            if SLOT_46:
                storeValue(2, 46, 0, 0)
                Unknown53(2, 2, 46, 23, 0, 0)
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('gks_kmhm_naka01', 100)
            Unknown633(16, 20)
            Unknown633(17, 20)
    sprite('kamehameha1', 1)
    makeActive()
    Unknown202(100000, 0)
    label('loop')
    sprite('kamehameha1', 1)
    Unknown734(0)
    sprite('kamehameha1', 2)
    Unknown2301(1200)
    sprite('kamehameha1', 1)
    Unknown2301(1000)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def AirKamehameha_Naname_End():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown457(2)
        Unknown164(-45000)
        Unknown289(60)
        Unknown2036(2, 0)
        Unknown2488('02000000190100000200000019010000')
        Unknown58(1)
        Unknown450('gks_kmhm_end00')

        def upon_3():
            if Unknown51(2):
                Unknown2488('02000000190100000200000019010000')
                Unknown2036(2, 0)

        def upon_1():
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('gks_kmhm_end01', 100)
    label('loop')
    sprite('null', 2)
    Unknown2301(1000)
    sprite('null', 2)
    Unknown2301(1200)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def groundSmoke_EXtame():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown454(2)
        Unknown458(2)
        Unknown289(300)

        def upon_12():
            if Unknown2033(3, 'CmnActChangeLeave'):
                Unknown19(23)
    label('loop')
    sprite('null', 10)
    Unknown2273(0, 1200)
    Unknown449('bg_undersmoke00', 100)
    Unknown3()
    labelEnd('loop')

@State
def GKS_aura():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown458(2)
        Unknown454(2)
        Unknown455(3)
        Unknown1955('636d6e5f5332617572615f6c6f6f700000000000000000000000000000000000')
        Unknown289(300)
        Unknown35('1700000041746b0000000000000000000000000000000000000000000000000000000000')
        Unknown35('18000000456e640000000000000000000000000000000000000000000000000000000000')

        def upon_12():
            if Unknown2033(3, 'CmnActChangeLeave'):
                Unknown19(23)
    label('Start')
    sprite('null', 15)
    Unknown448('cmn_Saura_nokosi', 100)
    Unknown3()
    labelEnd('Start')
    label('Atk')
    sprite('null', 1)
    Unknown450('cmn_S2auraYoko_loop')
    label('AtkLoop')
    sprite('null', 15)
    Unknown449('cmn_Saura_nokosi', 100)
    Unknown3()
    labelEnd('AtkLoop')
    label('End')
    sprite('null', 30)
    Unknown23(23)
    Unknown23(24)
    Unknown450('cmn_S2auraYoko_end')
    Unknown3()

@State
def S_Kamehameha_Tame():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown458(2)
        Unknown450('gks_kmhmEX_tame00')
        Unknown289(300)
        Unknown35('170000005761727000000000000000000000000000000000000000000000000000000000')

        def upon_12():
            Unknown2036(2, 0)
    sprite('null', 4)
    Unknown188(250)
    sprite('null', 49)
    Unknown188(300)
    sprite('null', 3)
    Unknown188(400)
    sprite('null', 3)
    Unknown188(500)
    Unknown1732(20000)
    sprite('null', 6)
    Unknown188(650)
    Unknown1732(20000)

@State
def S_Kamehameha_Warp_Tame():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown458(2)
        Unknown450('gks_kmhmEX_tame00')

        def upon_12():
            Unknown2036(2, 0)
    sprite('null', 4)
    Unknown188(250)
    Unknown1732(20000)
    sprite('null', 37)
    Unknown188(300)
    sprite('null', 28)
    Unknown338(0)
    sprite('null', 13)
    Unknown338(255)
    sprite('null', 3)
    Unknown188(400)
    sprite('null', 3)
    Unknown188(500)
    Unknown1732(20000)
    sprite('null', 6)
    Unknown188(650)
    Unknown1732(20000)

@State
def S_Kamehameha_Core():

    def upon_IMMEDIATE():
        Unknown456(3)
        Unknown454(3)
        Unknown289(300)
        Unknown450('gks_kmhmEX_core00')
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
        Unknown35('2f000000656e640000000000000000000000000000000000000000000000000000000000')

        def upon_35():
            Unknown456(0)
            Unknown454(0)
            Unknown295(1)

        def upon_24():
            Unknown23(24)
            storeValue(2, 45, 0, 0)
            Unknown1803('S_Kamehameha_Atk', 29)
            if Unknown2033(3, 'S_Kamehameha'):
                Unknown53(3, 2, 45, 23, 0, 0)
                Unknown1798(3, 25)
            if Unknown2033(3, 'S_AirKamehameha'):
                Unknown53(3, 2, 45, 23, 0, 0)
                Unknown1798(3, 25)
            storeValue(2, 47, 0, 1)
            storeValue(2, 51, 0, 1)

            def upon_24():
                Unknown54('00000000020000002f0000000000000001000000')
                if (SLOT_47 >= 8):
                    if Unknown2033(3, 'S_Kamehameha'):
                        Unknown1798(3, 24)
                    if Unknown2033(3, 'S_AirKamehameha'):
                        Unknown1798(3, 24)
                else:
                    if Unknown2033(3, 'S_Kamehameha'):
                        Unknown1798(3, 25)
                    if Unknown2033(3, 'S_AirKamehameha'):
                        Unknown1798(3, 25)

        def upon_3():
            if (not SLOT_46):
                Unknown1804('535f4b616d6568616d6568615f41746b0000000000000000000000000000000017000000')
    label('loop')
    sprite('null', 2)
    Unknown54('0000000002000000300000000000000001000000')
    Unknown2279('02000000300000000200000033000000')
    Unknown445('535f4b616d6568616d6568615f41746b0000000000000000000000000000000064000000')
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
    ActivateEffScript('S_Kamehameha_Atk', 100)
    Unknown1803('S_Kamehameha_Atk', 30)
    if Unknown2033(3, 'S_Kamehameha'):
        Unknown1798(3, 24)
    if Unknown2033(3, 'S_AirKamehameha'):
        Unknown1798(3, 24)
    Unknown454(0)
    Unknown456(0)
    Unknown294(1)
    sprite('null', 1)
    Unknown32('S_Kamehameha_Atk')
    sprite('null', 13)
    Unknown450('gks_kmhmEX_core01')
    sprite('null', 35)

@State
def S_Kamehameha_Atk():

    def upon_IMMEDIATE():
        Unknown245()
        callSubroutine('cmnAtkLevel_4_AtkInit')
        callSubroutine('cmnUltimateShot_AtkInit')
        damage1(250)
        Unknown1086(31)
        mod_hitstop(2)
        or_standhit(11)
        or_launchhit(11)
        airHitPushbackX(60000)
        airHitPushbackY(13000)
        Unknown1186('0100000010270000c0c62d006400000000000000')
        Unknown842(0)
        untech_Override(30)
        Unknown1027(50000000, -410000, 0, 0)
        if Unknown2033(3, 'S_Kamehameha'):
            Unknown1027(50000000, -410000, 0, 0)
        else:
            Unknown1027(50000000, -385000, 0, 0)
        Unknown716(1)
        Unknown733(1)
        Unknown734(1)
        Unknown1192('100000004152435f42544c5f434d4e5f4869745f4265616d4c6f6f705f4c50000000000000000000')
        Unknown1193('110000004152435f42544c5f434d4e5f4772645f4265616d4c6f6f705f4c50000000000000000000')
        Unknown1191(1)
        Unknown719(1)

        def upon_30():
            airHitPushbackY(35000)
            or_standhit(12)
            or_launchhit(12)
            Unknown1186('0000000000000000000000000000000000000000')
            untech_Override(22)
            mod_opphitstop(0, 8, 8)
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
        Unknown450('gks_kmhmEX_naka00')

        def upon_23():
            Unknown23(23)
            ActivateEffScript('S_Kamehameha_End', 100)
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
                if Unknown2033(3, 'S_Kamehameha'):
                    Unknown53(3, 2, 45, 23, 0, 0)
                if Unknown2033(3, 'S_AirKamehameha'):
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
            if (SLOT_18 <= 500000):
                Unknown670('03000000e80300000000000000000000')
            if (not 
            Unknown53(23, 2, 0, 22, 2, 36)):
                Unknown633(16, 20)
                Unknown633(17, 20)
            if (not 
            Unknown2033(3, 'S_Kamehameha')):
                if (not 
                Unknown2033(3, 'S_AirKamehameha')):
                    Unknown633(16, 20)
                    Unknown633(17, 20)

        def upon_1():
            if SLOT_46:
                storeValue(2, 46, 0, 0)
                Unknown53(2, 2, 46, 23, 0, 0)
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('gks_kmhmEX_naka01', 100)
    sprite('S_kamehameha0', 1)
    makeActive()
    Unknown202(100000, 0)
    label('loop')
    sprite('S_kamehameha0', 1)
    Unknown734(0)
    sprite('S_kamehameha0', 2)
    Unknown2301(1200)
    sprite('S_kamehameha0', 1)
    Unknown2301(1000)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def S_Kamehameha_End():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown457(2)
        Unknown289(60)
        Unknown2036(2, 0)
        Unknown58(1)
        Unknown450('gks_kmhmEX_end00')

        def upon_3():
            if Unknown51(2):
                Unknown2488('02000000190100000200000019010000')
                Unknown2036(2, 0)

        def upon_1():
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('gks_kmhmEX_end01', 100)
    label('loop')
    sprite('null', 2)
    Unknown2301(1000)
    sprite('null', 2)
    Unknown2301(1200)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def S_Kamehameha_Naname_Core():

    def upon_IMMEDIATE():
        Unknown456(3)
        Unknown454(3)
        Unknown164(45000)
        Unknown289(300)
        Unknown450('gks_kmhmEX_core00')
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
        Unknown35('2f000000656e640000000000000000000000000000000000000000000000000000000000')

        def upon_35():
            Unknown456(0)
            Unknown454(0)
            Unknown295(1)

        def upon_24():
            Unknown23(24)
            storeValue(2, 45, 0, 0)
            Unknown1803('S_Kamehameha_Naname_Atk', 29)
            if Unknown2033(3, 'S_Kamehameha_Naname'):
                Unknown53(3, 2, 45, 23, 0, 0)
                Unknown1798(3, 25)
            if Unknown2033(3, 'S_Kamehameha_Warp'):
                Unknown53(3, 2, 45, 23, 0, 0)
                Unknown1798(3, 25)
            if Unknown2033(3, 'S_AirKamehameha_Warp'):
                Unknown53(3, 2, 45, 23, 0, 0)
                Unknown1798(3, 25)
            storeValue(2, 47, 0, 1)
            storeValue(2, 51, 0, 1)

            def upon_24():
                Unknown54('00000000020000002f0000000000000001000000')
                if (SLOT_47 >= 8):
                    if Unknown2033(3, 'S_Kamehameha_Naname'):
                        Unknown1798(3, 24)
                    if Unknown2033(3, 'S_Kamehameha_Warp'):
                        Unknown1798(3, 24)
                    if Unknown2033(3, 'S_AirKamehameha_Warp'):
                        Unknown1798(3, 24)
                else:
                    if Unknown2033(3, 'S_Kamehameha_Naname'):
                        Unknown1798(3, 25)
                    if Unknown2033(3, 'S_Kamehameha_Warp'):
                        Unknown1798(3, 25)
                    if Unknown2033(3, 'S_AirKamehameha_Warp'):
                        Unknown1798(3, 25)

        def upon_3():
            if (not SLOT_46):
                Unknown1804('535f4b616d6568616d6568615f4e616e616d655f41746b00000000000000000017000000')
    label('loop')
    sprite('null', 2)
    Unknown54('0000000002000000300000000000000001000000')
    Unknown2279('02000000300000000200000033000000')
    Unknown445('535f4b616d6568616d6568615f4e616e616d655f41746b00000000000000000064000000')
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
    ActivateEffScript('S_Kamehameha_Naname_Atk', 100)
    Unknown1803('S_Kamehameha_Naname_Atk', 30)
    if Unknown2033(3, 'S_Kamehameha_Naname'):
        Unknown1798(3, 24)
    if Unknown2033(3, 'S_Kamehameha_Warp'):
        Unknown1798(3, 24)
    if Unknown2033(3, 'S_AirKamehameha_Warp'):
        Unknown1798(3, 24)
    Unknown454(0)
    Unknown456(0)
    Unknown294(1)
    sprite('null', 1)
    Unknown32('S_Kamehameha_Naname_Atk')
    sprite('null', 13)
    Unknown450('gks_kmhmEX_core01')
    sprite('null', 35)

@State
def S_Kamehameha_Naname_Atk():

    def upon_IMMEDIATE():
        Unknown245()
        callSubroutine('cmnAtkLevel_4_AtkInit')
        callSubroutine('cmnUltimateShot_AtkInit')
        damage1(270)
        Unknown1086(30)
        mod_hitstop(2)
        or_standhit(12)
        or_launchhit(12)
        airHitPushbackX(25000)
        airHitPushbackY(25000)
        Unknown1027(50000000, -245000, 0, 0)
        untech_Override(40)
        Unknown716(1)
        Unknown733(1)
        Unknown734(1)
        Unknown1192('100000004152435f42544c5f434d4e5f4869745f4265616d4c6f6f705f4c50000000000000000000')
        Unknown1193('110000004152435f42544c5f434d4e5f4772645f4265616d4c6f6f705f4c50000000000000000000')
        Unknown1191(1)
        Unknown719(1)

        def upon_30():
            airHitPushbackX(45000)
            airHitPushbackY(60000)
            Unknown1185('0000000000000000000000000000000000000000')
            Unknown1186('0000000000000000000000000000000000000000')
            Unknown1027(50000000, -245000, 0, 0)
            mod_opphitstop(0, 10, 10)
            untech_Override(35)
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
        Unknown450('gks_kmhmEX_naka00')

        def upon_23():
            Unknown23(23)
            ActivateEffScript('S_Kamehameha_Naname_End', 100)
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
                if Unknown2033(3, 'S_Kamehameha_Naname'):
                    Unknown53(3, 2, 45, 23, 0, 0)
                if Unknown2033(3, 'S_Kamehameha_Warp'):
                    Unknown53(3, 2, 45, 23, 0, 0)
                if Unknown2033(3, 'S_AirKamehameha_Warp'):
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
            Unknown2033(3, 'S_Kamehameha_Naname')):
                Unknown633(16, 20)
                Unknown633(17, 20)

        def upon_1():
            if SLOT_46:
                storeValue(2, 46, 0, 0)
                Unknown53(2, 2, 46, 23, 0, 0)
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('gks_kmhmEX_naka01', 100)
    sprite('S_kamehameha1', 2)
    makeActive()
    Unknown1185('0100000090d00300a08601004b00000000000000')
    Unknown1186('01000000f0490200a08601004b00000000000000')
    Unknown202(100000, 0)
    Unknown1027(220000, -245000, -250000, -5000000)
    sprite('S_kamehameha2', 2)
    Unknown1185('0100000020a10700a08601004b00000000000000')
    Unknown1186('0100000070640800e09304006400000000000000')
    Unknown2301(1200)
    Unknown734(0)
    Unknown1027(50000000, -245000, 0, 0)
    sprite('S_kamehameha2', 2)
    Unknown1185('0000000000000000000000000000000000000000')
    Unknown1186('01000000b0710b00e09304006400000000000000')
    Unknown2301(1000)
    sprite('S_kamehameha2', 2)
    Unknown1186('01000000f07e0e00e09304006400000000000000')
    Unknown2301(1200)
    sprite('S_kamehameha2', 2)
    Unknown1186('01000000308c1100e09304006400000000000000')
    Unknown2301(1000)
    sprite('S_kamehameha2', 2)
    Unknown1186('0100000070991400e09304006400000000000000')
    Unknown2301(1200)
    label('loop')
    sprite('S_kamehameha2', 2)
    Unknown2301(1000)
    sprite('S_kamehameha2', 2)
    Unknown2301(1200)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def S_Kamehameha_Naname_End():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown457(2)
        Unknown164(45000)
        Unknown289(60)
        Unknown2036(2, 0)
        Unknown58(1)
        Unknown450('gks_kmhmEX_end00')

        def upon_3():
            if Unknown51(2):
                Unknown2488('02000000190100000200000019010000')
                Unknown2036(2, 0)

        def upon_1():
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('gks_kmhmEX_end01', 100)
    label('loop')
    sprite('null', 2)
    Unknown2301(1000)
    sprite('null', 2)
    Unknown2301(1200)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def S_AirKamehameha_Naname_Core():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown454(2)
        Unknown164(-45000)
        Unknown289(300)
        Unknown450('gks_kmhmEX_core00')
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
        Unknown35('2f000000656e640000000000000000000000000000000000000000000000000000000000')

        def upon_35():
            Unknown456(0)
            Unknown454(0)
            Unknown295(1)

        def upon_24():
            Unknown23(24)
            storeValue(2, 45, 0, 0)
            Unknown1803('S_AirKamehameha_Naname_Atk', 29)
            if Unknown2033(3, 'S_AirKamehameha_Naname'):
                Unknown53(3, 2, 45, 23, 0, 0)
                Unknown1798(3, 25)
            storeValue(2, 47, 0, 1)
            storeValue(2, 51, 0, 1)

            def upon_24():
                Unknown54('00000000020000002f0000000000000001000000')
                if (SLOT_47 >= 8):
                    if Unknown2033(3, 'S_AirKamehameha_Naname'):
                        Unknown1798(3, 24)
                elif Unknown2033(3, 'S_AirKamehameha_Naname'):
                    Unknown1798(3, 25)

        def upon_3():
            if (not SLOT_46):
                Unknown1804('535f4169724b616d6568616d6568615f4e616e616d655f41746b00000000000017000000')
    label('loop')
    sprite('null', 2)
    Unknown54('0000000002000000300000000000000001000000')
    Unknown2279('02000000300000000200000033000000')
    Unknown445('535f4169724b616d6568616d6568615f4e616e616d655f41746b00000000000064000000')
    if (SLOT_45 >= 8):
        Unknown53(1, 2, 45, 23, 0, 1)
    if (not SLOT_50):
        storeValue(2, 50, 0, 1)
        Unknown53(1, 2, 50, 23, 0, 1)
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
    ActivateEffScript('S_AirKamehameha_Naname_Atk', 100)
    Unknown1803('S_AirKamehameha_Naname_Atk', 30)
    if Unknown2033(3, 'S_AirKamehameha_Naname'):
        Unknown1798(3, 24)
    Unknown454(0)
    Unknown456(0)
    Unknown294(1)
    sprite('null', 1)
    Unknown32('S_AirKamehameha_Naname_Atk')
    sprite('null', 13)
    Unknown450('gks_kmhmEX_core01')
    sprite('null', 35)
    Unknown633(0, 35)

@State
def S_AirKamehameha_Naname_Atk():

    def upon_IMMEDIATE():
        Unknown245()
        callSubroutine('cmnAtkLevel_4_AtkInit')
        callSubroutine('cmnUltimateShot_AtkInit')
        damage1(250)
        Unknown1086(30)
        mod_hitstop(2)
        or_standhit(11)
        or_launchhit(11)
        airHitPushbackX(0)
        airHitPushbackY(3000)
        Unknown1027(50000000, -285000, 0, 0)
        untech_Override(30)
        Unknown941(5)
        Unknown842(0)
        Unknown716(1)
        Unknown733(1)
        Unknown734(1)
        Unknown1192('100000004152435f42544c5f434d4e5f4869745f4265616d4c6f6f705f4c50000000000000000000')
        Unknown1193('110000004152435f42544c5f434d4e5f4772645f4265616d4c6f6f705f4c50000000000000000000')
        Unknown1191(1)
        Unknown719(1)

        def upon_30():
            or_standhit(11)
            or_launchhit(11)
            airHitPushbackX(40000)
            airHitPushbackY(-40000)
            Unknown1207('000000006400000000000000000000000000000000000000')
            Unknown1208('000000006400000000000000000000000000000000000000')
            untech_Override(60)
            Unknown941(30)
            Unknown842(0)
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
        Unknown450('gks_kmhmEX_naka00')

        def upon_23():
            Unknown23(23)
            ActivateEffScript('S_AirKamehameha_Naname_End', 100)
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
                if Unknown2033(3, 'S_AirKamehameha_Naname'):
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
            if (SLOT_18 <= 0):
                if SLOT_50:
                    Unknown23(3)
                    Unknown448('bg_groundsmokeS', 123)
                    Unknown2193(123, -200000, 0)
                    Unknown2277(1)
                    Unknown449('bg_groundsmokeS', 130)
                    Unknown670('01000000e80300000000000000000000')
            if (not 
            Unknown53(23, 2, 0, 22, 2, 36)):
                Unknown633(16, 20)
                Unknown633(17, 20)
            if (not 
            Unknown2033(3, 'S_AirKamehameha_Naname')):
                Unknown633(16, 20)
                Unknown633(17, 20)

        def upon_1():
            if SLOT_46:
                storeValue(2, 46, 0, 0)
                Unknown53(2, 2, 46, 23, 0, 0)
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('gks_kmhmEX_naka01', 100)
    sprite('S_kamehameha1', 1)
    makeActive()
    Unknown202(100000, 0)
    Unknown1207('0100000064000000a086010050c300006400000000000000')
    Unknown1208('0100000064000000d0a8faff50c300006400000000000000')
    label('loop')
    sprite('S_kamehameha2', 1)
    Unknown734(0)
    Unknown1207('000000006400000000000000000000000000000000000000')
    Unknown1208('000000006400000000000000000000000000000000000000')
    sprite('S_kamehameha2', 2)
    Unknown2301(1200)
    sprite('S_kamehameha2', 1)
    Unknown2301(1000)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def S_AirKamehameha_Naname_End():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown457(2)
        Unknown164(-45000)
        Unknown289(60)
        Unknown2036(2, 0)
        Unknown58(1)
        Unknown450('gks_kmhmEX_end00')

        def upon_3():
            if Unknown51(2):
                Unknown2488('02000000190100000200000019010000')
                Unknown2036(2, 0)

        def upon_1():
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('gks_kmhmEX_end01', 100)
    label('loop')
    sprite('null', 2)
    Unknown2301(1000)
    sprite('null', 2)
    Unknown2301(1200)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def M_Kamehameha_Tame():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown450('gks_kmhm_tame00')
        Unknown294(1)
        Unknown94(50000)
    sprite('null', 3)
    Unknown188(250)
    sprite('null', 15)
    Unknown188(300)
    Unknown94(-15000)
    Unknown99(-5000)
    Unknown3()

@State
def M_Kamehameha_Core():

    def upon_IMMEDIATE():
        Unknown456(3)
        Unknown454(3)
        Unknown289(300)
        Unknown94(150000)
        Unknown450('gks_kmhmSP_core00')
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
        Unknown35('2f000000656e640000000000000000000000000000000000000000000000000000000000')

        def upon_35():
            Unknown456(0)
            Unknown454(0)
            Unknown295(1)

        def upon_24():
            Unknown23(24)
            storeValue(2, 45, 0, 0)
            Unknown1803('M_Kamehameha_Atk', 29)
            if Unknown2033(3, 'MeteoSmash'):
                Unknown53(3, 2, 45, 23, 0, 0)
            storeValue(2, 47, 0, 1)

            def upon_24():
                Unknown54('00000000020000002f0000000000000001000000')
                if (SLOT_47 >= 16):
                    if Unknown2033(3, 'MeteoSmash'):
                        Unknown1798(3, 24)

        def upon_3():
            if (not SLOT_46):
                Unknown1804('4d5f4b616d6568616d6568615f41746b0000000000000000000000000000000017000000')
    label('loop')
    sprite('null', 2)
    Unknown54('0000000002000000300000000000000001000000')
    Unknown2279('02000000300000000000000000000000')
    Unknown445('4d5f4b616d6568616d6568615f41746b0000000000000000000000000000000064000000')
    if (SLOT_45 <= 9):
        Unknown41(1)
        Unknown1199(1, 0)
        Unknown40()
    if (SLOT_45 >= 16):
        Unknown1798(1, 28)
    if (SLOT_45 >= 22):
        Unknown53(1, 2, 45, 23, 0, 1)
    sprite('null', 2)
    Unknown3()
    Unknown54('00000000020000002d0000000000000001000000')
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000002d0000000000000018000000')
    label('end')
    sprite('null', 1)
    Unknown23(23)
    Unknown23(24)
    Unknown23(47)
    Unknown23(3)
    storeValue(2, 49, 0, 1)
    ActivateEffScript('M_Kamehameha_Atk', 100)
    Unknown1803('M_Kamehameha_Atk', 30)
    if Unknown2033(3, 'MeteoSmash'):
        Unknown1798(3, 24)
    Unknown94(150000)
    Unknown454(0)
    Unknown456(0)
    Unknown294(1)
    sprite('null', 1)
    Unknown32('M_Kamehameha_Atk')
    sprite('null', 13)
    Unknown450('gks_kmhmSP_core01')
    sprite('null', 35)

@State
def M_Kamehameha_Atk():

    def upon_IMMEDIATE():
        Unknown245()
        callSubroutine('cmnAtkLevel_4_AtkInit')
        callSubroutine('cmnUltimateShot_AtkInit')
        Unknown1028(5)
        damage1(130)
        Unknown1086(46)
        mod_hitstop(2)
        or_standhit(11)
        or_launchhit(11)
        airHitPushbackX(80000)
        airHitPushbackY(1000)
        Unknown1186('01000000c0d40100f04902006400000000000000')
        Unknown842(0)
        untech_Override(60)
        Unknown1187(0)
        Unknown1079(1)
        Unknown1192('100000004152435f42544c5f434d4e5f4869745f4265616d4c6f6f705f4c50000000000000000000')
        Unknown1193('110000004152435f42544c5f434d4e5f4772645f4265616d4c6f6f705f4c50000000000000000000')
        Unknown1191(1)
        Unknown719(1)

        def upon_30():
            Unknown1186('0000000000000000000000000000000000000000')
            Unknown842(1)
            Unknown790(0)
            Unknown937(12)
            airHitPushbackX(100000)
            airHitPushbackY(10000)
            mod_opphitstop(0, 7, 7)
            Unknown1064('436d6e4e65757472616c00000000000000000000000000000000000000000000')
            if conditionalunk2499(3, 2, 24):
                makeActive()
            else:
                beginRecovery()
            if conditionalunk2500(12, 2, 2, 47, 0, 16):
                beginRecovery()

        def upon_28():
            Unknown1191(2)
        Unknown456(2)
        Unknown454(2)
        Unknown457(2)
        Unknown453(2)
        Unknown289(60)
        Unknown94(-150000)
        Unknown1954(1)
        Unknown58(1)
        Unknown450('gks_kmhmSP_naka00')

        def upon_23():
            Unknown23(23)
            ActivateEffScript('M_Kamehameha_End', 100)
            storeValue(2, 46, 0, 1)
            Unknown53(2, 2, 46, 23, 0, 1)

        def upon_93():
            Unknown53(2, 2, 115, 23, 2, 115)
            Unknown19(23)
            Unknown1798(2, 24)

        def upon_29():
            storeValue(2, 45, 0, 0)

        def upon_8():
            if SLOT_45:
                Unknown1798(2, 23)

        def upon_90():
            Unknown23(90)
            callSubroutine('cmnUltimate_CameraCombo')

        def upon_3():
            if conditionalunk2498(2, 2, 47):
                if conditionalunk2499(2, 2, 49):
                    Unknown53(23, 2, 0, 2, 2, 115)
                    if (SLOT_115 <= SLOT_0):
                        Unknown19(23)
            if (SLOT_18 <= 500000):
                Unknown670('03000000e80300000000000000000000')
            if (not 
            Unknown53(23, 2, 0, 22, 2, 36)):
                Unknown633(16, 20)
                Unknown633(17, 20)

        def upon_1():
            if SLOT_46:
                storeValue(2, 46, 0, 0)
                Unknown53(2, 2, 46, 23, 0, 0)
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('gks_kmhmSP_naka01', 100)
    sprite('M_kamehameha', 1)
    makeActive()
    Unknown202(90000, 0)
    label('loop')
    sprite('M_kamehameha', 1)
    sprite('M_kamehameha', 2)
    Unknown2301(1200)
    sprite('M_kamehameha', 1)
    Unknown2301(1000)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def M_Kamehameha_End():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown457(2)
        Unknown289(60)
        Unknown2036(2, 0)
        Unknown58(1)
        Unknown450('gks_kmhmSP_end00')

        def upon_3():
            if Unknown51(2):
                Unknown2488('02000000190100000200000019010000')
                Unknown2036(2, 0)

        def upon_1():
            Unknown2274(0, 1000)
            Unknown2276(0, 0)
            Unknown449('gks_kmhmSP_end01', 100)
    label('loop')
    sprite('null', 2)
    Unknown2301(1000)
    sprite('null', 2)
    Unknown2301(1200)
    Unknown3()
    Unknown13('6c6f6f70000000000000000000000000000000000000000000000000000000000d000000020000000d0000000000000078000000')

@State
def Meteo_aura():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown457(2)
        Unknown454(2)
        Unknown455(3)
        Unknown1955('636d6e5f5332617572615f6c6f6f700000000000000000000000000000000000')
        Unknown99(-20000)
        Unknown289(1200)
        Unknown35('17000000796f6b6f00000000000000000000000000000000000000000000000000000000')
        Unknown35('180000007461746500000000000000000000000000000000000000000000000000000000')
        Unknown35('19000000416c7068615a65726f0000000000000000000000000000000000000000000000')
        Unknown35('1a00000074616d6500000000000000000000000000000000000000000000000000000000')
        Unknown35('1b000000456e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)
    ActivateEffScript('Meteo_wind', 100)
    label('Start')
    sprite('null', 15)
    Unknown448('cmn_Saura_nokosi', 100)
    Unknown3()
    labelEnd('Start')
    label('yoko')
    sprite('null', 1)
    Unknown338(255)
    Unknown188(1000)
    Unknown1955('636d6e5f533261757261596f6b6f5f6c6f6f7000000000000000000000000000')
    label('LoopA')
    sprite('null', 15)
    Unknown448('cmn_Saura_nokosi', 100)
    Unknown3()
    labelEnd('LoopA')
    label('tate')
    sprite('null', 1)
    Unknown338(255)
    Unknown1955('636d6e5f5332617572615f6c6f6f700000000000000000000000000000000000')
    label('LoopB')
    sprite('null', 15)
    Unknown448('cmn_Saura_nokosi', 100)
    Unknown3()
    labelEnd('LoopB')
    label('AlphaZero')
    sprite('null', 2147483647)
    Unknown338(0)
    Unknown3()
    label('tame')
    sprite('null', 1)
    Unknown338(255)
    Unknown188(800)
    Unknown1955('636d6e5f5332617572615f6c6f6f700000000000000000000000000000000000')
    label('LoopC')
    sprite('null', 15)
    Unknown448('cmn_Saura_nokosi', 100)
    Unknown3()
    labelEnd('LoopC')
    label('End')
    sprite('null', 40)
    Unknown23(23)
    Unknown23(24)
    Unknown23(25)
    Unknown23(26)
    Unknown23(27)
    Unknown338(255)
    Unknown1955('636d6e5f533261757261596f6b6f5f656e640000000000000000000000000000')

@State
def Meteo_wind():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown99(125000)
    sprite('null', 60)
    Unknown188(650)
    Unknown450('gks_meteowind')

@State
def Meteo_auraGround():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown457(2)
        Unknown454(2)
        Unknown99(40000)
        Unknown289(1200)
        Unknown1955('636d6e5f53617572615f67726f756e6400000000000000000000000000000000')
        Unknown35('170000007461746500000000000000000000000000000000000000000000000000000000')
        Unknown35('18000000796f6b6f00000000000000000000000000000000000000000000000000000000')
        Unknown35('1900000044656c6c00000000000000000000000000000000000000000000000000000000')
    label('tate')
    sprite('null', 2147483647)
    Unknown338(255)
    Unknown188(800)
    Unknown3()
    label('yoko')
    sprite('null', 2147483647)
    Unknown338(255)
    Unknown188(1200)
    Unknown3()
    label('Dell')
    sprite('null', 2147483647)
    Unknown338(0)
    Unknown3()

@State
def Meteo_TameSphere():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown457(2)
        Unknown454(2)
        Unknown289(1200)
        Unknown35('170000003100000000000000000000000000000000000000000000000000000000000000')
        Unknown35('180000003200000000000000000000000000000000000000000000000000000000000000')
        Unknown35('190000003300000000000000000000000000000000000000000000000000000000000000')
        Unknown35('1a0000003400000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown450('gks_kmhmSP_tama')
    Unknown99(190000)
    Unknown94(-110000)
    Unknown188(800)
    label('1')
    sprite('null', 2147483647)
    Unknown188(500)
    Unknown1732(50000)
    Unknown94(50000)
    Unknown99(40000)
    Unknown3()
    label('2')
    sprite('null', 2147483647)
    Unknown94(120000)
    Unknown99(-7000)
    Unknown1732(50000)
    Unknown3()
    label('3')
    sprite('null', 2147483647)
    Unknown94(35000)
    Unknown99(-1000)
    Unknown3()
    label('4')
    sprite('null', 2)
    Unknown188(2000)
    Unknown94(100000)
    Unknown99(52500)
    sprite('null', 2)
    Unknown188(2500)
    sprite('null', 2)
    Unknown188(3000)
    sprite('null', 2147483647)
    Unknown3()

@State
def Meteo_rock():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown1801(1)
        Unknown457(2)
        Unknown99(-300000)
    sprite('null', 10)
    physicsImpulseY(30000)
    Unknown450('bg_gks436_stone')
    sprite('null', 60)
    physicsImpulseY(0)

@State
def gks_431_E_Light():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
    sprite('null', 1000)
    Unknown450('gks_431_E_Light')

@State
def SSJ3_kaijoEff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
    sprite('null', 10)
    Unknown450('gks_431_kaijo')
    sprite('null', 60)
    Unknown457(0)
    Unknown454(0)

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
    Unknown2076('0525feff1c5102008b2c0000441900004c2000000000000048000000000000005a0000001e00000001000000')
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
    Unknown2076('da20ffffec3f0200ea82ffff53210000fe1600000000000048000000000000005a0000001e00000001000000')
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
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def FinishCamera_Tyo_TKamehameha():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 10)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    Unknown2079('0d000000e888fffff6d70500023d01004e0100003c0700000000000036000000000000000a00000000000000000000000200000002000000')
    sprite('null', 50)
    Unknown2079('0d0000001baefbffe5eb0700e5a80000e908000065190000000000003600000050000000140000000a000000000000000200000002000000')
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def FinishCamera_W_Kamehameha():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 10)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    Unknown2079('0d000000e888fffff6d70500023d01004e0100003c0700000000000036000000000000000a00000000000000000000000200000002000000')
    sprite('null', 50)
    Unknown2079('0d0000001baefbffe5eb0700e5a80000e908000065190000000000003600000050000000140000000a000000000000000200000002000000')
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def GKS600Flash():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown450('gks600_scrFlash')
    sprite('null', 9)
    Unknown3()

@State
def GKS600Eff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown450('gks600_scranime')
    sprite('null', 90)
    Unknown3()

@State
def GKS600BodyAura():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown1955('636d6e5f53617572615f6c6f6f70000000000000000000000000000000000000')
        Unknown232(-450000)
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
    ActivateEffScript('GKS600BodyAuraDust', 100)
    Unknown94(-350000)
    Unknown1732(-400000)
    Unknown99(80000)
    Unknown232(450000)
    Unknown188(1200)
    Unknown3()

@State
def GKS600BodyAuraDust():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown1955('676b733630305f61757261647573740000000000000000000000000000000000')
        Unknown188(80)
    sprite('null', 2147483647)
    Unknown99(215000)
    Unknown94(400000)
    Unknown1732(450000)
    Unknown3()

@State
def GKScs600_groundsmoke():

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
    Unknown3()
    labelEnd('loop')

@State
def GKScs600_groundsmoke2():

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
    Unknown3()
    labelEnd('loop')

@State
def GKS801_FRN():

    def upon_IMMEDIATE():
        Unknown92(0)
        Unknown98(0)
        Unknown1731(0)
        Unknown454(2)
        Unknown2494('46524e000000000000000000000000000000000000000000000000000000000046524e5f474b5338303163735f30310000000000000000000000000000000000')
        Unknown457(2)
        Unknown35('170000004475737446616c6c000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    label('DustFall')
    sprite('null', 2147483647)
    ActivateEffScript('GKS801_Dust', 149)
    Unknown41(1)
    Unknown94(-200000)
    Unknown99(-200000)
    Unknown188(4000)
    Unknown40()

@State
def GKS801_KRN():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown451('56535f46524e5f4b524e000000000000000000000000000000000000000000004b524e5f474b5338303163735f30310000000000000000000000000000000000')
    sprite('null', 2147483647)

@State
def GKS801_bomb():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('gks_801_bomb')
        Unknown99(3000000)
        Unknown188(2500)
    sprite('null', 4)
    sprite('null', 4)
    Unknown189(1000)
    sprite('null', 4)
    Unknown189(800)
    sprite('null', 120)
    Unknown189(1000)
    Unknown99(-500000)

@State
def GKS801_Dust():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('gks_801_bombDust')
    sprite('null', 2147483647)

@State
def GKS801_stone():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('gks_801_stone')
    sprite('null', 360)

@State
def GKS801_Aura():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown450('gks_801_aura1')
        Unknown98(0)
        Unknown188(2000)
    sprite('null', 4)
    sprite('null', 4)
    Unknown188(2500)
    sprite('null', 4)
    Unknown188(3000)
    sprite('null', 80)
    Unknown188(3500)
    sprite('null', 300)
    Unknown188(1000)
    Unknown450('gks_801_aura2')

@State
def GKS801_Manp01_01():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown451('4d4e5000000000000000000000000000000000000000000000000000000000004d4e505f474b5338303163735f30315f30310000000000000000000000000000')
    sprite('null', 2147483647)

@State
def GKS801_Manp01_02():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown451('4d4e5000000000000000000000000000000000000000000000000000000000004d4e505f474b5338303163735f30315f30320000000000000000000000000000')
    sprite('null', 2147483647)

@State
def GKS801_Manp02_01():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown451('4d4e5000000000000000000000000000000000000000000000000000000000004d4e505f474b5338303163735f30325f30310000000000000000000000000000')
    sprite('null', 2147483647)

@State
def GKS801_FaceManp02_01():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown451('4d4e5000000000000000000000000000000000000000000000000000000000004d4e505f66616365474b5338303163735f30325f30315f315f30310000000000')
    sprite('null', 2147483647)

@State
def GKScs610_HensinKaijoEff():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('gks_610_hensinkaijo')
        Unknown99(350000)
        Unknown94(-60000)
        Unknown188(700)
    sprite('null', 60)

@State
def GKS805_FRN():

    def upon_IMMEDIATE():
        Unknown92(0)
        Unknown98(0)
        Unknown1731(0)
        Unknown454(2)
        Unknown2494('46524e000000000000000000000000000000000000000000000000000000000046524e5f474b5338303563730000000000000000000000000000000000000000')
        Unknown457(2)
        Unknown2189(0, 5)
    sprite('null', 2147483647)

    def upon_3():
        onFrame(0, 0)
        ActivateEffScript('GKS805_SmokeL', 160)
        ActivateEffScript('GKS805_SmokeR', 161)
        endIf()
        onFrame(0, 48)
        ActivateEffScript('GKS805_YukaDonSmoke', 157)
        ActivateEffScript('GKS805_YukaDonSmoke2', 157)
        endIf()
        onFrame(0, 880)
        ActivateEffScript('GKS805_FRNBeam', 156)
        endIf()
        onFrame(0, 1111)
        ActivateEffScript('GKS805_FRNBeam3', 100)
        endIf()
        onFrame(0, 1183)
        ActivateEffScript('GKS805_DeleteRay', 147)
        endIf()
    Unknown3()

@State
def GKS805_Manp01_01():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown451('4d4e5000000000000000000000000000000000000000000000000000000000004d4e505f474b5338303563735f30310000000000000000000000000000000000')
        Unknown2189(0, 5)
    sprite('null', 2147483647)

@State
def GKS805_Manp01_02():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown451('4d4e5000000000000000000000000000000000000000000000000000000000004d4e505f474b5338303563735f30320000000000000000000000000000000000')
        Unknown2189(0, 5)
    sprite('null', 2147483647)

@State
def GKS805_SmokeR():

    def upon_IMMEDIATE():
        Unknown457(2)
        physicsImpulseX(15000)
        Unknown1732(175000)
        Unknown99(-15000)
    sprite('null', 7)
    Unknown2283(0, -40000)
    Unknown449('bg_undersmoke00', 100)
    sprite('null', 7)
    Unknown2283(0, -40000)
    Unknown449('bg_undersmoke00', 100)
    sprite('null', 7)
    Unknown2283(0, -40000)
    Unknown449('bg_undersmoke00', 100)
    sprite('null', 7)
    Unknown2283(0, -40000)
    Unknown449('bg_undersmoke00', 100)
    sprite('null', 7)
    Unknown2283(0, -40000)
    Unknown449('bg_undersmoke00', 100)

@State
def GKS805_SmokeL():

    def upon_IMMEDIATE():
        Unknown457(2)
        physicsImpulseX(15000)
        Unknown1732(-175000)
        Unknown99(-15000)
    sprite('null', 7)
    Unknown2283(0, 40000)
    Unknown449('bg_undersmoke00', 100)
    sprite('null', 7)
    Unknown2283(0, 40000)
    Unknown449('bg_undersmoke00', 100)
    sprite('null', 7)
    Unknown2283(0, 40000)
    Unknown449('bg_undersmoke00', 100)
    sprite('null', 7)
    Unknown2283(0, 40000)
    Unknown449('bg_undersmoke00', 100)
    sprite('null', 7)
    Unknown2283(0, 40000)
    Unknown449('bg_undersmoke00', 100)

@State
def GKS805_YukaDonSmoke():

    def upon_IMMEDIATE():
        Unknown99(-30000)
        Unknown94(-25000)
        Unknown457(2)
    sprite('null', 1)
    Unknown2273(0, 300)
    Unknown449('bg_undersmoke00', 100)

@State
def GKS805_YukaDonSmoke2():

    def upon_IMMEDIATE():
        Unknown99(-30000)
        Unknown94(25000)
        Unknown457(2)
    sprite('null', 1)
    Unknown2273(0, 300)
    Unknown2283(0, -180000)
    Unknown449('bg_undersmoke00', 100)

@State
def GKS805_FRNBeam():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('gks_805_FRNbeam1')
        Unknown164(-38000)
        Unknown232(20000)
        Unknown99(150000)
        Unknown94(-175000)
        Unknown1732(-175000)
        Unknown188(1300)
    sprite('null', 120)
    Unknown191(0)

@State
def GKS805_FRNBeam2():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('gks_805_FRNbeam2')
        Unknown164(-10000)
    sprite('null', 80)
    Unknown191(0)

@State
def GKS805_FRNBeam3():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('gks_805_FRNbeam3')
        Unknown94(700000)
        Unknown1732(200000)
    sprite('null', 28)
    sprite('null', 8)
    Unknown450('gks_805_FRNbeam4')
    sprite('null', 36)
    Unknown450('gks_805_flash')

@State
def GKS805_DeleteRay():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('gks_805_DeleteRay')
    sprite('null', 250)

@State
def GKS805_Hinoko():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('gks_805_hinoko')
        Unknown94(150000)
        Unknown99(-150000)
        Unknown188(700)
    sprite('null', 130)

@State
def GKS808_BUK():

    def upon_IMMEDIATE():
        Unknown92(0)
        Unknown98(0)
        Unknown1731(0)
        Unknown454(2)
        Unknown2494('42554b000000000000000000000000000000000000000000000000000000000042554b5f474b5338303863730000000000000000000000000000000000000000')
        Unknown457(2)
        Unknown2189(0, 5)
    sprite('null', 2147483647)

@State
def GKS808_Manp01_01():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown451('4d4e5000000000000000000000000000000000000000000000000000000000004d4e505f474b5338303863735f30310000000000000000000000000000000000')
        Unknown2189(0, 5)
    sprite('null', 2147483647)

@State
def GKS808_Manp01_02():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown451('4d4e5000000000000000000000000000000000000000000000000000000000004d4e505f474b5338303863735f30320000000000000000000000000000000000')
        Unknown2189(0, 5)
    sprite('null', 2147483647)

@State
def GKS808_kaijo():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown450('gks_808_kaijo')
        Unknown94(80000)
        Unknown1732(23000)
    sprite('null', 3)
    sprite('null', 4)
    Unknown94(200000)
    Unknown99(-80000)
    Unknown1732(-23000)
    sprite('null', 4)
    Unknown94(250000)
    sprite('null', 8)
    Unknown94(150000)

@State
def GKS808_Warp():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('gks_808_warp')
        Unknown232(90000)
    sprite('null', 40)

@State
def GKS808_Tame():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown99(450000)
        Unknown1732(100000)
        Unknown94(50000)
        Unknown188(340)
    sprite('null', 40)
    sprite('null', 200)
    Unknown450('gks_808_tameRay')

@State
def GKS808_zuzaa():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('gks_808_zuzaa')
        Unknown94(500000)
        Unknown239()
    sprite('null', 120)

@State
def GKS808_GenkiDama():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('gks_808_genkidama1')
        Unknown99(2500000)
        Unknown188(8500)
        Unknown164(-20000)
        Unknown35('170000004d6f766500000000000000000000000000000000000000000000000000000000')
        Unknown35('180000004d6f766532000000000000000000000000000000000000000000000000000000')
        Unknown35('1900000053746f7000000000000000000000000000000000000000000000000000000000')
        Unknown35('1a00000053746f7032000000000000000000000000000000000000000000000000000000')
        Unknown35('1b0000004d6f766533000000000000000000000000000000000000000000000000000000')
        Unknown35('1c0000004d6f766534000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    label('Move')
    sprite('null', 2147483647)
    Unknown450('gks_808_genkidama2')
    Unknown94(3700000)
    Unknown99(240000)
    Unknown1732(-1000000)
    Unknown188(4000)
    physicsImpulseY(-2000)
    physicsImpulseX(3000)
    Unknown164(45000)
    label('Move2')
    sprite('null', 2147483647)
    Unknown164(20000)
    Unknown99(-4000000)
    Unknown94(-400000)
    Unknown1732(-300000)
    Unknown188(2000)
    physicsImpulseY(-8000)
    physicsImpulseX(12000)
    Unknown1736(-2000)
    label('Stop')
    sprite('null', 2147483647)
    Unknown450('gks_808_genkidama3')
    Unknown164(0)
    Unknown1732(300000)
    Unknown94(-900000)
    Unknown99(270000)
    Unknown188(5000)
    physicsImpulseY(0)
    physicsImpulseX(0)
    Unknown1736(0)
    label('Stop2')
    sprite('null', 2147483647)
    Unknown450('gks_808_genkidama2')
    label('Move3')
    sprite('null', 25)
    Unknown450('gks_808_genkidama4')
    Unknown1732(300000)
    Unknown98(0)
    Unknown188(2800)
    Unknown191(15)
    physicsImpulseX(750)
    sprite('null', 5)
    Unknown191(300)
    physicsImpulseX(75000)
    sprite('null', 10)
    Unknown191(100)
    physicsImpulseX(7500)
    sprite('null', 2147483647)
    Unknown191(0)
    physicsImpulseX(3750)
    label('Move4')
    sprite('null', 4)
    Unknown450('gks_808_genkidama_nomikomi')
    Unknown188(1500)
    physicsImpulseX(0)
    Unknown1732(270000)
    Unknown94(400000)
    Unknown99(250000)
    sprite('null', 16)
    Unknown188(1700)
    sprite('null', 4)
    Unknown94(200000)
    sprite('null', 240)
    Unknown164(0)
    Unknown94(200000)
    Unknown99(100000)
    Unknown191(8)

@State
def GKS808_GenkiDamaSmoke():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown1732(1000000)
        Unknown94(400000)
    label('Loop')
    sprite('null', 7)
    Unknown2283(0, -70000)
    Unknown2273(0, 2000)
    Unknown449('bg_undersmoke00', 100)
    labelEnd('Loop')

@State
def GKS808_GenkiDamaSmoke2():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown1732(-500000)
        Unknown94(2000000)
    label('Loop')
    sprite('null', 7)
    Unknown2283(0, 220000)
    Unknown2273(0, 2000)
    Unknown449('bg_undersmoke00', 100)
    labelEnd('Loop')

@State
def GKS808_RayBoo():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('gks_808_ray3')
        Unknown94(1650000)
        Unknown99(200000)
        Unknown1732(100000)
        Unknown188(1500)
    sprite('null', 2147483647)

@State
def GKS808_Ray():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('gks_808_ray')
        Unknown35('170000004d6f766500000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    label('Move')
    sprite('null', 2147483647)
    Unknown99(-70000)
    Unknown94(60000)
    Unknown1732(20000)
    Unknown188(1000)

@State
def GKS808_ChangeSS():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('gks_808_changeSS')
    sprite('null', 60)

@State
def GKS808_kaijo2():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown450('gks_808_kaijo2')
        Unknown188(500)
    sprite('null', 30)

@State
def GKS808_Ray2():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('gks_808_ray2')
        Unknown35('170000004d6f766500000000000000000000000000000000000000000000000000000000')
        Unknown188(3500)
    sprite('null', 2147483647)

@State
def GKS808_EndParticle():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('gks_808_genkidamaEnd')
        Unknown99(1400000)
        Unknown94(-300000)
        Unknown188(350)
    sprite('null', 2147483647)

@State
def GKS814_brs():

    def upon_IMMEDIATE():
        Unknown92(0)
        Unknown98(0)
        Unknown1731(0)
        Unknown454(2)
        Unknown2494('62727300000000000000000000000000000000000000000000000000000000006272735f474b5338313463730000000000000000000000000000000000000000')
        Unknown457(2)
        Unknown2189(0, 5)
        Unknown35('17000000426f6d6200000000000000000000000000000000000000000000000000000000')
        Unknown35('180000004b697a756b690000000000000000000000000000000000000000000000000000')
    sprite('null', 3000)
    Unknown3()
    label('Kizuki')
    sprite('null', 30000)
    ActivateEffScript('GKS814_Kizuki', 149)
    Unknown3()
    label('Bomb')
    sprite('null', 3000)
    ActivateEffScript('GKS814_Bom', 147)
    Unknown3()

@State
def GKS814_Manp01_01():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown451('4d4e5000000000000000000000000000000000000000000000000000000000004d4e505f474b5338313463735f30310000000000000000000000000000000000')
        Unknown2189(0, 5)
    sprite('null', 2147483647)

@State
def GKS814_Manp01_02():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown451('4d4e5000000000000000000000000000000000000000000000000000000000004d4e505f474b5338313463735f30320000000000000000000000000000000000')
        Unknown2189(0, 5)
    sprite('null', 2147483647)

@State
def GKS814_BlackWipe():

    def upon_IMMEDIATE():
        Unknown457(2)
    sprite('null', 2147483647)
    Unknown450('gks_814_wipe')

@State
def GKS814_Kizuki():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown188(300)
        Unknown1732(-25000)
        Unknown99(15000)
    sprite('null', 30)
    Unknown450('gks_814_kizuki')

@State
def GKS814_SmokeR():

    def upon_IMMEDIATE():
        Unknown457(2)
        physicsImpulseX(15000)
        Unknown94(1700000)
        Unknown1732(150000)
        Unknown99(-15000)
    sprite('null', 7)
    Unknown2283(0, -25000)
    Unknown449('bg_undersmoke00', 100)
    sprite('null', 7)
    Unknown2283(0, -25000)
    Unknown449('bg_undersmoke00', 100)

@State
def GKS814_SmokeL():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown94(1700000)
        physicsImpulseX(15000)
        Unknown1732(-150000)
        Unknown99(-15000)
    sprite('null', 7)
    Unknown2283(0, 25000)
    Unknown449('bg_undersmoke00', 100)
    sprite('null', 7)
    Unknown2283(0, 25000)
    Unknown449('bg_undersmoke00', 100)

@State
def GKS814_PunchWind():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('gks_814_punchWind')
        Unknown94(450000)
        Unknown1732(150000)
        Unknown99(-35000)
        Unknown188(1200)
    sprite('null', 60)

@State
def GKS814_CmnWind():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('gks_814_punchWind3')
    sprite('null', 120)

@State
def GKS814_Ray():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('gks_814_ray')
        Unknown1732(-50000)
        Unknown94(150000)
        Unknown99(215000)
    sprite('null', 120)

@State
def GKS814_FaceSparkMatome():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown457(2)
        Unknown454(2)
        Unknown1976(1)
        Unknown289(10000)
    sprite('null', 68)
    Unknown479('474b533831345f46616365537061726b000000000000000000000000000000000100000001000000')

@State
def GKS814_FaceSpark():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('gks_814_spark')
        Unknown1732(-500000)
    sprite('null', 68)

@State
def GKS814_Bom():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('gks_814_bomb01')
        Unknown99(18000)
        Unknown35('17000000466c617368000000000000000000000000000000000000000000000000000000')
        Unknown35('18000000426f6d6200000000000000000000000000000000000000000000000000000000')
    sprite('null', 4)
    sprite('null', 4)
    Unknown99(50000)
    sprite('null', 10)
    Unknown1732(-110000)
    Unknown99(95000)
    Unknown94(200000)
    sprite('null', 3000)
    label('Flash')
    sprite('null', 3000)
    Unknown450('gks_814_bomb02')
    Unknown232(0)
    Unknown164(0)
    Unknown188(1000)
    Unknown151(0)
    Unknown159(0)
    Unknown183(0)
    Unknown3()
    label('Bomb')
    sprite('null', 3000)
    Unknown450('gks_814_bomb03')
    Unknown232(-15000)
    Unknown164(-25000)
    Unknown3()

@State
def GKS814_EndParticle():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('gks_814_zansi')
    sprite('null', 2147483647)

@State
def GKS819_JRN():

    def upon_IMMEDIATE():
        Unknown92(0)
        Unknown98(0)
        Unknown1731(0)
        Unknown454(2)
        Unknown2494('4a524e00000000000000000000000000000000000000000000000000000000004a524e5f474b5338313963730000000000000000000000000000000000000000')
        Unknown457(2)
        Unknown2189(0, 5)
        Unknown2379(0, 2)
    sprite('null', 2147483647)

    def upon_3():
        onFrame(0, 75)
        ActivateEffScript('GKS819_fire01_EFF', 147)
        endIf()
        onFrame(0, 83)
        ActivateEffScript('GKS819_jrn_aura01_EFF', 147)
        endIf()
        onFrame(0, 119)
        ActivateEffScript('GKS819_jrn_fire01_EFF', 160)
        endIf()
        onFrame(0, 124)
        Unknown32('GKS819_jrn_aura01_EFF')
        endIf()
        onFrame(0, 154)
        Unknown32('GKS819_jrn_fire01_EFF')
        ActivateEffScript('GKS819_jrn_fire02_EFF', 160)
        endIf()
        onFrame(0, 171)
        ActivateEffScript('GKS819_guard01_EFF', 100)
        endIf()
        onFrame(0, 186)
        Unknown1803('GKS819_guard01_EFF', 23)
        endIf()
        onFrame(0, 187)
        Unknown32('GKS819_jrn_fire02_EFF')
        endIf()
        onFrame(0, 307)
        ActivateEffScript('GKS819_smoke_wipe01_EFF', 100)
        endIf()
        onFrame(0, 315)
        Unknown32('GKS819_guard01_EFF')
        endIf()
        onFrame(0, 350)
        Unknown1803('GKS819_smoke_wipe01_EFF', 23)
        endIf()
        onFrame(0, 355)
        Unknown1803('GKS819_smoke_wipe01_EFF', 24)
        endIf()
        onFrame(0, 515)
        ActivateEffScript('GKS819_line01_EFF', 100)
        endIf()
        onFrame(0, 543)
        Unknown32('GKS819_line01_EFF')
        ActivateEffScript('GKS819_line02_EFF', 100)
        endIf()
        onFrame(0, 627)
        Unknown32('GKS819_line02_EFF')
        endIf()
        onFrame(0, 831)
        ActivateEffScript('GKS819_line03_EFF', 100)
        endIf()
        onFrame(0, 863)
        Unknown32('GKS819_line03_EFF')
        ActivateEffScript('GKS819_groundsmoke06_EFF', 100)
        endIf()
        onFrame(0, 927)
        Unknown32('GKS819_groundsmoke06_EFF')
        endIf()
        onFrame(0, 1075)
        ActivateEffScript('GKS819_aura01_end_EFF', 100)
        endIf()
        onFrame(0, 1087)
        ActivateEffScript('GKS819_ground_break01_EFF', 100)
        endIf()
        onFrame(0, 1099)
        Unknown2095(0, 1)
        Unknown1803('GKS819_ground_break01_EFF', 23)
        endIf()
        onFrame(0, 1175)
        Unknown1803('GKS819_ground_break01_EFF', 24)
        endIf()
        onFrame(0, 1231)
        Unknown32('GKS819_ground_break01_EFF')
        ActivateEffScript('GKS819_foll_glow_EFF', 100)
        endIf()
        onFrame(0, 1363)
        Unknown32('GKS819_foll_glow_EFF')
        ActivateEffScript('GKS819_foll_glow2_EFF', 100)
        endIf()
        onFrame(0, 1511)
        Unknown32('GKS819_foll_glow2_EFF')
        ActivateEffScript('GKS819_scr_split01_EFF', 100)
        Unknown2096(1)
        endIf()
        onFrame(0, 1679)
        Unknown2095(0, 1)
        Unknown32('GKS819_scr_split01_EFF')
        ActivateEffScript('GKS819_DestructionBG_EFF', 100)
        endIf()
        onFrame(0, 1691)
        ActivateEffScript('GKS819_Destruction01_EFF', 100)
        endIf()
        onFrame(0, 1739)
        Unknown1803('GKS819_Destruction01_EFF', 23)
        endIf()
        onFrame(0, 1897)
        Unknown448('gks819_smokewipe03', 100)
        Unknown2525()
        endIf()
        onFrame(0, 1907)
        Unknown2096(1)
        Unknown32('GKS819_DestructionBG_EFF')
        Unknown32('GKS819_Destruction01_EFF')
        ActivateEffScript('GKS819_JRN_BG01_EFF', 100)
        endIf()
        onFrame(0, 2043)
        ActivateEffScript('GKS819_HimoSmoke01_EFF', 100)
        endIf()
        onFrame(0, 2187)
        Unknown32('GKS819_HimoSmoke01_EFF')
        Unknown32('GKS819_JRN_BG01_EFF')
        ActivateEffScript('GKS819_JRN_BG02_EFF', 100)
        endIf()
        onFrame(0, 2431)
        Unknown32('GKS819_JRN_BG02_EFF')
        endIf()
    Unknown3()

@State
def GKS819_FRN():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown2493('66726e000000000000000000000000000000000000000000000000000000000046524e5f474b5338313963730000000000000000000000000000000000000000')
        Unknown2189(0, 5)
    sprite('null', 200)
    sprite('null', 2147483647)
    Unknown2379(0, 2)
    Unknown3()

@State
def GKS819_Manp01_01():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown451('4d4e5000000000000000000000000000000000000000000000000000000000004d4e505f474b5338313963735f30310000000000000000000000000000000000')
        Unknown2189(0, 5)
    sprite('null', 2147483647)
    Unknown3()

@State
def GKS819_Manp01_02():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown451('4d4e5000000000000000000000000000000000000000000000000000000000004d4e505f474b5338313963735f30320000000000000000000000000000000000')
        Unknown2189(0, 5)
    sprite('null', 2147483647)
    Unknown3()

@State
def GKS819_Manp01_03():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown451('4d4e5000000000000000000000000000000000000000000000000000000000004d4e505f474b5338313963735f30330000000000000000000000000000000000')
        Unknown2189(0, 5)
    sprite('null', 2147483647)
    Unknown3()

@State
def GKS819_EFFDUMMY():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown451('45464600000000000000000000000000000000000000000000000000000000004546465f474b5338313963735f30310000000000000000000000000000000000')
        Unknown2189(0, 5)
    sprite('null', 2147483647)
    Unknown3()

@State
def GKS819_fire01_EFF():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(3)
        Unknown454(2)
        Unknown456(2)
        Unknown94(-100000)
        Unknown99(-25000)
        Unknown1732(10000)
    sprite('null', 4)
    Unknown450('gks819_fire01')
    sprite('null', 4)
    Unknown188(1500)
    sprite('null', 4)
    Unknown188(3000)
    sprite('null', 4)
    Unknown188(6000)
    sprite('null', 30)
    Unknown3()

@State
def GKS819_jrn_aura01_EFF():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(3)
        Unknown454(2)
        Unknown456(2)
        Unknown99(-250000)
        Unknown1732(25000)
        Unknown450('gks819_jrn_Aura01')
    sprite('null', 2)
    Unknown188(400)
    sprite('null', 2)
    Unknown188(500)
    sprite('null', 300)
    Unknown188(800)
    Unknown3()

@State
def GKS819_jrn_fire01_EFF():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(3)
        Unknown454(2)
        Unknown456(2)
        Unknown289(300)
        Unknown450('gks819_jrn_fire01')
    sprite('null', 4)
    Unknown448('gks819_jrn_fire02', 100)
    Unknown94(-100000)
    Unknown1732(20000)
    Unknown188(450)
    sprite('null', 4)
    Unknown448('gks819_jrn_fire02', 100)
    Unknown94(-100000)
    Unknown1732(20000)
    Unknown188(750)
    label('loop')
    sprite('null', 4)
    Unknown448('gks819_jrn_fire02', 100)
    Unknown94(-100000)
    Unknown1732(20000)
    Unknown188(1000)
    labelEnd('loop')
    Unknown3()

@State
def GKS819_jrn_fire02_EFF():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(3)
        Unknown454(2)
        Unknown456(2)
        Unknown92(100000)
        Unknown1731(-100000)
        Unknown188(1250)
        Unknown289(300)
        Unknown450('gks819_jrn_fire01')
        ActivateEffScript('GKS819_jrn_fire01_glow_EFF', 100)
    label('loop')
    sprite('null', 4)
    Unknown448('gks819_jrn_fire02', 100)
    Unknown94(-200000)
    labelEnd('loop')
    Unknown3()

@State
def GKS819_jrn_fire01_glow_EFF():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(3)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 300)
    Unknown450('gks819_jrn_fire01_glow')
    Unknown3()

@State
def GKS819_guard01_EFF():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(3)
        Unknown454(2)
        Unknown456(2)
        Unknown450('gks819_guard01')
        Unknown232(220000)
        Unknown94(-1850000)
        Unknown99(250000)
        Unknown1732(110000)
        Unknown35('170000006c6f6f7000000000000000000000000000000000000000000000000000000000')
    sprite('null', 4)
    Unknown188(50)
    sprite('null', 4)
    Unknown188(750)
    sprite('null', 4)
    Unknown188(1000)
    sprite('null', 300)
    label('loop')
    sprite('null', 300)
    Unknown450('gks819_guard02')
    Unknown92(600000)
    Unknown1732(-100000)
    Unknown188(2500)
    Unknown232(165000)
    Unknown3()

@State
def GKS819_smoke_wipe01_EFF():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(3)
        Unknown454(2)
        Unknown456(2)
        Unknown35('170000006c6f6f7032000000000000000000000000000000000000000000000000000000')
        Unknown35('18000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 8)
    ActivateEffScript('GKS819_smoke_wipe00_EFF', 100)
    Unknown450('gks819_smoke_wipe01')
    Unknown94(100000)
    label('loop1')
    sprite('null', 4)
    Unknown450('gks819_smoke_wipe01_01')
    Unknown92(200000)
    sprite('null', 4)
    Unknown450('gks819_smoke_wipe01_02')
    sprite('null', 4)
    Unknown450('gks819_smoke_wipe01_03')
    sprite('null', 4)
    Unknown450('gks819_smoke_wipe01_04')
    labelEnd('loop1')
    label('loop2')
    sprite('null', 4)
    Unknown94(-2200000)
    Unknown99(-80000)
    Unknown1732(500000)
    Unknown450('gks819_smoke_wipe01_01')
    sprite('null', 4)
    Unknown450('gks819_smoke_wipe01_02')
    sprite('null', 4)
    Unknown450('gks819_smoke_wipe01_03')
    sprite('null', 4)
    Unknown450('gks819_smoke_wipe01_04')
    sprite('null', 4)
    Unknown450('gks819_smoke_wipe01_01')
    sprite('null', 4)
    Unknown450('gks819_smoke_wipe01_02')
    sprite('null', 4)
    Unknown450('gks819_smoke_wipe01_03')
    sprite('null', 4)
    Unknown450('gks819_smoke_wipe01_04')
    label('end')
    sprite('null', 4)
    Unknown450('gks819_smoke_wipe01_end')
    sprite('null', 4)
    Unknown94(-100000)
    sprite('null', 4)
    Unknown94(-100000)
    sprite('null', 60)
    Unknown94(-100000)
    Unknown3()

@State
def GKS819_smoke_wipe00_EFF():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(3)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 100)
    Unknown450('gks819_smoke_wipe00')
    Unknown3()

@State
def GKS819_line01_EFF():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(3)
        Unknown454(2)
        Unknown456(2)
        Unknown92(-2400000)
        Unknown98(270000)
        Unknown1731(90000)
        Unknown188(125)
    sprite('null', 4)
    Unknown450('gks819_line01')
    sprite('null', 4)
    Unknown94(20000)
    Unknown1732(-15000)
    sprite('null', 4)
    Unknown94(20000)
    Unknown1732(-15000)
    sprite('null', 4)
    Unknown94(20000)
    Unknown1732(-15000)
    sprite('null', 4)
    Unknown94(20000)
    Unknown1732(-15000)
    sprite('null', 4)
    Unknown94(20000)
    Unknown1732(-15000)
    Unknown3()

@State
def GKS819_line02_EFF():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(3)
        Unknown454(2)
        Unknown456(2)
        Unknown99(100000)
    sprite('null', 300)
    Unknown450('gks819_line02')
    Unknown3()

@State
def GKS819_groundsmoke06_EFF():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(3)
        Unknown454(2)
        Unknown456(2)
        Unknown94(246000)
        Unknown1732(25000)
    sprite('null', 90)
    Unknown450('gks819_groundsmoke06')
    Unknown3()

@State
def GKS819_line03_EFF():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(3)
        Unknown454(2)
        Unknown456(2)
        Unknown98(270000)
        Unknown1731(35000)
        Unknown232(90000)
        Unknown188(150)
    sprite('null', 28)
    Unknown450('gks819_line03')
    sprite('null', 6)
    Unknown164(180000)
    Unknown188(700)
    Unknown94(100000)
    Unknown99(-75000)
    Unknown3()

@State
def GKS819_aura01_end_EFF():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(3)
        Unknown454(2)
        Unknown456(2)
        Unknown164(225000)
        Unknown232(90000)
        Unknown99(1200000)
        Unknown1732(1200000)
    sprite('null', 60)
    Unknown450('gks819_aura01_end')
    Unknown3()

@State
def GKS819_ground_break01_EFF():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(3)
        Unknown454(2)
        Unknown456(2)
        Unknown232(90000)
        Unknown35('170000006c6f6f7000000000000000000000000000000000000000000000000000000000')
        Unknown35('18000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 120)
    Unknown450('gks819_ground_break01')
    label('loop')
    sprite('null', 300)
    Unknown450('gks819_ground_break02')
    Unknown232(-90000)
    Unknown164(45000)
    Unknown188(4500)
    Unknown99(200000)
    label('end')
    sprite('null', 120)
    Unknown450('gks819_ground_break03')
    Unknown188(1500)
    Unknown1732(350000)
    Unknown99(350000)
    Unknown164(225000)
    physicsImpulseY(240000)
    Unknown1736(240000)
    Unknown3()

@State
def GKS819_foll_glow_EFF():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(3)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 300)
    Unknown450('gks819_scr_foll00')
    Unknown3()

@State
def GKS819_foll_glow2_EFF():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(3)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 300)
    Unknown450('gks819_scr_foll01')
    Unknown3()

@State
def GKS819_scr_split01_EFF():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(3)
        Unknown454(2)
        Unknown456(2)
        Unknown239()
        Unknown450('gks819_scr_split01')
        Unknown99(300000)
        Unknown188(350)
    sprite('null', 31)
    sprite('null', 4)
    Unknown94(-2500)
    sprite('null', 4)
    Unknown94(5000)
    sprite('null', 4)
    Unknown94(-5000)
    sprite('null', 4)
    Unknown94(5000)
    sprite('null', 4)
    Unknown94(-10000)
    sprite('null', 4)
    Unknown94(10000)
    sprite('null', 4)
    Unknown94(-10000)
    sprite('null', 4)
    Unknown94(15000)
    sprite('null', 4)
    Unknown94(-15000)
    sprite('null', 300)
    Unknown92(0)
    Unknown3()

@State
def GKS819_Destruction01_EFF():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(3)
        Unknown454(2)
        Unknown456(2)
        Unknown239()
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 300)
    Unknown450('gks819_shine_Landing01')
    Unknown99(40000)
    label('end')
    sprite('null', 4)
    Unknown450('gks819_shine02')
    sprite('null', 4)
    Unknown188(2500)
    sprite('null', 4)
    Unknown188(5000)
    sprite('null', 300)
    Unknown239()
    Unknown450('gks819_Destruction01')
    Unknown99(5000)
    Unknown188(10000)
    Unknown3()

@State
def GKS819_smoke_wipe02_EFF():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(3)
        Unknown454(2)
        Unknown456(2)
    sprite('null', 90)
    Unknown450('gks819_smoke_wipe02')
    Unknown3()

@State
def GKS819_DestructionBG_EFF():

    def upon_IMMEDIATE():
        Unknown239()
        Unknown457(2)
        Unknown458(3)
        Unknown188(10000)
    sprite('null', 2147483647)
    Unknown450('gks819_DestructionBG')
    Unknown3()

@State
def GKS819_JRN_BG01_EFF():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(3)
        Unknown454(2)
        Unknown456(2)
        Unknown1732(-250000)
    sprite('null', 2147483647)
    Unknown450('gks819_BG02')
    Unknown3()

@State
def GKS819_JRN_BG02_EFF():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(3)
        Unknown454(2)
        Unknown456(2)
        Unknown1732(-230000)
        Unknown94(75000)
    sprite('null', 2147483647)
    Unknown450('gks819_BG02')
    Unknown3()

@State
def GKS819_HimoSmoke01_EFF():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown458(3)
        Unknown454(2)
        Unknown456(2)
        Unknown94(-3116148)
        Unknown99(243489)
        Unknown1732(-1870777)
    sprite('null', 2147483647)
    Unknown450('gks819_HimoSmoke01')
    Unknown3()

@State
def DUMMYDUMMY():
    sprite('null', 1)