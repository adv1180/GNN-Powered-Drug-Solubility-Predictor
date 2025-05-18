# 🧬 GNN Drug Solubility Predictor

**Predict water solubility (log mol/L) of molecules using a Graph Neural Network (GNN) model.**  
Users can input a SMILES string or draw a molecule using an interactive editor powered by [Kekule.js](https://partridgejiang.github.io/Kekule.js/).

![Kekule.js Molecule Editor](https://partridgejiang.github.io/Kekule.js/documents/tutorial/_images/composerUI.png)

---

## 🚀 Features

- 🔬 GNN-based solubility prediction trained on molecular graph data.
- ✍️ Interactive molecule drawing with Kekule.js.
- ⚡ FastAPI backend for efficient predictions.
- 🌐 User-friendly web interface with real-time feedback.
- 🧪 Compound name resolution from SMILES inputs.

---

## 🖼️ Screenshots

### Molecule Drawing Panel

![Drawing Panel](https://partridgejiang.github.io/Kekule.js/documents/tutorial/_images/composerUI.png)

---

## 🛠️ Installation Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/gnn-drug-solubility-predictor.git
cd gnn-drug-solubility-predictor
```

### Step 2: Create and Activate Virtual Environment

```bash
python -m venv drug_gnn_venv
source drug_gnn_venv/bin/activate   # On Windows: drug_gnn_venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, install manually:

```bash
pip install fastapi uvicorn torch torchvision torchaudio rdkit-pypi torch-geometric jinja2 requests
```

**Important:** Use a safe version of NumPy to avoid RDKit issues:

```bash
pip install numpy==1.24.4
```

---

## ▶️ Running the App

```bash
uvicorn main:app --reload --port 8001
```

Visit: [http://localhost:8001](http://localhost:8001)

---

## 🧪 Usage

### Option 1: Enter SMILES String

- Input a valid SMILES like `CCO`
- Click “🔮 Predict”

### Option 2: Draw Molecule

- Use Kekule.js panel to draw atoms and bonds
- Click “🧪 Use Drawing” → auto-converts to SMILES
- Click “🔮 Predict”

---


## 

- [Kekule.js](https://partridgejiang.github.io/Kekule.js/)
- [RDKit](https://www.rdkit.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/)
