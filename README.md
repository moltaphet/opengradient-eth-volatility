# 🚀 OpenGradient AI Workflow: ETH/USD Volatility Prediction

This repository contains the complete implementation and deployment scripts for an automated AI workflow running on the **OpenGradient Alpha Testnet**.

## 📝 Project Overview

The goal of this project is to provide decentralized, on-chain predictions for **ETH/USD volatility**. The workflow leverages historical market data and executes automated inferences to bridge AI intelligence with blockchain technology.

### 🔍 Technical Specifications

* **Workflow Type:** ETH Volatility Analysis.
* **Input Data:** 10 candles of 30-minute OHLC (Open, High, Low, Close) data.
* **Execution Frequency:** Automated every 3600 seconds (1 hour).
* **Network:** OpenGradient Alpha Testnet.
* **Contract Address:** `0x6c0C8A85e737e95d913B78cd5270b8fC59b5bC61`

---

## ⚠️ Important: Security Configuration

Before running the scripts, you **must** update the Private Key to your own Alpha Testnet wallet key.

1. Open `run_alpha.py` or `test_alpha.py`.
2. Locate the following line:
```python
PK = "YOUR_PRIVATE_KEY_HERE"

```


3. Replace `"YOUR_PRIVATE_KEY_HERE"` with your actual Private Key.

> **Note:** Never commit your real Private Key to GitHub. It is recommended to use environment variables for better security.

---

## 🛠 Getting Started

### 1. Prerequisites

* Python 3.10 or higher.
* An OpenGradient account and Alpha Testnet tokens.
* OpenGradient SDK installed.

### 2. Installation & Setup

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/moltaphet/opengradient-eth-volatility.git
cd opengradient-eth-volatility
python3 -m venv venv
source venv/bin/activate
pip install opengradient==0.1.0rc9

```

### 3. Deployment

To deploy the workflow to the Alpha Testnet, use the `run_alpha.py` script:

```bash
python3 run_alpha.py

```

### 4. Testing Inferences

To verify that the model is calculating and providing outputs on-chain, run the test script:

```bash
python3 test_alpha.py

```

---

## 📂 Repository Structure

* `run_alpha.py`: The main deployment script using OpenGradient SDK.
* `test_alpha.py`: A utility script to trigger and fetch manual inferences.
* `.gitignore`: Configured to exclude environment files and sensitive data.

---

## 👤 Verification

The successful deployment of this workflow can be verified on the OpenGradient Alpha Explorer using the contract address: `0x6c0C8A85e737e95d913B78cd5270b8fC59b5bC61`.

---