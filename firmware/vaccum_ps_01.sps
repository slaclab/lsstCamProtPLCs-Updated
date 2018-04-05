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

! Id_Pluto_Double[D45]:0=000000000010


! I0.0                                  ;HEX Vacuum Gauge for interlock safety VHX-UTT-GCC-01
! I0.1                                  ;HEX Turbo Vac VHX-UTT-GCC-00
! I0.2                                  ;Main Chamber redundant seal VCR-UTT-GCC-02
! I0.3                                  ;Cryostat Vacuum monitor VCR-UTT-GCC-01
! I0.4                                  ;Cryostat Vacuum Gauge for interlock safety VCR-UTT-GCC-00
! I0.6=HVTurboSpeed                     ;HEX Vacuum Turbo speed
! I0.7=CVTurboSpeed                     ;Cryostat Vacuum Turbo speed
! Q0.0=CVStat                           ;Cryostat Vacuum Status PRT-UTT-PLC-03/I6
! Q0.1=HVStat                           ;HEX-Can Vacuum Status PRT-UTT-PLC-03/I5
! Q0.2=MainVcrVcc                       ;Cryostat VCR-UTT-VCC-00
! Q0.3=MainVhxVcc                       ;HEX-Can VHX-UTT-VGC-01

! Pgm_Pluto:0
! Instruction_Set_3
;VCR-UTT-PLC-00
;
;Cryo Vaccum PLC

! I0.0,Analog,10V
! I0.1,Analog,10V
! I0.2,Analog,10V
! I0.3,Analog,10V
! I0.4,Analog,10V
! I0.6,Analog,10V
! I0.7,Analog,10V
! I0.30,A_Pulse,Non_Inv
! I0.31,A_Pulse,Non_Inv
! I0.32,B_Pulse,Non_Inv
! I0.33,B_Pulse,Non_Inv
! I0.34,C_Pulse,Non_Inv
! Q0.10,A_Pulse
! Q0.11,B_Pulse
! Q0.12,C_Pulse
! Q0.20,Static
! Q0.21,Static
! Q0.22,Static
! Q0.23,Static

! Q0.4=VCRPumpPerm                      ;Cryo Turbo Pump Permit VCR-UTT-PCT-00/J1-3
! Q0.5=VHXPumpPerm                      ;HEX-Can Turbo Pump Permit VHX-UTT-PCT-01/J1-3
! Q0.10=APower                          ;VCR-UTT-VCC-00
! Q0.11=BPower                          ;VHX-UTT-VGC-00
! Q0.12=CPower                          ;roufhing pump contact
! Q0.20=VcrVcc01                        ;VCR-UTT-VCC-01
! Q0.21=VcrVcc02                        ;VCR-UTT-VCC-02
! Q0.22=VcrVcc03                        ;VCR-UTT-VCC-03
! Q0.23=VcrVcc04                        ;VCR-UTT-VCC-04


S0.0_0
CVStat:HVStat:MainVcrVcc:VHXPumpPerm:VCRPumpPerm
MainVhxVcc
