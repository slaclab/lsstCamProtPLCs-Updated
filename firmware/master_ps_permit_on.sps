$Name <FILENAME>

! Obj_Source
;Project created by:
;Joao Rodrigues SLAC
;joaoprod@slac.staford.edu
;
;Project reviewed by:
;
;Project tested by:
;
;
;
;History of change:

#Include <func06.fps>

! Id_Pluto[D20]:1=000000000001
! Id_Pluto[D20]:2=000000000002
! Id_Pluto[D20]:3=000000000003


! I1.0=P1_TSW0                          ;Thermal switch PRT-UTT-TSSW-00
! I1.1=P1_TSW1                          ;Thermal switch  PRT-UTT-TSSW-01
! I1.2=P1_TSW2                          ;Thermal switch  PRT-UTT-TSSW-02
! I1.3=P1_TSW3                          ;Thermal switch  PRT-UTT-TSSW-03
! I1.4=P1_NO_LEAK                       ;No Leak signal from leak detector PRT-UTT-LLD-00
! I1.5=P1_LEAK                          ;Leak signal from leak detector PRT-UTT-LLD-00
! I1.6=P1_SMK                           ;Smoke detector alarm contact PRT-UTT-SMK-00
! I1.7=P1_LEAK_FAULT                    ;Leak detector fault signal  PRT-UTT-LLD-00
! Q1.0=P1_UTPowPerm                     ;Utility Trunk High Power Permit PWR-UTT-FRB-00
! Q1.1=P1_REBPowPerm                    ;REB Power Suplly Permit
! Q1.2=P1_CoolantValve                  ;Coolant valve contrrol PRT-UTT-RLY-00
! Q1.3=P1_LeakPow                       ;Leak Detection Power PRT-UTT-DCD-00
! GM1.0=P1_TSW0L                        ;Latch TSW0 input
! GM1.1=P1_TSW1L                        ;Latch TSW1 input
! GM1.2=P1_TSW2L                        ;Latch TSW2 input
! GM1.3=P1_TSW3L                        ;Latch TSW3 input
! GM1.4=P1_SMKL                         ;Latch SMK input
! GM1.5=P1_LEAKL                        ;Latch Leak input
! GM1.6=P1_LEAKFAULTL                   ;Latch Leak Fault input
! GM1.7=P1_NO_LEAKL                     ;Latch No Leak input
! GM1.8=P1_TempOkL                      ;3 of four temps ok
! GM1.10=P1_Overflow                    ;
! GM1.11=P1_Present                     ;
! Q2.0=P2_ColdHeatPerm                  ;Cold Plate Heater Permit
! Q2.1=P2_ColdRefPerm                   ;Cold Plate refrigerator Permit
! GM2.7=P2_MasterReset                  ;Resets all latches for intialization purposes
! Q3.0=P3_CryoHeatPerm                  ;Cryo Plate Heater Permit
! Q3.1=P3_CryoRefPerm                   ;Cryo Plate refrigerator Permit

! Pgm_Pluto:1
! Instruction_Set_3
! Ext_comm:0=Device 0,Packet 0, 400
;PRT-UTT-PLC1
;
;Utility Trunk Power Interlocks
;REB PS interlocks
;
;Inputs: Utility trunk thermal switches, smoke detector, master permit, reset
;Controls: Utility Trunk Power and the REB power supplies.
;


! Q1.10=P1_APower                       ;TSW0, TSW2 and Smoke Detector Power
! Q1.11=P1_BPower                       ;TSW3, No_Leak and Leak Power ????????????????
! Q1.12                                 ;Smoke detector contact power
! Q1.13=P1_UTLeakAn                     ;UT Coolant Leak Indicator
! Q1.14=P1_UTHotAn                      ;UT Hot Indicator
! Q1.15=P1_UTSmkAn                      ;UT Smoke Indicator
! Q1.16=P1_UTPowAn                      ;UT Power Status
! Q1.17=P1_REBPowAn                     ;REB Power Status
! M1.5=P1_OutToGateway                  ;????????????????????
! M1.6=P1_ResetUTe                      ;External reset for the utility trunk power
! M1.7=P1_MUTReset                      ;(External UT reset) OR (Master reset)


S1.0_0
P1_UTPowPerm
P1_REBPowPerm
P1_CoolantValve:P1_LeakPow

! Pgm_Pluto:2
! Instruction_Set_3
;PRT-UTT-PLC2
;
;Cold Heaters and Refrigeration Interlocks
;
;Inputs: 4 cold plate conditioned  RTD anlalog signals plus a reset
;Outputs: Cold plate heater interlock and cold plater refrigerator interlock
;




S2.0_0
P2_ColdHeatPerm
P2_ColdRefPerm

! Pgm_Pluto:3
! Instruction_Set_3
;PRT-UTT-PLC3
;
;Cryo Heaters and Refrigeration Interlocks
;
;Inputs: 4 cryo plate conditioned  RTD anlalog signals, vacuum status,  plus resets
;Outputs: Cryo plate heater interlock and cryo plate refrigerator interlock




S3.0_0
P3_CryoHeatPerm
P3_CryoRefPerm
