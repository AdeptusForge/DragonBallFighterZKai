@State
def cmn_Dummy():
    sprite('null', 2147483647)

@Subroutine
def cmn_EnvInit():
    pass

@Subroutine
def cmn_SkillInit():
    move_register('CmnNeutral')
    Unknown1405(0)
    move_state(0)
    move_alias('')
    Unknown1506(0)
    move_endregister()
    move_register('CmnStandForce')
    Unknown1405(17)
    move_state(1)
    move_alias('CmnActStand')
    Unknown1538(0)
    move_input(55)
    move_input(68)
    move_input(81)
    move_input(94)
    move_endregister()
    move_register('CmnFWalk')
    Unknown1405(1)
    move_state(1)
    Unknown1411(1)
    move_input(120)
    move_alias('CmnActFWalk')
    move_endregister()
    move_register('CmnFDash')
    Unknown1405(3)
    move_state(1)
    Unknown1411(1)
    move_input(217)
    move_alias('CmnActFDash')
    move_endregister()
    move_register('CmnActFDash2Button')
    Unknown1405(47)
    move_state(1)
    Unknown1411(1)
    move_input(121)
    move_input(22)
    move_input(31)
    move_alias('CmnActFDash')
    move_endregister()
    move_register('CmnBWalk')
    Unknown1405(2)
    move_state(1)
    Unknown1411(1)
    move_input(94)
    move_alias('CmnActBWalk')
    move_endregister()
    move_register('CmnBDash')
    Unknown1405(4)
    move_state(1)
    Unknown1411(1)
    move_input(289)
    move_alias('CmnActBDash')
    move_endregister()
    move_register('CmnVJump')
    Unknown1405(7)
    move_state(1)
    move_input(147)
    Unknown1411(6)
    move_alias('CmnActJumpPre')
    Unknown1422(16388)
    Unknown1574()
    move_endregister()
    move_register('CmnBJump')
    Unknown1405(6)
    move_state(1)
    move_input(147)
    move_input(95)
    Unknown1411(6)
    move_alias('CmnActJumpPre')
    Unknown1422(65540)
    Unknown1574()
    move_endregister()
    move_register('CmnFJump')
    Unknown1405(5)
    move_state(1)
    move_input(147)
    move_input(121)
    Unknown1411(6)
    move_alias('CmnActJumpPre')
    Unknown1422(32772)
    Unknown1574()
    move_endregister()
    move_register('CmnVHighJump')
    Unknown1405(10)
    move_state(1)
    move_input(147)
    move_input(215)
    Unknown1411(6)
    Unknown1411(1)
    move_alias('CmnActJumpPre')
    Unknown1422(16386)
    Unknown1574()
    move_endregister()
    move_register('CmnBHighJump')
    Unknown1405(9)
    move_state(1)
    move_input(147)
    move_input(95)
    move_input(215)
    Unknown1411(6)
    Unknown1411(1)
    move_alias('CmnActJumpPre')
    Unknown1422(65538)
    Unknown1574()
    move_endregister()
    move_register('CmnFHighJump')
    Unknown1405(8)
    move_state(1)
    move_input(147)
    move_input(121)
    move_input(215)
    Unknown1411(6)
    Unknown1411(1)
    move_alias('CmnActJumpPre')
    Unknown1422(32770)
    Unknown1574()
    move_endregister()
    move_register('CmnVAirJump')
    Unknown1405(13)
    move_state(3)
    move_input(216)
    Unknown1411(6)
    Unknown1411(110)
    move_alias('CmnActJumpPre')
    Unknown1422(16388)
    move_endregister()
    move_register('CmnBAirJump')
    Unknown1405(12)
    move_state(3)
    move_input(216)
    move_input(95)
    Unknown1411(6)
    Unknown1411(110)
    move_alias('CmnActJumpPre')
    Unknown1422(65540)
    move_endregister()
    move_register('CmnFAirJump')
    Unknown1405(11)
    move_state(3)
    move_input(216)
    move_input(121)
    Unknown1411(6)
    Unknown1411(110)
    move_alias('CmnActJumpPre')
    Unknown1422(32772)
    move_endregister()
    move_register('CmnBAirDash')
    Unknown1405(15)
    move_state(3)
    move_input(218)
    Unknown1411(7)
    Unknown1411(2)
    Unknown1411(77)
    move_alias('CmnActAirBDash')
    move_endregister()
    move_register('CmnFAirDash')
    Unknown1405(14)
    move_state(3)
    move_input(217)
    Unknown1411(7)
    Unknown1411(2)
    Unknown1411(77)
    move_alias('CmnActAirFDash')
    move_endregister()
    move_register('CmnActFAirDash2Button')
    Unknown1405(49)
    move_state(3)
    move_input(121)
    move_input(22)
    move_input(31)
    Unknown1411(7)
    Unknown1411(2)
    Unknown1411(77)
    move_alias('CmnActAirFDash')
    move_endregister()
    move_register('CmnActRushStart')
    Unknown1405(38)
    move_state(0)
    move_input(299)
    move_alias('CmnActRushStart')
    Unknown1525(-526, -381, 495, 320)
    Unknown1567()
    Unknown1538(50)
    Unknown1539(30)
    move_endregister()
    move_register('RequestChangeMember1')
    Unknown1405(29)
    move_state(0)
    move_input(120)
    move_input(293)
    move_input(273)
    move_input(295)
    move_input(301)
    Unknown1411(135)
    Unknown1411(133)
    Unknown1423(0, 100)
    Unknown1424('cmn_ReqChangeMember1')
    Unknown1539(50)
    Unknown1569()
    move_endregister()
    move_register('RequestChangeMember2')
    Unknown1405(29)
    move_state(0)
    move_input(120)
    move_input(294)
    move_input(273)
    move_input(296)
    move_input(301)
    Unknown1411(135)
    Unknown1411(134)
    Unknown1423(1, 100)
    Unknown1424('cmn_ReqChangeMember2')
    Unknown1539(50)
    Unknown1569()
    move_endregister()
    move_register('RequestChangeMemberUltimate1_1')
    Unknown1405(30)
    move_state(0)
    move_input(175)
    move_input(293)
    Unknown1411(135)
    Unknown1411(146)
    Unknown1411(4)
    Unknown1423(0, 50)
    Unknown1408()
    endElse()
    Unknown1424('cmn_ReqChangeMemberUltimate1_1')
    Unknown1539(70)
    move_endregister()
    move_register('RequestChangeMemberUltimate1_2')
    Unknown1405(30)
    move_state(0)
    move_input(177)
    move_input(293)
    Unknown1411(135)
    Unknown1411(146)
    Unknown1411(138)
    Unknown1423(0, 50)
    Unknown1408()
    endElse()
    Unknown1424('cmn_ReqChangeMemberUltimate1_2')
    Unknown1539(100)
    move_endregister()
    move_register('RequestChangeMemberUltimate2_1')
    Unknown1405(30)
    move_state(0)
    move_input(175)
    move_input(294)
    Unknown1411(135)
    Unknown1411(147)
    Unknown1411(4)
    Unknown1423(1, 50)
    Unknown1408()
    endElse()
    Unknown1424('cmn_ReqChangeMemberUltimate2_1')
    Unknown1539(70)
    move_endregister()
    move_register('RequestChangeMemberUltimate2_2')
    Unknown1405(30)
    move_state(0)
    move_input(177)
    move_input(294)
    Unknown1411(135)
    Unknown1411(147)
    Unknown1411(138)
    Unknown1423(1, 50)
    Unknown1408()
    endElse()
    Unknown1424('cmn_ReqChangeMemberUltimate2_2')
    Unknown1539(100)
    move_endregister()
    move_register('RequestAssistAttack1')
    Unknown1405(27)
    move_state(1)
    move_input(128)
    move_input(297)
    move_alias('ZAttack1')
    move_endregister()
    move_register('RequestAssistAttack2')
    Unknown1405(27)
    move_state(1)
    move_input(128)
    move_input(298)
    move_alias('ZAttack2')
    move_endregister()
    move_register('CmnChangeEnterAttack')
    Unknown1405(31)
    move_state(0)
    move_alias('CmnActHomingDash')
    Unknown1411(135)
    Unknown1411(132)
    move_endregister()
    move_register('CmnChangeEnterAttackUltimate1')
    Unknown1405(32)
    move_state(0)
    move_alias('ChangeEnterAttackUltimate1')
    Unknown1411(135)
    Unknown1411(145)
    Unknown1539(70)
    move_endregister()
    move_register('CmnChangeEnterAttackUltimate2')
    Unknown1405(33)
    move_state(0)
    move_alias('ChangeEnterAttackUltimate2')
    Unknown1411(135)
    Unknown1411(145)
    Unknown1539(70)
    move_endregister()
    move_register('CmnGuardCancelChangeEnterAttack')
    Unknown1405(36)
    move_state(0)
    move_alias('CmnActHomingDash')
    Unknown1411(135)
    Unknown1411(145)
    Unknown1539(70)
    move_endregister()
    move_register('CmnActHomingDash')
    Unknown1405(37)
    move_state(0)
    move_input(128)
    move_input(5)
    move_input(14)
    move_input(22)
    move_input(31)
    move_alias('CmnActHomingDash')
    Unknown1560()
    Unknown1539(30)
    move_endregister()
    move_register('CmnActMikiwameMove')
    Unknown1405(39)
    move_state(0)
    move_input(5)
    move_input(13)
    move_input(22)
    move_input(32)
    Unknown1411(4)
    Unknown1560()
    move_alias('CmnActMikiwameMove')
    Unknown1569()
    Unknown1562()
    Unknown1538(10)
    Unknown1539(50)
    Unknown1540(600)
    move_endregister()
    move_register('CmnActShotHajiki')
    Unknown1405(41)
    move_state(1)
    move_input(94)
    move_input(23)
    move_input(31)
    Unknown1412(1)
    Unknown1575()
    Unknown1539(80)
    move_endregister()
    move_register('CmnActKiaitame')
    Unknown1405(45)
    Unknown1414(5)
    move_state(1)
    move_input(4)
    move_input(31)
    move_input(14)
    move_input(23)
    Unknown1412(1)
    Unknown1562()
    Unknown1539(20)
    move_endregister()
    move_register('CmnActGuardCancelAttack')
    Unknown1405(22)
    move_state(1)
    Unknown1433(4)
    move_input(121)
    move_input(293)
    move_input(273)
    move_input(121)
    move_input(294)
    Unknown1411(4)
    Unknown1411(144)
    Unknown1569()
    Unknown1539(70)
    Unknown1540(600)
    move_endregister()
    move_register('RequestGuardCancelChangeMember1')
    Unknown1405(46)
    move_state(1)
    Unknown1433(4)
    move_input(121)
    move_input(293)
    Unknown1411(135)
    Unknown1411(148)
    Unknown1411(4)
    Unknown1423(0, 100)
    Unknown1424('cmn_ReqGuardCancelChangeMember1')
    Unknown1569()
    Unknown1539(70)
    Unknown1540(900)
    move_endregister()
    move_register('RequestGuardCancelChangeMember2')
    Unknown1405(46)
    move_state(1)
    Unknown1433(4)
    move_input(121)
    move_input(294)
    Unknown1411(135)
    Unknown1411(149)
    Unknown1411(4)
    Unknown1423(1, 100)
    Unknown1424('cmn_ReqGuardCancelChangeMember2')
    Unknown1569()
    Unknown1539(70)
    Unknown1540(900)
    move_endregister()
    move_register('CmnActSparkingBurst')
    Unknown1405(44)
    move_state(0)
    move_input(4)
    move_input(13)
    move_input(22)
    move_input(31)
    Unknown1411(104)
    Unknown1569()
    Unknown1582()
    Unknown1539(80)
    move_endregister()

@Subroutine
def cmn_RoundInit():
    Unknown1212(9800)
    Unknown1213(8200)
    Unknown1214(29000)
    Unknown1215(47000)
    Unknown1216(0)
    Unknown1217(0)
    Unknown1218(14500)
    Unknown1219(13000)
    Unknown1220(39000)
    Unknown1221(2000)
    Unknown1222(15500)
    Unknown1223(13000)
    Unknown1224(53000)
    Unknown1225(2000)
    Unknown1226(900)
    Unknown1251(36000)
    Unknown1233(11)
    Unknown1252(32000)
    Unknown1234(9)
    Unknown1242(5)
    Unknown1243(5)
    Unknown1282(3000)
    Unknown1289(4)
    Unknown1290(6)
    Unknown1291(10)
    Unknown1292(20)
    Unknown1253(155000)
    Unknown1255(155000)
    Unknown1257(155000)
    Unknown1254(220000)
    Unknown1256(160000)
    Unknown1258(260000)
    Unknown1259(-70000)
    Unknown1260(297500)
    Unknown1262(0)
    Unknown1261('080000000800000008000000080000000800000008000000')
    Unknown1268(0)
    Unknown1305(150)
    Unknown1306(420)
    Unknown1270(1000)
    Unknown1293(20000)
    Unknown1271(1000)
    Unknown1294(20000)
    Unknown1272(1000)
    Unknown1273(2000)
    Unknown1274(40000)
    Unknown1275(4000)

@Subroutine
def cmn_ReqChangeMember1():
    TagCheck(2, -1, 0)

@Subroutine
def cmn_ReqChangeMemberUltimate1_1():
    TagCheck(2, 0, -1)

@Subroutine
def cmn_ReqChangeMemberUltimate1_2():
    TagCheck(2, 1, -1)

@Subroutine
def cmn_ReqGuardCancelChangeMember1():
    TagCheck(2, -1, 1)

@Subroutine
def cmn_ReqChangeMember2():
    TagCheck(3, -1, 0)

@Subroutine
def cmn_ReqChangeMemberUltimate2_1():
    TagCheck(3, 0, -1)

@Subroutine
def cmn_ReqChangeMemberUltimate2_2():
    TagCheck(3, 1, -1)

@Subroutine
def cmn_ReqGuardCancelChangeMember2():
    TagCheck(3, -1, 1)

@Subroutine
def cmn_ReqAssistAttack1():
    Unknown1675('ZAttack1')

@Subroutine
def cmn_ReqAssistAttack2():
    Unknown1675('ZAttack2')

@Subroutine
def cmn_ReqAssistAttackUltimate1():
    Unknown2484(2)

@Subroutine
def cmn_ReqAssistAttackUltimate2():
    Unknown2484(3)

@Subroutine
def cmnAssistAttackInit():
    Unknown2477()
    Unknown1117(0)
    Unknown1051(0)
    Unknown287(1)
    Unknown1058(1)
    Unknown1827(1)
    Unknown53(23, 2, 83, 29, 2, 83)
    Unknown94(-100000)
    Unknown98(30000)
    if SLOT_32:
        if (SLOT_83 <= (-3000000)):
            storeValue(2, 83, 0, -3000000)
    elif (SLOT_83 >= 3000000):
        storeValue(2, 83, 0, 3000000)
    if Unknown2033(23, 'AssistAttack3'):
        Unknown1128(1)

        def upon_90():
            Unknown23(90)
            storeValue(2, 51, 0, 1)

    def upon_3():
        if (SLOT_105 == 0):
            Unknown2055(0)
            if Unknown2033(23, 'AssistAttack3'):
                if SLOT_16:
                    if SLOT_214:
                        Unknown23(2)
                        Unknown23(3)
                        Unknown23(85)
                        Unknown1303(500)
                        storeValue(2, 50, 0, 1)
                        Unknown2491()
                        Unknown14('assist_c_rapid')
        if (SLOT_105 == 1):
            Unknown2315(1)
            Unknown176(1)
            Unknown240()
            Unknown448('cmn_Warp', 103)
            Unknown2055(1)
            Unknown1827(0)
            Unknown2491()
        if (SLOT_105 == 2):
            Unknown135()

    def upon_2():
        Unknown23(2)
        Unknown23(3)
        Unknown23(85)

        def upon_85():
            Unknown23(85)
            Unknown23(3)
            Unknown23(8)
            Unknown23(92)
            Unknown23(89)
            Unknown23(49)
            Unknown1827(0)
            Unknown14('end')
        Unknown287(1)
        Unknown1827(0)
        if SLOT_52:
            Unknown1827(0)
            Unknown14('end')
        else:
            Unknown14('landing')
            if Unknown2033(23, 'AssistAttack3'):
                Unknown449('cmn_Assist_C', 103)

    def upon_85():
        Unknown23(85)
        storeValue(2, 52, 0, 1)

    def upon_1():
        Unknown1304()

@Subroutine
def cmnChangeUltimateInit():
    Unknown287(1)
    Unknown251(0)
    Unknown1827(1)
    Unknown53(23, 2, 83, 35, 2, 83)
    Unknown94(-100000)
    Unknown98(30000)
    if SLOT_214:
        if SLOT_294:
            storeValue(2, 52, 0, 1)

    def upon_3():
        if (SLOT_105 == 0):
            Unknown2055(0)
        if (SLOT_105 == 1):
            Unknown2315(1)
            Unknown176(1)
            Unknown240()
            Unknown448('cmn_Warp', 103)
            Unknown2055(1)
            if SLOT_52:
                Unknown271('0700000064000000000000001e000000')
            else:
                Unknown271('07000000640000000f0000000f000000')
        if (SLOT_105 == 2):
            Unknown135()

    def upon_2():
        Unknown23(2)
        Unknown23(3)
        Unknown23(85)
        Unknown287(1)
        Unknown14('landing')

    def upon_1():
        Unknown1827(1)

@Subroutine
def cmnAssist_Pos():
    if (SLOT_104 <= SLOT_51):
        Unknown53(23, 2, 83, 32, 2, 83)
        Unknown94(-190000)
    else:
        Unknown54('00000000020000003300000000000000d019fdff')
        if SLOT_32:
            Unknown54('0100000002000000530000000200000033000000')
        else:
            Unknown54('0000000002000000530000000200000033000000')
    if SLOT_214:
        if conditionalunk2498(32, 2, 30):
            Unknown94(180000)
    if SLOT_32:
        if (SLOT_83 <= (-3000000)):
            storeValue(2, 83, 0, -3000000)
    elif (SLOT_83 >= 3000000):
        storeValue(2, 83, 0, 3000000)
    storeValue(2, 51, 0, 0)

