# pybricks blocks file:{"blocks":{"languageVersion":0,"blocks":[{"type":"blockGlobalSetup","id":"bjK,wS1MYO7aiYkFSwd{","x":-124,"y":-212,"deletable":false,"next":{"block":{"type":"variables_set_xbox_controller","id":"~:i4j7srgTq~Z;E4g|o;","fields":{"VAR":{"id":"A8X8@1XBK9_Px_$-@W,L"}},"next":{"block":{"type":"variables_set_technic_hub","id":"``3lHmaB@iSl6RV;hBs)","extraState":{"optionLevel":2},"fields":{"VAR":{"id":"TQ6ny{0sf4|FBX)HumD@"},"FIELDBROADCAST":0},"inputs":{"AXIS_TOP":{"shadow":{"type":"blockParametersAxis","id":"xXUA,/P7t!N2/Gm@DUKw","fields":{"VALUE":"z"}}},"AXIS_FRONT":{"shadow":{"type":"blockParametersAxis","id":"p{Cg(Dvs[{7etCj_rE9q","fields":{"VALUE":"x"}}}},"next":{"block":{"type":"variables_set_motor","id":"BTwzxrw;/!nCiX#{fM!?","fields":{"VAR":{"id":"]FHhb|O4.qHZ|@R27y;o"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"L7s)gfH)U1Kp|*,zRle:","fields":{"NAME":"B"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"lu%H7A9pS%Rosdpd8}BM","fields":{"SELECTION":"Direction.COUNTERCLOCKWISE"}}}},"next":{"block":{"type":"variables_set_motor","id":"-z_f$zMmk}_j,[Ci_z/~","fields":{"VAR":{"id":"7qXs_1~:Inu:|UQyn3K$"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"=Qz*MH|*5Vfgo0OQSVmb","fields":{"NAME":"A"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"+2o6x(e.3m(Ie}a[uxk{","fields":{"SELECTION":"Direction.CLOCKWISE"}}}},"next":{"block":{"type":"variables_set_motor","id":"7C(#CLIw6_+{gu$lQ!^G","fields":{"VAR":{"id":"et}D7}-mSrg`)g2/s!v|"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"tBUPhF_Ee|jI.24YSTl^","fields":{"NAME":"D"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"e[TJ;K},ez3lcZ]haxMa","fields":{"SELECTION":"Direction.COUNTERCLOCKWISE"}}}}}}}}}}}}}}},{"type":"blockGlobalStart","id":"3tJe|AWl0baN(wH9a$@.","x":-124,"y":157,"deletable":false,"next":{"block":{"type":"blockComment","id":"6A$*-Wv/;G`KM,NSRc[7","fields":{"FIELDNAME":"You need to start bottom hub + xbox controller first\nThen start the top hub\nHere are the controls:\nRight and left triggers and buttons are for the tracks\nDpad left / right are for the main structure rotate\nLeft joystick vertical is for main structure \nright joystick horizontal and vertical are for the other motors\nA button is for opening the bucket\nB button is for closing the bucket"},"next":{"block":{"type":"blockMotorConfigure","id":"_-(CH+f9[crFQbbj=@7{","extraState":{"optionLevel":1},"fields":{"METHOD":"MOTOR_ACCELERATION"},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"4.4G$w|:~|]FuRfZS`;.","fields":{"VAR":{"id":"7qXs_1~:Inu:|UQyn3K$","name":"left tracks","type":"Motor"}}}},"ARG0":{"shadow":{"type":"unit_angularAcceleration","id":"`%{H$7bWtTYfeI,J,ay*","fields":{"VALUE0":2500}}}},"next":{"block":{"type":"blockMotorConfigure","id":"ggluwEXm4^Nv@yNDt@$9","extraState":{"optionLevel":1},"fields":{"METHOD":"MOTOR_ACCELERATION"},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"DT!H0X5nxfhj#EqEQy]_","fields":{"VAR":{"id":"]FHhb|O4.qHZ|@R27y;o","name":"right tracks","type":"Motor"}}}},"ARG0":{"shadow":{"type":"unit_angularAcceleration","id":"kykHuG_}^1sJ+U6XSWG^","fields":{"VALUE0":2500}}}},"next":{"block":{"type":"blockMotorConfigure","id":"@*J2!-8NGN14o#1ciEjo","extraState":{"optionLevel":1},"fields":{"METHOD":"MOTOR_ACCELERATION"},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"xpHWky7QiUMAk;0-+R*b","fields":{"VAR":{"id":"et}D7}-mSrg`)g2/s!v|","name":"base","type":"Motor"}}}},"ARG0":{"shadow":{"type":"unit_angularAcceleration","id":"I-kF~p;hiM}nF9.x6oJ8","fields":{"VALUE0":2500}}}},"next":{"block":{"type":"blockLightOnColor","id":"eilOu*@HmcD[-$yUZv-z","extraState":{"optionLevel":1},"fields":{"METHOD":"LIGHT_ON"},"inputs":{"VAR":{"shadow":{"type":"variables_get_color_light_device","id":"19R1WpeGx9c;{Fz=UrZ|","fields":{"VAR":{"id":"TQ6ny{0sf4|FBX)HumD@","name":"bottom","type":"TechnicHub"}}}},"COLOR":{"shadow":{"type":"variables_get_color","id":"Q_GYg)ba)[8%.O+}A`3c","fields":{"COLOUR":"#00ff00","VAR":{"id":"voNeNNP$#9J.GDn*.vTx","name":"green","type":"ColorDef"}}}}},"next":{"block":{"type":"blockFlowWhile","id":"uO#7]DY[+.kr{AU?m^1D","fields":{"MODE":"WHILE"},"inputs":{"BOOL":{"shadow":{"type":"blockLogicTrue","id":"sz[r_x8h-g=Ihy9FYk.."}},"DO":{"block":{"type":"blockIfElse","id":"%lx}IQ:T(gvn:N~n[x-u","extraState":{"optionLevel":0},"inputs":{"IF0":{"shadow":{"type":"blockLogicTrue","id":"|62l-s^6nf4j3Qa0OV=S"},"block":{"type":"blockButtonIsPressed","id":"eB[gidDJ`BT-vL[XWE7@","inputs":{"VAR":{"shadow":{"type":"variables_get_keypad","id":"?=0O2l*|?E0ZFhCQ$mQx","fields":{"VAR":{"id":"TQ6ny{0sf4|FBX)HumD@","name":"bottom","type":"TechnicHub"}}}},"VALUE0":{"shadow":{"type":"blockParametersButton","id":"9(*g39E13O)Ag{#7SS3(","fields":{"VALUE":"CENTER"}}}}}},"DO0":{"block":{"type":"blockHubShutdown","id":"Kja]%}kci*gJjorxq-eQ","inputs":{"VAR":{"shadow":{"type":"variables_get_button_hub","id":"#_i#w`BB5Ur08WN|4o@K","fields":{"VAR":{"id":"TQ6ny{0sf4|FBX)HumD@","name":"bottom","type":"TechnicHub"}}}}}}}},"next":{"block":{"type":"blockIfElse","id":"p]e9O96EP{n4E]73+)Fr","extraState":{"optionLevel":1},"inputs":{"IF0":{"shadow":{"type":"blockLogicTrue","id":"uQqPE3/U11XoCUPtOfGI"},"block":{"type":"blockJoystickValue","id":"_K3Fdoz;872iP@*!0*BX","fields":{"JOYSTICK":"XBOX_LT"},"inputs":{"VAR":{"shadow":{"type":"variables_get_gamepad","id":"?vmqH@IYi/Q`[k2G#r$Q","fields":{"VAR":{"id":"A8X8@1XBK9_Px_$-@W,L","name":"xbox","type":"XboxController"}}}}}}},"DO0":{"block":{"type":"blockMotorRun","id":"y#q2^!=qm!.bJ|*HQOtS","extraState":{"optionLevel":0},"fields":{"METHOD":"MOTOR_RUN_FOREVER"},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"IrMw!}X3ZT.SM`46D+Rq","fields":{"VAR":{"id":"7qXs_1~:Inu:|UQyn3K$","name":"left tracks","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_angularVelocity","id":"d@;DArr7oi5DJg6Rb7a|","fields":{"VALUE0":500}},"block":{"type":"blockMathArithmetic","id":"@15rKS#Q#GV%.m+#0/b9","fields":{"OP":"MULTIPLY"},"inputs":{"A":{"shadow":{"type":"blockMathNumber","id":"]8VGN~A[H[tUywhJ-Szw","fields":{"NUM":25}}},"B":{"shadow":{"type":"blockMathNumber","id":"9%BtezH}M8NMbyA?N*I(","fields":{"NUM":1}},"block":{"type":"blockJoystickValue","id":"{y@)GhNr`_y_#;S4PYq;","fields":{"JOYSTICK":"XBOX_LT"},"inputs":{"VAR":{"shadow":{"type":"variables_get_gamepad","id":"E0PXd71^Pc*Z{d)UN$Gb","fields":{"VAR":{"id":"A8X8@1XBK9_Px_$-@W,L","name":"xbox","type":"XboxController"}}}}}}}}}}}}},"ELSE":{"block":{"type":"blockIfElse","id":"A/sZoXOQIQHJ#_./FUK(","extraState":{"optionLevel":1},"inputs":{"IF0":{"shadow":{"type":"blockLogicTrue","id":"/YG.q$A0H)lRhcnsGs{V"},"block":{"type":"blockButtonIsPressed","id":"s?G3dC87e0]3i)tkghfk","inputs":{"VAR":{"shadow":{"type":"variables_get_keypad","id":"TFH?1baJ6Yw^[aTEo!6)","fields":{"VAR":{"id":"A8X8@1XBK9_Px_$-@W,L","name":"xbox","type":"XboxController"}}}},"VALUE0":{"shadow":{"type":"blockParametersButton","id":"A,8;3kXOt9(W`q:!m`mD","fields":{"VALUE":"LB"}}}}}},"DO0":{"block":{"type":"blockMotorRun","id":"dBD+|Ch{K%(eSImMy;|R","extraState":{"optionLevel":0},"fields":{"METHOD":"MOTOR_RUN_FOREVER"},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"p966x+#%WY1g6VN]McFd","fields":{"VAR":{"id":"7qXs_1~:Inu:|UQyn3K$","name":"left tracks","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_angularVelocity","id":"pLrzI7{92HS_;Y[u|xX}","fields":{"VALUE0":-2500}}}}}},"ELSE":{"block":{"type":"blockMotorStop","id":"$fT?Dwzr`]r/N}6_hx~o","inputs":{"VAR":{"shadow":{"type":"variables_get_simple_motor_device","id":"{As~B(NUBhvVP*|xTZmM","fields":{"VAR":{"id":"7qXs_1~:Inu:|UQyn3K$","name":"left tracks","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"parameters_stop_3","id":"{TF+O#vv~0B4ahv}hPSj","fields":{"VALUE":"Stop.BRAKE"}}}}}}}}}},"next":{"block":{"type":"blockIfElse","id":"M[jo.@e7PUwvrL)`vM#x","extraState":{"optionLevel":1},"inputs":{"IF0":{"shadow":{"type":"blockLogicTrue","id":"+Wwv.Y/)dU^tq:3s`!{S"},"block":{"type":"blockJoystickValue","id":"tKbuEN,Uc[X}Y6.WN)~e","fields":{"JOYSTICK":"XBOX_RT"},"inputs":{"VAR":{"shadow":{"type":"variables_get_gamepad","id":"MEq$-Vo{x(ZH~RculHcJ","fields":{"VAR":{"id":"A8X8@1XBK9_Px_$-@W,L","name":"xbox","type":"XboxController"}}}}}}},"DO0":{"block":{"type":"blockMotorRun","id":"D{V#%2@uIbXycW1y2lno","extraState":{"optionLevel":0},"fields":{"METHOD":"MOTOR_RUN_FOREVER"},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"x]*{P@ul9O9|.hq/v+T2","fields":{"VAR":{"id":"]FHhb|O4.qHZ|@R27y;o","name":"right tracks","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_angularVelocity","id":"NNg4-Ri8rmFY!+h.5W;4","fields":{"VALUE0":500}},"block":{"type":"blockMathArithmetic","id":"0Hbz=1kP_]!biX`.T}88","fields":{"OP":"MULTIPLY"},"inputs":{"A":{"shadow":{"type":"blockMathNumber","id":"!oILbMfpL01JOA:A+9n#","fields":{"NUM":25}}},"B":{"shadow":{"type":"blockMathNumber","id":"gz(,xI;K*Q?k1U,t?kqV","fields":{"NUM":1}},"block":{"type":"blockJoystickValue","id":"NU7qa;Z[@jYVZnhPY]w$","fields":{"JOYSTICK":"XBOX_RT"},"inputs":{"VAR":{"shadow":{"type":"variables_get_gamepad","id":":iO2Tn37ISA.L#=PqEC*","fields":{"VAR":{"id":"A8X8@1XBK9_Px_$-@W,L","name":"xbox","type":"XboxController"}}}}}}}}}}}}},"ELSE":{"block":{"type":"blockIfElse","id":"E6|k/lyC@6SMfavifXL[","extraState":{"optionLevel":1},"inputs":{"IF0":{"shadow":{"type":"blockLogicTrue","id":"WONf+nF1/mb]8-5Gare~"},"block":{"type":"blockButtonIsPressed","id":"6O!C[[xZ){CKZbG{U6B%","inputs":{"VAR":{"shadow":{"type":"variables_get_keypad","id":"!bI]aIoWf|L`:te:BH0F","fields":{"VAR":{"id":"A8X8@1XBK9_Px_$-@W,L","name":"xbox","type":"XboxController"}}}},"VALUE0":{"shadow":{"type":"blockParametersButton","id":"hD=|`QuG_A-qM|wV3NBV","fields":{"VALUE":"RB"}}}}}},"DO0":{"block":{"type":"blockMotorRun","id":"BhCS.bd^Zp*P9tK%[kjx","extraState":{"optionLevel":0},"fields":{"METHOD":"MOTOR_RUN_FOREVER"},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"SybVdhz6fF9V:G-u%0BY","fields":{"VAR":{"id":"]FHhb|O4.qHZ|@R27y;o","name":"right tracks","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_angularVelocity","id":"GhiU:v3Dc:n96l!UZTNR","fields":{"VALUE0":-2500}}}}}},"ELSE":{"block":{"type":"blockMotorStop","id":"q7[Eygp[SHkyN3-Xl91k","inputs":{"VAR":{"shadow":{"type":"variables_get_simple_motor_device","id":"#qzZmcTqTUiq(2}Sr0/8","fields":{"VAR":{"id":"]FHhb|O4.qHZ|@R27y;o","name":"right tracks","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"parameters_stop_3","id":"Z17KXV]fszz*V#g74rQY","fields":{"VALUE":"Stop.BRAKE"}}}}}}}}}},"next":{"block":{"type":"blockIfElse","id":"A%)*xBa]3rpaet45L40`","extraState":{"optionLevel":1},"inputs":{"IF0":{"shadow":{"type":"blockLogicTrue","id":"yDF?^|o}V5vts86GeP0B"},"block":{"type":"blockButtonIsPressed","id":"Cy.)]F!/I(3/iJh/re`-","inputs":{"VAR":{"shadow":{"type":"variables_get_keypad","id":"ASe@*{$FSI;4gR$^Vr:3","fields":{"VAR":{"id":"A8X8@1XBK9_Px_$-@W,L","name":"xbox","type":"XboxController"}}}},"VALUE0":{"shadow":{"type":"blockParametersButton","id":"u;s2G#*;XF5`@I~G0`F,","fields":{"VALUE":"LEFT"}}}}}},"DO0":{"block":{"type":"blockMotorRun","id":"*ttR0N)rP$eh~8OmlL_$","extraState":{"optionLevel":0},"fields":{"METHOD":"MOTOR_RUN_FOREVER"},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"H4Zc-ZnTkUT,90YmhnJ{","fields":{"VAR":{"id":"et}D7}-mSrg`)g2/s!v|","name":"base","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_angularVelocity","id":"tt,B~C#tI4k.6V8`sl)S","fields":{"VALUE0":-2500}}}}}},"ELSE":{"block":{"type":"blockIfElse","id":"Tbaa|,TFarfoG9`[#YZ-","extraState":{"optionLevel":1},"inputs":{"IF0":{"shadow":{"type":"blockLogicTrue","id":"yDF?^|o}V5vts86GeP0B"},"block":{"type":"blockButtonIsPressed","id":"!3uvJyV0XhSRMZXXlB5=","inputs":{"VAR":{"shadow":{"type":"variables_get_keypad","id":"tvRBjEy1n|~[i6NXiyU.","fields":{"VAR":{"id":"A8X8@1XBK9_Px_$-@W,L","name":"xbox","type":"XboxController"}}}},"VALUE0":{"shadow":{"type":"blockParametersButton","id":"O)|ZzzBLSU2`7zlJVjX%","fields":{"VALUE":"RIGHT"}}}}}},"DO0":{"block":{"type":"blockMotorRun","id":"~)~i7q,/K0-)r`m$gVI2","extraState":{"optionLevel":0},"fields":{"METHOD":"MOTOR_RUN_FOREVER"},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"={CumKlu4PKUz|55}vuP","fields":{"VAR":{"id":"et}D7}-mSrg`)g2/s!v|","name":"base","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_angularVelocity","id":".F4)yo{j*m76e]UwdYdw","fields":{"VALUE0":2500}}}}}},"ELSE":{"block":{"type":"blockMotorStop","id":"Gt2G[`PpmSaePf24WU=%","inputs":{"VAR":{"shadow":{"type":"variables_get_simple_motor_device","id":"%Dp6lpbY#5dME91Ke?c0","fields":{"VAR":{"id":"et}D7}-mSrg`)g2/s!v|","name":"base","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"parameters_stop_3","id":"O}yK+TCrDTwW7q)#i;_2","fields":{"VALUE":"Stop.BRAKE"}}}}}}}}}},"next":{"block":{"type":"blockBleBroadcast","id":"O]|cG7uhUyL}_(x],/IR","inputs":{"VAR":{"shadow":{"type":"variables_get_ble_hub","id":"l;|I7=b#7+)*Y2D7P~d4","fields":{"VAR":{"id":"TQ6ny{0sf4|FBX)HumD@","name":"bottom","type":"TechnicHub"}}}},"VALUE0":{"shadow":{"type":"blockMathNumber","id":"^]{Pids!T`ZnGU3;NWch","fields":{"NUM":0}},"block":{"type":"blockListCreate","id":"`l|tGQ,v%8LN)TPIv^ZJ","extraState":{"optionLevel":5},"inputs":{"ADD0":{"shadow":{"type":"blockMathNumber","id":"[+n^VX}#`^F9m~bERW3~","fields":{"NUM":0}},"block":{"type":"blockJoystickValue","id":"I1=}mp,C)rMTKYe`.OkA","fields":{"JOYSTICK":"XBOX_LJ_Y"},"inputs":{"VAR":{"shadow":{"type":"variables_get_gamepad","id":"}EJ^D6;?k:7utwuFti.J","fields":{"VAR":{"id":"A8X8@1XBK9_Px_$-@W,L","name":"xbox","type":"XboxController"}}}}}}},"ADD1":{"shadow":{"type":"blockMathNumber","id":"klW}{|9+P[4,7ZnAm;0$","fields":{"NUM":0}},"block":{"type":"blockJoystickValue","id":"ETKm5Wk=;7o2t1`c3t-5","fields":{"JOYSTICK":"XBOX_RJ_X"},"inputs":{"VAR":{"shadow":{"type":"variables_get_gamepad","id":"j.#07pU+NXZs=q0CB-d0","fields":{"VAR":{"id":"A8X8@1XBK9_Px_$-@W,L","name":"xbox","type":"XboxController"}}}}}}},"ADD2":{"shadow":{"type":"blockMathNumber","id":"O%[}H#F{ELTU?#D.OmGH","fields":{"NUM":0}},"block":{"type":"blockJoystickValue","id":"]-2*M!zHnzmQsu.F|!u*","fields":{"JOYSTICK":"XBOX_RJ_Y"},"inputs":{"VAR":{"shadow":{"type":"variables_get_gamepad","id":"f81;rsa-:q{M.7]@.S}g","fields":{"VAR":{"id":"A8X8@1XBK9_Px_$-@W,L","name":"xbox","type":"XboxController"}}}}}}},"ADD3":{"shadow":{"type":"blockMathNumber","id":",HN,xZ$z~nwTf#La/vq1","fields":{"NUM":0}},"block":{"type":"blockLogicTernary","id":"7LC/^B4:Ez#e4Xyh.^^6","inputs":{"THEN":{"shadow":{"type":"blockMathNumber","id":"VF6B*}4Na%{[y*3Hi-u^","fields":{"NUM":1}}},"IF":{"shadow":{"type":"blockLogicTrue","id":"N0S;*i1XQ2O*@h$FnNo%"},"block":{"type":"blockButtonIsPressed","id":"ao9:M1n5UDMwO8*mH,Le","inputs":{"VAR":{"shadow":{"type":"variables_get_keypad","id":"M#|`f1x5N;O+=_5M0r1%","fields":{"VAR":{"id":"A8X8@1XBK9_Px_$-@W,L","name":"xbox","type":"XboxController"}}}},"VALUE0":{"shadow":{"type":"blockParametersButton","id":"W`(=O({J=.L48)5J*QZi","fields":{"VALUE":"A"}}}}}},"ELSE":{"shadow":{"type":"blockMathNumber","id":"|KtjEop~5]w42_:zF`U@","fields":{"NUM":0}}}}}},"ADD4":{"shadow":{"type":"blockMathNumber","id":"1B7cwL+SM^gP6ig^qEb;","fields":{"NUM":0}},"block":{"type":"blockLogicTernary","id":"BK{%UJL6ycDh-onYn1-m","inputs":{"THEN":{"shadow":{"type":"blockMathNumber","id":"AzBHy3Dxj8x0qHxCUv?0","fields":{"NUM":1}}},"IF":{"shadow":{"type":"blockLogicTrue","id":"1iH@iW{p8PK3HoyMDbaa"},"block":{"type":"blockButtonIsPressed","id":"Bc89Ws.FC-MqywLu7u]n","inputs":{"VAR":{"shadow":{"type":"variables_get_keypad","id":"R8Zk|_);`b+-]4Hqt31n","fields":{"VAR":{"id":"A8X8@1XBK9_Px_$-@W,L","name":"xbox","type":"XboxController"}}}},"VALUE0":{"shadow":{"type":"blockParametersButton","id":"c*lm9|YKz$(.H7TJw*59","fields":{"VALUE":"B"}}}}}},"ELSE":{"shadow":{"type":"blockMathNumber","id":"Bq,i,^t,nat;EK|c;%Dx","fields":{"NUM":0}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}]},"variables":[{"name":"red","id":"oC!lXf$5HeAqEjlas4P_","type":"ColorDef"},{"name":"orange","id":".}R_hekVWVP`WuqCmkdI","type":"ColorDef"},{"name":"yellow","id":"+(_T1/q/bJCeP[W_+=)x","type":"ColorDef"},{"name":"green","id":"voNeNNP$#9J.GDn*.vTx","type":"ColorDef"},{"name":"cyan","id":":uBI(?qO#FqbSm{]h57~","type":"ColorDef"},{"name":"blue","id":"@+)g:ZUZ%(tX7L^7DK)v","type":"ColorDef"},{"name":"violet","id":"b+*4b(TSNAE}s-ERFn,1","type":"ColorDef"},{"name":"magenta","id":"|:0(4RXJPol_HNkzf=$0","type":"ColorDef"},{"name":"white","id":"3Mu5C%3yzy1nb_p$_IcT","type":"ColorDef"},{"name":"none","id":"1]5a[lxR:$]n%ic73au2","type":"ColorDef"},{"name":"bottom","id":"TQ6ny{0sf4|FBX)HumD@","type":"TechnicHub"},{"name":"xbox","id":"A8X8@1XBK9_Px_$-@W,L","type":"XboxController"},{"name":"base","id":"et}D7}-mSrg`)g2/s!v|","type":"Motor"},{"name":"left tracks","id":"7qXs_1~:Inu:|UQyn3K$","type":"Motor"},{"name":"right tracks","id":"]FHhb|O4.qHZ|@R27y;o","type":"Motor"}],"info":{"type":"pybricks","version":"1.2.3"}}
from pybricks.hubs import TechnicHub
from pybricks.iodevices import XboxController
from pybricks.parameters import Axis, Button, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor

