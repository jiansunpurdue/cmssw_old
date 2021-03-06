import FWCore.ParameterSet.Config as cms

ptSeedParameterization = cms.PSet(
    SMB_21 = cms.vdouble(1.04575, -0.163287, 0.0, 0.183661, -0.049415, 
        0.0),
    SMB_20 = cms.vdouble(0.990194, -0.058027, 0.0, 0.157433, 0.049581, 
        0.0),
    SMB_22 = cms.vdouble(1.389607, -0.691458, 0.0, -0.204387, 0.471755, 
        0.0),
    OL_2213 = cms.vdouble(0.736644, -0.65969, 0.0, -0.429713, 0.813747, 
        0.0),
    # Sigle CSC Segments 
    # CSCDet_Id         p1        p2        p3       ep1      ep2      ep3
    #------------------------------------------------------------------------    #
    SME_11 = cms.vdouble(2.612846, -0.976852, 0.0, -5.986027, 4.000885, 
        0.0),
    SME_13 = cms.vdouble(0.576629, 0.010521, 0.0, 0.624575, 1.518433, 
        0.0),
    SME_12 = cms.vdouble(0.02713, 0.623194, 0.0, 1.623888, -0.362265, 
        0.0),
    SME_32 = cms.vdouble(-0.242825, 0.163158, 0.0, 183.95999, -133.799119, 
        0.0),
    SME_31 = cms.vdouble(-0.4583, 0.2501, 0.0, -202.733432, 92.182385, 
        0.0),
    SME_42 = cms.vdouble(-0.242825, 0.163158, 0.0, 183.95999, -133.799119, 
        0.0),
    # OL Parameters 
    # Det_Layers        p1        p2        p3       ep1      ep2      ep3
    #------------------------------------------------------------------------    #
    OL_1213 = cms.vdouble(1.089127, -0.865182, 0.0, 0.307029, -0.056826, 
        0.0),
    DT_13 = cms.vdouble(0.333344, 0.089449, -0.171128, 0.149048, -0.097795, 
        0.174794),
    # DT Parameters 
    # Det_Stations          p1        p2        p3       ep1      ep2      ep3
    #------------------------------------------------------------------------    #
    DT_12 = cms.vdouble(0.192702, 0.067231, -0.1026, 0.13832, -0.120017, 
        0.175494),
    DT_14 = cms.vdouble(0.380675, 0.091873, -0.172667, 0.192447, -0.04005, 
        0.100509),
    OL_1232 = cms.vdouble(0.19594, -0.012048, 0.0, 0.366937, -0.002214, 
        0.0),
    CSC_23 = cms.vdouble(-0.095236, 0.122061, -0.029852, -11.396689, 15.933598,
        -4.267065),
    CSC_24 = cms.vdouble(-0.049769, 0.063087, -0.011029, -13.765978, 16.296143,
        -4.241835),
    CSC_03 = cms.vdouble(0.498992, -0.086235, -0.025772, 2.761006, -2.667607,
        0.72802),
    SMB_31 = cms.vdouble(0.5905, -0.172563, 0.0, 0.591524, -0.051003, 
        0.0),
    # CSC Parameters 
    # Det_Stations      p1        p2        p3       ep1      ep2      ep3
    #------------------------------------------------------------------------    #
    CSC_01 = cms.vdouble(0.155906, -0.000406, 0.0, 0.194022, -0.010181,
        0.0),
    SMB_32 = cms.vdouble(0.632907, -0.255332, 0.0, 0.951006, -0.216346, 
        0.0),
    SMB_30 = cms.vdouble(0.54032, -0.064278, 0.0, 0.579023, -0.090837, 
        0.0),
    OL_2222 = cms.vdouble(0.067377, 0.0, 0.0, 0.76627, 0.0, 
        0.0),
    # Sigle DT Segments 
    # DTDet_Id          p1        p2        p3       ep1      ep2      ep3
    #------------------------------------------------------------------------    #
    SMB_10 = cms.vdouble(1.350718, -0.122906, 0.0, 0.118062, -0.079225, 
        0.0),
    SMB_11 = cms.vdouble(1.42858, -0.157879, 0.0, 0.075437, 0.031277, 
        0.0),
    SMB_12 = cms.vdouble(1.920222, -0.779074, 0.0, 0.065771, 0.066339, 
        0.0),
    DT_23 = cms.vdouble(0.136351, 0.04724, -0.089448, 0.220512, -0.056609, 
        0.167122),
    DT_24 = cms.vdouble(0.186817, 0.059153, -0.111626, 0.312139, -0.156575, 
        0.469607),
    SME_21 = cms.vdouble(1.155785, -0.364076, 0.0, -19.122395, 13.18083, 
        0.0),
    SME_22 = cms.vdouble(-0.739515, 0.769174, 0.0, 58.238261, -37.114818, 
        0.0),
    CSC_34 = cms.vdouble(0.144321, -0.142283, 0.035636, 190.260708, -180.888643,
        43.430395),
    CSC_02 = cms.vdouble(0.600235, -0.205683, 0.001113, 0.655625, -0.682129,
        0.253916),
    SME_41 = cms.vdouble(-0.698854, 0.306105, 0.0, -44.919988, 17.730305, 
        0.0),
    DT_34 = cms.vdouble(0.040386, 0.007193, -0.016506, 1.514816, -1.460786, 
        1.555718),
    CSC_14 = cms.vdouble(0.952517, -0.532733, 0.084601, 1.615881, -1.630744,
        0.514139),
    OL_1222 = cms.vdouble(0.251087, 0.004875, 0.0, 0.282026, -0.001649, 
        0.0),
    CSC_13 = cms.vdouble(1.22495, -1.792358, 0.711378, 5.271848, -6.280625,
        2.0142),
    CSC_12 = cms.vdouble(-0.363549, 0.569552, -0.173186, 7.777069, -10.203618,
        3.478874)
)


