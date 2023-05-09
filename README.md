#### bynder-demo

### 1. Fork this repo

After forking this project in `Github`, run these commands:

```bash
## clone this repo to a local directory
git clone https://github.com/sikhwalanil2/Bynder.git

```

### 2. Install required packages
```bash
## install the node_modules
pip install -r requirements.txt

```
### 3. Run Test Suite

```bash
## Run Test on local with headless  mode
pytest --html=report.html
<img width="1334" alt="image" src="https://user-images.githubusercontent.com/47314061/191962490-e8a1351c-c4dd-4fc3-b476-7bba9526c36c.png">


## Run Test on local with docker
npm run docker-test
<img width="1335" alt="image" src="https://user-images.githubusercontent.com/47314061/191962638-bbbd32b5-912f-4fe4-9d7e-53c73da3c82f.png">

```
### 4. Deal with Test runner
```bash
## launch the cypress test runner
npm run cy:open
<img width="1693" alt="image" src="https://user-images.githubusercontent.com/47314061/191962742-7a43cb60-e921-4b52-82e2-578719b4d45f.png">

```
