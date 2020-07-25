#include "RunSimulation.h"
#include "ui_RunSimulation.h"
#include <QFile>
#include <QFileInfo>
#include <QTextCodec>
#include <QTextDocumentWriter>
#include <QFileDialog>
#include <QMessageBox>

RunSimulation::RunSimulation(QWidget *parent,QString str) :
    QDialog(parent),
    ui(new Ui::RunSimulation)
{
    ui->setupUi(this);
    dnaIn = str;
    ui->LE_file->setText(str);
    ui->PB_proceed->setEnabled(false);
    dnaAnalysis=NULL;
    worker=NULL;
    thread=NULL;
    timer=NULL;


    connect(ui->PB_previous,SIGNAL(released()),this,SLOT(previous()),Qt::UniqueConnection);
    connect(ui->PB_run,SIGNAL(pressed()),this,SLOT(startSim()));
    connect(ui->PB_stop,SIGNAL(pressed()),this,SLOT(stopSim()));
    connect(ui->PB_proceed,SIGNAL(released()),this,SLOT(DNA_analysis()));
    connect(this,SIGNAL(closeProgram()),this,SLOT(close()));

}



RunSimulation::~RunSimulation()
{

    delete ui;

}

void RunSimulation::closeEvent(QCloseEvent *event)
{

    if(dnaAnalysis!=NULL)
    {
        delete dnaAnalysis;
        dnaAnalysis=NULL;
    }

    event->accept();
}


void RunSimulation :: deleteThread()
{


    delete worker;
    delete thread;


}


void RunSimulation :: startSim(){

//    QTimer *timeServer = new QTimer();
//    timeServer->setInterval(0);
    worker = new execSimulation(this,dnaIn);
    thread= new QThread();


    connect(thread,SIGNAL(started()),worker,SLOT(run()));

    connect(worker,SIGNAL(completed()),this,SLOT(simulationFinished()));
    connect(this,SIGNAL(stopSimulation()),worker,SLOT(stop()),Qt::DirectConnection);
    connect(worker,SIGNAL(finished()),this,SLOT(completed()));
    connect(worker,SIGNAL(sendOutDat(QString)),this,SLOT(datFile(QString)));


    connect(worker,SIGNAL(finished()),thread,SLOT(quit()));
    connect(thread,SIGNAL(finished()),this,SLOT(deleteThread()));


    worker->moveToThread(thread);



    thread->start(QThread::TimeCriticalPriority);
    ui->PB_run->setEnabled(false);
    ui->progressBar->setValue(0);
    ui->progressBar->setMaximum(100);
    timer = new QTimer(this);
    timer->start(1000);
    connect(timer,SIGNAL(timeout()),this,SLOT(incr_progressBar()));


}


void RunSimulation :: incr_progressBar()
{

    count++;
    if(ui->progressBar->maximum() <= count)
    {
        ui->progressBar->setMaximum(0);
    }
    ui->progressBar->setValue(count);




}


void RunSimulation::previous()
{

    this->close();

}




void RunSimulation :: completed()
{
    ui->LE_output->setText(dat);
    ui->PB_proceed->setEnabled(true);

}

void RunSimulation :: stopSim()
{

    timer->stop();
    count=0;
    ui->progressBar->setMaximum(1);
    ui->progressBar->setMinimum(0);
    ui->progressBar->setValue(1);
    delete timer;
    emit stopSimulation();
    ui->PB_stop->setEnabled(false);


}

void RunSimulation :: simulationFinished()
{


    timer->stop();
    count=0;
    ui->progressBar->setMaximum(1);
    ui->progressBar->setMinimum(0);
    ui->progressBar->setValue(1);
    delete timer;
    ui->PB_stop->setEnabled(false);

}


void RunSimulation :: datFile(QString str)
{
    dat = str;

}



void RunSimulation :: DNA_analysis()
{

    if(dnaAnalysis==NULL)
    {
        dnaAnalysis = new SimulationAnalysis(this,dat);
        connect(dnaAnalysis,SIGNAL(closeAll()),this,SIGNAL(closeProgram()));
        dnaAnalysis->show();
    }


}
