const button = document.getElementById("file_upload"),
    headerFileName = document.getElementById("filename"),
    input = document.getElementById("fileID"),
    loader = document.getElementById("loader");

function onButtonClick() {
    input.click();
};

input.addEventListener("change", function (e) {
    var fileName = e.target.files[0].name;
    let filedata = `<h4>${fileName}</h4>`;
    headerFileName.innerHTML = filedata;
});


function showLoader() {
    document.querySelectorAll('button').forEach(elem => {
        elem.disabled = true;
    });
    loader.hidden = false;
    return false;
}
