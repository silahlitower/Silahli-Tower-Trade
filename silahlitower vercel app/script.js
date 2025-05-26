function searchData() {
    let searchTerm = document.getElementById("searchInput").value;
    let resultDiv = document.getElementById("searchResults");

    if (searchTerm.length > 0) {
        resultDiv.innerHTML = `<p><strong>${searchTerm}</strong> için veri aranıyor...</p>`;
    } else {
        resultDiv.innerHTML = `<p>Lütfen aramak istediğiniz firma veya ürünü yazın.</p>`;
    }
}