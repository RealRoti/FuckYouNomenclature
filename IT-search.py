def search_in_file(term):
    file_content = """
    "FeCl2    Dicloruro di ferro    Cloruro ferroso
    FeCl3    Tricloruro di ferro    Cloruro ferrico
    CO    Ossido di carbonio    Ossido di carbonio
    CO2    Diossido di carbonio    Anidride carbonica
    P2O3    Triossido di di fosforo    Anidride fosforosa
    P2O5    Pentossido di di fosforo    Anidride fosforica
    N2O    ossido di di azoto    Protossido di azoto
    NO    Ossido di azoto    Ossido di azoto
    N2O3    Triossido di di azoto    Anidride nitrosa
    NO2    Diossido di azoto    Ipoazotide
    N2O5    Pentossido di di azoto    Anidride nitrica
    HCl    Cloruro di idrogeno    Acido cloridrico
    Hg2Cl2    Dicloruro di di mercurio    Calomelano
    H2S    Solfuro di di idrogeno    Acido solfidrico
    H2O    Ossido di idrogeno    Acqua
    H2O2    Perossido di idrogeno    Acqua ossigenata
    PH3    Triidruro di fosforo    Fosfina
    MoO4    Tetrossido di molibdeno    Tetrossido di molibdeno
    OF2    Fluoruro di idrogeno    Fluoruro di idrogeno
    +1    Li2O    Ossido di dilitio    Ossido di litio
    +1    Na2O    Ossido di disodio    Ossido di sodio
    +2    MgO    Ossido di magnesio    Ossido di magnesio
    +2    CaO    Ossido di calcio    Ossido di calcio
    +2    CrO    Ossido di cromo    Ossido cromoso
    +3    Cr2O3    Triossido di dicromo    Ossido cromico
    +2    MnO    Ossido di manganese    Ossido manganoso
    +3    Mn2O3    Triossido di dimanganese    Ossido manganico
    +2    SnO    Monossido di stagno    Ossido stannoso
    +3    Tl2O3    Triossido di ditallio    Ossido di tallio 
    +3    B2O3    triossido di diboro    Anidride borica
    +2    CO    Monossido di carbonio    Ossido di carbonio
    +4    CO2    Diossido di carbonio    Anidride carbonica
    +1    N2O    Ossido di diazoto    Protossido di azoto
    +2    NO    Monossido di azoto    Ossido di azoto
    +3    N2O3    Triossido di diazoto    Anidride nitrosa
    +4    NO2    Diossido di azoto    Anidride nitroso/nitrica
    +4    N2O4    Tetraossido di diazoto    Ipoazotide
    +5    N2O5    Pentaossido di diazoto    Anidride nitrica
    +3    P4O6    Esaossido di tetrafosforo    Anidride fosforosa
    +5    P4O10    Decaossido di tetrafosforo    Anidride fosforica
    +4    SO2    Diossido di zolfo    Anidride solforosa
    +6    SO3    Triossido di zolfo    Anidride solforica
    +1    Cl2O    Ossido di dicloro    Anidride ipoclorosa
    +3    Cl2O3    Triossido di dicloro    Anidride clorosa
    +5    Cl2O5    Pentaossido di dicloro    Anidride clorica
    +7    Cl2O7    Eptaossido di dicloro    Anidride perclorica
    +6    CrO3    Triossido di cromo    Anidride cromica
    +7    Mn2O7    Eptaossido di dimanganese    Anidride permanganica 
    +2    ZnO    Ossido di zinco    Ossido di zinco
    +4    SnO2    Diossido di stagno    Ossido stannico
    +3    Al2O3    Triossido di dialluminio    Allumina
    +3    Cr2O3    Triossido di dicromo    Ossido cromico
    +3    Mn2O3    Triossido di dimanganese    Ossido manganico
    HF    Fluoruro di idrogeno    Acido fluoridrico
    HCl    Cloruro di idrogeno    Acido cloridrico
    HBr    Bromuro di idrogeno    Acido bromidrico
    HI    Ioduro di idrogeno    Acido iodidrico
    H2S    Solfuro di diidrogeno    Acido solfidrico
    H2Se    Seleniuro di diidrogeno    Acido selenidrico
    HCN    Cianuro di idrogeno    Acido cianidrico 
    +3    B2O3    H3BO3    Acido triossoborico    Acido ortoborico    BO33- ortoborato
    +3    B2O3    HBO2    Acido diossoborico    Acido metaborico    BO2- metaborato
    +4    CO2    H2CO3    Acido triossocarbonico    Acido carbonico    CO32- carbonato
    +4    SiO2    H4SiO4    Acido tetraossosilicico    Acido ortosilicico    SiO44- ortosilicato
    +3    N2O3    HNO2    Acido diossonitrico    Acido nitroso    NO2- nitrito
    +5    N2O5    HNO3    Acido triossonitrico    Acido nitrico    NO3- nitrato
    +5    P2O5    H3PO4    Acido tetraossofosforico    Acido ortofosforico    PO43- ortofosfato
    +5    P2O5    H4P2O7    Acido eptaossodifosforico    Acido pirofosforico    H2P2O72- pirofosfato diacido
    +5    P2O5    HPO3    Acido triossofosforico    Acido metafosforico    PO3- metafosfato
    +4    SO2    H2SO3    Acido triossosolforico    Acido solforoso    SO32- solfito
    +6    SO3    H2SO4    Acido tetraossosolforico    Acido solforico    SO42- solfato
    +1    Cl2O    HClO    Acido monossoclorico    Acido ipocloroso    ClO- ipoclorito
    +3    Cl2O3    HClO2    Acido diossoclorico    Acido cloroso    ClO2- clorito
    +5    Cl2O5    HClO3    Acido triossoclorico    Acido clorico    ClO3- clorato
    +7    Cl2O7    HClO4    Acido tetraossoclorico    Acido perclorico    ClO4- perclorato
    HCl acido cloridrico    CaCl2    Dicloruro di calcio    Cloruro di calcio
    HNO2 acido nitroso    Al(NO2)3    Triossidonitrato di alluminio    Nitrito di alluminio
    H2SO4 acido solforico    Sn(SO4)2    Ditetraossosolfato di stagno    Solfato stannico
    H3PO4 acido fosforico    Sn3(PO4)2    Ditetraossofosfato di stagno    Ortosolfato stannoso
    HClO acido ipocloroso    NaClO    Monossoclorato di sodio    Ipoclorito sodico
    HClO2 acido cloroso    LiClO2    Diossoclorato di litio    Clorito di litio
    HClO3 acido clorico    NaClO3    Triossoclorato di sodio    Clorato di sodio
    HNO3 acido nitrico    Pb(NO3)2    Ditriossonitrato di piombo    Nitrato piomboso
    H2SO3 acido solforoso    Cu2SO3    Triossosolfato di rame    Solfito rameoso
    HClO4 acido perclorico    Ba(ClO4)2    Ditetraossoclorato di bario    Perclorato di bario
    H2CO3 acido carbonico    Fe2(CO3)3    Tritriossocarbonato di ferro    Carbonato ferrico
    H2S acido solfidrico    ZnS    Solfuro di zinco    Solfuro di zinco
    NaHCO3    Idrogenocarbonato di sodio    Bicarbonato di sodio
    KHSO3    Idrogenosolfito di potassio    Bisolfito di potassio
    KHSO4    Idrogenosolfato di potassio    Bisolfato di potassio
    Na2PO3    Idrogenofosfito di sodio    Fosfito monosodico
    Na2PO4    Diidrogenofosfato di sodio    Fosfato diacido di sodio
    K2HPO4    Idrogenofosfato di potassio    Fosfato monoacido di potassio 
    MgF(OH)    Idrossofluoruro di magnesio    Fluoruro monobasico di magnesio
    FeCl(OH)2    Diidrossocloruro di ferro    Cloruro dibasico di ferro 
    -3    N3-    Nitruro    Ione azoturo
    -2    S2-    Solfuro    Ione solfuro
    -1    Cl-    Cloruro    Ione cloruro
    +1    Na+    Sodio    Ione sodio
    +2    Sn2+    Stagno (II)    Ione stannoso
    +2    Fe2+    Ferro (II)    Ione ferroso
    +3    Fe3+    Ferro (III)    Ione ferrico
    +3    Al3+    Alluminio    Ione alluminio
    +4    Sn4+    Stagno (IV)    Ione stannico "
    """

    # Dividi il contenuto del file in righe
    lines = file_content.split('\n')

    matching_lines = []
    for line in lines:
        if term.lower() in line.lower():
            matching_lines.append(line.strip())
    
    if matching_lines:
        return matching_lines
    else:
        return ["No results"]

# Esempio di utilizzo
search_term = input("Inserisci il termine da cercare nel file: ")

result = search_in_file(search_term)
for line in result:
    print(line)