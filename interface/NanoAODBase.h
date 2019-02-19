//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Thu Feb 14 16:09:22 2019 by ROOT version 6.12/07
// from TTree Events/Events
// found on file: root://xrootd-cms.infn.it//store/data/Run2016C/JetHT/NANOAOD/Nano14Dec2018-v1/280000/FDCE1B38-A947-D444-8F4B-1DDFC776056B.root
// found on file: root://xrootd-cms.infn.it//store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/FA634BB9-271F-4B4E-8AAD-5DF99571650F.root
// found on file: root://xrootd-cms.infn.it//store/data/Run2018C/JetHT/NANOAOD/Nano14Dec2018-v1/20000/F9BFB094-D60C-6548-8FA9-289193C7C3C1.root
//////////////////////////////////////////////////////////

#ifndef NanoAODBase_h
#define NanoAODBase_h

#define __USE_MET__ TRUE
#define __USE_ELECTRONS__ TRUE
#define __USE_FATJETS__ FALSE
#define __USE_ISOTRACKS__ FALSE
#define __USE_JETS__ TRUE
#define __USE_MUONS__ TRUE
#define __USE_PHOTONS__ TRUE
#define __USE_SOFTACTIVITYJETS__ FALSE
#define __USE_SUBJETS__ FALSE
#define __USE_TAU__ TRUE
#define __USE_TRIGOBJS__ TRUE
#define __USE_PVS__ TRUE
#define __USE_SVS__ FALSE
#define __USE_FILTERS__ TRUE

#define __MAX_ELECTRONS__ 20
#define __MAX_MUONS__ 20
#define __MAX_TAUS__ 20
#define __MAX_PHOTONS__ 20
#define __MAX_FATJETS__ 20
#define __MAX_ISOTRACKS__ 20
#define __MAX_JETS__ 40
#define __MAX_SOFTACTIVITYJETS__ 10
#define __MAX_SUBJETS__ 20
#define __MAX_TRIGOBJS__ 100
#define __MAX_SVS__ 30

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.

class NanoAODBase {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   UInt_t          run;
   UInt_t          luminosityBlock;
   ULong64_t       event;

   #ifdef __USE_MET__
   Float_t         CaloMET_phi;
   Float_t         CaloMET_pt;
   Float_t         CaloMET_sumEt;
   Float_t         ChsMET_phi;
   Float_t         ChsMET_pt;
   Float_t         ChsMET_sumEt;
   Float_t         METFixEE2017_MetUnclustEnUpDeltaX;
   Float_t         METFixEE2017_MetUnclustEnUpDeltaY;
   Float_t         METFixEE2017_phi;
   Float_t         METFixEE2017_pt;
   Float_t         METFixEE2017_sumEt;

   Float_t         MET_MetUnclustEnUpDeltaX;
   Float_t         MET_MetUnclustEnUpDeltaY;
   Float_t         MET_phi;
   Float_t         MET_pt;
   Float_t         MET_sumEt;

   Float_t         PuppiMET_phi;
   Float_t         PuppiMET_pt;
   Float_t         PuppiMET_sumEt;
   Float_t         RawMET_phi;
   Float_t         RawMET_pt;
   Float_t         RawMET_sumEt;

   Float_t         TkMET_phi;
   Float_t         TkMET_pt;
   Float_t         TkMET_sumEt;

   #endif

