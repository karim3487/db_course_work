var currentTab = 0;
document.addEventListener("DOMContentLoaded", function (event) {
    showTab(currentTab);
});

function showTab(n) {
    var x = document.getElementsByClassName("tab");
    x[n].style.display = "block";
    fixStepIndicator(n)
}

function nextPrev(n) {
    var x = document.getElementsByClassName("tab");
    if (n === 1 && !validateForm()) return false;
    x[currentTab].style.display = "none";
    currentTab = currentTab + n;
    if (currentTab >= x.length) {
        // document.getElementById("regForm").submit();
        // return false;
        //alert("sdf");
        document.getElementById("nextprevious").style.display = "none";
        document.getElementById("all-steps").style.display = "none";
        document.getElementById("register").style.display = "none";
        document.getElementById("text-message").style.display = "block";


    }
    showTab(currentTab);
}

function selectSpecialty(specialtyId, specialtyName) {
    var x = document.getElementsByClassName("tab");
    var doctors = document.getElementsByClassName("doctor");


    for (var i = 0; i < doctors.length; i++) {
        var specId = doctors[i].getAttribute("spec_id");
        console.log(specId === specialtyId.toString())
        if (specId === specialtyId.toString()) {
            doctors[i].style.display = ""; // Отображение строки
        } else {
            doctors[i].style.display = "none"; // Скрытие строки
        }
        setSelectSpecName(specialtyName);
    }

    document.getElementsByClassName("step")[currentTab].className += " finish";
    x[currentTab].style.display = "none";
    currentTab = currentTab + 1;
    showTab(currentTab);
}

function toggleFooter(button) {
  var cardFooter = button.closest(".card").querySelector(".card-footer");
  cardFooter.classList.toggle("d-none");
}

function validateForm() {
    var x, y, i, valid = true;
    x = document.getElementsByClassName("tab");
    y = x[currentTab].getElementsByTagName("input");
    for (i = 0; i < y.length; i++) {
        if (y[i].value === "") {
            y[i].className += " invalid";
            valid = false;
        }
    }
    if (valid) {
        document.getElementsByClassName("step")[currentTab].className += " finish";
    }
    return valid;
}

function fixStepIndicator(n) {
    var i, x = document.getElementsByClassName("step");
    for (i = 0; i < x.length; i++) {
        x[i].className = x[i].className.replace(" active", "");
    }
    x[n].className += " active";
}

function setSelectSpecName(specialtyName) {
    var container = document.getElementById("spec-name")
    container.innerHTML = specialtyName;
}
