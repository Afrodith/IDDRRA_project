#include "SimulationInput.h"
#include "ui_SimulationInput.h"
#include "QFileDialog"
#include "QFile"
#include "QMessageBox"
#include "QDir"
#include "QProcess"
#include <QFile>
#include <QFileInfo>
#include <QTextCodec>
#include <QTextDocumentWriter>
#include <QFileDialog>
#include <QMessageBox>
#include <QTextStream>

SimulationInput::SimulationInput(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::SimulationInput)
{
    ui->setupUi(this);

    simulatuion=NULL;

    connect(ui->PB_next,SIGNAL(released()),SLOT(next()),Qt::UniqueConnection);
    connect(ui->PB_load,SIGNAL(pressed()),SLOT(load_file()),Qt::UniqueConnection);
    connect(ui->PB_save,SIGNAL(pressed()),this,SLOT(fileSave()));
    connect(ui->PB_previous,SIGNAL(released()),this,SLOT(previous()),Qt::UniqueConnection);
    connect(this,SIGNAL(closeEverything()),this,SLOT(close()));
    python_pdb.clear();


}

SimulationInput::~SimulationInput()
{

    delete ui;
}


void SimulationInput ::closeEvent(QCloseEvent *event)
{

    if(simulatuion!=NULL)
    {
       delete simulatuion;
       simulatuion=NULL;
    }

    event->accept();


}


void SimulationInput :: previous()
{

    this->close();
}

void SimulationInput :: Init(QString st)
{


   python_pdb = st;


}

void SimulationInput::load_file()
 {

    QString appPath = QDir::currentPath();
    QDir dir(appPath);
    dir.cdUp();
    filename = QFileDialog::getOpenFileName(this,tr("Open File"), dir.absolutePath(), tr("Mac Files (*.in)"));
    if (filename.isEmpty())
        return;
    else {


        ui->LE_input->setText(filename);
        edit_mac_file();
        load(filename);


    }


}



void SimulationInput::edit_mac_file()
{


    QFile file(filename);

    if (!file.open(QIODevice::ReadOnly)) {
        QMessageBox::information(this, tr("Unable to open file"),
                                 file.errorString());
        return;
    }
    QTextStream in (&file);
    QByteArray bArr;
    QString line;
    QString copy = python_pdb;
    QString searchString = "/PDB4DNA/det/loadPDB";

    do {
        line = in.readLine();
        if (line.startsWith("/PDB4DNA/det/loadPDB")){
            line = "/PDB4DNA/det/loadPDB  "+python_pdb;
        }
        
       bArr.append(line+"\n");
    } while (!line.isNull());
     file.close();



    if (!file.open(QIODevice::WriteOnly)) {
        QMessageBox::information(this, tr("Unable to open file"),
                                 file.errorString());
        return;
    }

     file.write(bArr);

     file.close();





}


bool SimulationInput::load(const QString &f)
{

    edit_mac_file();

    if (!QFile::exists(f))
        return false;

    QFile file(f);
    if (!file.open(QFile::ReadOnly))
        return false;

    QByteArray ba= file.readAll();
    QTextCodec *codec = Qt::codecForHtml(ba);
    QString str = codec->toUnicode(ba);
    if (Qt::mightBeRichText(str)) {
        ui->editor->setHtml(str);
    } else {
        str = QString::fromLocal8Bit(ba);
        ui->editor->setPlainText(str);
    }

    file.close();
    setCurrentFileName(f);
    ui->LE_input->setText(f);
    return true;
}



void SimulationInput::setCurrentFileName(const QString &fileName)
{
    inputFilename = fileName;
    ui->editor->document()->setModified(false);

    QString shownName;
    if (fileName.isEmpty())
        shownName = "untitled.txt";
    else
        shownName = QFileInfo(fileName).fileName();

    setWindowTitle(tr("%1[*] - %2").arg(shownName).arg(tr("Rich Text")));
    setWindowModified(false);
}

void SimulationInput::fileSave()
{


    if (!filename.isNull())
        {
            QFile file(filename);
            file.open(QIODevice::WriteOnly);

            QByteArray outputByteArray;
            outputByteArray.append(ui->editor->toPlainText().toUtf8());
            file.write(outputByteArray);
            file.close();

            //fileName = outputFileName;
        }



}



void SimulationInput::next()
{
    if(simulatuion==NULL)
    {
        simulatuion = new RunSimulation(this,filename);
        simulatuion->show();
        connect(simulatuion,SIGNAL(closeProgram()),this,SIGNAL(closeEverything()));
        ui->LE_input->clear();
    }
}