@Subroutine
def cmnAssist_Pos_Away():
    Unknown94(150000)
    if (not SLOT_214):
        if (SLOT_104 <= 700000):
            Unknown53(23, 2, 83, 32, 2, 83)
            Unknown94(-600000)
    if (SLOT_20 <= 800000):
        if SLOT_32:
            storeValue(2, 83, 0, -2400000)
        else:
            storeValue(2, 83, 0, 2400000)

@Subroutine
def cmnAssist_C_Pos():
    if (SLOT_104 >= 0):
        Unknown53(23, 2, 83, 32, 2, 83)
        Unknown94(-190000)
        if SLOT_214:
            if conditionalunk2498(32, 2, 30):
                Unknown53(23, 2, 83, 32, 2, 83)
                Unknown94(-1000)
    else:
        Unknown94(150000)
    if SLOT_32:
        if (SLOT_83 <= (-3000000)):
            storeValue(2, 83, 0, -3000000)
    elif (SLOT_83 >= 3000000):
        storeValue(2, 83, 0, 3000000)
    storeValue(2, 51, 0, 0)
    if SLOT_50:
        Unknown98(0)

@Subroutine
def cmnAssist3LastAtkPre_IDLING():
    if (not SLOT_52):
        storeValue(2, 52, 0, 10)

    def upon_3():
        if SLOT_51:
            if (SLOT_51 >= SLOT_52):
                Unknown23(3)
                if SLOT_16:
                    if SLOT_214:
                        if SLOT_51:
                            if (not 
                            Unknown2033(32, 'CmnActSlidedown')):
                                if (not 
                                Unknown2033(32, 'CmnActFDownLoop')):
                                    Unknown176(1)
                                    Unknown14('assist_last')
                                    Unknown23(3)
            Unknown54('0000000002000000330000000000000001000000')

@Subroutine
def cmnAssist3LastAtk():
    Unknown1059(0)
    Unknown1018(0)
    Unknown1058(0)
    Unknown1157(0)
    Unknown1142(0)
    Unknown1061(0)
    Unknown1073(0)
    Unknown1043(0)
    Unknown1974(0)
    Unknown1128(0)
    mod_opphitstop(0, 0, 0)
    Unknown1117(0)
    ChangeAtkDir(0)
    damage1(400)
    Unknown1092(90)
    Unknown1095(1000)
    Unknown1051(0)
    airHitPushbackX(15000)
    airHitPushbackY(-80000)
    untech_Override(80)
    Unknown941(20)
    mod_hitstop(16)
    or_standhit(11)
    or_launchhit(11)
    Unknown842(0)
    Unknown854(1)
    Unknown806(10000)
    Unknown808(10000)
    Unknown802(100)
    Unknown1190(1)
    Unknown1045('04000000636d6e5f6869745f737000000000000000000000000000000000000000000000')

    def upon_92():
        Unknown23(92)
        Unknown251(0)
        Unknown268(0)
        Unknown2189(2, 4)
        Unknown41(29)
        Unknown2189(2, 4)
        Unknown40()

@Subroutine
def cmnAssist_C_RapidStart():
    if SLOT_50:
        Unknown2055(1)
        Unknown448('cmn_Assist_C', 103)

@Subroutine
def cmnRendaChain_Clear_Idling():
    Unknown23(3)

    def upon_3():
        if (SLOT_105 == 10):
            Unknown1677(1)
            Unknown1678(1)
            Unknown1679(1)

@Subroutine
def cmnSpecialAttackExInit():
    Unknown1117(0)
    Unknown1204(1)
    Unknown910(0)
    Unknown296(120)
    Unknown36(13, 4)

    def upon_13():
        Unknown23(13)
        Unknown292(5000)
        Unknown448('cmn_EXstart', 103)
        Unknown612('ARC_BTL_SYS_ActSkill_Normal')

@Subroutine
def cmnSpecialAttackEx_ExeInit():
    Unknown1117(0)
    Unknown1204(1)
    Unknown910(0)

@Subroutine
def cmnSpecialAttackEx_ShotInit():
    Unknown1117(0)
    Unknown1204(1)
    Unknown910(0)

@Subroutine
def cmnSpecialAttackEx_TimeLagShotI():
    Unknown1117(0)
    Unknown910(0)

@Subroutine
def cmn1gaugeWLDSTP():
    Unknown2231(1)
    Unknown1354(1)
    Unknown1827(1)
    Unknown294(1)
    Unknown2189(2, 4)
    Unknown2078()
    Unknown296(300)

@Subroutine
def cmn3gaugeWLDSTP():
    Unknown294(1)
    Unknown2189(2, 4)
    Unknown1827(1)
    Unknown2078()
    Unknown296(300)

@Subroutine
def cmnUltimate_Clear():
    Unknown2231(0)
    Unknown1971(0)
    Unknown1354(0)

@Subroutine
def cmnUltimate_CameraCombo():
    storeValue(2, 283, 0, 1)
    storeValue(2, 284, 0, 1)
    storeValue(2, 285, 0, 1)

@Subroutine
def cmn_MutekiFollowKinshiInit():

    def upon_86():
        storeValue(2, 52, 0, 0)

        def upon_12():
            if (not SLOT_81):
                Unknown54('0000000002000000340000000000000001000000')
                if (SLOT_52 >= 11):
                    Unknown23(12)
                    Unknown23(86)
                    Unknown1645(0)
                    Unknown1369(0)
                    Unknown1354(0)

@Subroutine
def cmn_MutekiFollowAssistKinshiIni():
    Unknown1358(0)

    def upon_91():
        Unknown23(91)
        Unknown1358(1)

@Subroutine
def cmn_NandemoEnableStand():
    Unknown2172(1)
    Unknown1347(1)
    Unknown1348(1)
    Unknown1353(1, 1)
    Unknown1334(1)
    Unknown1335(1)
    Unknown1336(1)
    Unknown1338(1)
    Unknown1339(1)
    Unknown1341(1)
    Unknown1352(1)
    Unknown1362(1)

@Subroutine
def cmn_NandemoEnableCrouch():
    Unknown2172(1)
    Unknown1347(1)
    Unknown1348(1)
    Unknown1353(1, 1)
    Unknown1335(1)
    Unknown1336(1)
    Unknown1338(1)
    Unknown1339(1)
    Unknown1341(1)
    Unknown1352(1)
    Unknown1362(1)

@Subroutine
def cmn_NandemoEnableAir():
    Unknown2172(1)
    Unknown1347(1)
    Unknown1348(1)
    Unknown1353(1, 1)
    Unknown1343(1)
    Unknown1344(1)
    Unknown1345(1)
    Unknown1352(1)
    Unknown1362(1)
    if Unknown2033(23, 'CmnActMikiwameMove'):

        def upon_36():
            Unknown2203(1)
            Unknown2172(1)

@Subroutine
def cmnAtkTemplNageDageki():
    Unknown1128(1)
    Unknown1160(1)
    Unknown1057(1)
    Unknown1051(0)
    Unknown1111(1)
    Unknown1079(1)
    Unknown1059(1)
    Unknown1075(1)
    Unknown997(0)

@Subroutine
def cmnAtkTemplNageDagekiHissori():
    callSubroutine('cmnAtkLevel_0_AtkInit')
    Unknown1128(1)
    Unknown1160(1)
    Unknown1057(1)
    Unknown1051(0)
    Unknown1079(1)
    Unknown1059(1)
    Unknown1075(1)
    Unknown997(0)
    Unknown1019(1)
    damage1(0)
    Unknown1095(0)
    Unknown1117(0)
    mod_hitstop(0)
    grHitPushbackX(0)
    Unknown1018(1)
    Unknown1058(1)
    Unknown1157(1)
    Unknown1142(1)
    Unknown1061(1)
    Unknown1073(1)
    Unknown1043(1)
    Unknown1974(1)

@Subroutine
def cmnAtkTemplNageLand():
    callSubroutine('cmnAtkLevel_0_AtkInit')
    Unknown1128(1)
    Unknown1160(1)
    Unknown1057(1)
    Unknown1051(0)
    Unknown1079(1)
    Unknown1059(1)
    Unknown1075(1)
    Unknown997(0)
    Unknown1019(1)
    damage1(0)
    Unknown1095(0)
    Unknown1117(0)
    mod_hitstop(0)
    grHitPushbackX(0)
    Unknown1157(1)
    Unknown1142(1)
    Unknown1058(1)
    Unknown1061(1)
    Unknown1073(1)
    Unknown1158(1)
    ChangeAtkDir(3)
    Unknown1100(1)
    Unknown1040(1)
    Unknown1043(1)

@Subroutine
def cmnAtkTemplNageAir():
    callSubroutine('cmnAtkLevel_0_AtkInit')
    Unknown1128(1)
    Unknown1160(1)
    Unknown1057(1)
    Unknown1051(0)
    Unknown1079(1)
    Unknown1059(1)
    Unknown1075(1)
    Unknown997(0)
    Unknown1019(1)
    damage1(0)
    Unknown1095(0)
    Unknown1117(0)
    mod_hitstop(0)
    grHitPushbackX(0)
    Unknown1157(1)
    Unknown1142(1)
    Unknown1058(1)
    Unknown1061(1)
    Unknown1073(1)
    Unknown1158(1)
    ChangeAtkDir(3)
    Unknown1100(1)
    Unknown1041(1)
    Unknown1053(1)

@Subroutine
def cmnAtkTemplNageExe():
    Unknown1160(1)
    Unknown1057(1)
    Unknown1051(0)
    Unknown1079(1)
    Unknown1143(1)
    Unknown1128(1)
    Unknown1095(0)
    grHitPushbackX(0)
    Unknown1018(1)
    Unknown1061(1)
    Unknown1073(1)
    Unknown1043(1)
    Unknown1974(1)

@Subroutine
def cmn_MutekiArmor():
    Unknown1827(1)
    Unknown1840(1)
    Unknown1839(0)
    Unknown1850(0)
    Unknown1861(0)
    Unknown1846(0)
    Unknown2292(1)

@Subroutine
def cmn_AirAtkHosei():
    Unknown1092(90)

@Subroutine
def cmn_JumpATadanHosei():
    damage1(300)
    Unknown1092(90)
    Unknown1143(1)

@Subroutine
def cmn_JumpBTadanHosei():
    damage1(500)
    Unknown1092(90)
    Unknown1143(1)

@Subroutine
def cmn_JumpCTadanHosei():
    damage1(650)
    Unknown1092(90)
    Unknown1143(1)

@Subroutine
def cmn_LandATadanHosei():
    damage1(300)
    Unknown1092(90)
    Unknown1143(1)

@Subroutine
def cmn_LandBTadanHosei():
    damage1(500)
    Unknown1143(1)

@Subroutine
def cmn_GedanHosei():
    Unknown1092(90)

@Subroutine
def cmn_KuzushiHosei():
    Unknown1092(80)

@Subroutine
def cmn_MutekiHosei():
    Unknown1092(80)

@Subroutine
def cmn_ArmorHosei():
    Unknown1092(90)

@Subroutine
def cmn_AssistHosei():
    Unknown1092(90)
    Unknown1095(1000)
    Unknown1117(0)

@Subroutine
def cmn_UltimateHosei():
    Unknown1095(1000)
    Unknown1117(0)

@Subroutine
def cmn_AssistShotHosei():
    if Unknown2033(3, 'AssistAttack'):
        Unknown1092(90)
        Unknown1095(1000)
        Unknown1117(0)
    if Unknown2033(3, 'AssistAttack2'):
        Unknown1092(90)
        Unknown1095(1000)
        Unknown1117(0)
    if Unknown2033(3, 'AssistAttack3'):
        Unknown1092(90)
        Unknown1095(1000)
        Unknown1117(0)

@Subroutine
def cmnAtkLevel_0_AtkInit():
    Unknown711(0)
    damage1(300)
    Unknown910(40)
    Unknown1095(500)
    Unknown1092(100)
    Unknown1143(0)
    Unknown1117(500)
    mod_hitstop(6)
    blockstun_override(11)
    Unknown1024(2)
    hitstun_Override(14)
    untech_Override(14)
    airHitPushbackX(10500)
    airHitPushbackY(22400)

@Subroutine
def cmnAtkLevel_1_AtkInit():
    Unknown711(1)
    damage1(400)
    Unknown910(40)
    Unknown1095(500)
    Unknown1092(100)
    Unknown1143(0)
    Unknown1117(500)
    mod_hitstop(8)
    blockstun_override(11)
    Unknown1024(2)
    hitstun_Override(16)
    untech_Override(16)
    airHitPushbackX(10500)
    airHitPushbackY(22575)

@Subroutine
def cmnAtkLevel_2_AtkInit():
    Unknown711(2)
    damage1(700)
    Unknown910(40)
    Unknown1095(500)
    Unknown1092(100)
    Unknown1143(0)
    Unknown1117(700)
    mod_hitstop(11)
    blockstun_override(15)
    Unknown1024(2)
    hitstun_Override(18)
    untech_Override(18)
    airHitPushbackX(10500)
    airHitPushbackY(23887)

@Subroutine
def cmnAtkLevel_3_AtkInit():
    Unknown711(3)
    damage1(850)
    Unknown910(40)
    Unknown1095(500)
    Unknown1092(100)
    Unknown1143(0)
    Unknown1117(1200)
    mod_hitstop(14)
    blockstun_override(15)
    Unknown1024(2)
    hitstun_Override(20)
    untech_Override(20)
    airHitPushbackX(10500)
    airHitPushbackY(24675)

@Subroutine
def cmnAtkLevel_4_AtkInit():
    Unknown711(4)
    damage1(1000)
    Unknown910(40)
    Unknown1095(500)
    Unknown1092(100)
    Unknown1143(0)
    Unknown1117(1200)
    mod_hitstop(16)
    blockstun_override(15)
    Unknown1024(2)
    hitstun_Override(22)
    untech_Override(22)
    airHitPushbackX(10500)
    airHitPushbackY(25200)

@Subroutine
def cmnNormalShot_AtkInit():
    Unknown1028(1)
    damage1(600)
    Unknown1143(1)
    Unknown1092(90)
    Unknown1117(600)
    mod_hitstop(5)

@Subroutine
def cmnSpecialShot_AtkInit():
    Unknown1028(3)
    Unknown1092(90)
    Unknown1117(1200)
    mod_hitstop(5)

@Subroutine
def cmnUltimateShot_AtkInit():
    Unknown1028(4)
    Unknown1117(0)
    mod_hitstop(5)
    Unknown1095(1000)
    Unknown737(1)

@Subroutine
def cmn_OnIdling():
    if SLOT_31:
        if SLOT_213:
            Unknown2232()
            if SLOT_263:
                storeValue(2, 286, 0, 0)
    callSubroutine('cmn_SparkingBurst_PowerUp')

@Subroutine
def cmn_okasi():
    Unknown457(2)
    Unknown454(2)
    Unknown456(2)
    Unknown289(1200)

    def upon_23():
        Unknown41(29)
        Unknown176(1)
        Unknown2029('020000002000000072000000000000000000000000000000000000000000000060ea000000000000204e0000')
        Unknown40()

        def upon_3():
            if (SLOT_14 <= 300000):
                if (not SLOT_46):
                    storeValue(2, 46, 0, 1)
                    Unknown41(29)
                    Unknown111(10)
                    Unknown2029('02000000160000007200000000000000000000000000000000000000000000003075000000000000e8030000')
                    Unknown40()
            Unknown52('03000000020000000e00000000000000d0070000020000002d000000')
            Unknown54('00000000020000002d000000000000002c010000')
            if (SLOT_45 <= 1000):
                Unknown54('01000000020000002d0000000200000063000000')
                if (SLOT_45 >= (-30)):
                    Unknown54('000000000200000063000000020000002d000000')
                else:
                    Unknown54('00000000020000006300000000000000e2ffffff')

        def upon_1():
            Unknown41(29)
            Unknown176(1)
            Unknown2025()
            Unknown40()

@Subroutine
def cmnFDashStopInit():
    Unknown36(13, 70)

    def upon_13():
        Unknown27('CmnActFDashStop')

@Subroutine
def cmnAirFDashInit():
    if Unknown2030('NmlAtk6B'):
        Unknown127(1300)

@Subroutine
def cmnBDashStopInit():
    physicsImpulseX(-8000)
    Unknown2229(85)
    Unknown1341(1)
    Unknown1347(1)
    Unknown1348(1)
    Unknown1364(1)

    def upon_3():
        onFrame(0, 4)
        endIf()
        onFrame(0, 10)
        Unknown176(1)
        endIf()

@Subroutine
def cmnBDashMutekiInit():
    Unknown2186(15)

@Subroutine
def cmnBDashSpeed():
    if (SLOT_314 != 10):
        physicsImpulseX(-90000)
    else:
        physicsImpulseX(-180000)
    Unknown2229(85)

@Subroutine
def cmn_InitGuardCancelAttack():
    callSubroutine('cmnAtkLevel_2_AtkInit')
    damage2(4)
    Unknown1092(50)
    Unknown1117(0)
    or_standhit(12)
    or_launchhit(12)
    airHitPushbackX(30000)
    airHitPushbackY(40000)
    Unknown1059(2)
    Unknown1118('ARC_BTL_CMN_Hit_Large-A')
    Unknown1119('ARC_BTL_CMN_Guard_Large')
    Unknown296(120)
    Unknown292(10000)
    Unknown271('06000000640000000f0000000f000000')
    Unknown1827(1)
    Unknown294(1)
    Unknown2231(1)

    def upon_3():
        if (SLOT_105 == 0):
            Unknown2315(3)
            Unknown2003(-1)
        if (SLOT_105 == 3):
            Unknown2315(12)
            Unknown176(1)
            Unknown2055(0)
            Unknown2003(-16777216)
            Unknown448('cmn_mikiwame', 103)
            Unknown196('200000007b00000080e5f9ff0000000003000000')
            Unknown2323(-1)
            Unknown1974(1)
            Unknown251(0)
        if (SLOT_105 == 6):
            Unknown176(1)
            Unknown240()
        if (SLOT_105 == 11):
            Unknown448('cmn_mikiwame', 103)
        if (SLOT_105 == 13):
            Unknown2315(2)
            Unknown2055(1)
            Unknown251(1)
            Unknown294(0)
        if (SLOT_105 == 28):
            Unknown2231(0)

