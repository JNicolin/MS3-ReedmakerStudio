document.addEventListener("DOMContentLoaded", function () {
    const selects = document.querySelectorAll("form select");
    selects.forEach(select => {
      select.addEventListener("change", function () {
        this.form.submit();
      });
    });
  });