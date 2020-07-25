//  *********************************************************************
//  * DISCLAIMER                                                        *
//  *                                                                   *
//  * Neither the authors of this software system, nor their employing  *
//  * institutes, nor the agencies providing financial support for this *
//  * work  make  any representation or  warranty, express or implied,  *
//  * regarding  this  software system or assume any liability for its  *
//  * use.                                                              *
//  *                                                                   *
//  *                                                                   *
//  * By copying,  distributing  or modifying the Program (or any work  *
//  * based  on  the Program)  you indicate  your  acceptance of  this  *
//  * statement, and all its terms.                                     *
//  *********************************************************************
//
//######################################################################################
//# Authors   : Konstantinos Chatzipapas                                               # 
//#                                                                                    #
//# Program   : txtProjToAscii.c  25-MAY-2017                                          # 
//#                                                                                    #   
//# Objective : To read the SPECT projections (.txt datafiles), and generates          #
//#             a pair of ascii files (a header file .Cdh and a data file .Cdf.        #
//#                                                                                    #
//# Input     : Datafiles (*.txt) obtained with randy SPECT scanner at Demokritos.     #
//#                                                                                    #
//# Output    : A pair of ascii files (a header file .Cdh and a data file .Cdf.        #
//#           : The files can be used as an input to CASToR program  ./castor-recon    # 
//#                                                                                    #
//#                                                                                    #
//######################################################################################
//
/// \file EventAction.cc
/// \brief Implementation of the EventAction class

#include "EventAction.hh"

#include "Analysis.hh"
#include "EventActionMessenger.hh"
#include "G4Event.hh"
#include "G4UnitsTable.hh"
#include "G4SystemOfUnits.hh"
#include "Randomize.hh"

#include <algorithm>

#include <iostream>
#include <fstream>

//using namespace std;

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......




bool fileExists(const std::string& filename)
{
    struct stat buf;
    if (stat(filename.c_str(), &buf) != -1)
    {
        return true;
    }
    return false;
}



EventAction::EventAction():G4UserEventAction()
{
  //default parameter values
  //
  fThresEdepForSSB=18*eV;
  fThresDistForDSB=10;
  fTotalEnergyDeposit=0;

  //create commands
  //
  fpEventMessenger = new EventActionMessenger(this);



  // Open an output file
  //
  G4String pre = "strandDamage_";
  G4String filename,nb;

  QString appPath = QDir::currentPath();
  QDir dir(appPath);
  dir.cdUp();
  QString output_dir= dir.absolutePath();
  QString exp = output_dir.append("/Simulation_output/");

  G4String loc = exp.toStdString();

  /////////////////////////////////////////////////////////////////////////////////////////////

  for( int k=0; k < 103; k++ ) {

    nb = std::to_string(k);
    filename = pre + nb + ".dat";
    outputFile = loc +filename;
    if(!fileExists(outputFile))
      break;

   }

   outFile.open(outputFile);



}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