@State
def cmn_aura():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown458(2)
        Unknown454(2)
        Unknown455(3)
        Unknown671(0)
        Unknown35('17000000456e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 15)
    label('Loop')
    sprite('null', 15)
    if conditionalunk2499(3, 2, 81):
        Unknown2077('ShakeTateYoko', 100, 0, 14, 1)
    Unknown3()
    labelEnd('Loop')
    label('End')
    sprite('null', 30)
    Unknown23(23)
    Unknown671(1)

@Subroutine
def cmnKiaitame_Init():
    Unknown1058(1)
    Unknown1369(0)
    Unknown1644('CmnActHomingDash')
    Unknown1662('CmnActHomingDash', 15)

    def upon_3():
        if (SLOT_105 == 3):
            Unknown1182(1)
        if (SLOT_105 == 14):
            ActivateEffScript('cmn_aura', 100)
            Unknown43(11, 1)
            Unknown30('676b6200000000000000000000000000')
            storeValue(2, 46, 0, 1)
        Unknown30('76676200000000000000000000000000')
        storeValue(2, 46, 0, 1)
        endIf()
        Unknown30('67627200000000000000000000000000')
        storeValue(2, 46, 0, 1)
        endIf()
        Unknown30('76746200000000000000000000000000')
        storeValue(2, 46, 0, 1)
        endIf()
        Unknown30('7a6d6200000000000000000000000000')
        storeValue(2, 46, 0, 1)
        endIf()
        Unknown30('76746200000000000000000000000000')
        storeValue(2, 46, 0, 1)
        endIf()
        Unknown30('6e687900000000000000000000000000')
        storeValue(2, 46, 0, 1)
        endIf()
        Unknown30('6d677300000000000000000000000000')
        storeValue(2, 46, 0, 1)
        endIf()
        if SLOT_46:
            Unknown631('000000004152435f42544c5f434d4e5f436861726765476f645f4c6f6f705f4c5000000064000000')
        else:
            Unknown631('000000004152435f42544c5f434d4e5f4368617267655f4c6f6f705f4c5000000000000064000000')
        endIf()
        if SLOT_278:
            Unknown913(100, 10, 0)
        if (SLOT_105 >= 14):
            if conditionalunk2500(10, 32, 2, 77, 0, 0):
                Unknown2190(12)
                if (SLOT_47 >= 20):
                    storeValue(2, 47, 0, 0)
                    if (not SLOT_214):
                        Unknown54('0000000002000000300000000000000001000000')
                Unknown54('00000000020000002f0000000000000001000000')
                if (SLOT_48 >= 1):
                    Unknown2190(10)
                if (SLOT_48 >= 2):
                    Unknown2190(10)
                if (SLOT_48 >= 3):
                    Unknown2190(10)
                if (SLOT_48 >= 4):
                    Unknown2190(10)
                if (SLOT_48 >= 5):
                    Unknown2190(10)
                if (SLOT_48 >= 6):
                    Unknown2190(10)
                if (SLOT_48 >= 7):
                    Unknown2190(10)
                if (SLOT_48 >= 8):
                    Unknown2190(10)
                if (SLOT_48 >= 9):
                    Unknown2190(10)
                if (SLOT_48 >= 10):
                    Unknown2190(10)
                if (SLOT_48 >= 11):
                    Unknown2190(80)
        if (SLOT_105 == 29):
            enableWhiffCancel(1)
        if (SLOT_105 >= 48):
            if (not 
            Unknown48(1)):
                if (not 
                Unknown48(28)):
                    Unknown1798(11, 23)
                    Unknown23(3)
                    enableWhiffCancel(0)
                    Unknown14('end')
        if (SLOT_105 >= 293):
            if (SLOT_109 >= 70000):
                Unknown1798(11, 23)
                Unknown23(3)
                enableWhiffCancel(0)
                Unknown14('end')

    def upon_1():
        Unknown1798(11, 23)

@Subroutine
def cmnActMikiwame_AtkInit():
    if SLOT_31:
        Unknown1668(18, 1)
    else:
        Unknown1668(18, 3)
    Unknown2485('14000000000000000a00000000000000')
    callSubroutine('cmnAtkLevel_3_AtkInit')
    damage1(850)
    Unknown1086(20)
    Unknown1203(0)
    Unknown1095(2500)
    mod_hitstop(17)
    or_standhit(8)
    or_launchhit(8)
    airHitPushbackX(80000)
    airHitPushbackY(17000)
    grHitPushbackX(50)
    blockstun_override(16)
    untech_Override(25)
    Unknown1190(1)
    Unknown1027(500000, 0, 500000, -500000)
    Unknown1197(1)
    Unknown1117(0)
    Unknown1204(1)
    Unknown296(120)
    Unknown1051(0)
    Unknown2232()
    Unknown1645(0)
    Unknown1353(0, 0)
    Unknown2486(1)
    if SLOT_278:
        storeValue(2, 46, 0, 1)
    else:
        if Unknown2033(32, 'CmnActFuttobiFinish'):
            Unknown23(12)
            if (SLOT_15 >= 250000):
                Unknown2036(32, 100)
                Unknown94(-300000)
                Unknown99(100000)
        if Unknown2033(32, 'CmnActFuttobiBGTrans'):
            Unknown23(12)
            if (SLOT_15 >= 250000):
                Unknown2036(32, 100)
                Unknown94(-300000)
                Unknown99(100000)
    Unknown36(13, 21)

    def upon_13():
        if Unknown48(10):
            if Unknown48(19):
                if (not SLOT_287):
                    storeValue(2, 45, 0, 1)
                    if SLOT_214:
                        storeValue(2, 287, 0, 1)

    def upon_3():
        if (SLOT_105 == 3):
            Unknown23(3)
            Unknown1828(25)

    def upon_12():
        Unknown69(0)
        endIf()

    def upon_89():
        Unknown23(89)
        if SLOT_16:
            if SLOT_214:
                if SLOT_316:
                    if SLOT_263:
                        if (not SLOT_285):
                            storeValue(2, 285, 0, 1)
                            storeValue(2, 283, 0, 1)
                            mod_hitstop(0)
                            or_standhit(11)
                            or_launchhit(11)
                            airHitPushbackX(100000)
                            untech_Override(60)
                            Unknown842(1)
                            Unknown790(25)
                            Unknown294(0)
                            Unknown1653(1)
                            Unknown1356(1)

                            def upon_95():
                                Unknown23(95)
                                Unknown69(0)
                                Unknown271('00000000640000001400000014000000')
                        Unknown2040(23, 'CameraCombo_Mikiwame', 0)
        endIf()

@Subroutine
def cmnNotMainPlayer_ObjectDelete():
    if (not SLOT_263):
        Unknown2208(23)

@Subroutine
def cmnAtkRushStartInit():
    callSubroutine('cmnAtkLevel_0_AtkInit')
    damage1(0)
    Unknown1095(0)
    mod_hitstop(0)
    Unknown1142(1)
    Unknown1128(1)
    Unknown1127(1)
    Unknown997(0)
    Unknown1160(1)
    Unknown1039(1)
    Unknown1057(1)
    Unknown1051(0)
    Unknown1079(1)
    Unknown1059(1)
    Unknown1133(1)
    Unknown1043(1)
    Unknown1158(1)
    ChangeAtkDir(3)
    Unknown1100(1)
    Unknown1077(1)
    Unknown1084(1)
    Unknown1043(1)
    Unknown1019(1)
    Unknown1042('436d6e4163745275736852656a65637457616974000000000000000000000000')
    Unknown1071(1)
    Unknown997(5)
    Unknown1064('436d6e4163745275736852757368000000000000000000000000000000000000')
    Unknown1196(27)
    Unknown2486(1)

    def upon_90():
        storeValue(2, 283, 0, 1)
        storeValue(2, 288, 0, 1)
        Unknown2232()
    if (SLOT_7 <= 0):
        Unknown111(0)
    Unknown143(60)
    Unknown111(40)
    Unknown116(0)
    Unknown131(0)

    def upon_12():
        Unknown1027(220000, 0, 170000, -170000)
        if conditionalunk2499(32, 2, 318):
            if SLOT_214:
                Unknown1027(300000, 0, 200000, -170000)
    if SLOT_31:
        Unknown1040(1)

        def upon_3():
            if (SLOT_105 == 6):
                Unknown176(1)
            if (SLOT_105 == 18):
                if (not SLOT_288):
                    makeActive()
                Unknown2229(90)
            if (SLOT_105 == 27):
                beginRecovery()
                storeValue(2, 45, 0, 0)
                Unknown2229(75)
            if (not SLOT_16):
                beginRecovery()
    else:
        Unknown1190(1)
        Unknown1041(1)
        Unknown1053(1)
        Unknown2169(0)
        Unknown2170(0)
        Unknown2168(0)

        def upon_3():
            if (SLOT_105 == 6):
                Unknown176(1)
            if (SLOT_105 == 18):
                if (not SLOT_288):
                    makeActive()
                Unknown2229(90)
                Unknown2230(80)
                if (SLOT_35 <= 0):
                    storeValue(2, 45, 0, 1)
                else:
                    storeValue(2, 45, 0, 2)
            if (SLOT_105 == 27):
                beginRecovery()
                storeValue(2, 45, 0, 0)
                Unknown2229(75)
                Unknown2230(70)

            if (SLOT_105 == 31):
                Unknown2169(1)
                Unknown2170(1)
                Unknown2168(1)
                Unknown1824(3, 1)
                Unknown99(1)
                Unknown176(1)
                Unknown135()
                if (SLOT_35 >= 0):

                    storeValue(2, 45, 0, 0)
                if (SLOT_18 < 20001):
                    Unknown98(20000)
            if (SLOT_45 == 2):
                if (SLOT_35 <= 0):
                    storeValue(2, 45, 0, 0)
            if (not SLOT_16):
                beginRecovery()

@Subroutine
def cmnAtkRushRushInit():
    Unknown1673(18, 0)
    callSubroutine('cmnAtkLevel_3_AtkInit')
    callSubroutine('cmnAtkTemplNageExe')
    mod_hitstop(0)
    Unknown1050(1)
    Unknown1139(1)
    Unknown1059(1)
    Unknown1045('010000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1117(250)
    Unknown305()
    damage1(120)
    Unknown1118('dammyName')
    if SLOT_30:
        Unknown99(70000)
    storeValue(2, 46, 0, 1)
    storeValue(2, 47, 0, 0)
    storeValue(2, 48, 0, 1)
    Unknown41(32)
    Unknown240()
    Unknown40()
    storeValue(2, 45, 0, 0)
    Unknown54('00000000020000002f000000020000002e000000')
    Unknown54('000000000200000030000000020000002f000000')

@Subroutine
def cmnAtkRushMoveAndCameraInit():
    if SLOT_31:
        physicsImpulseX(5000)
        Unknown2076('d083fcff6e9104009e9c0100f9feffff791f00000000000036000000780000000f2700000f00000001000000')
    else:
        physicsImpulseX(4000)
        physicsImpulseY(2000)
        Unknown127(0)
        Unknown2076('e898fcff100905001c960200e6f8ffffc61b00000000000036000000780000000f2700000f00000001000000')

@Subroutine
def cmnAtkRushFinishChaseInit():
    Unknown1668(18, 0)
    callSubroutine('cmnAtkLevel_3_AtkInit')
    callSubroutine('cmnAtkTemplNageExe')
    damage1(800)
    Unknown1095(4500)
    Unknown1117(2500)
    or_launchhit(30)
    or_standhit(30)
    mod_hitstop(15)
    untech_Override(200)
    Unknown1059(1)
    Unknown1133(1)
    Unknown1064('436d6e41637446696e6973684368617365456e64000000000000000000000000')
    Unknown1118('ARC_BTL_CMN_Hit_XLarge')
    Unknown1018(1)
    Unknown1353(0, 0)
    Unknown176(1)
    Unknown2076('d083fcff6e9104009e9c0100f9feffff791f00000000000046000000500000000f2700000000000001000000')

@Subroutine
def cmnActRushFinishChaseEndInit():
    Unknown1353(0, 0)
    callSubroutine('cmnAtkLevel_2_AtkInit')
    or_standhit(8)
    or_launchhit(8)
    mod_hitstop(15)
    damage1(300)
    Unknown1059(1)
    Unknown1118('ARC_BTL_CMN_Hit_Large-A')
    storeValue(2, 283, 0, 1)
    storeValue(2, 286, 0, 1)

    def upon_3():
        Unknown2190(45)

    def upon_10():
        Unknown1353(1, 1)
        Unknown1347(1)
        Unknown1348(1)
        Unknown111(50)
        Unknown116(50)
        Unknown113(25000)
        Unknown135()

@Subroutine
def cmnActRushFinishChangeInit():
    Unknown1353(0, 0)
    callSubroutine('cmnAtkLevel_4_AtkInit')
    callSubroutine('cmnAtkTemplNageExe')
    Unknown1095(4500)
    Unknown1117(400)
    or_standhit(12)
    or_launchhit(12)
    airHitPushbackX(72000)
    airHitPushbackY(25000)
    untech_Override(60)
    Unknown1059(1)
    Unknown1018(1)
    Unknown1200(1)
    if SLOT_320:
        if SLOT_30:
            Unknown548()
            physicsImpulseX(8000)
            physicsImpulseY(20000)
            Unknown135()

            def upon_92():
                Unknown111(250)
    else:
        Unknown53(23, 2, 45, 22, 2, 279)
        if (SLOT_45 > 1):
            airHitPushbackX(100000)
            airHitPushbackY(15000)
            Unknown778(0)
            mod_hitstop(15)
            Unknown1064('436d6e4e65757472616c00000000000000000000000000000000000000000000')

            def upon_90():
                Unknown449('cmn_ForcedChange', 103)

            def upon_3():
                if (SLOT_105 == 1):
                    Unknown176(1)
                    Unknown2076('b85bfdff3672050037f6010090feffffd2180000000000003600000009000000190000000a00000001000000')
                if (SLOT_105 == 19):
                    Unknown23(3)
                    if SLOT_30:
                        physicsImpulseX(15000)
                        Unknown127(4500)
        elif SLOT_30:
            Unknown548()
            physicsImpulseX(8000)
            physicsImpulseY(20000)
            Unknown135()

            def upon_92():
                Unknown111(250)
    Unknown1653(0)

    def upon_89():
        Unknown1915()
        Unknown1045('04000000636d6e5f46696e6973684368616e676500000000000000000000000000000000')
        storeValue(2, 283, 0, 1)
        storeValue(2, 284, 0, 1)
        storeValue(2, 285, 0, 1)

@Subroutine
def cmnActRushFinishDamageInit():
    callSubroutine('cmnAtkLevel_4_AtkInit')
    callSubroutine('cmnAtkTemplNageExe')
    damage1(500)
    Unknown1095(4500)
    Unknown1117(400)
    untech_Override(60)
    Unknown1018(1)
    if SLOT_31:
        or_standhit(8)
        airHitPushbackX(100000)
        airHitPushbackY(20000)
        Unknown1197(1)
    else:
        storeValue(2, 45, 0, 1)
        or_launchhit(11)
        Unknown842(0)
        airHitPushbackX(45000)
        airHitPushbackY(-40000)
        Unknown548()
        physicsImpulseX(8000)
        physicsImpulseY(20000)
        Unknown135()

        def upon_90():
            Unknown941(30)
            Unknown810(30000)
            physicsImpulseY(-30000)
            Unknown778(3000)
            Unknown127(3000)
    if SLOT_278:
        Unknown1652(1)
        cancel_onhitorblock_('CmnFAirDash')
        cancel_onhitorblock_('CmnActFAirDash2Button')
    Unknown1353(0, 0)

    def upon_92():
        Unknown1653(1)
        Unknown1353(1, 1)
        Unknown1354(1)
        Unknown1369(1)
        if SLOT_45:
            Unknown111(250)
        storeValue(2, 283, 0, 1)
        storeValue(2, 284, 0, 1)
        storeValue(2, 285, 0, 1)

@Subroutine
def cmnShakeRushFinish():
    Unknown2077('ShakeTate', 1500, 0, 20, 3)

@Subroutine
def cmnAtkRushSousaiInit():
    callSubroutine('cmnAtkLevel_3_AtkInit')
    callSubroutine('cmnAtkTemplNageExe')
    damage1(0)
    Unknown710(1)
    mod_hitstop(0)
    Unknown1050(1)
    Unknown1059(1)
    Unknown1045('010000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown305()
    Unknown1820()
    Unknown1822()
    Unknown2232()
    Unknown2188(1)
    if SLOT_30:
        Unknown99(70000)
    storeValue(2, 45, 0, 0)
    storeValue(2, 48, 0, 2)
    storeValue(2, 49, 0, 1)

@Subroutine
def cmnHomingDash_StartInit():

    def upon_3():
        if (SLOT_105 == 0):
            if SLOT_30:
                Unknown2229(95)
                physicsImpulseX(-10000)
                physicsImpulseY(7000)
                Unknown127(-500)
        if (SLOT_105 == 4):
            if SLOT_31:
                Unknown2229(95)
                physicsImpulseX(-10000)
                physicsImpulseY(7000)
                Unknown127(-500)
        if (SLOT_105 == 20):
            storeValue(2, 52, 0, 1)
            makeActive()
        if (SLOT_105 >= 21):
            if (SLOT_23 <= 250000):
                Unknown54('0000000002000000300000000000000001000000')
                if (SLOT_48 == 1):
                    Unknown1827(0)

@Subroutine
def cmnHomingDash_Init():

    def upon_36():
        if SLOT_52:
            if Unknown2033(32, 'CmnActHomingDash'):
                Unknown1027(0, 0, 0, 0)
            else:
                Unknown1027(250000, -250000, 250000, -250000)
                if SLOT_47:
                    Unknown1027(300000, -250000, 250000, -250000)
                if Unknown2033(32, 'MTN_AirHoming'):
                    Unknown1027(0, 0, 0, 0)
                if Unknown2033(32, 'MTN_Change'):
                    Unknown1027(0, 0, 0, 0)
                if Unknown2033(32, 'MTN_GCChange'):
                    Unknown1027(0, 0, 0, 0)
            if (SLOT_104 <= (-300000)):
                if (SLOT_8 >= 0):
                    Unknown23(36)
                    Unknown2232()
                    Unknown14('end')
            if Unknown2033(32, 'CmnActMikiwameMove'):
                if (SLOT_104 <= 0):
                    Unknown23(36)
                    Unknown2232()
                    Unknown14('end')
        endUpon()

        def upon_7():
            Unknown111(30)
            Unknown116(60)
            Unknown2203(1)
            Unknown2172(1)

@Subroutine
def cmnHomingDash_SpeedUp():
    if (SLOT_283 == 1):
        if Unknown2030('NmlAtk5A3rd'):
            Unknown1751(15, 20000, 100000, 300, 1500, 80, 80, 0)
        if Unknown2030('NmlAtk5A3rdExe'):
            Unknown1751(15, 20000, 100000, 300, 1500, 80, 80, 0)
        if Unknown2030('NmlAtk5C'):
            Unknown1751(15, 20000, 100000, 300, 1500, 80, 80, 0)
        if Unknown2030('NmlAtk5CExe'):
            Unknown1751(15, 20000, 100000, 300, 1500, 80, 80, 0)
        if Unknown2030('NmlAtk2C'):
            Unknown1751(15, 20000, 100000, 300, 1500, 80, 80, 0)
        if Unknown2030('NmlAtkAir5C'):
            Unknown1751(15, 20000, 100000, 300, 1500, 80, 80, 0)
        if Unknown2030('NmlAtkAir2C'):
            Unknown1751(15, 20000, 100000, 300, 1500, 80, 80, 0)

@Subroutine
def cmn_InitHomingDash():
    Unknown1751(18, 20000, 95000, 300, 1500, 80, 80, 0)
    callSubroutine('cmnAtkLevel_2_AtkInit')
    damage1(300)
    Unknown1092(90)
    Unknown1117(800)
    mod_hitstop(0)
    or_standhit(27)
    or_launchhit(27)
    airHitPushbackX(3000)
    airHitPushbackY(30000)
    blockstun_override(5)
    Unknown1190(1)
    Unknown1182(1)
    Unknown1059(1)
    Unknown911(1)
    Unknown1118('ARC_BTL_CMN_Hit_Large-A')
    Unknown1119('ARC_BTL_CMN_Guard_Large')
    callSubroutine('cmnHomingDash_Init')
    callSubroutine('cmnHomingDash_SpeedUp')
    callSubroutine('CharaHomingDash_SpeedUp')
    Unknown1653(0)
    Unknown1358(1)
    Unknown36(13, 5)

    def upon_13():
        Unknown1824(10, 1)

    def upon_8():
        if SLOT_275:
            Unknown23(8)
            Unknown1751(18, 20000, 95000, 300, 1500, 80, 80, 1)
            mod_hitstop(15)
            or_standhit(1)
            or_launchhit(1)
            airHitPushbackX(15000)
            airHitPushbackY(28000)
            Unknown240()
            Unknown135()
            Unknown2232()
        if (SLOT_18 <= 100):
            Unknown99(1)

    def upon_10():
        if SLOT_275:
            Unknown23(10)
            Unknown1751(18, 20000, 95000, 300, 1500, 80, 80, 0)
            Unknown1347(1)
            Unknown1348(1)
            Unknown1653(1)
            Unknown240()
            Unknown111(10)
            Unknown107(13000)
            Unknown116(20)
            Unknown113(28000)
            Unknown135()

    def upon_93():
        Unknown23(93)
        Unknown240()
        physicsImpulseX(5000)
        Unknown116(10)
        Unknown113(23000)
        Unknown135()

    def upon_96():
        Unknown23(96)
        Unknown240()
        Unknown94(-10000)
        physicsImpulseX(-10000)
        Unknown116(0)
        Unknown113(30000)
        Unknown135()

        def upon_47():
            storeValue(2, 51, 0, 1)

    def upon_86():
        Unknown23(86)
        Unknown240()
        if SLOT_278:
            Unknown1751(18, 20000, 95000, 300, 1500, 80, 80, 0)
            Unknown1347(1)
            Unknown1348(1)
            Unknown1653(1)
            Unknown111(10)
            Unknown116(25)
            Unknown107(5000)
            Unknown113(15000)
            Unknown135()
        else:
            physicsImpulseX(-8000)
            Unknown116(10)
            Unknown113(28000)
            Unknown127(4000)

    def upon_98():
        Unknown23(98)
        Unknown1751(18, 20000, 95000, 300, 1500, 80, 80, 1)
        mod_hitstop(15)
        if SLOT_49:
            mod_hitstop(6)
        Unknown240()
        if SLOT_278:
            Unknown1751(18, 20000, 95000, 300, 1500, 80, 80, 0)
            Unknown1347(1)
            Unknown1348(1)
            Unknown1653(1)
            Unknown111(10)
            Unknown116(25)
            Unknown107(5000)
            Unknown113(15000)
            Unknown135()
        else:
            physicsImpulseX(-8000)
            Unknown116(10)
            Unknown113(28000)
            Unknown127(4000)

    def upon_97():
        Unknown23(97)
        Unknown32('cmn_HomingDash_JizokuTrail')
        storeValue(2, 49, 0, 1)
        mod_hitstop(15)

@Subroutine
def cmn_InitHomingDashChange():
    Unknown1751(6, 20000, 90000, 300, 1500, 80, 80, 0)
    callSubroutine('cmnAtkLevel_2_AtkInit')
    damage1(300)
    Unknown1092(90)
    Unknown1117(800)
    mod_hitstop(0)
    or_standhit(27)
    or_launchhit(27)
    airHitPushbackX(3000)
    airHitPushbackY(30000)
    blockstun_override(5)
    Unknown1190(1)
    Unknown1182(1)
    Unknown1059(1)
    Unknown911(1)
    Unknown1118('ARC_BTL_CMN_Hit_Large-A')
    Unknown1119('ARC_BTL_CMN_Guard_Large')
    callSubroutine('cmnHomingDash_Init')
    callSubroutine('cmnHomingDash_SpeedUp')
    Unknown1653(0)
    Unknown2491()
    Unknown36(13, 5)

    def upon_13():
        Unknown1824(10, 1)

    def upon_8():
        if SLOT_275:
            Unknown23(8)
            Unknown1751(6, 20000, 90000, 300, 1500, 80, 80, 1)
            mod_hitstop(15)
            or_standhit(1)
            or_launchhit(1)
            airHitPushbackX(15000)
            airHitPushbackY(28000)
            Unknown240()
            Unknown135()
            Unknown2232()
        if (SLOT_18 <= 100):
            Unknown99(1)

    def upon_10():
        if SLOT_275:
            Unknown23(10)
            Unknown1751(6, 20000, 90000, 300, 1500, 80, 80, 0)
            Unknown1347(1)
            Unknown1348(1)
            Unknown1653(1)
            Unknown240()
            Unknown111(10)
            Unknown107(13000)
            Unknown116(20)
            Unknown113(28000)
            Unknown135()

    def upon_93():
        Unknown23(93)
        Unknown240()
        physicsImpulseX(5000)
        Unknown116(10)
        Unknown113(23000)
        Unknown135()

    def upon_96():
        Unknown23(96)
        Unknown240()
        Unknown94(-10000)
        physicsImpulseX(-10000)
        Unknown116(0)
        Unknown113(30000)
        Unknown135()

        def upon_47():
            storeValue(2, 51, 0, 1)

    def upon_86():
        Unknown23(86)
        Unknown240()
        physicsImpulseX(-8000)
        Unknown116(10)
        Unknown113(28000)
        Unknown127(4000)

    def upon_98():
        Unknown23(98)
        Unknown1751(6, 20000, 90000, 300, 1500, 80, 80, 1)
        mod_hitstop(15)
        if SLOT_49:
            mod_hitstop(6)
        Unknown240()
        physicsImpulseX(-8000)
        Unknown116(10)
        Unknown113(28000)
        Unknown127(4000)

    def upon_97():
        Unknown23(97)
        Unknown32('cmn_HomingDash_JizokuTrail')
        storeValue(2, 49, 0, 1)
        mod_hitstop(15)

@Subroutine
def cmn_InitHomingDashGuardCancel():
    Unknown1751(6, 20000, 90000, 300, 1500, 80, 80, 0)
    callSubroutine('cmnAtkLevel_2_AtkInit')
    damage1(300)
    Unknown1092(50)
    Unknown1117(0)
    mod_hitstop(0)
    or_standhit(27)
    or_launchhit(27)
    airHitPushbackX(3000)
    airHitPushbackY(30000)
    blockstun_override(5)
    Unknown1190(1)
    Unknown1182(1)
    Unknown1059(2)
    Unknown911(1)
    untech_Override(28)
    storeValue(2, 47, 0, 1)
    Unknown1079(1)
    damage2(4)
    Unknown734(1)
    Unknown1118('ARC_BTL_CMN_Hit_Large-A')
    Unknown1119('ARC_BTL_CMN_Guard_Large')
    callSubroutine('cmnHomingDash_Init')
    Unknown296(120)
    Unknown1827(1)
    Unknown1653(0)
    Unknown271('06000000640000000f0000000f000000')
    Unknown1820()
    Unknown1822()
    Unknown2491()
    Unknown2137(5, 12, 1)
    Unknown2231(1)
    Unknown36(13, 5)

    def upon_13():
        Unknown1824(10, 1)

    def upon_8():
        if SLOT_275:
            Unknown23(8)
            Unknown1751(1, 20000, 90000, 300, 1500, 80, 80, 1)
            mod_hitstop(15)
            or_standhit(1)
            or_launchhit(1)
            airHitPushbackX(40000)
            airHitPushbackY(30000)
            Unknown240()
            Unknown135()
            Unknown2232()

    def upon_10():
        if SLOT_275:
            Unknown23(10)
            Unknown1751(1, 20000, 90000, 300, 1500, 80, 80, 1)
            Unknown240()
            physicsImpulseX(-10000)
            Unknown116(10)
            Unknown113(23000)
            Unknown127(4000)
            callSubroutine('cmnUltimate_CameraCombo')
        if (SLOT_18 <= 100):
            Unknown99(1)

        def upon_47():
            storeValue(2, 52, 0, 1)

    def upon_93():
        Unknown23(93)
        Unknown240()
        physicsImpulseX(5000)
        Unknown116(10)
        Unknown113(23000)
        Unknown127(4000)
        Unknown1827(0)

    def upon_96():
        Unknown23(96)
        Unknown240()
        Unknown94(-10000)
        physicsImpulseX(-10000)
        Unknown116(0)
        Unknown113(30000)
        Unknown135()
        Unknown1827(0)

        def upon_47():
            storeValue(2, 51, 0, 1)

    def upon_86():
        Unknown23(86)
        Unknown240()
        physicsImpulseX(-2000)
        physicsImpulseY(42000)
        Unknown127(4000)
        Unknown1824(10, 1)
        Unknown1827(0)

        def upon_47():
            storeValue(2, 52, 0, 1)

    def upon_98():
        Unknown23(98)
        Unknown1751(1, 20000, 90000, 300, 1500, 80, 80, 1)
        mod_hitstop(15)
        if SLOT_49:
            mod_hitstop(6)
        Unknown240()
        physicsImpulseX(-2000)
        physicsImpulseY(42000)
        Unknown127(4000)
        Unknown1824(10, 1)
        Unknown1827(0)

        def upon_47():
            storeValue(2, 52, 0, 1)

    def upon_97():
        Unknown23(97)
        Unknown32('cmn_HomingDash_JizokuTrail')
        storeValue(2, 49, 0, 1)
        mod_hitstop(15)

@Subroutine
def cmn_InitSparkingBurst():
    Unknown1369(0)
    Unknown176(1)
    Unknown1827(1)
    Unknown294(1)
    Unknown2486(1)

    def upon_50():
        Unknown2079('1700000019ceffffa6030a009ca30100c7010000000000000000000036000000090000000a00000006000000000000000200000000000000')

    def upon_3():
        if (SLOT_105 == 3):
            Unknown127(-2600)
            if (not SLOT_92):
                Unknown271('00000000640000001600000016000000')
        if (SLOT_105 == 6):
            Unknown271('00000000640000001300000013000000')
        if (SLOT_105 == 13):
            Unknown176(1)
            ActivateEffScript('cmnSparkingBurst', 103)
            if SLOT_90:
                Unknown59('5452505f535041524b494e475f4c560000000000000000000000000000000000020000009d000000')
                if (SLOT_157 == 0):
                    if (SLOT_279 == 3):
                        Unknown551(420)
                    if (SLOT_279 == 2):
                        Unknown551(840)
                    if (SLOT_279 == 1):
                        Unknown551(1260)
                if (SLOT_157 == 1):
                    Unknown551(420)
                if (SLOT_157 == 2):
                    Unknown551(840)
                if (SLOT_157 == 3):
                    Unknown551(1260)
                if (SLOT_157 == 4):
                    Unknown551(420)
            else:
                if (SLOT_279 == 3):
                    Unknown551(420)
                if (SLOT_279 == 2):
                    Unknown551(840)
                if (SLOT_279 == 1):
                    Unknown551(1260)
        if (SLOT_105 == 31):
            Unknown135()
            Unknown1698(5)
            Unknown1700(0)
        if (SLOT_105 == 34):
            if (not SLOT_45):
                Unknown1827(0)

@Subroutine
def cmn_SparkingBurst_PowerUp():
    if SLOT_278:
        Unknown912(120, 11, 0)
        Unknown913(200, 11, 0)
        Unknown1298(0)
        Unknown1278(10)
        Unknown1280(10)
        Unknown1276(5)
        Unknown1279(2)
        Unknown1308(10)
        Unknown1310(10)
        Unknown1307(12)
        Unknown1309(2)
        if SLOT_319:
            Unknown912(130, 11, 0)
    else:
        Unknown912(100, 10, 0)
        Unknown913(100, 10, 0)
        Unknown1298(60)
        Unknown1278(10)
        Unknown1280(10)
        Unknown1276(5)
        Unknown1279(2)
        Unknown1308(10)
        Unknown1310(10)
        Unknown1307(12)
        Unknown1309(2)
        if SLOT_319:
            Unknown912(120, 11, 0)

@State
def cmnSparkingBurst():

    def upon_IMMEDIATE():
        Unknown244()
        callSubroutine('cmnAtkLevel_2_AtkInit')
        damage1(0)
        Unknown1079(1)
        mod_hitstop(3)
        Unknown1021(1)
        Unknown778(2500)
        grHitPushbackX(200)
        Unknown1128(1)
        Unknown717('ShakeTateYoko', 2500, 5, 20, 5)
        Unknown1045('010000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1117(0)
        Unknown1118('ARC_BTL_CMN_Hit_Large-A')
        Unknown1119('ARC_BTL_CMN_Guard_Beam')

        def upon_9():
            Unknown23(9)
            if Unknown2033(3, 'CmnActSparkingBurst'):
                Unknown53(3, 2, 45, 23, 0, 1)
        if SLOT_214:
            or_standhit(27)
            or_launchhit(27)
            airHitPushbackX(5000)
            airHitPushbackY(60000)
            Unknown778(3500)
            Unknown806(80000)
            Unknown854(1)
            Unknown802(25)
            untech_Override(60)

            def upon_90():
                Unknown23(90)
                Unknown457(0)
                storeValue(2, 45, 0, 1)
        else:
            Unknown1092(50)
            or_standhit(8)
            or_launchhit(8)
            airHitPushbackX(50000)
            airHitPushbackY(35000)
        Unknown99(100000)
        Unknown450('cmn_burst_blue')
        Unknown454(2)
        Unknown456(2)
        Unknown457(2)
    sprite('null', 1)
    Unknown188(1000)
    sprite('null', 1)
    Unknown188(1200)
    sprite('null', 1)
    Unknown188(1400)
    sprite('null', 1)
    Unknown188(1600)
    sprite('burst_00', 2)
    makeActive()
    sprite('null', 200)

@Subroutine
def cmnActHajikiInit():
    Unknown1182(1)
    Unknown1827(1)
    Unknown1840(1)
    Unknown1839(0)
    Unknown1846(0)
    Unknown1369(0)
    Unknown1851(5, -2)
    Unknown1058(1)
    if Unknown2030('CmnActShotHajiki'):
        Unknown2185(1)
        Unknown36(13, 23)

        def upon_13():
            Unknown2185(0)
            Unknown1846(0)
    else:
        Unknown2185(0)
        Unknown1846(0)

    def upon_3():
        if (SLOT_105 >= 16):
            Unknown1637('CmnActShotHajiki')
        if SLOT_48:
            Unknown2249(0)
            Unknown54('0000000002000000300000000000000001000000')
            if (SLOT_48 == 17):
                Unknown1662('NmlAtk5A', 7)
                Unknown1662('NmlAtk5B', 7)
                Unknown1662('NmlAtk6B', 7)
                Unknown1662('NmlAtk5C', 7)
                Unknown1662('NmlAtk2A', 7)
                Unknown1662('NmlAtk2B', 7)
                Unknown1662('NmlAtk2C', 7)
                Unknown1662('CmnActMikiwameMove', 7)
                Unknown1662('CmnActHomingDash', 7)
                Unknown1662('CmnActRushStart', 7)
                Unknown1671(7)
                Unknown1827(0)
                Unknown2292(0)

    def upon_87():
        Unknown23(87)
        Unknown23(13)
        storeValue(2, 48, 0, 1)
        Unknown2190(150)
        enableWhiffCancel(1)
        Unknown2185(1)
        Unknown1846(1)

    def upon_64():
        Unknown23(64)
        Unknown23(43)
        Unknown23(13)
        storeValue(2, 48, 0, 1)
        Unknown2190(150)
        enableWhiffCancel(1)
        Unknown2292(1)
        Unknown2185(1)
        Unknown1846(1)

    def upon_43():
        Unknown23(43)
        Unknown23(13)
        storeValue(2, 48, 0, 1)
        Unknown2190(250)
        enableWhiffCancel(1)
        Unknown2292(1)
        Unknown2185(1)
        Unknown1846(1)

@State
def cmnHajikiBack():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown32('cmnHajikiBack')
    sprite('burst_00', 5)
    Unknown612('ARC_BTL_CMN_Sousai_Niku')
    sprite('burst_00', 15)
    Unknown2036(2, 100)
    Unknown240()
    physicsImpulseX(-100000)
    Unknown2229(90)

    def upon_3():
        if (not SLOT_24):
            onFrame(0, 0)
            Unknown2424()
        Unknown2036(2, 100)
        if SLOT_32:
            Unknown54('0100000002000000530000000200000007000000')
        else:
            Unknown54('0000000002000000530000000200000007000000')
        Unknown53(2, 2, 83, 23, 2, 83)
        endIf()

@Subroutine
def cmnNmlAtk5A_AtkInit():
    callSubroutine('cmnAtkLevel_1_AtkInit')
    Unknown1092(90)
    Unknown1143(1)

@Subroutine
def cmnNmlAtk5A2nd_AtkInit():
    callSubroutine('cmnAtkLevel_2_AtkInit')
    Unknown1143(1)

@Subroutine
def cmnNmlAtk5A3rd_AtkInit():
    callSubroutine('cmnAtkLevel_4_AtkInit')
    Unknown1121(3)
    Unknown1143(1)
    or_standhit(12)
    or_launchhit(12)
    airHitPushbackX(20000)
    airHitPushbackY(45000)
    untech_Override(35)
    Unknown1051(0)

@Subroutine
def cmnNmlAtk2A_AtkInit():
    callSubroutine('cmnAtkLevel_1_AtkInit')
    Unknown1092(90)
    Unknown1143(1)

@Subroutine
def cmnNmlAtk5B_AtkInit():
    callSubroutine('cmnAtkLevel_2_AtkInit')
    Unknown1143(1)
    airHitPushbackX(14000)
    airHitPushbackY(27000)

@Subroutine
def cmnNmlAtk2B_AtkInit():
    callSubroutine('cmnAtkLevel_2_AtkInit')
    ChangeAtkDir(2)
    Unknown1143(1)
    or_launchhit(28)
    or_standhit(28)
    untech_Override(22)
    airHitPushbackX(14000)
    airHitPushbackY(11000)
    Unknown778(1100)

@Subroutine
def cmnNmlAtk6B_AtkInit():
    callSubroutine('cmnAtkLevel_3_AtkInit')
    callSubroutine('cmn_KuzushiHosei')
    ChangeAtkDir(1)
    Unknown1143(1)
    hitstun_Override(18)
    untech_Override(23)
    Unknown1118('ARC_BTL_CMN_Hit_Midle-A')
    Unknown1119('ARC_BTL_CMN_Guard_Midle')
    if (SLOT_314 == 24):
        Unknown884(1)
        Unknown896(1)
        Unknown756(8000)
        Unknown768(-20000)
        Unknown804(100)
        Unknown806(26000)
        Unknown856(1)
        Unknown820(44)
        Unknown832(58)

@Subroutine
def cmnNmlAtk5C_AtkInit():
    callSubroutine('cmnAtkLevel_4_AtkInit')
    Unknown1121(3)
    damage1(850)
    Unknown1143(1)
    or_standhit(8)
    or_launchhit(8)
    airHitPushbackX(45000)
    airHitPushbackY(15000)
    Unknown1197(1)

@Subroutine
def cmnNmlAtk2C_AtkInit():
    callSubroutine('cmnAtkLevel_4_AtkInit')
    Unknown1121(3)
    damage1(850)
    Unknown1143(1)
    or_launchhit(9)
    or_standhit(9)
    Unknown1051(0)
    airHitPushbackX(3500)
    airHitPushbackY(63000)
    Unknown1099(1)

@Subroutine
def cmnNmlAtkAir5A_AtkInit():
    callSubroutine('cmnAtkLevel_1_AtkInit')
    callSubroutine('cmn_AirAtkHosei')
    Unknown1143(1)
    airHitPushbackX(10500)
    airHitPushbackY(23000)

@Subroutine
def cmnNmlAtkAir5B_AtkInit():
    callSubroutine('cmnAtkLevel_2_AtkInit')
    callSubroutine('cmn_AirAtkHosei')
    Unknown1143(1)
    airHitPushbackX(10500)
    airHitPushbackY(24500)

@Subroutine
def cmnNmlAtkAir5C_AtkInit():
    callSubroutine('cmnAtkLevel_3_AtkInit')
    callSubroutine('cmn_AirAtkHosei')
    or_standhit(3)
    or_launchhit(11)
    Unknown1143(1)
    Unknown842(0)
    airHitPushbackX(30000)
    airHitPushbackY(-50000)
    untech_Override(60)
    Unknown778(2400)

@Subroutine
def cmnNmlAtkAir2C_AtkInit():
    callSubroutine('cmnAtkLevel_3_AtkInit')
    callSubroutine('cmn_AirAtkHosei')
    or_launchhit(9)
    or_standhit(9)
    Unknown1051(0)
    Unknown1143(1)
    airHitPushbackX(3500)
    airHitPushbackY(63000)
    ChangeAtkDir(0)

@Subroutine
def cmnNmlAtk5A_Init():
    Unknown1655(1)
    cancel_whiff_('NmlAtk5A2nd')
    Unknown1640('NmlAtk5A2nd')
    Unknown1637('NmlAtk5A2nd')
    Unknown1637('NmlAtk5A')
    cancel_onhitorblock_('NmlAtk5A')
    cancel_onhitorblock_('NmlAtk2A')
    cancel_onhitorblock_('NmlAtk5B')
    cancel_onhitorblock_('NmlAtk2B')
    cancel_onhitorblock_('NmlAtk6B')
    cancel_onhitorblock_('NmlAtk5C')
    cancel_onhitorblock_('NmlAtk2C')
    cancel_onhitorblock_('NmlAtk5D')
    cancel_onhitorblock_('CmnActRushStart')
    if SLOT_278:
        Unknown1652(1)

@Subroutine
def cmnNmlAtk5A2nd_Init():
    Unknown1655(1)
    cancel_whiff_('NmlAtk5A3rd')
    Unknown1640('NmlAtk5A3rd')
    Unknown1637('NmlAtk5A3rd')
    cancel_onhitorblock_('NmlAtk5B')
    cancel_onhitorblock_('NmlAtk2B')
    cancel_onhitorblock_('NmlAtk6B')
    cancel_onhitorblock_('NmlAtk5C')
    cancel_onhitorblock_('NmlAtk2C')
    cancel_onhitorblock_('NmlAtk5D')
    if SLOT_278:
        Unknown1652(1)
        cancel_onhitorblock_('CmnFAirDash')
        cancel_onhitorblock_('CmnActFAirDash2Button')

@Subroutine
def cmnNmlAtk5A3rd_Init():
    cancel_autocombo_('CmnActHomingDash')

    def upon_89():
        Unknown23(89)
        if SLOT_16:
            if SLOT_263:
                if (not SLOT_283):
                    storeValue(2, 283, 0, 1)
                    storeValue(2, 286, 0, 1)
                Unknown2310(15)
                mod_hitstop(0)

                def upon_95():
                    Unknown23(95)
                    Unknown69(0)
                    Unknown271('00000000640000001900000019000000')
                    Unknown2077('ShakeTateYoko', 1000, 0, 18, 1)
            if SLOT_32:
                if (SLOT_83 <= (-2900000)):
                    storeValue(2, 83, 0, -2900000)
            elif (SLOT_83 >= 2900000):
                storeValue(2, 83, 0, 2900000)
            Unknown2040(23, 'CameraCombo_5A3rd', 0)
        endIf()
    if SLOT_278:
        Unknown1652(1)
        cancel_onhitorblock_('CmnFAirDash')
        cancel_onhitorblock_('CmnActFAirDash2Button')

@Subroutine
def cmnNmlAtk2A_Init():
    Unknown1637('NmlAtk2A')
    cancel_onhitorblock_('NmlAtk5A')
    cancel_onhitorblock_('NmlAtk2A')
    cancel_onhitorblock_('NmlAtk5B')
    cancel_onhitorblock_('NmlAtk2B')
    cancel_onhitorblock_('NmlAtk6B')
    cancel_onhitorblock_('NmlAtk5C')
    cancel_onhitorblock_('NmlAtk2C')
    cancel_onhitorblock_('NmlAtk5D')
    if SLOT_278:
        Unknown1652(1)

@Subroutine
def cmnNmlAtk5B_Init():
    Unknown1655(1)
    Unknown1641('NmlAtk2B')
    cancel_onhitorblock_('NmlAtk2B')
    cancel_onhitorblock_('NmlAtk6B')
    cancel_onhitorblock_('NmlAtk5C')
    cancel_onhitorblock_('NmlAtk2C')
    cancel_onhitorblock_('NmlAtk5D')
    if SLOT_278:
        Unknown1652(1)

@Subroutine
def cmnNmlAtk2B_Init():
    cancel_onhitorblock_('NmlAtk5B')
    cancel_onhitorblock_('NmlAtk6B')
    cancel_onhitorblock_('NmlAtk5C')
    cancel_onhitorblock_('NmlAtk2C')
    cancel_onhitorblock_('NmlAtk5D')
    if SLOT_278:
        Unknown1652(1)

@Subroutine
def cmnNmlAtk6B_Init():
    Unknown176(1)
    Unknown1653(0)
    Unknown1369(0)
    if SLOT_278:
        Unknown1653(1)
        Unknown1652(1)
        cancel_onhitorblock_('CmnFAirDash')
        cancel_onhitorblock_('CmnActFAirDash2Button')

        def upon_8():
            Unknown1369(1)
    Unknown36(13, 5)

    def upon_13():
        physicsImpulseX(6000)
        physicsImpulseY(14000)
        Unknown127(1000)
        Unknown1824(6, 1)
        Unknown2204(1)
        Unknown1975(40000)

@Subroutine
def cmnNmlAtk5C_Init():
    cancel_onhitorblock_('NmlAtk2C')
    cancel_onhitorblock_('NmlAtk5D')
    if SLOT_283:
        storeValue(2, 283, 0, 2)

    def upon_89():
        Unknown23(89)
        if SLOT_16:
            if SLOT_263:
                if (not SLOT_283):
                    storeValue(2, 283, 0, 1)
                    Unknown2310(15)
                    Unknown1676('CmnActHomingDash')
                    damage1(1000)
                    mod_hitstop(0)
                    or_standhit(11)
                    or_launchhit(11)
                    airHitPushbackX(100000)
                    untech_Override(40)
                    Unknown790(0)
                    Unknown937(4)

                    def upon_95():
                        Unknown23(95)
                        Unknown69(0)
                        Unknown2077('ShakeTateYoko', 1000, 0, 18, 1)
                        Unknown271('00000000640000001900000019000000')
                if SLOT_32:
                    if (SLOT_83 <= (-2900000)):
                        storeValue(2, 83, 0, -2900000)
                elif (SLOT_83 >= 2900000):
                    storeValue(2, 83, 0, 2900000)
                Unknown2040(23, 'CameraCombo_5C', 0)
        endIf()
    if SLOT_278:
        Unknown1652(1)
        cancel_onhitorblock_('CmnFAirDash')
        cancel_onhitorblock_('CmnActFAirDash2Button')

@Subroutine
def cmnNmlAtk2C_Init():
    Unknown250(300000)
    Unknown249(160000)
    Unknown36(13, 4)

    def upon_13():
        Unknown1866(1)
    if SLOT_283:
        storeValue(2, 283, 0, 2)

    def upon_89():
        Unknown23(89)
        if SLOT_16:
            if SLOT_263:
                if (not SLOT_283):
                    storeValue(2, 283, 0, 1)
                    storeValue(2, 286, 0, 1)
                    Unknown2310(15)
                    Unknown1676('CmnActHomingDash')
                    damage1(1000)
                    mod_hitstop(0)
                    untech_Override(40)

                    def upon_95():
                        Unknown23(95)
                        Unknown69(0)
                        Unknown271('00000000640000001900000019000000')
                        Unknown2077('ShakeTateYoko', 1000, 0, 18, 1)
                if SLOT_32:
                    if (SLOT_83 <= (-2900000)):
                        storeValue(2, 83, 0, -2900000)
                elif (SLOT_83 >= 2900000):
                    storeValue(2, 83, 0, 2900000)
                Unknown2040(23, 'CameraCombo_2C', 0)
        endIf()
    if SLOT_278:
        Unknown1652(1)
        cancel_onhitorblock_('CmnFAirDash')
        cancel_onhitorblock_('CmnActFAirDash2Button')

@Subroutine
def cmnNmlAtk5D_Init():
    Unknown1058(1)
    Unknown1653(0)
    Unknown1651(0)
    cancel_onhitorblock_('NmlAtk5C')
    cancel_onhitorblock_('NmlAtk2C')

    def upon_3():
        if SLOT_52:
            Unknown1653(1)
            Unknown1651(1)
            Unknown1356(1)
            Unknown1354(1)
            if SLOT_278:
                Unknown1662('CmnVJump', 10)
                Unknown1662('CmnBJump', 10)
                Unknown1662('CmnFJump', 10)
                Unknown1652(1)
        else:
            Unknown1653(0)
            Unknown1651(0)
            Unknown1356(0)
            Unknown1354(0)
            Unknown1652(0)
        if (SLOT_105 == 4):
            Unknown1671(20)
            Unknown1662('NmlAtk5C', 8)
            Unknown1662('NmlAtk2C', 8)

@Subroutine
def cmnNmlAtk2D_Init():
    Unknown1058(1)
    Unknown1653(0)
    Unknown1651(0)
    cancel_onhitorblock_('NmlAtk5C')
    cancel_onhitorblock_('NmlAtk2C')
    cancel_onhitorblock_('NmlAtk5D')

    def upon_3():
        if SLOT_52:
            Unknown1653(1)
            Unknown1651(1)
            Unknown1356(1)
            Unknown1354(1)
            if SLOT_278:
                Unknown1662('CmnVAirJump', 10)
                Unknown1662('CmnBAirJump', 10)
                Unknown1662('CmnFAirJump', 10)
                Unknown1662('CmnVJump', 10)
                Unknown1662('CmnBJump', 10)
                Unknown1662('CmnFJump', 10)
                Unknown1662('CmnFAirDash', 10)
                Unknown1662('CmnActFAirDash2Button', 10)
                Unknown1652(1)
                cancel_onhitorblock_('CmnFAirDash')
                cancel_onhitorblock_('CmnActFAirDash2Button')
        else:
            Unknown1653(0)
            Unknown1651(0)
            Unknown1356(0)
            Unknown1354(0)
            Unknown1652(0)
        if (SLOT_105 == 4):
            Unknown1671(20)
            Unknown1662('NmlAtk5C', 8)
            Unknown1662('NmlAtk2C', 8)
            Unknown1662('NmlAtk5D', 8)

@Subroutine
def cmnNmlAtkAir5A_Init():
    Unknown1652(1)
    cancel_onhitorblock_('NmlAtkAir5A')
    cancel_onhitorblock_('NmlAtkAir5B')
    cancel_onhitorblock_('NmlAtkAir5C')
    cancel_onhitorblock_('NmlAtkAir2C')
    cancel_onhitorblock_('NmlAtkAir5D')
    Unknown2359(1)
    if SLOT_278:
        cancel_onhitorblock_('CmnFAirDash')
        cancel_onhitorblock_('CmnActFAirDash2Button')

    def upon_89():
        Unknown23(89)
        if (not 
        Unknown2030('NmlAtkAir5B')):
            if (not 
            Unknown2030('NmlAtkAir5A')):
                if conditionalunk2499(32, 2, 318):
                    cancel_autocombo_('NmlAtkAir5B')
    callSubroutine('cmnAir_F_NO_STOP_IDLING')

@Subroutine
def cmnNmlAtkAir5B_Init():
    Unknown1652(1)
    cancel_onhitorblock_('NmlAtkAir5A')
    cancel_onhitorblock_('NmlAtkAir5C')
    cancel_onhitorblock_('NmlAtkAir2C')
    cancel_onhitorblock_('NmlAtkAir5D')
    if SLOT_278:
        cancel_onhitorblock_('CmnFAirDash')
        cancel_onhitorblock_('CmnActFAirDash2Button')
    if SLOT_249:
        Unknown1658('NmlAtkAir5A')
        cancel_autocombo_('NmlAtkAir5C')
        Unknown240()
        Unknown135()
        if Unknown53(3, 2, 0, 32, 2, 18):
            storeValue(2, 7, 2, 14)
            if (SLOT_7 <= 150000):
                storeValue(2, 7, 0, 10000)
            else:
                storeValue(2, 7, 0, 20000)
            storeValue(2, 8, 2, 35)
            if (SLOT_8 >= 100000):
                storeValue(2, 8, 0, 45000)
            elif (SLOT_8 <= (-130000)):
                storeValue(2, 8, 0, 25000)
            else:
                storeValue(2, 8, 0, 30000)
    callSubroutine('cmnAir_F_NO_STOP_IDLING')

@Subroutine
def cmnNmlAtkAir5C_Init():
    cancel_onhitorblock_('NmlAtkAir2C')
    cancel_onhitorblock_('NmlAtkAir5D')
    if SLOT_283:
        storeValue(2, 283, 0, 2)

    def upon_89():
        Unknown23(89)
        if SLOT_16:
            if SLOT_263:
                if SLOT_286:
                    if (not SLOT_257):
                        if SLOT_249:
                            storeValue(2, 284, 0, 1)
                            Unknown2310(14)

                            def upon_95():
                                Unknown23(95)
                                Unknown69(0)
                                Unknown271('00000000640000001900000019000000')
                                Unknown2077('ShakeTateYoko', 1000, 0, 18, 1)
                        mod_hitstop(0)
                        Unknown711(4)
                        airHitPushbackX(60000)
                        airHitPushbackY(-30000)
                        untech_Override(35)
                        or_standhit(8)
                        Unknown842(1)
                        Unknown790(33)
                        Unknown937(0)
                        if SLOT_32:
                            if (SLOT_83 <= (-2900000)):
                                storeValue(2, 83, 0, -2900000)
                        elif (SLOT_83 >= 2900000):
                            storeValue(2, 83, 0, 2900000)
                        Unknown2232()
                        Unknown2040(23, 'CameraCombo_Air5C', 0)
                if (not SLOT_284):
                    storeValue(2, 284, 0, 1)
                    Unknown2310(15)
                    Unknown711(4)
                    mod_hitstop(0)
                    Unknown941(35)
                    or_standhit(8)

                    def upon_95():
                        Unknown23(95)
                        Unknown69(0)
                        Unknown271('00000000640000001e0000001e000000')
                        Unknown2077('ShakeTateYoko', 1000, 0, 18, 1)
                if SLOT_32:
                    if (SLOT_83 <= (-2900000)):
                        storeValue(2, 83, 0, -2900000)
                elif (SLOT_83 >= 2900000):
                    storeValue(2, 83, 0, 2900000)
                Unknown778(3000)
                Unknown127(3000)
                Unknown113(-45000)
                if (SLOT_8 <= (-45000)):
                    physicsImpulseY(-45000)
                Unknown2232()
                Unknown2040(23, 'CameraCombo_Air5C', 0)
        endIf()
        endIf()
    if SLOT_278:
        Unknown1652(1)
        cancel_onhitorblock_('CmnFAirDash')
        cancel_onhitorblock_('CmnActFAirDash2Button')
    callSubroutine('cmnAir_F_NO_STOP_IDLING')

@Subroutine
def cmnNmlAtkAir2C_Init():
    cancel_onhitorblock_('NmlAtkAir5D')
    Unknown1652(1)
    if SLOT_278:
        cancel_onhitorblock_('CmnFAirDash')
        cancel_onhitorblock_('CmnActFAirDash2Button')
    if SLOT_283:
        storeValue(2, 283, 0, 2)

    def upon_89():
        Unknown23(89)
        if SLOT_16:
            if SLOT_263:
                if (not SLOT_283):
                    storeValue(2, 283, 0, 1)
                    storeValue(2, 286, 0, 1)
                    Unknown2310(15)
                    Unknown1676('CmnActHomingDash')
                    mod_hitstop(0)
                    airHitPushbackY(60000)
                    untech_Override(40)

                    def upon_95():
                        Unknown23(95)
                        Unknown69(0)
                        Unknown271('00000000640000001900000019000000')
                        Unknown2077('ShakeTateYoko', 1000, 0, 18, 1)
                if SLOT_32:
                    if (SLOT_83 <= (-2900000)):
                        storeValue(2, 83, 0, -2900000)
                elif (SLOT_83 >= 2900000):
                    storeValue(2, 83, 0, 2900000)
                Unknown2040(23, 'CameraCombo_Air2C', 0)
        endIf()

@Subroutine
def cmnNmlAtkAir5D_Init():
    Unknown1058(1)
    Unknown1653(0)
    Unknown1651(0)

    def upon_3():
        if SLOT_52:
            Unknown1653(1)
            Unknown1651(1)
            Unknown1356(1)
            Unknown1354(1)
            if SLOT_278:
                Unknown1662('CmnVAirJump', 10)
                Unknown1662('CmnBAirJump', 10)
                Unknown1662('CmnFAirJump', 10)
                Unknown1662('CmnFAirDash', 10)
                Unknown1662('CmnActFAirDash2Button', 10)
                Unknown1652(1)
                cancel_onhitorblock_('CmnFAirDash')
                cancel_onhitorblock_('CmnActFAirDash2Button')
        else:
            Unknown1653(0)
            Unknown1651(0)
            Unknown1356(0)
            Unknown1354(0)
            Unknown1652(0)
        if (SLOT_105 == 4):
            Unknown1671(20)

@Subroutine
def cmnNmlAtkAir2D_Init():
    Unknown1058(1)
    Unknown1653(0)
    Unknown1651(0)

    def upon_3():
        if SLOT_52:
            Unknown1653(1)
            Unknown1651(1)
            Unknown1356(1)
            Unknown1354(1)
            if SLOT_278:
                Unknown1662('CmnVAirJump', 10)
                Unknown1662('CmnBAirJump', 10)
                Unknown1662('CmnFAirJump', 10)
                Unknown1662('CmnFAirDash', 10)
                Unknown1662('CmnActFAirDash2Button', 10)
                Unknown1652(1)
                cancel_onhitorblock_('CmnFAirDash')
                cancel_onhitorblock_('CmnActFAirDash2Button')
        else:
            Unknown1653(0)
            Unknown1651(0)
            Unknown1356(0)
            Unknown1354(0)
            Unknown1652(0)
        if (SLOT_105 == 4):
            Unknown1671(20)

@Subroutine
def cmnAir_F_NO_STOP_IDLING():

    def upon_12():
        Unknown1056(0)
        if (SLOT_8 >= (-5000)):
            Unknown1056(1)

@Subroutine
def cmnKidan_RendaInit():
    storeValue(2, 46, 0, 0)
    if Unknown48(102):
        if Unknown48(128):
            if Unknown48(5):
                if Unknown48(14):
                    if Unknown48(23):
                        if Unknown48(28):
                            if (SLOT_104 <= 900000):
                                storeValue(2, 46, 0, 1)
                            elif Unknown48(76):
                                storeValue(2, 46, 0, 1)
    endIf()

@Subroutine
def cmnKidan_Init():
    Unknown1118('ARC_BTL_CMN_Hit_Kidan')
    Unknown1119('ARC_BTL_CMN_Guard_Kidan')
    Unknown1914(0)
    Unknown1954(1)
    Unknown458(0)
    Unknown58(1)
    Unknown289(300)
    Unknown2211(1)
    Unknown2221(1)
    Unknown2212(1)
    Unknown2213(1)
    Unknown2214(1)
    Unknown2215(1)
    Unknown35('2d0000004b6f776172650000000000000000000000000000000000000000000000000000')

    def upon_8():
        storeValue(2, 52, 0, 1)
        ActivateEffScript('cmn_kidan_end', 100)

    def upon_87():
        Unknown23(87)
        ActivateEffScript('cmn_reversalkidan', 100)
        storeValue(2, 52, 0, 1)
        Unknown450('')
        Unknown2208(23)

    def upon_2():
        Unknown448('bg_groundsmokeS', 123)
        Unknown670('00000000e80300000000000000000000')
        Unknown2208(23)

    def upon_3():
        if SLOT_52:
            Unknown54('0000000002000000340000000000000001000000')
        if (SLOT_52 > 5):
            storeValue(2, 52, 0, 0)
            if Unknown2033(3, 'NmlAtk5D'):
                Unknown53(3, 2, 52, 3, 0, 1)
            if Unknown2033(3, 'NmlAtk2D'):
                Unknown53(3, 2, 52, 3, 0, 1)
            if Unknown2033(3, 'NmlAtkAir5D'):
                Unknown53(3, 2, 52, 3, 0, 1)
            if Unknown2033(3, 'NmlAtkAir2D'):
                Unknown53(3, 2, 52, 3, 0, 1)

    def upon_47():
        Unknown23(47)
        Unknown23(3)

@Subroutine
def cmn5DKidan_AtkInit():
    callSubroutine('cmnNormalShot_AtkInit')
    damage1(300)
    Unknown1143(1)
    airHitPushbackX(25000)
    airHitPushbackY(6000)
    grHitPushbackX(120)
    untech_Override(20)
    mod_hitstop(5)

@Subroutine
def cmn2DKidan_AtkInit():
    callSubroutine('cmnNormalShot_AtkInit')
    Unknown1143(1)
    airHitPushbackX(10000)
    airHitPushbackY(15000)
    untech_Override(30)
    mod_hitstop(5)

@Subroutine
def cmnAir5DKidan_AtkInit():
    callSubroutine('cmnNormalShot_AtkInit')
    Unknown1143(1)
    airHitPushbackY(8000)
    untech_Override(20)
    mod_hitstop(5)

@Subroutine
def cmn_ChangeEnterCutscene():
    Unknown1670()
    Unknown2189(2, 5)
    Unknown92(0)
    if Unknown2033(23, 'CmnActChangeEnterCutscene'):
        storeValue(2, 45, 0, 1)

    def upon_3():
        onFrame(0, 0)
        if SLOT_45:
            ActivateEffScript('cmn_ChangeEnterCutsceneCamera', 100)
            ActivateEffScript('cmn_RestartEff_Ryuhai', 100)
        endIf()
        onFrame(0, 120)
        Unknown205(131500, 360000)
        if SLOT_45:
            Unknown2076('00000000530d0700efbe0400aa01000000c0ffff000000000f00000000000000780000000000000000000000')
            Unknown2077('RoundRestart', 500, 0, 30, 10)
        endIf()
        onFrame(0, 156)
        Unknown1708()
        endIf()
        onFrame(0, 160)
        Unknown1708()
        if SLOT_45:
            Unknown2076('0000000033bf0600efbe0400aa01000000c0ffff000000000f00000001000000000000000500000000000000')
        endIf()
        onFrame(0, 162)
        Unknown94(30000)
        Unknown206(-40000, 50000, 3200)
        endIf()

    def upon_2():
        Unknown14('landing')
        Unknown94(-30000)
        physicsImpulseX(-4000)
        Unknown2229(80)

@State
def cmn_Land_Break_S():
    sprite('null', 1)
    sprite('null', 1)
    Unknown670('00000000e80300000000000000000000')

@State
def cmn_whiteout():
    sprite('null', 20)
    Unknown294(1)
    Unknown2003(-1)
    Unknown188(1000000)
    Unknown92(0)
    Unknown98(500000)
    Unknown450('cmn_kizetu')

@State
def cmn_SmokeJizoku():

    def upon_IMMEDIATE():
        Unknown2480(1, 1)
        Unknown117(-1500, -3000)
        Unknown154(-150, 150)
        Unknown162(0, 150)
        Unknown103(-15000, 0)
        Unknown295(1)
        Unknown1801(1)
        Unknown2481(0, 0)
    sprite('null', 40)
    sprite('null', 40)

    def upon_79():
        Unknown23(79)
        Unknown23(84)
        if SLOT_241:
            pass
        else:
            pass
        Unknown14('ChangeSmoke')

    def upon_84():
        Unknown23(79)
        Unknown23(84)
        if SLOT_242:
            pass
        else:
            pass
        Unknown14('ChangeSmoke')
    sprite('null', 1)
    Unknown23(79)
    Unknown23(84)
    labelEnd('End')
    Unknown3()
    label('ChangeSmoke')
    sprite('null', 60)
    Unknown32('cmn_SmokeJizokuSub')
    Unknown3()
    label('End')

@State
def cmn_SmokeJizokuSub():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown457(2)
        Unknown1801(1)
    label('Loop')
    sprite('null', 10)
    Unknown3()
    labelEnd('Loop')

@Subroutine
def cmn_match_start_effect():
    Unknown449('bg_startwind', 143)

@Subroutine
def cmn_dashstart_default():
    Unknown449('bg_dash_default', 143)

@Subroutine
def cmn_dash_default():
    Unknown449('bg_dash_default', 143)

@Subroutine
def cmn_dashbrake_default():
    Unknown449('bg_dashbrake_default', 143)

@Subroutine
def cmn_jump_default():
    Unknown449('bg_jump_default', 143)

@Subroutine
def cmn_land_default():
    Unknown449('bg_land_default', 143)

@Subroutine
def cmn_down_default():
    Unknown449('bg_down_default', 104)
    ActivateEffScript('cmn_SmokeJizoku', 100)

@Subroutine
def cmn_nokezori_default():
    Unknown449('bg_nokezori_default', 143)

@Subroutine
def cmn_slidedown_default():
    Unknown2277(1)
    Unknown449('bg_undersmoke00', 143)

@Subroutine
def cmn_slidedownend_default():
    if (SLOT_282 == 0):
        Unknown2273(0, 1000)
    if (SLOT_282 == 1):
        Unknown2273(0, 1000)
    if (SLOT_282 == 2):
        Unknown2273(0, 1200)
    if (SLOT_282 == 3):
        Unknown2273(0, 1500)
    Unknown449('bg_land_default', 143)

@State
def cmn_futtobi_yoko_obj():
    sprite('null', 60)
    Unknown454(2)
    Unknown457(2)
    Unknown450('cmn_futtobi_yoko')

@State
def cmn_kirimomi_obj():
    sprite('null', 60)
    Unknown454(2)
    Unknown457(2)
    Unknown450('cmn_kirimomi')

@State
def cmn_LastRushHits():

    def upon_IMMEDIATE():
        Unknown455(3)
        Unknown457(3)
        Unknown454(2)
        Unknown295(1)
        Unknown450('cmn_RushSpeed')
        Unknown99(180000)
        Unknown94(150000)
    label('loops')
    sprite('null', 5)
    ActivateEffScript('cmn_LastRushHit', 100)
    Unknown41(1)
    Unknown94(40000)
    Unknown99(-40000)
    Unknown1732(40000)
    Unknown40()
    sprite('null', 5)
    ActivateEffScript('cmn_LastRushHit', 100)
    Unknown41(1)
    Unknown94(-40000)
    Unknown99(40000)
    Unknown1732(-40000)
    Unknown40()
    sprite('null', 5)
    ActivateEffScript('cmn_LastRushHit', 100)
    Unknown41(1)
    Unknown94(60000)
    Unknown40()
    Unknown3()
    labelEnd('loops')

@State
def cmn_LastRushHit():

    def upon_IMMEDIATE():
        Unknown455(2)
        Unknown457(2)
        Unknown454(2)
        Unknown295(1)
        Unknown450('cmn_RushHit')
    sprite('null', 30)

@State
def cmn_LastRushSousaiHits():

    def upon_IMMEDIATE():
        Unknown455(3)
        Unknown457(3)
        Unknown454(2)
        Unknown295(1)
        Unknown450('cmn_RushSpeed')
        Unknown99(180000)
        Unknown94(150000)
    label('loops')
    sprite('null', 7)
    ActivateEffScript('cmn_LastRushSousaiHit', 100)
    Unknown41(1)
    Unknown94(40000)
    Unknown99(-40000)
    Unknown1732(40000)
    Unknown40()
    sprite('null', 7)
    ActivateEffScript('cmn_LastRushSousaiHit', 100)
    Unknown41(1)
    Unknown94(-40000)
    Unknown99(40000)
    Unknown1732(-40000)
    Unknown40()
    sprite('null', 7)
    ActivateEffScript('cmn_LastRushSousaiHit', 100)
    Unknown41(1)
    Unknown94(60000)
    Unknown40()
    Unknown3()
    labelEnd('loops')

@State
def cmn_LastRushSousaiHit():

    def upon_IMMEDIATE():
        Unknown455(2)
        Unknown457(2)
        Unknown454(2)
        Unknown295(1)
        Unknown450('cmn_RushHit')
    sprite('null', 30)

@State
def cmn_LastTwinkle():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown295(1)
        Unknown450('cmn_Rush_Twinkle')
        Unknown178(22)
        Unknown99(-200000)
    sprite('null', 40)

@State
def cmn_LastRushSpeed():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown239()
        Unknown295(1)
        Unknown450('cmn_RushScrAnim01')
    sprite('null', 32)

@State
def cmn_LastRushAnim():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown239()
        Unknown295(1)
        Unknown671(7)
    sprite('null', 32)

@State
def cmn_AirLastRushAnim():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown239()
        Unknown295(1)
        Unknown671(8)
    sprite('null', 32)

@State
def cmn_LastRushAnim_Nml():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown239()
        Unknown295(1)
        Unknown671(7)
    sprite('null', 32)

@State
def cmn_AirLastRushAnim_Nml():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown239()
        Unknown295(1)
        Unknown671(8)
    sprite('null', 32)

@State
def cmn_RestartEff_Ryuhai():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('bg_restart_ryuhai')
    sprite('null', 48)
    ActivateEffScript('cmn_RestartEff_Smoke', 100)
    Unknown2095(0, 0)
    Unknown612('ARC_BTL_SYS_ReStart')
    sprite('null', 38)
    Unknown2096(1)
    sprite('null', 150)
    Unknown2136('80e5f9ff0000000000000000e803000000000000780000001e000000')
    ActivateEffScript('cmn_restart_shock', 100)
    ActivateEffScript('cmn_restart_groundsmoke', 100)
    ActivateEffScript('cmn_restart_groundsmoke2', 100)

@State
def cmn_RestartEff_Smoke():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown94(-6000000)
    sprite('null', 6)
    Unknown448('bg_restart_dash', 100)
    sprite('null', 4)
    physicsImpulseX(250000)
    Unknown448('bg_restart_dash', 100)
    sprite('null', 4)
    Unknown448('bg_restart_dash', 100)
    sprite('null', 2)
    Unknown448('bg_restart_dash', 100)
    sprite('null', 2)
    Unknown448('bg_restart_dash', 100)
    sprite('null', 3)
    Unknown448('bg_restart_dash', 100)
    sprite('null', 4)
    Unknown448('bg_restart_dash', 100)
    sprite('null', 3)
    Unknown448('bg_restart_dash', 100)
    physicsImpulseX(0)
    sprite('null', 3)
    Unknown2273(0, 1500)
    Unknown449('bg_restart_dash', 100)

@State
def cmn_restart_shock():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown1955('62675f726573746172745f73686f636b00000000000000000000000000000000')
        Unknown99(200000)
    sprite('null', 3)
    Unknown189(200)
    Unknown232(225000)
    sprite('null', 3)
    Unknown189(200)
    Unknown232(337500)
    sprite('null', 3)
    Unknown189(300)
    sprite('null', 3)
    Unknown189(300)
    Unknown232(450000)
    sprite('null', 3)
    Unknown189(400)
    sprite('null', 3)
    Unknown189(400)
    Unknown232(562500)
    sprite('null', 3)
    Unknown189(500)
    sprite('null', 3)
    Unknown189(500)
    Unknown232(675000)
    sprite('null', 3)
    Unknown189(600)
    sprite('null', 3)
    Unknown189(600)
    Unknown232(787500)
    sprite('null', 4)
    Unknown189(600)
    sprite('null', 150)
    Unknown232(0)

@State
def cmn_restart_groundsmoke():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown454(2)
        Unknown457(2)
        Unknown94(-800000)
        Unknown1732(150000)
    sprite('null', 10)
    Unknown2273(0, 2500)
    Unknown2283(0, -25000)
    Unknown449('bg_undersmoke00', 100)
    sprite('null', 10)
    Unknown2273(0, 2500)
    Unknown2283(0, -25000)
    Unknown449('bg_undersmoke00', 100)

@State
def cmn_restart_groundsmoke2():

    def upon_IMMEDIATE():
        Unknown456(2)
        Unknown454(2)
        Unknown457(2)
        Unknown94(800000)
        Unknown1732(150000)
    sprite('null', 10)
    Unknown2273(0, 2500)
    Unknown2283(0, -155000)
    Unknown449('bg_undersmoke00', 100)
    sprite('null', 10)
    Unknown2273(0, 2500)
    Unknown2283(0, -155000)
    Unknown449('bg_undersmoke00', 100)

@State
def cmn_GrandBrakeRockEX():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown1801(1)
        Unknown450('bg_GroundBrakeEX')
        Unknown466(2)
        Unknown169(7500, -7500)
        Unknown194(100, -100)
        Unknown103(0, -30000)
    sprite('null', 10)
    Unknown99(-150000)
    physicsImpulseY(10000)
    sprite('null', 50)
    physicsImpulseY(0)
    Unknown295(0)
    Unknown1801(0)
    sprite('null', 3)
    Unknown99(-7500)
    Unknown159(-10)
    sprite('null', 3)
    Unknown99(-7500)
    sprite('null', 3)
    Unknown99(-15000)
    sprite('null', 3)
    Unknown99(-15000)
    sprite('null', 3)
    Unknown99(-30000)
    sprite('null', 3)
    Unknown99(-30000)

@State
def cmn_FuttobasiEff_Ryuhai():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown457(2)
    sprite('null', 1)
    sprite('null', 10)
    Unknown450('bg_FuttobiFinish_ryuhai')
    Unknown2095(0, 0)
    sprite('null', 60)
    Unknown2096(1)
    Unknown450('bg_FuttobiFinish_ryuhaiEnd')

@State
def cmn_FuttobasiEff_smokeMatome():

    def upon_IMMEDIATE():
        Unknown457(2)
    sprite('null', 1)
    physicsImpulseX(-489999)
    ActivateEffScript('cmn_FuttobasiEff_smoke', 100)
    Unknown41(1)
    Unknown188(2500)
    Unknown1732(75000)
    Unknown99(32500)
    Unknown40()
    sprite('null', 2)
    ActivateEffScript('cmn_FuttobasiEff_smoke', 100)
    physicsImpulseX(-350000)
    sprite('null', 2)
    ActivateEffScript('cmn_FuttobasiEff_smoke', 100)
    sprite('null', 4)
    ActivateEffScript('cmn_FuttobasiEff_smoke', 100)
    sprite('null', 4)
    ActivateEffScript('cmn_FuttobasiEff_smoke', 100)
    sprite('null', 4)
    ActivateEffScript('cmn_FuttobasiEff_smoke', 100)
    sprite('null', 2147483647)

@State
def cmn_FuttobasiEff_smoke():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown186(100, 80)
        Unknown188(2200)
        Unknown450('bg_FuttobiFinish_smoke')
    sprite('null', 240)

@State
def cmn_bigSmokeEff():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown450('bg_pressuresmoke00')
        Unknown93(900000)
        Unknown98(120000)
        Unknown1731(-1000000)
        Unknown70('636d6e5f626967536d6f6b654566660000000000000000000000000000000000')
    sprite('null', 30)
    Unknown1801(1)
    sprite('null', 120)
    Unknown1801(0)

@State
def cmn_WinFlash():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown450('cmn_scrflash')
    sprite('null', 30)
    Unknown3()

@State
def PushAndDamage():

    def upon_IMMEDIATE():
        Unknown243()
        Unknown251(1)
        Unknown237(1)
    sprite('vr_debug_dmg', 2400)

@State
def PushFix():

    def upon_IMMEDIATE():
        Unknown243()
        Unknown251(1)
        Unknown237(1)
        Unknown363(-16711936)
        Unknown255(1)
    sprite('vr_debug_dmg', 2400)

@State
def HitStopObj():

    def upon_IMMEDIATE():
        Unknown245()
        mod_opphitstop(30, 30, 30)
        damage1(20000)
        Unknown178(22)
    sprite('vr_debug_dmg', 10)
    makeActive()
    sprite('vr_debug_dmg', 10)
    makeActive()
    sprite('vr_debug_dmg', 10)
    makeActive()
    sprite('vr_debug_dmg', 10)
    makeActive()
    sprite('vr_debug_dmg', 10)
    makeActive()
    sprite('vr_debug_dmg', 10)
    makeActive()
    sprite('vr_debug_dmg', 10)
    makeActive()
    sprite('vr_debug_dmg', 10)
    makeActive()

@State
def cmn_BattleStartCamera():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 180)
    Unknown2098(2, 22)
    Unknown2099(2, 22)
    Unknown2134(1)
    Unknown2052('BattleStart1', 23, 0, 1)

@State
def cmn_FinishCamera_Near1():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 60)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown2080('0d0000000e000000e8030000c0d4010080380100e8030000a086010000000000c0f2fcff32000000480000000f000000460000001e000000000000000200000002000000')
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def cmn_FinishCamera_Near2():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 60)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown2080('0d0000000e000000e8030000c0d4010080380100e8030000a086010000000000c0f2fcff32000000480000000f000000460000001e000000000000000200000002000000')
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def cmn_FinishCamera_Far1():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    if Unknown2031('200000004e6d6c41746b3243000000000000000000000000000000000000000000000000'):
        labelEnd('Test')
    if Unknown2031('200000005065726665637441747461636b5f420000000000000000000000000000000000'):
        labelEnd('Test')
    sprite('null', 3)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    Unknown2079('0e000000604bfbffe85807005dde0200c0f9ffff75180000000000003600000000000000b400000000000000000000000000000000000000')
    sprite('null', 3)
    Unknown2079('0e000000c39dfbff92e00600d0c70200c0f9ffff75180000000000003600000001000000b400000000000000000000000000000000000000')
    Unknown2079('0e000000604bfbffe85807005dde0200c0f9ffff75180000000000003600000001000000b400000000000000000000000000000000000000')
    sprite('null', 3)
    Unknown2079('0e000000c39dfbff92e00600d0c70200c0f9ffff75180000000000003600000001000000b400000000000000000000000000000000000000')
    sprite('null', 40)
    Unknown2079('0e0000004f2afcff4a13060031a10200c0f9ffff75180000000000003600000001000000b400000000000000000000000000000000000000')
    sprite('null', 42)
    Unknown2080('0d0000000e00000000000000f049020090d0030000000000f049020000000000c0f2fcff320000004800000021000000280000000a000000000000000200000002000000')
    Unknown32('cmn_syutyusen')
    Unknown3()
    Unknown18()
    label('Test')
    Unknown457(2)
    Unknown454(2)
    Unknown239()
    Unknown295(1)
    sprite('null', 60)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown2079('0d000000b4ce04004ab40500cbd800005d070000fddbffff0000000036000000000000007800000000000000000000000000000000000000')
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def cmn_FinishCamera_Far2():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    if Unknown2031('200000004e6d6c41746b3243000000000000000000000000000000000000000000000000'):
        labelEnd('Test')
    if Unknown2031('200000005065726665637441747461636b5f420000000000000000000000000000000000'):
        labelEnd('Test')
    sprite('null', 3)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    Unknown2079('0e000000604bfbffe85807005dde0200c0f9ffff75180000000000003600000000000000b400000000000000000000000000000000000000')
    sprite('null', 3)
    Unknown2079('0e000000c39dfbff92e00600d0c70200c0f9ffff75180000000000003600000001000000b400000000000000000000000000000000000000')
    Unknown2079('0e000000604bfbffe85807005dde0200c0f9ffff75180000000000003600000001000000b400000000000000000000000000000000000000')
    sprite('null', 3)
    Unknown2079('0e000000c39dfbff92e00600d0c70200c0f9ffff75180000000000003600000001000000b400000000000000000000000000000000000000')
    sprite('null', 40)
    Unknown2079('0e0000004f2afcff4a13060031a10200c0f9ffff75180000000000003600000001000000b400000000000000000000000000000000000000')
    sprite('null', 42)
    Unknown2080('0d0000000e00000000000000f049020090d0030000000000f049020000000000c0f2fcff320000004800000021000000280000000a000000000000000200000002000000')
    Unknown32('cmn_syutyusen')
    Unknown3()
    Unknown18()
    label('Test')
    Unknown457(2)
    Unknown454(2)
    Unknown239()
    Unknown295(1)
    sprite('null', 60)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown2079('0d000000b4ce04004ab40500cbd800005d070000fddbffff0000000036000000000000007800000000000000000000000000000000000000')
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def cmn_FinishCamera_Draw():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 59)

