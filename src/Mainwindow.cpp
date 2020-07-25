#include "Mainwindow.h"
#include "ui_Mainwindow.h"
#include <QGraphicsScene>
#include <QTextEdit>
#include <QProcess>
#include <QFile>
#include <QFileInfo>
#include <QTextCodec>
#include <QByteArray>
#include <QTextDocumentWriter>
#include <QFileDialog>
#include <QString>
#include <QMessageBox>
#include <QResource>
#include <QDebug>
#include <QDir>
#include <QStandardPaths>
#include <QDesktopServices>



Mainwindow::Mainwindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Mainwindow)
{
    ui->setupUi(this);
    this->layout()->setSizeConstraint(QLayout::SetFixedSize);
    this->setFixedSize(this->width(), this->height());

    ui->PB_onlyAnalysis->setEnabled(true);

    sim_input = NULL;
    dnaAnalysis = NULL;

    QPixmap image_red = QPixmap::fromImage(QImage(":/icons/iddra1.jpg"));

    QGraphicsScene* scene1= new QGraphicsScene(ui->GV_image);
    scene1->addPixmap(image_red);
    scene1->setSceneRect(image_red.rect());

    ui->GV_image->setGeometry(image_red.rect());
    ui->GV_image->setScene(scene1);

    ui->GV_image->show();
    connect(ui->PB_runDNA_Design,SIGNAL(released()),this,SLOT(run_dnaDesign()));
    connect(ui->PB_nxt,SIGNAL(pressed()),this,SLOT(proceed()),Qt::UniqueConnection);
    connect(ui->PB_onlyAnalysis,SIGNAL(pressed()),this,SLOT(DNA_analysis()));
    connect(ui->PB_openScript,SIGNAL(pressed()),this,SLOT(open_script()));
    connect(ui->PB_cancel,SIGNAL(pressed()),this,SLOT(on_PB_cancel_pressed()));
    //ui->PB_nxt->setEnabled(false);


}

Mainwindow::~Mainwindow()
{

     delete ui;
}

void Mainwindow :: closeEvent(QCloseEvent *event)
{
  if(sim_input!=NULL)
  {
    delete sim_input;
    sim_input=NULL;
    delete dnaAnalysis;
    dnaAnalysis=NULL;
  }

  event->accept();
}

void Mainwindow::run_dnaDesign()
{

pdb_out.clear();
QString appPath = QDir::currentPath();
QDir dir(appPath);
dir.cdUp();
QString python_exec= dir.absolutePath();
QString program = python_exec.append("/python/DNAdesign.py");

QStringList arguments {program, ui->LE_pyOutput->text()+ext};
QProcess *p = new QProcess(this);
p->start("/usr/local/bin/python", arguments);
connect(p, SIGNAL(finished(int, QProcess::ExitStatus)), this, SLOT(itHasFinished(int, QProcess::ExitStatus)));
connect(p, SIGNAL(started()),this,SLOT(proc_started()));

ui->PB_runDNA_Design->setEnabled(false);

ui->progressBar->setValue(0);
ui->progressBar->setMaximum(100);



}


void Mainwindow :: open_script()
{
    QString appPath = QDir::currentPath();
    QDir dir(appPath);
    dir.cdUp();
    QString python_exec= dir.absolutePath();
    QString program = python_exec.append("/python/DNAdesign.py");

    QDesktopServices::openUrl(program);


}


void Mainwindow :: increment_progressBar()
{

    incr++;
    if(ui->progressBar->maximum() <= incr)
    {
        ui->progressBar->setMaximum(0);
    }

    ui->progressBar->setValue(incr);


}

void Mainwindow :: proc_started()
{

    timer = new QTimer(this);
    timer->start(1000);
    connect(timer,SIGNAL(timeout()),this,SLOT(increment_progressBar()));

}

void Mainwindow::itHasFinished(int exitcode, QProcess::ExitStatus exitStatus)
{
    if(exitStatus == QProcess::NormalExit) //The application closed properly (no crash)
    {
        //Let's make progress bar to show 100%
        ui->PB_runDNA_Design->setEnabled(true);
        ui->PB_nxt->setEnabled(true);
        timer->stop();
        incr=0;
        ui->progressBar->setMaximum(1);
        ui->progressBar->setMinimum(0);
        ui->progressBar->setValue(1);
        delete timer;

        pdb_out = ui->LE_pyOutput->text()+ext;

        QString appPath = QDir::currentPath();
        QDir dir(appPath);
        dir.cdUp();
        QString python_exec= dir.absolutePath();

        QString text_output = python_exec.append("/python/printOutput.txt");
        Print(text_output);

    }

}

void Mainwindow::Print(const QString& f)
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

void Mainwindow :: proceed()
{

    QString appPath = QDir::currentPath();
    QDir dir(appPath);
    dir.cdUp();
    QString python_output = dir.absolutePath().append("/python/"+pdb_out);

    if(sim_input==NULL)
    {
    sim_input = new SimulationInput(this);
    sim_input->Init(python_output);
    connect(sim_input,SIGNAL(closeEverything()),this,SLOT(close()));
    sim_input->show();
    }




}





void Mainwindow::on_PB_cancel_pressed()
{
    this->close();
}

void Mainwindow::on_PB_editDatFile_pressed()
{
    QString appPath = QDir::currentPath();
    QDir dir(appPath);
    dir.cdUp();
    QString python_dat = dir.absolutePath().append("/python/dnaBasesSequence.dat");
    QDesktopServices::openUrl(python_dat);


}

void Mainwindow :: datFile(QString str)
{
    dat = str;

}

void Mainwindow :: DNA_analysis()
{

    if(dnaAnalysis==NULL)
    {
        QString appPath = QDir::currentPath();
        QDir dir(appPath);
        dir.cdUp();
        dat = dir.absolutePath().append("/Simulation_output/strandDamage_0.dat");
        dnaAnalysis = new SimulationAnalysis(this,dat);
        connect(dnaAnalysis,SIGNAL(closeAll()),this,SIGNAL(closeProgram()));
        dnaAnalysis->show();
    }


}
