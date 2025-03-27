const handlePago = async () => {
    const response = await fetch("http://127.0.0.1:8000/api/crear-pago", { method: "POST" });
    const data = await response.json();
    window.location.href = data.url;
};