@State
def cmn_FinishCamera_TestForSousai():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 50)
    Unknown2231(1)

@State
def cmn_FinishCamera_DokiDoki():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 100)
    Unknown2080('0d0000000e00000050c30000a0860100a086010000000000a08601000000000010b6fdff1e0000005a0000000a0000003c0000000a000000000000000200000000000000')

@State
def cmn_FinishCamera_XNearYFar():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 3)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    Unknown2079('0e000000604bfbffe85807005dde0200c0f9ffff75180000000000003600000000000000b400000000000000000000000000000000000000')
    sprite('null', 3)
    Unknown2079('0e000000c39dfbff92e00600d0c70200c0f9ffff75180000000000003600000001000000b400000000000000000000000000000000000000')
    Unknown2079('0e000000604bfbffe85807005dde0200c0f9ffff75180000000000003600000001000000b400000000000000000000000000000000000000')
    sprite('null', 3)
    Unknown2079('0e000000c39dfbff92e00600d0c70200c0f9ffff75180000000000003600000001000000b400000000000000000000000000000000000000')
    sprite('null', 40)
    Unknown2079('0e0000004f2afcff4a13060031a10200c0f9ffff75180000000000003600000001000000b400000000000000000000000000000000000000')
    sprite('null', 42)
    Unknown2079('0e0000004f2afcff4a13060031a10200c0f9ffff75180000000000003600000021000000280000000a000000000000000200000002000000')
    Unknown32('cmn_syutyusen')
    Unknown3()

