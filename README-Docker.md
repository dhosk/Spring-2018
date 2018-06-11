# Docker installation instructions

## (Docker) System requirements
- Newer Mac: Apple Mac OS Yosemite 10.10.3 or above
- Newer PC: Microsoft Windows 10 Professional or Enterprise 64-bit 
- Older system refers to any other Mac or PC

## (Docker) Download
- Newer PC: https://store.docker.com/editions/community/docker-ce-desktop-windows
- Newer Mac: https://store.docker.com/editions/community/docker-ce-desktop-mac
- On older systems that do not meet requirements: https://docs.docker.com/toolbox/overview/

## (Docker) Installation

### Newer system
  - Mac instructions: https://docs.docker.com/docker-for-mac/install/
  - Windows instructions: https://docs.docker.com/docker-for-windows/install/   

### Older system
- Docker Toolbox installation:
  - Mac instructions: https://docs.docker.com/toolbox/toolbox_install_mac/
  - Windows instructions: https://docs.docker.com/toolbox/toolbox_install_windows/
  
# Running course docker image

## Running the image

- Open a command line window (on windows, launch cmd as an __administrator__)

- Pull the notebook image: `docker pull syoh/pstat-134-234`

- Determine the location where you would like to save your notebook files:   
  Mac: go to the target directory (using `cd`) and type `pwd`. Note this location  
  PC: go to the target directory and note the location
  
- Run the image with some variation of the following command:  
  `docker run -p 8888:8888 -v [target location]:/home/jovyan syoh/pstat-134-234

- Note the last few lines that give the token for the notebook: e.g.  
  ```
  ...
  [I 11:59:16.597 NotebookApp] The Jupyter Notebook is running at:  
  http://localhost:8888/?token=c8de56fa4deed24899803e93c227592aef6538f93025fe01   
  ...
  ```
- Using your browser, navigate to `http://localhost:8888/?token=[your token]`: e.g.   
  `http://localhost:8888/?token=c8de56fa4deed24899803e93c227592aef6538f93025fe01`   
