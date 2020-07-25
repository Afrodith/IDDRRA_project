#----------------------------------------------------------------------------
# Setup the project
#
cmake_minimum_required(VERSION 2.6 FATAL_ERROR)
project(IDDRRA)


#----------------------------------------------------------------------------
# Find Geant4 package, activating all available UI and Vis drivers by default
# You can set WITH_GEANT4_UIVIS to OFF via the command line or ccmake/cmake-gui
# to build a batch mode only executable
#
option(WITH_GEANT4_UIVIS "Build example with Geant4 UI and Vis drivers" ON)
if(WITH_GEANT4_UIVIS)
  find_package(Geant4 REQUIRED ui_all vis_all)
else()
  find_package(Geant4 REQUIRED)
endif()

#find_package(ROOT REQUIRED)


#----------------------------------------------------------------------------
# Setup Geant4 include directories and compile definitions
# Setup include directory for this project
#
INCLUDE_DIRECTORIES(
  ${CMAKE_CURRENT_BINARY_DIR}
  ${CMAKE_CURRENT_SOURCE_DIR}
)

# Find includes in corresponding build directories
set(CMAKE_INCLUDE_CURRENT_DIR ON)
# Instruct CMake to run moc automatically when needed
set(CMAKE_AUTOMOC ON)
# Create code from a list of Qt designer ui files
set(CMAKE_AUTOUIC OFF)



include(${Geant4_USE_FILE})
#include(${ROOT_USE_FILE})
include_directories(${PROJECT_SOURCE_DIR}/include)
include_directories(${Geant4_INCLUDE_DIRS})
#include_directories(${ROOT_INCLUDE_DIRS})
#add_definitions(${ROOT_CXX_FLAGS})



#----------------------------------------------------------------------------


set(SOURCES
    src/ActionInitialization.cc
    src/CommandLineParser.cc
    src/DetectorConstruction.cc
    src/DetectorMessenger.cc
    src/EventAction.cc
    src/EventActionMessenger.cc
    src/PDBatom.cc
    src/PDBbarycenter.cc
    src/PDBlib.cc
    src/PDBmolecule.cc
    src/PDBresidue.cc
    src/PhysicsList.cc
    src/PrimaryGeneratorAction.cc
    src/RunAction.cc
    src/RunInitObserver.cc
    src/SteppingAction.cc
    src/Mainwindow.cpp
    src/RunSimulation.cpp
    src/SimulationInput.cpp
    src/SimulationAnalysis.cpp
    src/execSimulation.cpp
    main.cc
    )

set(MOC
    include/ActionInitialization.hh
    include/CommandLineParser.hh
    include/DetectorConstruction.hh
    include/DetectorMessenger.hh
    include/EventAction.hh
    include/EventActionMessenger.hh
    include/PDBatom.hh
    include/PDBbarycenter.hh
    include/PDBlib.hh
    include/PDBmolecule.hh
    include/PDBresidue.hh
    include/PhysicsList.hh
    include/PrimaryGeneratorAction.hh
    include/RunAction.hh
    include/RunInitObserver.hh
    include/SteppingAction.hh
    include/Mainwindow.h
    include/RunSimulation.h
    include/SimulationInput.h
    include/SimulationAnalysis.h
    include/execSimulation.h
    )

set(UI
    ui/Mainwindow.ui
    ui/RunSimulation.ui
    ui/SimulationInput.ui
    ui/SimulationAnalysis.ui

    )

set(RCC
    icons/icons.qrc
    )

find_package(Qt5 REQUIRED COMPONENTS Core Gui)
find_package(Qt5 COMPONENTS Widgets REQUIRED)
get_target_property(QtCore_location Qt5::Core LOCATION)
get_target_property(QtGui_location Qt5::Gui LOCATION)


find_package(Qt5Widgets)
get_target_property(QtWidgets_location Qt5::Widgets LOCATION)

find_package(Qt5PrintSupport)
get_target_property(QtPrintSupport_location Qt5::PrintSupport LOCATION)


qt5_wrap_cpp(MOC_GENERATED ${MOC})
qt5_wrap_ui(UI_GENERATED ${UI})
qt5_add_resources(RCC_GENERATED ${RCC})

source_group("Form Files" FILES ${UI} )
source_group("Resource Files" FILES ${RCC} )
source_group("Generated Files" FILES ${MOC_GENERATED}   ${UI_GENERATED}  ${RCC_GENERATED} )



INCLUDE_DIRECTORIES( /usr/include/x86_64-linux-gnu/qt5/QtWidgets
     /usr/include/x86_64-linux-gnu/qt5/QtCore
    /usr/include/x86_64-linux-gnu/qt5/QtGui
    /usr/include/x86_64-linux-gnu/qt5/QtPrintSupport
    ${CMAKE_BINARY_DIR})



#----------------------------------------------------------------------------
# Add the executable, and link it to the Geant4 libraries
#
add_executable(IDDRRA  ${SOURCES}
    ${MOC_GENERATED}   ${UI_GENERATED}  ${RCC_GENERATED} )
target_link_libraries(IDDRRA ${Geant4_LIBRARIES} #${ROOT_LIBRARIES}
         Qt5::Widgets
         Qt5::PrintSupport
         Qt5::Gui
         )

#----------------------------------------------------------------------------
# Copy all scripts to the build directory, i.e. the directory in which we
# build pdb4dna. This is so that we can run the executable directly because
# it relies on these scripts being in the current working directory.
#
set(IDDRRA_SCRIPTS

  python/dnaPython.pdb
  Simulation_input/electronSpect.dat
  Simulation_input/init.mac
  Simulation_input/init_vis.mac
  Simulation_input/vis.mac

  )

foreach(plugin ${Qt5GUI_PLUGINS} ${Qt5Widgets_PLUGINS} ${Qt5PrintSuppport_PLUGINS})
  get_target_property(_loc ${plugin} LOCATION)
  message("Plugin ${plugin} is at location ${_loc}")
endforeach()

foreach(_script ${IDDRRA_SCRIPTS})
  configure_file(
    ${PROJECT_SOURCE_DIR}/${_script}
    ${PROJECT_BINARY_DIR}/${_script}
    COPYONLY
    )
endforeach()

#----------------------------------------------------------------------------
# Install the executable to 'bin' directory under CMAKE_INSTALL_PREFIX
#
install(TARGETS IDDRRA DESTINATION bin)