# Set up all devices.
bottom = TechnicHub(top_side=Axis.Z, front_side=Axis.X, broadcast_channel=0)
right_tracks = Motor(Port.B, Direction.COUNTERCLOCKWISE)
left_tracks = Motor(Port.A, Direction.CLOCKWISE)
base = Motor(Port.D, Direction.COUNTERCLOCKWISE)
xbox = XboxController()


# The main program starts here.
# You need to start bottom hub + xbox controller first
# Then start the top hub
# Here are the controls:
# Right and left triggers and buttons are for the tracks
# Dpad left / right are for the main structure rotate
# Left joystick vertical is for main structure
# right joystick horizontal and vertical are for the other motors
# A button is for opening the bucket
# B button is for closing the bucket
left_tracks.control.limits(acceleration=2500)
right_tracks.control.limits(acceleration=2500)
base.control.limits(acceleration=2500)
bottom.light.on(Color.GREEN)
while True:
    if Button.CENTER in bottom.buttons.pressed():
        bottom.system.shutdown()
    if xbox.triggers()[0]:
        left_tracks.run(25 * xbox.triggers()[0])
    else:
        if Button.LB in xbox.buttons.pressed():
            left_tracks.run(-2500)
        else:
            left_tracks.brake()
    if xbox.triggers()[1]:
        right_tracks.run(25 * xbox.triggers()[1])
    else:
        if Button.RB in xbox.buttons.pressed():
            right_tracks.run(-2500)
        else:
            right_tracks.brake()
    if Button.LEFT in xbox.buttons.pressed():
        base.run(-2500)
    else:
        if Button.RIGHT in xbox.buttons.pressed():
            base.run(2500)
        else:
            base.brake()
    bottom.ble.broadcast([xbox.joystick_left()[1], xbox.joystick_right()[0], xbox.joystick_right()[1], 1 if Button.A in xbox.buttons.pressed() else 0, 1 if Button.B in xbox.buttons.pressed() else 0])