
/**
 *  @file   SimulationInput.h
 *  @brief  User Parameters For Simulation
 *  @author Afroditi Toufa
 *  @date   2020-07-09
 ***********************************************/

#ifndef SIMULATIONINPUT_H
#define SIMULATIONINPUT_H

#include <QDialog>
#include "RunSimulation.h"
#include <QCloseEvent>

namespace Ui {
class SimulationInput;
}

class SimulationInput : public QDialog
{
    Q_OBJECT



public:
    /**
     * @brief class constructor
     * @param QWidget parent
     */
    explicit SimulationInput(QWidget *parent = nullptr);
    ~SimulationInput();
    QString filename;
    RunSimulation *simulatuion;
    QString inputFilename;
    /**
     * @brief holds the dnaDesign.py output file name
     */
    QString python_pdb;
    /**
     * @brief Stores dnaDesign.py output file to the @p python_pdb public string
     * @param dnaDesign.py output file name
     */
    void Init(QString st);


signals:
void closeEverything();

public slots:
/**
  * @brief Proceed to the Simulation dialog
  */
 void next();
 /**
  * @brief Closes the current dialog
  */
 void previous();

protected:
 /**
  * @brief Closes the dailog and delete pointers
  */
 void closeEvent(QCloseEvent *);



private slots:
 /**
     * @brief Loads the init.mac file with simulation's parameters and edit it to the dnaDesign.py script output file
     * as a parameter and loads it to a text editor
     */
    void load_file();
    /**
     * @brief Add the dnaDesing python script's output as a parameter in the init.mac file
     */
    void edit_mac_file();
    /**
     * @brief Save the init file's changes made in the editor
     */
    void fileSave();
private:
    /**
     * @brief Sets loaded .mac filename
     * @param name
     */
    void setCurrentFileName(const QString &fileName);
    /**
     * @brief Load simulation's init.mac file to a text editor for editing purposes
     * @param filename
     * @return
     */
    bool load(const QString &f);
    Ui::SimulationInput *ui;
};

#endif // SIMULATIONINPUT_H
