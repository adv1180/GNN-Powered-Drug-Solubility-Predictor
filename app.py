from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import torch
from model import GCN
from utils import smiles_to_data, get_compound_name_from_smiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = GCN(num_node_features=6, hidden_channels=64).to(device)
model.load_state_dict(torch.load("gcn_esol_model.pt", map_location=device))
model.eval()

@app.get("/", response_class=HTMLResponse)
def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "prediction": None})

@app.post("/", response_class=HTMLResponse)
def form_post(request: Request, smiles: str = Form(...)):
    compound_name = get_compound_name_from_smiles(smiles)

    data = smiles_to_data(smiles)
    if data is None:
        prediction = "❌ Invalid SMILES string."
    else:
        data = data.to(device)
        data.batch = torch.zeros(data.x.size(0), dtype=torch.long).to(device)
        with torch.no_grad():
            pred = model(data.x, data.edge_index, data.batch).item()
        prediction = round(pred, 4)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "prediction": prediction,
        "compound_name": compound_name,
        "smiles": smiles
    })