<h1 align='center'>FIT-5226</h1>

## Lab scripts for fit-5226: Multi agent systems and collective behaviour.  

## Preparation

### Create conda virtual-environment
```bash
conda env create -f environment.yml
```

## Project Structure
```
├── base_env: establish base env
    ├── base_agent: Construct Agent class.
    ├── base_grid: Construct Grid class.
├── labs: Lab tasks (python/jupyter file) per week
    ├── week2_lab.py: week2 lab tasks 
    ├── week3_lab.py: week3 lab tasks 
    ├── .....
└── environment.yml: file for build conda env
```

## Use extra envs in jupyter

For example: I create a conda-env named "fit5226", I want it to show the name "fit" in jupyter.  
Then run this follow code:
```bash
python -m ipykernel install --user --name fit5226 --display-name "fit"
```