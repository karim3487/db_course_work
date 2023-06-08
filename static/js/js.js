var currentTab = 0;
var appInfo = {}
document.addEventListener("DOMContentLoaded", function (event) {
    showTab(currentTab);


    var doctorElements = document.querySelectorAll('.doctor');
    var doctors = Array.from(doctorElements).map(function (element) {
        return element.dataset.doctorId;
    });
    doctors.forEach(function (doctorId) {
        var $selectDate = $('#select-date-' + doctorId),
            $selectTalon = $('#select-talon-' + doctorId),
            $options = $selectTalon.find('option');

        $selectDate.on('change', function () {
            $selectTalon.html($options.filter('[value="' + this.value + '"]'));
            appInfo['date'] = this.value;
            console.log(appInfo)
        }).trigger('change');

        $selectTalon.on('change', function () {
            appInfo['time'] = $("#select-talon-" + doctorId + " option:selected").text().split(",")[0].trim();
            console.log(appInfo)
        }).trigger('change');
    });

    $('#regForm').submit(function (event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию

        var form = $(this);
        var url = form.attr('action');
        var method = form.attr('method');
        var formData = form.serialize();

        console.log(formData)

        for (var key in appInfo) {
            if (appInfo.hasOwnProperty(key)) {
                formData += "&" + key + "=" + appInfo[key]
            }
        }
        console.log(formData)

        var xhr = new XMLHttpRequest();
        xhr.open(method, url, true);
        xhr.onload = function () {
            if (xhr.status === 200) {
                console.log(xhr.responseText);
            } else {
                console.error(xhr.responseText);
            }
        };
        xhr.onerror = function () {
            console.error(xhr.responseText);
        };
        xhr.send(formData);
    });
})

function showTab(n) {
    var x = document.getElementsByClassName("tab");
    x[n].style.display = "block";
    fixStepIndicator(n)
}

function nextPrev(n) {
    var x = document.getElementsByClassName("tab");
    if (n === 1) return false;
    document.getElementsByClassName("step")[currentTab].className += " finish";
    x[currentTab].style.display = "none";
    currentTab = currentTab + n;
    showTab(currentTab);
}

function selectSpecialty(specialtyId, specialtyName) {
    var x = document.getElementsByClassName("tab");
    var doctors = document.getElementsByClassName("doctor");


    for (var i = 0; i < doctors.length; i++) {
        var specId = doctors[i].getAttribute("spec_id");
        console.log(specId === specialtyId.toString())
        if (specId === specialtyId.toString()) {
            doctors[i].style.display = "";
        } else {
            doctors[i].style.display = "none";
        }
    }
    setSelectSpecName(specialtyName);

    document.getElementsByClassName("step")[currentTab].className += " finish";
    x[currentTab].style.display = "none";
    currentTab = currentTab + 1;
    showTab(currentTab);
}

function showPatient() {
    var x = document.getElementsByClassName("tab");

    document.getElementsByClassName("step")[currentTab].className += " finish";
    x[currentTab].style.display = "none";
    currentTab = currentTab + 1;
    showTab(currentTab);
}

function toggleFooter(button, docId) {
    var cardFooter = button.closest(".card").querySelector(".card-footer");
    cardFooter.classList.toggle("d-none");
    appInfo['doc_id'] = docId
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
