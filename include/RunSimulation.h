/**
 *  @file   RunSimulation.h
 *  @brief  Simulation runnig thread
 *  @author Afroditi Toufa
 *  @date   2020-07-09
 ***********************************************/


#ifndef RUNSIMULATION_H
#define RUNSIMULATION_H

#include <QDialog>
#include <QThread>
#include "execSimulation.h"
#include "SimulationAnalysis.h"
#include <QTimer>
#include <QCloseEvent>

namespace Ui {
class RunSimulation;
}

class RunSimulation : public QDialog
{
    Q_OBJECT

public:
    /**
     * @brief class constructor
     * @param QWidget parent
     * @param .mac filename
     */
    explicit RunSimulation(QWidget *parent = nullptr,QString str="");
    ~RunSimulation();
    /**
     * @brief public string that holds the .mac filename
     */
    QString dnaIn;
    /**
     * @brief Thread wrapper
     */
    QThread *thread;
    /**
     * @brief simulation execution pointer
     */
    execSimulation *worker;
    /**
     * @brief String that holds the generated .dat file from the simulation
     */
    QString dat;
    /**
     * @brief SimulationAnalysis dialog pointer
     */
    SimulationAnalysis *dnaAnalysis;
    /**
     * @brief timer utility that starts the execution in the separate thread
     */
    QTimer *timer;
    /**
     * @brief Progressbar incrementation
     */
    int count=0;



signals:
    /**
   * @brief signal to stop the running simulation
   */
  void stopSimulation();
  /**
   * @brief Signal that closes the dialog and clean reserved memory
   */
  void closeProgram();

public slots:
  /**
   * @brief Construct the thread and move the execution of the simulation to it in order to run in parallel.
   * Set the commmunication of the main thread and seprate thread and starts the execution process.
   */
  void startSim();
  /**
   * @brief Kills the execution of the simulation in the seprate thread when is manually selected by the user.
   * Clears and resets the timer and progressbar
   */
  void stopSim();
  /**
   * @brief When the simulation is finished, writes the output file name in a line edit and enables the user to
   * proceed in the Simulation Analysis dialog.
   */
  void completed();
  /**
   * @brief Closes the current dialog
   */
  void previous();
  /**
   * @brief Gets the name of the simulation's generated .dat file
   */
  void datFile(QString);
  /**
   * @brief Open the analysis dialog when the execution of the simulation is finished and load the output .dat file
   */
  void DNA_analysis();
  /**
   * @brief Increment the progressbar as the simulation is running
   */
  void incr_progressBar(); 
  /**
   * @brief Is called by the separate thead when the execution of the simulation is finished uninterrupted.
   * Clears and resets the timer and progressbar
   */
  void simulationFinished();

protected:
  /**
  * @brief Closes the dialog and deletes pointers
  */
 void closeEvent(QCloseEvent *);

private slots:
 /**
   * @brief deletes thread and pointer
   */
  void deleteThread();


private:

    Ui::RunSimulation *ui;
};

#endif // RUNSIMULATION_H
