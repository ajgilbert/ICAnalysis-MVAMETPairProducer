import FWCore.ParameterSet.Config as cms

from RecoMET.METPUSubtraction.mvaPFMET_cff    import *

mvaMetPairs = cms.EDProducer("CommonMVAMETPairProducer", **pfMVAMEt.parameters_())