@State
def cmn_FinishCamera_AkebonoNear():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 60)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown2080('0d0000000e000000e8030000c0d4010080380100e8030000a086010000000000c0f2fcff32000000480000000f000000460000001e000000000000000200000002000000')
    Unknown2077('ShakeTate', 1500, 3, 20, 3)
    sprite('null', 30)
    Unknown32('cmn_syutyusen')

@State
def cmn_FinishCamera_AkebonoFar():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
    sprite('null', 3)
    ActivateEffScript('cmn_syutyusen', 132)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2077('ShakeTate', 1500, 3, 25, 3)
    Unknown2079('0e000000604bfbffe85807005dde0200c0f9ffff75180000000000003600000000000000b400000000000000000000000000000000000000')
    sprite('null', 3)
    Unknown2079('0e000000c39dfbff92e00600d0c70200c0f9ffff75180000000000003600000001000000b400000000000000000000000000000000000000')
    Unknown2079('0e000000604bfbffe85807005dde0200c0f9ffff75180000000000003600000001000000b400000000000000000000000000000000000000')
    sprite('null', 3)
    Unknown2079('0e000000c39dfbff92e00600d0c70200c0f9ffff75180000000000003600000001000000b400000000000000000000000000000000000000')
    sprite('null', 20)
    Unknown2079('0e0000004f2afcff4a13060031a10200c0f9ffff75180000000000003600000001000000b400000000000000000000000000000000000000')
    sprite('null', 62)
    Unknown2080('0d0000000e00000000000000f049020090d0030000000000f049020000000000c0f2fcff3200000048000000350000001400000014000000000000000200000002000000')
    Unknown32('cmn_syutyusen')
    Unknown3()
    Unknown18()