EventAction::~EventAction()
{
  delete fpEventMessenger;
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void EventAction::BeginOfEventAction( const G4Event*)
{
  // Initialization of parameters
  //
  fTotalEnergyDeposit=0.;
  fEdepStrand1.clear();
  fEdepStrand2.clear();




}


void EventAction::endAllEvents()
{


    fTotalEnergyDeposit=0.;
    fEdepStrand1.clear();
    fEdepStrand2.clear();
    if(outFile.is_open())
      outFile.close();


}


QString EventAction :: datOutputFile()
{
    return QString::fromStdString(outputFile).toLocal8Bit();

}



//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void EventAction::EndOfEventAction( const G4Event*)
{
  // At the end of an event, compute the number of strand breaks
  //
  G4int sb[3] = {0,0,0};
  ComputeStrandBreaks(sb);
  // Fill histograms
  //

/*
  G4AnalysisManager* analysisManager = G4AnalysisManager::Instance();

  if ( fTotalEnergyDeposit>0. )
  {
    analysisManager->FillH1(1,fTotalEnergyDeposit);
  }
  if ( sb[0]>0 )
  {
    analysisManager->FillH1(2,sb[0]);
  }
  if ( sb[1]>0 )
  {
    analysisManager->FillH1(3,sb[1]);
  }
  if ( sb[2]>0 )
  {
    analysisManager->FillH1(4,sb[2]);
  }
*/
  

  
  
  for (auto elem1 : fEdepStrand1)
  {
    G4cout << "A " << elem1.first << " " << elem1.second << G4endl;
    outFile.open(outputFile, std::ios::app);
    outFile << "A " << elem1.first << " " << elem1.second << G4endl;
    outFile.close();
    //analysisManager->FillH2(1,elem1.first,elem1.second);

  }
  for (auto elem2 : fEdepStrand2)
  {
    G4cout << "B " << elem2.first << " " << elem2.second << G4endl;
    outFile.open(outputFile, std::ios::app);
    outFile << "B " << elem2.first << " " << elem2.second << G4endl;
    outFile.close();
    //analysisManager->FillH2(2,elem2.first,elem2.second);
  }
  //fclose(pFile);
  //outFile.close();
  
  
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void EventAction::ComputeStrandBreaks(G4int* sb)
{
  // sb quantities
  //
  G4int ssb1=0;
  G4int ssb2=0;
  G4int dsb=0;
  G4int cds=0;

  // nucleotide id and energy deposit for each strand
  G4int nucl1;
  G4int nucl2;
  G4int nucl3;
  G4int nucl4;
  G4int nucl5;
  G4int nucl6;
  G4double edep1;
  G4double edep2;
  G4double edep3;
  G4double edep4;
  G4double edep5;
  G4double edep6;

  for(it2 = fEdepStrand2.begin(); it2 != fEdepStrand2.end(); it2++)
  {
    nucl2 = it2->first;
    edep2 = it2->second;
    //G4cout << "compute" << fEdepStrand2;
    
    if ( edep2 >= fThresEdepForSSB/eV )
    {
      ssb2++;
      //G4cout << "SSB	n2=	" << nucl2 << "	e2=	" << edep2 << G4endl;
    }
  }
        
  for(it1 = fEdepStrand1.begin(); it1 != fEdepStrand1.end(); it1++)
  {
    nucl1 = it1->first;
    edep1 = it1->second;
    //std::cout << "compute" << fEdepStrand1;
    //G4cout << "check   n1= " << nucl1 << "  e1= " << edep1 << G4endl;
    
    if ( edep1 >= fThresEdepForSSB/eV )
    {
      ssb1++;
      //G4cout << "SSB	n1=	" << nucl1 << "	e1=	" << edep1 << G4endl;
      
      for(it7 = fEdepStrand2.begin(); it7 != fEdepStrand2.end(); it7++)
      {
	nucl2 = it7->first;
	edep2 = it7->second;
	//G4cout << "check DSB   n1= " << nucl1 << "  e1= " << edep1 << "  n2= " << nucl2 << "  e2= " << edep2 << G4endl;
	
	if ( edep2 >= fThresEdepForSSB/eV )
	{  
	  if ( std::abs(nucl1-nucl2)<fThresDistForDSB )
	  {
	    G4cout << "DSB   n1= " << nucl1 << "  e1= " << edep1 << "  n2= " << nucl2 << "  e2= " << edep2 << G4endl;
	    dsb++;
	    ssb1--;
	    ssb2--;
	  }
	}
      }
    }
  }
  
//

  for(it3 = fEdepStrand1.begin(); it3 != fEdepStrand1.end(); it3++)
  {
    nucl3 = it3->first;
    edep3 = it3->second;
    //std::cout << "compute" << fEdepStrand1;
    
    if ( edep3 >= fThresEdepForSSB/eV )
    {
      
      for(it4 = fEdepStrand1.begin(); it4 != fEdepStrand1.end(); it4++)
      {
	nucl4 = it4->first;
	edep4 = it4->second;
	
	if ( edep4 >= fThresEdepForSSB/eV )
	{  
	  if ( ( std::abs(nucl3-nucl4)<fThresDistForDSB ) && ( std::abs(nucl3-nucl4)>0 ) )
	  {
	    cds++;
	  }
	}
      }
    }
  }

  for(it5 = fEdepStrand2.begin(); it5 != fEdepStrand2.end(); it5++)
  {
    nucl5 = it5->first;
    edep5 = it5->second;
    //std::cout << "compute" << fEdepStrand1;
    
    if ( edep5 >= fThresEdepForSSB/eV )
    {
      
      for(it6 = fEdepStrand2.begin(); it6 != fEdepStrand2.end(); it6++)
      {
	nucl6 = it6->first;
	edep6 = it6->second;
	
	if ( edep6 >= fThresEdepForSSB/eV )
	{  
	  if ( ( std::abs(nucl5-nucl6)<fThresDistForDSB ) && ( std::abs(nucl5-nucl6)>0 ) )
	  {
	    cds++;
	  }
	}
      }
    }
  }

  
//
  
    //fEdepStrand1.erase( fEdepStrand1.begin(), fEdepStrand1.end());
    //fEdepStrand2.erase( fEdepStrand2.begin(), fEdepStrand2.end());
    
    sb[0]=ssb1+ssb2;
    sb[1]=dsb;
    
    //
    sb[2]=cds;
    //
}
