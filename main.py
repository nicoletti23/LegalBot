from fastapi import FastAPI
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = FastAPI()

# Configurar DeepSeek LLM
modelo_id = "deepseek-ai/deepseek-coder-6.7b"
tokenizer = AutoTokenizer.from_pretrained(modelo_id)
modelo = AutoModelForCausalLM.from_pretrained(modelo_id, torch_dtype=torch.float16, device_map="auto")

@app.post("/chatbot/")
async def chatbot(pregunta: str):
    prompt = f"Consulta legal en Colombia: {pregunta}"
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")
    output = modelo.generate(**inputs, max_length=200)
    respuesta = tokenizer.decode(output[0], skip_special_tokens=True)
    return {"respuesta": respuesta}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