@State
def cmn_AkebonoFinish():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown1801(1)
        Unknown98(0)
        Unknown450('cmn_specialbg')
        Unknown448('cmn_akebono_slow', 100)
        Unknown41(22)
        Unknown2273(0, 350)
        Unknown449('cmn_finish_akebono', 102)
        Unknown40()

    def upon_1():
        Unknown2133('0a000000000000000000000000000000')
        Unknown2096(0)
        Unknown2231(1)
    sprite('null', 180)
    Unknown612('ARC_BTL_CMN_Hit_XLarge')
    Unknown2095(0, 0)

@State
def cmn_hijump_obj():
    sprite('null', 40)
    Unknown450('cmn_hijump')
    Unknown156(3000)
    Unknown454(2)
    Unknown456(2)
    Unknown458(2)
    Unknown338(0)

    def upon_3():
        if (SLOT_13 >= 2):
            if Unknown2033(2, 'CmnActJump'):
                Unknown338(255)
                if (SLOT_13 <= 8):
                    Unknown53(23, 2, 7, 2, 2, 7)
                    Unknown53(23, 2, 8, 2, 2, 8)
                    Unknown200(90000)
                    Unknown176(1)

@State
def cmn_DragonRushCamera_m():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2082()
        Unknown178(2)
    sprite('null', 180)
    Unknown2052('DragonRush_m', 23, 5, 1)

