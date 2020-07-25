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
/// \file pdb4dna.cc
/// \brief Main program of the pdb4dna example



#include "CommandLineParser.hh"
#include "RunAction.hh"

#include <QString>
#include <QDir>

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

using namespace G4DNAPARSER;
CommandLineParser* parser(0);

void Parse(int& argc, char *argv[]);

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......


#include "execSimulation.h"
#include "G4VUserActionInitialization.hh"
#include "G4UIterminal.hh"
#include "G4UItcsh.hh"


execSimulation::execSimulation(QWidget *parent,QString pdb)
{
    out_pdb = pdb;
    interrupted=false;

}

execSimulation :: ~execSimulation()
{



}

void execSimulation :: run()
{

        //////////
        // Parse options given in commandLine
        //

      int argc=3;
      QString mac = "-mac";
      QByteArray ba1 = mac.toLocal8Bit();
      QByteArray ba2 = out_pdb.toLocal8Bit();
      char *argv[3];
      char *c_str1 = ba1.data();
      char *c_str2 = ba2.data();

          argv[0] = c_str1;
          argv[1] = c_str1;
          argv[2] = c_str2;



       Parse(argc, argv);

      // Set the Seed
      CLHEP::RanecuEngine defaultEngine(1234567);
      G4Random::setTheEngine(&defaultEngine);

      // Choose the Random engine
      //
      CLHEP::HepRandom::setTheEngine(new CLHEP::RanecuEngine);

      //////////
      // Construct the run manager according to whether MT is activated or not
      //
      Command* commandLine(0);

    #ifdef G4MULTITHREADED
      G4MTRunManager* runManager= new G4MTRunManager;
      if ((commandLine = parser->GetCommandIfActive("-mt")))
      {
        int nThreads = 4;
        if(commandLine->GetOption() == "NMAX")
        {
         nThreads = G4Threading::G4GetNumberOfCores();
        }
        else
        {
         nThreads = G4UIcommand::ConvertToInt(commandLine->GetOption());
        }
        G4cout << "===== IDDRRA has started with "
           << runManager->GetNumberOfThreads()
           << " threads =====" << G4endl;

        runManager->SetNumberOfThreads(nThreads);
      }
    #else

      runManager = new G4RunManager();

    #endif

      // Set user classes
      //
      runManager->SetUserInitialization(new DetectorConstruction());
      runManager->SetUserInitialization(new PhysicsList);
      actionInit = new ActionInitialization();
      runManager->SetUserInitialization(actionInit);



      // Initialize G4 keRnel
      //
      // runManager->Initialize();


      QString appPath = QDir::currentPath();
      QDir dir(appPath);
      dir.cdUp();
      QString simDir = "/Simulation_input/";
      QString dir_copy =simDir;



      // Initialize visualization
      visManager = new G4VisExecutive;
      visManager->Initialize();

      // Get the pointer to the User Interface manager
    #ifdef _WIN32
       G4UIsession * session = new G4UIterminal();
    #else
       G4UIsession * session = new G4UIterminal(new G4UItcsh);
    #endif
       UImanager = G4UImanager::GetUIpointer();
       G4UIExecutive* ui(0);

      QString command_exec = "/control/execute ";
      QString vis_mac = dir_copy.append("vis.mac");
      command_exec.append(vis_mac);
      QByteArray ba = command_exec.toLocal8Bit();

      dir_copy.clear();

      QString command_exec2 = "/control/execute ";
      dir_copy =simDir;
      QString init_mac = dir_copy.append("init.mac");
      command_exec2.append(init_mac);
      QByteArray baI = command_exec2.toLocal8Bit();

      // interactive mode : define UI session
      if ((commandLine = parser->GetCommandIfActive("-gui")))
      {
        ui = new G4UIExecutive(argc,argv,
                               commandLine->GetOption());

        if(parser->GetCommandIfActive("-novis") == 0)
        // visualization is used by default
        {
          if ((commandLine = parser->GetCommandIfActive("-vis")))
          // select a visualization driver if needed (e.g. HepFile)
          {
            UImanager->ApplyCommand(G4String("/vis/open ")+
                                    commandLine->GetOption());
          }
          else
          // by default OGL is used
          {
            UImanager->ApplyCommand("/vis/open OGLSX 600x600-0+0");
          }

          UImanager->ApplyCommand(ba.data());
        }
        if (ui->IsGUI())
          UImanager->ApplyCommand("/control/execute gui.mac");
      }
      else
      // to be use visualization file (= store the visualization into
      // an external file:
      // ASCIITree ;  DAWNFILE ; HepRepFile ; VRML(1,2)FILE ; gMocrenFile ...
      {
        if ((commandLine = parser->GetCommandIfActive("-vis")))
        {
          UImanager->ApplyCommand(G4String("/vis/open ")+
                                  commandLine->GetOption());
          UImanager->ApplyCommand(ba.data());
        }
      }

      if ((commandLine = parser->GetCommandIfActive("-mac")))
      {

          G4String command = "/control/execute ";
          UImanager->ApplyCommand(command + commandLine->GetOption());
          //session->SessionStart();
          delete session;


      }
      else
      {
        UImanager->ApplyCommand(baI.data());
      }

      if ((commandLine = parser->GetCommandIfActive("-gui")))
      {


    #ifdef G4UI_USE_QT
        G4UIQt* UIQt = static_cast<G4UIQt*> (UImanager->GetG4UIWindow());
        if ( UIQt) {
          UIQt->AddViewerTabFromFile("README", "README from "+ G4String(argv[0]));
        }
    #endif

        ui->SessionStart();
        delete ui;
      }

      // Job termination


     if(!interrupted)
      {
        actionInit->eventAction->endAllEvents();
        outputDat = actionInit->getOutputfile();
        emit completed();
        emit sendOutDat(outputDat);
      }


      delete visManager;


      delete runManager;

      

      emit finished();






}






