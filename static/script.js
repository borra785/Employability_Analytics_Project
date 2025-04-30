function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
    localStorage.setItem("darkMode", document.body.classList.contains("dark-mode"));
}

// Load dark mode preference
window.onload = function() {
    if (localStorage.getItem("darkMode") === "true") {
        document.body.classList.add("dark-mode");
    }
};

function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
    localStorage.setItem("darkMode", document.body.classList.contains("dark-mode"));
}

window.onload = function() {
    if (localStorage.getItem("darkMode") === "true") {
        document.body.classList.add("dark-mode");
    }
    populateColumnFilter();
};

function searchTable() {
    let input = document.getElementById("searchInput").value.toLowerCase();
    let table = document.querySelector("table");
    let rows = table.getElementsByTagName("tr");
    
    for (let i = 1; i < rows.length; i++) {
        let cells = rows[i].getElementsByTagName("td");
        let match = false;
        for (let cell of cells) {
            if (cell.innerText.toLowerCase().includes(input)) {
                match = true;
                break;
            }
        }
        rows[i].style.display = match ? "" : "none";
    }
}

function populateColumnFilter() {
    let table = document.querySelector("table");
    let headers = table.getElementsByTagName("th");
    let columnFilter = document.getElementById("columnFilter");

    for (let i = 0; i < headers.length; i++) {
        let option = document.createElement("option");
        option.value = i;
        option.textContent = headers[i].innerText;
        columnFilter.appendChild(option);
    }
}

function filterTable() {
    let selectedColumn = document.getElementById("columnFilter").value;
    let table = document.querySelector("table");
    let rows = table.getElementsByTagName("tr");

    for (let i = 1; i < rows.length; i++) {
        let cells = rows[i].getElementsByTagName("td");
        for (let j = 0; j < cells.length; j++) {
            cells[j].style.display = (selectedColumn === "all" || j == selectedColumn) ? "" : "none";
        }
    }
}

function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
    localStorage.setItem("darkMode", document.body.classList.contains("dark-mode"));
}

window.onload = function() {
    if (localStorage.getItem("darkMode") === "true") {
        document.body.classList.add("dark-mode");
    }
    populateColumnFilter();
    makeTableSortable();
};

function searchTable() {
    let input = document.getElementById("searchInput").value.toLowerCase();
    let table = document.querySelector("table");
    let rows = table.getElementsByTagName("tr");

    for (let i = 1; i < rows.length; i++) {
        let cells = rows[i].getElementsByTagName("td");
        let match = false;
        for (let cell of cells) {
            if (cell.innerText.toLowerCase().includes(input)) {
                match = true;
                break;
            }
        }
        rows[i].style.display = match ? "" : "none";
    }
}

function populateColumnFilter() {
    let table = document.querySelector("table");
    let headers = table.getElementsByTagName("th");
    let columnFilter = document.getElementById("columnFilter");

    for (let i = 0; i < headers.length; i++) {
        let option = document.createElement("option");
        option.value = i;
        option.textContent = headers[i].innerText;
        columnFilter.appendChild(option);
    }
}

function filterTable() {
    let selectedColumn = document.getElementById("columnFilter").value;
    let table = document.querySelector("table");
    let rows = table.getElementsByTagName("tr");

    for (let i = 1; i < rows.length; i++) {
        let cells = rows[i].getElementsByTagName("td");
        for (let j = 0; j < cells.length; j++) {
            cells[j].style.display = (selectedColumn === "all" || j == selectedColumn) ? "" : "none";
        }
    }
}

function makeTableSortable() {
    let headers = document.querySelectorAll("th");
    headers.forEach((header, index) => {
        header.style.cursor = "pointer";
        header.addEventListener("click", () => sortTableByColumn(index));
    });
}

function sortTableByColumn(columnIndex) {
    let table = document.querySelector("table");
    let rows = Array.from(table.rows).slice(1);
    let ascending = table.getAttribute("data-sort-order") !== "asc";

    rows.sort((rowA, rowB) => {
        let cellA = rowA.cells[columnIndex].innerText.trim();
        let cellB = rowB.cells[columnIndex].innerText.trim();
        return ascending ? cellA.localeCompare(cellB) : cellB.localeCompare(cellA);
    });

    table.setAttribute("data-sort-order", ascending ? "asc" : "desc");

    rows.forEach(row => table.appendChild(row));
}

function downloadCSV() {
    let table = document.querySelector("table");
    let rows = Array.from(table.rows);
    let csvContent = rows.map(row => Array.from(row.cells).map(cell => `"${cell.innerText}"`).join(",")).join("\n");

    let blob = new Blob([csvContent], { type: "text/csv" });
    let link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "filtered_data.csv";
    link.click();
}