@State
def cmn_ChangeEnterCutsceneCamera():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
        Unknown178(2)
        Unknown2052('ReStart', 23, 0, -1)
    sprite('null', 180)

@State
def cmn_CameraFuttobiFinish_nomove():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
        Unknown1801(0)
    sprite('null', 1)
    Unknown2076('6f810300e1d60400b7a50100acfeffffb9e9ffff000000003600000001000000b40000000100000001000000')
    Unknown2077('ShakeTate', 1500, 0, 60, 30)
    sprite('null', 220)
    Unknown239()
    Unknown2052('BlowOffFinish_nomove', 23, 15, -1)

@State
def cmn_FuttobiFinish_root():

    def upon_IMMEDIATE():
        Unknown457(2)
        ActivateEffScript('cmn_FuttobasiEff_Ryuhai', 100)
    sprite('null', 10)

    def upon_3():
        onFrame(0, 0)
        Unknown631('000000004152435f42475f4674627346696e5f426c6f774f75740000000000000000000064000000')
        endIf()
        onFrame(0, 30)
        Unknown633(0, 60)
        endIf()
        onFrame(0, 70)
        Unknown612('ARC_BG_FtbsFin_Hit')
        endIf()
    sprite('null', 1)
    ActivateEffScript('cmn_FuttobiFinish_bg', 100)
    sprite('null', 9999)

@State
def cmn_FuttobiFinish_bg():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown298(1)
        Unknown457(2)
        Unknown2095(0, 0)
        Unknown450('bg_FuttobiFinishBG')
    sprite('null', 9999)

@Subroutine
def cmn_DestFinishInit_root():
    Unknown295(1)
    Unknown1801(1)
    Unknown298(1)
    Unknown301()

@Subroutine
def cmn_DestFinishInit_bg():
    Unknown295(1)
    Unknown298(1)
    Unknown457(2)

@State
def cmn_DestFinish_Ground_root():

    def upon_IMMEDIATE():
        callSubroutine('cmn_DestFinishInit_root')
    sprite('null', 1)
    if (SLOT_280 == 0):
        Unknown448('cmn_DestructionFinish2_Start', 100)
    else:
        Unknown448('cmn_DestructionFinish_Start', 100)
    sprite('null', 25)
    sprite('null', 45)
    if (SLOT_280 == 0):
        Unknown612('ARC_BG_ExplFin_Tunagi')
    else:
        Unknown612('ARC_BG_LsrFin_Tunagi')
    sprite('null', 90)
    Unknown300()
    sprite('null', 1)
    Unknown1801(0)
    Unknown294(1)
    Unknown1801(1)
    Unknown2097()
    Unknown2082()
    Unknown92(0)
    Unknown98(0)
    Unknown1731(0)
    sprite('null', 230)
    if (SLOT_280 == 0):
        Unknown612('ARC_BTL_CMN_ExplFin_Near')
    else:
        Unknown612('ARC_BTL_CMN_LsrFin_Near')
    Unknown2052('DestructionFinish_Ground', 23, 0, -1)
    ActivateEffScript('cmn_DestFinish_Ground_bg', 100)
    ActivateEffScript('cmn_DestFinish_Ground_Effect', 100)
    sprite('null', 150)
    Unknown302()

@State
def cmn_DestFinish_Ground_bg():

    def upon_IMMEDIATE():
        callSubroutine('cmn_DestFinishInit_bg')
        Unknown450('bg_DestructionFinish_BG')
        Unknown188(10000)
    sprite('null', 500)

@State
def cmn_DestFinish_Ground_Effect():

    def upon_IMMEDIATE():
        Unknown188(10000)
        callSubroutine('cmn_DestFinishInit_bg')
        if (SLOT_280 == 0):
            Unknown450('DestructionFinish_Ground_bomb')
        else:
            Unknown450('DestructionFinish_Ground_beam')
    sprite('null', 500)

