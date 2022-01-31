# OC_P7
Creating algorithms to solve knapsack problem

## Installation
Clone repositery using : 
```bash
git clone https://github.com/AlexandreDuthil/OC_P7.git
```
Move to the project directory using : 
```bash
cd OC_P7
```
Create virtual environment in root folder of project :
```bash
python3 -m venv env
```
Activate virtual environment
```bash
source ./env/bin/activate
```
Install dependencies :
```bash
pip install -r requirements.txt
```

## Usage
Execute python script with a filename, a wallet size and an algorithm type ( by default wallet=500 et algorithm_type=brute )
```bash
python3 main.py "filename" --wallet=500 --algorithm_type="brute"
```
