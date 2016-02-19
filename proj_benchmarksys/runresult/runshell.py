
import commands
import os
import subprocess

sum_list=[]
def shellrun(target_simulator, target_binary, golden_simulator, golden_binary, caselist, rundate):
    output="/slowfs/hs_scr1/ytan/pysig_output/"+"run_1/"
    input_cct="/slowfs/hs_scr1/ytan/fsim_testing/project/hspice/bsim3_testing/first-round/to_reg1/"+"input_pysig.sp"
    list1="/slowfs/hs_scr1/ytan/fsim_testing/project/hspice/bsim3_testing/first-round/to_reg1/"+"case_pysig.list"
    atom_reg="/slowfs/fs_model3/yjxu/atom_2015.01/bin/atom_reg "
    case_root="/slowfs/hs_scr1/ytan/fsim_testing/project/hspice/bsim3_testing/first-round/to_reg1/hsp_reg/ "
    host_file="/remote/us01home30/ytan/HOSTS_SH "

    if target_binary=="default":
        if target_simulator=="FineSim":
            target="/u/fsimmgr/finesim_integ/main/Images/"+rundate+"/Testing/bin/finesim"
        else:    
            target="/u/hspmgr/QA_dirs/main/backup/"+rundate+"/star_hspice/VERILOGA_HOME/bin/hspice"
    else:
        target=target_binary

    if golden_binary=="default":
        if golden_simulator=="FineSim":
            golden="/u/fsimmgr/finesim_integ/main/Images/"+rundate+"/Testing/bin/finesim"
        else:    
            golden="/u/hspmgr/QA_dirs/main/backup/"+rundate+"/star_hspice/VERILOGA_HOME/bin/hspice"
    else:       
        golden=golden_binary

    runshell=open("/slowfs/hs_scr1/ytan/pysig_output/run.sh",'w')
    runshell.write("#/bin/sh -x \n")
    if (target_simulator=="FineSim"):
        runshell.write("setenv FINESIM_EXEC "+target+"\n")
    else:    
        runshell.write("setenv HSPICE_EXEC "+target+"\n")
    if (golden_simulator=="FineSim"):
        runshell.write("setenv FINESIM_EXEC "+golden+"\n")
    else:    
        runshell.write("setenv HSPICE_EXEC "+golden+"\n")
    commands.getstatusoutput("mkdir "+output)     
    runshell.write(atom_reg+" -cct " +input_cct+" -case_root "+case_root+" -case_list "+list1+" -output "+output+" -host "+host_file)
    runshell.write(" > "+output+"run.log \n")
    #commands.getstatusoutput("sh -x /slowfs/hs_scr1/ytan/pysig_output/run.sh")     
    #os.system("sh -x /slowfs/hs_scr1/ytan/pysig_output/run.sh")     
    subprocess.Popen("sh -x /slowfs/hs_scr1/ytan/pysig_output/run.sh", shell=True)
    sum_list.append(output+"summary/"+"case_pysig.list.acc")
    sum_list.append(output+"summary/"+"case_pysig.list.meas")
    return sum_list


        

        
    
