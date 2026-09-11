async function compressPDF() {

    const file =
        document.getElementById("pdf").files[0];

    if (!file) {
        alert("Select PDF");
        return;
    }

    const formData = new FormData();

    formData.append("file", file);

    const response = await fetch(
        "https://pdf-compressor-nn8p.onrender.com/compress",
        {
            method: "POST",
            body: formData
        }
    );

    const blob = await response.blob();

    const url =
        window.URL.createObjectURL(blob);

    const a =
        document.createElement("a");

    a.href = url;
    a.download = "compressed.pdf";

    a.click();
}