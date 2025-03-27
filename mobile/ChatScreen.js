import React, { useState } from "react";
import { View, Text, TextInput, Button, ScrollView } from "react-native";
import axios from "axios";

const ChatScreen = () => {
    const [pregunta, setPregunta] = useState("");
    const [respuesta, setRespuesta] = useState("");

    const handleAsk = async () => {
        const response = await axios.post("http://127.0.0.1:8000/chatbot/", { pregunta });
        setRespuesta(response.data.respuesta);
    };

    return (
        <ScrollView>
            <Text>Chatbot Legal</Text>
            <TextInput value={pregunta} onChangeText={setPregunta} />
            <Button title="Consultar" onPress={handleAsk} />
            <Text>{respuesta}</Text>
        </ScrollView>
    );
};

export default ChatScreen;
