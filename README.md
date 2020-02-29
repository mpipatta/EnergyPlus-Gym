# EnergyPlus-Gym

### This environment has been tested in Mac OS Catalina (by MP, v.10.15.2) and in Ubuntu 16.04 OS (by Zhiang Zhang).

This environment wraps EnergyPlus-v-8-7 (MP) and EnergyPlus-v-8-6 (Zhiang Zhang) into the OpenAI gym environment interface.

### Installation
1. Download EnergyPlus-v-8-7 (or EnergyPlus-v-8-6) from https://energyplus.net/downloads, extract it, and place it to the directory 
eplus_env/envs/EnergyPlus-8-7-0 (or eplus_env/envs/EnergyPlus-8-6-0). 

2. The environment already has BCVTB-1.6.0 (https://simulationresearch.lbl.gov/bcvtb). BCVTB-1.6.0 is compiled with Java-1.8. Make sure you have Java-1.8 on your OS. 

3. Start virtual environment

```
$ virtualenv virt_env --python=python3
$ source virt_env/bin/activate
$ pip install gym
```

### Configure EnergyPlus
Gym-Eplus is implemented based on EnergyPlus ExternalInterface function. The EnergyPlus model should be configured based on the guidelines here (https://simulationresearch.lbl.gov/bcvtb/releases/latest/doc/manual/tit-EnePluCon.xhtml).

1. Under ExternalInterface, add "Ptolemy" server as the name of external interface.

2. Under ExternalInterface:Schedule, add the name of your external control (e.g., ExternalControl1), type of control (e.g., Temperature) and initial value (e.g., 25)

3. To control thermostat set point, add the name of your external control to "ThermostatSetpoint:SingleCooling"


### Usage
1. Copy EnergyPlus IDF and weather files: 
* Copy the IDF file to '/eplus_env/envs/eplus_models/demo_5z/learning/idf/'
* Copy the EPW file to '/eplus_env/envs/weather/'

2. Edit The 'variables' file: 
The 'variables' file is located at '/eplus_env/envs/eplus_models/demo_5z/learning/cfg/'. Please specify the variables to be retrived from EnergyPlus, and the variables to be sent to EnergyPlus (e.g., external control).

3. Create a new environment: Create a new environment in '/eplus_env/__init__.py' file.  This file sets the paths to: EnergyPlus, weather file, BCVTB, variables, IDF file, and specify the environment name.


### To Run
See test.py
1. Make the environment, env = gym.make('environment name')
2. Reset the environment, env.reset()
3. Run the environment, env.step()
4. Save the data in a DataFrame
5. Close the environment, env.close()


### Reference: 
https://github.com/zhangzhizza/Gym-Eplus
