document.addEventListener("DOMContentLoaded", function () {
  var sidebar = document.getElementById("sidebar");

  document.addEventListener("mousemove", function (event) {
    var x = event.clientX;

    if (x <= 10) {
      sidebar.style.left = "0"; // Show sidebar
    } else {
      sidebar.style.left = "-250px"; // Hide sidebar
    }
  });
});
