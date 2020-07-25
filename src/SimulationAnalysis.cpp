#include "SimulationAnalysis.h"
#include "ui_SimulationAnalysis.h"
#include <QDir>
#include <QDesktopServices>
#include <QUrl>
#include <QTextEdit>
#include <QTextCodec>
#include <QString>

SimulationAnalysis::SimulationAnalysis(QWidget *parent, QString str) :
    QDialog(parent),
    ui(new Ui::SimulationAnalysis)
{
    ui->setupUi(this);
    DatFile=str;
    ui->LE_datFile->setText(str);
    connect(ui->PB_openscript,SIGNAL(pressed()),this,SLOT(open_script()));
    connect(ui->PB_runAnal,SIGNAL(pressed()),this,SLOT(runAnalysis()));
}

SimulationAnalysis::~SimulationAnalysis()
{
    delete ui;
}


void SimulationAnalysis :: runAnalysis()
{

    QString appPath = QDir::currentPath();
    QDir dir(appPath);
    dir.cdUp();
    QString python_exec= dir.absolutePath();
    QString program = python_exec.append("/python/dsbCount_Upgraded.py");

    QStringList arguments {program,ui->LE_datFile->text()};
    QProcess *p = new QProcess(this);
    p->start("/usr/local/bin/python", arguments);
    p->waitForStarted();
    connect(p, SIGNAL(finished(int, QProcess::ExitStatus)), this, SLOT(itHasFinished(int, QProcess::ExitStatus)));


}

void SimulationAnalysis::itHasFinished(int exitCode, QProcess::ExitStatus exitStatus)
{
    if(exitStatus == QProcess::NormalExit) //The application closed properly (no crash)
    {
        QString appPath = QDir::currentPath();
        QDir dir(appPath);
        dir.cdUp();    
        QString python_exec= dir.absolutePath();
        QString analysis_output = python_exec.append("/python/analysisOutput.txt");
        Print(analysis_output);
    }

}



void SimulationAnalysis :: open_script()
{

    QString appPath = QDir::currentPath();
    QDir dir(appPath);
    dir.cdUp();
    QString python_exec= dir.absolutePath();
    QString py = python_exec.append("/python/dsbCount_Upgraded.py");

    QDesktopServices::openUrl(py);


}


void SimulationAnalysis::Print(const QString& f)
{


    if (QFile::exists(f))
    {
      QFile file(f);
      QTextEdit *editor = new QTextEdit();

      if (file.open(QFile::ReadOnly))
      {
          QByteArray I_data = file.readAll();
          QTextCodec *codec = Qt::codecForHtml(I_data);
          QString text = codec->toUnicode(I_data);
          if (Qt::mightBeRichText(text))
          {
              editor->setHtml(text);
          } else
          {
              text = QString::fromLocal8Bit(I_data);
              editor->setPlainText(text);
              editor->resize(500,500);
              editor->showNormal();

          }
      }
    }




}


void SimulationAnalysis::on_PB_finish_pressed()
{
    this->close();
    emit closeAll();
}
