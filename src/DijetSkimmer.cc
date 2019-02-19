#ifndef DijetSkimmer_cxx
#define DijetSkimmer_cxx

DijetSkimmer::DijetSkimmer() : NanoAODBase() {
	_gt = "AUTO";
}

void DijetSkimmer::Begin(TTree *tree) {
	// Set GT
	if (_gt == "AUTO") {
		if (_source == kMC) {
			if (_year == k2016) {
				_gt = "Summer16_07Aug2017_V11_MC";
			} else if (_year == k2017) {
				_gt = "Fall17_17Nov2017_V32_MC";
			} else if (_year == k2018) {
				_gt = "Autumn18_V2_MC";
			}
		} else if (_source == kDATA) {
			if (_year == k2016) {
				_gt = "Summer16_07Aug2017_V11";
			} else if (_year == k2017) {
				_gt == "Fall17_17Nov2017_V32";
			} else if (_year == k2018) {
				_gt = "";
			}
		}
	}
}

Bool_t DijetSkimmer::Process(Long64_t entry) {
   fReader.SetEntry(entry);

}

void DijetSkimmer::Terminate() {

}


#endif