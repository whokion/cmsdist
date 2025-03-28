### RPM cms cmsswdata 42.0
## NOCOMPILER
Source: none

%define BaseTool %(echo %n | tr '[a-z-]' '[A-Z_]')

Requires: data-CondTools-SiPhase2Tracker
Requires: data-SimCalorimetry-EcalEBTrigPrimProducers
Requires: data-DataFormats-DetId
Requires: data-DataFormats-SiStripCluster
Requires: data-DQM-HcalTasks
Requires: data-DataFormats-Scouting
Requires: data-DataFormats-HLTReco
Requires: data-RecoPPS-Local
Requires: data-DataFormats-L1TGlobal
Requires: data-DataFormats-FEDRawData
Requires: data-DataFormats-Common
Requires: data-CondTools-Hcal
Requires: data-RecoTracker-DisplacedRegionalTracking
Requires: data-RecoEgamma-EgammaPhotonProducers
Requires: data-L1TriggerConfig-L1TConfigProducers
Requires: data-DQM-Integration
Requires: data-CondTools-SiStrip
Requires: data-RecoEcal-EgammaClusterProducers
Requires: data-DQM-EcalMonitorClient
Requires: data-RecoTracker-MkFit
Requires: data-RecoMuon-TrackerSeedGenerator
Requires: data-Validation-HGCalValidation
Requires: data-HeterogeneousCore-SonicTriton
Requires: data-L1Trigger-TrackTrigger
Requires: data-RecoTracker-TkSeedGenerator
Requires: data-Alignment-OfflineValidation
Requires: data-Geometry-DTGeometryBuilder
Requires: data-L1Trigger-CSCTriggerPrimitives
Requires: data-L1Trigger-Phase2L1ParticleFlow
Requires: data-L1Trigger-DTTriggerPhase2
Requires: data-L1Trigger-TrackFindingTracklet
Requires: data-L1Trigger-TrackFindingTMTT
Requires: data-Geometry-TestReference
Requires: data-RecoMTD-TimingIDTools
Requires: data-MagneticField-Engine
Requires: data-PhysicsTools-PatUtils
Requires: data-RecoTauTag-TrainingFiles
Requires: data-DetectorDescription-Schema
Requires: data-MagneticField-Interpolation
Requires: data-L1Trigger-L1TCalorimeter
Requires: data-L1Trigger-RPCTrigger
Requires: data-RecoParticleFlow-PFBlockProducer
Requires: data-RecoParticleFlow-PFTracking
Requires: data-RecoParticleFlow-PFProducer
Requires: data-RecoMuon-MuonIdentification
Requires: data-RecoMET-METPUSubtraction
Requires: data-RecoEgamma-ElectronIdentification
Requires: data-RecoEgamma-PhotonIdentification
Requires: data-RecoJets-JetProducers
Requires: data-CalibTracker-SiPixelESProducers
Requires: data-CalibCalorimetry-CaloMiscalibTools
Requires: data-CalibPPS-ESProducers
Requires: data-Configuration-Generator
Requires: data-DQM-PhysicsHWW
Requires: data-DQM-SiStripMonitorClient
Requires: data-CondFormats-JetMETObjects
Requires: data-RecoLocalCalo-EcalDeadChannelRecoveryAlgos
Requires: data-RecoHI-HiJetAlgos
Requires: data-GeneratorInterface-EvtGenInterface
Requires: data-MagneticField-Interpolation
Requires: data-RecoBTag-SoftLepton
Requires: data-Calibration-Tools
Requires: data-RecoBTag-SecondaryVertex
Requires: data-HLTrigger-JetMET
Requires: data-EventFilter-L1TRawToDigi
Requires: data-FastSimulation-TrackingRecHitProducer
Requires: data-RecoBTag-Combined
Requires: data-RecoBTag-CTagging
Requires: data-L1Trigger-L1TMuon
Requires: data-L1Trigger-L1TGlobal
Requires: data-L1Trigger-L1THGCal
Requires: data-SLHCUpgradeSimulations-Geometry
Requires: data-CalibTracker-SiStripDCS
Requires: data-SimTracker-SiStripDigitizer
Requires: data-CalibCalorimetry-EcalTrivialCondModules
Requires: data-DataFormats-PatCandidates
Requires: data-SimTransport-HectorProducer
Requires: data-PhysicsTools-NanoAOD
Requires: data-RecoTracker-FinalTrackSelectors
Requires: data-EgammaAnalysis-ElectronTools
Requires: data-DQM-DTMonitorClient
Requires: data-SimTransport-PPSProtonTransport
Requires: data-SimTransport-TotemRPProtonTransportParametrization
Requires: data-FWCore-Modules
Requires: data-IOPool-Input
Requires: data-RecoCTPPS-TotemRPLocal
Requires: data-IOPool-Input
Requires: data-RecoHGCal-TICL
Requires: data-SimG4CMS-HGCalTestBeam
Requires: data-SimPPS-PPSPixelDigiProducer

Requires: data-FastSimulation-MaterialEffects
Requires: data-SimG4CMS-Calo
Requires: data-SimG4CMS-Forward
Requires: data-Validation-Geometry
Requires: data-Fireworks-Geometry
Requires: data-GeneratorInterface-ReggeGribovPartonMCInterface

## INCLUDE cmsswdata