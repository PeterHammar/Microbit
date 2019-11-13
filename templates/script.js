$(function () {
    getSessionCount();
    getStorageCount();


    $("#btnSession").click(function() {
        var count = getSessionCount();
        count++;
        setSessionCount(count);
        getSessionCount();
    });
    
    $("#btnStorage").click(function () {
        var count = getStorageCount();
        count++;
        setStorageCount(count);
        getStorageCount();
    });
});

function getSessionCount() {
    var count = 0;
    if (sessionStorage) {
        count = sessionStorage.getItem("ss_count");
        count = !count ? 0 : count * 1;                    
    }
    $("#txtSession").val(count);
    return count;
}
function setSessionCount(count) {
    if (sessionStorage)
        sessionStorage.setItem("ss_count", count.toString());
}
function getStorageCount() {
    var count = 0;
    if (localStorage) {
        count = localStorage.getItem("ls_count");
        count = !count ? count = 0 : count * 1;
    }
    $("#txtStorage").val(count);
    return count;
}
function setStorageCount(count) {
    if (localStorage)
        localStorage.setItem("ls_count", count);
}      