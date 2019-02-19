#ifndef DijetSkimmer_h
#define DijetSkimmer_h

#include <iostream>
#include <vector>
#include <map>

#include "TString.h"

#include "PhysicsTools/DijetSkimmer/interface/NanoAODBase.h"
#include "PhysicsTools/DijetSkimmer/interface/Enums.h"

class DijetSkimmer : public NanoAODBase {
public:
	DijetSkimmer();
	~DijetSkimmer();

	void	 Begin(TTree *tree);
	Bool_t   Process(Long64_t entry);
	void	 Terminate();

	inline void SetYear(int year) {
		if (year == 2016) {
			_year = k2016;
		} else if (year == 2017) {
			_year = k2017;
		} else if (year = 2018) {
			_year = k2018;
		} else {
			std::cerr << "[DijetSkimmer::SetYear] ERROR : Unknown year " << year << std::endl;
			exit(1);
		}
	}

	inline void SetSource(TString& source) {
		TString source_lower = source.ToLower();
		if (source_lower == "data") {
			_source = kDATA;
		} else if (source_lower == "mc") {
			source = kMC;
		} else {
			std::cerr << "[DijetSkimmer::SetSource] ERROR : Unknown source " << source << std::endl;
			exit(1);
		}
	}

public:
	TString _gt;

};