@State
def cmn_DestFinish_Planet_root():

    def upon_IMMEDIATE():
        callSubroutine('cmn_DestFinishInit_root')
    sprite('null', 1)
    if (SLOT_280 == 0):
        Unknown448('cmn_DestructionFinish2_Start', 100)
    else:
        Unknown448('cmn_DestructionFinish_Start', 100)
    sprite('null', 25)
    sprite('null', 45)
    if (SLOT_280 == 0):
        Unknown612('ARC_BG_ExplFin_TunagiFar')
    else:
        Unknown612('ARC_BG_LsrFin_TunagiFar')
    sprite('null', 90)
    Unknown300()
    sprite('null', 1)
    Unknown1801(0)
    Unknown294(1)
    Unknown1801(1)
    Unknown2097()
    Unknown2082()
    Unknown92(0)
    Unknown98(0)
    Unknown1731(0)
    sprite('null', 230)
    if (SLOT_280 == 0):
        Unknown2052('DestructionFinish_Planet_Bomb', 23, 0, -1)
        Unknown612('ARC_BTL_CMN_ExplFin_Far')
    else:
        Unknown2052('DestructionFinish_Planet_Beam', 23, 0, -1)
        Unknown612('ARC_BTL_CMN_LsrFin_Far')
    ActivateEffScript('cmn_DestFinish_Planet_bg', 100)
    ActivateEffScript('cmn_DestFinish_Planet_Effect', 100)
    sprite('null', 150)
    Unknown302()

@State
def cmn_DestFinish_Planet_bg():

    def upon_IMMEDIATE():
        callSubroutine('cmn_DestFinishInit_bg')
        Unknown450('bg_DestructionFinish_BG')
    sprite('null', 500)

@State
def cmn_DestFinish_Planet_Effect():

    def upon_IMMEDIATE():
        callSubroutine('cmn_DestFinishInit_bg')
        if (SLOT_280 == 0):
            Unknown450('DestructionFinish_Planet_Bomb')
        else:
            Unknown450('DestructionFinish_Planet_Beam')
        Unknown188(10000)
    sprite('null', 500)

@Subroutine
def cmn_match_start_destruction():
    ActivateEffScript('cmn_after_destruction', 100)

@State
def cmn_after_destruction():

    def upon_IMMEDIATE():
        Unknown92(0)
        Unknown98(0)
        Unknown1731(0)
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
        Unknown450('cmn_DestructionFinish_End')
    sprite('null', 1)
    sprite('null', 300)
    Unknown612('ARC_BG_FinSmoke_PreFight')
    Unknown2076('00000000603d0800406c08000000000000c0ffff000000003600000000000000000000007800000000000000')

@State
def cmn_BGTransStart():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
        Unknown454(2)
        Unknown1801(0)
    sprite('null', 1)
    Unknown2076('6f810300e1d60400b7a50100acfeffffb9e9ffff000000003600000001000000b40000000100000001000000')
    Unknown2077('ShakeTate', 1500, 0, 60, 30)
    Unknown612('ARC_BG_FtbsFin_Start')
    sprite('null', 6)
    physicsImpulseX(5000)
    ActivateEffScript('cmn_BGChangeRyuhai', 100)
    Unknown2077('ShakeTateYoko', 250, 0, 100, 0)
    sprite('null', 14)
    Unknown612('ARC_BG_FtbsFin_Futtobi')
    sprite('null', 30)
    sprite('null', 3)
    ActivateEffScript('cmn_BGChangeWipeOut', 100)

@State
def cmn_BGChangeWipeOut():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown450('cmn_bgchange_wipeout')
    sprite('null', 30)

@State
def cmn_BGChangeRyuhai():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown454(2)
        Unknown457(2)
    sprite('null', 1)
    sprite('null', 10)
    Unknown450('bg_bgchange_ryuhai')
    Unknown2095(0, 0)
    sprite('null', 300)

@Subroutine
def cmn_match_start_futtobi_transbg():
    ActivateEffScript('cmn_BGChangeCamera', 100)
    ActivateEffScript('cmn_BGChangeMatome', 100)

@State
def cmn_BGChangeCamera():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
        Unknown92(0)
        Unknown98(0)
        Unknown1731(0)
        Unknown239()
    sprite('null', 100)
    Unknown2052('BlowOffFinish_move', 23, 0, 1)

@State
def cmn_BGChangeMatome():

    def upon_IMMEDIATE():
        pass
    sprite('null', 9)
    Unknown2095(0, 0)
    ActivateEffScript('cmn_BGChangeWipeIn', 100)
    ActivateEffScript('cmn_BGChangeBG', 100)
    Unknown43(4, 1)
    ActivateEffScript('cmn_BGChangeObjectA', 100)
    ActivateEffScript('cmn_BGChangeObjectB', 100)
    sprite('null', 28)
    Unknown1803('cmn_BGChangeObjectA', 23)
    sprite('null', 38)
    Unknown1803('cmn_BGChangeObjectB', 23)
    sprite('null', 1)
    Unknown32('cmn_BGChangeObjectA')
    Unknown32('cmn_BGChangeObjectB')
    Unknown19(4)
    Unknown2095(1000, 0)
    ActivateEffScript('cmn_BGChangeStart', 100)

@State
def cmn_BGChangeWipeIn():

    def upon_IMMEDIATE():
        Unknown450('cmn_bgchange_wipein')
    sprite('null', 30)

@State
def cmn_BGChangeBG():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('bg_bgchange_bg')
    sprite('null', 2147483647)

@State
def cmn_BGChangeObjectA():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('bg_bgchange_objA')
        Unknown35('1700000042726f6b656e0000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    label('Broken')
    sprite('null', 2147483647)
    Unknown450('bg_bgchange_objA_broken')
    Unknown3()

@State
def cmn_BGChangeObjectB():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown450('bg_bgchange_objB')
        Unknown35('1700000042726f6b656e0000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    label('Broken')
    sprite('null', 2147483647)
    Unknown450('bg_bgchange_objB_broken')
    Unknown3()

@State
def cmn_BGChangeStart():

    def upon_IMMEDIATE():
        Unknown2502(80, 40)
    sprite('null', 100)
    Unknown3()

@State
def cmn_ShenlongSystem():

    def upon_IMMEDIATE():
        Unknown1971(1)
        Unknown242()
        Unknown2082()
        Unknown295(1)
        Unknown1801(1)
        Unknown298(1)
        Unknown271('08000000640000001027000010270000')
        storeValue(2, 45, 0, 255)
        storeValue(2, 46, 0, 0)
        Unknown397()

        def upon_1():
            Unknown400()
    sprite('null', 2147483647)

    def upon_3():
        onFrame(0, 0)
        Unknown2095(0, 140)
        endIf()
        onFrame(0, 15)
        Unknown41(2)
        Unknown624('vxxx129', 100, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown40()
        endIf()
        onFrame(0, 56)
        Unknown612('ARC_BTL_CMN_Shenlong_Appear')
        endIf()
        onFrame(0, 60)
        ActivateEffScript('cmn_DragonBall', 100)
        ActivateEffScript('cmn_Shenlong_StartCamera', 100)
        endIf()
        onFrame(0, 140)
        Unknown404(0)
        endIf()
        onFrame(0, 140)
        Unknown2425(0, 0)
        ActivateEffScript('cmn_DBstartBG', 164)
        endIf()
        onFrame(0, 222)
        ActivateEffScript('cmn_ShenlongAura', 100)
        endIf()
        onFrame(0, 222)
        Unknown403(1)
        Unknown2422(-1, 90)
        Unknown32('cmn_DragonBall')
        endIf()
        onFrame(0, 312)
        ActivateEffScript('cmn_ShenlongBG', 100)
        ActivateEffScript('cmn_Shenlong', 100)
        ActivateEffScript('cmn_Shenlong_IdleCamera', 100)
        Unknown32('cmn_Shenlong_StartCamera')
        Unknown2423(60)
        Unknown2425(1, 1)
        endIf()
        onFrame(0, 380)
        Unknown399(300)
        Unknown14('UI')
        endIf()
    Unknown3()
    label('UI')
    sprite('null', 15)
    sprite('null', 1)
    Unknown405()
    label('wish')
    sprite('null', 1)
    Unknown54('00000000020000002e0000000000000001000000')
    if (SLOT_45 != 255):
        Unknown14('decide')
    elif (SLOT_46 >= 300):
        Unknown14('close')
    labelEnd('wish')
    label('decide')
    sprite('null', 60)
    label('close')
    sprite('null', 15)
    Unknown400()
    Unknown2422(-1, 15)
    sprite('null', 2147483647)

    def upon_3():
        onFrame(0, 0)
        Unknown2425(0, 0)
        Unknown2423(30)
        ActivateEffScript('cmn_Shenlong_FinishCamera', 100)
        Unknown32('cmn_ShenlongBG')
        Unknown32('cmn_Shenlong')
        Unknown32('cmn_Shenlong_IdleCamera')
        ActivateEffScript('cmn_DBdisapear', 100)
        Unknown404(1)
        Unknown612('ARC_BTL_CMN_Shenlong_Gone')
        endIf()
        onFrame(0, 90)
        Unknown2425(1, 1)
        Unknown403(0)
        Unknown2096(60)
        endIf()
        onFrame(0, 180)
        Unknown32('cmn_Shenlong_FinishCamera')
        Unknown14('Execute')
        endIf()
    Unknown3()
    label('Execute')
    sprite('null', 60)
    Unknown402()
    sprite('null', 1)
    Unknown398()

@State
def cmn_Shenlong():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown2157('5368656e676c6f6e670000000000000000000000000000000000000000000000')
        Unknown2045('SRN001cs', 0)
    sprite('null', 2147483647)

@State
def cmn_DragonBall():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown2189(2, 5)
        Unknown2157('447261676f6e42616c6c00000000000000000000000000000000000000000000')
        Unknown2045('DRB001cs', 0)
    sprite('null', 2147483647)

@State
def cmn_Shenlong_StartCamera():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
        Unknown2052('DRB001', 23, 0, 0)
    sprite('null', 2147483647)

@State
def cmn_Shenlong_IdleCamera():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
        Unknown2052('SRN001', 23, 0, 6)
    sprite('null', 2147483647)

@State
def cmn_Shenlong_FinishCamera():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown294(1)
        Unknown1801(1)
        Unknown2097()
        Unknown2082()
        Unknown2052('DRB002', 23, 0, 6)
    sprite('null', 2147483647)

@State
def cmn_ShenlongFlash():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown450('cmn_shenlongFlash')
        Unknown457(2)
        Unknown99(300000)
    sprite('null', 240)

@State
def cmn_DBstartBG():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown450('cmn_DBstartBG')
    sprite('null', 600)

@State
def cmn_ShenlongAura():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown450('cmn_shenlongAura')
        Unknown457(2)
        Unknown99(-4000000)
        Unknown1732(500000)
        Unknown188(4000)
    sprite('null', 30)
    physicsImpulseY(90000)
    Unknown1736(-27428)
    sprite('null', 50)
    physicsImpulseY(2000)
    Unknown1736(0)

@State
def cmn_ShenlongBG():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown457(2)
        Unknown450('cmn_shenlongBG')
        Unknown99(250000)
        Unknown1732(-4000000)
    sprite('null', 2147483647)

@State
def cmn_DBdisapear():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown450('cmn_DBdisapear')
        Unknown457(2)
        Unknown99(4500000)
    sprite('null', 120)

@State
def cmn_SpecialBG():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown1801(1)
        Unknown450('cmn_specialbg')
    sprite('null', 2147483647)
    Unknown35('1700000046616465456e6400000000000000000000000000000000000000000000000000')
    Unknown3()
    label('FadeEnd')
    sprite('null', 10)

@State
def cmn_Windpressure_Tate():

    def upon_IMMEDIATE():
        Unknown295(1)
    sprite('null', 60)
    Unknown450('cmn_strike00')

@State
def cmn_Windpressure_Yoko():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown164(80000)
    sprite('null', 60)
    Unknown450('cmn_strike00')

@State
def cmn_kidan_end():

    def upon_IMMEDIATE():
        Unknown450('cmn_bomb_s3')
        Unknown294(1)
        Unknown1801(1)
    sprite('null', 7)
    Unknown2136('000000000000000000000000f4010000000000003c0000001e000000')
    sprite('null', 51)
    Unknown1801(0)

@State
def cmn_kidan_end_M():

    def upon_IMMEDIATE():
        Unknown450('cmn_bomb_s2')
        Unknown294(1)
        Unknown1801(1)
        Unknown188(700)
    sprite('null', 11)
    Unknown2136('000000000000000000000000f4010000000000003c0000001e000000')
    sprite('null', 65)
    Unknown1801(0)

@State
def cmn_kidan_end_L():

    def upon_IMMEDIATE():
        Unknown450('cmn_bomb_sp')
        Unknown294(1)
        Unknown1801(1)
    sprite('null', 15)
    Unknown2136('000000000000000000000000e803000000000000640000001e000000')
    sprite('null', 120)
    Unknown1801(0)

@State
def cmn_bomb_g1_end():

    def upon_IMMEDIATE():
        Unknown450('cmn_bomb_g1')
        Unknown294(1)
        Unknown1801(1)
    sprite('null', 15)
    Unknown2136('000000000000000000000000f4010000000000003c0000001e000000')
    sprite('null', 50)
    Unknown1801(0)

@State
def cmn_bomb_g2_end():

    def upon_IMMEDIATE():
        Unknown450('cmn_bomb_g2')
        Unknown294(1)
        Unknown1801(1)
    sprite('null', 15)
    Unknown2136('000000000000000000000000e803000000000000640000001e000000')
    sprite('null', 80)
    Unknown1801(0)

@State
def cmn_kidan():

    def upon_IMMEDIATE():
        Unknown450('cmn_kidan')
        physicsImpulseX(40000)
    sprite('null', 1)
    ActivateEffScript('cmn_mazzle', 100)
    label('1')
    sprite('null', 1)
    Unknown113(1000)
    labelEnd('1')

@State
def cmn_mazzle():

    def upon_IMMEDIATE():
        Unknown188(1200)
    sprite('null', 100)
    Unknown450('cmn_mazzle')

@State
def cmn_kidan_charge():

    def upon_IMMEDIATE():
        Unknown454(2)
        Unknown450('cmn_charge')
    sprite('null', 300)
    Unknown3()

@State
def cmn_kidan_smoke():

    def upon_IMMEDIATE():
        Unknown94(-100000)
    sprite('null', 1)
    Unknown448('bg_undersmoke00', 100)

@State
def cmn_GroundSmoke():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown98(0)
        Unknown94(150000)
    label('loop')
    sprite('null', 10)
    Unknown448('bg_undersmoke00', 100)
    Unknown3()
    labelEnd('loop')

@State
def cmn_reversal_mazzle():
    Unknown448('cmn_reversal_mazzle', 100)

@State
def cmn_reversalkidan():

    def upon_IMMEDIATE():
        Unknown476('636d6e5f726576657273616c5f6b6964616e0000000000000000000000000000')
        Unknown176(1)
    sprite('null', 2147483647)
    ActivateEffScript('cmn_reversal_mazzle', 100)

@State
def cmn_blue_reversalkidan():

    def upon_IMMEDIATE():
        Unknown476('636d6e5f626c75655f726576657273616c5f6b6964616e000000000000000000')
        Unknown176(1)
    sprite('null', 2147483647)
    ActivateEffScript('cmn_reversal_mazzle', 100)

@State
def cmn_kamehameha_shadow():

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
    Unknown23(23)
    Unknown3()

@State
def cmn_kamehameha_shadow_Assist():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown289(300)
        Unknown35('17000000656e640000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2147483647)
    Unknown450('cmn_shadowLine_loop_Assist')
    Unknown3()
    label('end')
    sprite('null', 1)
    Unknown23(23)
    Unknown3()

@State
def cmn_HomingDash_Jizoku():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown671(2)
    sprite('null', 2147483647)

@State
def cmn_HomingDash_JizokuTrail():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown671(3)
    sprite('null', 2147483647)

@State
def cmn_HomingDash_Start():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown671(5)
    sprite('null', 12)

@State
def cmn_HomingDash_End():

    def upon_IMMEDIATE():
        Unknown671(4)
        Unknown295(1)
        Unknown1801(1)
    sprite('null', 30)

@State
def cmn_HomingDash_Stop():

    def upon_IMMEDIATE():
        Unknown457(2)
        Unknown454(2)
        Unknown671(6)
    sprite('null', 2147483647)

@State
def cmn_SparkingAuraObj():

    def upon_IMMEDIATE():
        Unknown450('cmn_SparkingAura')
        Unknown1976(1)
    sprite('null', 2147483647)

@State
def cmn_syutyusen():

    def upon_IMMEDIATE():
        Unknown450('cmn_syutyusen')
        Unknown1976(1)
    sprite('null', 200)

@State
def cmn_syutyusen2():

    def upon_IMMEDIATE():
        Unknown450('cmn_syutyusen2')
        Unknown1976(1)
        Unknown188(500)
    sprite('null', 200)

@State
def cmn_DestructionCollision():
    sprite('null', 2)

@State
def cmn_HUDTutorial():

    def upon_IMMEDIATE():
        Unknown295(1)
        Unknown1801(1)
        Unknown298(1)
        Unknown271('00000000640000001027000010270000')
        Unknown2095(50, 1)
        Unknown2511()

        def upon_1():
            Unknown2096(1)
    sprite('null', 2147483647)

@Subroutine
def DebugBomberInit():
    Unknown244()
    or_standhit(8)
    or_launchhit(8)
    airHitPushbackX(25000)
    airHitPushbackY(25000)
    Unknown778(5000)
    Unknown711(4)
    Unknown1028(4)
    Unknown1093(100)
    Unknown1095(0)
    Unknown1018(1)
    Unknown1079(1)
    ChangeAtkDir(3)

@State
def cmn_DebugBomberDageki():

    def upon_IMMEDIATE():
        callSubroutine('DebugBomberInit')
        Unknown1028(0)
    sprite('debugbomber', 1)
    makeActive()

@State
def cmn_DebugBomberShot():

    def upon_IMMEDIATE():
        callSubroutine('DebugBomberInit')
    sprite('debugbomber', 1)
    makeActive()

@State
def cmn_DramaticFinishStart():

    def upon_IMMEDIATE():
        Unknown294(1)
        Unknown1801(1)
    sprite('null', 15)
    sprite('null', 200)
    Unknown2137(120, 0, 0)

@State
def DUMMYDUMMY():
    sprite('null', 1)