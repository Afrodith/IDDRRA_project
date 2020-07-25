//
// ********************************************************************
// * License and Disclaimer                                           *
// *                                                                  *
// * The  Geant4 software  is  copyright of the Copyright Holders  of *
// * the Geant4 Collaboration.  It is provided  under  the terms  and *
// * conditions of the Geant4 Software License,  included in the file *
// * LICENSE and available at  http://cern.ch/geant4/license .  These *
// * include a list of copyright holders.                             *
// *                                                                  *
// * Neither the authors of this software system, nor their employing *
// * institutes,nor the agencies providing financial support for this *
// * work  make  any representation or  warranty, express or implied, *
// * regarding  this  software system or assume any liability for its *
// * use.  Please see the license in the file  LICENSE  and URL above *
// * for the full disclaimer and the limitation of liability.         *
// *                                                                  *
// * This  code  implementation is the result of  the  scientific and *
// * technical work of the GEANT4 collaboration.                      *
// * By using,  copying,  modifying or  distributing the software (or *
// * any work based  on the software)  you  agree  to acknowledge its *
// * use  in  resulting  scientific  publications,  and indicate your *
// * acceptance of all terms of the Geant4 Software license.          *
// ********************************************************************
//
// This example is provided by the Geant4-DNA collaboration
// Any report or published results obtained using the Geant4-DNA software
// shall cite the following Geant4-DNA collaboration publication:
// Med. Phys. 37 (2010) 4692-4708
// Delage et al. PDB4DNA: implementation of DNA geometry from the Protein Data
//                  Bank (PDB) description for Geant4-DNA Monte-Carlo
//                  simulations (submitted to Comput. Phys. Commun.)
// The Geant4-DNA web site is available at http://geant4-dna.org
//
// $Id$
//
/// \file RunAction.cc
/// \brief Implementation of the RunAction class

#include "RunAction.hh"
#include "RunInitObserver.hh"
#include <string> 
#include <fstream>

#include "Analysis.hh"
#include "G4Run.hh"
#include "G4UnitsTable.hh"

//qt related
#include <QString>
#include <QDir>

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

RunAction::RunAction() : G4UserRunAction()
{
/*
  G4AnalysisManager* analysisManager = G4AnalysisManager::Instance();
  analysisManager->SetFirstHistoId(1);

  // Creating histograms
  //
  analysisManager->CreateH1("1",
                            "Energy deposit in the target (MeV)",
                            1000,0.,1000.);
  analysisManager->CreateH1("2",
                            "Number of SSB",
                            10,0.,10.);
  analysisManager->CreateH1("3",
                            "Number of DSB",
                            10,0.,10.);
  analysisManager->CreateH1("4",
                            "Number of CDS",
                            10,0.,10.);
  analysisManager->CreateH2("strandA",
                            "Position of events on strand A",
                            10000,0.,10000,
			    100,0.,100,
			    "none",
			    "eV");
  analysisManager->CreateH2("strandB",
                            "Position of events on strand B",
                            10000,0.,10000,
			    100,0.,100,
			    "none",
			    "eV");


  
  // Open an output file
  //
  G4String filename = "IDDRRA_output_";
  int k=0;
  G4String s = std::to_string(k);
  G4String fileName = filename + s + ".root";

  QString appPath = QDir::currentPath();
  QDir dir(appPath);
  dir.cdUp();
  QString output_dir= dir.absolutePath();
  QString exp = output_dir.append("/Simulation_output/");

  G4String loc = exp.toStdString();
  outputFile = loc + fileName;

  /////////////////////////////////////////////////////////////////////////////////////////////

  for( k=0; k < 103; k++ ) {

    s = std::to_string(k);
    fileName = filename + s + ".root";
    outputFile = loc + fileName;
    std::ifstream file(outputFile);
    if (!file)
      break;

   }
  
  
  analysisManager->OpenFile(outputFile);
  // G4String extension = analysisManager->GetFileType();
  /////////////////////////////////////////////////////////////////////////////////////////////
    
  G4cout << "\n----> Histogram file is opened in " << fileName << G4endl;
*/
}
/*
QString RunAction :: rootOutputFile()
{
    return QString::fromStdString(outputFile);

}
*/

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

RunAction::~RunAction()
{
/*
  G4AnalysisManager* analysisManager = G4AnalysisManager::Instance();
  analysisManager->CloseFile();

  delete G4AnalysisManager::Instance();
*/
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void RunAction::BeginOfRunAction(const G4Run*)
{
  RunInitManager::Instance()->Initialize();
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void RunAction::EndOfRunAction(const G4Run*)
{
  //G4AnalysisManager* analysisManager = G4AnalysisManager::Instance();
  // save histograms 
  //
  //analysisManager->Write();
}