   #ifdef __USE_ELECTRONS__
   UInt_t          nElectron;
   Float_t         Electron_deltaEtaSC[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_dr03EcalRecHitSumEt[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_dr03HcalDepth1TowerSumEt[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_dr03TkSumPt[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_dr03TkSumPtHEEP[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_dxy[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_dxyErr[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_dz[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_dzErr[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_eInvMinusPInv[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_energyErr[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_eta[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_hoe[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_ip3d[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_jetRelIso[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_mass[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_miniPFRelIso_all[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_miniPFRelIso_chg[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_mvaFall17V1Iso[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_mvaFall17V1noIso[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_mvaFall17V2Iso[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_mvaFall17V2noIso[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_mvaSpring16GP[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_mvaSpring16HZZ[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_pfRelIso03_all[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_pfRelIso03_chg[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_phi[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_pt[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_r9[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_sieie[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_sip3d[__MAX_ELECTRONS__];   //[nElectron]
   Float_t         Electron_mvaTTH[__MAX_ELECTRONS__];   //[nElectron]
   Int_t           Electron_charge[__MAX_ELECTRONS__];   //[nElectron]
   Int_t           Electron_cutBased[__MAX_ELECTRONS__];   //[nElectron]
   Int_t           Electron_cutBased_Fall17_V1[__MAX_ELECTRONS__];   //[nElectron]
   Int_t           Electron_cutBased_HLTPreSel[__MAX_ELECTRONS__];   //[nElectron]
   Int_t           Electron_cutBased_Spring15[__MAX_ELECTRONS__];   //[nElectron]
   Int_t           Electron_cutBased_Sum16[__MAX_ELECTRONS__];   //[nElectron]
   Int_t           Electron_jetIdx[__MAX_ELECTRONS__];   //[nElectron]
   Int_t           Electron_pdgId[__MAX_ELECTRONS__];   //[nElectron]
   Int_t           Electron_photonIdx[__MAX_ELECTRONS__];   //[nElectron]
   Int_t           Electron_tightCharge[__MAX_ELECTRONS__];   //[nElectron]
   Int_t           Electron_vidNestedWPBitmap[__MAX_ELECTRONS__];   //[nElectron]
   Int_t           Electron_vidNestedWPBitmapSpring15[__MAX_ELECTRONS__];   //[nElectron]
   Int_t           Electron_vidNestedWPBitmapSum16[__MAX_ELECTRONS__];   //[nElectron]
   Bool_t          Electron_convVeto[__MAX_ELECTRONS__];   //[nElectron]
   Bool_t          Electron_cutBased_HEEP[__MAX_ELECTRONS__];   //[nElectron]
   Bool_t          Electron_isPFcand[__MAX_ELECTRONS__];   //[nElectron]
   UChar_t         Electron_lostHits[__MAX_ELECTRONS__];   //[nElectron]
   Bool_t          Electron_mvaFall17V1Iso_WP80[__MAX_ELECTRONS__];   //[nElectron]
   Bool_t          Electron_mvaFall17V1Iso_WP90[__MAX_ELECTRONS__];   //[nElectron]
   Bool_t          Electron_mvaFall17V1Iso_WPL[__MAX_ELECTRONS__];   //[nElectron]
   Bool_t          Electron_mvaFall17V1noIso_WP80[__MAX_ELECTRONS__];   //[nElectron]
   Bool_t          Electron_mvaFall17V1noIso_WP90[__MAX_ELECTRONS__];   //[nElectron]
   Bool_t          Electron_mvaFall17V1noIso_WPL[__MAX_ELECTRONS__];   //[nElectron]
   Bool_t          Electron_mvaFall17V2Iso_WP80[__MAX_ELECTRONS__];   //[nElectron]
   Bool_t          Electron_mvaFall17V2Iso_WP90[__MAX_ELECTRONS__];   //[nElectron]
   Bool_t          Electron_mvaFall17V2Iso_WPL[__MAX_ELECTRONS__];   //[nElectron]
   Bool_t          Electron_mvaFall17V2noIso_WP80[__MAX_ELECTRONS__];   //[nElectron]
   Bool_t          Electron_mvaFall17V2noIso_WP90[__MAX_ELECTRONS__];   //[nElectron]
   Bool_t          Electron_mvaFall17V2noIso_WPL[__MAX_ELECTRONS__];   //[nElectron]
   Bool_t          Electron_mvaSpring16GP_WP80[__MAX_ELECTRONS__];   //[nElectron]
   Bool_t          Electron_mvaSpring16GP_WP90[__MAX_ELECTRONS__];   //[nElectron]
   Bool_t          Electron_mvaSpring16HZZ_WPL[__MAX_ELECTRONS__];   //[nElectron]
   #endif

   #ifdef __USE_FATJETS__
   UInt_t          nFatJet;
   Float_t         FatJet_area[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_btagCMVA[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_btagCSVV2[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_btagDeepB[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_btagHbb[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_deepTagMD_H4qvsQCD[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_deepTagMD_HbbvsQCD[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_deepTagMD_TvsQCD[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_deepTagMD_WvsQCD[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_deepTagMD_ZHbbvsQCD[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_deepTagMD_ZHccvsQCD[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_deepTagMD_ZbbvsQCD[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_deepTagMD_ZvsQCD[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_deepTagMD_bbvsLight[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_deepTagMD_ccvsLight[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_deepTag_TvsQCD[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_deepTag_WvsQCD[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_deepTag_ZvsQCD[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_eta[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_mass[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_msoftdrop[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_n2b1[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_n3b1[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_phi[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_pt[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_rawFactor[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_tau1[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_tau2[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_tau3[__MAX_FATJETS__];   //[nFatJet]
   Float_t         FatJet_tau4[__MAX_FATJETS__];   //[nFatJet]
   Int_t           FatJet_jetId[__MAX_FATJETS__];   //[nFatJet]
   Int_t           FatJet_subJetIdx1[__MAX_FATJETS__];   //[nFatJet]
   Int_t           FatJet_subJetIdx2[__MAX_FATJETS__];   //[nFatJet]
   #endif

   #ifdef __USE_ISOTRACKS__
   UInt_t          nIsoTrack;
   Float_t         IsoTrack_dxy[__MAX_ISOTRACKS__];   //[nIsoTrack]
   Float_t         IsoTrack_dz[__MAX_ISOTRACKS__];   //[nIsoTrack]
   Float_t         IsoTrack_eta[__MAX_ISOTRACKS__];   //[nIsoTrack]
   Float_t         IsoTrack_pfRelIso03_all[__MAX_ISOTRACKS__];   //[nIsoTrack]
   Float_t         IsoTrack_pfRelIso03_chg[__MAX_ISOTRACKS__];   //[nIsoTrack]
   Float_t         IsoTrack_phi[__MAX_ISOTRACKS__];   //[nIsoTrack]
   Float_t         IsoTrack_pt[__MAX_ISOTRACKS__];   //[nIsoTrack]
   Float_t         IsoTrack_miniPFRelIso_all[__MAX_ISOTRACKS__];   //[nIsoTrack]
   Float_t         IsoTrack_miniPFRelIso_chg[__MAX_ISOTRACKS__];   //[nIsoTrack]
   Int_t           IsoTrack_fromPV[__MAX_ISOTRACKS__];   //[nIsoTrack]
   Int_t           IsoTrack_pdgId[__MAX_ISOTRACKS__];   //[nIsoTrack]
   Bool_t          IsoTrack_isHighPurityTrack[__MAX_ISOTRACKS__];   //[nIsoTrack]
   Bool_t          IsoTrack_isPFcand[__MAX_ISOTRACKS__];   //[nIsoTrack]
   Bool_t          IsoTrack_isFromLostTrack[__MAX_ISOTRACKS__];   //[nIsoTrack]
   #endif

   #ifdef __USE_JETS__
   UInt_t          nJet;
   Float_t         Jet_area[__MAX_JETS__];   //[nJet]
   Float_t         Jet_btagCMVA[__MAX_JETS__];   //[nJet]
   Float_t         Jet_btagCSVV2[__MAX_JETS__];   //[nJet]
   Float_t         Jet_btagDeepB[__MAX_JETS__];   //[nJet]
   Float_t         Jet_btagDeepC[__MAX_JETS__];   //[nJet]
   Float_t         Jet_btagDeepFlavB[__MAX_JETS__];   //[nJet]
   Float_t         Jet_chEmEF[__MAX_JETS__];   //[nJet]
   Float_t         Jet_chHEF[__MAX_JETS__];   //[nJet]
   Float_t         Jet_eta[__MAX_JETS__];   //[nJet]
   Float_t         Jet_mass[__MAX_JETS__];   //[nJet]
   Float_t         Jet_muEF[__MAX_JETS__];   //[nJet]
   Float_t         Jet_neEmEF[__MAX_JETS__];   //[nJet]
   Float_t         Jet_neHEF[__MAX_JETS__];   //[nJet]
   Float_t         Jet_phi[__MAX_JETS__];   //[nJet]
   Float_t         Jet_pt[__MAX_JETS__];   //[nJet]
   Float_t         Jet_qgl[__MAX_JETS__];   //[nJet]
   Float_t         Jet_rawFactor[__MAX_JETS__];   //[nJet]
   Float_t         Jet_bRegCorr[__MAX_JETS__];   //[nJet]
   Float_t         Jet_bRegRes[__MAX_JETS__];   //[nJet]
   Int_t           Jet_electronIdx1[__MAX_JETS__];   //[nJet]
   Int_t           Jet_electronIdx2[__MAX_JETS__];   //[nJet]
   Int_t           Jet_jetId[__MAX_JETS__];   //[nJet]
   Int_t           Jet_muonIdx1[__MAX_JETS__];   //[nJet]
   Int_t           Jet_muonIdx2[__MAX_JETS__];   //[nJet]
   Int_t           Jet_nConstituents[__MAX_JETS__];   //[nJet]
   Int_t           Jet_nElectrons[__MAX_JETS__];   //[nJet]
   Int_t           Jet_nMuons[__MAX_JETS__];   //[nJet]
   Int_t           Jet_puId[__MAX_JETS__];   //[nJet]
   #endif

   #ifdef __USE_MUONS__
   UInt_t          nMuon;
   Float_t         Muon_dxy[__MAX_MUONS__];   //[nMuon]
   Float_t         Muon_dxyErr[__MAX_MUONS__];   //[nMuon]
   Float_t         Muon_dz[__MAX_MUONS__];   //[nMuon]
   Float_t         Muon_dzErr[__MAX_MUONS__];   //[nMuon]
   Float_t         Muon_eta[__MAX_MUONS__];   //[nMuon]
   Float_t         Muon_ip3d[__MAX_MUONS__];   //[nMuon]
   Float_t         Muon_jetRelIso[__MAX_MUONS__];   //[nMuon]
   Float_t         Muon_mass[__MAX_MUONS__];   //[nMuon]
   Float_t         Muon_miniPFRelIso_all[__MAX_MUONS__];   //[nMuon]
   Float_t         Muon_miniPFRelIso_chg[__MAX_MUONS__];   //[nMuon]
   Float_t         Muon_pfRelIso03_all[__MAX_MUONS__];   //[nMuon]
   Float_t         Muon_pfRelIso03_chg[__MAX_MUONS__];   //[nMuon]
   Float_t         Muon_pfRelIso04_all[__MAX_MUONS__];   //[nMuon]
   Float_t         Muon_phi[__MAX_MUONS__];   //[nMuon]
   Float_t         Muon_pt[__MAX_MUONS__];   //[nMuon]
   Float_t         Muon_ptErr[__MAX_MUONS__];   //[nMuon]
   Float_t         Muon_segmentComp[__MAX_MUONS__];   //[nMuon]
   Float_t         Muon_sip3d[__MAX_MUONS__];   //[nMuon]
   Float_t         Muon_mvaTTH[__MAX_MUONS__];   //[nMuon]
   Int_t           Muon_charge[__MAX_MUONS__];   //[nMuon]
   Int_t           Muon_jetIdx[__MAX_MUONS__];   //[nMuon]
   Int_t           Muon_nStations[__MAX_MUONS__];   //[nMuon]
   Int_t           Muon_nTrackerLayers[__MAX_MUONS__];   //[nMuon]
   Int_t           Muon_pdgId[__MAX_MUONS__];   //[nMuon]
   Int_t           Muon_tightCharge[__MAX_MUONS__];   //[nMuon]
   UChar_t         Muon_highPtId[__MAX_MUONS__];   //[nMuon]
   Bool_t          Muon_inTimeMuon[__MAX_MUONS__];   //[nMuon]
   Bool_t          Muon_isGlobal[__MAX_MUONS__];   //[nMuon]
   Bool_t          Muon_isPFcand[__MAX_MUONS__];   //[nMuon]
   Bool_t          Muon_isTracker[__MAX_MUONS__];   //[nMuon]
   Bool_t          Muon_mediumId[__MAX_MUONS__];   //[nMuon]
   Bool_t          Muon_mediumPromptId[__MAX_MUONS__];   //[nMuon]
   UChar_t         Muon_miniIsoId[__MAX_MUONS__];   //[nMuon]
   UChar_t         Muon_multiIsoId[__MAX_MUONS__];   //[nMuon]
   UChar_t         Muon_mvaId[__MAX_MUONS__];   //[nMuon]
   UChar_t         Muon_pfIsoId[__MAX_MUONS__];   //[nMuon]
   Bool_t          Muon_softId[__MAX_MUONS__];   //[nMuon]
   Bool_t          Muon_softMvaId[__MAX_MUONS__];   //[nMuon]
   Bool_t          Muon_tightId[__MAX_MUONS__];   //[nMuon]
   UChar_t         Muon_tkIsoId[__MAX_MUONS__];   //[nMuon]
   Bool_t          Muon_triggerIdLoose[__MAX_MUONS__];   //[nMuon]
   #endif

   #ifdef __USE_PHOTONS__
   UInt_t          nPhoton;
   Float_t         Photon_eCorr[__MAX_PHOTONS__];   //[nPhoton]
   Float_t         Photon_energyErr[__MAX_PHOTONS__];   //[nPhoton]
   Float_t         Photon_eta[__MAX_PHOTONS__];   //[nPhoton]
   Float_t         Photon_hoe[__MAX_PHOTONS__];   //[nPhoton]
   Float_t         Photon_mass[__MAX_PHOTONS__];   //[nPhoton]
   Float_t         Photon_mvaID[__MAX_PHOTONS__];   //[nPhoton]
   Float_t         Photon_mvaID17[__MAX_PHOTONS__];   //[nPhoton]
   Float_t         Photon_pfRelIso03_all[__MAX_PHOTONS__];   //[nPhoton]
   Float_t         Photon_pfRelIso03_chg[__MAX_PHOTONS__];   //[nPhoton]
   Float_t         Photon_phi[__MAX_PHOTONS__];   //[nPhoton]
   Float_t         Photon_pt[__MAX_PHOTONS__];   //[nPhoton]
   Float_t         Photon_r9[__MAX_PHOTONS__];   //[nPhoton]
   Float_t         Photon_sieie[__MAX_PHOTONS__];   //[nPhoton]
   Int_t           Photon_charge[__MAX_PHOTONS__];   //[nPhoton]
   Int_t           Photon_cutBased[__MAX_PHOTONS__];   //[nPhoton]
   Int_t           Photon_cutBased17Bitmap[__MAX_PHOTONS__];   //[nPhoton]
   Int_t           Photon_electronIdx[__MAX_PHOTONS__];   //[nPhoton]
   Int_t           Photon_jetIdx[__MAX_PHOTONS__];   //[nPhoton]
   Int_t           Photon_pdgId[__MAX_PHOTONS__];   //[nPhoton]
   Int_t           Photon_vidNestedWPBitmap[__MAX_PHOTONS__];   //[nPhoton]
   Bool_t          Photon_electronVeto[__MAX_PHOTONS__];   //[nPhoton]
   Bool_t          Photon_isScEtaEB[__MAX_PHOTONS__];   //[nPhoton]
   Bool_t          Photon_isScEtaEE[__MAX_PHOTONS__];   //[nPhoton]
   Bool_t          Photon_mvaID17_WP80[__MAX_PHOTONS__];   //[nPhoton]
   Bool_t          Photon_mvaID17_WP90[__MAX_PHOTONS__];   //[nPhoton]
   Bool_t          Photon_mvaID_WP80[__MAX_PHOTONS__];   //[nPhoton]
   Bool_t          Photon_mvaID_WP90[__MAX_PHOTONS__];   //[nPhoton]
   Bool_t          Photon_pixelSeed[__MAX_PHOTONS__];   //[nPhoton]
   #endif

   Float_t         fixedGridRhoFastjetAll;
   Float_t         fixedGridRhoFastjetCentralCalo;
   Float_t         fixedGridRhoFastjetCentralNeutral;
   
   #ifdef __USE_SOFTACTIVITYJETS__
   UInt_t          nSoftActivityJet;
   Float_t         SoftActivityJet_eta[__MAX_SOFTACTIVITYJETS__];   //[nSoftActivityJet]
   Float_t         SoftActivityJet_phi[__MAX_SOFTACTIVITYJETS__];   //[nSoftActivityJet]
   Float_t         SoftActivityJet_pt[__MAX_SOFTACTIVITYJETS__];   //[nSoftActivityJet]
   Float_t         SoftActivityJetHT;
   Float_t         SoftActivityJetHT10;
   Float_t         SoftActivityJetHT2;
   Float_t         SoftActivityJetHT5;
   Int_t           SoftActivityJetNjets10;
   Int_t           SoftActivityJetNjets2;
   Int_t           SoftActivityJetNjets5;
   #endif

   #ifdef __USE_SUBJETS__
   UInt_t          nSubJet;
   Float_t         SubJet_btagCMVA[__MAX_SUBJETS__];   //[nSubJet]
   Float_t         SubJet_btagCSVV2[__MAX_SUBJETS__];   //[nSubJet]
   Float_t         SubJet_btagDeepB[__MAX_SUBJETS__];   //[nSubJet]
   Float_t         SubJet_eta[__MAX_SUBJETS__];   //[nSubJet]
   Float_t         SubJet_mass[__MAX_SUBJETS__];   //[nSubJet]
   Float_t         SubJet_n2b1[__MAX_SUBJETS__];   //[nSubJet]
   Float_t         SubJet_n3b1[__MAX_SUBJETS__];   //[nSubJet]
   Float_t         SubJet_phi[__MAX_SUBJETS__];   //[nSubJet]
   Float_t         SubJet_pt[__MAX_SUBJETS__];   //[nSubJet]
   Float_t         SubJet_rawFactor[__MAX_SUBJETS__];   //[nSubJet]
   Float_t         SubJet_tau1[__MAX_SUBJETS__];   //[nSubJet]
   Float_t         SubJet_tau2[__MAX_SUBJETS__];   //[nSubJet]
   Float_t         SubJet_tau3[__MAX_SUBJETS__];   //[nSubJet]
   Float_t         SubJet_tau4[__MAX_SUBJETS__];   //[nSubJet]
   #endif

   #ifdef __USE_TAU__
   UInt_t          nTau;
   Float_t         Tau_chargedIso[__MAX_TAUS__];   //[nTau]
   Float_t         Tau_dxy[__MAX_TAUS__];   //[nTau]
   Float_t         Tau_dz[__MAX_TAUS__];   //[nTau]
   Float_t         Tau_eta[__MAX_TAUS__];   //[nTau]
   Float_t         Tau_leadTkDeltaEta[__MAX_TAUS__];   //[nTau]
   Float_t         Tau_leadTkDeltaPhi[__MAX_TAUS__];   //[nTau]
   Float_t         Tau_leadTkPtOverTauPt[__MAX_TAUS__];   //[nTau]
   Float_t         Tau_mass[__MAX_TAUS__];   //[nTau]
   Float_t         Tau_neutralIso[__MAX_TAUS__];   //[nTau]
   Float_t         Tau_phi[__MAX_TAUS__];   //[nTau]
   Float_t         Tau_photonsOutsideSignalCone[__MAX_TAUS__];   //[nTau]
   Float_t         Tau_pt[__MAX_TAUS__];   //[nTau]
   Float_t         Tau_puCorr[__MAX_TAUS__];   //[nTau]
   Float_t         Tau_rawAntiEle[__MAX_TAUS__];   //[nTau]
   Float_t         Tau_rawIso[__MAX_TAUS__];   //[nTau]
   Float_t         Tau_rawIsodR03[__MAX_TAUS__];   //[nTau]
   Float_t         Tau_rawMVAnewDM2017v2[__MAX_TAUS__];   //[nTau]
   Float_t         Tau_rawMVAoldDM[__MAX_TAUS__];   //[nTau]
   Float_t         Tau_rawMVAoldDM2017v1[__MAX_TAUS__];   //[nTau]
   Float_t         Tau_rawMVAoldDM2017v2[__MAX_TAUS__];   //[nTau]
   Float_t         Tau_rawMVAoldDMdR032017v2[__MAX_TAUS__];   //[nTau]
   Int_t           Tau_charge[__MAX_TAUS__];   //[nTau]
   Int_t           Tau_decayMode[__MAX_TAUS__];   //[nTau]
   Int_t           Tau_jetIdx[__MAX_TAUS__];   //[nTau]
   Int_t           Tau_rawAntiEleCat[__MAX_TAUS__];   //[nTau]
   UChar_t         Tau_idAntiEle[__MAX_TAUS__];   //[nTau]
   UChar_t         Tau_idAntiMu[__MAX_TAUS__];   //[nTau]
   Bool_t          Tau_idDecayMode[__MAX_TAUS__];   //[nTau]
   Bool_t          Tau_idDecayModeNewDMs[__MAX_TAUS__];   //[nTau]
   UChar_t         Tau_idMVAnewDM2017v2[__MAX_TAUS__];   //[nTau]
   UChar_t         Tau_idMVAoldDM[__MAX_TAUS__];   //[nTau]
   UChar_t         Tau_idMVAoldDM2017v1[__MAX_TAUS__];   //[nTau]
   UChar_t         Tau_idMVAoldDM2017v2[__MAX_TAUS__];   //[nTau]
   UChar_t         Tau_idMVAoldDMdR032017v2[__MAX_TAUS__];   //[nTau]
   #endif

   #ifdef __USE_TRIGOBJS__
   UInt_t          nTrigObj;
   Float_t         TrigObj_pt[__MAX_TRIGOBJS__];   //[nTrigObj]
   Float_t         TrigObj_eta[__MAX_TRIGOBJS__];   //[nTrigObj]
   Float_t         TrigObj_phi[__MAX_TRIGOBJS__];   //[nTrigObj]
   Float_t         TrigObj_l1pt[__MAX_TRIGOBJS__];   //[nTrigObj]
   Float_t         TrigObj_l1pt_2[__MAX_TRIGOBJS__];   //[nTrigObj]
   Float_t         TrigObj_l2pt[__MAX_TRIGOBJS__];   //[nTrigObj]
   Int_t           TrigObj_id[__MAX_TRIGOBJS__];   //[nTrigObj]
   Int_t           TrigObj_l1iso[__MAX_TRIGOBJS__];   //[nTrigObj]
   Int_t           TrigObj_l1charge[__MAX_TRIGOBJS__];   //[nTrigObj]
   Int_t           TrigObj_filterBits[__MAX_TRIGOBJS__];   //[nTrigObj]
   #endif

   #ifdef __USE_PVS__
   UInt_t          nOtherPV;
   Float_t         OtherPV_z[20];   //[nOtherPV]
   Float_t         PV_ndof;
   Float_t         PV_x;
   Float_t         PV_y;
   Float_t         PV_z;
   Float_t         PV_chi2;
   Float_t         PV_score;
   Int_t           PV_npvs;
   Int_t           PV_npvsGood;
   #endif

   #ifdef __USE_SVS__
   UInt_t          nSV;
   Float_t         SV_dlen[__MAX_SVS__];   //[nSV]
   Float_t         SV_dlenSig[__MAX_SVS__];   //[nSV]
   Float_t         SV_pAngle[__MAX_SVS__];   //[nSV]
   UChar_t         Electron_cleanmask[__MAX_ELECTRONS__];   //[nElectron]
   UChar_t         Jet_cleanmask[__MAX_JETS__];   //[nJet]
   UChar_t         Muon_cleanmask[__MAX_MUONS__];   //[nMuon]
   UChar_t         Photon_cleanmask[__MAX_PHOTONS__];   //[nPhoton]
   UChar_t         Tau_cleanmask[__MAX_TAUS__];   //[nTau]
   Float_t         SV_chi2[__MAX_SVS__];   //[nSV]
   Float_t         SV_eta[__MAX_SVS__];   //[nSV]
   Float_t         SV_mass[__MAX_SVS__];   //[nSV]
   Float_t         SV_ndof[__MAX_SVS__];   //[nSV]
   Float_t         SV_phi[__MAX_SVS__];   //[nSV]
   Float_t         SV_pt[__MAX_SVS__];   //[nSV]
   Float_t         SV_x[__MAX_SVS__];   //[nSV]
   Float_t         SV_y[__MAX_SVS__];   //[nSV]
   Float_t         SV_z[__MAX_SVS__];   //[nSV]
   #endif

   #ifdef __USE_FILTERS__
   Bool_t          Flag_HBHENoiseFilter;
   Bool_t          Flag_HBHENoiseIsoFilter;
   Bool_t          Flag_CSCTightHaloFilter;
   Bool_t          Flag_CSCTightHaloTrkMuUnvetoFilter;
   Bool_t          Flag_CSCTightHalo2015Filter;
   Bool_t          Flag_globalTightHalo2016Filter;
   Bool_t          Flag_globalSuperTightHalo2016Filter;
   Bool_t          Flag_HcalStripHaloFilter;
   Bool_t          Flag_hcalLaserEventFilter;
   Bool_t          Flag_EcalDeadCellTriggerPrimitiveFilter;
   Bool_t          Flag_EcalDeadCellBoundaryEnergyFilter;
   Bool_t          Flag_ecalBadCalibFilter;
   Bool_t          Flag_goodVertices;
   Bool_t          Flag_eeBadScFilter;
   Bool_t          Flag_ecalLaserCorrFilter;
   Bool_t          Flag_trkPOGFilters;
   Bool_t          Flag_chargedHadronTrackResolutionFilter;
   Bool_t          Flag_muonBadTrackFilter;
   Bool_t          Flag_BadChargedCandidateFilter;
   Bool_t          Flag_BadPFMuonFilter;
   Bool_t          Flag_BadChargedCandidateSummer16Filter;
   Bool_t          Flag_BadPFMuonSummer16Filter;
   Bool_t          Flag_trkPOG_manystripclus53X;
   Bool_t          Flag_trkPOG_toomanystripclus53X;
   Bool_t          Flag_trkPOG_logErrorTooManyClusters;
   Bool_t          Flag_METFilters;
   #endif

   // List of branches
   TBranch        *b_run;   //!
   TBranch        *b_luminosityBlock;   //!
   TBranch        *b_event;   //!
   TBranch        *b_CaloMET_phi;   //!
   TBranch        *b_CaloMET_pt;   //!
   TBranch        *b_CaloMET_sumEt;   //!
   TBranch        *b_ChsMET_phi;   //!
   TBranch        *b_ChsMET_pt;   //!
   TBranch        *b_ChsMET_sumEt;   //!
   TBranch        *b_nElectron;   //!
   TBranch        *b_Electron_deltaEtaSC;   //!
   TBranch        *b_Electron_dr03EcalRecHitSumEt;   //!
   TBranch        *b_Electron_dr03HcalDepth1TowerSumEt;   //!
   TBranch        *b_Electron_dr03TkSumPt;   //!
   TBranch        *b_Electron_dr03TkSumPtHEEP;   //!
   TBranch        *b_Electron_dxy;   //!
   TBranch        *b_Electron_dxyErr;   //!
   TBranch        *b_Electron_dz;   //!
   TBranch        *b_Electron_dzErr;   //!
   TBranch        *b_Electron_eInvMinusPInv;   //!
   TBranch        *b_Electron_energyErr;   //!
   TBranch        *b_Electron_eta;   //!
   TBranch        *b_Electron_hoe;   //!
   TBranch        *b_Electron_ip3d;   //!
   TBranch        *b_Electron_jetRelIso;   //!
   TBranch        *b_Electron_mass;   //!
   TBranch        *b_Electron_miniPFRelIso_all;   //!
   TBranch        *b_Electron_miniPFRelIso_chg;   //!
   TBranch        *b_Electron_mvaFall17V1Iso;   //!
   TBranch        *b_Electron_mvaFall17V1noIso;   //!
   TBranch        *b_Electron_mvaFall17V2Iso;   //!
   TBranch        *b_Electron_mvaFall17V2noIso;   //!
   TBranch        *b_Electron_mvaSpring16GP;   //!
   TBranch        *b_Electron_mvaSpring16HZZ;   //!
   TBranch        *b_Electron_pfRelIso03_all;   //!
   TBranch        *b_Electron_pfRelIso03_chg;   //!
   TBranch        *b_Electron_phi;   //!
   TBranch        *b_Electron_pt;   //!
   TBranch        *b_Electron_r9;   //!
   TBranch        *b_Electron_sieie;   //!
   TBranch        *b_Electron_sip3d;   //!
   TBranch        *b_Electron_mvaTTH;   //!
   TBranch        *b_Electron_charge;   //!
   TBranch        *b_Electron_cutBased;   //!
   TBranch        *b_Electron_cutBased_Fall17_V1;   //!
   TBranch        *b_Electron_cutBased_HLTPreSel;   //!
   TBranch        *b_Electron_cutBased_Spring15;   //!
   TBranch        *b_Electron_cutBased_Sum16;   //!
   TBranch        *b_Electron_jetIdx;   //!
   TBranch        *b_Electron_pdgId;   //!
   TBranch        *b_Electron_photonIdx;   //!
   TBranch        *b_Electron_tightCharge;   //!
   TBranch        *b_Electron_vidNestedWPBitmap;   //!
   TBranch        *b_Electron_vidNestedWPBitmapSpring15;   //!
   TBranch        *b_Electron_vidNestedWPBitmapSum16;   //!
   TBranch        *b_Electron_convVeto;   //!
   TBranch        *b_Electron_cutBased_HEEP;   //!
   TBranch        *b_Electron_isPFcand;   //!
   TBranch        *b_Electron_lostHits;   //!
   TBranch        *b_Electron_mvaFall17V1Iso_WP80;   //!
   TBranch        *b_Electron_mvaFall17V1Iso_WP90;   //!
   TBranch        *b_Electron_mvaFall17V1Iso_WPL;   //!
   TBranch        *b_Electron_mvaFall17V1noIso_WP80;   //!
   TBranch        *b_Electron_mvaFall17V1noIso_WP90;   //!
   TBranch        *b_Electron_mvaFall17V1noIso_WPL;   //!
   TBranch        *b_Electron_mvaFall17V2Iso_WP80;   //!
   TBranch        *b_Electron_mvaFall17V2Iso_WP90;   //!
   TBranch        *b_Electron_mvaFall17V2Iso_WPL;   //!
   TBranch        *b_Electron_mvaFall17V2noIso_WP80;   //!
   TBranch        *b_Electron_mvaFall17V2noIso_WP90;   //!
   TBranch        *b_Electron_mvaFall17V2noIso_WPL;   //!
   TBranch        *b_Electron_mvaSpring16GP_WP80;   //!
   TBranch        *b_Electron_mvaSpring16GP_WP90;   //!
   TBranch        *b_Electron_mvaSpring16HZZ_WPL;   //!
   TBranch        *b_nFatJet;   //!
   TBranch        *b_FatJet_area;   //!
   TBranch        *b_FatJet_btagCMVA;   //!
   TBranch        *b_FatJet_btagCSVV2;   //!
   TBranch        *b_FatJet_btagDeepB;   //!
   TBranch        *b_FatJet_btagHbb;   //!
   TBranch        *b_FatJet_deepTagMD_H4qvsQCD;   //!
   TBranch        *b_FatJet_deepTagMD_HbbvsQCD;   //!
   TBranch        *b_FatJet_deepTagMD_TvsQCD;   //!
   TBranch        *b_FatJet_deepTagMD_WvsQCD;   //!
   TBranch        *b_FatJet_deepTagMD_ZHbbvsQCD;   //!
   TBranch        *b_FatJet_deepTagMD_ZHccvsQCD;   //!
   TBranch        *b_FatJet_deepTagMD_ZbbvsQCD;   //!
   TBranch        *b_FatJet_deepTagMD_ZvsQCD;   //!
   TBranch        *b_FatJet_deepTagMD_bbvsLight;   //!
   TBranch        *b_FatJet_deepTagMD_ccvsLight;   //!
   TBranch        *b_FatJet_deepTag_TvsQCD;   //!
   TBranch        *b_FatJet_deepTag_WvsQCD;   //!
   TBranch        *b_FatJet_deepTag_ZvsQCD;   //!
   TBranch        *b_FatJet_eta;   //!
   TBranch        *b_FatJet_mass;   //!
   TBranch        *b_FatJet_msoftdrop;   //!
   TBranch        *b_FatJet_n2b1;   //!
   TBranch        *b_FatJet_n3b1;   //!
   TBranch        *b_FatJet_phi;   //!
   TBranch        *b_FatJet_pt;   //!
   TBranch        *b_FatJet_rawFactor;   //!
   TBranch        *b_FatJet_tau1;   //!
   TBranch        *b_FatJet_tau2;   //!
   TBranch        *b_FatJet_tau3;   //!
   TBranch        *b_FatJet_tau4;   //!
   TBranch        *b_FatJet_jetId;   //!
   TBranch        *b_FatJet_subJetIdx1;   //!
   TBranch        *b_FatJet_subJetIdx2;   //!
   TBranch        *b_nIsoTrack;   //!
   TBranch        *b_IsoTrack_dxy;   //!
   TBranch        *b_IsoTrack_dz;   //!
   TBranch        *b_IsoTrack_eta;   //!
   TBranch        *b_IsoTrack_pfRelIso03_all;   //!
   TBranch        *b_IsoTrack_pfRelIso03_chg;   //!
   TBranch        *b_IsoTrack_phi;   //!
   TBranch        *b_IsoTrack_pt;   //!
   TBranch        *b_IsoTrack_miniPFRelIso_all;   //!
   TBranch        *b_IsoTrack_miniPFRelIso_chg;   //!
   TBranch        *b_IsoTrack_fromPV;   //!
   TBranch        *b_IsoTrack_pdgId;   //!
   TBranch        *b_IsoTrack_isHighPurityTrack;   //!
   TBranch        *b_IsoTrack_isPFcand;   //!
   TBranch        *b_IsoTrack_isFromLostTrack;   //!
   TBranch        *b_nJet;   //!
   TBranch        *b_Jet_area;   //!
   TBranch        *b_Jet_btagCMVA;   //!
   TBranch        *b_Jet_btagCSVV2;   //!
   TBranch        *b_Jet_btagDeepB;   //!
   TBranch        *b_Jet_btagDeepC;   //!
   TBranch        *b_Jet_btagDeepFlavB;   //!
   TBranch        *b_Jet_chEmEF;   //!
   TBranch        *b_Jet_chHEF;   //!
   TBranch        *b_Jet_eta;   //!
   TBranch        *b_Jet_mass;   //!
   TBranch        *b_Jet_muEF;   //!
   TBranch        *b_Jet_neEmEF;   //!
   TBranch        *b_Jet_neHEF;   //!
   TBranch        *b_Jet_phi;   //!
   TBranch        *b_Jet_pt;   //!
   TBranch        *b_Jet_qgl;   //!
   TBranch        *b_Jet_rawFactor;   //!
   TBranch        *b_Jet_bRegCorr;   //!
   TBranch        *b_Jet_bRegRes;   //!
   TBranch        *b_Jet_electronIdx1;   //!
   TBranch        *b_Jet_electronIdx2;   //!
   TBranch        *b_Jet_jetId;   //!
   TBranch        *b_Jet_muonIdx1;   //!
   TBranch        *b_Jet_muonIdx2;   //!
   TBranch        *b_Jet_nConstituents;   //!
   TBranch        *b_Jet_nElectrons;   //!
   TBranch        *b_Jet_nMuons;   //!
   TBranch        *b_Jet_puId;   //!
   TBranch        *b_METFixEE2017_MetUnclustEnUpDeltaX;   //!
   TBranch        *b_METFixEE2017_MetUnclustEnUpDeltaY;   //!
   TBranch        *b_METFixEE2017_phi;   //!
   TBranch        *b_METFixEE2017_pt;   //!
   TBranch        *b_METFixEE2017_sumEt;   //!
   TBranch        *b_MET_MetUnclustEnUpDeltaX;   //!
   TBranch        *b_MET_MetUnclustEnUpDeltaY;   //!
   TBranch        *b_MET_phi;   //!
   TBranch        *b_MET_pt;   //!
   TBranch        *b_MET_sumEt;   //!
   TBranch        *b_nMuon;   //!
   TBranch        *b_Muon_dxy;   //!
   TBranch        *b_Muon_dxyErr;   //!
   TBranch        *b_Muon_dz;   //!
   TBranch        *b_Muon_dzErr;   //!
   TBranch        *b_Muon_eta;   //!
   TBranch        *b_Muon_ip3d;   //!
   TBranch        *b_Muon_jetRelIso;   //!
   TBranch        *b_Muon_mass;   //!
   TBranch        *b_Muon_miniPFRelIso_all;   //!
   TBranch        *b_Muon_miniPFRelIso_chg;   //!
   TBranch        *b_Muon_pfRelIso03_all;   //!
   TBranch        *b_Muon_pfRelIso03_chg;   //!
   TBranch        *b_Muon_pfRelIso04_all;   //!
   TBranch        *b_Muon_phi;   //!
   TBranch        *b_Muon_pt;   //!
   TBranch        *b_Muon_ptErr;   //!
   TBranch        *b_Muon_segmentComp;   //!
   TBranch        *b_Muon_sip3d;   //!
   TBranch        *b_Muon_mvaTTH;   //!
   TBranch        *b_Muon_charge;   //!
   TBranch        *b_Muon_jetIdx;   //!
   TBranch        *b_Muon_nStations;   //!
   TBranch        *b_Muon_nTrackerLayers;   //!
   TBranch        *b_Muon_pdgId;   //!
   TBranch        *b_Muon_tightCharge;   //!
   TBranch        *b_Muon_highPtId;   //!
   TBranch        *b_Muon_inTimeMuon;   //!
   TBranch        *b_Muon_isGlobal;   //!
   TBranch        *b_Muon_isPFcand;   //!
   TBranch        *b_Muon_isTracker;   //!
   TBranch        *b_Muon_mediumId;   //!
   TBranch        *b_Muon_mediumPromptId;   //!
   TBranch        *b_Muon_miniIsoId;   //!
   TBranch        *b_Muon_multiIsoId;   //!
   TBranch        *b_Muon_mvaId;   //!
   TBranch        *b_Muon_pfIsoId;   //!
   TBranch        *b_Muon_softId;   //!
   TBranch        *b_Muon_softMvaId;   //!
   TBranch        *b_Muon_tightId;   //!
   TBranch        *b_Muon_tkIsoId;   //!
   TBranch        *b_Muon_triggerIdLoose;   //!
   TBranch        *b_nPhoton;   //!
   TBranch        *b_Photon_energyErr;   //!
   TBranch        *b_Photon_eta;   //!
   TBranch        *b_Photon_hoe;   //!
   TBranch        *b_Photon_mass;   //!
   TBranch        *b_Photon_mvaID;   //!
   TBranch        *b_Photon_mvaID17;   //!
   TBranch        *b_Photon_pfRelIso03_all;   //!
   TBranch        *b_Photon_pfRelIso03_chg;   //!
   TBranch        *b_Photon_phi;   //!
   TBranch        *b_Photon_pt;   //!
   TBranch        *b_Photon_r9;   //!
   TBranch        *b_Photon_sieie;   //!
   TBranch        *b_Photon_charge;   //!
   TBranch        *b_Photon_cutBased;   //!
   TBranch        *b_Photon_cutBased17Bitmap;   //!
   TBranch        *b_Photon_electronIdx;   //!
   TBranch        *b_Photon_jetIdx;   //!
   TBranch        *b_Photon_pdgId;   //!
   TBranch        *b_Photon_vidNestedWPBitmap;   //!
   TBranch        *b_Photon_electronVeto;   //!
   TBranch        *b_Photon_isScEtaEB;   //!
   TBranch        *b_Photon_isScEtaEE;   //!
   TBranch        *b_Photon_mvaID17_WP80;   //!
   TBranch        *b_Photon_mvaID17_WP90;   //!
   TBranch        *b_Photon_mvaID_WP80;   //!
   TBranch        *b_Photon_mvaID_WP90;   //!
   TBranch        *b_Photon_pixelSeed;   //!
   TBranch        *b_PuppiMET_phi;   //!
   TBranch        *b_PuppiMET_pt;   //!
   TBranch        *b_PuppiMET_sumEt;   //!
   TBranch        *b_RawMET_phi;   //!
   TBranch        *b_RawMET_pt;   //!
   TBranch        *b_RawMET_sumEt;   //!
   TBranch        *b_fixedGridRhoFastjetAll;   //!
   TBranch        *b_fixedGridRhoFastjetCentralCalo;   //!
   TBranch        *b_fixedGridRhoFastjetCentralNeutral;   //!
   TBranch        *b_nSoftActivityJet;   //!
   TBranch        *b_SoftActivityJet_eta;   //!
   TBranch        *b_SoftActivityJet_phi;   //!
   TBranch        *b_SoftActivityJet_pt;   //!
   TBranch        *b_SoftActivityJetHT;   //!
   TBranch        *b_SoftActivityJetHT10;   //!
   TBranch        *b_SoftActivityJetHT2;   //!
   TBranch        *b_SoftActivityJetHT5;   //!
   TBranch        *b_SoftActivityJetNjets10;   //!
   TBranch        *b_SoftActivityJetNjets2;   //!
   TBranch        *b_SoftActivityJetNjets5;   //!
   TBranch        *b_nSubJet;   //!
   TBranch        *b_SubJet_btagCMVA;   //!
   TBranch        *b_SubJet_btagCSVV2;   //!
   TBranch        *b_SubJet_btagDeepB;   //!
   TBranch        *b_SubJet_eta;   //!
   TBranch        *b_SubJet_mass;   //!
   TBranch        *b_SubJet_n2b1;   //!
   TBranch        *b_SubJet_n3b1;   //!
   TBranch        *b_SubJet_phi;   //!
   TBranch        *b_SubJet_pt;   //!
   TBranch        *b_SubJet_rawFactor;   //!
   TBranch        *b_SubJet_tau1;   //!
   TBranch        *b_SubJet_tau2;   //!
   TBranch        *b_SubJet_tau3;   //!
   TBranch        *b_SubJet_tau4;   //!
   TBranch        *b_nTau;   //!
   TBranch        *b_Tau_chargedIso;   //!
   TBranch        *b_Tau_dxy;   //!
   TBranch        *b_Tau_dz;   //!
   TBranch        *b_Tau_eta;   //!
   TBranch        *b_Tau_leadTkDeltaEta;   //!
   TBranch        *b_Tau_leadTkDeltaPhi;   //!
   TBranch        *b_Tau_leadTkPtOverTauPt;   //!
   TBranch        *b_Tau_mass;   //!
   TBranch        *b_Tau_neutralIso;   //!
   TBranch        *b_Tau_phi;   //!
   TBranch        *b_Tau_photonsOutsideSignalCone;   //!
   TBranch        *b_Tau_pt;   //!
   TBranch        *b_Tau_puCorr;   //!
   TBranch        *b_Tau_rawAntiEle;   //!
   TBranch        *b_Tau_rawIso;   //!
   TBranch        *b_Tau_rawIsodR03;   //!
   TBranch        *b_Tau_rawMVAnewDM2017v2;   //!
   TBranch        *b_Tau_rawMVAoldDM;   //!
   TBranch        *b_Tau_rawMVAoldDM2017v1;   //!
   TBranch        *b_Tau_rawMVAoldDM2017v2;   //!
   TBranch        *b_Tau_rawMVAoldDMdR032017v2;   //!
   TBranch        *b_Tau_charge;   //!
   TBranch        *b_Tau_decayMode;   //!
   TBranch        *b_Tau_jetIdx;   //!
   TBranch        *b_Tau_rawAntiEleCat;   //!
   TBranch        *b_Tau_idAntiEle;   //!
   TBranch        *b_Tau_idAntiMu;   //!
   TBranch        *b_Tau_idDecayMode;   //!
   TBranch        *b_Tau_idDecayModeNewDMs;   //!
   TBranch        *b_Tau_idMVAnewDM2017v2;   //!
   TBranch        *b_Tau_idMVAoldDM;   //!
   TBranch        *b_Tau_idMVAoldDM2017v1;   //!
   TBranch        *b_Tau_idMVAoldDM2017v2;   //!
   TBranch        *b_Tau_idMVAoldDMdR032017v2;   //!
   TBranch        *b_TkMET_phi;   //!
   TBranch        *b_TkMET_pt;   //!
   TBranch        *b_TkMET_sumEt;   //!
   TBranch        *b_nTrigObj;   //!
   TBranch        *b_TrigObj_pt;   //!
   TBranch        *b_TrigObj_eta;   //!
   TBranch        *b_TrigObj_phi;   //!
   TBranch        *b_TrigObj_l1pt;   //!
   TBranch        *b_TrigObj_l1pt_2;   //!
   TBranch        *b_TrigObj_l2pt;   //!
   TBranch        *b_TrigObj_id;   //!
   TBranch        *b_TrigObj_l1iso;   //!
   TBranch        *b_TrigObj_l1charge;   //!
   TBranch        *b_TrigObj_filterBits;   //!
   TBranch        *b_nOtherPV;   //!
   TBranch        *b_OtherPV_z;   //!
   TBranch        *b_PV_ndof;   //!
   TBranch        *b_PV_x;   //!
   TBranch        *b_PV_y;   //!
   TBranch        *b_PV_z;   //!
   TBranch        *b_PV_chi2;   //!
   TBranch        *b_PV_score;   //!
   TBranch        *b_PV_npvs;   //!
   TBranch        *b_PV_npvsGood;   //!
   TBranch        *b_nSV;   //!
   TBranch        *b_SV_dlen;   //!
   TBranch        *b_SV_dlenSig;   //!
   TBranch        *b_SV_pAngle;   //!
   TBranch        *b_Electron_cleanmask;   //!
   TBranch        *b_Jet_cleanmask;   //!
   TBranch        *b_Muon_cleanmask;   //!
   TBranch        *b_Photon_cleanmask;   //!
   TBranch        *b_Tau_cleanmask;   //!
   TBranch        *b_SV_chi2;   //!
   TBranch        *b_SV_eta;   //!
   TBranch        *b_SV_mass;   //!
   TBranch        *b_SV_ndof;   //!
   TBranch        *b_SV_phi;   //!
   TBranch        *b_SV_pt;   //!
   TBranch        *b_SV_x;   //!
   TBranch        *b_SV_y;   //!
   TBranch        *b_SV_z;   //!
   TBranch        *b_Flag_HBHENoiseFilter;   //!
   TBranch        *b_Flag_HBHENoiseIsoFilter;   //!
   TBranch        *b_Flag_CSCTightHaloFilter;   //!
   TBranch        *b_Flag_CSCTightHaloTrkMuUnvetoFilter;   //!
   TBranch        *b_Flag_CSCTightHalo2015Filter;   //!
   TBranch        *b_Flag_globalTightHalo2016Filter;   //!
   TBranch        *b_Flag_globalSuperTightHalo2016Filter;   //!
   TBranch        *b_Flag_HcalStripHaloFilter;   //!
   TBranch        *b_Flag_hcalLaserEventFilter;   //!
   TBranch        *b_Flag_EcalDeadCellTriggerPrimitiveFilter;   //!
   TBranch        *b_Flag_EcalDeadCellBoundaryEnergyFilter;   //!
   TBranch        *b_Flag_ecalBadCalibFilter;   //!
   TBranch        *b_Flag_goodVertices;   //!
   TBranch        *b_Flag_eeBadScFilter;   //!
   TBranch        *b_Flag_ecalLaserCorrFilter;   //!
   TBranch        *b_Flag_trkPOGFilters;   //!
   TBranch        *b_Flag_chargedHadronTrackResolutionFilter;   //!
   TBranch        *b_Flag_muonBadTrackFilter;   //!
   TBranch        *b_Flag_BadChargedCandidateFilter;   //!
   TBranch        *b_Flag_BadPFMuonFilter;   //!
   TBranch        *b_Flag_BadChargedCandidateSummer16Filter;   //!
   TBranch        *b_Flag_BadPFMuonSummer16Filter;   //!
   TBranch        *b_Flag_trkPOG_manystripclus53X;   //!
   TBranch        *b_Flag_trkPOG_toomanystripclus53X;   //!
   TBranch        *b_Flag_trkPOG_logErrorTooManyClusters;   //!
   TBranch        *b_Flag_METFilters;   //!
   TBranch        *b_HLTriggerFirstPath;   //!
   TBranch        *b_HLT_AK8PFJet360_TrimMass30;   //!
   TBranch        *b_HLT_AK8PFHT700_TrimR0p1PT0p03Mass50;   //!
   TBranch        *b_HLT_AK8PFHT650_TrimR0p1PT0p03Mass50;   //!
   TBranch        *b_HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20;   //!
   TBranch        *b_HLT_CaloJet500_NoJetID;   //!

   NanoAODBase(TTree *tree=0);
   virtual ~NanoAODBase();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef NanoAODBase_cxx
NanoAODBase::NanoAODBase(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("root://xrootd-cms.infn.it//store/data/Run2016C/JetHT/NANOAOD/Nano14Dec2018-v1/280000/FDCE1B38-A947-D444-8F4B-1DDFC776056B.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("root://xrootd-cms.infn.it//store/data/Run2016C/JetHT/NANOAOD/Nano14Dec2018-v1/280000/FDCE1B38-A947-D444-8F4B-1DDFC776056B.root");
      }
      f->GetObject("Events",tree);

   }
   Init(tree);
}

NanoAODBase::~NanoAODBase()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t NanoAODBase::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t NanoAODBase::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void NanoAODBase::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("run", &run, &b_run);
   fChain->SetBranchAddress("luminosityBlock", &luminosityBlock, &b_luminosityBlock);
   fChain->SetBranchAddress("event", &event, &b_event);

   fChain->SetBranchAddress("CaloMET_phi", &CaloMET_phi, &b_CaloMET_phi);
   fChain->SetBranchAddress("CaloMET_pt", &CaloMET_pt, &b_CaloMET_pt);
   fChain->SetBranchAddress("CaloMET_sumEt", &CaloMET_sumEt, &b_CaloMET_sumEt);
   fChain->SetBranchAddress("ChsMET_phi", &ChsMET_phi, &b_ChsMET_phi);
   fChain->SetBranchAddress("ChsMET_pt", &ChsMET_pt, &b_ChsMET_pt);
   fChain->SetBranchAddress("ChsMET_sumEt", &ChsMET_sumEt, &b_ChsMET_sumEt);

   fChain->SetBranchAddress("nElectron", &nElectron, &b_nElectron);
   fChain->SetBranchAddress("Electron_deltaEtaSC", Electron_deltaEtaSC, &b_Electron_deltaEtaSC);
   fChain->SetBranchAddress("Electron_dr03EcalRecHitSumEt", Electron_dr03EcalRecHitSumEt, &b_Electron_dr03EcalRecHitSumEt);
   fChain->SetBranchAddress("Electron_dr03HcalDepth1TowerSumEt", Electron_dr03HcalDepth1TowerSumEt, &b_Electron_dr03HcalDepth1TowerSumEt);
   fChain->SetBranchAddress("Electron_dr03TkSumPt", Electron_dr03TkSumPt, &b_Electron_dr03TkSumPt);
   fChain->SetBranchAddress("Electron_dr03TkSumPtHEEP", Electron_dr03TkSumPtHEEP, &b_Electron_dr03TkSumPtHEEP);
   fChain->SetBranchAddress("Electron_dxy", Electron_dxy, &b_Electron_dxy);
   fChain->SetBranchAddress("Electron_dxyErr", Electron_dxyErr, &b_Electron_dxyErr);
   fChain->SetBranchAddress("Electron_dz", Electron_dz, &b_Electron_dz);
   fChain->SetBranchAddress("Electron_dzErr", Electron_dzErr, &b_Electron_dzErr);
   fChain->SetBranchAddress("Electron_eInvMinusPInv", Electron_eInvMinusPInv, &b_Electron_eInvMinusPInv);
   fChain->SetBranchAddress("Electron_energyErr", Electron_energyErr, &b_Electron_energyErr);
   fChain->SetBranchAddress("Electron_eta", Electron_eta, &b_Electron_eta);
   fChain->SetBranchAddress("Electron_hoe", Electron_hoe, &b_Electron_hoe);
   fChain->SetBranchAddress("Electron_ip3d", Electron_ip3d, &b_Electron_ip3d);
   fChain->SetBranchAddress("Electron_jetRelIso", Electron_jetRelIso, &b_Electron_jetRelIso);
   fChain->SetBranchAddress("Electron_mass", Electron_mass, &b_Electron_mass);
   fChain->SetBranchAddress("Electron_miniPFRelIso_all", Electron_miniPFRelIso_all, &b_Electron_miniPFRelIso_all);
   fChain->SetBranchAddress("Electron_miniPFRelIso_chg", Electron_miniPFRelIso_chg, &b_Electron_miniPFRelIso_chg);
   fChain->SetBranchAddress("Electron_mvaFall17V1Iso", Electron_mvaFall17V1Iso, &b_Electron_mvaFall17V1Iso);
   fChain->SetBranchAddress("Electron_mvaFall17V1noIso", Electron_mvaFall17V1noIso, &b_Electron_mvaFall17V1noIso);
   fChain->SetBranchAddress("Electron_mvaFall17V2Iso", Electron_mvaFall17V2Iso, &b_Electron_mvaFall17V2Iso);
   fChain->SetBranchAddress("Electron_mvaFall17V2noIso", Electron_mvaFall17V2noIso, &b_Electron_mvaFall17V2noIso);
   fChain->SetBranchAddress("Electron_mvaSpring16GP", Electron_mvaSpring16GP, &b_Electron_mvaSpring16GP);
   fChain->SetBranchAddress("Electron_mvaSpring16HZZ", Electron_mvaSpring16HZZ, &b_Electron_mvaSpring16HZZ);
   fChain->SetBranchAddress("Electron_pfRelIso03_all", Electron_pfRelIso03_all, &b_Electron_pfRelIso03_all);
   fChain->SetBranchAddress("Electron_pfRelIso03_chg", Electron_pfRelIso03_chg, &b_Electron_pfRelIso03_chg);
   fChain->SetBranchAddress("Electron_phi", Electron_phi, &b_Electron_phi);
   fChain->SetBranchAddress("Electron_pt", Electron_pt, &b_Electron_pt);
   fChain->SetBranchAddress("Electron_r9", Electron_r9, &b_Electron_r9);
   fChain->SetBranchAddress("Electron_sieie", Electron_sieie, &b_Electron_sieie);
   fChain->SetBranchAddress("Electron_sip3d", Electron_sip3d, &b_Electron_sip3d);
   fChain->SetBranchAddress("Electron_mvaTTH", Electron_mvaTTH, &b_Electron_mvaTTH);
   fChain->SetBranchAddress("Electron_charge", Electron_charge, &b_Electron_charge);
   fChain->SetBranchAddress("Electron_cutBased", Electron_cutBased, &b_Electron_cutBased);
   fChain->SetBranchAddress("Electron_cutBased_Fall17_V1", Electron_cutBased_Fall17_V1, &b_Electron_cutBased_Fall17_V1);
   fChain->SetBranchAddress("Electron_cutBased_HLTPreSel", Electron_cutBased_HLTPreSel, &b_Electron_cutBased_HLTPreSel);
   fChain->SetBranchAddress("Electron_cutBased_Spring15", Electron_cutBased_Spring15, &b_Electron_cutBased_Spring15);
   fChain->SetBranchAddress("Electron_cutBased_Sum16", Electron_cutBased_Sum16, &b_Electron_cutBased_Sum16);
   fChain->SetBranchAddress("Electron_jetIdx", Electron_jetIdx, &b_Electron_jetIdx);
   fChain->SetBranchAddress("Electron_pdgId", Electron_pdgId, &b_Electron_pdgId);
   fChain->SetBranchAddress("Electron_photonIdx", Electron_photonIdx, &b_Electron_photonIdx);
   fChain->SetBranchAddress("Electron_tightCharge", Electron_tightCharge, &b_Electron_tightCharge);
   fChain->SetBranchAddress("Electron_vidNestedWPBitmap", Electron_vidNestedWPBitmap, &b_Electron_vidNestedWPBitmap);
   fChain->SetBranchAddress("Electron_vidNestedWPBitmapSpring15", Electron_vidNestedWPBitmapSpring15, &b_Electron_vidNestedWPBitmapSpring15);
   fChain->SetBranchAddress("Electron_vidNestedWPBitmapSum16", Electron_vidNestedWPBitmapSum16, &b_Electron_vidNestedWPBitmapSum16);
   fChain->SetBranchAddress("Electron_convVeto", Electron_convVeto, &b_Electron_convVeto);
   fChain->SetBranchAddress("Electron_cutBased_HEEP", Electron_cutBased_HEEP, &b_Electron_cutBased_HEEP);
   fChain->SetBranchAddress("Electron_isPFcand", Electron_isPFcand, &b_Electron_isPFcand);
   fChain->SetBranchAddress("Electron_lostHits", Electron_lostHits, &b_Electron_lostHits);
   fChain->SetBranchAddress("Electron_mvaFall17V1Iso_WP80", Electron_mvaFall17V1Iso_WP80, &b_Electron_mvaFall17V1Iso_WP80);
   fChain->SetBranchAddress("Electron_mvaFall17V1Iso_WP90", Electron_mvaFall17V1Iso_WP90, &b_Electron_mvaFall17V1Iso_WP90);
   fChain->SetBranchAddress("Electron_mvaFall17V1Iso_WPL", Electron_mvaFall17V1Iso_WPL, &b_Electron_mvaFall17V1Iso_WPL);
   fChain->SetBranchAddress("Electron_mvaFall17V1noIso_WP80", Electron_mvaFall17V1noIso_WP80, &b_Electron_mvaFall17V1noIso_WP80);
   fChain->SetBranchAddress("Electron_mvaFall17V1noIso_WP90", Electron_mvaFall17V1noIso_WP90, &b_Electron_mvaFall17V1noIso_WP90);
   fChain->SetBranchAddress("Electron_mvaFall17V1noIso_WPL", Electron_mvaFall17V1noIso_WPL, &b_Electron_mvaFall17V1noIso_WPL);
   fChain->SetBranchAddress("Electron_mvaFall17V2Iso_WP80", Electron_mvaFall17V2Iso_WP80, &b_Electron_mvaFall17V2Iso_WP80);
   fChain->SetBranchAddress("Electron_mvaFall17V2Iso_WP90", Electron_mvaFall17V2Iso_WP90, &b_Electron_mvaFall17V2Iso_WP90);
   fChain->SetBranchAddress("Electron_mvaFall17V2Iso_WPL", Electron_mvaFall17V2Iso_WPL, &b_Electron_mvaFall17V2Iso_WPL);
   fChain->SetBranchAddress("Electron_mvaFall17V2noIso_WP80", Electron_mvaFall17V2noIso_WP80, &b_Electron_mvaFall17V2noIso_WP80);
   fChain->SetBranchAddress("Electron_mvaFall17V2noIso_WP90", Electron_mvaFall17V2noIso_WP90, &b_Electron_mvaFall17V2noIso_WP90);
   fChain->SetBranchAddress("Electron_mvaFall17V2noIso_WPL", Electron_mvaFall17V2noIso_WPL, &b_Electron_mvaFall17V2noIso_WPL);
   fChain->SetBranchAddress("Electron_mvaSpring16GP_WP80", Electron_mvaSpring16GP_WP80, &b_Electron_mvaSpring16GP_WP80);
   fChain->SetBranchAddress("Electron_mvaSpring16GP_WP90", Electron_mvaSpring16GP_WP90, &b_Electron_mvaSpring16GP_WP90);
   fChain->SetBranchAddress("Electron_mvaSpring16HZZ_WPL", Electron_mvaSpring16HZZ_WPL, &b_Electron_mvaSpring16HZZ_WPL);

   fChain->SetBranchAddress("nFatJet", &nFatJet, &b_nFatJet);
   fChain->SetBranchAddress("FatJet_area", FatJet_area, &b_FatJet_area);
   fChain->SetBranchAddress("FatJet_btagCMVA", FatJet_btagCMVA, &b_FatJet_btagCMVA);
   fChain->SetBranchAddress("FatJet_btagCSVV2", FatJet_btagCSVV2, &b_FatJet_btagCSVV2);
   fChain->SetBranchAddress("FatJet_btagDeepB", FatJet_btagDeepB, &b_FatJet_btagDeepB);
   fChain->SetBranchAddress("FatJet_btagHbb", FatJet_btagHbb, &b_FatJet_btagHbb);
   fChain->SetBranchAddress("FatJet_deepTagMD_H4qvsQCD", FatJet_deepTagMD_H4qvsQCD, &b_FatJet_deepTagMD_H4qvsQCD);
   fChain->SetBranchAddress("FatJet_deepTagMD_HbbvsQCD", FatJet_deepTagMD_HbbvsQCD, &b_FatJet_deepTagMD_HbbvsQCD);
   fChain->SetBranchAddress("FatJet_deepTagMD_TvsQCD", FatJet_deepTagMD_TvsQCD, &b_FatJet_deepTagMD_TvsQCD);
   fChain->SetBranchAddress("FatJet_deepTagMD_WvsQCD", FatJet_deepTagMD_WvsQCD, &b_FatJet_deepTagMD_WvsQCD);
   fChain->SetBranchAddress("FatJet_deepTagMD_ZHbbvsQCD", FatJet_deepTagMD_ZHbbvsQCD, &b_FatJet_deepTagMD_ZHbbvsQCD);
   fChain->SetBranchAddress("FatJet_deepTagMD_ZHccvsQCD", FatJet_deepTagMD_ZHccvsQCD, &b_FatJet_deepTagMD_ZHccvsQCD);
   fChain->SetBranchAddress("FatJet_deepTagMD_ZbbvsQCD", FatJet_deepTagMD_ZbbvsQCD, &b_FatJet_deepTagMD_ZbbvsQCD);
   fChain->SetBranchAddress("FatJet_deepTagMD_ZvsQCD", FatJet_deepTagMD_ZvsQCD, &b_FatJet_deepTagMD_ZvsQCD);
   fChain->SetBranchAddress("FatJet_deepTagMD_bbvsLight", FatJet_deepTagMD_bbvsLight, &b_FatJet_deepTagMD_bbvsLight);
   fChain->SetBranchAddress("FatJet_deepTagMD_ccvsLight", FatJet_deepTagMD_ccvsLight, &b_FatJet_deepTagMD_ccvsLight);
   fChain->SetBranchAddress("FatJet_deepTag_TvsQCD", FatJet_deepTag_TvsQCD, &b_FatJet_deepTag_TvsQCD);
   fChain->SetBranchAddress("FatJet_deepTag_WvsQCD", FatJet_deepTag_WvsQCD, &b_FatJet_deepTag_WvsQCD);
   fChain->SetBranchAddress("FatJet_deepTag_ZvsQCD", FatJet_deepTag_ZvsQCD, &b_FatJet_deepTag_ZvsQCD);
   fChain->SetBranchAddress("FatJet_eta", FatJet_eta, &b_FatJet_eta);
   fChain->SetBranchAddress("FatJet_mass", FatJet_mass, &b_FatJet_mass);
   fChain->SetBranchAddress("FatJet_msoftdrop", FatJet_msoftdrop, &b_FatJet_msoftdrop);
   fChain->SetBranchAddress("FatJet_n2b1", FatJet_n2b1, &b_FatJet_n2b1);
   fChain->SetBranchAddress("FatJet_n3b1", FatJet_n3b1, &b_FatJet_n3b1);
   fChain->SetBranchAddress("FatJet_phi", FatJet_phi, &b_FatJet_phi);
   fChain->SetBranchAddress("FatJet_pt", FatJet_pt, &b_FatJet_pt);
   fChain->SetBranchAddress("FatJet_rawFactor", FatJet_rawFactor, &b_FatJet_rawFactor);
   fChain->SetBranchAddress("FatJet_tau1", FatJet_tau1, &b_FatJet_tau1);
   fChain->SetBranchAddress("FatJet_tau2", FatJet_tau2, &b_FatJet_tau2);
   fChain->SetBranchAddress("FatJet_tau3", FatJet_tau3, &b_FatJet_tau3);
   fChain->SetBranchAddress("FatJet_tau4", FatJet_tau4, &b_FatJet_tau4);
   fChain->SetBranchAddress("FatJet_jetId", FatJet_jetId, &b_FatJet_jetId);
   fChain->SetBranchAddress("FatJet_subJetIdx1", FatJet_subJetIdx1, &b_FatJet_subJetIdx1);
   fChain->SetBranchAddress("FatJet_subJetIdx2", FatJet_subJetIdx2, &b_FatJet_subJetIdx2);

   fChain->SetBranchAddress("nIsoTrack", &nIsoTrack, &b_nIsoTrack);
   fChain->SetBranchAddress("IsoTrack_dxy", IsoTrack_dxy, &b_IsoTrack_dxy);
   fChain->SetBranchAddress("IsoTrack_dz", IsoTrack_dz, &b_IsoTrack_dz);
   fChain->SetBranchAddress("IsoTrack_eta", IsoTrack_eta, &b_IsoTrack_eta);
   fChain->SetBranchAddress("IsoTrack_pfRelIso03_all", IsoTrack_pfRelIso03_all, &b_IsoTrack_pfRelIso03_all);
   fChain->SetBranchAddress("IsoTrack_pfRelIso03_chg", IsoTrack_pfRelIso03_chg, &b_IsoTrack_pfRelIso03_chg);
   fChain->SetBranchAddress("IsoTrack_phi", IsoTrack_phi, &b_IsoTrack_phi);
   fChain->SetBranchAddress("IsoTrack_pt", IsoTrack_pt, &b_IsoTrack_pt);
   fChain->SetBranchAddress("IsoTrack_miniPFRelIso_all", IsoTrack_miniPFRelIso_all, &b_IsoTrack_miniPFRelIso_all);
   fChain->SetBranchAddress("IsoTrack_miniPFRelIso_chg", IsoTrack_miniPFRelIso_chg, &b_IsoTrack_miniPFRelIso_chg);
   fChain->SetBranchAddress("IsoTrack_fromPV", IsoTrack_fromPV, &b_IsoTrack_fromPV);
   fChain->SetBranchAddress("IsoTrack_pdgId", IsoTrack_pdgId, &b_IsoTrack_pdgId);
   fChain->SetBranchAddress("IsoTrack_isHighPurityTrack", IsoTrack_isHighPurityTrack, &b_IsoTrack_isHighPurityTrack);
   fChain->SetBranchAddress("IsoTrack_isPFcand", IsoTrack_isPFcand, &b_IsoTrack_isPFcand);
   fChain->SetBranchAddress("IsoTrack_isFromLostTrack", IsoTrack_isFromLostTrack, &b_IsoTrack_isFromLostTrack);

   fChain->SetBranchAddress("nJet", &nJet, &b_nJet);
   fChain->SetBranchAddress("Jet_area", Jet_area, &b_Jet_area);
   fChain->SetBranchAddress("Jet_btagCMVA", Jet_btagCMVA, &b_Jet_btagCMVA);
   fChain->SetBranchAddress("Jet_btagCSVV2", Jet_btagCSVV2, &b_Jet_btagCSVV2);
   fChain->SetBranchAddress("Jet_btagDeepB", Jet_btagDeepB, &b_Jet_btagDeepB);
   fChain->SetBranchAddress("Jet_btagDeepC", Jet_btagDeepC, &b_Jet_btagDeepC);
   fChain->SetBranchAddress("Jet_btagDeepFlavB", Jet_btagDeepFlavB, &b_Jet_btagDeepFlavB);
   fChain->SetBranchAddress("Jet_chEmEF", Jet_chEmEF, &b_Jet_chEmEF);
   fChain->SetBranchAddress("Jet_chHEF", Jet_chHEF, &b_Jet_chHEF);
   fChain->SetBranchAddress("Jet_eta", Jet_eta, &b_Jet_eta);
   fChain->SetBranchAddress("Jet_mass", Jet_mass, &b_Jet_mass);
   fChain->SetBranchAddress("Jet_muEF", Jet_muEF, &b_Jet_muEF);
   fChain->SetBranchAddress("Jet_neEmEF", Jet_neEmEF, &b_Jet_neEmEF);
   fChain->SetBranchAddress("Jet_neHEF", Jet_neHEF, &b_Jet_neHEF);
   fChain->SetBranchAddress("Jet_phi", Jet_phi, &b_Jet_phi);
   fChain->SetBranchAddress("Jet_pt", Jet_pt, &b_Jet_pt);
   fChain->SetBranchAddress("Jet_qgl", Jet_qgl, &b_Jet_qgl);
   fChain->SetBranchAddress("Jet_rawFactor", Jet_rawFactor, &b_Jet_rawFactor);
   fChain->SetBranchAddress("Jet_bRegCorr", Jet_bRegCorr, &b_Jet_bRegCorr);
   fChain->SetBranchAddress("Jet_bRegRes", Jet_bRegRes, &b_Jet_bRegRes);
   fChain->SetBranchAddress("Jet_electronIdx1", Jet_electronIdx1, &b_Jet_electronIdx1);
   fChain->SetBranchAddress("Jet_electronIdx2", Jet_electronIdx2, &b_Jet_electronIdx2);
   fChain->SetBranchAddress("Jet_jetId", Jet_jetId, &b_Jet_jetId);
   fChain->SetBranchAddress("Jet_muonIdx1", Jet_muonIdx1, &b_Jet_muonIdx1);
   fChain->SetBranchAddress("Jet_muonIdx2", Jet_muonIdx2, &b_Jet_muonIdx2);
   fChain->SetBranchAddress("Jet_nConstituents", Jet_nConstituents, &b_Jet_nConstituents);
   fChain->SetBranchAddress("Jet_nElectrons", Jet_nElectrons, &b_Jet_nElectrons);
   fChain->SetBranchAddress("Jet_nMuons", Jet_nMuons, &b_Jet_nMuons);
   fChain->SetBranchAddress("Jet_puId", Jet_puId, &b_Jet_puId);
   fChain->SetBranchAddress("METFixEE2017_MetUnclustEnUpDeltaX", &METFixEE2017_MetUnclustEnUpDeltaX, &b_METFixEE2017_MetUnclustEnUpDeltaX);
   fChain->SetBranchAddress("METFixEE2017_MetUnclustEnUpDeltaY", &METFixEE2017_MetUnclustEnUpDeltaY, &b_METFixEE2017_MetUnclustEnUpDeltaY);
   fChain->SetBranchAddress("METFixEE2017_phi", &METFixEE2017_phi, &b_METFixEE2017_phi);
   fChain->SetBranchAddress("METFixEE2017_pt", &METFixEE2017_pt, &b_METFixEE2017_pt);
   fChain->SetBranchAddress("METFixEE2017_sumEt", &METFixEE2017_sumEt, &b_METFixEE2017_sumEt);
   fChain->SetBranchAddress("MET_MetUnclustEnUpDeltaX", &MET_MetUnclustEnUpDeltaX, &b_MET_MetUnclustEnUpDeltaX);
   fChain->SetBranchAddress("MET_MetUnclustEnUpDeltaY", &MET_MetUnclustEnUpDeltaY, &b_MET_MetUnclustEnUpDeltaY);
   fChain->SetBranchAddress("MET_phi", &MET_phi, &b_MET_phi);
   fChain->SetBranchAddress("MET_pt", &MET_pt, &b_MET_pt);
   fChain->SetBranchAddress("MET_sumEt", &MET_sumEt, &b_MET_sumEt);

   fChain->SetBranchAddress("nMuon", &nMuon, &b_nMuon);
   fChain->SetBranchAddress("Muon_dxy", Muon_dxy, &b_Muon_dxy);
   fChain->SetBranchAddress("Muon_dxyErr", Muon_dxyErr, &b_Muon_dxyErr);
   fChain->SetBranchAddress("Muon_dz", Muon_dz, &b_Muon_dz);
   fChain->SetBranchAddress("Muon_dzErr", Muon_dzErr, &b_Muon_dzErr);
   fChain->SetBranchAddress("Muon_eta", Muon_eta, &b_Muon_eta);
   fChain->SetBranchAddress("Muon_ip3d", Muon_ip3d, &b_Muon_ip3d);
   fChain->SetBranchAddress("Muon_jetRelIso", Muon_jetRelIso, &b_Muon_jetRelIso);
   fChain->SetBranchAddress("Muon_mass", Muon_mass, &b_Muon_mass);
   fChain->SetBranchAddress("Muon_miniPFRelIso_all", Muon_miniPFRelIso_all, &b_Muon_miniPFRelIso_all);
   fChain->SetBranchAddress("Muon_miniPFRelIso_chg", Muon_miniPFRelIso_chg, &b_Muon_miniPFRelIso_chg);
   fChain->SetBranchAddress("Muon_pfRelIso03_all", Muon_pfRelIso03_all, &b_Muon_pfRelIso03_all);
   fChain->SetBranchAddress("Muon_pfRelIso03_chg", Muon_pfRelIso03_chg, &b_Muon_pfRelIso03_chg);
   fChain->SetBranchAddress("Muon_pfRelIso04_all", Muon_pfRelIso04_all, &b_Muon_pfRelIso04_all);
   fChain->SetBranchAddress("Muon_phi", Muon_phi, &b_Muon_phi);
   fChain->SetBranchAddress("Muon_pt", Muon_pt, &b_Muon_pt);
   fChain->SetBranchAddress("Muon_ptErr", Muon_ptErr, &b_Muon_ptErr);
   fChain->SetBranchAddress("Muon_segmentComp", Muon_segmentComp, &b_Muon_segmentComp);
   fChain->SetBranchAddress("Muon_sip3d", Muon_sip3d, &b_Muon_sip3d);
   fChain->SetBranchAddress("Muon_mvaTTH", Muon_mvaTTH, &b_Muon_mvaTTH);
   fChain->SetBranchAddress("Muon_charge", Muon_charge, &b_Muon_charge);
   fChain->SetBranchAddress("Muon_jetIdx", Muon_jetIdx, &b_Muon_jetIdx);
   fChain->SetBranchAddress("Muon_nStations", Muon_nStations, &b_Muon_nStations);
   fChain->SetBranchAddress("Muon_nTrackerLayers", Muon_nTrackerLayers, &b_Muon_nTrackerLayers);
   fChain->SetBranchAddress("Muon_pdgId", Muon_pdgId, &b_Muon_pdgId);
   fChain->SetBranchAddress("Muon_tightCharge", Muon_tightCharge, &b_Muon_tightCharge);
   fChain->SetBranchAddress("Muon_highPtId", Muon_highPtId, &b_Muon_highPtId);
   fChain->SetBranchAddress("Muon_inTimeMuon", Muon_inTimeMuon, &b_Muon_inTimeMuon);
   fChain->SetBranchAddress("Muon_isGlobal", Muon_isGlobal, &b_Muon_isGlobal);
   fChain->SetBranchAddress("Muon_isPFcand", Muon_isPFcand, &b_Muon_isPFcand);
   fChain->SetBranchAddress("Muon_isTracker", Muon_isTracker, &b_Muon_isTracker);
   fChain->SetBranchAddress("Muon_mediumId", Muon_mediumId, &b_Muon_mediumId);
   fChain->SetBranchAddress("Muon_mediumPromptId", Muon_mediumPromptId, &b_Muon_mediumPromptId);
   fChain->SetBranchAddress("Muon_miniIsoId", Muon_miniIsoId, &b_Muon_miniIsoId);
   fChain->SetBranchAddress("Muon_multiIsoId", Muon_multiIsoId, &b_Muon_multiIsoId);
   fChain->SetBranchAddress("Muon_mvaId", Muon_mvaId, &b_Muon_mvaId);
   fChain->SetBranchAddress("Muon_pfIsoId", Muon_pfIsoId, &b_Muon_pfIsoId);
   fChain->SetBranchAddress("Muon_softId", Muon_softId, &b_Muon_softId);
   fChain->SetBranchAddress("Muon_softMvaId", Muon_softMvaId, &b_Muon_softMvaId);
   fChain->SetBranchAddress("Muon_tightId", Muon_tightId, &b_Muon_tightId);
   fChain->SetBranchAddress("Muon_tkIsoId", Muon_tkIsoId, &b_Muon_tkIsoId);
   fChain->SetBranchAddress("Muon_triggerIdLoose", Muon_triggerIdLoose, &b_Muon_triggerIdLoose);

   fChain->SetBranchAddress("nPhoton", &nPhoton, &b_nPhoton);
   fChain->SetBranchAddress("Photon_energyErr", Photon_energyErr, &b_Photon_energyErr);
   fChain->SetBranchAddress("Photon_eta", Photon_eta, &b_Photon_eta);
   fChain->SetBranchAddress("Photon_hoe", Photon_hoe, &b_Photon_hoe);
   fChain->SetBranchAddress("Photon_mass", Photon_mass, &b_Photon_mass);
   fChain->SetBranchAddress("Photon_mvaID", Photon_mvaID, &b_Photon_mvaID);
   fChain->SetBranchAddress("Photon_mvaID17", Photon_mvaID17, &b_Photon_mvaID17);
   fChain->SetBranchAddress("Photon_pfRelIso03_all", Photon_pfRelIso03_all, &b_Photon_pfRelIso03_all);
   fChain->SetBranchAddress("Photon_pfRelIso03_chg", Photon_pfRelIso03_chg, &b_Photon_pfRelIso03_chg);
   fChain->SetBranchAddress("Photon_phi", Photon_phi, &b_Photon_phi);
   fChain->SetBranchAddress("Photon_pt", Photon_pt, &b_Photon_pt);
   fChain->SetBranchAddress("Photon_r9", Photon_r9, &b_Photon_r9);
   fChain->SetBranchAddress("Photon_sieie", Photon_sieie, &b_Photon_sieie);
   fChain->SetBranchAddress("Photon_charge", Photon_charge, &b_Photon_charge);
   fChain->SetBranchAddress("Photon_cutBased", Photon_cutBased, &b_Photon_cutBased);
   fChain->SetBranchAddress("Photon_cutBased17Bitmap", Photon_cutBased17Bitmap, &b_Photon_cutBased17Bitmap);
   fChain->SetBranchAddress("Photon_electronIdx", Photon_electronIdx, &b_Photon_electronIdx);
   fChain->SetBranchAddress("Photon_jetIdx", Photon_jetIdx, &b_Photon_jetIdx);
   fChain->SetBranchAddress("Photon_pdgId", Photon_pdgId, &b_Photon_pdgId);
   fChain->SetBranchAddress("Photon_vidNestedWPBitmap", Photon_vidNestedWPBitmap, &b_Photon_vidNestedWPBitmap);
   fChain->SetBranchAddress("Photon_electronVeto", Photon_electronVeto, &b_Photon_electronVeto);
   fChain->SetBranchAddress("Photon_isScEtaEB", Photon_isScEtaEB, &b_Photon_isScEtaEB);
   fChain->SetBranchAddress("Photon_isScEtaEE", Photon_isScEtaEE, &b_Photon_isScEtaEE);
   fChain->SetBranchAddress("Photon_mvaID17_WP80", Photon_mvaID17_WP80, &b_Photon_mvaID17_WP80);
   fChain->SetBranchAddress("Photon_mvaID17_WP90", Photon_mvaID17_WP90, &b_Photon_mvaID17_WP90);
   fChain->SetBranchAddress("Photon_mvaID_WP80", Photon_mvaID_WP80, &b_Photon_mvaID_WP80);
   fChain->SetBranchAddress("Photon_mvaID_WP90", Photon_mvaID_WP90, &b_Photon_mvaID_WP90);
   fChain->SetBranchAddress("Photon_pixelSeed", Photon_pixelSeed, &b_Photon_pixelSeed);

   fChain->SetBranchAddress("PuppiMET_phi", &PuppiMET_phi, &b_PuppiMET_phi);
   fChain->SetBranchAddress("PuppiMET_pt", &PuppiMET_pt, &b_PuppiMET_pt);
   fChain->SetBranchAddress("PuppiMET_sumEt", &PuppiMET_sumEt, &b_PuppiMET_sumEt);
   fChain->SetBranchAddress("RawMET_phi", &RawMET_phi, &b_RawMET_phi);
   fChain->SetBranchAddress("RawMET_pt", &RawMET_pt, &b_RawMET_pt);
   fChain->SetBranchAddress("RawMET_sumEt", &RawMET_sumEt, &b_RawMET_sumEt);

   fChain->SetBranchAddress("fixedGridRhoFastjetAll", &fixedGridRhoFastjetAll, &b_fixedGridRhoFastjetAll);
   fChain->SetBranchAddress("fixedGridRhoFastjetCentralCalo", &fixedGridRhoFastjetCentralCalo, &b_fixedGridRhoFastjetCentralCalo);
   fChain->SetBranchAddress("fixedGridRhoFastjetCentralNeutral", &fixedGridRhoFastjetCentralNeutral, &b_fixedGridRhoFastjetCentralNeutral);

   fChain->SetBranchAddress("nSoftActivityJet", &nSoftActivityJet, &b_nSoftActivityJet);
   fChain->SetBranchAddress("SoftActivityJet_eta", SoftActivityJet_eta, &b_SoftActivityJet_eta);
   fChain->SetBranchAddress("SoftActivityJet_phi", SoftActivityJet_phi, &b_SoftActivityJet_phi);
   fChain->SetBranchAddress("SoftActivityJet_pt", SoftActivityJet_pt, &b_SoftActivityJet_pt);
   fChain->SetBranchAddress("SoftActivityJetHT", &SoftActivityJetHT, &b_SoftActivityJetHT);
   fChain->SetBranchAddress("SoftActivityJetHT10", &SoftActivityJetHT10, &b_SoftActivityJetHT10);
   fChain->SetBranchAddress("SoftActivityJetHT2", &SoftActivityJetHT2, &b_SoftActivityJetHT2);
   fChain->SetBranchAddress("SoftActivityJetHT5", &SoftActivityJetHT5, &b_SoftActivityJetHT5);
   fChain->SetBranchAddress("SoftActivityJetNjets10", &SoftActivityJetNjets10, &b_SoftActivityJetNjets10);
   fChain->SetBranchAddress("SoftActivityJetNjets2", &SoftActivityJetNjets2, &b_SoftActivityJetNjets2);
   fChain->SetBranchAddress("SoftActivityJetNjets5", &SoftActivityJetNjets5, &b_SoftActivityJetNjets5);

   fChain->SetBranchAddress("nSubJet", &nSubJet, &b_nSubJet);
   fChain->SetBranchAddress("SubJet_btagCMVA", SubJet_btagCMVA, &b_SubJet_btagCMVA);
   fChain->SetBranchAddress("SubJet_btagCSVV2", SubJet_btagCSVV2, &b_SubJet_btagCSVV2);
   fChain->SetBranchAddress("SubJet_btagDeepB", SubJet_btagDeepB, &b_SubJet_btagDeepB);
   fChain->SetBranchAddress("SubJet_eta", SubJet_eta, &b_SubJet_eta);
   fChain->SetBranchAddress("SubJet_mass", SubJet_mass, &b_SubJet_mass);
   fChain->SetBranchAddress("SubJet_n2b1", SubJet_n2b1, &b_SubJet_n2b1);
   fChain->SetBranchAddress("SubJet_n3b1", SubJet_n3b1, &b_SubJet_n3b1);
   fChain->SetBranchAddress("SubJet_phi", SubJet_phi, &b_SubJet_phi);
   fChain->SetBranchAddress("SubJet_pt", SubJet_pt, &b_SubJet_pt);
   fChain->SetBranchAddress("SubJet_rawFactor", SubJet_rawFactor, &b_SubJet_rawFactor);
   fChain->SetBranchAddress("SubJet_tau1", SubJet_tau1, &b_SubJet_tau1);
   fChain->SetBranchAddress("SubJet_tau2", SubJet_tau2, &b_SubJet_tau2);
   fChain->SetBranchAddress("SubJet_tau3", SubJet_tau3, &b_SubJet_tau3);
   fChain->SetBranchAddress("SubJet_tau4", SubJet_tau4, &b_SubJet_tau4);

   fChain->SetBranchAddress("nTau", &nTau, &b_nTau);
   fChain->SetBranchAddress("Tau_chargedIso", Tau_chargedIso, &b_Tau_chargedIso);
   fChain->SetBranchAddress("Tau_dxy", Tau_dxy, &b_Tau_dxy);
   fChain->SetBranchAddress("Tau_dz", Tau_dz, &b_Tau_dz);
   fChain->SetBranchAddress("Tau_eta", Tau_eta, &b_Tau_eta);
   fChain->SetBranchAddress("Tau_leadTkDeltaEta", Tau_leadTkDeltaEta, &b_Tau_leadTkDeltaEta);
   fChain->SetBranchAddress("Tau_leadTkDeltaPhi", Tau_leadTkDeltaPhi, &b_Tau_leadTkDeltaPhi);
   fChain->SetBranchAddress("Tau_leadTkPtOverTauPt", Tau_leadTkPtOverTauPt, &b_Tau_leadTkPtOverTauPt);
   fChain->SetBranchAddress("Tau_mass", Tau_mass, &b_Tau_mass);
   fChain->SetBranchAddress("Tau_neutralIso", Tau_neutralIso, &b_Tau_neutralIso);
   fChain->SetBranchAddress("Tau_phi", Tau_phi, &b_Tau_phi);
   fChain->SetBranchAddress("Tau_photonsOutsideSignalCone", Tau_photonsOutsideSignalCone, &b_Tau_photonsOutsideSignalCone);
   fChain->SetBranchAddress("Tau_pt", Tau_pt, &b_Tau_pt);
   fChain->SetBranchAddress("Tau_puCorr", Tau_puCorr, &b_Tau_puCorr);
   fChain->SetBranchAddress("Tau_rawAntiEle", Tau_rawAntiEle, &b_Tau_rawAntiEle);
   fChain->SetBranchAddress("Tau_rawIso", Tau_rawIso, &b_Tau_rawIso);
   fChain->SetBranchAddress("Tau_rawIsodR03", Tau_rawIsodR03, &b_Tau_rawIsodR03);
   fChain->SetBranchAddress("Tau_rawMVAnewDM2017v2", Tau_rawMVAnewDM2017v2, &b_Tau_rawMVAnewDM2017v2);
   fChain->SetBranchAddress("Tau_rawMVAoldDM", Tau_rawMVAoldDM, &b_Tau_rawMVAoldDM);
   fChain->SetBranchAddress("Tau_rawMVAoldDM2017v1", Tau_rawMVAoldDM2017v1, &b_Tau_rawMVAoldDM2017v1);
   fChain->SetBranchAddress("Tau_rawMVAoldDM2017v2", Tau_rawMVAoldDM2017v2, &b_Tau_rawMVAoldDM2017v2);
   fChain->SetBranchAddress("Tau_rawMVAoldDMdR032017v2", Tau_rawMVAoldDMdR032017v2, &b_Tau_rawMVAoldDMdR032017v2);
   fChain->SetBranchAddress("Tau_charge", Tau_charge, &b_Tau_charge);
   fChain->SetBranchAddress("Tau_decayMode", Tau_decayMode, &b_Tau_decayMode);
   fChain->SetBranchAddress("Tau_jetIdx", Tau_jetIdx, &b_Tau_jetIdx);
   fChain->SetBranchAddress("Tau_rawAntiEleCat", Tau_rawAntiEleCat, &b_Tau_rawAntiEleCat);
   fChain->SetBranchAddress("Tau_idAntiEle", Tau_idAntiEle, &b_Tau_idAntiEle);
   fChain->SetBranchAddress("Tau_idAntiMu", Tau_idAntiMu, &b_Tau_idAntiMu);
   fChain->SetBranchAddress("Tau_idDecayMode", Tau_idDecayMode, &b_Tau_idDecayMode);
   fChain->SetBranchAddress("Tau_idDecayModeNewDMs", Tau_idDecayModeNewDMs, &b_Tau_idDecayModeNewDMs);
   fChain->SetBranchAddress("Tau_idMVAnewDM2017v2", Tau_idMVAnewDM2017v2, &b_Tau_idMVAnewDM2017v2);
   fChain->SetBranchAddress("Tau_idMVAoldDM", Tau_idMVAoldDM, &b_Tau_idMVAoldDM);
   fChain->SetBranchAddress("Tau_idMVAoldDM2017v1", Tau_idMVAoldDM2017v1, &b_Tau_idMVAoldDM2017v1);
   fChain->SetBranchAddress("Tau_idMVAoldDM2017v2", Tau_idMVAoldDM2017v2, &b_Tau_idMVAoldDM2017v2);
   fChain->SetBranchAddress("Tau_idMVAoldDMdR032017v2", Tau_idMVAoldDMdR032017v2, &b_Tau_idMVAoldDMdR032017v2);

   fChain->SetBranchAddress("TkMET_phi", &TkMET_phi, &b_TkMET_phi);
   fChain->SetBranchAddress("TkMET_pt", &TkMET_pt, &b_TkMET_pt);
   fChain->SetBranchAddress("TkMET_sumEt", &TkMET_sumEt, &b_TkMET_sumEt);

   fChain->SetBranchAddress("nTrigObj", &nTrigObj, &b_nTrigObj);
   fChain->SetBranchAddress("TrigObj_pt", TrigObj_pt, &b_TrigObj_pt);
   fChain->SetBranchAddress("TrigObj_eta", TrigObj_eta, &b_TrigObj_eta);
   fChain->SetBranchAddress("TrigObj_phi", TrigObj_phi, &b_TrigObj_phi);
   fChain->SetBranchAddress("TrigObj_l1pt", TrigObj_l1pt, &b_TrigObj_l1pt);
   fChain->SetBranchAddress("TrigObj_l1pt_2", TrigObj_l1pt_2, &b_TrigObj_l1pt_2);
   fChain->SetBranchAddress("TrigObj_l2pt", TrigObj_l2pt, &b_TrigObj_l2pt);
   fChain->SetBranchAddress("TrigObj_id", TrigObj_id, &b_TrigObj_id);
   fChain->SetBranchAddress("TrigObj_l1iso", TrigObj_l1iso, &b_TrigObj_l1iso);
   fChain->SetBranchAddress("TrigObj_l1charge", TrigObj_l1charge, &b_TrigObj_l1charge);
   fChain->SetBranchAddress("TrigObj_filterBits", TrigObj_filterBits, &b_TrigObj_filterBits);

   fChain->SetBranchAddress("nOtherPV", &nOtherPV, &b_nOtherPV);
   fChain->SetBranchAddress("OtherPV_z", OtherPV_z, &b_OtherPV_z);

   fChain->SetBranchAddress("PV_ndof", &PV_ndof, &b_PV_ndof);
   fChain->SetBranchAddress("PV_x", &PV_x, &b_PV_x);
   fChain->SetBranchAddress("PV_y", &PV_y, &b_PV_y);
   fChain->SetBranchAddress("PV_z", &PV_z, &b_PV_z);
   fChain->SetBranchAddress("PV_chi2", &PV_chi2, &b_PV_chi2);
   fChain->SetBranchAddress("PV_score", &PV_score, &b_PV_score);
   fChain->SetBranchAddress("PV_npvs", &PV_npvs, &b_PV_npvs);
   fChain->SetBranchAddress("PV_npvsGood", &PV_npvsGood, &b_PV_npvsGood);
   fChain->SetBranchAddress("nSV", &nSV, &b_nSV);
   fChain->SetBranchAddress("SV_dlen", SV_dlen, &b_SV_dlen);
   fChain->SetBranchAddress("SV_dlenSig", SV_dlenSig, &b_SV_dlenSig);
   fChain->SetBranchAddress("SV_pAngle", SV_pAngle, &b_SV_pAngle);
   fChain->SetBranchAddress("Electron_cleanmask", Electron_cleanmask, &b_Electron_cleanmask);
   fChain->SetBranchAddress("Jet_cleanmask", Jet_cleanmask, &b_Jet_cleanmask);
   fChain->SetBranchAddress("Muon_cleanmask", Muon_cleanmask, &b_Muon_cleanmask);
   fChain->SetBranchAddress("Photon_cleanmask", Photon_cleanmask, &b_Photon_cleanmask);
   fChain->SetBranchAddress("Tau_cleanmask", Tau_cleanmask, &b_Tau_cleanmask);
   fChain->SetBranchAddress("SV_chi2", SV_chi2, &b_SV_chi2);
   fChain->SetBranchAddress("SV_eta", SV_eta, &b_SV_eta);
   fChain->SetBranchAddress("SV_mass", SV_mass, &b_SV_mass);
   fChain->SetBranchAddress("SV_ndof", SV_ndof, &b_SV_ndof);
   fChain->SetBranchAddress("SV_phi", SV_phi, &b_SV_phi);
   fChain->SetBranchAddress("SV_pt", SV_pt, &b_SV_pt);
   fChain->SetBranchAddress("SV_x", SV_x, &b_SV_x);
   fChain->SetBranchAddress("SV_y", SV_y, &b_SV_y);
   fChain->SetBranchAddress("SV_z", SV_z, &b_SV_z);

   fChain->SetBranchAddress("Flag_HBHENoiseFilter", &Flag_HBHENoiseFilter, &b_Flag_HBHENoiseFilter);
   fChain->SetBranchAddress("Flag_HBHENoiseIsoFilter", &Flag_HBHENoiseIsoFilter, &b_Flag_HBHENoiseIsoFilter);
   fChain->SetBranchAddress("Flag_CSCTightHaloFilter", &Flag_CSCTightHaloFilter, &b_Flag_CSCTightHaloFilter);
   fChain->SetBranchAddress("Flag_CSCTightHaloTrkMuUnvetoFilter", &Flag_CSCTightHaloTrkMuUnvetoFilter, &b_Flag_CSCTightHaloTrkMuUnvetoFilter);
   fChain->SetBranchAddress("Flag_CSCTightHalo2015Filter", &Flag_CSCTightHalo2015Filter, &b_Flag_CSCTightHalo2015Filter);
   fChain->SetBranchAddress("Flag_globalTightHalo2016Filter", &Flag_globalTightHalo2016Filter, &b_Flag_globalTightHalo2016Filter);
   fChain->SetBranchAddress("Flag_globalSuperTightHalo2016Filter", &Flag_globalSuperTightHalo2016Filter, &b_Flag_globalSuperTightHalo2016Filter);
   fChain->SetBranchAddress("Flag_HcalStripHaloFilter", &Flag_HcalStripHaloFilter, &b_Flag_HcalStripHaloFilter);
   fChain->SetBranchAddress("Flag_hcalLaserEventFilter", &Flag_hcalLaserEventFilter, &b_Flag_hcalLaserEventFilter);
   fChain->SetBranchAddress("Flag_EcalDeadCellTriggerPrimitiveFilter", &Flag_EcalDeadCellTriggerPrimitiveFilter, &b_Flag_EcalDeadCellTriggerPrimitiveFilter);
   fChain->SetBranchAddress("Flag_EcalDeadCellBoundaryEnergyFilter", &Flag_EcalDeadCellBoundaryEnergyFilter, &b_Flag_EcalDeadCellBoundaryEnergyFilter);
   fChain->SetBranchAddress("Flag_ecalBadCalibFilter", &Flag_ecalBadCalibFilter, &b_Flag_ecalBadCalibFilter);
   fChain->SetBranchAddress("Flag_goodVertices", &Flag_goodVertices, &b_Flag_goodVertices);
   fChain->SetBranchAddress("Flag_eeBadScFilter", &Flag_eeBadScFilter, &b_Flag_eeBadScFilter);
   fChain->SetBranchAddress("Flag_ecalLaserCorrFilter", &Flag_ecalLaserCorrFilter, &b_Flag_ecalLaserCorrFilter);
   fChain->SetBranchAddress("Flag_trkPOGFilters", &Flag_trkPOGFilters, &b_Flag_trkPOGFilters);
   fChain->SetBranchAddress("Flag_chargedHadronTrackResolutionFilter", &Flag_chargedHadronTrackResolutionFilter, &b_Flag_chargedHadronTrackResolutionFilter);
   fChain->SetBranchAddress("Flag_muonBadTrackFilter", &Flag_muonBadTrackFilter, &b_Flag_muonBadTrackFilter);
   fChain->SetBranchAddress("Flag_BadChargedCandidateFilter", &Flag_BadChargedCandidateFilter, &b_Flag_BadChargedCandidateFilter);
   fChain->SetBranchAddress("Flag_BadPFMuonFilter", &Flag_BadPFMuonFilter, &b_Flag_BadPFMuonFilter);
   fChain->SetBranchAddress("Flag_BadChargedCandidateSummer16Filter", &Flag_BadChargedCandidateSummer16Filter, &b_Flag_BadChargedCandidateSummer16Filter);
   fChain->SetBranchAddress("Flag_BadPFMuonSummer16Filter", &Flag_BadPFMuonSummer16Filter, &b_Flag_BadPFMuonSummer16Filter);
   fChain->SetBranchAddress("Flag_trkPOG_manystripclus53X", &Flag_trkPOG_manystripclus53X, &b_Flag_trkPOG_manystripclus53X);
   fChain->SetBranchAddress("Flag_trkPOG_toomanystripclus53X", &Flag_trkPOG_toomanystripclus53X, &b_Flag_trkPOG_toomanystripclus53X);
   fChain->SetBranchAddress("Flag_trkPOG_logErrorTooManyClusters", &Flag_trkPOG_logErrorTooManyClusters, &b_Flag_trkPOG_logErrorTooManyClusters);
   fChain->SetBranchAddress("Flag_METFilters", &Flag_METFilters, &b_Flag_METFilters);

   Notify();
}

Bool_t NanoAODBase::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void NanoAODBase::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t NanoAODBase::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef NanoAODBase_cxx
