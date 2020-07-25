#ifndef EXECSIMULATION_H
#define EXECSIMULATION_H

#include <QObject>

#include "DetectorConstruction.hh"
#include "PhysicsList.hh"
#include "ActionInitialization.hh"

#ifdef G4MULTITHREADED
#include "G4MTRunManager.hh"
#else
#include "G4RunManager.hh"
#endif

#include "G4UImanager.hh"
#include "Randomize.hh"
#include "G4VisExecutive.hh"
#include "G4UIExecutive.hh"
#include "G4UIQt.hh"




class execSimulation : public QObject
{
    Q_OBJECT
public:
    execSimulation(QWidget *parent, QString pdb="");
    ~execSimulation();
    QString out_pdb;
    QString outputDat;

    G4VisManager* visManager;
    G4RunManager* runManager;
    G4UImanager* UImanager;
    ActionInitialization * actionInit;



signals:

  void finished();
  void sendOutDat(QString);
  void completed();


public slots:
    void run();
    void stop();

private:

bool interrupted;



};

#endif // EXECSIMULATION_H
