def search_in_file(term):
    file_content = """
    "	H2O	Acqua	Ossido di idrogeno		
	CO2	Anidride carbonica	Ossido di carbonio (IV)		
	NaCl	Sale comune	Cloruro di sodio		
	H2SO4	Acido solforico	Acido ossosolforico		
	NH3	Ammoniaca	Tri idruro di azoto		
	CaCO3	Calcite	Carbonato di calcio		
	CH4	Metano	Metano		
	HCl	Acido cloridrico	Cloruro di idrogeno		
	NaOH	Soda caustica	Idrossido di sodio		
	Fe2O3	Ematite	Ossido di ferro (III)		
	KCl	Cloruro di potassio	Cloruro di potassio		
	HNO3	Acido nitrico	Acido ossonitrico		
	Mg(OH)2	Idrossido di magnesio	Idrossido di magnesio		
	H2S	Idrogeno solforato	Solfo idruro di idrogeno		
	CO	Monossido di carbonio	Ossido di carbonio (II)		
	Na2CO3	Carbonato di sodio	Carbonato di sodio		
	CuSO4	Solfato di rame (II)	Solfato di rame (II)		
	H2O2	Perossido di idrogeno	Idrogeno perossido		
	Na2SO4	Solfato di sodio	Solfato di sodio		
	Ba(OH)2	Idrossido di bario	Idrossido di bario		
	CO3	Carbonato	Carbonato		
	SiO2	Biossido di silicio	Ossido di silicio (IV)		
	CaCl2	Cloruro di calcio	Cloruro di calcio		
	Na2O	Ossido di sodio	Ossido di sodio		
	SO2	Anidride solforosa	Ossido di zolfo (IV)		
	Al2O3	Allumina	Ossido di alluminio		
	CuO	Ossido di rame (II)	Ossido di rame (II)		
	H2	Idrogeno	Di idruro di idrogeno		
	NaH	Idruro di sodio	Tri idruro di sodio		
	MgCl2	Cloruro di magnesio	Cloruro di magnesio		
	H2SO3	Acido solforoso	Acido ossosolforoso		
	NH4OH	Ammoniaca liquida	Idrossido di ammonio		
	FeCl3	Cloruro ferrico	Cloruro di ferro (III)		
	NaNO3	Nitrato di sodio	Nitrato di sodio		
	BaCl2	Cloruro di bario	Cloruro di bario		
	Na2S	Solfuro di sodio	Solfuro di sodio		
	H3PO4	Acido fosforico	Acido ossofosforico		
	H2CO3	Acido carbonico	Acido ossocarbonico		
	NaHCO3	Bicarbonato di sodio	Idrogenocarbonato di sodio		
	K2CO3	Carbonato di potassio	Carbonato di potassio		
	Pb(NO3)2	Nitrato di piombo (II)	Nitrato di piombo (II)		
	HBr	Acido bromidrico	Bromuro di idrogeno		
	NaF	Fluoruro di sodio	Fluoruro di sodio		
	NaClO	Iperclorito di sodio	Iperclorito di sodio		
	FeS	Solfuro ferroso	Solfuro di ferro (II)		
	NaHSO4	Solfato idrogenato di sodio	Solfato di idrogeno di sodio		
	Al(OH)3	Idrossido di alluminio	Idrossido di alluminio (III)		
	Na2S2O3	Tiosolfato di sodio	Tiosolfato di sodio		
	KClO3	Clorato di potassio	Clorato di potassio		
	ZnSO4	Solfato di zinco	Solfato di zinco		
	Fe(NO3)3	Nitrato ferrico	Nitrato di ferro (III)		
	H2Se	Seleniuro di idrogeno	Solfo idruro di idrogeno (II)		
	Na2CO2	Sesquicarbonato di sodio	Carbonato di sodio (II)		
	MgO	Ossido di magnesio	Ossido di magnesio		
	Ca(OH)2	Calce spenta	Idrossido di calcio		
	K2SO4	Solfato di potassio	Solfato di potassio		
	HgO	Ossido di mercurio (II)	Ossido di mercurio (II)		
	NaH2PO4	Fosfato acido di sodio	Fosfato di idrogeno di sodio		
	Na2CrO4	Cromato di sodio	Cromato di sodio		
	Na2O2	Perossido di sodio	Idrogeno perossido di sodio		
	HgCl2	Cloruro di mercurio (II)	Cloruro di mercurio (II)		
	BaSO4	Solfato di bario	Solfato di bario		
	Na2SO3	Solfito di sodio	Solfito di sodio		
	ZnCl2	Cloruro di zinco	Cloruro di zinco		
	Fe(OH)3	Idrossido ferrico	Idrossido di ferro (III)		
	Na2Cr2O7	Dicromato di sodio	Dicromato di sodio		
	CaSO4	Gesso	Solfato di calcio		
	K2S	Solfuro di potassio	Solfuro di potassio		
	H2Te	Teluriuro di idrogeno	Solfo idruro di idrogeno (II)		
	Na3PO4	Fosfato trisodico	Fosfato di sodio		
	Mg(NO3)2	Nitrato di magnesio	Nitrato di magnesio		
	Ca(NO3)2	Nitrato di calcio	Nitrato di calcio		
	KNO3	Nitrato di potassio	Nitrato di potassio		
	MgSO4	Solfato di magnesio	Solfato di magnesio		
	FeCl2	Cloruro ferroso	Cloruro di ferro (II)		
	Na2HPO4	Fosfato disodico	Fosfato di idrogeno di sodio		
	Al2(SO4)3	Solfato di alluminio	Solfato di alluminio		
	NH4Cl	Cloruro ammonico	Cloruro di ammonio		
	NaClO3	Clorato di sodio	Clorato di sodio		
	K2Cr2O7	Dicromato di potassio	Dicromato di potassio		
	CuCl2	Cloruro di rame (II)	Cloruro di rame (II)		
	NaHCO2	Idrogenocarbonato di sodio	Carbonato di sodio (II)		
	Ca3(PO4)2	Fosfato tricalcico	Fosfato di calcio (II)		
	KMnO4	Permanganato di potassio	Permanganato di potassio		
	ZnO	Ossido di zinco	Ossido di zinco		
	H2S2	Solfo idruro di idrogeno	Solfo idruro di idrogeno (II)		
	Na2SO5	Ipersolfito di sodio	Ipersolfito di sodio		
	AlPO4	Fosfato di alluminio	Fosfato di alluminio		
	NaH2PO3	Fosfato di sodio	Fosfato di idrogeno di sodio		
	FeS2	Pirite	Solfuro di ferro (II)		
	NH4NO3	Nitrato ammonico	Nitrato di ammonio		
	K2S2O3	Tiosolfato di potassio	Tiosolfato di potassio		
	Ca(OCl)2	Iperclorito di calcio	Iperclorito di calcio		
	HClO4	Acido clorico	Acido ossoclorico		
	Na2SiO3	Silicato di sodio	Silicato di sodio		
	Ba(NO3)2	Nitrato di bario	Nitrato di bario		
	Mg(HCO3)2	Idrogenocarbonato di magnesio	Carbonato di magnesio (II)		
	NaBr	Bromuro di sodio	Bromuro di sodio		
	KHSO4	Solfato acido di potassio	Solfato di idrogeno di potassio		
	Zn(OH)2	Idrossido di zinco	Idrossido di zinco		
	FePO4	Fosfato ferrico	Fosfato di ferro (III)		
	NaHS	Solfito di sodio	Solfito di sodio		
	Cu(NO3)2	Nitrato di rame (II)	Nitrato di rame (II)		
	NaHSO3	Solfato idrogenato di sodio	Solfato di idrogeno di sodio		
	AlCl3	Cloruro di alluminio	Cloruro di alluminio		
	Na2B4O7	Borato di sodio	Tetraborato di disodio		
	KBr	Bromuro di potassio	Bromuro di potassio		
	H3BO3	Acido borico	Acido ossoborico		
	KHS	Solfito di potassio	Solfito di potassio		
	NaH2AsO4	Arseniato acido di sodio	Arseniato di idrogeno di sodio		
	Ca(H2PO4)2	Difosfato di calcio	Fosfato di idrogeno di calcio		
	H2CrO4	Acido cromico	Acido ossocromico		
	Na2C2O4	Ossalato di sodio	Ossalato di sodio		
	K2HPO4	Fosfato di potassio	Fosfato di idrogeno di potassio		
	Ca3(PO3)2	Fosfito tricalcico	Fosfito di calcio (II)		
	H3AsO4	Acido arsenico	Acido ossoarsenico		
	Na2SO2	Solfuro di sodio	Solfuro di sodio		
	K2S2O4	Iposolfito di potassio	Iposolfito di potassio		
	Mg(HSO4)2	Solfato acido di magnesio	Solfato di idrogeno di magnesio		
	NaH2PO2	Fosfato di sodio	Fosfato di idrogeno di sodio		
	Ca(HCO3)2	Idrogenocarbonato di calcio	Carbonato di calcio (II)		
	HNO2	Acido nitroso	Acido ossonitroso		
	NaBH4	Boroidruro di sodio	Idruro di sodio		
	KHSO3	Solfato idrogenato di potassio	Solfato di idrogeno di potassio		
	NaH2PO4	Fosfato di sodio	Fosfato di idrogeno di sodio		
	H3PO3	Acido fosforoso	Acido ossofosforoso		
	K2SiO3	Silicato di potassio	Silicato di potassio		
	Ca3(PO4)2	Fosfato tricalcico	Fosfato di calcio (II)		
	NH4HSO4	Solfato acido di ammonio	Solfato di idrogeno di ammonio		
	Al(OH)3	Idrossido di alluminio	Idrossido di alluminio (III)		
	Na2S2O3	Tiosolfato di sodio	Tiosolfato di sodio		
	KClO3	Clorato di potassio	Clorato di potassio		
	ZnSO4	Solfato di zinco	Solfato di zinco		
	Fe(NO3)3	Nitrato ferrico	Nitrato di ferro (III)		
	H2Se	Seleniuro di idrogeno	Solfo idruro di idrogeno (II)		
	Na2CO2	Sesquicarbonato di sodio	Carbonato di sodio (II)		
	MgO	Ossido di magnesio	Ossido di magnesio		
	Ca(OH)2	Calce spenta	Idrossido di calcio		
	K2SO4	Solfato di potassio	Solfato di potassio		
	HgO	Ossido di mercurio (II)	Ossido di mercurio (II)		
	NaH2PO4	Fosfato acido di sodio	Fosfato di idrogeno di sodio		
	Na2CrO4	Cromato di sodio	Cromato di sodio		
	Na2O2	Perossido di sodio	Idrogeno perossido di sodio		
	HgCl2	Cloruro di mercurio (II)	Cloruro di mercurio (II)		
	BaSO4	Solfato di bario	Solfato di bario		
	Na2SO3	Solfito di sodio	Solfito di sodio		
	ZnCl2	Cloruro di zinco	Cloruro di zinco		
	Fe(OH)3	Idrossido ferrico	Idrossido di ferro (III)		
	Na2Cr2O7	Dicromato di sodio	Dicromato di sodio		
	CaSO4	Gesso	Solfato di calcio		
	K2S	Solfuro di potassio	Solfuro di potassio		
	H2Te	Teluriuro di idrogeno	Solfo idruro di idrogeno (II)		
	Na3PO4	Fosfato trisodico	Fosfato di sodio		
	Mg(NO3)2	Nitrato di magnesio	Nitrato di magnesio		
	Ca(NO3)2	Nitrato di calcio	Nitrato di calcio		
	KNO3	Nitrato di potassio	Nitrato di potassio		
	MgSO4	Solfato di magnesio	Solfato di magnesio		
	FeCl2	Cloruro ferroso	Cloruro di ferro (II)		
	Na2HPO4	Fosfato disodico	Fosfato di idrogeno di sodio		
	Al2(SO4)3	Solfato di alluminio	Solfato di alluminio		
	NH4Cl	Cloruro ammonico	Cloruro di ammonio		
	NaClO3	Clorato di sodio	Clorato di sodio		
	K2Cr2O7	Dicromato di potassio	Dicromato di potassio		
	CuCl2	Cloruro di rame (II)	Cloruro di rame (II)		
	NaHCO2	Idrogenocarbonato di sodio	Carbonato di sodio (II)		
	Ca3(PO4)2	Fosfato tricalcico	Fosfato di calcio (II)		
	KMnO4	Permanganato di potassio	Permanganato di potassio		
	ZnO	Ossido di zinco	Ossido di zinco		
	H2S2	Solfo idruro di idrogeno	Solfo idruro di idrogeno (II)		
	Na2SO5	Ipersolfito di sodio	Ipersolfito di sodio		
	AlPO4	Fosfato di alluminio	Fosfato di alluminio		
	NaH2PO3	Fosfato di sodio	Fosfato di idrogeno di sodio		
	FeS2	Pirite	Solfuro di ferro (II)		
	NH4NO3	Nitrato ammonico	Nitrato di ammonio		
	K2S2O3	Tiosolfato di potassio	Tiosolfato di potassio		
	Ca(OCl)2	Iperclorito di calcio	Iperclorito di calcio		
	HClO4	Acido clorico	Acido ossoclorico		
	Na2SiO3	Silicato di sodio	Silicato di sodio		
	Ba(NO3)2	Nitrato di bario	Nitrato di bario		
	Mg(HCO3)2	Idrogenocarbonato di magnesio	Carbonato di magnesio (II)		
	NaBr	Bromuro di sodio	Bromuro di sodio		
	KHSO4	Solfato acido di potassio	Solfato di idrogeno di potassio		
	Zn(OH)2	Idrossido di zinco	Idrossido di zinco		
	FePO4	Fosfato ferrico	Fosfato di ferro (III)		
	NaHS	Solfito di sodio	Solfito di sodio		
	Cu(NO3)2	Nitrato di rame (II)	Nitrato di rame (II)		
	NaHSO3	Solfato idrogenato di sodio	Solfato di idrogeno di sodio		
	AlCl3	Cloruro di alluminio	Cloruro di alluminio		
	Na2B4O7	Borato di sodio	Tetraborato di disodio		
	KBr	Bromuro di potassio	Bromuro di potassio		
	H3BO3	Acido borico	Acido ossoborico		
	KHS	Solfito di potassio	Solfito di potassio		
	NaH2AsO4	Arseniato acido di sodio	Arseniato di idrogeno di sodio		
	Ca(H2PO4)2	Difosfato di calcio	Fosfato di idrogeno di calcio		
	H2CrO4	Acido cromico	Acido ossocromico		
	Na2C2O4	Ossalato di sodio	Ossalato di sodio		
	K2HPO4	Fosfato di potassio	Fosfato di idrogeno di potassio		
	Ca3(PO3)2	Fosfito tricalcico	Fosfito di calcio (II)		
	H3AsO4	Acido arsenico	Acido ossoarsenico		
	Na2SO2	Solfuro di sodio	Solfuro di sodio		
	K2S2O4	Iposolfito di potassio	Iposolfito di potassio		
	Mg(HSO4)2	Solfato acido di magnesio	Solfato di idrogeno di magnesio		
	NaH2PO2	Fosfato di sodio	Fosfato di idrogeno di sodio		
	Ca(HCO3)2	Idrogenocarbonato di calcio	Carbonato di calcio (II)		
	HNO2	Acido nitroso	Acido ossonitroso		
	NaBH4	Boroidruro di sodio	Idruro di sodio		
	KHSO3	Solfato idrogenato di potassio	Solfato di idrogeno di potassio		
	NaH2PO4	Fosfato di sodio	Fosfato di idrogeno di sodio		
	H3PO3	Acido fosforoso	Acido ossofosforoso		
	K2SiO3	Silicato di potassio	Silicato di potassio		
1	Li2O	Ossido di litio	Ossido di dilitio		
1	Na2O	Ossido di sodio	Ossido di disodio		
2	MgO	Ossido di magnesio	Ossido di magnesio		
2	CaO	Ossido di calcio	Ossido di calcio		
2	CrO	Ossido cromoso	Ossido di cromo		
3	Cr2O3	Ossido cromico	Triossido di dicromo		
2	MnO	Ossido manganoso	Ossido di manganese		
3	Mn2O3	Ossido manganico	Triossido di dimanganese		
2	SnO	Ossido stannoso	Monossido di stagno		
3	Tl2O3	Ossido di tallio	Triossido di ditallio		
3	B2O3	Anidride borica	Triossido di diboro		
2	CO	Ossido di carbonio	Monossido di carbonio		
4	CO2	Anidride carbonica	Diossido di carbonio		
1	N2O	Protossido di azoto	Ossido di diazoto		
2	NO	Ossido di azoto	Monossido di azoto		
3	N2O3	Anidride nitrosa	Triossido di diazoto		
4	NO2	Anidride nitroso	Diossido di azoto		
5	N2O5	Anidride nitrica	Pentaossido di diazoto		
3	P2O3	Anidride fosforosa	Triossido di di fosforo		
5	P2O5	Anidride fosforica	Pentossido di di fosforo		
4	SO2	Anidride solforosa	Diossido di zolfo		
6	SO3	Anidride solforica	Triossido di zolfo		
1	Cl2O	Anidride ipoclorosa	Ossido di dicloro		
3	Cl2O3	Anidride clorosa	Triossido di dicloro		
5	Cl2O5	Anidride clorica	Pentaossido di dicloro		
7	Cl2O7	Anidride perclorica	Eptaossido di dicloro		
6	CrO3	Anidride cromica	Triossido di cromo		
7	Mn2O7	Anidride permanganica	Eptaossido di dimanganese		
2	ZnO	Ossido di zinco	Ossido di zinco		
4	SnO2	Ossido stannico	Diossido di stagno		
3	Al2O3	Allumina	Triossido di dialluminio		
3	Cr2O3	Ossido cromico	Triossido di dicromo		
3	Mn2O3	Ossido manganico	Triossido di dimanganese		
-1	Cl-	Ione cloruro	Cloruro		
1	Na+	Ione sodio	Sodio		
2	Sn2+	Ione stannoso	Stagno (II)		
2	Fe2+	Ione ferroso	Ferro (II)		
3	Fe3+	Ione ferrico	Ferro (III)		
3	Al3+	Ione alluminio	Alluminio		
4	Sn4+	Ione stannico	Stagno (IV)		
-3	N3-	Ione azoturo	Nitruro		
-2	S2-	Ione solfuro	Solfuro		
2	Sn(SO4)2	Solfato stannico	Ditetraossosolfato di stagno		
-1	OH-	Ione idrossido	Idrossido		
-1	CO3^2-	Ione carbonato	Carbonato		
-1	HCO3^-	Ione bicarbonato	Bicarbonato		
-2	SO4^2-	Ione solfato	Solfato		
-2	HSO4^-	Ione idrogenosolfato	Idrogenosolfato		
-1	ClO^-	Ione ipoclorito	Ipoclorito		
-1	ClO2^-	Ione clorito	Clorito		
-1	ClO3^-	Ione clorato	Clorato		
-1	ClO4^-	Ione perclorato	Perclorato		
-1	NO2^-	Ione nitrito	Nitrito		
-1	NO3^-	Ione nitrato	Nitrato		
-1	PO3^3-	Ione fosfito	Fosfito		
-1	PO4^3-	Ione fosfato	Fosfato		
-1	HPO4^2-	Ione idrogenofosfato	Idrogenofosfato		
-1	H2PO4^-	Ione diidrogenofosfato	Dihidrogenofosfato		
-1	BO2^-	Ione metaborato	Metaborato		
-1	BO3^-	Ione ortoborato	Orto-borato		
-1	H2BO3^-	Ione diidrogenometaborato	Acido metaborico		
-1	H3BO3	Ione triborato	Acido borico		
-2	SiO3^2-	Ione meta-silicato	Meta-silicato		
-2	SiO4^4-	Ione orto-silicato	Orto-silicato		
-2	H2SiO3^-	Ione diidrogenometasilicato	Meta-silicato acido		
-2	H4SiO4	Ione tetra-silicato	Acido ortosilicico		
-2	OH-	Ione idrato	Idrato		
-2	H2O2	Ione perossido	Perossido		
-3	OH-	Ione idrossido	Idrossido		
-3	H3O+	Ione idronio	Ione idronio"
    """

    lines = file_content.split('\n')

    matching_lines = []
    for line in lines:
        if term.lower() in line.lower():
            matching_lines.append(line.strip())
    
    return matching_lines if matching_lines else ["No results"]

# Loop
while True:
    search_term = input("Input ricerca: ")
    
    if search_term.lower() == "e":
        break
    
    result = search_in_file(search_term)
    for line in result:
        print(line)