void execSimulation :: stop()
{


  visManager->Disable();
  G4String cmd = "/control/beamOn 0";
  actionInit->eventAction->endAllEvents();
  UImanager->ApplyCommand(cmd);
  runManager->AbortEvent();
  runManager->AbortRun(true);

  outputDat = actionInit->getOutputfile();
  emit sendOutDat(outputDat);
  interrupted=true;





}


void Parse(int& argc, char** argv)
{
  //////////
  // Parse options given in commandLine
  //
  parser = CommandLineParser::GetParser();

  parser->AddCommand("-gui",
                     Command::OptionNotCompulsory,
                    "Select geant4 UI or just launch a geant4 terminal session",
                    "qt");

  parser->AddCommand("-mac",
                     Command::WithOption,
                     "Give a mac file to execute",
                     ".in");

// You cann your own command, as for instance:
//  parser->AddCommand("-seed",
//                     Command::WithOption,
//                     "Give a seed value in argument to be tested", "seed");
// it is then up to you to manage this option

#ifdef G4MULTITHREADED
  parser->AddCommand("-mt", Command::WithOption,
                     "Launch in MT mode (events computed in parallel)",
                     "2");
#endif

  parser->AddCommand("-vis",
                     Command::WithOption,
                     "Select a visualization driver",
                     "OGLSX 600x600-0+0");

  parser->AddCommand("-novis",
                     Command::WithoutOption,
                     "Deactivate visualization when using GUI");

  //////////
  // If -h or --help is given in option : print help and exit
  //
  if (parser->Parse(argc, argv) != 0) // help is being printed
  {
    // if you are using ROOT, create a TApplication in this condition in order
    // to print the help from ROOT as well
    CommandLineParser::DeleteInstance();
    std::exit(0);
  }

  ///////////
  // Kill application if wrong argument in command line
  //
  if (parser->CheckIfNotHandledOptionsExists(argc, argv))
  {
    // if you are using ROOT, you should initialise your TApplication
    // before this condition
    abort();
  }
}
