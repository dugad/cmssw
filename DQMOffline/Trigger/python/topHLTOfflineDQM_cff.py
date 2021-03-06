import FWCore.ParameterSet.Config as cms

from DQMOffline.Trigger.topDiLeptonHLTEventDQM_cfi import *
from DQMOffline.Trigger.topSingleLeptonHLTEventDQM_cfi import *
from DQMOffline.Trigger.singletopHLTEventDQM_cfi import *
from JetMETCorrections.Configuration.JetCorrectionProducersAllAlgos_cff import *



topHLTriggerOfflineDQM = cms.Sequence(  
        DiMuonHLTOfflineDQM
        *DiElectronHLTOfflineDQM
        *ElecMuonHLTOfflineDQM
        *topSingleMuonHLTOfflineDQM
        *topSingleElectronHLTOfflineDQM
        *SingleTopSingleMuonHLTOfflineDQM
        *SingleTopSingleElectronHLTOfflineDQM	
        )

