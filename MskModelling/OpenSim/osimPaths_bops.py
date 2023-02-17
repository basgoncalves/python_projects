
import os
import xml.etree.ElementTree as ET
import xmltodict
import json

fp = os.sep

def getosimPath(mainFolder):
    
    bopsXML_path = r'C:\Git\MSKmodelling\src\bops_tool\Templates\bopsSettings.xml'
    
    tree = ET.parse(bopsXML_path)
    xml_data = tree.getroot()
    Dir = ET.tostring(xml_data, encoding='utf-8', method='xml')

    # Dir = dict(xmltodict.parse(xmlstr))   
    
    # Dir.InputData           = os.path.join(mainFolder, 'InputData')
    # Dir.ElaboratedData      = os.path.join(mainFolder, 'ElaboratedData')
    return Dir
#     Dir.subjectInfoCSV      = [os.path.split(Dir.setupbopsXML) fp 'subjectinfo.csv'];
#     Dir.eventsCSV           = [os.path.split(Dir.setupbopsXML) fp 'events.csv'];
#     Dir.modelsCSV           = [os.path.split(Dir.setupbopsXML) fp 'Models.csv'];
#     Dir.CEINMSexe           = [masterDir fp 'src\Ceinms\CEINMS_2'];                                                     % add CEINMS 2 directory
#     Dir.InputData           = [mainFolder fp 'InputData'];
#     Dir.ElaboratedData      = [mainFolder fp 'ElaboratedData'];

#     Dir.Results = [mainFolder fp 'Results'];

#     templateDir                  = [dataDir fp 'templates'];
#     Dir.templatesDir             = templateDir;   
#     Dir.templates                = struct;                                                                              % Directory with template setup files for this project
#     Dir.templates.acquisitionXML = [templateDir fp 'acquisition.xml'];                                                  % MOtoNMS (see https://scfbm.biomedcentral.com/articles/10.1186/s13029-015-0044-4)
#     Dir.templates.elaborationXML = [templateDir fp 'elaboration.xml'];

#     Dir.templates.Model     = [templateDir fp bops.dataStructure.OSIMModelName '.osim'];                                %OpenSim
#     Dir.templates.ScaleTool = [templateDir fp 'ScaleTool.xml'];
#     Dir.templates.Static    = [templateDir fp 'static.xml'];

#     Dir.templates.IKSetup = [templateDir fp 'IK_setup.xml'];                                                            % Inverse kinematics

#     Dir.templates.IDSetup = [templateDir fp 'ID_setup.xml'];                                                            % Inverse dynamics
#     Dir.templates.GRF = [templateDir fp 'ID_externalForces_RL.xml'];

#     Dir.templates.RRASetup                      = [templateDir fp 'RRA_setup.xml'];                                     % residual reduction analysis
#     Dir.templates.RRAActuators                  = [templateDir fp 'RRA_actuators.xml'];   
#     Dir.templates.RRATaks                       = [templateDir fp 'RRA_tasks.xml'];
#     Dir.templates.RRASetup_actuation_analyze    = [templateDir fp 'RRA_setup_actuation_analyze.xml'];

#     Dir.templates.MASetup = [templateDir fp 'MA_setup.xml'];                                                            % muscle analysis

#     Dir.templates.SOSetup       = [templateDir fp 'SO_setup.xml'];                                                      % static optimization 
#     Dir.templates.SOActuators   = [templateDir fp 'SO_actuators.xml'];

#     Dir.templates.CMCSetup      = [templateDir fp 'CMC_setup.xml'];                                                     % computed muscle control
#     Dir.templates.CMCControls   = [templateDir fp 'CMC_ControlConstraints.xml'];
#     Dir.templates.CMCtasks      = [templateDir fp 'CMC_tasks.xml'];
#     Dir.templates.CMCactuators  = [templateDir fp 'CMC_actuators.xml'];

#     Dir.templates.CEINMSuncalibratedmodel = [templateDir fp 'CEINMS_uncalibrated_RL.xml'];                              % CEINMS templates
#     Dir.templates.CEINMScalibrationCfg = [templateDir fp 'CEINMS_calibrationCfg_RL.xml'];                                       
#     Dir.templates.CEINMScalibrationCfg_HJCF = [templateDir fp 'CEINMS_calibrationCfg_RL_HJCF.xml'];                                  
#     Dir.templates.CEINMSexcitationGenerator = [templateDir fp 'CEINMS_excitationGenerator.xml'];
#     Dir.templates.CEINMSexecutionSetup = [templateDir fp 'CEINMS_executionSetup.xml'];                                               
#     Dir.templates.CEINMSexecutionCfg = [templateDir fp 'CEINMS_executionCfg.xml'];                                                   
#     Dir.templates.CEINMScontactmodel = [templateDir fp 'CEINMS_contactOpenSimModel.xml'];                                            

#     Dir.templates.JRAsetup = [templateDir fp 'JCF_setup.xml'];                                                          % joint reaction analysis                                                     

#     Dir.templates.IAASetup = [templateDir fp 'IAA_setup.xml'];                                                          % induced acceleration analysis
                                                                                                        
#     bops.directories = Dir;
#     bops = ConvertLogicToString(bops);
#     if ~isequal(og_bopsSetup,bops)                                                                                      % save new xml if original bops is different from the new one
#     xml_write(Dir.setupbopsXML,bops,'bops',bops.xmlPref);
#     end
    
    
a = 2