async function uploadPDF() {
    const fileInput = document.getElementById("pdf-file");
    const file = fileInput.files[0];

    if (!file) {
        document.getElementById("status").innerText = "Please select a file.";
        return;
    }

    const formData = new FormData();
    formData.append("pdf", file);

    document.getElementById("status").innerText = "Processing...";

    try {
        const response = await fetch("http://127.0.0.1:5000/upload", {
            method: "POST",
            body: formData,
        });

        if (response.ok) {
            document.getElementById("status").innerText = "Playing audiobook...";
        } else {
            const errorText = await response.text();
            document.getElementById("status").innerText = `Error: ${errorText}`;
        }
    } catch (error) {
        document.getElementById("status").innerText = `Error: ${error.message}`;
    }
}