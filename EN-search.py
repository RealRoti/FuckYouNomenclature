def search_in_file(term):
    file_content = """
    "FeCl2    Iron(II) chloride    Ferrous chloride
    FeCl3    Iron(III) chloride    Ferric chloride
    CO    Carbon monoxide    Carbon monoxide
    CO2    Carbon dioxide    Carbon dioxide
    P2O3    Phosphorus trioxide    Phosphorous anhydride
    P2O5    Phosphorus pentoxide    Phosphoric anhydride
    N2O    Nitrous oxide    Nitrous oxide
    NO    Nitric oxide    Nitric oxide
    N2O3    Dinitrogen trioxide    Nitrous anhydride
    NO2    Nitrogen dioxide    Nitrogen dioxide
    N2O5    Dinitrogen pentoxide    Nitric anhydride
    HCl    Hydrogen chloride    Hydrochloric acid
    Hg2Cl2    Mercury(I) chloride    Calomel
    H2S    Hydrogen sulfide    Hydrogen sulfide
    H2O    Water    Water
    H2O2    Hydrogen peroxide    Hydrogen peroxide
    PH3    Phosphine    Phosphine
    MoO4    Molybdate    Molybdate
    OF2    Oxygen difluoride    Oxygen difluoride
    +1    Li2O    Lithium oxide    Lithium oxide
    +1    Na2O    Sodium oxide    Sodium oxide
    +2    MgO    Magnesium oxide    Magnesium oxide
    +2    CaO    Calcium oxide    Calcium oxide
    +2    CrO    Chromium(II) oxide    Chromous oxide
    +3    Cr2O3    Chromium(III) oxide    Chromic oxide
    +2    MnO    Manganese(II) oxide    Manganous oxide
    +3    Mn2O3    Manganese(III) oxide    Manganic oxide
    +2    SnO    Tin(II) oxide    Stannous oxide
    +3    Tl2O3    Thallium(III) oxide    Thallium(I) oxide
    +3    B2O3    Boron trioxide    Boric anhydride
    +2    CO    Carbon monoxide    Carbon monoxide
    +4    CO2    Carbon dioxide    Carbon dioxide
    +1    N2O    Nitrous oxide    Nitrous oxide
    +2    NO    Nitric oxide    Nitric oxide
    +3    N2O3    Dinitrogen trioxide    Nitrous anhydride
    +4    NO2    Nitrogen dioxide    Nitrous anhydride
    +4    N2O4    Dinitrogen tetroxide    Ipoazotide
    +5    N2O5    Dinitrogen pentoxide    Nitric anhydride
    +3    P4O6    Phosphorus trioxide    Phosphorous anhydride
    +5    P4O10    Phosphorus pentoxide    Phosphoric anhydride
    +4    SO2    Sulfur dioxide    Sulfurous anhydride
    +6    SO3    Sulfur trioxide    Sulfuric anhydride
    +1    Cl2O    Dichlorine monoxide    Hypochlorous anhydride
    +3    Cl2O3    Dichlorine trioxide    Chlorous anhydride
    +5    Cl2O5    Dichlorine pentoxide    Chloric anhydride
    +7    Cl2O7    Dichlorine heptoxide    Perchloric anhydride
    +6    CrO3    Chromium trioxide    Chromic anhydride
    +7    Mn2O7    Manganese(VII) oxide    Permanganic anhydride
    +2    ZnO    Zinc oxide    Zinc oxide
    +4    SnO2    Tin(IV) oxide    Stannic oxide
    +3    Al2O3    Aluminium oxide    Alumina
    +3    Cr2O3    Chromium(III) oxide    Chromic oxide
    +3    Mn2O3    Manganese(III) oxide    Manganic oxide
    HF    Hydrofluoric acid    Hydrofluoric acid
    HCl    Hydrochloric acid    Hydrochloric acid
    HBr    Hydrobromic acid    Hydrobromic acid
    HI    Hydroiodic acid    Hydroiodic acid
    H2S    Hydrogen sulfide    Hydrogen sulfide
    H2Se    Hydrogen selenide    Hydroselenic acid
    HCN    Hydrogen cyanide    Hydrocyanic acid 
    +3    B2O3    H3BO3    Boric acid    Boric acid    Borate
    +3    B2O3    HBO2    Metaboric acid    Metaboric acid    Metaborate
    +4    CO2    H2CO3    Carbonic acid    Carbonic acid    Carbonate
    +4    SiO2    H4SiO4    Orthosilicic acid    Orthosilicic acid    Orthosilicate
    +3    N2O3    HNO2    Nitrous acid    Nitrous acid    Nitrite
    +5    N2O5    HNO3    Nitric acid    Nitric acid    Nitrate
    +5    P2O5    H3PO4    Phosphoric acid    Phosphoric acid    Phosphate
    +5    P2O5    H4P2O7    Pyrophosphoric acid    Pyrophosphoric acid    Pyrophosphate
    +5    P2O5    HPO3    Metaphosphoric acid    Metaphosphoric acid    Metaphosphate
    +4    SO2    H2SO3    Sulfurous acid    Sulfurous acid    Sulfite
    +6    SO3    H2SO4    Sulfuric acid    Sulfuric acid    Sulfate
    +1    Cl2O    HClO    Hypochlorous acid    Hypochlorous acid    Hypochlorite
    +3    Cl2O3    HClO2    Chlorous acid    Chlorous acid    Chlorite
    +5    Cl2O5    HClO3    Chloric acid    Chloric acid    Chlorate
    +7    Cl2O7    HClO4    Perchloric acid    Perchloric acid    Perchlorate
    HCl    Hydrochloric acid    Hydrochloric acid    Hydrochloric acid
    HNO2    Nitrous acid    Nitrous acid    Nitrite
    H2SO4    Sulfuric acid    Sulfuric acid    Sulfate
    H3PO4    Phosphoric acid    Phosphoric acid    Phosphate
    HClO    Hypochlorous acid    Hypochlorous acid    Hypochlorite
    HClO2    Chlorous acid    Chlorous acid    Chlorite
    HClO3    Chloric acid    Chloric acid    Chlorate
    HNO3    Nitric acid    Nitric acid    Nitrate
    H2SO3    Sulfurous acid    Sulfurous acid    Sulfite
    HClO4    Perchloric acid    Perchloric acid    Perchlorate
    H2CO3    Carbonic acid    Carbonic acid    Carbonate
    H2S    Hydrogen sulfide    Hydrogen sulfide    Hydrogen sulfide
    NaHCO3    Sodium bicarbonate    Sodium bicarbonate
    KHSO3    Potassium bisulfite    Potassium bisulfite
    KHSO4    Potassium bisulfate    Potassium bisulfate
    Na2PO3    Sodium phosphite    Sodium phosphite
    Na2PO4    Sodium dihydrogen phosphate    Sodium dihydrogen phosphate
    K2HPO4    Dipotassium phosphate    Dipotassium phosphate 
    MgF(OH)    Magnesium hydroxide fluoride    Magnesium monobasic fluoride
    FeCl(OH)2    Iron(II) hydroxide chloride    Iron dibasic chloride 
    -3    N3-    Nitride    Azide ion
    -2    S2-    Sulfide    Sulfide ion
    -1    Cl-    Chloride    Chloride ion
    +1    Na+    Sodium    Sodium ion
    +2    Sn2+    Tin(II)    Stannous ion
    +2    Fe2+    Iron(II)    Ferrous ion
    +3    Fe3+    Iron(III)    Ferric ion
    +3    Al3+    Aluminium    Aluminium ion
    +4    Sn4+    Tin(IV)    Stannic ion"
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
    
    result = search_in_file(search_term)
    for line in result:
        print(line)
