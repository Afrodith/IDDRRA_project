//QT related//
#include <QApplication>
#include <QDir>
#include <QProcess>
#include "Mainwindow.h"



int main(int argc,char *argv[])
{

    QApplication a(argc, argv);



    Mainwindow mainwindow;

    QString appPath = QDir::currentPath();
    QDir dir(appPath);
    dir.cdUp();
    if(!QDir("Simulation_output").exists())
        dir.mkdir("Simulation_output");

    mainwindow.show();



 // return 0;
  return a.exec();
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo.....


