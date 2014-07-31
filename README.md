Introduction
============

This package provides a modified version of the MVA MET producer which is designed to calculate an MVA MET object for each possible pairing of the input lepton collections. This is in contrast to the official producer which treats all electrons, muons and taus passing a default selection as the lepton inputs to the algorithm.

Due to minor compatibility issues, separate branches are provided in this package: `4_2_X` and `5_3_X` for the respective release series. The `5_3_X` branch will be checked out by default when cloning this repository.

**Important:** This package is not expected to compile or run under a default CMSSW release, as updates to several other packages are also required. Please consult the ICHiggsTauTau [documentation](http://agilbert.web.cern.ch/agilbert/analysis/index.html), in the section *Physics Objects* for instructions on setting up a CMSSW release for the MVA MET computation as well as example python configurations.