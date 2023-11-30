document.getElementById("qr_from").addEventListener("submit", handleClick);

function handleClick(event) {
  event.preventDefault();
  var data = document.getElementById("data").value;
  get_qr(data);
  document.getElementById("submit").disabled = true;
}
function get_qr(data) {
  var url =
    "https://api.qrserver.com/v1/create-qr-code/?data=" +
    data +
    "&size=200x200";

  var options = {
    method: "GET",
  };

  fetch(url, options)
    .then(function (response) {
      if (response.status == 200) {
        var qr_img = document.createElement("img");
        qr_img.src = url;
        qr_img.id = "qr_code";
        var src = document.getElementById("qr_img");
        src.appendChild(qr_img);
        console.log("worked");
      }
    })
    .catch(function (error) {
      console.log(error);
    });
}

function deleteImg() {
  var img = document.getElementById("qr_code");
  img.remove();
  document.getElementById("submit").disabled = false;
}

function toggle() {
  var element = document.getElementById("help");
  var hidden = element.getAttribute("hidden");

  if (hidden) {
    element.removeAttribute("hidden");
  } else {
    element.setAttribute("hidden", "hidden");
  }
}
