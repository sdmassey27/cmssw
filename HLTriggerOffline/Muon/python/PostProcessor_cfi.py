import FWCore.ParameterSet.Config as cms

postProcessor = cms.EDFilter("PostProcessor",
    subDir         = cms.untracked.string('HLT/Muon/Distributions/*'),
    outputFileName = cms.untracked.string('PostProcessor.root'),
    commands       = cms.vstring(),
    resolution     = cms.vstring(),                                    
    efficiency     = cms.vstring(
        "genTurnOn_L1Filtered 'L1 Turn On, label=L1Filtered;Highest Generated Muon p_{T} (GeV);L1 Pass / Gen (%)' genPassMaxPt_L1Filtered genPassMaxPt_All",
        "genEffEta_L1Filtered 'L1 #eta Efficiency label=L1Filtered;Generated Muon #eta;L1 Pass / Gen (%)' genPassEta_L1Filtered genPassEta_All",
        "genEffPhi_L1Filtered 'L1 #phi Efficiency label=L1Filtered;Generated Muon #phi;L1 Pass / Gen (%)' genPassPhi_L1Filtered genPassPhi_All", 
        "genEffPt_L1Filtered 'L1 pt Efficiency label=L1Filtered;Generated Muon pt (GeV);L1 Pass / Gen (%)' genPassPt_L1Filtered genPassPt_All", 
        "genTurnOn_L2Filtered 'Turn On label=L2Filtered;Highest Generated Muon p_{T} (GeV);L2 Pass / L1 Pass (%)' genPassMaxPt_L2Filtered genPassMaxPt_L1Filtered", 
        "genEffEta_L2Filtered '#eta Efficiency label=L2Filtered;Generated Muon #eta;L2 Pass / L1 Pass (%)' genPassEta_L2Filtered genPassEta_L1Filtered", 
        "genEffPhi_L2Filtered '#phi Efficiency label=L2Filtered;Generated Muon #phi;L2 Pass / L1 Pass (%)' genPassPhi_L2Filtered genPassPhi_L1Filtered", 
        "genEffPt_L2Filtered 'pt Efficiency label=L2Filtered;Generated Muon pt (GeV);L2 Pass / L1 Pass (%)' genPassPt_L2Filtered genPassPt_L1Filtered",
        "genTurnOn_L2PreFiltered 'Turn On label=L2PreFiltered;Highest Generated Muon p_{T} (GeV);L2 Pass / L1 Pass (%)' genPassMaxPt_L2PreFiltered genPassMaxPt_L1Filtered", 
        "genEffEta_L2PreFiltered '#eta Efficiency label=L2PreFiltered;Generated Muon #eta;L2 Pass / L1 Pass (%)' genPassEta_L2PreFiltered genPassEta_L1Filtered", 
        "genEffPhi_L2PreFiltered '#phi Efficiency label=L2PreFiltered;Generated Muon #phi;L2 Pass / L1 Pass (%)' genPassPhi_L2PreFiltered genPassPhi_L1Filtered", 
        "genEffPt_L2PreFiltered 'pt Efficiency label=L2PreFiltered;Generated Muon pt (GeV);L2 Pass / L1 Pass (%)' genPassPt_L2PreFiltered genPassPt_L1Filtered",
        "genTurnOn_L2IsoFiltered 'Turn On label=L2IsoFiltered;Highest Generated Muon p_{T} (GeV);L2 Pass / L1 Pass (%)' genPassMaxPt_L2IsoFiltered genPassMaxPt_L1Filtered", 
        "genEffEta_L2IsoFiltered '#eta Efficiency label=L2IsoFiltered;Generated Muon #eta;L2 Pass / L1 Pass (%)' genPassEta_L2IsoFiltered genPassEta_L1Filtered", 
        "genEffPhi_L2IsoFiltered '#phi Efficiency label=L2IsoFiltered;Generated Muon #phi;L2 Pass / L1 Pass (%)' genPassPhi_L2IsoFiltered genPassPhi_L1Filtered", 
        "genEffPt_L2IsoFiltered 'pt Efficiency label=L2IsoFiltered;Generated Muon pt (GeV);L2 Pass / L1 Pass (%)' genPassPt_L2IsoFiltered genPassPt_L1Filtered",
        "genTurnOn_L3Filtered 'Turn On label=L3Filtered;Highest Generated Muon p_{T} (GeV);L3 Pass / L1 Pass (%)' genPassMaxPt_L3Filtered genPassMaxPt_L1Filtered", 
        "genEffEta_L3Filtered '#eta Efficiency label=L3Filtered;Generated Muon #eta;L3 Pass / L1 Pass (%)' genPassEta_L3Filtered genPassEta_L1Filtered", 
        "genEffPhi_L3Filtered '#phi Efficiency label=L3Filtered;Generated Muon #phi;L3 Pass / L1 Pass (%)' genPassPhi_L3Filtered genPassPhi_L1Filtered", 
        "genEffPt_L3Filtered 'pt Efficiency label=L3Filtered;Generated Muon pt (GeV);L2 Pass / L1 Pass (%)' genPassPt_L3Filtered genPassPt_L1Filtered",
        "genTurnOn_L3PreFiltered 'Turn On label=L3PreFiltered;Highest Generated Muon p_{T} (GeV);L3 Pass / L1 Pass (%)' genPassMaxPt_L3PreFiltered genPassMaxPt_L1Filtered", 
        "genEffEta_L3PreFiltered '#eta Efficiency label=L3PreFiltered;Generated Muon #eta;L3 Pass / L1 Pass (%)' genPassEta_L3PreFiltered genPassEta_L1Filtered", 
        "genEffPhi_L3PreFiltered '#phi Efficiency label=L3PreFiltered;Generated Muon #phi;L3 Pass / L1 Pass (%)' genPassPhi_L3PreFiltered genPassPhi_L1Filtered", 
        "genEffPt_L3PreFiltered 'pt Efficiency label=L3PreFiltered;Generated Muon pt (GeV);L2 Pass / L1 Pass (%)' genPassPt_L3PreFiltered genPassPt_L1Filtered",
        "genTurnOn_L3IsoFiltered 'Turn On label=L3IsoFiltered;Highest Generated Muon p_{T} (GeV);L3 Pass / L1 Pass (%)' genPassMaxPt_L3IsoFiltered genPassMaxPt_L1Filtered", 
        "genEffEta_L3IsoFiltered '#eta Efficiency label=L3IsoFiltered;Generated Muon #eta;L3 Pass / L1 Pass (%)' genPassEta_L3IsoFiltered genPassEta_L1Filtered", 
        "genEffPhi_L3IsoFiltered '#phi Efficiency label=L3IsoFiltered;Generated Muon #phi;L3 Pass / L1 Pass (%)' genPassPhi_L3IsoFiltered genPassPhi_L1Filtered", 
        "genEffPt_L3IsoFiltered 'pt Efficiency label=L3IsoFiltered;Generated Muon pt (GeV);L2 Pass / L1 Pass (%)' genPassPt_L3IsoFiltered genPassPt_L1Filtered",
        "recTurnOn_L1Filtered 'L1 Turn On, label=L1Filtered;Highest Reconstructed Muon p_{T} (GeV);L1 Pass / Reconstructed (%)' recPassMaxPt_L1Filtered recPassMaxPt_All",
        "recEffEta_L1Filtered 'L1 #eta Efficiency label=L1Filtered;Reconstructed Muon #eta;L1 Pass / Reconstructed (%)' recPassEta_L1Filtered recPassEta_All",
        "recEffPhi_L1Filtered 'L1 #phi Efficiency label=L1Filtered;Reconstructed Muon #phi;L1 Pass / Reconstructed (%)' recPassPhi_L1Filtered recPassPhi_All", 
        "recEffPt_L1Filtered 'L1 pt Efficiency label=L1Filtered;Reconstructed Muon pt (GeV);L1 Pass / Reconstructed (%)' recPassPt_L1Filtered recPassPt_All", 
        "recTurnOn_L2Filtered 'Turn On label=L2Filtered;Highest Reconstructed Muon p_{T} (GeV);L2 Pass / L1 Pass (%)' recPassMaxPt_L2Filtered recPassMaxPt_L1Filtered", 
        "recEffEta_L2Filtered '#eta Efficiency label=L2Filtered;Reconstructed Muon #eta;L2 Pass / L1 Pass (%)' recPassEta_L2Filtered recPassEta_L1Filtered", 
        "recEffPhi_L2Filtered '#phi Efficiency label=L2Filtered;Reconstructed Muon #phi;L2 Pass / L1 Pass (%)' recPassPhi_L2Filtered recPassPhi_L1Filtered", 
        "recEffPt_L2Filtered 'pt Efficiency label=L2Filtered;Reconstructed Muon pt (GeV);L2 Pass / L1 Pass (%)' recPassPt_L2Filtered recPassPt_L1Filtered",
        "recTurnOn_L2PreFiltered 'Turn On label=L2PreFiltered;Highest Reconstructed Muon p_{T} (GeV);L2 Pass / L1 Pass (%)' recPassMaxPt_L2PreFiltered recPassMaxPt_L1Filtered", 
        "recEffEta_L2PreFiltered '#eta Efficiency label=L2PreFiltered;Reconstructed Muon #eta;L2 Pass / L1 Pass (%)' recPassEta_L2PreFiltered recPassEta_L1Filtered", 
        "recEffPhi_L2PreFiltered '#phi Efficiency label=L2PreFiltered;Reconstructed Muon #phi;L2 Pass / L1 Pass (%)' recPassPhi_L2PreFiltered recPassPhi_L1Filtered", 
        "recEffPt_L2PreFiltered 'pt Efficiency label=L2PreFiltered;Reconstructed Muon pt (GeV);L2 Pass / L1 Pass (%)' recPassPt_L2PreFiltered recPassPt_L1Filtered",
        "recTurnOn_L2IsoFiltered 'Turn On label=L2IsoFiltered;Highest Reconstructed Muon p_{T} (GeV);L2 Pass / L1 Pass (%)' recPassMaxPt_L2IsoFiltered recPassMaxPt_L1Filtered", 
        "recEffEta_L2IsoFiltered '#eta Efficiency label=L2IsoFiltered;Reconstructed Muon #eta;L2 Pass / L1 Pass (%)' recPassEta_L2IsoFiltered recPassEta_L1Filtered", 
        "recEffPhi_L2IsoFiltered '#phi Efficiency label=L2IsoFiltered;Reconstructed Muon #phi;L2 Pass / L1 Pass (%)' recPassPhi_L2IsoFiltered recPassPhi_L1Filtered", 
        "recEffPt_L2IsoFiltered 'pt Efficiency label=L2IsoFiltered;Reconstructed Muon pt (GeV);L2 Pass / L1 Pass (%)' recPassPt_L2IsoFiltered recPassPt_L1Filtered",
        "recTurnOn_L3Filtered 'Turn On label=L3Filtered;Highest Reconstructed Muon p_{T} (GeV);L3 Pass / L1 Pass (%)' recPassMaxPt_L3Filtered recPassMaxPt_L1Filtered", 
        "recEffEta_L3Filtered '#eta Efficiency label=L3Filtered;Reconstructed Muon #eta;L3 Pass / L1 Pass (%)' recPassEta_L3Filtered recPassEta_L1Filtered", 
        "recEffPhi_L3Filtered '#phi Efficiency label=L3Filtered;Reconstructed Muon #phi;L3 Pass / L1 Pass (%)' recPassPhi_L3Filtered recPassPhi_L1Filtered", 
        "recEffPt_L3Filtered 'pt Efficiency label=L3Filtered;Reconstructed Muon pt (GeV);L2 Pass / L1 Pass (%)' recPassPt_L3Filtered recPassPt_L1Filtered",
        "recTurnOn_L3PreFiltered 'Turn On label=L3PreFiltered;Highest Reconstructed Muon p_{T} (GeV);L3 Pass / L1 Pass (%)' recPassMaxPt_L3PreFiltered recPassMaxPt_L1Filtered", 
        "recEffEta_L3PreFiltered '#eta Efficiency label=L3PreFiltered;Reconstructed Muon #eta;L3 Pass / L1 Pass (%)' recPassEta_L3PreFiltered recPassEta_L1Filtered", 
        "recEffPhi_L3PreFiltered '#phi Efficiency label=L3PreFiltered;Reconstructed Muon #phi;L3 Pass / L1 Pass (%)' recPassPhi_L3PreFiltered recPassPhi_L1Filtered", 
        "recEffPt_L3PreFiltered 'pt Efficiency label=L3PreFiltered;Reconstructed Muon pt (GeV);L2 Pass / L1 Pass (%)' recPassPt_L3PreFiltered recPassPt_L1Filtered",
        "recTurnOn_L3IsoFiltered 'Turn On label=L3IsoFiltered;Highest Reconstructed Muon p_{T} (GeV);L3 Pass / L1 Pass (%)' recPassMaxPt_L3IsoFiltered recPassMaxPt_L1Filtered", 
        "recEffEta_L3IsoFiltered '#eta Efficiency label=L3IsoFiltered;Reconstructed Muon #eta;L3 Pass / L1 Pass (%)' recPassEta_L3IsoFiltered recPassEta_L1Filtered", 
        "recEffPhi_L3IsoFiltered '#phi Efficiency label=L3IsoFiltered;Reconstructed Muon #phi;L3 Pass / L1 Pass (%)' recPassPhi_L3IsoFiltered recPassPhi_L1Filtered", 
        "recEffPt_L3IsoFiltered 'pt Efficiency label=L3IsoFiltered;Reconstructed Muon pt (GeV);L2 Pass / L1 Pass (%)' recPassPt_L3IsoFiltered recPassPt_L1Filtered",
    )
)

