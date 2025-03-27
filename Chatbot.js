import React, { useState } from "react";
import axios from "axios";

const Chatbot = () => {
    const [pregunta, setPregunta] = useState("");
    const [respuesta, setRespuesta] = useState("");

    const handleAsk = async () => {
        const response = await axios.post("http://127.0.0.1:8000/chatbot/", { pregunta });
        setRespuesta(response.data.respuesta);
    };

    return (
        <div>
            <h2>Chatbot Legal</h2>
            <input type="text" value={pregunta} onChange={(e) => setPregunta(e.target.value)} />
            <button onClick={handleAsk}>Consultar</button>
            <p>{respuesta}</p>
        </div>
    );
};

export default Chatbot;
